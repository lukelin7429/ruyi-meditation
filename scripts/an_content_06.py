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


# --------------------------------------------------------------------------- #
# Chapter 4 — Devatāvagga (AN 6.31–42)
# --------------------------------------------------------------------------- #
VAGGA_4 = "<em>Devatāvagga</em> &mdash; the fourth chapter of the Sixes"


# --------------------------------------------------------------------------- #
# AN 6.31 — Sekhasutta
# --------------------------------------------------------------------------- #
page(
    31, "Sekha", "A Trainee",
    vagga=VAGGA_4,
    meta_title="AN 6.31 — A Trainee | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sekhasutta, opening "
        "the Sixes' fourth chapter with six things that lead a trainee mendicant to decline, "
        "and their six opposites. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, in a single short "
                 "discourse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This theme of decline versus non-decline for a trainee recurs "
                              "across the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, opening "
                       "a chapter that will return to this decline theme repeatedly"),
    ],
    why=(
        "The chapter titled &lsquo;Deities&rsquo; opens, somewhat unexpectedly, with no deity "
        "at all: a bare six-item list of what causes a <em>sekha</em>, a trainee, to decline, "
        "paired immediately with its six-item reversal. The deities the chapter is named for "
        "arrive at the very next discourse, AN 6.32, which restates closely related material "
        "through a nighttime visitor."),
    guide=[
        ("The teaching in one sentence", [
            "A trainee mendicant declines by relishing work, talk, sleep, and company, failing "
            "to guard the sense doors, and eating too much; they avoid decline by the six direct "
            "opposites of these."]),
        ("A specific target: the trainee, not every mendicant", [
            "Unlike AN 6.21's causes of decline, stated for &ldquo;a mendicant&rdquo; generally, "
            "this discourse specifies <em>sekhassa bhikkhuno</em>, a trainee mendicant &mdash; "
            "someone who has entered the path (the same term defined at AN 5.1's reading guide "
            "earlier in this series) but not yet completed it. The list may be aimed "
            "specifically at this population because a trainee, unlike an arahant, still has "
            "something at stake in these six habits."]),
        ("Four familiar items, two new ones", [
            "Work, talk, sleep, and company repeat the trio-plus-one already met at AN 6.14, "
            "6.15, 6.17, and 6.21. The two new items &mdash; not guarding the sense doors "
            "(<em>indriyesu aguttadvāratā</em>) and eating without moderation "
            "(<em>bhojane amattaññutā</em>) &mdash; extend the pattern from social and "
            "attentional habits to the specific discipline of sense-restraint and eating, both "
            "recurring elsewhere in the canon's standard descriptions of a well-trained "
            "mendicant's daily conduct."]),
        ("Compression as the discourse's whole method", [
            "Nothing here is elaborated: no story, no closing verse, no explanation of why any "
            "one item matters. The entire discourse is the bare naming of six causes and six "
            "reversals, back to back, trusting the reader to recognize each item from its "
            "appearance elsewhere or its self-evident sense."]),
        ("Opening a chapter that returns to this theme", [
            "AN 6.31 is the first of several discourses in this chapter concerned with what "
            "preserves or undermines a mendicant's practice &mdash; AN 6.32 and 6.33 restate "
            "closely related six-item lists via a deity's report, and AN 6.40, later in the "
            "chapter, asks the same question of the entire teaching's long-term survival rather "
            "than one mendicant's progress."]),
    ],
    terms=[
        ("sekha",
         "&ldquo;trainee&rdquo; &mdash; one who has entered the path but not completed it, "
         "already defined at AN 5.1 earlier in this series."),
        ("indriyesu aguttadvāratā",
         "&ldquo;not guarding the sense doors&rdquo; &mdash; the fifth cause of decline, new to "
         "this discourse compared to AN 6.14/6.15/6.17/6.21."),
        ("bhojane amattaññutā",
         "&ldquo;not knowing moderation in eating&rdquo; &mdash; the sixth cause, likewise new "
         "to this discourse."),
        ("parihāna",
         "&ldquo;decline&rdquo; &mdash; unchanged from AN 6.21/6.22, now applied specifically "
         "to a trainee."),
        ("aparihāna",
         "&ldquo;non-decline&rdquo; &mdash; the direct reversal named in this discourse's "
         "second half."),
    ],
    text_intro=(
        "The discourse in full: six causes of a trainee's decline, and their six reversals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six causes of a trainee's decline"),
        ("p", "&sect;1", "an6.31:1.1-1.4"),
        ("h3", "Six causes of non-decline"),
        ("p", "&sect;2", "an6.31:2.1-2.4"),
    ],
    quiz=[
        {"q": "What population does this discourse specifically address, unlike AN 6.21?",
         "opts": [
             "Lay followers only",
             "A trainee mendicant (sekha) specifically, rather than mendicants in general",
             "Only fully awakened arahants",
             "Only senior mendicants"],
         "correct": 1,
         "expl": "Sekhassa bhikkhuno — someone who has entered the path but not completed it."},
        {"q": "Which four of the six causes of decline repeat items already met earlier in this "
              "chapter's predecessor?",
         "opts": [
             "Faith, energy, mindfulness, wisdom",
             "Work, talk, sleep, and company",
             "Danger, suffering, disease, boil",
             "Seeing, listening, acquisition, training"],
         "correct": 1,
         "expl": "Already met at AN 6.14, 6.15, 6.17, and 6.21."},
        {"q": "What two items are new to this discourse's list?",
         "opts": [
             "Faith and wisdom",
             "Not guarding the sense doors, and not knowing moderation in eating",
             "Generosity and ethics",
             "Seeing and hearing"],
         "correct": 1,
         "expl": "Extending the pattern into sense-restraint and eating discipline specifically."},
        {"q": "What is the discourse's entire method, according to the guide?",
         "opts": [
             "An extended narrative with multiple characters",
             "Bare naming of six causes and six reversals, with no story, closing verse, or "
             "explanation of any single item",
             "A detailed philosophical argument",
             "A dialogue between the Buddha and a deity"],
         "correct": 1,
         "expl": "Compression is the whole method — no elaboration is offered."},
        {"q": "How does this discourse set up the rest of the chapter, according to the guide?",
         "opts": [
             "It has no connection to what follows",
             "It opens a chapter that returns repeatedly to what preserves or undermines a "
             "mendicant's practice, including AN 6.32/6.33 and AN 6.40",
             "It is the only discourse in the chapter on this theme",
             "It directly contradicts AN 6.32's teaching"],
         "correct": 1,
         "expl": "A recurring concern across several discourses in this chapter."},
        {"q": "What does <em>indriyesu aguttadvāratā</em> mean?",
         "opts": [
             "Guarding the sense doors well",
             "Not guarding the sense doors",
             "Having five faculties",
             "Eating in moderation"],
         "correct": 1,
         "expl": "The fifth cause of decline, new to this discourse."},
        {"q": "Is a setting stated for AN 6.31?",
         "opts": ["Yes, at Rājagaha", "No — none is stated", "Yes, at Kimbilā", "Yes, at Icchānaṅgala"],
         "correct": 1,
         "expl": "A bare formula opening the chapter, despite its title 'Deities'."},
        {"q": "Why might this list target the trainee specifically, rather than every "
              "mendicant, according to the guide?",
         "opts": [
             "Because trainees are considered less capable overall",
             "Because a trainee, unlike an arahant, still has something at stake in these six "
             "habits — progress that could still be lost",
             "The guide offers no explanation for this",
             "Because only trainees are permitted to hear this teaching"],
         "correct": 1,
         "expl": "An arahant has nothing further to decline from in the relevant sense."},
        {"q": "What does <em>bhojane amattaññutā</em> mean?",
         "opts": [
             "Eating in moderation",
             "Not knowing moderation in eating",
             "Fasting entirely",
             "Sharing food with companions"],
         "correct": 1,
         "expl": "The sixth cause of decline, new to this discourse's list."},
        {"q": "What is notable about the chapter's title, 'Deities' (Devatāvagga), compared to "
              "its opening discourse?",
         "opts": [
             "AN 6.31 features an extended dialogue with a deity",
             "AN 6.31 has no deity at all — the deities the chapter is named for arrive at the "
             "very next discourse",
             "The chapter title is unrelated to any discourse within it",
             "Every discourse in the chapter features a deity"],
         "correct": 1,
         "expl": "A chapter title that describes its later content more than its opening."},
    ],
    marginalia=[
        ("Six causes of decline", [
            "work &middot; talk &middot; sleep",
            "company &middot; unguarded",
            "senses &middot; overeating",
        ]),
        ("New to this list", [
            "sense-door guarding",
            "and eating moderation —",
            "not met before this page",
        ]),
        ("Specifically the trainee", [
            "not every mendicant —",
            "the sekha still has",
            "something left to lose",
        ]),
        ("Cross-references", [
            "AN 6.21 &middot; the general version",
            "AN 6.32 &middot; next, a deity's version",
        ]),
    ],
    further=[
        '<a href="%s/an6.31/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.32.html">AN 6.32 &middot; Non-decline (1st)</a> &mdash; next, a deity '
        "reports a related six-item list.",
        '<a href="an-6.21.html">AN 6.21 &middot; At Sāma Village</a> &mdash; the earlier, '
        "general-mendicant version of this decline theme.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.32 — Paṭhamaaparihānasutta
# --------------------------------------------------------------------------- #
page(
    32, "Paṭhamaaparihāna", "Non-decline (1st)",
    vagga=VAGGA_4,
    meta_title="AN 6.32 — Non-decline (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamaaparihānasutta, "
        "in which a glorious deity lights up Jeta's Grove to report six kinds of respect that "
        "keep a mendicant from decline. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove — a deity's nighttime visit"),
        ("Speakers", "A deity, reporting to the Buddha; then the Buddha, in verse, to the "
                     "mendicants"),
        ("Form", "A deity's report, approved by the Buddha, followed by his own closing verse "
                 "restating the same six items"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Deity-visit narratives on non-decline recur across the Saṁyutta "
                              "and its Chinese counterparts; this reading guide does not assert "
                              "a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short narrative giving "
                       "the chapter its title"),
    ],
    why=(
        "This is the discourse that gives the &lsquo;Deities&rsquo; chapter its name: a "
        "glorious deity, lighting up the whole of Jeta's Grove, reports to the Buddha six "
        "things that keep a mendicant from decline &mdash; not habits to avoid, as in AN 6.31, "
        "but six kinds of respect to maintain. The Buddha approves, and the next morning "
        "restates the same six in verse to the assembled mendicants."),
    guide=[
        ("The teaching in one sentence", [
            "Respect for the Teacher, the teaching, the Saṅgha, the training, diligence, and "
            "hospitality keeps a mendicant from decline."]),
        ("A shift from habits to respect", [
            "AN 6.31's non-decline was about what a trainee does or doesn't do &mdash; relishing "
            "or not relishing work, talk, sleep, company, guarding the senses, moderate eating. "
            "This discourse's six items are all forms of <em>gārava</em>, respect or reverence, "
            "directed at six objects: the three refuges, the training, diligence itself, and "
            "hospitality. The register shifts from conduct to attitude."]),
        ("The same deity-narrative structure as AN 6.21", [
            "As at AN 6.21, a deity reports first, the Buddha approves without adding new "
            "content of his own beyond restating what was said, and the deity departs after "
            "circling the Buddha respectfully. Here, though, the Buddha's own addition the next "
            "morning is not new material but a verse restating the deity's own six items, "
            "closing with &ldquo;has drawn near to extinguishment&rdquo; &mdash; a stronger "
            "claim than merely avoiding decline."]),
        ("A pairing with AN 6.33 worth watching closely", [
            "AN 6.33, immediately following, restates a nearly identical scene &mdash; another "
            "glorious deity, another report of six things preventing decline, four of them "
            "identical (respect for the Teacher, the teaching, the Saṅgha, the training) &mdash; "
            "but its final two items differ from this discourse's diligence and hospitality. A "
            "reader should check the actual Pāli of both sixth items rather than assume the two "
            "discourses simply repeat each other."]),
        ("Why hospitality closes this particular list", [
            "<em>Paṭisanthāra</em>, hospitality or welcome, closing a list otherwise built from "
            "the three refuges, training, and diligence, extends respect outward from internal "
            "orientation toward how a mendicant treats those who arrive &mdash; fellow "
            "practitioners and visitors alike. It is a social virtue closing a list that is "
            "otherwise about inward orientation."]),
    ],
    terms=[
        ("gārava",
         "&ldquo;respect,&rdquo; &ldquo;reverence&rdquo; &mdash; the quality named six times "
         "over in this discourse, directed at six different objects."),
        ("sikkhāgārava",
         "&ldquo;respect for the training&rdquo; &mdash; the fourth of the six, respect for the "
         "mendicant's own discipline."),
        ("appamādagārava",
         "&ldquo;respect for diligence&rdquo; &mdash; the fifth, treating heedfulness itself as "
         "worthy of reverence, not merely a technique."),
        ("paṭisanthāragārava",
         "&ldquo;respect for hospitality&rdquo; &mdash; the sixth and closing item, extending "
         "respect toward how visitors and companions are received."),
        ("nibbānasseva santike",
         "&ldquo;drawn near to extinguishment&rdquo; &mdash; the Buddha's closing verse "
         "describes the mendicant with these six qualities in these terms, stronger than the "
         "deity's own claim of mere non-decline."),
    ],
    text_intro=(
        "The discourse in full: the deity's report, and the Buddha's closing verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A deity lights up Jeta's Grove"),
        ("p", "&sect;1", "an6.32:1.1-2.7"),
        ("h3", "The Buddha's closing verse"),
        ("p", "&sect;2", "an6.32:3.1-4.6"),
    ],
    quiz=[
        {"q": "What six things does the deity report as preventing a mendicant's decline?",
         "opts": [
             "Not relishing work, talk, sleep, and company; guarding the senses; eating in "
             "moderation",
             "Respect for the Teacher, the teaching, the Saṅgha, the training, diligence, and "
             "hospitality",
             "The five faculties plus liberation",
             "Danger, suffering, disease, boil, chain, bog"],
         "correct": 1,
         "expl": "Six forms of gārava, respect, directed at six different objects."},
        {"q": "How does this discourse's register differ from AN 6.31's, according to the "
              "guide?",
         "opts": [
             "They are identical in register",
             "A shift from conduct (habits to avoid) to attitude — respect directed at six "
             "objects, rather than actions to relish or avoid",
             "AN 6.32 concerns only lay followers",
             "AN 6.32 abandons the decline theme entirely"],
         "correct": 1,
         "expl": "Gārava, respect or reverence, replaces the earlier discourse's habit-focused "
                 "list."},
        {"q": "What structural parallel does this discourse share with AN 6.21?",
         "opts": [
             "No parallel at all",
             "A deity reports first, the Buddha approves, and departs respectfully — matching "
             "the earlier deity-narrative structure",
             "Both feature Mahākaccāna resolving a debate",
             "Both are set at Isipatana"],
         "correct": 1,
         "expl": "The same narrative shape as the chapter 3 opener, now giving this chapter its "
                 "title."},
        {"q": "What caution does the guide raise about AN 6.33, the next discourse?",
         "opts": [
             "That it should be skipped as a pure duplicate",
             "That while four of its six items match this discourse's, its final two differ — a "
             "reader should check the actual terms rather than assume simple repetition",
             "That AN 6.33 contradicts this discourse entirely",
             "That AN 6.33 is spoken by a different deity with no relation to this one"],
         "correct": 1,
         "expl": "A close but not identical companion, worth verifying directly."},
        {"q": "What does <em>paṭisanthāragārava</em> mean?",
         "opts": [
             "Respect for the training", "Respect for hospitality, extending outward toward how "
             "visitors are received", "Respect for diligence", "Respect for the Saṅgha"],
         "correct": 1,
         "expl": "The sixth and closing item, a social virtue closing an otherwise inward-facing "
                 "list."},
        {"q": "What claim does the Buddha's closing verse make, stronger than the deity's own "
              "report?",
         "opts": [
             "That the mendicant becomes famous",
             "That the mendicant with these six qualities has 'drawn near to extinguishment,' "
             "not merely avoided decline",
             "That the mendicant gains psychic powers",
             "That the mendicant will be reborn as a deity"],
         "correct": 1,
         "expl": "A stronger claim than the deity's original statement about non-decline alone."},
        {"q": "Where is AN 6.32 set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove — the site of the deity's nighttime visit",
             "Kimbilā, in the Freshwater Mangrove Wood",
             "Icchānaṅgala, in a forest"],
         "correct": 1,
         "expl": "A fresh, specific setting for this narrative discourse."},
        {"q": "What does <em>appamādagārava</em> mean?",
         "opts": [
             "Respect for hospitality",
             "Respect for diligence — treating heedfulness itself as worthy of reverence",
             "Respect for the teaching",
             "Respect for the Saṅgha"],
         "correct": 1,
         "expl": "The fifth of the six items in this discourse's list."},
        {"q": "What does the deity do after delivering the report?",
         "opts": [
             "Remains to debate with the Buddha",
             "Bows and respectfully circles the Buddha, keeping him on the right, before "
             "vanishing",
             "Asks the Buddha a further question",
             "Is rebuked by the Buddha for the report"],
         "correct": 1,
         "expl": "A standard formula for a deity's respectful departure, matching AN 6.21."},
        {"q": "What comes immediately after AN 6.32?",
         "opts": [
             "AN 6.34, With Mahāmoggallāna",
             "AN 6.33, another deity's report on non-decline with two different closing items",
             "The chapter ends here",
             "A return to the thoroughbred simile"],
         "correct": 1,
         "expl": "A close companion discourse, not an identical repeat."},
    ],
    marginalia=[
        ("The deity's six", [
            "respect for: Teacher,",
            "teaching, Saṅgha, training,",
            "diligence, hospitality",
        ]),
        ("From habit to attitude", [
            "AN 6.31: what to do",
            "AN 6.32: what to",
            "hold in reverence",
        ]),
        ("A stronger closing claim", [
            "not just non-decline —",
            "'drawn near to",
            "extinguishment'",
        ]),
        ("Cross-references", [
            "AN 6.21 &middot; the same narrative shape",
            "AN 6.33 &middot; next, a close companion",
        ]),
    ],
    further=[
        '<a href="%s/an6.32/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.33.html">AN 6.33 &middot; Non-decline (2nd)</a> &mdash; next, a close but '
        "not identical companion.",
        '<a href="an-6.31.html">AN 6.31 &middot; A Trainee</a> &mdash; previous, the '
        "habit-focused version of non-decline.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.33 — Dutiyaaparihānasutta
# --------------------------------------------------------------------------- #
page(
    33, "Dutiyaaparihāna", "Non-decline (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 6.33 — Non-decline (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyaaparihānasutta, "
        "a close companion to AN 6.32 whose sixth-item pair — checked directly against the "
        "Pāli — is conscience and prudence, not diligence and hospitality. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove — narrated by the Buddha as having occurred "
                    "'tonight', the night before this telling"),
        ("Speakers", "The Buddha, recounting a deity's visit to the mendicants"),
        ("Form", "The Buddha's own retelling of a deity's report, closed with a verse restating "
                 "the six items"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "As with AN 6.32, deity-visit narratives on non-decline recur "
                              "across the Saṁyutta and its Chinese counterparts; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief, but worth reading "
                       "beside AN 6.32 rather than skimmed as a duplicate"),
    ],
    why=(
        "AN 6.33 looks, at a glance, like a repeat of AN 6.32: another glorious deity lighting "
        "up Jeta's Grove, another report of six things preventing a mendicant's decline, four "
        "of them identical &mdash; respect for the Teacher, the teaching, the Saṅgha, and the "
        "training. Checked directly against the Pāli, though, the final two items are "
        "genuinely different: not diligence and hospitality, as at AN 6.32, but "
        "<em>hirimā</em> and <em>ottappī</em>, conscience and prudence &mdash; the same pair "
        "already introduced at AN 5.1's reading guide earlier in this series."),
    guide=[
        ("The teaching in one sentence", [
            "Respect for the Teacher, the teaching, the Saṅgha, and the training, together with "
            "conscience and prudence, keeps a mendicant from decline."]),
        ("Four shared items, two genuinely different ones", [
            "This discourse and AN 6.32 share their first four items outright: "
            "<em>satthugāravatā, dhammagāravatā, saṅghagāravatā, sikkhāgāravatā</em>. Where AN "
            "6.32 closed with <em>appamādagārava</em> and <em>paṭisanthāragārava</em>, respect "
            "for diligence and for hospitality, this discourse closes instead with "
            "<em>hirimā</em> and <em>ottappī</em> &mdash; not phrased as a form of "
            "<em>gārava</em>, respect, at all, but as directly possessing conscience and "
            "prudence themselves."]),
        ("A pair already met in this series", [
            "Conscience and prudence, <em>hiri</em> and <em>ottappa</em>, were introduced in "
            "detail at AN 5.1's reading guide, which called them <em>lokapāla</em>, "
            "world-protectors, following AN 2.9's earlier treatment. Their appearance here, "
            "closing a list otherwise built from respect for the three refuges and the "
            "training, ties this discourse back to that established pair rather than "
            "introducing new vocabulary."]),
        ("A narrated retelling, not a live report", [
            "AN 6.32 narrates the deity's visit as an event the compiler describes directly. AN "
            "6.33 frames the same kind of scene differently: the Buddha himself tells the "
            "mendicants, in his own words, &ldquo;tonight, a glorious deity&hellip; came to "
            "me,&rdquo; making this discourse the Buddha's first-person account rather than a "
            "third-person narration. The content parallels AN 6.32's structure closely, but the "
            "narrative voice does not."]),
        ("Why check rather than assume", [
            "Given how closely this discourse resembles AN 6.32 &mdash; same opening scene, "
            "same four shared items, same closing verse pattern &mdash; the risk of treating it "
            "as a pure repeat is real. This page follows the same discipline already applied at "
            "AN 6.25 and AN 6.29: verify the actual terms before concluding two similar "
            "passages say the same thing."]),
    ],
    terms=[
        ("hirimā",
         "&ldquo;having conscience&rdquo; &mdash; the fifth item here, distinct from AN 6.32's "
         "diligence."),
        ("ottappī",
         "&ldquo;having prudence&rdquo; &mdash; the sixth and closing item here, distinct from "
         "AN 6.32's hospitality."),
        ("lokapāla",
         "&ldquo;world-protector&rdquo; &mdash; the epithet AN 2.9 gives to conscience and "
         "prudence together, as discussed at AN 5.1's reading guide."),
        ("gārava",
         "&ldquo;respect&rdquo; &mdash; still governing this discourse's first four items, "
         "though not its final two, which are named as qualities directly possessed rather than "
         "objects of respect."),
        ("satthugāravatā",
         "&ldquo;respect for the Teacher&rdquo; &mdash; the first item, shared word for word "
         "with AN 6.32."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's own account of the deity's visit, and his closing "
        "verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha recounts a deity's visit"),
        ("p", "&sect;1", "an6.33:1.1-1.7"),
        ("h3", "The closing verse"),
        ("p", "&sect;2", "an6.33:2.1-2.6"),
    ],
    quiz=[
        {"q": "How many of the six items in this discourse match AN 6.32's list word for word?",
         "opts": [
             "None", "All six", "Four — respect for the Teacher, the teaching, the Saṅgha, and "
             "the training", "Only two"],
         "correct": 2,
         "expl": "The first four items are shared; the final two are genuinely different."},
        {"q": "What are this discourse's final two items, checked directly against the Pāli?",
         "opts": [
             "Diligence and hospitality, matching AN 6.32",
             "Conscience and prudence (hirimā and ottappī), not diligence and hospitality",
             "Faith and wisdom",
             "Sensual restraint and moderation in eating"],
         "correct": 1,
         "expl": "A genuine difference from AN 6.32's closing pair, not a paraphrase."},
        {"q": "Where were conscience and prudence previously introduced in this series?",
         "opts": [
             "Nowhere — they are new to this discourse",
             "At AN 5.1's reading guide, which called them 'world-protectors' following AN 2.9's "
             "earlier treatment",
             "At AN 6.1",
             "At AN 6.13"],
         "correct": 1,
         "expl": "This discourse ties back to an already-established pair rather than "
                 "introducing new vocabulary."},
        {"q": "How does this discourse's narrative framing differ from AN 6.32's?",
         "opts": [
             "They are framed identically",
             "AN 6.32 is narrated in the third person; AN 6.33 is the Buddha's own first-person "
             "retelling — 'tonight, a glorious deity... came to me'",
             "AN 6.33 has no narrative framing at all",
             "AN 6.33 is spoken by a mendicant, not the Buddha"],
         "correct": 1,
         "expl": "The same kind of scene, told in a different narrative voice."},
        {"q": "What discipline does the guide say it applies in reading this discourse against "
              "AN 6.32?",
         "opts": [
             "Assuming the two are identical because they resemble each other closely",
             "The same discipline already applied at AN 6.25 and AN 6.29: verifying the actual "
             "terms before concluding two similar passages say the same thing",
             "Ignoring AN 6.32 entirely",
             "Treating AN 6.33 as a later, corrupted version of AN 6.32"],
         "correct": 1,
         "expl": "A consistent practice across this reading-guide project when discourses "
                 "closely resemble each other."},
        {"q": "What does <em>hirimā</em> mean?",
         "opts": ["Having prudence", "Having conscience", "Having diligence", "Having "
                  "hospitality"],
         "correct": 1,
         "expl": "The fifth item in this discourse's list."},
        {"q": "Are the final two items here phrased as forms of 'respect' (gārava), like the "
              "first four?",
         "opts": [
             "Yes, identically to the first four",
             "No — they are named as qualities directly possessed, not objects of respect",
             "The text does not distinguish this",
             "Only the fifth item is phrased as respect"],
         "correct": 1,
         "expl": "A grammatical shift alongside the content shift, noted directly from the "
                 "source."},
        {"q": "Where is AN 6.33 set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove — matching AN 6.32's setting",
             "Kimbilā",
             "Icchānaṅgala"],
         "correct": 1,
         "expl": "The same location as AN 6.32, though narrated differently."},
        {"q": "What is the risk the guide identifies in reading this discourse quickly?",
         "opts": [
             "Missing its connection to AN 6.34",
             "Treating it as a pure repeat of AN 6.32 given how closely the two resemble each "
             "other in scene, four shared items, and closing structure",
             "Confusing it with AN 6.21",
             "Assuming it contradicts AN 6.32 entirely"],
         "correct": 1,
         "expl": "A close but not identical companion, worth reading side by side rather than "
                 "skimmed."},
        {"q": "What does <em>ottappī</em> mean?",
         "opts": ["Having conscience", "Having prudence", "Having diligence", "Having faith"],
         "correct": 1,
         "expl": "The sixth and closing item of this discourse's list."},
    ],
    marginalia=[
        ("Four shared, two different", [
            "Teacher, teaching,",
            "Saṅgha, training — same",
            "diligence/hospitality vs.",
            "conscience/prudence",
        ]),
        ("A familiar pair returns", [
            "<span class=\"pali\">hiri</span> &amp; <span class=\"pali\">ottappa</span>",
            "first met at AN 5.1,",
            "AN 2.9's 'world-protectors'",
        ]),
        ("Different narrative voice", [
            "AN 6.32: third person",
            "AN 6.33: the Buddha's",
            "own first-person account",
        ]),
        ("Cross-references", [
            "AN 6.32 &middot; previous, the companion",
            "AN 5.1 &middot; conscience &amp; prudence introduced",
        ]),
    ],
    further=[
        '<a href="%s/an6.33/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.34.html">AN 6.34 &middot; With Mahāmoggallāna</a> &mdash; next, a very '
        "different kind of deity-related discourse.",
        '<a href="an-6.32.html">AN 6.32 &middot; Non-decline (1st)</a> &mdash; previous, for '
        "direct comparison of the two closing items.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.34 — Mahāmoggallānasutta
# --------------------------------------------------------------------------- #
page(
    34, "Mahāmoggallāna", "With Mahāmoggallāna",
    vagga=VAGGA_4,
    meta_title="AN 6.34 — With Mahāmoggallāna | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mahāmoggallānasutta, "
        "in which Mahāmoggallāna visits a realm of divinity to ask a deceased mendicant which "
        "gods know they are stream-enterers. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove — Mahāmoggallāna's own dwelling, before he "
                    "travels by psychic power to a realm of divinity"),
        ("Speakers", "Mahāmoggallāna and the divinity Tissa, a recently deceased mendicant"),
        ("Form", "A private reflection, a psychic journey, a question-and-answer dialogue "
                 "repeated across six classes of deities"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Cross-realm dialogues verifying stream-entry recur in related "
                              "form across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a vivid narrative whose real "
                       "content is a precise doctrinal point about what stream-entry requires"),
    ],
    why=(
        "Mahāmoggallāna, wondering privately which gods know themselves to be stream-enterers, "
        "simply travels to find out &mdash; vanishing from Jeta's Grove and reappearing in a "
        "realm of divinity, where a monk named Tissa, recently reborn there, receives him as an "
        "old friend. The question and its answer repeat across six classes of deities, and the "
        "answer is the same each time: rank among the gods has nothing to do with it. What "
        "matters is confidence in the Triple Gem and ethics loved by the noble ones."),
    guide=[
        ("The teaching in one sentence", [
            "Across six classes of deities, from the gods of the four great kings up through the "
            "gods who control what is created by others, only those with experiential "
            "confidence in the Buddha, the teaching, and the Saṅgha, and the ethics loved by the "
            "noble ones, know that they are stream-enterers &mdash; not all members of any "
            "class, regardless of how exalted."]),
        ("A question answered by travel, not speculation", [
            "The discourse opens with Mahāmoggallāna wondering something in private retreat, "
            "and instead of reasoning it out, he simply goes to check &mdash; &ldquo;as easily "
            "as a strong person would extend or contract their arm.&rdquo; The psychic journey "
            "is treated matter-of-factly, without commentary on how remarkable it is; the "
            "discourse's interest lies entirely in what he finds when he arrives, not in the "
            "means of travel."]),
        ("The same question, asked six times, with the same answer each time", [
            "Mahāmoggallāna asks Tissa about the gods of the four great kings, then in turn "
            "about the gods of the thirty-three, the gods of Yama, the joyful gods, the gods "
            "who love to create, and the gods who control what is created by others &mdash; six "
            "classes forming an ascending hierarchy of heavenly realms. Tissa's answer is "
            "identical for every class: some know, some don't, and rank within the heavenly "
            "hierarchy makes no difference to which."]),
        ("What actually distinguishes those who know", [
            "The dividing line Tissa names is not birth, status, or which heaven a deity "
            "occupies, but two things: &ldquo;experiential confidence&rdquo; "
            "(<em>aveccappasāda</em>) in the Buddha, the teaching, and the Saṅgha, and "
            "possessing &ldquo;the ethics loved by the noble ones.&rdquo; A deity lacking these, "
            "however exalted their realm, does not know their own attainment; a deity with "
            "them does, regardless of realm."]),
        ("Confirmation rather than debate", [
            "Mahāmoggallāna's closing response &mdash; &ldquo;approved and agreed with what the "
            "divinity Tissa said&rdquo; &mdash; frames the whole exchange as verification of "
            "something the discourse assumes was already understood correctly, not as new "
            "doctrine being negotiated. The elaborate cross-realm structure exists to confirm "
            "one plain point across six increasingly exalted settings, not to complicate it."]),
    ],
    terms=[
        ("sotāpanna",
         "&ldquo;stream-enterer&rdquo; &mdash; one who has entered the stream to awakening, "
         "assured of eventual full liberation and no longer liable to rebirth in the underworld."),
        ("aveccappasāda",
         "&ldquo;experiential confidence,&rdquo; &ldquo;confirmed confidence&rdquo; &mdash; the "
         "quality Tissa names as one of the two things that let a deity know their own "
         "attainment."),
        ("ariyakantasīla",
         "&ldquo;ethics loved by the noble ones&rdquo; &mdash; the second quality Tissa names, "
         "paired with confidence in the Triple Gem."),
        ("cātumahārājika",
         "&ldquo;the gods of the four great kings&rdquo; &mdash; the first and lowest of the six "
         "classes of deities named in this discourse's ascending sequence."),
        ("iddhi",
         "&ldquo;psychic power&rdquo; &mdash; what carries Mahāmoggallāna between Jeta's Grove "
         "and the realm of divinity, treated matter-of-factly rather than as the discourse's "
         "main point."),
    ],
    text_intro=(
        "The discourse in full: Mahāmoggallāna's private question, his journey, and his "
        "dialogue with the divinity Tissa across six classes of deities. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Mahāmoggallāna's question, and his journey"),
        ("p", "&sect;1", "an6.34:1.1-2.9"),
        ("h3", "The gods of the four great kings"),
        ("p", "&sect;2", "an6.34:3.1-4.4"),
        ("h3", "Five further classes of deities, and Mahāmoggallāna's return"),
        ("p", "&sect;3", "an6.34:5.1-7.1"),
    ],
    quiz=[
        {"q": "What does Mahāmoggallāna wonder while in private retreat?",
         "opts": [
             "How many topics for recollection there are",
             "Which gods know that they are stream-enterers, not liable to rebirth in the "
             "underworld, assured, destined for awakening",
             "How to develop psychic power",
             "Whether deities exist at all"],
         "correct": 1,
         "expl": "A question he answers by traveling to find out, rather than reasoning it out."},
        {"q": "How does Mahāmoggallāna find the answer to his question?",
         "opts": [
             "He asks the Buddha directly",
             "He travels by psychic power to a realm of divinity to ask a recently deceased "
             "mendicant, Tissa, now reborn there",
             "He consults ancient texts",
             "He waits for a deity to visit him"],
         "correct": 1,
         "expl": "'As easily as a strong person would extend or contract their arm.'"},
        {"q": "Across how many classes of deities does the same question get asked?",
         "opts": ["Three", "Six, forming an ascending hierarchy of heavenly realms", "Ten", "One"],
         "correct": 1,
         "expl": "From the gods of the four great kings up through the gods who control what is "
                 "created by others."},
        {"q": "What is Tissa's answer for each class of deity?",
         "opts": [
             "All members of each class know they are stream-enterers",
             "Only those with experiential confidence in the Triple Gem and the ethics loved by "
             "the noble ones know — rank within the class makes no difference",
             "None of them know, regardless of class",
             "Only the highest-ranked deities in each class know"],
         "correct": 1,
         "expl": "The identical answer repeated across all six classes."},
        {"q": "What two qualities does Tissa name as actually distinguishing those who know "
              "their attainment?",
         "opts": [
             "Wealth and social status",
             "Experiential confidence in the Buddha, the teaching, and the Saṅgha, and the "
             "ethics loved by the noble ones",
             "Physical beauty and psychic power",
             "Length of time spent as a deity"],
         "correct": 1,
         "expl": "Neither depends on which heavenly realm a deity occupies."},
        {"q": "How does the guide characterize Mahāmoggallāna's closing response to Tissa?",
         "opts": [
             "As a rejection of Tissa's answer",
             "As confirmation of something already understood correctly, not new doctrine being "
             "negotiated — 'approved and agreed with what the divinity Tissa said'",
             "As a request for further clarification",
             "As a challenge to debate the point further"],
         "correct": 1,
         "expl": "The elaborate structure confirms one plain point rather than complicating it."},
        {"q": "What does <em>aveccappasāda</em> mean?",
         "opts": [
             "Blind faith without examination",
             "Experiential confidence, confirmed confidence",
             "Fear of the deities",
             "A type of psychic power"],
         "correct": 1,
         "expl": "One of the two qualities Tissa names as distinguishing those who know their "
                 "own attainment."},
        {"q": "Where does this discourse's narrative begin?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, before Mahāmoggallāna travels by psychic power",
             "Kimbilā, in the Freshwater Mangrove Wood",
             "Icchānaṅgala, in a forest"],
         "correct": 1,
         "expl": "The setting the whole nipāta has repeatedly defaulted to."},
        {"q": "Who is Tissa, according to the discourse?",
         "opts": [
             "A deity who has always been divine",
             "A monk who had recently passed away and been reborn in a realm of divinity",
             "A senior disciple still living as a mendicant",
             "A brahmin who converted to the teaching"],
         "correct": 1,
         "expl": "A formerly ordinary mendicant, now able to answer Mahāmoggallāna's question "
                 "from direct experience."},
        {"q": "What does <em>cātumahārājika</em> refer to?",
         "opts": [
             "The gods of the thirty-three",
             "The gods of the four great kings — the first and lowest class named in this "
             "discourse's sequence",
             "The highest class of deity named",
             "A class of human beings, not deities"],
         "correct": 1,
         "expl": "Where the ascending sequence of six deity-classes begins."},
    ],
    marginalia=[
        ("Six deity classes", [
            "four great kings",
            "the thirty-three &middot; Yama",
            "joyful &middot; creators",
            "controllers of others'",
            "creations",
        ]),
        ("One answer, repeated", [
            "not all members know —",
            "only those with faith",
            "and noble ethics",
        ]),
        ("Travel as method", [
            "no debate on how —",
            "he simply goes",
            "and asks directly",
        ]),
        ("Cross-references", [
            "AN 6.32/6.33 &middot; respect that prevents decline",
        ]),
    ],
    further=[
        '<a href="%s/an6.34/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.35.html">AN 6.35 &middot; Things That Play a Part in Realization</a> '
        "&mdash; next, six perceptions central to insight.",
        '<a href="an-6.33.html">AN 6.33 &middot; Non-decline (2nd)</a> &mdash; previous, a '
        "different register of deity-related teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.35 — Vijjābhāgiyasutta
# --------------------------------------------------------------------------- #
page(
    35, "Vijjābhāgiya", "Things That Play a Part in Realization",
    vagga=VAGGA_4,
    meta_title="AN 6.35 — Things That Play a Part in Realization | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vijjābhāgiyasutta, "
        "naming six perceptions — of impermanence, of suffering in impermanence, of not-self "
        "in suffering, of giving up, of fading away, and of cessation — that build toward "
        "insight. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A bare list of six named perceptions, each building on the one before"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The impermanence-suffering-not-self progression of insight "
                              "perceptions recurs across the Chinese Āgamas and Abhidharma "
                              "literature; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, but each term names "
                       "a distinct stage in a cumulative sequence, not six independent items"),
    ],
    why=(
        "AN 6.35 names six perceptions &ldquo;that play a part in realization&rdquo; &mdash; "
        "<em>vijjābhāgiya</em>, contributing to knowledge or true understanding. Unlike most of "
        "this chapter's six-item lists, these six are not parallel, interchangeable items but a "
        "cumulative chain, each perception explicitly building on its predecessor: the "
        "perception of suffering arises <em>in</em> impermanence, the perception of not-self "
        "arises <em>in</em> suffering, and so on."),
    guide=[
        ("The teaching in one sentence", [
            "Six perceptions play a part in realization: of impermanence, of suffering in what "
            "is impermanent, of not-self in what is suffering, of giving up, of fading away, "
            "and of cessation."]),
        ("A chain, not a list of options", [
            "The Pāli itself encodes the cumulative structure directly in its compound terms: "
            "<em>anicce dukkhasaññā</em>, &ldquo;perception of suffering <em>in "
            "impermanence</em>,&rdquo; and <em>dukkhe anattasaññā</em>, &ldquo;perception of "
            "not-self <em>in suffering</em>.&rdquo; The second perception is not a separate "
            "observation alongside the first; it is what becomes visible once the first has "
            "been seen through. The same logic likely extends through giving up, fading away, "
            "and cessation, each a further deepening rather than a fresh, unrelated insight."]),
        ("The first three as the classic three marks", [
            "The first three items &mdash; impermanence, suffering, not-self &mdash; are the "
            "canon's three characteristics (<em>tilakkhaṇa</em>) of conditioned existence, "
            "presented here in their canonical order and their logical relationship: not three "
            "independent facts to notice, but one seen inside another, suffering discovered "
            "within impermanence and selflessness discovered within suffering."]),
        ("The last three as what follows from seeing clearly", [
            "Giving up (<em>pahāna</em>), fading away (<em>virāga</em>), and cessation "
            "(<em>nirodha</em>) name not further facts to perceive about experience but "
            "responses that become available once the first three perceptions are established: "
            "what is truly seen as impermanent, suffering, and not-self becomes something a "
            "mind can give up, from which desire fades, and which can cease."]),
        ("A discourse offering vocabulary, not instruction", [
            "As with several of this chapter's shortest discourses, AN 6.35 supplies technical "
            "terms without walking through how to develop any of the six perceptions in "
            "practice. It functions as a compact map of a progression the canon elaborates at "
            "far greater length elsewhere &mdash; naming the stages, not teaching the method."]),
    ],
    terms=[
        ("vijjābhāgiya",
         "&ldquo;playing a part in realization,&rdquo; &ldquo;contributing to true "
         "knowledge&rdquo; &mdash; the discourse's own title, describing what all six "
         "perceptions have in common."),
        ("aniccasaññā",
         "&ldquo;perception of impermanence&rdquo; &mdash; the first and foundational "
         "perception in this cumulative chain."),
        ("anicce dukkhasaññā",
         "&ldquo;perception of suffering in impermanence&rdquo; &mdash; the second, arising "
         "within the first rather than beside it."),
        ("dukkhe anattasaññā",
         "&ldquo;perception of not-self in suffering&rdquo; &mdash; the third, completing the "
         "canon's three characteristics of conditioned existence in cumulative form."),
        ("nirodhasaññā",
         "&ldquo;perception of cessation&rdquo; &mdash; the sixth and final perception, closing "
         "the chain."),
    ],
    text_intro=(
        "The discourse in full: the six perceptions that play a part in realization. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six perceptions that play a part in realization"),
        ("p", "&sect;1", "an6.35:1.1-1.4"),
    ],
    quiz=[
        {"q": "What six perceptions does AN 6.35 name?",
         "opts": [
             "Impermanence; suffering in impermanence; not-self in suffering; giving up; fading "
             "away; cessation",
             "Faith, energy, mindfulness, immersion, wisdom, and liberation",
             "Danger, suffering, disease, boil, chain, bog",
             "Seeing, listening, acquisition, training, service, recollection"],
         "correct": 0,
         "expl": "A cumulative six-stage progression, not six independent items."},
        {"q": "How does the guide characterize the relationship between the first and second "
              "perceptions?",
         "opts": [
             "They are entirely independent observations",
             "The second is not separate from the first but arises within it — 'perception of "
             "suffering in impermanence', encoded directly in the Pāli compound",
             "The second contradicts the first",
             "They apply to different objects entirely"],
         "correct": 1,
         "expl": "What becomes visible once impermanence has been seen through."},
        {"q": "What are the first three perceptions collectively known as, elsewhere in the "
              "canon?",
         "opts": [
             "The four brahmavihāra",
             "The three characteristics (tilakkhaṇa) of conditioned existence — impermanence, "
             "suffering, not-self",
             "The three refuges",
             "The three sources of deeds"],
         "correct": 1,
         "expl": "Presented here in their canonical order and cumulative relationship."},
        {"q": "What do the last three perceptions — giving up, fading away, cessation — "
              "represent, according to the guide?",
         "opts": [
             "Three further independent facts to notice about experience",
             "Responses that become available once the first three perceptions are established "
             "— what is truly seen as impermanent, suffering, and not-self can then be given "
             "up, faded from, and ceased",
             "A contradiction of the first three",
             "A completely unrelated list appended for length"],
         "correct": 1,
         "expl": "A natural continuation once the three characteristics are genuinely seen."},
        {"q": "What does <em>vijjābhāgiya</em> mean?",
         "opts": [
             "'Opposed to knowledge'",
             "'Playing a part in realization', contributing to true knowledge",
             "'A type of meditative absorption'",
             "'Belonging to a deity'"],
         "correct": 1,
         "expl": "What all six perceptions are said to have in common."},
        {"q": "What kind of discourse is AN 6.35, according to the guide?",
         "opts": [
             "A detailed step-by-step meditation manual",
             "A compact map supplying technical vocabulary for a progression, without walking "
             "through how to develop any of the six perceptions",
             "A narrative involving multiple characters",
             "A refutation of a wrong view held by a brahmin"],
         "correct": 1,
         "expl": "Naming stages, not teaching method — consistent with several of this "
                 "chapter's shortest discourses."},
        {"q": "Is a setting stated for AN 6.35?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, continuing this nipāta's frequent pattern."},
        {"q": "What does <em>dukkhe anattasaññā</em> mean?",
         "opts": [
             "Perception of impermanence",
             "Perception of not-self in suffering",
             "Perception of cessation",
             "Perception of giving up"],
         "correct": 1,
         "expl": "The third perception, completing the three characteristics in cumulative form."},
        {"q": "What does <em>pahāna</em> mean, as the fourth perception in this sequence?",
         "opts": ["Fading away", "Cessation", "Giving up", "Impermanence"],
         "correct": 2,
         "expl": "The first of the three response-perceptions following the three "
                 "characteristics."},
        {"q": "How many total perceptions does this discourse name?",
         "opts": ["Three", "Five", "Six", "Nine"],
         "correct": 2,
         "expl": "Three characteristics of existence, plus three responses that follow from "
                 "seeing them clearly."},
    ],
    marginalia=[
        ("Three characteristics", [
            "impermanence",
            "&rarr; suffering within it",
            "&rarr; not-self within that",
        ]),
        ("Three responses", [
            "giving up &middot; fading",
            "away &middot; cessation",
        ]),
        ("A chain, not a list", [
            "each perception arises",
            "within the one before it,",
            "not beside it",
        ]),
        ("Cross-references", [
            "AN 6.34 &middot; previous, a different subject",
        ]),
    ],
    further=[
        '<a href="%s/an6.35/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.36.html">AN 6.36 &middot; Roots of Dispute</a> &mdash; next, six causes '
        "of conflict within the Saṅgha.",
        '<a href="an-6.34.html">AN 6.34 &middot; With Mahāmoggallāna</a> &mdash; previous, a '
        "different subject from this chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.36 — Vivādamūlasutta
# --------------------------------------------------------------------------- #
page(
    36, "Vivādamūla", "Roots of Dispute",
    vagga=VAGGA_4,
    meta_title="AN 6.36 — Roots of Dispute | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vivādamūlasutta, "
        "naming six character flaws that generate conflict within the Saṅgha, each with the "
        "same practical instruction attached. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Six character traits named in turn, each followed by an identical closing "
                 "instruction to give up or forestall it"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The six roots of dispute recur closely in the Vinaya's own "
                              "account of the Kosambī schism and across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct and practical, "
                       "naming interpersonal failings rather than abstract qualities"),
    ],
    why=(
        "Where much of this chapter has concerned individual practice &mdash; decline, "
        "recollection, perception &mdash; AN 6.36 turns to what actually fractures a "
        "community: six character traits, from irritability to rigid attachment to one's own "
        "views, each identified as a root from which disputes in the Saṅgha grow. Every one of "
        "the six carries the identical instruction attached: notice it in yourself or others, "
        "and work to give it up."),
    guide=[
        ("The teaching in one sentence", [
            "Six roots generate disputes in the Saṅgha: being irritable and acrimonious, "
            "offensive and contemptuous, jealous and stingy, devious and deceitful, having "
            "corrupt wishes and wrong view, and being attached to one's own views, holding them "
            "tight and refusing to let go."]),
        ("Paired traits, not six isolated flaws", [
            "Each of the six items names not one quality but a pair: irritable "
            "<em>and</em> acrimonious, offensive <em>and</em> contemptuous, jealous "
            "<em>and</em> stingy, devious <em>and</em> deceitful, corrupt wishes <em>and</em> "
            "wrong view. The pairing suggests each root is a cluster &mdash; an inner "
            "disposition and its outward expression &mdash; rather than a single simple "
            "trait."]),
        ("A shared consequence stated for each", [
            "Every one of the six items, not only the sixth, is followed by the identical "
            "diagnosis: such a mendicant &ldquo;lacks respect and reverence for the Teacher, "
            "the teaching, and the Saṅgha, and doesn't fulfill the training,&rdquo; and "
            "&ldquo;creates a dispute in the Saṅgha, which is for the detriment and suffering "
            "of the people&hellip; for the harm, detriment, and suffering of gods and "
            "humans.&rdquo; This is a serious claim: the discourse treats interpersonal "
            "friction not as a minor social problem but as harm extending to &ldquo;gods and "
            "humans&rdquo; broadly."]),
        ("An identical instruction, repeated six times", [
            "Rather than varying its advice item by item, the discourse attaches the same "
            "instruction to every root: &ldquo;if you see such a root of dispute in yourselves "
            "or others, you should try to give up this bad thing. If you don't see it, you "
            "should practice so that it doesn't come up in the future.&rdquo; The instruction "
            "covers both correction and prevention, and applies equally whether the fault is "
            "found in oneself or observed in another."]),
        ("The sixth root as a special case", [
            "The final root, attachment to one's own views &mdash; &ldquo;holding them tight, "
            "and refusing to let go&rdquo; &mdash; stands apart from the other five, which "
            "concern temperament and conduct. This one concerns intellectual rigidity "
            "specifically, and its presence at the list's end, closing five traits about how a "
            "person acts with one about how a person clings to what they believe, suggests "
            "dispute can be rooted as much in doctrine defended too fiercely as in bad "
            "behavior."]),
    ],
    terms=[
        ("vivādamūla",
         "&ldquo;root of dispute&rdquo; &mdash; the discourse's own title, naming what each of "
         "the six character traits is said to generate."),
        ("kodhana upanāhī",
         "&ldquo;irritable and acrimonious&rdquo; &mdash; the first root, pairing a hot temper "
         "with a tendency to hold grudges."),
        ("issukī maccharī",
         "&ldquo;jealous and stingy&rdquo; &mdash; the third root, pairing resentment of "
         "others' good fortune with reluctance to share one's own."),
        ("sandiṭṭhiparāmāsī ādhānagāhī duppaṭinissaggī",
         "&ldquo;attached to their own views, holding them tight, and refusing to let go&rdquo; "
         "&mdash; the sixth and final root, concerning intellectual rather than temperamental "
         "rigidity."),
        ("saṅghe vivādaṁ janeti",
         "&ldquo;creates a dispute in the Saṅgha&rdquo; &mdash; the shared consequence attached "
         "to every one of the six roots."),
    ],
    text_intro=(
        "The discourse in full: the six roots of dispute, each with its shared consequence and "
        "instruction. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The first root: irritable and acrimonious"),
        ("p", "&sect;1", "an6.36:1.1-1.8"),
        ("h3", "Five further roots, and the conclusion"),
        ("p", "&sect;2", "an6.36:2.1-2.11"),
    ],
    quiz=[
        {"q": "What six roots of dispute does this discourse name?",
         "opts": [
             "Irritable/acrimonious; offensive/contemptuous; jealous/stingy; devious/deceitful; "
             "corrupt wishes/wrong view; attachment to one's own views",
             "The five hindrances plus doubt",
             "Danger, suffering, disease, boil, chain, bog",
             "Work, talk, sleep, company, closeness, proliferation"],
         "correct": 0,
         "expl": "Six paired character traits, each generating conflict within the Saṅgha."},
        {"q": "How is each of the six roots structured, according to the guide?",
         "opts": [
             "As a single simple trait",
             "As a pair of qualities — an inner disposition and its outward expression — rather "
             "than one isolated flaw",
             "As three separate qualities each",
             "As a virtue rather than a flaw"],
         "correct": 1,
         "expl": "Irritable AND acrimonious, jealous AND stingy, and so on."},
        {"q": "What consequence is attached to every one of the six roots, not just the last?",
         "opts": [
             "Expulsion from the Saṅgha",
             "Lacking respect for the Teacher, teaching, and Saṅgha, and creating dispute that "
             "harms 'gods and humans' broadly",
             "No consequence is stated",
             "Rebirth in a bad place, immediately"],
         "correct": 1,
         "expl": "A serious claim treating interpersonal friction as harm extending well beyond "
                 "the immediate parties."},
        {"q": "What instruction is attached to each of the six roots?",
         "opts": [
             "A different, specific remedy for each root",
             "The identical instruction repeated six times: give it up if seen in yourself or "
             "others, and practice to prevent it if not yet present",
             "No instruction is given, only description",
             "Report the offending mendicant to a senior immediately"],
         "correct": 1,
         "expl": "Covering both correction and prevention, applied uniformly."},
        {"q": "How does the guide characterize the sixth root, compared to the other five?",
         "opts": [
             "It is identical in kind to the other five",
             "It stands apart, concerning intellectual rigidity — clinging to one's own views — "
             "rather than temperament and conduct",
             "It is the least serious of the six",
             "It does not actually cause dispute"],
         "correct": 1,
         "expl": "Suggesting dispute can be rooted in doctrine defended too fiercely, not only "
                 "bad behavior."},
        {"q": "What does <em>vivādamūla</em> mean?",
         "opts": ["Root of harmony", "Root of dispute", "Root of generosity", "Root of wisdom"],
         "correct": 1,
         "expl": "The discourse's own title."},
        {"q": "Is a setting stated for AN 6.36?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Kosambī", "Yes, at Rājagaha"],
         "correct": 1,
         "expl": "A bare formula, though the theme closely echoes the Vinaya's Kosambī schism "
                 "account."},
        {"q": "What does <em>saṅghe vivādaṁ janeti</em> mean?",
         "opts": [
             "'Brings harmony to the Saṅgha'",
             "'Creates a dispute in the Saṅgha'",
             "'Leaves the Saṅgha'",
             "'Teaches the Saṅgha'"],
         "correct": 1,
         "expl": "The shared consequence attached to all six roots."},
        {"q": "What does <em>issukī maccharī</em> mean?",
         "opts": [
             "Irritable and acrimonious",
             "Jealous and stingy",
             "Devious and deceitful",
             "Attached to one's own views"],
         "correct": 1,
         "expl": "The third of the six roots."},
        {"q": "What broader context does the guide note for this discourse's theme?",
         "opts": [
             "It has no relation to any other canonical text",
             "The six roots recur closely in the Vinaya's own account of the Kosambī schism",
             "It only applies to lay disputes, not the Saṅgha",
             "It was composed specifically to settle a dispute in this discourse's own narrative"],
         "correct": 1,
         "expl": "A theme with real institutional weight elsewhere in the canon."},
    ],
    marginalia=[
        ("Six roots, paired", [
            "irritable/acrimonious",
            "offensive/contemptuous",
            "jealous/stingy",
            "devious/deceitful",
            "corrupt wishes/wrong view",
            "clings to own views",
        ]),
        ("One shared instruction", [
            "see it — give it up",
            "don't see it — prevent",
            "it arising later",
        ]),
        ("A serious claim", [
            "not minor friction —",
            "harm to 'gods",
            "and humans' broadly",
        ]),
        ("Cross-references", [
            "AN 6.35 &middot; previous, insight perceptions",
            "AN 6.37 &middot; next, a gift's six factors",
        ]),
    ],
    further=[
        '<a href="%s/an6.36/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.37.html">AN 6.37 &middot; A Gift With Six Factors</a> &mdash; next, a '
        "very different register of teaching.",
        '<a href="an-6.35.html">AN 6.35 &middot; Things That Play a Part in Realization</a> '
        "&mdash; previous, a different subject entirely.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.37 — Chaḷaṅgadānasutta
# --------------------------------------------------------------------------- #
page(
    37, "Chaḷaṅgadāna", "A Gift With Six Factors",
    vagga=VAGGA_4,
    meta_title="A Gift With Six Factors | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Chaḷaṅgadānasutta, "
        "where the Buddha sees a laywoman's six-factored donation and compares its merit to "
        "the incalculable volume of the ocean. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery"),
        ("Speakers", SPEAKER),
        ("Form", "A witnessed event, an analytical breakdown into six factors, an extended "
                 "simile, and a closing verse"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Analyses of what makes a gift maximally meritorious recur across "
                              "the Chinese Āgamas and later Abhidharma literature; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a clear analytical structure "
                       "built around one memorable simile"),
    ],
    why=(
        "The Buddha, seeing with his clairvoyance a laywoman named Veḷukaṇṭakī preparing a "
        "donation for the Saṅgha, uses the occasion to analyze exactly what makes a gift "
        "maximally meritorious: three factors belonging to the donor's state of mind, and "
        "three to the recipients' state of purification. Six factors together, he says, "
        "produce merit as difficult to measure precisely as the water in the ocean &mdash; not "
        "immeasurable in the sense of infinite, but too vast to count exactly, reckoned only as "
        "&ldquo;an incalculable, immeasurable, great mass.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "A gift has six factors &mdash; three belonging to the donor (a good mood before "
            "giving, confidence while giving, feeling uplifted after giving) and three to the "
            "recipients (being free of greed, hate, and delusion, or practicing to be free of "
            "them) &mdash; and such a gift produces merit as difficult to measure precisely as "
            "the water in the ocean."]),
        ("Three factors on each side of the exchange", [
            "The analysis divides evenly: the donor's three factors concern the psychological "
            "quality of the act of giving itself &mdash; mood before, confidence during, and "
            "feeling after &mdash; while the recipients' three factors concern their own "
            "spiritual state, independent of anything the donor does. Merit, on this analysis, "
            "is not produced by the donor alone or the recipient alone but by the conjunction "
            "of both sides being right."]),
        ("An event the Buddha witnesses, not one he arranges", [
            "The occasion for this teaching is not a question asked or a problem raised but "
            "something the Buddha simply observes happening &mdash; a specific, named "
            "laywoman's preparation for a specific, named group of recipients, &ldquo;the "
            "mendicant Saṅgha headed by Sāriputta and Moggallāna.&rdquo; The analysis that "
            "follows is prompted by a real act already underway, not a hypothetical case."]),
        ("The ocean simile, and what 'immeasurable' actually means", [
            "The extended simile &mdash; trying to state exactly how many gallons of water fill "
            "the ocean &mdash; is worth reading carefully for what it claims and doesn't. It "
            "does not claim the merit is literally infinite or beyond all limit; it claims only "
            "that, like the ocean's volume, a precise figure is impractical to state, so both "
            "are &ldquo;simply reckoned as an incalculable, immeasurable, great mass.&rdquo; The "
            "vastness is a statement about difficulty of measurement, not a metaphysical claim "
            "about infinity."]),
        ("Closing verses naming a named practitioner's example", [
            "The closing verses restate the six factors in compressed form and end by "
            "describing an &ldquo;intelligent, faithful person&rdquo; who gives &ldquo;with a "
            "mind of letting go&rdquo; as reborn &ldquo;in a happy, pleasing world&rdquo; "
            "&mdash; drawing a direct line from the specific, witnessed act of generosity at "
            "the discourse's opening to a general statement about what such giving leads to."]),
    ],
    terms=[
        ("chaḷaṅgadāna",
         "&ldquo;gift with six factors&rdquo; &mdash; the discourse's own title, naming the "
         "specific structure of an especially meritorious donation."),
        ("dakkhiṇā",
         "&ldquo;religious donation,&rdquo; &ldquo;offering&rdquo; &mdash; the term for the "
         "gift being prepared and analyzed."),
        ("cāgasampahaṁsana",
         "not a single compound in this translation but the sense captured by &ldquo;feeling "
         "uplifted after giving&rdquo; &mdash; the donor's third factor."),
        ("khīṇarāgā khīṇadosā khīṇamohā",
         "&ldquo;free of greed, hate, and delusion&rdquo; &mdash; the recipients' state "
         "described in the first of their three factors, or else practicing toward it."),
        ("puññakkhandha",
         "&ldquo;mass of merit&rdquo; &mdash; what the discourse says such a six-factored "
         "donation produces, reckoned incalculable like the ocean's volume."),
    ],
    text_intro=(
        "The discourse in full: the witnessed donation, the six factors analyzed, and the "
        "closing simile and verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A witnessed donation"),
        ("p", "&sect;1", "an6.37:1.1-1.5"),
        ("h3", "The six factors, analyzed"),
        ("p", "&sect;2", "an6.37:2.1-3.5"),
        ("h3", "The ocean simile"),
        ("p", "&sect;3", "an6.37:4.1-5.4"),
        ("h3", "The closing verses"),
        ("p", "&sect;4", "an6.37:6.1-9.4"),
    ],
    quiz=[
        {"q": "What prompts this discourse?",
         "opts": [
             "A mendicant's question about generosity",
             "The Buddha seeing, with his clairvoyance, a laywoman named Veḷukaṇṭakī preparing "
             "a donation for the Saṅgha",
             "A debate between two mendicants",
             "A deity's nighttime visit"],
         "correct": 1,
         "expl": "A real, witnessed event, not a hypothetical case."},
        {"q": "What are the donor's three factors?",
         "opts": [
             "Being free of greed, hate, and delusion",
             "A good mood before giving, confidence while giving, and feeling uplifted after "
             "giving",
             "Wealth, status, and generosity",
             "Faith, energy, and wisdom"],
         "correct": 1,
         "expl": "The psychological quality of the act of giving itself."},
        {"q": "What are the recipients' three factors?",
         "opts": [
             "Seniority, learning, and reputation",
             "Being free of greed, hate, and delusion — or practicing to be free of them",
             "Physical beauty, strength, and speed",
             "Having received many donations before"],
         "correct": 1,
         "expl": "Independent of anything the donor does — the recipients' own spiritual state."},
        {"q": "What does the ocean simile actually claim, according to the guide?",
         "opts": [
             "That the merit is literally infinite and beyond all limit",
             "That, like the ocean's volume, a precise figure is impractical to state — a claim "
             "about difficulty of measurement, not a metaphysical claim about infinity",
             "That the merit can be calculated exactly with enough effort",
             "That giving to the ocean itself produces merit"],
         "correct": 1,
         "expl": "'Simply reckoned as an incalculable, immeasurable, great mass' — vastness, not "
                 "literal infinity."},
        {"q": "Where is AN 6.37 set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "Kimbilā",
             "Icchānaṅgala"],
         "correct": 1,
         "expl": "The setting most Aṅguttara discourses default to."},
        {"q": "Who are the specific recipients named in this donation?",
         "opts": [
             "An unnamed group of mendicants",
             "The mendicant Saṅgha headed by Sāriputta and Moggallāna",
             "Only the Buddha himself",
             "A group of lay followers"],
         "correct": 1,
         "expl": "A specific, named group, grounding the teaching in a concrete occasion."},
        {"q": "According to the discourse's analysis, is merit produced by the donor alone?",
         "opts": [
             "Yes, entirely by the donor's mental state",
             "No — merit is produced by the conjunction of both the donor's state of mind and "
             "the recipients' spiritual state",
             "No, entirely by the recipients alone",
             "The discourse does not address this question"],
         "correct": 1,
         "expl": "Three factors on each side, working together."},
        {"q": "What does <em>puññakkhandha</em> mean?",
         "opts": ["A type of meditation", "Mass of merit", "A monastic robe", "A ritual gesture"],
         "correct": 1,
         "expl": "What the six-factored donation is said to produce, reckoned incalculable."},
        {"q": "What does the closing verse say about the 'intelligent, faithful person' who "
              "gives this way?",
         "opts": [
             "They gain nothing from the act",
             "They give 'with a mind of letting go' and are reborn 'in a happy, pleasing world'",
             "They must repeat the gift many times to gain any merit",
             "They lose social standing"],
         "correct": 1,
         "expl": "A direct line from the specific witnessed act to a general statement of "
                 "consequence."},
        {"q": "How does the analysis divide the six factors?",
         "opts": [
             "All six belong to the donor",
             "Three belong to the donor's state of mind, three to the recipients' spiritual "
             "state",
             "All six belong to the recipients",
             "Two to the donor, four to the recipients"],
         "correct": 1,
         "expl": "An even split across both sides of the exchange."},
    ],
    marginalia=[
        ("Three from the donor", [
            "good mood before",
            "confidence during",
            "uplifted after",
        ]),
        ("Three from recipients", [
            "free of greed,",
            "hate, and delusion —",
            "or practicing toward it",
        ]),
        ("The ocean simile", [
            "not infinite —",
            "simply too vast",
            "to state precisely",
        ]),
        ("Cross-references", [
            "AN 6.36 &middot; previous, roots of dispute",
            "AN 6.38 &middot; next, a debate on volition",
        ]),
    ],
    further=[
        '<a href="%s/an6.37/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.38.html">AN 6.38 &middot; One&rsquo;s Own Volition</a> &mdash; next, a '
        "debate refuting a fatalist doctrine.",
        '<a href="an-6.36.html">AN 6.36 &middot; Roots of Dispute</a> &mdash; previous, a very '
        "different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.38 — Attakārīsutta
# --------------------------------------------------------------------------- #
page(
    38, "Attakārī", "One&rsquo;s Own Volition",
    vagga=VAGGA_4,
    meta_title="AN 6.38 — One's Own Volition | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Attakārīsutta, in "
        "which the Buddha refutes a brahmin's fatalist doctrine that no one acts of their own "
        "or another's volition, using six named elements of effort as evidence. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "A brahmin, and the Buddha"),
        ("Form", "A stated doctrine, a sharp rejection, and a two-part argument from observable "
                 "elements of effort"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Refutations of fatalist and determinist doctrines recur across "
                              "the Chinese Āgamas, often in debate with specific named "
                              "opponents; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a philosophical argument "
                       "worth following step by step, not merely a list to memorize"),
    ],
    why=(
        "A brahmin states a doctrine to the Buddha directly: no one acts of their own volition, "
        "nor of another's. The Buddha's response is unusually blunt for this series &mdash; "
        "&ldquo;may I never see or hear of anyone holding such a doctrine or view!&rdquo; "
        "&mdash; and his refutation is not abstract but built from six named observable "
        "elements: initiative, persistence, exertion, strength, endurance, and energy. If these "
        "elements exist, and beings who exercise them are found, then volition is real."),
    guide=[
        ("The teaching in one sentence", [
            "Because there is an observable element of initiative, and beings who initiate "
            "activity are found, and because there is an observable element of energy, and "
            "beings who exert energy are found, sentient beings do act of their own volition or "
            "that of another &mdash; refuting the brahmin's doctrine that no one acts of their "
            "own or another's volition."]),
        ("A doctrine of radical fatalism", [
            "The brahmin's position, stated in a single sentence, denies volition entirely: not "
            "&ldquo;fate governs some things,&rdquo; but that action itself, in either "
            "direction &mdash; self-caused or other-caused &mdash; does not occur. This is a "
            "stronger claim than ordinary determinism; it denies that the category of "
            "&ldquo;acting&rdquo; meaningfully applies to anyone at all."]),
        ("An argument from observed capacity, not abstract logic", [
            "Rather than arguing philosophically about causation, the Buddha points to six "
            "specific, nameable capacities &mdash; <em>ārambhadhātu</em>, initiative; "
            "persistence; exertion; strength; endurance; <em>vīriyadhātu</em>, energy &mdash; "
            "and asks the brahmin directly whether each exists and whether beings who exercise "
            "each are found. The brahmin agrees to every step. The argument's force comes from "
            "getting the brahmin's own agreement to premises that, taken together, contradict "
            "his stated doctrine."]),
        ("A pointed, almost sarcastic rebuttal", [
            "The Buddha's framing &mdash; &ldquo;how on earth can someone who comes and goes on "
            "his own say that one does not act of one's own volition&rdquo; &mdash; notes the "
            "performative contradiction directly: the brahmin walked to the Buddha under his "
            "own power to state a doctrine denying that anyone acts under their own power. The "
            "refutation is not only logical but points out the doctrine undermines the very "
            "situation of stating it."]),
        ("A doctrinal debate ending in conversion", [
            "Unlike most of this chapter's discourses, this one ends with a specific outcome: "
            "the brahmin, persuaded, declares himself &ldquo;a lay follower who has gone for "
            "refuge for life.&rdquo; The discourse is framed as successful persuasion, not "
            "merely a teaching stated and left to stand on its own."]),
    ],
    terms=[
        ("attakāra parakāra",
         "&ldquo;one's own volition, another's volition&rdquo; &mdash; the two forms of agency "
         "the brahmin's doctrine denies and the Buddha's argument restores."),
        ("ārambhadhātu",
         "&ldquo;element of initiative&rdquo; &mdash; the first of six observable elements the "
         "Buddha uses as evidence."),
        ("vīriyadhātu",
         "&ldquo;element of energy&rdquo; &mdash; the sixth and final element named, closing "
         "the argument's second stage."),
        ("akiriyavāda",
         "not directly named in this translation but the standard canonical term for the "
         "&ldquo;doctrine of non-action&rdquo; the brahmin appears to be stating."),
        ("saraṇaṁ gata",
         "&ldquo;gone for refuge&rdquo; &mdash; the brahmin's closing declaration, converting "
         "the discourse's philosophical debate into a concrete outcome."),
    ],
    text_intro=(
        "The discourse in full: the brahmin's doctrine, the Buddha's refutation in two stages, "
        "and the brahmin's conversion. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A brahmin states his doctrine"),
        ("p", "&sect;1", "an6.38:1.1-1.7"),
        ("h3", "The first argument: initiative"),
        ("p", "&sect;2", "an6.38:2.1-2.5"),
        ("h3", "The second argument: energy, and the brahmin's conversion"),
        ("p", "&sect;3", "an6.38:3.1-5.2"),
    ],
    quiz=[
        {"q": "What doctrine does the brahmin state to the Buddha?",
         "opts": [
             "That karma determines everything precisely",
             "That one does not act of one's own volition, nor does one act of another's "
             "volition",
             "That the gods control all human action",
             "That volition exists but has no consequences"],
         "correct": 1,
         "expl": "A radical denial that the category of 'acting' meaningfully applies to anyone."},
        {"q": "How does the Buddha's response to this doctrine compare in tone to most of this "
              "chapter's material?",
         "opts": [
             "Mild and non-committal",
             "Unusually blunt: 'May I never see or hear of anyone holding such a doctrine or "
             "view!'",
             "The Buddha declines to respond at all",
             "He agrees with the brahmin immediately"],
         "correct": 1,
         "expl": "A sharper rejection than most of this chapter's discourses."},
        {"q": "What six elements does the Buddha use as evidence against the brahmin's "
              "doctrine?",
         "opts": [
             "Faith, energy, mindfulness, immersion, and wisdom",
             "Initiative, persistence, exertion, strength, endurance, and energy",
             "The five hindrances plus doubt",
             "Danger, suffering, disease, boil, chain, and bog"],
         "correct": 1,
         "expl": "Observable capacities the brahmin agrees exist, contradicting his own stated "
                 "doctrine."},
        {"q": "What method does the Buddha use to build his argument?",
         "opts": [
             "Abstract philosophical reasoning with no reference to observation",
             "Getting the brahmin's own agreement, step by step, to premises that together "
             "contradict his stated doctrine",
             "Citing scriptural authority alone",
             "Threatening the brahmin with consequences"],
         "correct": 1,
         "expl": "An argument built from the interlocutor's own admissions."},
        {"q": "What performative contradiction does the guide say the Buddha points out?",
         "opts": [
             "That the brahmin cannot read",
             "That the brahmin walked to the Buddha under his own power to state a doctrine "
             "denying anyone acts under their own power",
             "That the brahmin is lying about his own name",
             "That the brahmin has never met another brahmin"],
         "correct": 1,
         "expl": "'How on earth can someone who comes and goes on his own say that...'"},
        {"q": "How does this discourse end?",
         "opts": [
             "With the brahmin unpersuaded and leaving in anger",
             "With the brahmin declaring himself a lay follower who has gone for refuge for life",
             "With an unresolved debate",
             "With the Buddha changing his own position"],
         "correct": 1,
         "expl": "A specific outcome of successful persuasion, unlike most discourses in this "
                 "chapter."},
        {"q": "What does <em>ārambhadhātu</em> mean?",
         "opts": ["Element of energy", "Element of initiative", "Element of endurance", "Element of strength"],
         "correct": 1,
         "expl": "The first of the six elements named in the argument."},
        {"q": "Is a setting stated for AN 6.38?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula introducing the brahmin's approach."},
        {"q": "How strong a claim is the brahmin's doctrine, compared to ordinary determinism?",
         "opts": [
             "Weaker — it only claims some actions are predetermined",
             "Stronger — it denies that action itself, self-caused or other-caused, occurs at "
             "all, not merely that outcomes are predetermined",
             "Identical to ordinary determinism",
             "The discourse does not distinguish the two"],
         "correct": 1,
         "expl": "A radical denial of the category of acting altogether, not a claim about "
                 "predetermined outcomes."},
        {"q": "What does <em>vīriyadhātu</em> mean?",
         "opts": ["Element of initiative", "Element of energy", "Element of persistence", "Element of strength"],
         "correct": 1,
         "expl": "The sixth and final element, closing the second stage of the argument."},
    ],
    marginalia=[
        ("Six elements cited", [
            "initiative &middot; persistence",
            "exertion &middot; strength",
            "endurance &middot; energy",
        ]),
        ("The brahmin's claim", [
            "no one acts of their",
            "own or another's",
            "volition — denied outright",
        ]),
        ("A pointed rebuttal", [
            "he walked here himself",
            "to deny that anyone",
            "walks by their own power",
        ]),
        ("Cross-references", [
            "AN 6.37 &middot; previous, a gift's six factors",
            "AN 6.39 &middot; next, sources of deeds",
        ]),
    ],
    further=[
        '<a href="%s/an6.38/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.39.html">AN 6.39 &middot; Sources</a> &mdash; next, on what actually '
        "gives rise to deeds.",
        '<a href="an-6.37.html">AN 6.37 &middot; A Gift With Six Factors</a> &mdash; previous, '
        "a very different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.39 — Nidānasutta
# --------------------------------------------------------------------------- #
page(
    39, "Nidāna", "Sources",
    vagga=VAGGA_4,
    meta_title="AN 6.39 — Sources | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nidānasutta, which "
        "names two triads — greed/hate/delusion and contentment/love/understanding — as the "
        "six sources that give rise to deeds, each self-perpetuating and never producing its "
        "opposite. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched triads, each stated with an identical internal structure of "
                 "self-perpetuation and consequence"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The three unwholesome and three wholesome roots recur "
                              "throughout the Chinese Āgamas and Abhidharma literature as basic "
                              "categories of motivation; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; conceptually dense despite "
                       "its brevity, worth reading for its precise claim about self-"
                       "perpetuation"),
    ],
    why=(
        "AN 6.39 names not one six-item list but two three-item ones, placed back to back: "
        "greed, hate, and delusion as sources of harmful deeds, and contentment, love, and "
        "understanding as sources of skillful ones. This discourse belongs to the Sixes not "
        "because any single list within it has six members, but because six sources are named "
        "across the whole teaching &mdash; and its central claim is unusually precise: each "
        "source gives rise only to more of itself, never to its opposite."),
    guide=[
        ("The teaching in one sentence", [
            "Greed, hate, and delusion are three sources that give rise to deeds, and each "
            "gives rise only to more of itself &mdash; greed to greed, hate to hate, delusion "
            "to delusion &mdash; leading to bad rebirths; contentment, love, and understanding "
            "are three further sources, each likewise self-perpetuating, leading to good "
            "rebirths."]),
        ("A precise claim: no source produces its opposite", [
            "The discourse's exact wording deserves attention: &ldquo;greed doesn't give rise "
            "to contentment. Rather, greed just gives rise to greed.&rdquo; This is not simply "
            "saying greed is harmful; it is denying a specific alternative &mdash; that greed "
            "might, given enough of it, eventually produce its own antidote. The discourse "
            "rules this out explicitly for all three unwholesome roots and, symmetrically, for "
            "all three wholesome ones."]),
        ("Why this discourse belongs among the Sixes", [
            "Nothing in this discourse is itself a six-item list; it is two three-item lists, "
            "stated in parallel. Its place in this nipāta depends on the total count across "
            "both halves &mdash; six sources named altogether &mdash; matching how AN 6.18 and "
            "several other discourses in this collection are numbered by total item count "
            "rather than by any single enumerated six-fold structure within them."]),
        ("The three unwholesome roots, and their consequence", [
            "Greed (<em>lobha</em>), hate (<em>dosa</em>), and delusion (<em>moha</em>) are the "
            "canon's standard three unwholesome roots, here linked directly and exclusively to "
            "rebirth &ldquo;in hell, the animal realm, the ghost realm, or any other bad "
            "places.&rdquo; The discourse does not describe intermediate or mixed outcomes; the "
            "link from these three roots to bad rebirth is stated as direct and total."]),
        ("The three wholesome roots as their precise mirror", [
            "Contentment (<em>alobha</em>, non-greed), love (<em>adosa</em>, non-hate), and "
            "understanding (<em>amoha</em>, non-delusion) are stated in a perfectly mirrored "
            "structure &mdash; same self-perpetuation claim, same total exclusivity of "
            "consequence, now leading to &ldquo;gods, humans, or those in any other good "
            "places.&rdquo; The discourse's two halves are constructed as exact structural "
            "twins, differing only in which triad and which consequence is named."]),
    ],
    terms=[
        ("nidāna",
         "&ldquo;source,&rdquo; &ldquo;origin&rdquo; &mdash; the discourse's own title, naming "
         "what each of the six items is said to be, for deeds."),
        ("lobha, dosa, moha",
         "&ldquo;greed, hate, delusion&rdquo; &mdash; the canon's three standard unwholesome "
         "roots, named here as the first triad of sources."),
        ("alobha, adosa, amoha",
         "&ldquo;non-greed, non-hate, non-delusion&rdquo; (rendered here as contentment, love, "
         "and understanding) &mdash; the three wholesome roots, mirroring the first triad "
         "exactly."),
        ("kamma",
         "&ldquo;deed,&rdquo; &ldquo;action&rdquo; &mdash; what all six sources are said to "
         "give rise to, whether harmful or skillful."),
        ("sugati duggati",
         "&ldquo;good place, bad place&rdquo; &mdash; the two categories of rebirth-destination "
         "the discourse links exclusively to the two respective triads."),
    ],
    text_intro=(
        "The discourse in full: the three unwholesome sources and the three wholesome sources, "
        "each self-perpetuating. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The three unwholesome sources"),
        ("p", "&sect;1", "an6.39:1.1-1.12"),
        ("h3", "The three wholesome sources"),
        ("p", "&sect;2", "an6.39:2.1-2.12"),
    ],
    quiz=[
        {"q": "How many item-lists does AN 6.39 actually contain, and how does it still belong "
              "to the Sixes?",
         "opts": [
             "One list of six items",
             "Two three-item lists, placed in parallel — its place among the Sixes depends on "
             "the total count across both halves, six sources named altogether",
             "Six separate discourses combined",
             "It does not belong among the Sixes at all"],
         "correct": 1,
         "expl": "Numbered by total item count, like several other discourses in this "
                 "collection."},
        {"q": "What precise claim does the discourse make about each source?",
         "opts": [
             "That each source eventually produces its opposite if pursued long enough",
             "That each source gives rise only to more of itself — greed to greed, hate to "
             "hate — never to its opposite",
             "That all six sources produce identical outcomes",
             "That sources have no lasting effect on future deeds"],
         "correct": 1,
         "expl": "A specific denial that greed might eventually produce contentment, or hate "
                 "produce love."},
        {"q": "What are the three unwholesome sources?",
         "opts": [
             "Contentment, love, and understanding",
             "Greed, hate, and delusion",
             "Danger, suffering, and disease",
             "Work, talk, and sleep"],
         "correct": 1,
         "expl": "The canon's standard three unwholesome roots (lobha, dosa, moha)."},
        {"q": "What are the three wholesome sources, and how do they relate structurally to "
              "the unwholesome triad?",
         "opts": [
             "Contentment, love, and understanding — exact structural twins of the unwholesome "
             "triad, differing only in which triad and consequence is named",
             "An entirely different and unrelated set of qualities",
             "The five faculties plus liberation",
             "They are not actually named in this discourse"],
         "correct": 0,
         "expl": "Alobha, adosa, amoha — a perfectly mirrored structure."},
        {"q": "What consequence does the discourse link to deeds born of greed, hate, and "
              "delusion?",
         "opts": [
             "A mixed outcome depending on circumstances",
             "Rebirth in hell, the animal realm, the ghost realm, or other bad places — stated "
             "as direct and total, with no intermediate outcomes described",
             "No consequence at all",
             "Rebirth as a deity"],
         "correct": 1,
         "expl": "An exclusive link, not a probabilistic or partial one."},
        {"q": "What does <em>nidāna</em> mean?",
         "opts": ["Consequence", "Source, origin", "Deed", "Rebirth"],
         "correct": 1,
         "expl": "The discourse's own title, applied to all six items across both triads."},
        {"q": "Is a setting stated for AN 6.39?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula stating both triads directly."},
        {"q": "What does the discourse say greed gives rise to?",
         "opts": [
             "Contentment, eventually",
             "Only more greed, never contentment",
             "Understanding",
             "Nothing at all"],
         "correct": 1,
         "expl": "The discourse's precise self-perpetuation claim, stated explicitly."},
        {"q": "What does <em>amoha</em> mean?",
         "opts": ["Delusion", "Non-delusion, understanding", "Hate", "Greed"],
         "correct": 1,
         "expl": "The third item of the wholesome triad, rendered here as 'understanding'."},
        {"q": "How are the two halves of this discourse related to each other, according to "
              "the guide?",
         "opts": [
             "Entirely unrelated content",
             "Constructed as exact structural twins — the same claim of self-perpetuation and "
             "total exclusivity of consequence, differing only in triad and outcome",
             "The second half contradicts the first",
             "Only the first half is doctrinally significant"],
         "correct": 1,
         "expl": "A deliberate mirrored structure across the whole discourse."},
    ],
    marginalia=[
        ("Two triads, six sources", [
            "greed &middot; hate &middot; delusion",
            "contentment &middot; love",
            "&middot; understanding",
        ]),
        ("Self-perpetuating", [
            "each gives rise only",
            "to more of itself —",
            "never to its opposite",
        ]),
        ("Exclusive consequence", [
            "unwholesome &rarr; bad rebirth",
            "wholesome &rarr; good rebirth",
            "no stated middle ground",
        ]),
        ("Cross-references", [
            "AN 6.38 &middot; previous, on volition",
            "AN 6.40 &middot; next, With Kimbila",
        ]),
    ],
    further=[
        '<a href="%s/an6.39/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.40.html">AN 6.40 &middot; With Kimbila</a> &mdash; next, on what keeps '
        "the teaching itself alive.",
        '<a href="an-6.38.html">AN 6.38 &middot; One&rsquo;s Own Volition</a> &mdash; previous, '
        "a debate on agency and action.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.40 — Kimilasutta
# --------------------------------------------------------------------------- #
page(
    40, "Kimila", "With Kimbila",
    vagga=VAGGA_4,
    meta_title="AN 6.40 — With Kimbila | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kimilasutta, where "
        "Venerable Kimbila asks why the true teaching does or doesn't last long after a "
        "Buddha's passing, and the answer names respect among all four assemblies. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Near Kimbilā, in the Freshwater Mangrove Wood"),
        ("Speakers", "Venerable Kimbila, questioning the Buddha"),
        ("Form", "Two paired questions and answers, using the identical six-item structure "
                 "already met at AN 6.32"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Reflections on what preserves a teaching's longevity after its "
                              "founder's passing recur across the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short dialogue reusing a "
                       "structure this series has already encountered once"),
    ],
    why=(
        "Kimbila asks a question with real stakes: why does the true teaching sometimes fail "
        "to last long after a Buddha's final passing, and what makes it last? The Buddha's "
        "answer names the identical six items already met at AN 6.32 &mdash; respect for the "
        "Teacher, the teaching, the Saṅgha, the training, diligence, and hospitality &mdash; "
        "but now applied across all four assemblies of the tradition, not mendicants alone, and "
        "tied directly to the teaching's institutional survival rather than one individual's "
        "decline."),
    guide=[
        ("The teaching in one sentence", [
            "The true teaching fails to last long after a Buddha's final passing when monks, "
            "nuns, laymen, and laywomen lack respect for the Teacher, the teaching, the Saṅgha, "
            "the training, diligence, and hospitality; it lasts long when all four assemblies "
            "maintain that respect."]),
        ("The same six items, checked directly, applied to a new scope", [
            "Compared word for word against AN 6.32's list &mdash; respect for the Teacher, the "
            "teaching, the Saṅgha, the training, diligence, hospitality &mdash; this discourse "
            "names the identical six. What changes is not the content but its scope: AN 6.32 "
            "concerned one mendicant's decline, while this discourse concerns whether &ldquo;the "
            "true teaching&rdquo; itself endures, and specifies all four assemblies &mdash; "
            "monks, nuns, laymen, laywomen &mdash; rather than mendicants alone."]),
        ("Kimbila's question, and why it matters", [
            "The question &ldquo;what is the cause, what is the reason why the true teaching "
            "does not last long&rdquo; is asked about events after &ldquo;the final quenching "
            "of the Realized One&rdquo; &mdash; a question about the tradition's own long-term "
            "future, not about any single practitioner's present conduct. Framing the answer "
            "around respect held by the whole community, not any one figure's authority, "
            "locates the teaching's survival in a distributed responsibility rather than "
            "reliance on any single leader after the Buddha's death."]),
        ("Symmetry as the whole answer", [
            "As at AN 6.31 and several other discourses in this chapter, the answer to "
            "&ldquo;what causes decline&rdquo; and &ldquo;what prevents it&rdquo; is a single "
            "list stated twice, once negated and once affirmed. No further elaboration is "
            "offered on how respect is cultivated or what erodes it; the discourse trusts the "
            "list itself to carry the weight of the answer."]),
        ("Kimbila as a minor but recurring figure", [
            "Kimbila, the discourse's named questioner, gives this text and its setting &mdash; "
            "near the town of Kimbilā, in the Freshwater Mangrove Wood &mdash; their specific "
            "identity. He appears elsewhere in the canon as a companion of several senior "
            "disciples; here his single recorded question concerns nothing less than the "
            "teaching's own institutional future."]),
    ],
    terms=[
        ("saddhamma",
         "&ldquo;the true teaching&rdquo; &mdash; what Kimbila asks about the longevity of, "
         "after the Buddha's final passing."),
        ("parinibbāna",
         "&ldquo;final quenching,&rdquo; &ldquo;final passing&rdquo; &mdash; the event after "
         "which the teaching's survival becomes uncertain, per Kimbila's question."),
        ("bhikkhu bhikkhunī upāsaka upāsikā",
         "&ldquo;monks, nuns, laymen, laywomen&rdquo; &mdash; the four assemblies this "
         "discourse addresses together, unlike AN 6.32's mendicant-only scope."),
        ("gārava",
         "&ldquo;respect&rdquo; &mdash; unchanged in content from AN 6.32, now scoped to the "
         "whole fourfold community."),
        ("ciraṭṭhitika",
         "&ldquo;lasting long,&rdquo; &ldquo;enduring&rdquo; &mdash; the quality of the "
         "teaching Kimbila's question concerns."),
    ],
    text_intro=(
        "The discourse in full: Kimbila's two questions, and the Buddha's paired answers. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Why the teaching fails to last long"),
        ("p", "&sect;1", "an6.40:1.1-1.6"),
        ("h3", "Why the teaching lasts long"),
        ("p", "&sect;2", "an6.40:2.1-2.3"),
    ],
    quiz=[
        {"q": "What question does Kimbila ask the Buddha?",
         "opts": [
             "How to develop psychic power",
             "What causes the true teaching to fail to last long, or to last long, after a "
             "Buddha's final passing",
             "How many topics for recollection there are",
             "Why senior mendicants sometimes sleep too much"],
         "correct": 1,
         "expl": "A question about the tradition's own long-term institutional future."},
        {"q": "How does this discourse's six-item list compare to AN 6.32's, checked directly?",
         "opts": [
             "Entirely different content",
             "Identical: respect for the Teacher, the teaching, the Saṅgha, the training, "
             "diligence, and hospitality",
             "Four items match, two differ, as with AN 6.33",
             "Only two items match"],
         "correct": 1,
         "expl": "The same six items, word for word, applied to a broader scope."},
        {"q": "What changes between AN 6.32 and this discourse, if the content is identical?",
         "opts": [
             "Nothing changes at all",
             "The scope — AN 6.32 concerned one mendicant's decline; this discourse concerns "
             "whether the whole teaching endures, across all four assemblies rather than "
             "mendicants alone",
             "The speaker changes from the Buddha to Kimbila",
             "The setting changes to Jeta's Grove"],
         "correct": 1,
         "expl": "Same six qualities, applied at the scale of the entire tradition's survival."},
        {"q": "What are the four assemblies named in this discourse?",
         "opts": [
             "Kings, brahmins, merchants, and farmers",
             "Monks, nuns, laymen, and laywomen",
             "Senior, junior, ordained, and lay",
             "Buddha, teaching, Saṅgha, and training"],
         "correct": 1,
         "expl": "The whole fourfold community, not mendicants alone."},
        {"q": "What does locating the answer in the whole community's respect, rather than any "
              "single leader, suggest, according to the guide?",
         "opts": [
             "That leadership after the Buddha's death is irrelevant",
             "A distributed responsibility for the teaching's survival, rather than reliance on "
             "any single figure after the Buddha's passing",
             "That the teaching cannot actually survive without the Buddha present",
             "That only monks bear responsibility for the teaching's survival"],
         "correct": 1,
         "expl": "Responsibility spread across all four assemblies, not concentrated in one role."},
        {"q": "Where is AN 6.40 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Near Kimbilā, in the Freshwater Mangrove Wood",
             "Rājagaha, on Vulture's Peak",
             "Icchānaṅgala"],
         "correct": 1,
         "expl": "A location tied to the discourse's named questioner, Kimbila."},
        {"q": "What does <em>saddhamma</em> mean?",
         "opts": ["A type of meditation", "The true teaching", "A monastic robe", "A ritual "
                  "offering"],
         "correct": 1,
         "expl": "What Kimbila's question concerns the longevity of."},
        {"q": "What does <em>parinibbāna</em> refer to?",
         "opts": [
             "A meditative attainment during life",
             "The Buddha's final passing, the event after which the teaching's survival becomes "
             "uncertain",
             "A type of psychic power",
             "The ordination of a new mendicant"],
         "correct": 1,
         "expl": "The temporal marker Kimbila's question is framed around."},
        {"q": "How is the answer structured, according to the guide?",
         "opts": [
             "As an extended philosophical argument",
             "As a single list stated twice, once negated and once affirmed, with no further "
             "elaboration — the same pattern already met at AN 6.31",
             "As a narrative involving multiple characters",
             "As a series of similes"],
         "correct": 1,
         "expl": "Trusting the list itself to carry the weight of the answer."},
        {"q": "Who is Kimbila, according to the guide?",
         "opts": [
             "A deity who visits the Buddha at night",
             "A named questioner who appears elsewhere in the canon as a companion of several "
             "senior disciples",
             "A brahmin hostile to the teaching",
             "A king ruling over the region"],
         "correct": 1,
         "expl": "A minor but recurring figure, giving this discourse its specific setting and "
                 "identity."},
    ],
    marginalia=[
        ("Same six items", [
            "as AN 6.32 —",
            "Teacher, teaching, Saṅgha,",
            "training, diligence,",
            "hospitality",
        ]),
        ("Wider scope", [
            "not one mendicant —",
            "all four assemblies:",
            "monks, nuns, laymen, laywomen",
        ]),
        ("The real stakes", [
            "not personal decline —",
            "the teaching's own",
            "survival after death",
        ]),
        ("Cross-references", [
            "AN 6.32 &middot; the identical six items",
        ]),
    ],
    further=[
        '<a href="%s/an6.40/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.41.html">AN 6.41 &middot; A Tree Trunk</a> &mdash; next, Sāriputta on the '
        "elements a psychic mind can determine.",
        '<a href="an-6.39.html">AN 6.39 &middot; Sources</a> &mdash; previous, on what gives '
        "rise to deeds.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.41 — Dārukkhandhasutta
# --------------------------------------------------------------------------- #
page(
    41, "Dārukkhandha", "A Tree Trunk",
    vagga=VAGGA_4,
    meta_title="AN 6.41 — A Tree Trunk | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dārukkhandhasutta, "
        "where Sāriputta uses a large tree trunk to illustrate the six things a mendicant with "
        "mastery of mind and psychic power could determine it to be. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Descending Vulture's Peak, near Rājagaha"),
        ("Speakers", "Sāriputta, addressing mendicants traveling with him"),
        ("Form", "A single observed object, and six parallel hypothetical determinations, each "
                 "with its own stated reason"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Element-determination through mastery of mind recurs in related "
                              "meditative literature across the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, but resting on a "
                       "distinctive and easily missed doctrinal point about what psychic power "
                       "actually does"),
    ],
    why=(
        "Descending from Vulture's Peak with a group of mendicants, Sāriputta stops at an "
        "ordinary large tree trunk and uses it to make a precise point: a mendicant with "
        "&ldquo;psychic powers who has mastered their mind&rdquo; could determine this same "
        "object to be nothing but earth, water, fire, air, beautiful, or ugly &mdash; not "
        "because the tree trunk actually transforms, but because each of these elements or "
        "qualities genuinely exists within it already, available to be brought forward by a "
        "sufficiently mastered mind."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant with psychic power who has mastered their mind could determine a large "
            "tree trunk to be nothing but earth, water, fire, air, beautiful, or ugly, because "
            "each of these elements genuinely exists within the tree trunk already."]),
        ("Six determinations, four elements and two qualities", [
            "The list is not uniform in kind: the first four items &mdash; earth, water, fire, "
            "air &mdash; are the canon's standard four elements (<em>mahābhūta</em>), while the "
            "final two &mdash; beautiful and ugly &mdash; are aesthetic qualities, not physical "
            "elements at all. Sāriputta's list moves from a familiar physical framework to a "
            "less expected extension of the same logic into perceived qualities."]),
        ("The stated reason, repeated for each item", [
            "For every one of the six determinations, Sāriputta gives an identical form of "
            "reason: &ldquo;because the [X] element exists in the tree trunk.&rdquo; This is "
            "the discourse's real point and easily missed if read quickly: the mendicant is not "
            "described as creating or imagining these qualities, only as bringing forward, "
            "through mastery, an element already genuinely present. Water exists latently in "
            "the tree trunk as much as earth does; the psychic determination reveals rather "
            "than invents."]),
        ("What 'mastery of mind' is doing here", [
            "The discourse names a specific precondition &mdash; <em>cetovasippatta</em>, "
            "having attained mastery over the mind &mdash; as what makes this kind of "
            "determination possible. The tree trunk itself does not change; what changes is the "
            "meditator's capacity to selectively bring one genuinely present element to the "
            "foreground of perception, a capacity dependent on the meditator's training rather "
            "than any special property of the object chosen."]),
        ("Ugliness as an element, not merely a judgment", [
            "The final item is the discourse's most striking claim: that ugliness "
            "(<em>asubha</em>) is itself an &ldquo;element&rdquo; present in the tree trunk, "
            "alongside earth, water, fire, and air, rather than simply a subjective response a "
            "viewer might have. This treats an aesthetic quality with the same ontological "
            "standing as a physical element &mdash; genuinely there to be perceived, not merely "
            "projected by the perceiver."]),
    ],
    terms=[
        ("cetovasippatta",
         "&ldquo;having attained mastery of mind&rdquo; &mdash; the discourse's stated "
         "precondition for making any of the six determinations."),
        ("iddhimā",
         "&ldquo;possessing psychic power&rdquo; &mdash; paired with mastery of mind as the "
         "capacity this discourse's mendicant has."),
        ("mahābhūta",
         "&ldquo;great element&rdquo; &mdash; the standard canonical term for earth, water, "
         "fire, and air, the first four of this discourse's six determinations."),
        ("pathavīdhātu",
         "&ldquo;earth element&rdquo; &mdash; the first determination named, and the discourse's "
         "template for how each of the six is explained."),
        ("subhaṁ...asubhaṁ",
         "&ldquo;beautiful...ugly&rdquo; &mdash; the fifth and sixth determinations, extending "
         "the element-framework from physical matter to aesthetic quality."),
    ],
    text_intro=(
        "The discourse in full: the tree trunk, and the six things a mind-mastering mendicant "
        "could determine it to be. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A large tree trunk, on the way down from Vulture's Peak"),
        ("p", "&sect;1", "an6.41:1.1-1.6"),
        ("h3", "Six things it could be determined to be"),
        ("p", "&sect;2", "an6.41:2.1-2.10"),
    ],
    quiz=[
        {"q": "What object prompts this discourse?",
         "opts": [
             "A river", "A large tree trunk, seen while descending Vulture's Peak", "A mountain "
             "cave", "A clay pot"],
         "correct": 1,
         "expl": "An ordinary object used to make a precise doctrinal point."},
        {"q": "What six things does Sāriputta say a mind-mastering mendicant could determine "
              "the tree trunk to be?",
         "opts": [
             "Six different colors",
             "Earth, water, fire, air, beautiful, and ugly",
             "The six sense doors",
             "Six different sizes"],
         "correct": 1,
         "expl": "Four standard elements plus two aesthetic qualities."},
        {"q": "What reason does Sāriputta give, in an identical form, for each of the six "
              "determinations?",
         "opts": [
             "Because the mendicant imagines it to be so",
             "Because that element genuinely exists in the tree trunk already — the "
             "determination reveals rather than invents",
             "Because the tree trunk physically transforms",
             "No reason is given for any of the six"],
         "correct": 1,
         "expl": "'Because the [X] element exists in the tree trunk' — the discourse's central, "
                 "easily missed point."},
        {"q": "What precondition does the discourse name as necessary for making these "
              "determinations?",
         "opts": [
             "Advanced age", "Mastery of mind (cetovasippatta) and possession of psychic power", "Physical strength", "Formal ordination"],
         "correct": 1,
         "expl": "A capacity dependent on training, not a special property of the object chosen."},
        {"q": "How does the guide describe the shift from the first four items to the final "
              "two?",
         "opts": [
             "No shift — all six are identical in kind",
             "From the four standard physical elements to two aesthetic qualities, beautiful "
             "and ugly, extending the same logic into perceived quality",
             "From aesthetic qualities to physical elements",
             "The final two items are not actually part of the same list"],
         "correct": 1,
         "expl": "A notable extension of the element-framework beyond physical matter."},
        {"q": "What claim does the guide highlight as the discourse's most striking?",
         "opts": [
             "That the tree trunk is not really there at all",
             "That ugliness is itself treated as an 'element' genuinely present in the object, "
             "not merely a subjective judgment projected by the viewer",
             "That psychic power is impossible to develop",
             "That mendicants should avoid large trees"],
         "correct": 1,
         "expl": "Treating an aesthetic quality with the same ontological standing as a physical "
                 "element."},
        {"q": "Where is AN 6.41 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Near Rājagaha, descending Vulture's Peak",
             "Near Kimbilā",
             "Icchānaṅgala"],
         "correct": 1,
         "expl": "A specific location tied to Sāriputta's own dwelling place in this discourse."},
        {"q": "Who speaks AN 6.41?",
         "opts": ["The Buddha", "Sāriputta, addressing mendicants traveling with him", "Mahākaccāna", "A deity"],
         "correct": 1,
         "expl": "One of the chapter's discourses spoken by a senior disciple rather than the "
                 "Buddha."},
        {"q": "What does <em>mahābhūta</em> mean?",
         "opts": ["Small element", "Great element — the standard term for earth, water, fire, "
                  "and air", "A type of deity", "A meditative absorption"],
         "correct": 1,
         "expl": "The canonical category the first four of this discourse's six items belong to."},
        {"q": "Does the tree trunk itself change, according to the discourse's logic?",
         "opts": [
             "Yes, it physically transforms into each element in turn",
             "No — what changes is the meditator's capacity to selectively bring forward an "
             "already-present element, not any property of the tree trunk",
             "The discourse does not address this question",
             "Yes, but only temporarily"],
         "correct": 1,
         "expl": "The object stays the same; the mastered mind determines which genuinely "
                 "present element to foreground."},
    ],
    marginalia=[
        ("Six determinations", [
            "earth &middot; water",
            "fire &middot; air",
            "beautiful &middot; ugly",
        ]),
        ("The stated reason", [
            "each element genuinely",
            "exists in the trunk —",
            "revealed, not invented",
        ]),
        ("Precondition", [
            "mastery of mind",
            "+ psychic power —",
            "a trained capacity",
        ]),
        ("Cross-references", [
            "AN 6.2 &middot; the six superhuman knowledges",
        ]),
    ],
    further=[
        '<a href="%s/an6.41/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.42.html">AN 6.42 &middot; With Nāgita</a> &mdash; next, closing the '
        "chapter with the Buddha's own reflections on fame and solitude.",
        '<a href="an-6.40.html">AN 6.40 &middot; With Kimbila</a> &mdash; previous, on the '
        "teaching's institutional survival.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.42 — Nāgitasutta
# --------------------------------------------------------------------------- #
page(
    42, "Nāgita", "With Nāgita",
    vagga=VAGGA_4,
    meta_title="AN 6.42 — With Nāgita | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nāgitasutta, closing "
        "the chapter with the Buddha refusing a crowd's noisy devotion, wishing never to "
        "become famous, and explaining in six scenarios why he favors wilderness dwelling. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "A forest near Icchānaṅgala, a village of Kosalan brahmins"),
        ("Speakers", "The Buddha, speaking to his attendant, Venerable Nāgita"),
        ("Form", "A noisy crowd, a rejected plea for the Buddha to relent, and six paired "
                 "scenarios contrasting village and wilderness dwelling"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The Buddha's preference for solitude over popularity recurs in "
                              "related episodes across the Chinese Āgamas; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a vivid, personal narrative "
                       "closing the chapter on a memorably blunt refrain"),
    ],
    why=(
        "A crowd of brahmins and householders arrives outside the Buddha's forest dwelling "
        "before dawn, making, in his own words, &ldquo;a colossal racket&rdquo; like "
        "&ldquo;fishermen hauling in a catch,&rdquo; eager to offer food. When his attendant "
        "Nāgita urges him to relent and accept their devotion, the Buddha refuses twice, with "
        "the same blunt line both times: &ldquo;May I never become famous. May fame not come "
        "to me.&rdquo; What follows is his own explanation, in six paired scenarios, of "
        "exactly why he values wilderness dwelling over the comforts a devoted following would "
        "bring."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha refuses the noisy devotion of a crowd bringing food, declaring he never "
            "wants fame, and explains through six contrasted scenarios of mendicants living in "
            "villages versus the wilderness why solitude protects meditative progress that "
            "popularity and comfort would put at risk."]),
        ("A scene with real, physical noise", [
            "The discourse opens on something unusually sensory for this collection: a crowd "
            "&ldquo;standing outside the gates making a colossal racket,&rdquo; compared "
            "directly by the Buddha to fishermen hauling in a catch. The comparison is not "
            "flattering &mdash; it likens eager devotional enthusiasm to the noise of a "
            "commercial catch being landed, not to reverent quiet."]),
        ("A refrain repeated exactly, twice", [
            "Nāgita's plea that &ldquo;now is the time for the Buddha to relent&rdquo; is met "
            "both times with the identical response, word for word: &ldquo;Nāgita, may I never "
            "become famous. May fame not come to me&hellip; Let them enjoy the filthy, lazy "
            "pleasure of possessions, honor, and popularity.&rdquo; The repetition itself makes "
            "the point &mdash; this is not a momentary reaction but a settled, restated "
            "position."]),
        ("Six scenarios, weighing samādhi against comfort", [
            "The Buddha's explanation takes the form of six paired observations: a "
            "village-dwelling mendicant already immersed in samādhi risks being disturbed by "
            "&ldquo;a monastery worker, a novice, or a fellow practitioner&rdquo; and so "
            "displeases him; a wilderness-dwelling mendicant nodding off in meditation will "
            "likely refocus and so pleases him; one not yet immersed will likely become "
            "immersed; one already immersed will likely preserve it; a village-dwelling "
            "mendicant absorbed in receiving requisites neglects retreat and displeases him; a "
            "wilderness-dwelling mendicant who fends off the same requisites does not neglect "
            "retreat and pleases him. In every pairing, the wilderness side is favored, and the "
            "reasoning concerns risk to meditative continuity, not location for its own sake."]),
        ("A closing image of plain relief", [
            "The discourse's final line drops the formal argument entirely for something almost "
            "domestic: &ldquo;when I'm walking along a road and I don't see anyone ahead or "
            "behind I feel relaxed, even if I need to urinate or defecate.&rdquo; Closing on "
            "this plain, physical detail rather than a doctrinal summary is unusual in this "
            "collection, and it grounds the whole discourse's argument about fame and solitude "
            "in something almost anticlimactically ordinary."]),
    ],
    terms=[
        ("kittisadda",
         "&ldquo;fame,&rdquo; &ldquo;reputation&rdquo; &mdash; what the Buddha twice declares "
         "he never wants."),
        ("nekkhammasukha pavivekasukha upasamasukha sambodhisukha",
         "&ldquo;the pleasure of renunciation, seclusion, peace, and awakening&rdquo; &mdash; "
         "the four pleasures the Buddha says he can access at will, without trouble, contrasted "
         "with fame's &ldquo;filthy, lazy pleasure.&rdquo;"),
        ("araññaka",
         "&ldquo;wilderness-dwelling,&rdquo; &ldquo;forest-dwelling&rdquo; &mdash; the kind of "
         "mendicant favored in all six of the discourse's paired scenarios."),
        ("lābhasakkārasiloka",
         "&ldquo;possessions, honor, and popularity&rdquo; &mdash; the three things the Buddha "
         "says those who cannot access his four pleasures are welcome to enjoy instead."),
        ("attānudayatā",
         "not directly named in this English translation but the sense underlying the closing "
         "image: a plain, personal relief at simple, unwitnessed solitude on the road."),
    ],
    text_intro=(
        "The discourse in full: the crowd's arrival, the Buddha's refusal, and his six "
        "scenarios explaining wilderness dwelling. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A crowd arrives at Icchānaṅgala"),
        ("p", "&sect;1", "an6.42:1.1-2.4"),
        ("h3", "The Buddha's first refusal"),
        ("p", "&sect;2", "an6.42:2.5-3.7"),
        ("h3", "The second refusal, and six scenarios"),
        ("p", "&sect;3", "an6.42:4.1-10.3"),
        ("h3", "The closing image"),
        ("p", "&sect;4", "an6.42:11.1"),
    ],
    quiz=[
        {"q": "What does the Buddha compare the crowd's noise to?",
         "opts": [
             "A festival celebration", "Fishermen hauling in a catch", "A thunderstorm", "A "
             "battle"],
         "correct": 1,
         "expl": "A pointedly unflattering comparison for eager devotional enthusiasm."},
        {"q": "What does the Buddha say, word for word, both times Nāgita urges him to relent?",
         "opts": [
             "'I will consider it carefully'",
             "'May I never become famous. May fame not come to me'",
             "'Send the crowd away immediately'",
             "'Nāgita, you decide for me'"],
         "correct": 1,
         "expl": "An identical refrain repeated twice, underscoring a settled position."},
        {"q": "What four pleasures does the Buddha say he can access at will, without trouble?",
         "opts": [
             "Wealth, fame, comfort, and status",
             "Renunciation, seclusion, peace, and awakening",
             "Food, sleep, company, and conversation",
             "Praise, honor, popularity, and possessions"],
         "correct": 1,
         "expl": "Contrasted directly with the 'filthy, lazy pleasure' of fame and possessions."},
        {"q": "In the six paired scenarios, which side does the Buddha consistently favor?",
         "opts": [
             "Village dwelling in every case",
             "Wilderness dwelling in every case — the reasoning concerns risk to meditative "
             "continuity, not location for its own sake",
             "Neither is favored; both are equally acceptable",
             "It varies scenario by scenario"],
         "correct": 1,
         "expl": "Village dwelling risks disturbance to samādhi and distraction by requisites; "
                 "wilderness dwelling protects both."},
        {"q": "Why does a village-dwelling mendicant already immersed in samādhi displease the "
              "Buddha, in the first scenario?",
         "opts": [
             "Because samādhi itself is undesirable",
             "Because a monastery worker, novice, or fellow practitioner risks making that "
             "mendicant fall from immersion",
             "Because village dwelling is forbidden by monastic rule",
             "Because the mendicant is not skilled enough"],
         "correct": 1,
         "expl": "A risk of disturbance specific to the village setting, not a judgment on the "
                 "meditator's skill."},
        {"q": "How does the discourse end?",
         "opts": [
             "With a formal doctrinal summary",
             "With a plain, physical image: feeling relaxed on an empty road, even needing to "
             "urinate or defecate",
             "With the crowd being turned away by force",
             "With a closing verse in praise of fame"],
         "correct": 1,
         "expl": "An unusually ordinary, anticlimactic close for this collection."},
        {"q": "Where is AN 6.42 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "A forest near Icchānaṅgala, a village of Kosalan brahmins",
             "Near Rājagaha, on Vulture's Peak",
             "Near Kimbilā"],
         "correct": 1,
         "expl": "A location reached while the Buddha was wandering with a large Saṅgha among "
                 "the Kosalans."},
        {"q": "Who is Nāgita?",
         "opts": [
             "A hostile brahmin", "The Buddha's attendant at the time of this discourse", "A "
             "deity", "A lay donor"],
         "correct": 1,
         "expl": "The discourse's named interlocutor, urging the Buddha to accept the crowd's "
                 "devotion."},
        {"q": "What does <em>lābhasakkārasiloka</em> mean?",
         "opts": [
             "Renunciation, seclusion, and peace",
             "Possessions, honor, and popularity",
             "Ethics, immersion, and wisdom",
             "Work, talk, and sleep"],
         "correct": 1,
         "expl": "What the Buddha says those unable to access his four pleasures are welcome to "
                 "enjoy instead."},
        {"q": "What consistent reasoning underlies all six of the Buddha's paired scenarios?",
         "opts": [
             "A general dislike of villages as places",
             "Protecting meditative continuity and progress from disturbance, distraction, and "
             "the pull of requisites and popularity",
             "A rule requiring all mendicants to live in forests",
             "A concern about food scarcity in villages"],
         "correct": 1,
         "expl": "Risk assessment focused on samādhi and retreat, not a blanket preference for "
                 "wilderness for its own sake."},
    ],
    marginalia=[
        ("The refused crowd", [
            "'a colossal racket' —",
            "like fishermen",
            "hauling in a catch",
        ]),
        ("Four pleasures", [
            "renunciation &middot; seclusion",
            "peace &middot; awakening —",
            "accessed without trouble",
        ]),
        ("Six scenarios", [
            "village vs. wilderness —",
            "samādhi's continuity",
            "weighed each time",
        ]),
        ("A plain closing image", [
            "no one ahead or behind",
            "on an empty road —",
            "simple, physical relief",
        ]),
    ],
    further=[
        '<a href="%s/an6.42/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.41.html">AN 6.41 &middot; A Tree Trunk</a> &mdash; previous, a different '
        "register of teaching from Sāriputta.",
        '<a href="an-6.31.html">AN 6.31 &middot; A Trainee</a> &mdash; this '
        "chapter&rsquo;s opening, for contrast with where it closes.",
    ],
)


# --------------------------------------------------------------------------- #
# Chapter 5 — Dhammikavagga (AN 6.43–54)
# --------------------------------------------------------------------------- #
VAGGA_5 = "<em>Dhammikavagga</em> &mdash; the fifth chapter of the Sixes"


# --------------------------------------------------------------------------- #
# AN 6.43 — Nāgasutta
# --------------------------------------------------------------------------- #
page(
    43, "Nāga", "The Giant",
    vagga=VAGGA_5,
    meta_title="AN 6.43 — The Giant | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nāgasutta, opening "
        "the Sixes' fifth chapter as King Pasenadi's bull elephant prompts a redefinition of "
        "'giant' and an extended verse praising the Buddha as the true nāga. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, at the eastern gate, after bathing at the Eastern Monastery"),
        ("Speakers", "Venerable Udāyī, questioning the Buddha; then Udāyī's own celebratory "
                     "verses"),
        ("Form", "A witnessed public spectacle, a question, a redefinition, and an extended "
                 "verse elaboration"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The elephant as a figure for the awakened one recurs widely "
                              "across the Chinese Āgamas and later Buddhist art and literature; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; an accessible narrative "
                       "opening onto an unusually long and image-dense verse passage"),
    ],
    why=(
        "A royal elephant emerges through Sāvatthī's eastern gate to fanfare, and the crowd's "
        "admiring cry &mdash; &ldquo;a giant, such a giant!&rdquo; &mdash; prompts Udāyī to ask "
        "whether the word applies only to elephants or to any creature of huge, formidable "
        "body. The Buddha's answer redirects the whole category: a &ldquo;giant&rdquo; in his "
        "sense is not a matter of physical size at all, but &ldquo;one who does nothing "
        "monstrous by way of body, speech, and mind.&rdquo; Udāyī's response is not a question "
        "but an extended celebratory verse, working out the redefined image point by point "
        "across a real elephant's anatomy."),
    guide=[
        ("The teaching in one sentence", [
            "Whatever creature's huge body prompts people to call it a &lsquo;giant&rsquo; "
            "&mdash; elephant, horse, bull, serpent, tree, or human &mdash; the Buddha redefines "
            "the term entirely: the true giant is one who does nothing monstrous by way of "
            "body, speech, and mind."]),
        ("A word stretched across many bodies, then redirected", [
            "Udāyī's question establishes that <em>nāga</em>, giant, already applies broadly "
            "&mdash; to elephants, horses, bulls, serpents, even large trees and unusually "
            "large humans &mdash; before the Buddha's answer. The redefinition that follows "
            "does not narrow the term to a single new referent but shifts its basis entirely, "
            "from physical scale to moral conduct, so that a person of ordinary or even small "
            "stature can be a &ldquo;giant&rdquo; while an elephant, on this new criterion, "
            "cannot."]),
        ("Udāyī's celebration as commentary in verse", [
            "Unusually for this collection, the discourse's real weight falls not on the "
            "Buddha's own words but on what follows them: Udāyī, moved to declare the teaching "
            "&ldquo;incredible&hellip; amazing,&rdquo; composes an extended verse working "
            "through an elephant's physical features one by one &mdash; trunk, tusks, feet, "
            "neck, head, tail &mdash; and assigning each a corresponding spiritual quality: "
            "faith as trunk, equanimity as tusks, wisdom as head, seclusion as tail."]),
        ("Two closing similes for what the giant does not cling to", [
            "The verse closes with two of the canon's most recognizable images: the white "
            "lotus, which grows in water yet is never wet by it, as the Buddha lives in the "
            "world yet is not stuck to it; and a fire that, its fuel exhausted, is simply said "
            "to be &ldquo;quenched&rdquo; &mdash; <em>nibbuta</em>, the same root underlying "
            "<em>nibbāna</em> &mdash; rather than having gone anywhere in particular."]),
        ("A giant defined by absence, not achievement", [
            "It is worth noticing what the core definition does and doesn't claim: "
            "&ldquo;one who does nothing monstrous&rdquo; is a description in the negative, "
            "naming what is absent (harm by body, speech, mind) rather than listing "
            "accomplishments to be checked off. The verse's later elaborations add positive "
            "qualities &mdash; faith, mindfulness, wisdom &mdash; but the Buddha's own defining "
            "sentence rests on restraint from harm as the essential criterion."]),
    ],
    terms=[
        ("nāga",
         "&ldquo;giant,&rdquo; also &ldquo;elephant&rdquo; or &ldquo;serpent&rdquo; depending "
         "on context &mdash; the discourse's central term, redefined from physical scale to "
         "moral conduct."),
        ("na kiñci pāpaṁ karoti kāyena vācāya manasā",
         "&ldquo;does nothing monstrous by way of body, speech, and mind&rdquo; &mdash; the "
         "Buddha's defining sentence for the true giant."),
        ("nibbuta",
         "&ldquo;quenched&rdquo; &mdash; the state of an extinguished fire the verse compares "
         "the giant to, sharing its root with <em>nibbāna</em>."),
        ("padumaṁ",
         "&ldquo;lotus&rdquo; &mdash; the verse's image for the Buddha's presence in the world "
         "without attachment to it, growing in water yet unwetted."),
        ("upekkhā",
         "&ldquo;equanimity&rdquo; &mdash; assigned in the verse to the giant's white tusks, "
         "one of several qualities mapped onto specific elephant features."),
    ],
    text_intro=(
        "The discourse in full: the crowd's cry, Udāyī's question, the Buddha's redefinition, "
        "and Udāyī's extended verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At the eastern gate: a royal elephant passes"),
        ("p", "&sect;1", "an6.43:1.1-3.15"),
        ("h3", "Udāyī's celebration begins"),
        ("p", "&sect;2", "an6.43:4.1-8.4"),
        ("h3", "The giant's anatomy, in verse"),
        ("p", "&sect;3", "an6.43:9.1-15.4"),
        ("h3", "The closing similes"),
        ("p", "&sect;4", "an6.43:16.1-20.4"),
    ],
    quiz=[
        {"q": "What prompts this discourse?",
         "opts": [
             "A mendicant's question about ethics",
             "A royal bull elephant passing through Sāvatthī's eastern gate, prompting the "
             "crowd's cry of 'a giant, such a giant!'",
             "A dispute between two mendicants",
             "A deity's nighttime visit"],
         "correct": 1,
         "expl": "A public spectacle witnessed by the Buddha and Ānanda after bathing."},
        {"q": "How does the Buddha redefine 'giant' (nāga)?",
         "opts": [
             "As applying only to the largest elephants",
             "Not by physical size at all, but as one who does nothing monstrous by way of "
             "body, speech, and mind",
             "As a term reserved for kings and nobles",
             "As identical in meaning to 'psychic power'"],
         "correct": 1,
         "expl": "A shift from physical scale to moral conduct as the basis of the term."},
        {"q": "What creatures does Udāyī's question establish already receive the term 'giant'?",
         "opts": [
             "Only elephants",
             "Elephants, horses, bulls, serpents, large trees, and unusually large humans",
             "Only mythical creatures",
             "Only deities"],
         "correct": 1,
         "expl": "A broadly applied term before the Buddha's redefinition narrows its criterion."},
        {"q": "What is unusual about where this discourse's real weight falls, according to the "
              "guide?",
         "opts": [
             "It falls entirely on the Buddha's brief defining sentence",
             "It falls on Udāyī's own extended celebratory verse, which elaborates the "
             "redefined image point by point across an elephant's anatomy",
             "It falls on a debate that is never resolved",
             "The discourse has no verse content at all"],
         "correct": 1,
         "expl": "Most of the text is Udāyī's own composition, not the Buddha's words."},
        {"q": "What two closing similes does the verse use?",
         "opts": [
             "A mountain and a river",
             "A white lotus unwetted by the water it grows in, and a fire simply said to be "
             "'quenched' once its fuel is exhausted",
             "A chariot and a horse",
             "A tree and its shadow"],
         "correct": 1,
         "expl": "Two of the canon's most recognizable images, both concerning non-attachment."},
        {"q": "What does <em>nibbuta</em> share its root with?",
         "opts": ["Nāga", "Nibbāna", "Upekkhā", "Padumaṁ"],
         "correct": 1,
         "expl": "'Quenched' — the same root underlying the term for full awakening."},
        {"q": "What quality does the guide note about the Buddha's core defining sentence for "
              "'giant'?",
         "opts": [
             "It is entirely positive, listing accomplishments to check off",
             "It is a description in the negative, naming what is absent — harm by body, "
             "speech, and mind — rather than an achievement to be verified",
             "It requires physical strength as a precondition",
             "It applies only to fully awakened beings"],
         "correct": 1,
         "expl": "Restraint from harm, not a list of attainments, is the essential criterion."},
        {"q": "Where does this discourse's narrative take place?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, at the eastern gate, after the Buddha and Ānanda bathed at the Eastern "
             "Monastery",
             "Near Kimbilā",
             "Icchānaṅgala"],
         "correct": 1,
         "expl": "A specific, sensory scene witnessed directly by the Buddha and Ānanda."},
        {"q": "What quality does the verse assign to the giant's 'white tusks'?",
         "opts": ["Faith", "Mindfulness", "Equanimity (upekkhā)", "Wisdom"],
         "correct": 2,
         "expl": "One of several elephant features mapped to specific spiritual qualities."},
        {"q": "Who is Udāyī, in this discourse?",
         "opts": [
             "A hostile brahmin",
             "A mendicant who asks the initiating question and then composes the discourse's "
             "extended celebratory verse",
             "A deity",
             "A layperson"],
         "correct": 1,
         "expl": "Both the question-asker and the verse's own composer."},
    ],
    marginalia=[
        ("Redefined 'giant'", [
            "not physical size —",
            "does nothing monstrous",
            "by body, speech, mind",
        ]),
        ("The giant's anatomy", [
            "faith: trunk",
            "equanimity: tusks",
            "wisdom: head",
            "seclusion: tail",
        ]),
        ("Two closing similes", [
            "lotus unwetted by water",
            "fire simply 'quenched' —",
            "<span class=\"pali\">nibbuta</span>",
        ]),
        ("Cross-references", [
            "AN 6.30 &middot; the last discourse of ch.3",
        ]),
    ],
    further=[
        '<a href="%s/an6.43/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.44.html">AN 6.44 &middot; With Migasālā</a> &mdash; next, Ānanda and a '
        "puzzled laywoman.",
        '<a href="an-6.42.html">AN 6.42 &middot; With Nāgita</a> &mdash; the previous '
        "chapter's close.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.44 — Migasālāsutta
# --------------------------------------------------------------------------- #
page(
    44, "Migasālā", "With Migasālā",
    vagga=VAGGA_5,
    meta_title="AN 6.44 — With Migasālā | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Migasālāsutta, where "
        "a laywoman's confusion over two relatives reborn identically leads the Buddha to warn "
        "against judging individuals by outward conduct alone. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The laywoman Migasālā, questioning Ānanda; then the Buddha, correcting "
                     "Ānanda's own answer"),
        ("Form", "A puzzled lay question, an honest but insufficient reply, and the Buddha's "
                 "correction built from six paired individuals"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Warnings against judging spiritual attainment by outward conduct "
                              "alone recur across the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;#9734;&#9734; &mdash; genuinely difficult "
                       "doctrinal territory, worth reading slowly rather than reduced to a "
                       "simple moral"),
    ],
    why=(
        "Migasālā's question is a real puzzle, not a rhetorical one: her chaste father and her "
        "unchaste uncle were both declared once-returners, reborn in exactly the same heavenly "
        "realm, despite living very differently. Even Ānanda, pressed to explain, can only "
        "confirm the fact without resolving it &mdash; &ldquo;that's how the Buddha declared "
        "it.&rdquo; The Buddha's own answer to Ānanda afterward is stern and, notably, does not "
        "fully resolve the puzzle either: it redirects the whole question away from comparing "
        "outward conduct and toward something only a Realized One can actually assess."),
    guide=[
        ("The teaching in one sentence", [
            "Six kinds of individuals are found in the world &mdash; gentle or difficult in "
            "temperament, each either having or lacking learning and even temporary freedom "
            "&mdash; and outward similarity between two people conceals a real difference that "
            "&ldquo;only a Realized One&rdquo; can actually assess, so ordinary people should "
            "not pass judgment on where anyone is headed."]),
        ("A real puzzle, honestly left partly open", [
            "Migasālā's question deserves to be taken at face value: it is not confused or "
            "unreasonable to wonder why two people who lived so differently &mdash; her father "
            "chaste, her uncle openly not &mdash; received the identical declared outcome. "
            "Ānanda's reply, &ldquo;that's how the Buddha declared it,&rdquo; is honest but "
            "genuinely insufficient, and the Buddha's later correction to Ānanda, while sharp in "
            "tone, does not supply a simple resolution either &mdash; it explains why the "
            "puzzle cannot be resolved from outside."]),
        ("Six individuals, distinguished by two variables", [
            "The Buddha's six-fold answer crosses two dimensions: temperament (gentle and "
            "pleasant, or angry, conceited, and prone to greedy thoughts or inappropriate "
            "speech) and spiritual development (having listened, learned, and found even "
            "temporary freedom, or not). Someone gentle without development and someone "
            "difficult with development can, on this analysis, arrive at very different "
            "outcomes despite superficial temperament suggesting otherwise &mdash; and the "
            "reverse holds too."]),
        ("Judgment as active harm, not mere error", [
            "The Buddha's instruction to Ānanda is unusually forceful: &ldquo;don't be "
            "judgmental about individuals&hellip; those who pass judgment on individuals harm "
            "themselves.&rdquo; This is not framed as advice against a minor social vice but as "
            "a warning that the act of comparative judgment itself &mdash; not merely getting "
            "the judgment wrong &mdash; causes real harm to the one making it."]),
        ("The closing line about Purāṇa and Isidatta", [
            "The discourse's final observation is easy to miss but central: &ldquo;if Isidatta "
            "had achieved Purāṇa's level of ethical conduct, Purāṇa could not have even known "
            "Isidatta's destination. And if Purāṇa had achieved Isidatta's level of wisdom, "
            "Isidatta could not have even known Purāṇa's destination. So both individuals were "
            "lacking in one respect.&rdquo; Neither man is praised as simply superior; each "
            "possessed something the other lacked, and their identical outcome does not erase "
            "that difference &mdash; it simply lies beyond what an outside observer, including "
            "Migasālā, could see."]),
    ],
    terms=[
        ("sakadāgāmī",
         "&ldquo;once-returner&rdquo; &mdash; the attainment declared for both Purāṇa and "
         "Isidatta, the shared outcome that prompts Migasālā's question."),
        ("tāvakālika vimutti",
         "&ldquo;temporary freedom&rdquo; &mdash; one of the qualities distinguishing the six "
         "individuals, alongside having listened, learned, and understood theoretically."),
        ("puggalavemattatā",
         "not a single compound in this translation but the underlying subject: the real "
         "variation between individuals that outward similarity can conceal."),
        ("dhammasota",
         "&ldquo;the stream of the teaching&rdquo; &mdash; what is said to carry along the "
         "individual who has developed skillful qualities, explaining why they fare better "
         "despite apparent similarity to another."),
        ("takkī",
         "&ldquo;judgmental,&rdquo; &ldquo;a reasoner&rdquo; &mdash; the quality the Buddha "
         "warns Ānanda against, of those who compare and pass judgment on individuals."),
    ],
    text_intro=(
        "The discourse in full: Migasālā's question, Ānanda's report to the Buddha, and the "
        "Buddha's correction built from six individuals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Migasālā's question to Ānanda"),
        ("p", "&sect;1", "an6.44:1.1-3.2"),
        ("h3", "The Buddha's response: six individuals"),
        ("p", "&sect;2", "an6.44:5.1-9.9"),
        ("h3", "Two further pairs, and the conclusion"),
        ("p", "&sect;3", "an6.44:10.1-18.3"),
    ],
    quiz=[
        {"q": "What puzzle does Migasālā bring to Ānanda?",
         "opts": [
             "Why some people are reborn as animals",
             "Why her chaste father and her unchaste uncle were both declared once-returners, "
             "reborn in exactly the same heavenly realm",
             "How to develop psychic power",
             "Why the Buddha travels so much"],
         "correct": 1,
         "expl": "A real, honestly puzzling case, not a rhetorical or confused question."},
        {"q": "How does Ānanda respond to Migasālā's question?",
         "opts": [
             "He explains the full doctrinal resolution immediately",
             "Honestly but insufficiently: 'You're right, sister, but that's how the Buddha "
             "declared it'",
             "He refuses to answer at all",
             "He declares Migasālā is mistaken about the facts"],
         "correct": 1,
         "expl": "An honest admission that he cannot resolve the puzzle himself."},
        {"q": "What two dimensions does the Buddha's six-fold answer cross?",
         "opts": [
             "Wealth and social status",
             "Temperament (gentle or difficult) and spiritual development (having found even "
             "temporary freedom, or not)",
             "Age and gender",
             "Location and occupation"],
         "correct": 1,
         "expl": "Producing six combinations that can yield very different outcomes despite "
                 "similar surface temperament."},
        {"q": "How forceful is the Buddha's warning to Ānanda about judging individuals?",
         "opts": [
             "Mild — a gentle suggestion to be more careful",
             "Strong — framed as active harm to the judger, not merely a risk of getting the "
             "judgment wrong: 'those who pass judgment on individuals harm themselves'",
             "The Buddha does not actually warn against judgment",
             "The warning applies only to laypeople, not mendicants"],
         "correct": 1,
         "expl": "The act of comparative judgment itself is treated as harmful to whoever makes "
                 "it."},
        {"q": "What does the discourse's closing observation about Purāṇa and Isidatta say?",
         "opts": [
             "That Purāṇa was simply superior to Isidatta in every way",
             "That each man possessed something the other lacked — Isidatta could not have "
             "known Purāṇa's destination without Purāṇa's wisdom, nor Purāṇa known Isidatta's "
             "without Isidatta's ethical conduct — so both were 'lacking in one respect'",
             "That the two men were in fact reborn in different realms",
             "That neither man actually attained anything"],
         "correct": 1,
         "expl": "A nuanced closing that resists declaring either man simply better."},
        {"q": "Does this discourse fully resolve Migasālā's original puzzle, according to the "
              "guide?",
         "opts": [
             "Yes, completely, with a simple explanation",
             "Not fully — the Buddha's answer explains why the puzzle cannot be resolved from "
             "outside, rather than supplying a simple resolution",
             "The discourse abandons the question entirely",
             "The Buddha declares the puzzle meaningless"],
         "correct": 1,
         "expl": "A genuinely difficult teaching, not reducible to a tidy moral."},
        {"q": "What does <em>dhammasota</em> mean?",
         "opts": [
             "The stream of the teaching, said to carry along one who has developed skillful "
             "qualities",
             "A type of meditative absorption",
             "A ritual bathing practice",
             "A synonym for 'once-returner'"],
         "correct": 0,
         "expl": "What explains why the developed individual fares better despite apparent "
                 "temperamental similarity to the undeveloped one."},
        {"q": "Is a setting stated for AN 6.44?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "The scene moves between Migasālā's home and wherever the Buddha is staying, "
                 "without a stated location."},
        {"q": "What attainment had both Purāṇa and Isidatta been declared to have reached?",
         "opts": ["Stream-entry", "Once-returning (sakadāgāmī)", "Full awakening", "Non-returning"],
         "correct": 1,
         "expl": "The shared outcome that prompts Migasālā's original confusion."},
        {"q": "Who alone, according to the Buddha, can truly assess the difference between two "
              "outwardly similar individuals?",
         "opts": [
             "A senior mendicant", "A Realized One (the Buddha)", "Any experienced layperson", "No one at all"],
         "correct": 1,
         "expl": "The basis for the instruction that ordinary people, including Ānanda, should "
                 "not pass such judgments."},
    ],
    marginalia=[
        ("A real puzzle", [
            "chaste father, unchaste",
            "uncle — same declared",
            "outcome, honestly asked",
        ]),
        ("Six individuals", [
            "gentle or difficult ×",
            "developed or not —",
            "outcomes vary either way",
        ]),
        ("Judgment as harm", [
            "not just 'getting it",
            "wrong' — the act itself",
            "harms the judger",
        ]),
        ("Cross-references", [
            "AN 6.43 &middot; previous, a redefinition",
        ]),
    ],
    further=[
        '<a href="%s/an6.44/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.45.html">AN 6.45 &middot; Debt</a> &mdash; next, an extended simile on '
        "spiritual poverty.",
        '<a href="an-6.43.html">AN 6.43 &middot; The Giant</a> &mdash; previous, a redefinition '
        "of a familiar term.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.45 — Iṇasutta
# --------------------------------------------------------------------------- #
page(
    45, "Iṇa", "Debt",
    vagga=VAGGA_5,
    meta_title="AN 6.45 — Debt | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Iṇasutta, which maps "
        "poverty, debt, interest, warning, prosecution, and imprisonment onto the inner life of "
        "someone lacking faith, conscience, prudence, energy, and wisdom. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A six-step Socratic sequence of confirmed questions, then a point-by-point "
                 "mapping onto spiritual poverty, closing in verse"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Debt as a figure for unwholesome states recurs in related form "
                              "across the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; an extended, methodically "
                       "built simile worth tracing step by step"),
    ],
    why=(
        "The Buddha builds this teaching by first securing agreement, step by step, that "
        "poverty, debt, unpaid interest, a warning, prosecution, and imprisonment are each "
        "&ldquo;suffering in the world for a person who enjoys sensual pleasures&rdquo; "
        "&mdash; six escalating stages of an ordinary financial catastrophe &mdash; before "
        "mapping every stage onto the inner condition of someone who lacks faith, conscience, "
        "prudence, energy, and wisdom. The simile is not decorative; each financial stage is "
        "matched to a specific psychological or karmic parallel."),
    guide=[
        ("The teaching in one sentence", [
            "Just as poverty, debt, interest, warning, prosecution, and imprisonment are six "
            "escalating stages of suffering for someone who enjoys sensual pleasures, so lacking "
            "faith, conscience, prudence, energy, and wisdom leads a person through a matching "
            "six-stage sequence, ending in the &ldquo;prison&rdquo; of hell or the animal realm."]),
        ("A confirmed sequence before the mapping begins", [
            "The Buddha does not simply assert the simile; he first gets the mendicants' "
            "explicit agreement to each of the six financial stages in turn &mdash; "
            "&ldquo;yes, sir&rdquo; repeated six times &mdash; before drawing the comparison. "
            "This Socratic structure ensures the base of the simile is uncontroversial before "
            "its application to inner life is introduced."]),
        ("Six financial stages mapped precisely", [
            "Lacking the five qualities (faith, conscience, prudence, energy, wisdom) is called "
            "&ldquo;poverty&rdquo; in the training; doing bad things by body, speech, and mind "
            "is the &ldquo;debt&rdquo;; concealing those bad deeds with corrupt wishes is the "
            "&ldquo;interest&rdquo; paid on that debt; being spoken of poorly by good-hearted "
            "companions is the &ldquo;warning&rdquo;; being beset by remorseful thoughts in "
            "solitude is the &ldquo;prosecution&rdquo;; and rebirth in hell or the animal realm "
            "is the &ldquo;imprisonment&rdquo; &mdash; described as worse than any actual prison, "
            "since it obstructs &ldquo;the supreme sanctuary from the yoke.&rdquo;"]),
        ("Concealment as the pivot of the whole sequence", [
            "The step from &ldquo;debt&rdquo; to &ldquo;interest&rdquo; is the simile's "
            "psychological center: it is not the bad deed alone that compounds the harm, but the "
            "subsequent wish, plan, and effort to conceal it &mdash; &ldquo;may no-one find me "
            "out!&rdquo; Concealment, on this analysis, functions exactly like interest on an "
            "unpaid debt: it accumulates on top of the original wrong, making the eventual "
            "reckoning worse."]),
        ("A closing verse offering the positive counterpart", [
            "The discourse does not end on imprisonment. Its closing verses turn to a "
            "&ldquo;faithful householder of discernment&rdquo; who gives generously from "
            "properly earned wealth, and then to the mendicant path itself &mdash; giving up the "
            "five hindrances, entering absorption, and reaching &ldquo;the highest freedom from "
            "debt&rdquo; &mdash; explicitly naming the positive mirror of everything the earlier "
            "simile diagnosed."]),
    ],
    terms=[
        ("iṇa",
         "&ldquo;debt&rdquo; &mdash; the discourse's own title and central image, mapped onto "
         "unskillful deeds done through lack of the five qualities."),
        ("vaḍḍhi",
         "&ldquo;interest&rdquo; &mdash; mapped onto the corrupt wishes used to conceal bad "
         "deeds, the simile's psychological turning point."),
        ("codanā",
         "&ldquo;warning,&rdquo; &ldquo;accusation&rdquo; &mdash; mapped onto good-hearted "
         "companions speaking critically of the person's conduct."),
        ("anuyoga",
         "&ldquo;prosecution&rdquo; &mdash; mapped onto remorseful thoughts arising in "
         "solitude, in the wilderness or an empty hut."),
        ("yogakkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; what the closing verses say the "
         "&ldquo;prison&rdquo; of a bad rebirth obstructs more than any actual imprisonment."),
    ],
    text_intro=(
        "The discourse in full: the confirmed financial sequence, its mapping onto spiritual "
        "poverty, and the closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six confirmed stages of financial suffering"),
        ("p", "&sect;1", "an6.45:1.1-7.1"),
        ("h3", "The mapping onto spiritual poverty"),
        ("p", "&sect;2", "an6.45:7.2-12.2"),
        ("h3", "The closing verses"),
        ("p", "&sect;3", "an6.45:13.1-28.4"),
    ],
    quiz=[
        {"q": "What six financial stages does the Buddha establish through confirmed questions?",
         "opts": [
             "Poverty, debt, interest, warning, prosecution, and imprisonment",
             "Wealth, investment, profit, taxation, audit, and bankruptcy",
             "Borrowing, lending, saving, spending, giving, and hoarding",
             "The five hindrances plus doubt"],
         "correct": 0,
         "expl": "Six escalating stages of an ordinary financial catastrophe, agreed to one at "
                 "a time."},
        {"q": "Why does the Buddha secure explicit agreement to each financial stage before "
              "drawing the comparison?",
         "opts": [
             "It is not a deliberate structure, simply incidental",
             "To ensure the base of the simile is uncontroversial before its application to "
             "inner life is introduced",
             "Because the mendicants initially disagreed",
             "To test the mendicants' memory"],
         "correct": 1,
         "expl": "A Socratic sequence of six 'yes, sir' confirmations before the mapping begins."},
        {"q": "What is mapped onto 'poverty' in the training of the Noble One?",
         "opts": [
             "Physical illness",
             "Lacking faith, conscience, prudence, energy, and wisdom",
             "Living without material possessions",
             "Being newly ordained"],
         "correct": 1,
         "expl": "The absence of the five qualities named as this simile's starting point."},
        {"q": "What is mapped onto 'interest,' and why does the guide call this the simile's "
              "psychological center?",
         "opts": [
             "Generosity toward others — interest is a positive quality here",
             "Concealing bad deeds with corrupt wishes ('may no-one find me out!') — "
             "concealment compounds harm just as interest accumulates on unpaid debt",
             "Meditation practice",
             "Nothing is mapped onto interest in this discourse"],
         "correct": 1,
         "expl": "The step from the original bad deed to its concealment is where the harm "
                 "compounds."},
        {"q": "What is mapped onto 'imprisonment,' the final and worst stage?",
         "opts": [
             "Being expelled from the Saṅgha",
             "Rebirth in hell or the animal realm, described as worse than any actual prison",
             "Poverty in a future life",
             "Loss of reputation among peers"],
         "correct": 1,
         "expl": "Named as obstructing 'the supreme sanctuary from the yoke' more than any "
                 "literal imprisonment could."},
        {"q": "What does the discourse's closing verse offer, beyond the simile of "
              "imprisonment?",
         "opts": [
             "Nothing further — the discourse ends on imprisonment",
             "A positive counterpart: a generous householder and, further, the mendicant path "
             "of giving up hindrances and reaching 'the highest freedom from debt'",
             "A warning against ever taking financial loans",
             "A denial that the simile applies to real life"],
         "correct": 1,
         "expl": "The closing verses explicitly mirror the earlier diagnosis with its positive "
                 "resolution."},
        {"q": "What does <em>codanā</em> mean, as mapped in this discourse?",
         "opts": [
             "Imprisonment", "Warning or accusation — mapped onto good-hearted companions "
             "speaking critically of one's conduct", "Interest", "Poverty"],
         "correct": 1,
         "expl": "The fourth stage in the mapped sequence."},
        {"q": "Is a setting stated for AN 6.45?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "A bare formula, though methodically constructed through confirmed questions."},
        {"q": "What is mapped onto 'prosecution'?",
         "opts": [
             "Being formally charged in a court",
             "Being beset by remorseful, unskillful thoughts when alone in a wilderness, the "
             "root of a tree, or an empty hut",
             "Losing one's monastic robes",
             "Public shaming by lay followers"],
         "correct": 1,
         "expl": "The fifth stage, an inward experience of remorse rather than an external event."},
        {"q": "What five qualities does lacking them constitute 'poverty' in this discourse?",
         "opts": [
             "Wealth, status, health, beauty, and strength",
             "Faith, conscience, prudence, energy, and wisdom",
             "Seeing, listening, acquisition, training, and service",
             "Work, talk, sleep, company, and closeness"],
         "correct": 1,
         "expl": "The starting condition the whole six-stage sequence unfolds from."},
    ],
    marginalia=[
        ("Six mapped stages", [
            "poverty &rarr; debt &rarr;",
            "interest &rarr; warning &rarr;",
            "prosecution &rarr; prison",
        ]),
        ("The turning point", [
            "not the bad deed alone —",
            "concealing it compounds",
            "the harm, like interest",
        ]),
        ("Worse than any prison", [
            "hell or the animal realm",
            "obstructs the supreme",
            "sanctuary from the yoke",
        ]),
        ("Cross-references", [
            "AN 6.44 &middot; previous, on judgment",
            "AN 6.46 &middot; next, Mahācunda",
        ]),
    ],
    further=[
        '<a href="%s/an6.45/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.46.html">AN 6.46 &middot; By Mahācunda</a> &mdash; next, on mutual '
        "respect between two styles of practice.",
        '<a href="an-6.44.html">AN 6.44 &middot; With Migasālā</a> &mdash; previous, on the '
        "limits of outside judgment.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.46 — Mahācundasutta
# --------------------------------------------------------------------------- #
page(
    46, "Mahācunda", "By Mahācunda",
    vagga=VAGGA_5,
    meta_title="AN 6.46 — By Mahācunda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mahācundasutta, in "
        "which Venerable Mahācunda diagnoses the mutual contempt between mendicants devoted to "
        "absorption and those devoted to doctrine, and prescribes mutual praise. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "The land of the Cetis, at Sahajāti"),
        ("Speakers", "Venerable Mahācunda, addressing the mendicants"),
        ("Form", "Two mirrored scenarios of mutual contempt, two mirrored scenarios of biased "
                 "praise, and two paired training instructions"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Tension between meditators and scholar-monks recurs as a "
                              "recognized concern across Buddhist monastic literature broadly, "
                              "including the Chinese Āgamas; this reading guide does not assert "
                              "a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a precisely balanced "
                       "discourse worth reading for its structural symmetry"),
    ],
    why=(
        "Mahācunda names a division this series has not yet directly addressed: mendicants who "
        "practice absorption meditation and mendicants who practice discernment of principles "
        "&mdash; doctrinal study and analysis &mdash; each capable of dismissing the other's "
        "path as not real practice at all. His discourse is built with unusual symmetry, giving "
        "each side's contempt, each side's biased praise, and each side's needed corrective "
        "equal and mirrored treatment."),
    guide=[
        ("The teaching in one sentence", [
            "Mendicants devoted to discernment of principles and mendicants devoted to "
            "absorption meditation should praise each other rather than show contempt or praise "
            "only their own kind, because genuine mastery of either path is rare and valuable "
            "in its own right."]),
        ("Contempt in both directions, given equal weight", [
            "Mahācunda states first how discernment-practicing mendicants mock those who "
            "practice absorption &mdash; &ldquo;why do they practice absorption meditation? In "
            "what way?&rdquo; &mdash; and then, in exactly mirrored language, how "
            "absorption-practicing mendicants mock those who study doctrine as "
            "&ldquo;restless, insolent, fickle&hellip; with straying minds.&rdquo; The discourse "
            "refuses to favor either side's contempt as more justified than the other's."]),
        ("A second failure: praising only one's own kind", [
            "Beyond outright contempt, Mahācunda names a subtler failure &mdash; discernment-"
            "practicing mendicants praising only others like themselves, and absorption-"
            "practicing mendicants doing the same. Both patterns, contempt and selective praise "
            "alike, are said to leave &ldquo;the people&rdquo; and &ldquo;gods and humans&rdquo; "
            "without benefit; the harm is described in exactly the same civic terms each time."]),
        ("The prescribed remedy, and its stated reason", [
            "Mahācunda's instruction is not to abandon either practice or to declare one "
            "superior, but for each side to actively train in praising the other. The reason "
            "given for each direction is specific and not interchangeable: discernment-"
            "practitioners should praise absorption-practitioners because direct meditative "
            "experience of &ldquo;the element free of death&rdquo; is rare, and absorption-"
            "practitioners should praise discernment-practitioners because penetrating "
            "wisdom into a deep saying's meaning is rare &mdash; two distinct, non-competing "
            "kinds of rarity, not one path ranked above the other."]),
        ("A named speaker rather than the Buddha, and why that may matter", [
            "This is one of several discourses in this chapter delivered by a senior disciple "
            "rather than the Buddha directly. Coming from Mahācunda, addressing an apparently "
            "real tension between two styles of practice within the monastic community, the "
            "teaching reads less like abstract doctrine and more like a senior figure directly "
            "managing a live source of friction among his peers."]),
    ],
    terms=[
        ("dhammayogā bhikkhū",
         "&ldquo;mendicants who practice discernment of principles&rdquo; &mdash; one of the "
         "two groups this discourse addresses, devoted to doctrinal study and analysis."),
        ("jhāyī bhikkhū",
         "&ldquo;mendicants who practice absorption&rdquo; &mdash; the second group, devoted to "
         "meditative concentration."),
        ("accantaniṭṭha amatadhātu",
         "&ldquo;the element free of death&rdquo; &mdash; what direct meditative experience of "
         "is said to be rare, the stated reason discernment-practitioners should praise "
         "absorption-practitioners."),
        ("gambhīraṁ atthapadaṁ paññāya ativijjha passanti",
         "&ldquo;see the meaning of a deep saying with penetrating wisdom&rdquo; &mdash; the "
         "rare capacity named as the reason absorption-practitioners should praise discernment-"
         "practitioners."),
        ("na ārādhako hoti",
         "&ldquo;is not inspired,&rdquo; &ldquo;does not succeed&rdquo; &mdash; the shared "
         "verdict on both groups whenever contempt or one-sided praise occurs."),
    ],
    text_intro=(
        "The discourse in full: two mirrored scenarios of contempt, two of biased praise, and "
        "the paired training instructions. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Mutual contempt, in both directions"),
        ("p", "&sect;1", "an6.46:2.1-3.4"),
        ("h3", "Praising only one's own kind"),
        ("p", "&sect;2", "an6.46:4.1-5.2"),
        ("h3", "The remedy, and its stated reasons"),
        ("p", "&sect;3", "an6.46:6.1-7.5"),
    ],
    quiz=[
        {"q": "What two groups of mendicants does Mahācunda address?",
         "opts": [
             "Senior and junior mendicants",
             "Mendicants who practice discernment of principles (doctrinal study) and "
             "mendicants who practice absorption meditation",
             "Village-dwelling and wilderness-dwelling mendicants",
             "Monks and nuns"],
         "correct": 1,
         "expl": "Two styles of practice this discourse treats with deliberate symmetry."},
        {"q": "How does the discourse structure its treatment of contempt between the two "
              "groups?",
         "opts": [
             "It favors one side's contempt as more justified",
             "With exact mirroring — each group's mockery of the other is given equal weight "
             "and nearly parallel language",
             "Only one group is shown expressing contempt",
             "The discourse denies any contempt exists between the groups"],
         "correct": 1,
         "expl": "Neither side's dismissiveness is favored over the other's."},
        {"q": "What second failure, beyond outright contempt, does Mahācunda name?",
         "opts": [
             "Refusing to eat almsfood",
             "Praising only others of one's own kind — discernment-practitioners praising only "
             "discernment-practitioners, and the reverse",
             "Talking too much during meals",
             "Sleeping too little"],
         "correct": 1,
         "expl": "A subtler failure than direct mockery, but treated with the same civic harm."},
        {"q": "What remedy does Mahācunda prescribe?",
         "opts": [
             "Abandoning one practice in favor of the other",
             "Each side should actively train in praising the other, for distinct, "
             "non-competing reasons",
             "Both practices should be banned",
             "Only senior mendicants should practice either"],
         "correct": 1,
         "expl": "Neither practice is ranked above the other; both are praised for what is "
                 "genuinely rare about each."},
        {"q": "Why should discernment-practitioners praise absorption-practitioners, according "
              "to the stated reason?",
         "opts": [
             "Because absorption practice is objectively superior",
             "Because it's rare to find individuals with direct meditative experience of 'the "
             "element free of death'",
             "Because absorption-practitioners are more senior",
             "No reason is given"],
         "correct": 1,
         "expl": "A specific rarity, distinct from the reason given in the other direction."},
        {"q": "Why should absorption-practitioners praise discernment-practitioners?",
         "opts": [
             "Because doctrinal study is objectively superior",
             "Because it's rare to find individuals who see the meaning of a deep saying with "
             "penetrating wisdom",
             "Because they are more numerous",
             "No reason is given"],
         "correct": 1,
         "expl": "A distinct kind of rarity, not a ranking of one path above the other."},
        {"q": "Where is AN 6.46 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "The land of the Cetis, at Sahajāti",
             "Rājagaha, on Vulture's Peak",
             "Near Kimbilā"],
         "correct": 1,
         "expl": "A location tied specifically to this discourse's speaker, Mahācunda."},
        {"q": "Who speaks this discourse?",
         "opts": ["The Buddha", "Venerable Mahācunda, addressing the mendicants", "Sāriputta", "Ānanda"],
         "correct": 1,
         "expl": "One of several discourses in this chapter delivered by a senior disciple "
                 "rather than the Buddha."},
        {"q": "What does the guide suggest about this discourse coming from a named senior "
              "disciple rather than the Buddha?",
         "opts": [
             "It carries less authority than a Buddha-spoken discourse",
             "It reads less like abstract doctrine and more like a senior figure directly "
             "managing a live source of friction within the monastic community",
             "It should be disregarded entirely",
             "It contradicts the Buddha's own teaching"],
         "correct": 1,
         "expl": "A practical, community-management register rather than a purely doctrinal one."},
        {"q": "What consequence is stated for both contempt and one-sided praise, in identical "
              "terms each time?",
         "opts": [
             "Both groups are expelled from the Saṅgha",
             "Neither group is 'inspired,' and both fail to act for the welfare and happiness "
             "of people, gods, and humans",
             "Only the discernment-practitioners suffer any consequence",
             "No consequence is stated"],
         "correct": 1,
         "expl": "The same civic-scale harm is named for each of the four failure scenarios."},
    ],
    marginalia=[
        ("Two styles, mirrored", [
            "discernment of principles",
            "vs. absorption meditation —",
            "equal treatment throughout",
        ]),
        ("Two failures", [
            "outright contempt",
            "praising only one's",
            "own kind",
        ]),
        ("Two distinct rarities", [
            "direct experience of",
            "deathlessness &middot; penetrating",
            "wisdom into deep sayings",
        ]),
        ("Cross-references", [
            "AN 6.45 &middot; previous, debt",
        ]),
    ],
    further=[
        '<a href="%s/an6.46/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.47.html">AN 6.47 &middot; Apparent in the Present Life (1st)</a> &mdash; '
        "next, a wanderer's question on a familiar phrase.",
        '<a href="an-6.45.html">AN 6.45 &middot; Debt</a> &mdash; previous, a different '
        "register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.47 — Paṭhamasandiṭṭhikasutta
# --------------------------------------------------------------------------- #
page(
    47, "Paṭhamasandiṭṭhika", "Apparent in the Present Life (1st)",
    vagga=VAGGA_5,
    meta_title="AN 6.47 — Apparent in the Present Life (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamasandiṭṭhikasutta, "
        "where the wanderer Moḷiyasīvaka asks what makes a teaching 'apparent in the present "
        "life,' and the Buddha answers with direct self-knowledge of greed, hate, and "
        "delusion. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The wanderer Moḷiyasīvaka, questioning the Buddha"),
        ("Form", "A question about a standing phrase, and a return-question building six "
                 "confirmed cases of self-awareness"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Verification of teaching through direct self-observation recurs "
                              "as a theme across the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a short dialogue with real "
                       "philosophical weight about what verification actually means"),
    ],
    why=(
        "The phrase &ldquo;apparent in the present life, immediately effective, inviting "
        "inspection&rdquo; recurs constantly through this series as part of the standard "
        "recollection-of-the-teaching formula, met most recently at AN 6.25 and 6.26 &mdash; "
        "but never before explained. Moḷiyasīvaka finally asks what it actually means, and the "
        "Buddha, rather than defining the phrase abstractly, answers with a question turned "
        "back on the wanderer's own immediate experience: do you know when there is greed in "
        "you, and when there is not?"),
    guide=[
        ("The teaching in one sentence", [
            "A teaching is &ldquo;apparent in the present life&rdquo; in the specific sense "
            "that one can know directly, right now, whether greed, hate, delusion, and their "
            "corresponding ideas are present or absent in oneself &mdash; verification requires "
            "no external authority, only attention to one's own mind."]),
        ("A phrase this series has used but not defined until now", [
            "This exact phrase &mdash; <em>sandiṭṭhiko dhammo</em>, and the fuller formula "
            "around it &mdash; has appeared repeatedly as part of the recollection-of-the-"
            "teaching formula, most recently at AN 6.25 and 6.26, always as something to "
            "recollect rather than something explained. AN 6.47 is where a questioner finally "
            "asks what grounds the claim, and the answer turns out to be simpler and more "
            "immediate than a doctrinal definition."]),
        ("Verification by return-question, not by argument", [
            "Rather than explaining the phrase in the abstract, the Buddha asks Sīvaka directly: "
            "&ldquo;when there's greed in you, do you understand &lsquo;I have greed in "
            "me&rsquo;?&rdquo; Sīvaka's own confirmed &ldquo;yes, sir&rdquo; becomes the proof: "
            "the very fact that he can answer the question demonstrates the teaching's "
            "verifiability, without the Buddha needing to argue for it separately."]),
        ("Six confirmed cases, three pairs", [
            "The pattern repeats across three named states &mdash; greed, hate, delusion "
            "&mdash; and, separately, their corresponding &ldquo;ideas&rdquo; (thoughts "
            "colored by greed, hate, or delusion, distinct from the states themselves), each "
            "checked in both directions: presence known as presence, absence known as absence. "
            "Six confirmed cases in total, each independently verifiable by the person asked."]),
        ("A wanderer's conversion, and what it signals", [
            "Sīvaka's closing declaration &mdash; &ldquo;excellent, sir!&rdquo; and going for "
            "refuge for life &mdash; is a real outcome, not a formality. Persuaded by nothing "
            "more than being shown that he already has direct access to verify a basic claim "
            "about his own mind, he converts on the strength of a method rather than a "
            "doctrine asserted to him from outside."]),
    ],
    terms=[
        ("sandiṭṭhiko dhammo",
         "&ldquo;a teaching apparent in the present life&rdquo; &mdash; the phrase Sīvaka asks "
         "about, part of the standard recollection-of-the-teaching formula met earlier in this "
         "nipāta."),
        ("akāliko",
         "&ldquo;immediately effective,&rdquo; not part of this discourse's own explanation but "
         "the next term in the same standing formula, verified by the same logic applied here."),
        ("rāgo, doso, moho",
         "&ldquo;greed, hate, delusion&rdquo; &mdash; the three states checked first, each in "
         "both its presence and absence."),
        ("sarāgā dhammā, sadosā dhammā, samohā dhammā",
         "&ldquo;greedy ideas, hateful ideas, delusional ideas&rdquo; &mdash; the second set of "
         "three checked, distinct from the bare states themselves."),
        ("paccattaṁ veditabbo viññūhi",
         "not directly translated in this English rendering but the standard closing phrase of "
         "the recollection-of-the-teaching formula: &ldquo;to be experienced by the wise for "
         "themselves.&rdquo;"),
    ],
    text_intro=(
        "The discourse in full: Moḷiyasīvaka's question, and the Buddha's six confirmed cases "
        "of self-knowledge. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Moḷiyasīvaka's question"),
        ("p", "&sect;1", "an6.47:1.1-1.4"),
        ("h3", "Greed, and the pattern established"),
        ("p", "&sect;2", "an6.47:2.1-2.6"),
        ("h3", "Hate, delusion, and their corresponding ideas"),
        ("p", "&sect;3", "an6.47:3.1-4.2"),
    ],
    quiz=[
        {"q": "What question does Moḷiyasīvaka ask the Buddha?",
         "opts": [
             "How many topics for recollection there are",
             "In what way is a teaching 'apparent in the present life, immediately effective, "
             "inviting inspection'",
             "How to develop psychic power",
             "Why the chaste and unchaste can receive the same rebirth"],
         "correct": 1,
         "expl": "A phrase this series has used repeatedly without ever explaining what grounds "
                 "the claim."},
        {"q": "How does the Buddha answer, rather than defining the phrase abstractly?",
         "opts": [
             "With a lengthy doctrinal explanation",
             "With a return-question, asking whether Sīvaka can directly know when greed is or "
             "isn't present in himself",
             "By refusing to answer",
             "By citing an authoritative scripture"],
         "correct": 1,
         "expl": "Sīvaka's own confirmed answer becomes the proof of the teaching's "
                 "verifiability."},
        {"q": "What six cases does the Buddha's question ultimately check?",
         "opts": [
             "The five faculties plus liberation",
             "Greed, hate, and delusion, and their corresponding 'ideas', each checked for both "
             "presence and absence",
             "The six sense doors",
             "Six kinds of superhuman knowledge"],
         "correct": 1,
         "expl": "Three states plus their corresponding thought-patterns, verified in both "
                 "directions."},
        {"q": "What does Sīvaka's confirmed 'yes, sir' demonstrate, according to the guide?",
         "opts": [
             "Nothing significant",
             "The teaching's verifiability itself — the very fact that he can answer "
             "demonstrates direct access to check the claim, without external argument",
             "That Sīvaka already understood the answer before asking",
             "That the Buddha's teaching requires blind faith"],
         "correct": 1,
         "expl": "Verification by return-question rather than by doctrinal assertion."},
        {"q": "How does this discourse end?",
         "opts": [
             "With Sīvaka remaining unconvinced",
             "With Sīvaka declaring himself a lay follower gone for refuge for life",
             "With an unresolved debate",
             "With the Buddha changing his teaching"],
         "correct": 1,
         "expl": "A real conversion on the strength of a demonstrated method, not an asserted "
                 "doctrine."},
        {"q": "Where has this exact phrase, 'apparent in the present life', appeared earlier in "
              "this nipāta?",
         "opts": [
             "Nowhere — this is its first appearance",
             "As part of the recollection-of-the-teaching formula, most recently at AN 6.25 and "
             "6.26",
             "Only in the Fours",
             "Only in this discourse and nowhere else"],
         "correct": 1,
         "expl": "Used repeatedly as something to recollect, never before explained until this "
                 "discourse."},
        {"q": "Is a setting stated for AN 6.47?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "A bare dialogue with no scene-setting clause."},
        {"q": "Who is Moḷiyasīvaka?",
         "opts": [
             "A senior mendicant", "A wanderer of another sect who questions the Buddha", "A "
             "deity", "A brahmin priest"],
         "correct": 1,
         "expl": "Distinguished from AN 6.48, the companion discourse's questioner, an unnamed "
                 "brahmin."},
        {"q": "What are 'greedy ideas' (sarāgā dhammā), as distinct from greed itself?",
         "opts": [
             "Identical to greed, no distinction is made",
             "A second, separate item checked alongside the bare state of greed — thoughts "
             "colored by greed, distinct from the underlying state",
             "A term for generosity",
             "Only relevant to advanced meditators"],
         "correct": 1,
         "expl": "The discourse checks six cases total: three states plus three corresponding "
                 "'ideas.'"},
        {"q": "What philosophical point does this discourse make about verification, according "
              "to the guide?",
         "opts": [
             "That verification requires trusting external authority",
             "That verifying a basic claim about the teaching requires no external authority, "
             "only attention to one's own mind",
             "That verification is impossible for ordinary people",
             "That only mendicants can verify such claims"],
         "correct": 1,
         "expl": "The whole discourse's real philosophical weight."},
    ],
    marginalia=[
        ("Six confirmed cases", [
            "greed &middot; hate &middot; delusion",
            "+ their corresponding",
            "'ideas', each way",
        ]),
        ("Method, not doctrine", [
            "no argument given —",
            "only a question turned",
            "back on one's own mind",
        ]),
        ("A phrase finally explained", [
            "used repeatedly since",
            "AN 6.25/6.26 —",
            "never before defined",
        ]),
        ("Cross-references", [
            "AN 6.48 &middot; next, a close companion",
        ]),
    ],
    further=[
        '<a href="%s/an6.47/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.48.html">AN 6.48 &middot; Apparent in the Present Life (2nd)</a> &mdash; '
        "next, a close companion with a genuinely different second triad.",
        '<a href="an-6.46.html">AN 6.46 &middot; By Mahācunda</a> &mdash; previous, a different '
        "register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.48 — Dutiyasandiṭṭhikasutta
# --------------------------------------------------------------------------- #
page(
    48, "Dutiyasandiṭṭhika", "Apparent in the Present Life (2nd)",
    vagga=VAGGA_5,
    meta_title="AN 6.48 — Apparent in the Present Life (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyasandiṭṭhikasutta, "
        "a brahmin's version of AN 6.47's question, whose second triad — checked directly — "
        "concerns corruption in body, speech, and mind, not greedy, hateful, and delusional "
        "ideas. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "A brahmin, questioning the Buddha"),
        ("Form", "The same question and return-question structure as AN 6.47, with a genuinely "
                 "different second triad"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "As with AN 6.47, verification through direct self-observation "
                              "recurs across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a close companion to AN "
                       "6.47, worth reading for its one genuine difference rather than skimmed "
                       "as a repeat"),
    ],
    why=(
        "AN 6.48 asks the identical question as AN 6.47 &mdash; this time from an unnamed "
        "brahmin rather than the wanderer Sīvaka &mdash; and the Buddha's method is identical: "
        "the same return-question about greed, hate, and delusion. But checked directly "
        "against the source, the discourse's second triad is not a repeat of AN 6.47's "
        "&ldquo;greedy, hateful, delusional ideas.&rdquo; It asks instead about corruption "
        "(<em>saṅkilesa</em>) leading to deeds of body, speech, and mind &mdash; a different, "
        "though related, set of three."),
    guide=[
        ("The teaching in one sentence", [
            "As at AN 6.47, a teaching is apparent in the present life because one can know "
            "directly whether greed, hate, and delusion are present or absent in oneself; this "
            "discourse's second triad extends the same self-checking method to corruption that "
            "leads to physical, verbal, and mental deeds, rather than to greedy, hateful, and "
            "delusional ideas."]),
        ("What is identical to AN 6.47", [
            "The opening question, the Buddha's return-question structure, the first triad "
            "(greed, hate, delusion checked for presence and absence), and the closing "
            "conversion formula all match AN 6.47 closely. A reader could reasonably expect the "
            "second triad to match as well &mdash; and checked directly, it does not."]),
        ("What genuinely differs, verified against the Pāli", [
            "Where AN 6.47's second triad names <em>sarāgā, sadosā, samohā dhammā</em> "
            "&mdash; greedy, hateful, delusional ideas, distinct thought-patterns &mdash; this "
            "discourse's second triad names <em>kāyaduccaritasaṅkilesa, "
            "vacīduccaritasaṅkilesa, manoduccaritasaṅkilesa</em> &mdash; corruption leading to "
            "misconduct of body, speech, and mind. One version checks colored mental states; "
            "the other checks whether corruption has actually led, or would lead, to conduct in "
            "each of the three doors of action."]),
        ("Why the difference is worth noting, not smoothing over", [
            "Following this guide's own established practice at AN 6.25, 6.29, and 6.33, the "
            "resemblance between two similarly titled, similarly structured discourses is "
            "exactly the situation that calls for checking rather than assuming. Here the "
            "difference is genuine and specific: one companion discourse verifies awareness of "
            "mental coloring, the other verifies awareness of corruption oriented toward actual "
            "conduct."]),
        ("Two questioners, one method", [
            "That the identical teaching method satisfies both a wandering ascetic of another "
            "sect (AN 6.47) and a brahmin (AN 6.48) &mdash; each converting by the same route, "
            "confirming a simple claim about their own mind &mdash; suggests the method's "
            "appeal was not limited to any one audience or background."]),
    ],
    terms=[
        ("saṅkilesa",
         "&ldquo;corruption&rdquo; &mdash; the term distinguishing this discourse's second "
         "triad from AN 6.47's &ldquo;ideas&rdquo; (dhammā)."),
        ("kāyaduccaritasaṅkilesa",
         "&ldquo;corruption leading to physical misconduct&rdquo; &mdash; the first item of "
         "this discourse's distinct second triad."),
        ("manoduccaritasaṅkilesa",
         "&ldquo;corruption leading to mental misconduct&rdquo; &mdash; the third item, closing "
         "the triad."),
        ("sarāgā dhammā",
         "&ldquo;greedy ideas&rdquo; &mdash; AN 6.47's corresponding first item in its own, "
         "different second triad, for direct comparison."),
        ("saraṇaṁ gata",
         "&ldquo;gone for refuge&rdquo; &mdash; the brahmin's closing declaration, matching "
         "Sīvaka's conversion at AN 6.47."),
    ],
    text_intro=(
        "The discourse in full: a brahmin's question, and the Buddha's six confirmed cases, "
        "including the distinct second triad. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A brahmin's question"),
        ("p", "&sect;1", "an6.48:1.1-1.4"),
        ("h3", "Greed, and the pattern established"),
        ("p", "&sect;2", "an6.48:2.1-2.6"),
        ("h3", "Hate, delusion, and corruption in body, speech, and mind"),
        ("p", "&sect;3", "an6.48:3.1-4.2"),
    ],
    quiz=[
        {"q": "How does the questioner in AN 6.48 differ from AN 6.47's?",
         "opts": [
             "They are the same person",
             "AN 6.48's questioner is an unnamed brahmin, rather than the wanderer Moḷiyasīvaka",
             "AN 6.48's questioner is a deity",
             "AN 6.48's questioner is Ānanda"],
         "correct": 1,
         "expl": "Different interlocutors, identical question and method."},
        {"q": "What does AN 6.47's second triad check, checked directly against the Pāli?",
         "opts": [
             "Corruption leading to misconduct of body, speech, and mind",
             "Greedy, hateful, and delusional ideas (dhammā) — distinct thought-patterns",
             "The five hindrances",
             "The five faculties"],
         "correct": 1,
         "expl": "AN 6.47's own second triad, for contrast with this discourse's."},
        {"q": "What does THIS discourse's (AN 6.48's) second triad actually check?",
         "opts": [
             "The same greedy, hateful, delusional ideas as AN 6.47",
             "Corruption (saṅkilesa) leading to misconduct of body, speech, and mind — a "
             "genuinely different set of three, not a repeat",
             "The six recollections",
             "The four brahmavihāra"],
         "correct": 1,
         "expl": "A specific, verified difference between two similarly structured companion "
                 "discourses."},
        {"q": "What distinction does the guide draw between the two versions' second triads?",
         "opts": [
             "There is no real distinction — they are identical",
             "One checks awareness of colored mental states (ideas); the other checks awareness "
             "of corruption oriented toward actual conduct in body, speech, and mind",
             "AN 6.47's version is doctrinally incorrect",
             "AN 6.48's version applies only to brahmins"],
         "correct": 1,
         "expl": "Two related but genuinely distinct forms of self-checking."},
        {"q": "What established practice does the guide say it follows in reading this "
              "discourse against AN 6.47?",
         "opts": [
             "Assuming identical companion discourses always match exactly",
             "The same discipline already applied at AN 6.25, AN 6.29, and AN 6.33: checking "
             "rather than assuming when two similar discourses resemble each other closely",
             "Ignoring AN 6.47 entirely when reading this discourse",
             "Treating this discourse as a later corruption of AN 6.47"],
         "correct": 1,
         "expl": "A consistent verification practice across this whole reading-guide project."},
        {"q": "What does <em>saṅkilesa</em> mean?",
         "opts": ["Purification", "Corruption", "Liberation", "Recollection"],
         "correct": 1,
         "expl": "The key term distinguishing this discourse's second triad from AN 6.47's."},
        {"q": "How does this discourse end?",
         "opts": [
             "With the brahmin remaining unconvinced",
             "With the brahmin declaring himself a lay follower gone for refuge for life, "
             "matching Sīvaka's conversion at AN 6.47",
             "With an unresolved debate",
             "With a rejection of the Buddha's teaching"],
         "correct": 1,
         "expl": "The same conversion outcome as the companion discourse, despite the different "
                 "questioner and the different second triad."},
        {"q": "Is a setting stated for AN 6.48?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "Matching AN 6.47, a bare dialogue with no scene-setting."},
        {"q": "What does <em>kāyaduccaritasaṅkilesa</em> mean?",
         "opts": [
             "Corruption leading to mental misconduct",
             "Corruption leading to physical misconduct",
             "Corruption leading to verbal misconduct",
             "A synonym for greed itself"],
         "correct": 1,
         "expl": "The first item of this discourse's own second triad."},
        {"q": "What does the guide conclude about the two questioners converting by the same "
              "method?",
         "opts": [
             "That the method only worked because both questioners already agreed with the "
             "Buddha beforehand",
             "That the method's appeal was not limited to any one audience or background — it "
             "satisfied both a wanderer of another sect and a brahmin",
             "That brahmins are more easily persuaded than wanderers",
             "That the two discourses actually contradict each other"],
         "correct": 1,
         "expl": "A shared method working across different backgrounds and questioners."},
    ],
    marginalia=[
        ("Same method", [
            "return-question on",
            "greed, hate, delusion —",
            "identical to AN 6.47",
        ]),
        ("Different second triad", [
            "not 'ideas' —",
            "corruption toward",
            "body, speech, mind conduct",
        ]),
        ("Two questioners", [
            "AN 6.47: a wanderer",
            "AN 6.48: a brahmin —",
            "both convert the same way",
        ]),
        ("Cross-references", [
            "AN 6.47 &middot; previous, the companion",
        ]),
    ],
    further=[
        '<a href="%s/an6.48/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.49.html">AN 6.49 &middot; With Khema</a> &mdash; next, two mendicants on '
        "how enlightenment is properly declared.",
        '<a href="an-6.47.html">AN 6.47 &middot; Apparent in the Present Life (1st)</a> &mdash; '
        "previous, for direct comparison of the two second triads.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.49 — Khemasutta
# --------------------------------------------------------------------------- #
page(
    49, "Khema", "With Khema",
    vagga=VAGGA_5,
    meta_title="AN 6.49 — With Khema | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Khemasutta, where two "
        "mendicants independently state opposite-sounding descriptions of an awakened mind, "
        "both approved, and the Buddha explains why neither involves the self at all. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery"),
        ("Speakers", "Venerable Khema, then Venerable Sumana, each independently addressing "
                     "the Buddha; then the Buddha, addressing the mendicants"),
        ("Form", "Two sequential, seemingly contradictory statements, both approved, followed "
                 "by the Buddha's explanation and closing verse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Declarations of enlightenment framed without reference to "
                              "self-comparison recur in related form across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;#9734;&#9734; &mdash; deceptively simple in form, "
                       "genuinely subtle in what it is actually claiming"),
    ],
    why=(
        "Khema and Sumana, arriving separately, each state something to the Buddha that sounds "
        "like the opposite of the other: Khema says an awakened mendicant does not think "
        "&ldquo;there is someone better, equal, or worse than me,&rdquo; while Sumana says an "
        "awakened mendicant does not think &ldquo;there is no-one better, equal, or worse than "
        "me.&rdquo; Both receive the Buddha's approval. Only after both have left does he "
        "explain to the assembly why neither statement actually contradicts the other."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who is perfected does not represent themselves as being among "
            "superiors, inferiors, or equals in any direction &mdash; not by claiming such "
            "comparisons exist for them, and not by claiming such comparisons don't exist "
            "&mdash; because for someone truly awakened, the whole framework of self-comparison "
            "no longer applies."]),
        ("Two statements that sound opposed, but are not", [
            "Read quickly, Khema's &ldquo;does not think 'there is someone better, equal, or "
            "worse than me'&rdquo; and Sumana's &ldquo;does not think 'there is no-one better, "
            "equal, or worse than me'&rdquo; look like a direct contradiction &mdash; one "
            "denying comparison exists, the other denying comparison doesn't exist. The "
            "Buddha's later comment resolves this: both statements deny that the awakened mind "
            "engages in ranking at all, whether the ranking concludes in the mendicant's favor, "
            "against them, or as absent."]),
        ("Speaking of the goal without involving the self", [
            "The Buddha's own gloss is precise: &ldquo;this is how gentlemen declare "
            "enlightenment. The goal is spoken of, but the self is not involved.&rdquo; Khema "
            "and Sumana both describe the attainment accurately without smuggling in any "
            "self-referential comparison &mdash; not even the comparison that denies "
            "comparison. Their statements work as declarations precisely because neither "
            "requires the speaker to locate themselves on a scale relative to anyone."]),
        ("A warning against false declaration", [
            "Immediately after praising Khema and Sumana's manner of speaking, the Buddha adds "
            "an unusually sharp aside: &ldquo;it seems that there are some futile men here who "
            "declare enlightenment as a joke. Later they will fall into distress.&rdquo; The "
            "praise of the correct form is paired directly with a warning about its abuse, "
            "distinguishing genuine declaration from performance."]),
        ("Why two mendicants, arriving separately, matters", [
            "The discourse's structure &mdash; two speakers, arriving one after the other, each "
            "unaware of what the other said &mdash; is doing real work. If either statement "
            "alone had been approved, a reader might mistake it for the single correct formula. "
            "Presenting both, independently approved, in apparently opposite phrasing, forces "
            "the recognition that the content approved of is not the specific wording but the "
            "underlying absence of self-comparison."]),
    ],
    terms=[
        ("khīṇāsava",
         "&ldquo;one whose defilements are ended&rdquo; &mdash; part of the standard formula "
         "both Khema and Sumana use to describe the perfected mendicant."),
        ("seyyo, sadiso, hīno",
         "&ldquo;better, equal, worse&rdquo; &mdash; the three-way comparison both statements "
         "deny applies to the awakened mind, whether affirmed or denied."),
        ("attā na upanīyati",
         "&ldquo;the self is not involved&rdquo; &mdash; the Buddha's own gloss on how "
         "gentlemen properly declare enlightenment."),
        ("aññaṁ byākaroti",
         "&ldquo;declares enlightenment&rdquo; &mdash; the act both Khema and Sumana are said "
         "to be engaged in, distinguished from mere boasting."),
        ("moghapurisā",
         "&ldquo;futile men&rdquo; &mdash; the Buddha's term for those who declare "
         "enlightenment insincerely, warned they will later fall into distress."),
    ],
    text_intro=(
        "The discourse in full: Khema's statement, Sumana's statement, and the Buddha's "
        "explanation and closing verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Khema's statement"),
        ("p", "&sect;1", "an6.49:2.1-2.5"),
        ("h3", "Sumana's statement"),
        ("p", "&sect;2", "an6.49:3.1-3.6"),
        ("h3", "The Buddha's explanation, in prose and verse"),
        ("p", "&sect;3", "an6.49:4.1-5.4"),
    ],
    quiz=[
        {"q": "What does Khema say an awakened mendicant does not think?",
         "opts": [
             "'There is no-one better, equal, or worse than me'",
             "'There is someone better than me, or equal to me, or worse than me'",
             "'I have attained enlightenment'",
             "'I am superior to all other mendicants'"],
         "correct": 1,
         "expl": "A denial that self-ranking comparisons apply."},
        {"q": "What does Sumana say, and how does it sound compared to Khema's statement?",
         "opts": [
             "The identical statement, word for word",
             "The seemingly opposite claim: an awakened mendicant does not think 'there is "
             "no-one better than me, or equal to me, or worse than me'",
             "That enlightenment does not exist",
             "That comparison is essential to awakening"],
         "correct": 1,
         "expl": "Read quickly, the two statements look like a direct contradiction."},
        {"q": "How does the Buddha resolve the apparent contradiction?",
         "opts": [
             "By declaring one of the two mendicants mistaken",
             "By explaining that both statements deny the awakened mind engages in ranking at "
             "all — whether the ranking favors, disfavors, or is simply absent for the speaker",
             "By ignoring the tension entirely",
             "By asking them to debate each other"],
         "correct": 1,
         "expl": "Neither statement smuggles in a comparison, even one that denies comparison."},
        {"q": "What is the Buddha's precise gloss on proper declaration of enlightenment?",
         "opts": [
             "'The self is central to the declaration'",
             "'The goal is spoken of, but the self is not involved'",
             "'Only silence is an acceptable declaration'",
             "'Declaration should always include a comparison to others'"],
         "correct": 1,
         "expl": "The core principle both Khema's and Sumana's statements satisfy."},
        {"q": "What warning does the Buddha add immediately after praising the two mendicants?",
         "opts": [
             "That declaring enlightenment is always forbidden",
             "That some 'futile men' declare enlightenment as a joke, and will later fall into "
             "distress",
             "That only senior mendicants may ever declare enlightenment",
             "No warning is given"],
         "correct": 1,
         "expl": "A sharp distinction between genuine declaration and its abuse."},
        {"q": "Why does the guide say the two-speaker structure matters?",
         "opts": [
             "It has no particular significance",
             "Presenting both statements, independently approved and apparently opposite, "
             "forces recognition that what's approved is the underlying absence of "
             "self-comparison, not one specific wording",
             "It shows the Buddha contradicting himself",
             "It proves Khema was correct and Sumana was mistaken"],
         "correct": 1,
         "expl": "If only one statement had been given, a reader might mistake its specific "
                 "phrasing for the essential content."},
        {"q": "Where is AN 6.49 set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Sāvatthī, in Jeta's Grove, Anāthapiṇḍika's monastery",
             "The land of the Cetis, at Sahajāti",
             "Near Kimbilā"],
         "correct": 1,
         "expl": "The setting most Aṅguttara discourses default to."},
        {"q": "What does <em>moghapurisā</em> mean?",
         "opts": ["Wise ones", "Futile men", "Senior disciples", "Deities"],
         "correct": 1,
         "expl": "The Buddha's term for those who falsely declare enlightenment."},
        {"q": "What do both Khema and Sumana do after speaking, before the Buddha's comment?",
         "opts": [
             "They remain to debate the point",
             "Each bows, respectfully circles the Buddha, and leaves — neither hears the "
             "other's statement or the Buddha's later explanation",
             "They argue with each other directly",
             "They ask the Buddha to judge which of them is correct"],
         "correct": 1,
         "expl": "The Buddha's explanation to the assembly comes only after both have already "
                 "departed."},
        {"q": "What three-way comparison does the whole discourse concern?",
         "opts": [
             "Rich, middle, and poor",
             "Better, equal, and worse (seyyo, sadiso, hīno)",
             "Young, middle-aged, and old",
             "Lay, novice, and senior"],
         "correct": 1,
         "expl": "The comparison both statements deny applies to the awakened mind in any "
                 "direction."},
    ],
    marginalia=[
        ("Two statements", [
            "Khema: no comparison",
            "exists for me",
            "Sumana: no absence",
            "of comparison, either",
        ]),
        ("Both approved", [
            "neither contradicts",
            "the other — both deny",
            "self-ranking altogether",
        ]),
        ("The Buddha's gloss", [
            "'the goal is spoken of,",
            "but the self is",
            "not involved'",
        ]),
        ("Cross-references", [
            "AN 6.48 &middot; previous, on verification",
        ]),
    ],
    further=[
        '<a href="%s/an6.49/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.50.html">AN 6.50 &middot; Sense Restraint</a> &mdash; next, a chain of '
        "conditions from restraint to freedom.",
        '<a href="an-6.48.html">AN 6.48 &middot; Apparent in the Present Life (2nd)</a> &mdash; '
        "previous, a different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.50 — Indriyasaṁvarasutta
# --------------------------------------------------------------------------- #
page(
    50, "Indriyasaṁvara", "Sense Restraint",
    vagga=VAGGA_5,
    meta_title="AN 6.50 — Sense Restraint | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Indriyasaṁvarasutta, "
        "which chains sense restraint through ethics, right immersion, true knowledge, and "
        "disillusionment to freedom, each step a destroyed or fulfilled condition for the "
        "next. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A five-step chain of conditions, stated first as sequential destruction, "
                 "then as sequential fulfillment, each closed with a tree simile"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Chains of conditions from sense restraint to liberation recur "
                              "widely across the Chinese Āgamas as a standard structure of the "
                              "path; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a precisely engineered "
                       "conditional chain, worth tracing link by link"),
    ],
    why=(
        "AN 6.50 states a five-step dependency with unusual precision: without sense restraint, "
        "a vital condition for ethical conduct is destroyed; without ethics, a vital condition "
        "for right immersion; without right immersion, for true knowledge and vision; without "
        "true knowledge, for disillusionment and dispassion; without disillusionment, for "
        "knowledge and vision of freedom. The discourse then states the identical chain "
        "positively, and illustrates both directions with the same simile of a tree."),
    guide=[
        ("The teaching in one sentence", [
            "Sense restraint is a vital condition for ethical conduct, ethical conduct for "
            "right immersion, right immersion for true knowledge and vision, true knowledge "
            "and vision for disillusionment and dispassion, and disillusionment and dispassion "
            "for knowledge and vision of freedom &mdash; each stage destroyed if the one before "
            "it is missing, fulfilled if the one before it is fulfilled."]),
        ("A chain, not a list of equally weighted virtues", [
            "Unlike many of this chapter's six-item lists, this discourse names five stages in "
            "an explicit dependency relationship, each stated to be a &ldquo;vital "
            "condition&rdquo; (<em>upanisā</em>) for the one after it. The structure is closer "
            "to a causal argument than an inventory: sense restraint is not simply one virtue "
            "among several but the specific foundation without which the next stage cannot "
            "arise at all."]),
        ("Both directions stated in full, not left to inference", [
            "The discourse does not state the destructive chain and leave the constructive one "
            "implicit. It restates the entire five-step sequence a second time in positive "
            "form &mdash; fulfilled sense restraint fulfilling ethics, fulfilled ethics "
            "fulfilling immersion, and so on &mdash; giving both directions equal, explicit "
            "treatment rather than trusting the reader to reverse the logic unaided."]),
        ("A tree with no branches or foliage", [
            "The shared simile closing both halves of the discourse pictures a tree lacking "
            "branches and foliage, whose &ldquo;shoots, bark, softwood, and heartwood would not "
            "grow to fullness&rdquo; &mdash; and, in the positive half, a tree complete with "
            "branches and foliage, whose parts all grow to fullness. The image locates the "
            "damage or growth not at one single point but distributed through the whole "
            "structure, consistent with the discourse's chain logic: a break anywhere upstream "
            "affects everything downstream."]),
        ("Where the chain ends, and why that matters", [
            "The final stage, &ldquo;knowledge and vision of freedom&rdquo; "
            "(<em>vimuttiñāṇadassana</em>), is the terminus of the whole sequence, not merely "
            "one more link. Everything from sense restraint onward is oriented toward this end "
            "point; the discourse's structure makes clear that sense restraint, the most modest-"
            "sounding item in the chain, is nonetheless the condition on which the entire "
            "sequence, up to and including final freedom, depends."]),
    ],
    terms=[
        ("indriyasaṁvara",
         "&ldquo;sense restraint&rdquo; &mdash; the discourse's own title and the first, "
         "foundational link in the chain."),
        ("upanisā",
         "&ldquo;vital condition,&rdquo; &ldquo;proximate cause&rdquo; &mdash; the relationship "
         "each stage is said to bear to the one following it."),
        ("sammāsamādhi",
         "&ldquo;right immersion&rdquo; &mdash; the third link, dependent on ethical conduct "
         "and itself a condition for true knowledge."),
        ("yathābhūtañāṇadassana",
         "&ldquo;true knowledge and vision&rdquo; &mdash; the fourth link, seeing things as "
         "they actually are."),
        ("vimuttiñāṇadassana",
         "&ldquo;knowledge and vision of freedom&rdquo; &mdash; the fifth and final link, the "
         "terminus the entire chain is oriented toward."),
    ],
    text_intro=(
        "The discourse in full: the five-step chain stated as destruction, then restated as "
        "fulfillment, each with its tree simile. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The chain of destruction"),
        ("p", "&sect;1", "an6.50:1.1-1.9"),
        ("h3", "The chain of fulfillment"),
        ("p", "&sect;2", "an6.50:2.1-2.8"),
    ],
    quiz=[
        {"q": "What five stages does this discourse chain together?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom",
             "Sense restraint, ethical conduct, right immersion, true knowledge and vision, "
             "disillusionment and dispassion — leading to knowledge and vision of freedom",
             "Seeing, listening, acquisition, training, service",
             "The five hindrances"],
         "correct": 1,
         "expl": "A five-step dependency chain culminating in freedom."},
        {"q": "How does the guide characterize this discourse's structure compared to many "
              "other six-item lists in this chapter?",
         "opts": [
             "Identical — a flat inventory of equally weighted items",
             "A causal chain, not a list of equally weighted virtues — each stage explicitly a "
             "'vital condition' for the one after it",
             "A random assortment with no logical relationship",
             "A single item repeated five times"],
         "correct": 1,
         "expl": "Sense restraint is the foundation without which the next stage cannot arise."},
        {"q": "Does the discourse leave the positive chain to be inferred from the negative "
              "one?",
         "opts": [
             "Yes, only the destructive chain is stated",
             "No — the entire five-step sequence is restated in full positive form, giving both "
             "directions equal, explicit treatment",
             "Only the positive chain is stated",
             "Neither direction is stated explicitly"],
         "correct": 1,
         "expl": "Both halves are given complete, parallel treatment."},
        {"q": "What image does the shared simile use?",
         "opts": [
             "A river and its tributaries",
             "A tree lacking or complete with branches and foliage, whose parts fail to grow or "
             "grow fully depending on that completeness",
             "A chariot with missing wheels",
             "A house without a foundation"],
         "correct": 1,
         "expl": "Damage or growth distributed through the whole structure, matching the "
                 "chain's own logic."},
        {"q": "What is the final stage of the chain, and what does the guide say about its "
              "role?",
         "opts": [
             "Ethical conduct, which is treated as the ultimate goal",
             "Knowledge and vision of freedom — the terminus the entire sequence, from sense "
             "restraint onward, is oriented toward",
             "Right immersion, treated as sufficient on its own",
             "The discourse does not specify a final stage"],
         "correct": 1,
         "expl": "Vimuttiñāṇadassana closes the chain that begins with the most modest-sounding "
                 "item."},
        {"q": "What does <em>upanisā</em> mean?",
         "opts": ["An unrelated virtue", "A vital condition, proximate cause", "A type of "
                  "meditative absorption", "A ritual offering"],
         "correct": 1,
         "expl": "The specific relationship each stage bears to the one following it."},
        {"q": "Is a setting stated for AN 6.50?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "A bare formula stating the chain directly."},
        {"q": "What does <em>sammāsamādhi</em> mean?",
         "opts": ["Right view", "Right immersion", "Right speech", "Right livelihood"],
         "correct": 1,
         "expl": "The third link, dependent on ethical conduct."},
        {"q": "What is the relationship between the destructive and constructive halves of "
              "this discourse?",
         "opts": [
             "They describe entirely unrelated processes",
             "They are the identical five-step chain, stated once as sequential destruction and "
             "once as sequential fulfillment",
             "The constructive half contradicts the destructive half",
             "Only three of the five stages are shared between them"],
         "correct": 1,
         "expl": "A single chain given in both its negative and positive forms."},
        {"q": "What is the first, foundational link in the chain?",
         "opts": ["Ethical conduct", "Sense restraint", "Right immersion", "True knowledge"],
         "correct": 1,
         "expl": "The discourse's own title and starting point, on which everything downstream "
                 "depends."},
    ],
    marginalia=[
        ("The five-step chain", [
            "sense restraint &rarr;",
            "ethics &rarr; right immersion &rarr;",
            "true knowledge &rarr;",
            "disillusionment &rarr; freedom",
        ]),
        ("Both directions given", [
            "destruction, stated in full",
            "fulfillment, restated",
            "in full — not inferred",
        ]),
        ("A tree simile", [
            "no branches, no growth",
            "full branches, full growth —",
            "damage spreads throughout",
        ]),
        ("Cross-references", [
            "AN 6.49 &middot; previous, on declaring awakening",
        ]),
    ],
    further=[
        '<a href="%s/an6.50/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.51.html">AN 6.51 &middot; With Ānanda</a> &mdash; next, Ānanda&rsquo;s '
        "own practice, described by Sāriputta.",
        '<a href="an-6.49.html">AN 6.49 &middot; With Khema</a> &mdash; previous, a different '
        "register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.51 — Ānandasutta
# --------------------------------------------------------------------------- #
page(
    51, "Ānanda", "With Ānanda",
    vagga=VAGGA_5,
    meta_title="AN 6.51 — With Ānanda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ānandasutta, where "
        "Ānanda, pressed by Sāriputta to answer his own question, describes the method he "
        "uses to hear, remember, exercise, and understand the teaching. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Ānanda and Sāriputta, in dialogue"),
        ("Form", "A fourfold question, a deflection, and Ānanda's own answer, praised as "
                 "describing Ānanda's own six qualities"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Ānanda's methodical retention of the teaching is recognized "
                              "widely across Buddhist tradition, including the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a practical, methodical "
                       "discourse describing a real workflow for retaining a teaching"),
    ],
    why=(
        "Ānanda asks Sāriputta a fourfold question about how a mendicant comes to hear, "
        "remember, exercise, and understand teachings &mdash; and Sāriputta, recognizing "
        "Ānanda's own learning, turns the question back on him. What Ānanda describes is not "
        "an abstract account of memory but a concrete method: memorize, teach and recite in "
        "detail, reflect internally, then specifically seek out senior mendicants during the "
        "rains retreat to ask direct questions and resolve doubts."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant comes to hear, remember, exercise, and understand teachings by "
            "memorizing them, teaching and reciting them in detail to others, reflecting on "
            "them internally, and then deliberately seeking out learned senior mendicants "
            "during the rains retreat to ask direct questions that reveal what is hidden and "
            "resolve doubt."]),
        ("Sāriputta's redirection, and what it implies", [
            "Sāriputta's reply &mdash; &ldquo;you're very learned. Why don't you clarify this "
            "yourself?&rdquo; &mdash; is not evasion but recognition: he treats Ānanda's own "
            "question as already answered by Ānanda's reputation and practice, and asks him to "
            "make explicit what he already does. The structure lets the discourse's content "
            "arrive as Ānanda's self-description rather than as instruction handed down from "
            "someone else."]),
        ("A method with distinct, sequential stages", [
            "Ānanda's answer names several discrete steps rather than a single technique: "
            "memorization of the full range of textual genres, active teaching and recitation "
            "of what was learned, internal reflection and examination, and &mdash; the step "
            "that makes the whole method complete &mdash; deliberately placing himself among "
            "&ldquo;senior mendicants who are very learned&hellip; who have memorized the "
            "teachings, the monastic law, and the outlines,&rdquo; specifically in order to ask "
            "them questions."]),
        ("Questions as the completing step, not an afterthought", [
            "The method's final and arguably decisive move is not solitary study but a "
            "deliberate social act: seeking out those with greater learning during the rains "
            "retreat and asking, plainly, &ldquo;why, sir, does it say this? What does that "
            "mean?&rdquo; The discourse credits the senior mendicants' answers &mdash; "
            "revealing what is hidden, clarifying what is unclear, dispelling doubt &mdash; as "
            "what actually completes the process of understanding, not merely supplementing "
            "it."]),
        ("Sāriputta's closing verdict, naming six qualities", [
            "Sāriputta's response treats Ānanda's answer as a description of Ānanda's own "
            "person: &ldquo;we will remember Venerable Ānanda as someone who possesses these "
            "six qualities.&rdquo; The discourse closes by restating each element of the method "
            "as an attribute Ānanda himself demonstrably has, turning what began as a "
            "hypothetical question into direct, specific praise."]),
    ],
    terms=[
        ("suttaṁ geyyaṁ veyyākaraṇaṁ gāthaṁ udānaṁ itivuttakaṁ jātakaṁ abbhutadhammaṁ "
         "vedallaṁ",
         "&ldquo;statements, mixed prose and verse, discussions, verses, inspired exclamations, "
         "legends, stories of past lives, amazing stories, and elaborations&rdquo; &mdash; the "
         "full range of textual genres Ānanda describes memorizing."),
        ("vassaṁ upagacchati",
         "&ldquo;enters the rains retreat&rdquo; &mdash; the specific occasion Ānanda names for "
         "deliberately seeking out learned senior mendicants."),
        ("chinnaṁ pariyāyaṁ vivaranti",
         "not a single compound in this translation but the sense of &ldquo;reveal what is "
         "hidden&rdquo; &mdash; what the questioned senior mendicants are said to do in "
         "response."),
        ("bahussuta",
         "&ldquo;very learned&rdquo; &mdash; how Sāriputta describes Ānanda at the discourse's "
         "opening, and the quality the senior mendicants sought out are said to share."),
        ("dhammadharā vinayadharā mātikādharā",
         "&ldquo;inheritors of the heritage, who have memorized the teachings, the monastic "
         "law, and the outlines&rdquo; &mdash; the specific credentials of the senior "
         "mendicants Ānanda seeks out."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's fourfold question to Sāriputta, and his own detailed "
        "answer. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda's question, and Sāriputta's redirection"),
        ("p", "&sect;1", "an6.51:2.1-2.6"),
        ("h3", "Ānanda's method, in detail"),
        ("p", "&sect;2", "an6.51:3.1-3.8"),
        ("h3", "Sāriputta's praise"),
        ("p", "&sect;3", "an6.51:4.1-4.9"),
    ],
    quiz=[
        {"q": "What fourfold question does Ānanda ask Sāriputta?",
         "opts": [
             "How to develop psychic power",
             "How a mendicant gets to hear a new teaching, remembers it, keeps exercising it, "
             "and comes to understand what wasn't understood before",
             "How many topics for recollection there are",
             "How to resolve disputes within the Saṅgha"],
         "correct": 1,
         "expl": "A question about the whole process of learning and retaining teachings."},
        {"q": "How does Sāriputta respond to Ānanda's question?",
         "opts": [
             "He answers it directly himself",
             "He redirects it back to Ānanda, recognizing that Ānanda's own learning and "
             "practice already answer it",
             "He refuses to engage with the question",
             "He declares the question unanswerable"],
         "correct": 1,
         "expl": "Not evasion but recognition of Ānanda's own demonstrated expertise."},
        {"q": "What stages does Ānanda's described method include?",
         "opts": [
             "Only silent memorization",
             "Memorization of the full range of textual genres, active teaching and recitation, "
             "internal reflection, and deliberately seeking out learned seniors to ask "
             "questions during the rains retreat",
             "Only asking questions of senior mendicants, with no prior study",
             "Formal debate with wanderers of other sects"],
         "correct": 1,
         "expl": "A sequential method with several distinct, described steps."},
        {"q": "What does the guide identify as the method's completing step?",
         "opts": [
             "Memorization alone",
             "The deliberate, social act of seeking out learned seniors during the rains "
             "retreat and asking direct questions, whose answers reveal what is hidden and "
             "resolve doubt",
             "Teaching others without ever asking questions",
             "Physical relocation to a new monastery"],
         "correct": 1,
         "expl": "Credited as what actually completes the process, not merely supplementing it."},
        {"q": "How does Sāriputta close the discourse?",
         "opts": [
             "By declaring Ānanda's answer incorrect",
             "By restating each element of Ānanda's described method as a quality Ānanda "
             "himself demonstrably possesses",
             "By asking a further, unrelated question",
             "By remaining silent"],
         "correct": 1,
         "expl": "Turning the hypothetical method into direct, specific praise of Ānanda."},
        {"q": "What specific occasion does Ānanda name for seeking out learned seniors?",
         "opts": [
             "Any time at all, with no particular occasion specified",
             "The rains retreat (vassa), spent in a monastery with senior mendicants who are "
             "very learned",
             "Only during almsround",
             "Only at the start of ordination"],
         "correct": 1,
         "expl": "A specific, recurring seasonal occasion for this deliberate practice."},
        {"q": "What does <em>bahussuta</em> mean?",
         "opts": ["Newly ordained", "Very learned", "Skilled in psychic power", "A lay follower"],
         "correct": 1,
         "expl": "How Sāriputta describes both Ānanda and the senior mendicants he seeks out."},
        {"q": "Is a setting stated for AN 6.51?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "A bare dialogue between two named senior disciples."},
        {"q": "What kind of questions does Ānanda ask the senior mendicants he consults?",
         "opts": [
             "Only questions about monastic discipline",
             "Direct questions such as 'why, sir, does it say this? What does that mean?'",
             "Only rhetorical questions requiring no answer",
             "Questions about their personal history"],
         "correct": 1,
         "expl": "Concrete requests for clarification on specific points of the teaching."},
        {"q": "What textual genres does Ānanda describe memorizing?",
         "opts": [
             "Only verse compositions",
             "A full range including statements, mixed prose and verse, discussions, inspired "
             "exclamations, legends, and elaborations",
             "Only monastic law",
             "Only stories of the Buddha's past lives"],
         "correct": 1,
         "expl": "A comprehensive list of the canon's recognized textual categories."},
    ],
    marginalia=[
        ("Ānanda's method", [
            "memorize &middot; teach",
            "&amp; recite &middot; reflect",
            "&middot; ask senior mendicants",
        ]),
        ("Not evasion", [
            "Sāriputta recognizes",
            "Ānanda's own learning —",
            "redirects, doesn't refuse",
        ]),
        ("The completing step", [
            "not solitary study —",
            "a deliberate question",
            "asked of a senior",
        ]),
        ("Cross-references", [
            "AN 6.50 &middot; previous, a chain of conditions",
        ]),
    ],
    further=[
        '<a href="%s/an6.51/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.52.html">AN 6.52 &middot; Aristocrats</a> &mdash; next, a '
        "brahmin&rsquo;s question about six kinds of people&rsquo;s ambitions.",
        '<a href="an-6.50.html">AN 6.50 &middot; Sense Restraint</a> &mdash; previous, a '
        "different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.52 — Khattiyasutta
# --------------------------------------------------------------------------- #
page(
    52, "Khattiya", "Aristocrats",
    vagga=VAGGA_5,
    meta_title="AN 6.52 — Aristocrats | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Khattiyasutta, where "
        "the brahmin Jānussoṇi asks the Buddha to name the ambition, preoccupation, fixation, "
        "insistence, and goal of six kinds of people, ending with ascetics themselves. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "The brahmin Jānussoṇi, questioning the Buddha"),
        ("Form", "The same five-part question asked six times in a row, for six different "
                 "social categories"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Sociological characterizations of different social roles recur "
                              "in related forms across the Chinese Āgamas; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a clear, almost taxonomic "
                       "discourse, notable for including the questioner's own category among "
                       "the six"),
    ],
    why=(
        "Jānussoṇi asks the same five-part question six times over &mdash; ambition, "
        "preoccupation, fixation, insistence, and ultimate goal &mdash; applied in turn to "
        "aristocrats, brahmins, householders, women, bandits, and finally ascetics. The Buddha "
        "answers each with the identical formulaic precision, producing a compact social "
        "taxonomy that treats brahmins (Jānussoṇi's own category) and even ascetics (the "
        "Buddha's own) with the same detached, descriptive method as bandits."),
    guide=[
        ("The teaching in one sentence", [
            "Aristocrats aim at wealth and authority through power and territory; brahmins aim "
            "at wealth and the realm of divinity through hymns and sacrifice; householders aim "
            "at wealth and finished work through their profession; women aim at a husband and "
            "authority through children and freedom from rivalry; bandits aim at theft and "
            "invisibility through stealth and darkness; and ascetics aim at patience and "
            "extinguishment through ethical conduct and owning nothing."]),
        ("One fixed question, applied without favoritism", [
            "The five-part question &mdash; ambition, preoccupation, fixation, insistence, "
            "ultimate goal &mdash; is asked in identical form for all six categories, and the "
            "Buddha answers each with the same structural precision. Notably, the discourse "
            "does not exempt Jānussoṇi's own category, brahmins, from the same descriptive "
            "treatment given to bandits, nor does it treat ascetics &mdash; the Buddha's own "
            "category &mdash; with special reverence in form, only in content."]),
        ("Wealth as the shared ambition of four of the six", [
            "Aristocrats, brahmins, householders, and even bandits (via theft) share wealth or "
            "its equivalent as their named ambition, differing chiefly in method and ultimate "
            "goal: power and territory for aristocrats, sacrifice and divinity for brahmins, "
            "professional completion for householders, invisibility for bandits. Only women and "
            "ascetics are described with an ambition not centered on wealth &mdash; a husband, "
            "in one case, and patience and gentleness, in the other."]),
        ("Ascetics named last, and answered without exception", [
            "The list's final category, ascetics, receives the Buddha's answer in exactly the "
            "same form as the other five: preoccupied with wisdom (shared, notably, with "
            "aristocrats, brahmins, and householders), fixated on ethical conduct, insisting on "
            "owning nothing, with extinguishment as the culmination. The Buddha does not step "
            "outside the taxonomy to describe his own path; he answers within its terms."]),
        ("A question that closes on conversion, as several in this chapter do", [
            "As with AN 6.38, 6.47, and 6.48, this discourse ends with Jānussoṇi declaring "
            "himself amazed and going for refuge for life &mdash; persuaded, in this case, not "
            "by a doctrinal argument but by the precision and evident insight of a purely "
            "descriptive social analysis."]),
    ],
    terms=[
        ("khattiya",
         "&ldquo;aristocrat,&rdquo; the warrior-ruler class &mdash; the first category "
         "analyzed, giving the discourse its title."),
        ("adhippāya, upavicāra, adhiṭṭhāna, abhinivesa, pariyosāna",
         "&ldquo;ambition, preoccupation, fixation, insistence, ultimate goal&rdquo; &mdash; "
         "the fixed five-part framework applied identically to all six categories."),
        ("brāhmaṇa",
         "&ldquo;brahmin&rdquo; &mdash; the second category, and Jānussoṇi's own, analyzed "
         "with the same method as every other."),
        ("samaṇa",
         "&ldquo;ascetic&rdquo; &mdash; the sixth and final category, the Buddha's own, "
         "answered within the same taxonomy rather than set apart from it."),
        ("khantisoraccādhippāyā",
         "&ldquo;have patience and gentleness as their ambition&rdquo; &mdash; the specific "
         "answer given for ascetics, distinct from the wealth-centered ambitions of four of the "
         "other five."),
    ],
    text_intro=(
        "The discourse in full: Jānussoṇi's six repeated questions, and the Buddha's six "
        "matching answers. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Aristocrats and brahmins"),
        ("p", "&sect;1", "an6.52:2.1-3.2"),
        ("h3", "Householders and women"),
        ("p", "&sect;2", "an6.52:4.1-5.2"),
        ("h3", "Bandits and ascetics"),
        ("p", "&sect;3", "an6.52:6.1-8.4"),
    ],
    quiz=[
        {"q": "What five-part question does Jānussoṇi ask about each of six categories?",
         "opts": [
             "Their age, wealth, family, occupation, and religion",
             "Their ambition, preoccupation, fixation, insistence, and ultimate goal",
             "Their strengths, weaknesses, opportunities, threats, and outcomes",
             "Their name, birthplace, teacher, students, and reputation"],
         "correct": 1,
         "expl": "An identical five-part framework applied to all six categories in turn."},
        {"q": "What are the six categories analyzed?",
         "opts": [
             "The five faculties plus one power",
             "Aristocrats, brahmins, householders, women, bandits, and ascetics",
             "Monks, nuns, laymen, laywomen, novices, and lay donors",
             "Kings, queens, ministers, generals, merchants, and farmers"],
         "correct": 1,
         "expl": "A broad social taxonomy including the questioner's own category and the "
                 "Buddha's."},
        {"q": "What does the guide note about how brahmins (Jānussoṇi's own category) are "
              "treated?",
         "opts": [
             "They are exempted from the analysis out of respect",
             "They receive the identical descriptive treatment as every other category, "
             "including bandits — no favoritism shown to the questioner's own group",
             "They are singled out for special praise",
             "The discourse refuses to characterize brahmins at all"],
         "correct": 1,
         "expl": "The same structural precision applied without exception."},
        {"q": "What ambition do four of the six categories share, according to the Buddha's "
              "answers?",
         "opts": [
             "Wisdom", "Wealth (or its equivalent, such as theft for bandits)", "Patience", "A "
             "husband"],
         "correct": 1,
         "expl": "Aristocrats, brahmins, householders, and bandits — differing chiefly in "
                 "method and ultimate goal."},
        {"q": "How does the Buddha answer for the ascetic category — his own — compared to the "
              "other five?",
         "opts": [
             "He refuses to characterize ascetics",
             "In exactly the same form as the other five, answering within the taxonomy's own "
             "terms rather than stepping outside it",
             "With a much longer, more elaborate answer than any other category",
             "By declaring ascetics superior to all other categories"],
         "correct": 1,
         "expl": "Patience and gentleness as ambition, ethical conduct as fixation, owning "
                 "nothing as insistence, extinguishment as culmination — structurally identical "
                 "to the other answers."},
        {"q": "How does this discourse end?",
         "opts": [
             "With Jānussoṇi unpersuaded",
             "With Jānussoṇi declaring himself amazed and going for refuge for life",
             "With an unresolved debate",
             "With the Buddha refusing to answer the final category"],
         "correct": 1,
         "expl": "Matching the conversion pattern already seen at AN 6.38, 6.47, and 6.48."},
        {"q": "What is named as women's ambition, distinct from the wealth-centered answers "
              "given for most other categories?",
         "opts": [
             "Wealth and power", "A man (husband)", "Sacrifice", "Invisibility"],
         "correct": 1,
         "expl": "One of only two categories (with ascetics) not centered on wealth."},
        {"q": "Is a setting stated for AN 6.52?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "A bare dialogue with no scene-setting clause."},
        {"q": "What is named as bandits' ultimate goal?",
         "opts": ["Authority", "Divinity", "Invisibility", "Extinguishment"],
         "correct": 2,
         "expl": "Fixated on their sword, insisting on darkness, aiming ultimately at going "
                 "unseen."},
        {"q": "What does <em>samaṇa</em> mean?",
         "opts": ["Aristocrat", "Ascetic", "Brahmin", "Bandit"],
         "correct": 1,
         "expl": "The sixth and final category, the Buddha's own, analyzed within the same "
                 "taxonomic method."},
    ],
    marginalia=[
        ("Six categories", [
            "aristocrats &middot; brahmins",
            "householders &middot; women",
            "bandits &middot; ascetics",
        ]),
        ("One fixed question", [
            "ambition &middot; preoccupation",
            "fixation &middot; insistence",
            "ultimate goal",
        ]),
        ("No favoritism", [
            "brahmins (the questioner's",
            "own group) get the same",
            "treatment as bandits",
        ]),
        ("Cross-references", [
            "AN 6.51 &middot; previous, Ānanda's method",
        ]),
    ],
    further=[
        '<a href="%s/an6.52/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.53.html">AN 6.53 &middot; Diligence</a> &mdash; next, six similes for '
        "one supreme quality.",
        '<a href="an-6.51.html">AN 6.51 &middot; With Ānanda</a> &mdash; previous, a different '
        "register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.53 — Appamādasutta
# --------------------------------------------------------------------------- #
page(
    53, "Appamāda", "Diligence",
    vagga=VAGGA_5,
    meta_title="AN 6.53 — Diligence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Appamādasutta, where "
        "a brahmin asks for the one thing that secures benefit in this life and lives to come, "
        "and the Buddha answers with diligence, illustrated through six similes of "
        "encompassing scale. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "A brahmin, questioning the Buddha"),
        ("Form", "A direct question for a single answer, followed by six similes each "
                 "illustrating the same claim of encompassing supremacy"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Diligence (appamāda) as the single quality the Buddha names on "
                              "his deathbed in the Mahāparinibbāna account recurs across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;#9734;&#9734;&#9734;&#9734; &mdash; a simple claim illustrated "
                       "six times over with vivid, easily pictured images"),
    ],
    why=(
        "A brahmin asks a pointed question: is there one thing, cultivated, that secures "
        "benefit both now and in future lives? The Buddha's answer is a single word, "
        "<em>appamāda</em>, diligence &mdash; and rather than arguing for the claim "
        "abstractly, he illustrates it six times over with images of one thing containing or "
        "surpassing many: an elephant's footprint holding every other footprint, a roof's peak "
        "where every rafter meets, the moon outshining every star."),
    guide=[
        ("The teaching in one sentence", [
            "Diligence is the one thing that, developed and cultivated, secures benefit for "
            "both this life and lives to come, illustrated by six similes each showing one "
            "thing that encompasses or surpasses many others of its kind."]),
        ("A question seeking exactly one answer", [
            "The brahmin's question is precise in its scope: not what secures the most "
            "benefit, or what is most important among many things, but whether there is "
            "<em>one</em> single thing sufficient on its own for both immediate and long-term "
            "good. The Buddha's answer matches that precision &mdash; a single word, given "
            "without qualification or a list of runners-up."]),
        ("Six similes, one shared logical shape", [
            "Every simile follows an identical pattern: many things of a kind are shown to be "
            "contained within, or subordinate to, one encompassing thing &mdash; every "
            "creature's footprint fits inside an elephant's; every rafter meets at the roof's "
            "peak; a reed-cutter gathers many reeds by their tops; every mango on a stalk "
            "follows when the stalk is cut; every lesser ruler is vassal to a wheel-turning "
            "monarch; every star's light together doesn't equal a sixteenth of the moon's. "
            "None of the six similes explains diligence directly; each instead demonstrates "
            "the logical shape the claim about diligence is meant to have."]),
        ("Six images, three different relationships", [
            "Though structurally similar, the six similes are not identical in the "
            "relationship they picture: the elephant's footprint and the rafters both show "
            "containment (many parts within or converging on one whole); the reed-cutter and "
            "the mango stalk show a single point of control that brings the rest along; the "
            "monarch and the moon show simple superiority of scale. Diligence is offered as "
            "playing all three roles at once &mdash; containing, controlling, and surpassing "
            "&mdash; rather than fitting only one of the three patterns."]),
        ("Elsewhere in the canon: the Buddha's own last word", [
            "<em>Appamāda</em> holds a distinctive place beyond this single discourse: the "
            "canon's account of the Buddha's final teaching before his death names diligence as "
            "his last recorded instruction to the assembled mendicants. This discourse's claim "
            "&mdash; one thing sufficient for benefit now and later &mdash; is not an isolated "
            "assertion but consistent with the weight the tradition gives this term at its most "
            "solemn moment."]),
    ],
    terms=[
        ("appamāda",
         "&ldquo;diligence,&rdquo; &ldquo;heedfulness&rdquo; &mdash; the discourse's own "
         "title and its single answer to the brahmin's question."),
        ("diṭṭhadhammika samparāyika attha",
         "&ldquo;benefit in this life&hellip; benefit in lives to come&rdquo; &mdash; the "
         "twofold scope of the brahmin's original question, both said to be secured by "
         "diligence alone."),
        ("hatthipada",
         "&ldquo;elephant's footprint&rdquo; &mdash; the first simile, in which every other "
         "creature's footprint is said to fit inside it."),
        ("cakkavattī",
         "&ldquo;wheel-turning monarch&rdquo; &mdash; the fifth simile's figure, to whom every "
         "lesser ruler is said to be a vassal."),
        ("candimā",
         "&ldquo;the moon&rdquo; &mdash; the sixth and final simile, whose radiance is said to "
         "outshine all the stars combined, sixteen times over."),
    ],
    text_intro=(
        "The discourse in full: the brahmin's question, and the Buddha's answer illustrated "
        "with six similes. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A brahmin's question, and the Buddha's answer"),
        ("p", "&sect;1", "an6.53:2.1-3.2"),
        ("h3", "Six similes"),
        ("p", "&sect;2", "an6.53:4.1-10.1"),
        ("h3", "The conclusion"),
        ("p", "&sect;3", "an6.53:11.1-11.2"),
    ],
    quiz=[
        {"q": "What question does the brahmin ask the Buddha?",
         "opts": [
             "How many topics for recollection there are",
             "Whether there is one thing that, developed and cultivated, secures benefit for "
             "both this life and lives to come",
             "How to develop psychic power",
             "Why aristocrats and brahmins differ in their ambitions"],
         "correct": 1,
         "expl": "A precisely scoped question seeking a single, sufficient answer."},
        {"q": "What single answer does the Buddha give?",
         "opts": [
             "Wisdom", "Diligence (appamāda)", "Generosity", "Faith"],
         "correct": 1,
         "expl": "A single word, without qualification or a list of alternatives."},
        {"q": "What shared logical shape do all six similes follow?",
         "opts": [
             "Each shows two equal and opposite things in balance",
             "Each shows many things of a kind contained within, or subordinate to, one "
             "encompassing thing",
             "Each shows a gradual process unfolding over time",
             "Each shows a debate between two figures"],
         "correct": 1,
         "expl": "A footprint containing all footprints, a peak where all rafters meet, and so "
                 "on."},
        {"q": "What three different relationships does the guide identify among the six "
              "similes, despite their shared structure?",
         "opts": [
             "All six show only containment, with no variation",
             "Containment (footprint, rafters), control that brings the rest along (reed-cutter, "
             "mango stalk), and simple superiority of scale (monarch, moon)",
             "All six show only superiority of scale",
             "The six similes are unrelated to each other in structure"],
         "correct": 1,
         "expl": "Diligence is offered as playing all three roles at once."},
        {"q": "What does the guide note about diligence elsewhere in the canon?",
         "opts": [
             "It appears only in this single discourse",
             "It is named as the Buddha's last recorded instruction to the assembled "
             "mendicants before his death, in the Mahāparinibbāna account",
             "It is considered a minor, secondary virtue elsewhere",
             "It contradicts the Buddha's teaching elsewhere"],
         "correct": 1,
         "expl": "A term carrying distinctive weight at the most solemn moment recorded in the "
                 "canon."},
        {"q": "What does the elephant's footprint simile illustrate?",
         "opts": [
             "That elephants are dangerous",
             "That the footprints of all creatures that walk can fit inside an elephant's "
             "footprint",
             "That footprints fade over time",
             "That elephants cannot be tamed"],
         "correct": 1,
         "expl": "The first of the six similes, illustrating containment."},
        {"q": "What does the reed-cutter simile illustrate?",
         "opts": [
             "A gradual process of growth",
             "Grabbing many reeds at the top and shaking them all down together — a single "
             "point of control bringing the rest along",
             "The danger of sharp tools",
             "Patience in agricultural work"],
         "correct": 1,
         "expl": "One of two similes the guide groups as showing control rather than simple "
                 "containment."},
        {"q": "Is a setting stated for AN 6.53?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "A bare dialogue with no scene-setting clause."},
        {"q": "How does this discourse end?",
         "opts": [
             "With the brahmin remaining unconvinced",
             "With the brahmin declaring himself amazed and going for refuge for life",
             "With an unresolved debate",
             "With the Buddha declining to answer further"],
         "correct": 1,
         "expl": "Matching the conversion pattern of several discourses earlier in this chapter."},
        {"q": "What does <em>cakkavattī</em> mean?",
         "opts": [
             "A type of meditative absorption", "A wheel-turning monarch, to whom every lesser "
             "ruler is a vassal", "A senior mendicant", "A deity"],
         "correct": 1,
         "expl": "The fifth simile's figure, illustrating supreme authority."},
    ],
    marginalia=[
        ("Six similes", [
            "elephant's footprint",
            "rafters at the peak",
            "reed-cutter's grip",
            "mango stalk",
            "wheel-turning monarch",
            "the moon's radiance",
        ]),
        ("One precise answer", [
            "not a list —",
            "a single word:",
            "<span class=\"pali\">appamāda</span>",
        ]),
        ("The Buddha's last word", [
            "diligence named at",
            "the deathbed teaching,",
            "elsewhere in the canon",
        ]),
        ("Cross-references", [
            "AN 6.52 &middot; previous, six kinds of people",
        ]),
    ],
    further=[
        '<a href="%s/an6.53/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.54.html">AN 6.54 &middot; About Dhammika</a> &mdash; next, closing this '
        "chapter and the First Fifty with an extended parable.",
        '<a href="an-6.52.html">AN 6.52 &middot; Aristocrats</a> &mdash; previous, a different '
        "register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.54 — Dhammikasutta
# --------------------------------------------------------------------------- #
page(
    54, "Dhammika", "About Dhammika",
    vagga=VAGGA_5,
    meta_title="AN 6.54 — About Dhammika | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dhammikasutta, "
        "closing the Sixes' First Fifty as a mendicant banished from seven monasteries for "
        "abuse learns, through the parable of a felled banyan tree, what an ascetic's duty "
        "actually is. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain"),
        ("Speakers", "The Buddha, addressing Venerable Dhammika, who has just arrived"),
        ("Form", "A frame narrative of repeated banishment, a bird simile, an extended parable "
                 "of a banyan tree, and its direct application"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "Parables of a tree failing its community after being wronged by "
                              "one person recur in related form across Buddhist narrative "
                              "literature broadly, including the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the longest and most "
                       "narratively complex discourse in this chapter, closing the First Fifty "
                       "on an extended parable rather than a formula"),
    ],
    why=(
        "Venerable Dhammika abuses every visiting mendicant at every one of the seven "
        "monasteries in his native land, and is banished from each in turn, finally banished "
        "from all seven at once. With nowhere left to go, he seeks out the Buddha &mdash; who "
        "responds not with reproach but with a bird simile and then a long parable about a "
        "magnificent banyan tree, felled by a storm after its resident deity, angered by one "
        "person's disrespect, wished it would stop bearing fruit for everyone. The parable's "
        "point turns out to be exactly Dhammika's own situation, examined from an unexpected "
        "angle."),
    guide=[
        ("The teaching in one sentence", [
            "An ascetic's actual duty is not to retaliate when abused, annoyed, or argued with "
            "&mdash; and Dhammika, banished from seven monasteries for doing the opposite, is "
            "shown through the parable of a banyan tree that a single guardian's overreaction "
            "to one bad actor can cost an entire community what it depended on."]),
        ("The bird released from a ship, first", [
            "Before the main parable, the Buddha offers a smaller image: sea-merchants release "
            "a land-spotting bird from a ship out of sight of land; it searches every "
            "direction, and returns to the ship only if it finds no land anywhere. Applied to "
            "Dhammika, banished everywhere else, coming to the Buddha is framed not as a "
            "special honor sought but as the last remaining option after every other has been "
            "exhausted &mdash; a notably unflattering opening to what becomes an extended "
            "teaching."]),
        ("The banyan tree: shared abundance, undone by one bad actor", [
            "King Koravya's royal banyan tree fed an entire community &mdash; king, troops, "
            "townspeople, ascetics, even animals, each from their own trunk, unguarded and "
            "undamaged by mutual restraint &mdash; until one person ate his fill, then broke "
            "off a branch out of simple carelessness on his way out. The tree's resident deity, "
            "outraged, wished the tree would bear no more fruit for anyone, and it stopped."]),
        ("Sakka's question, and the deity's true fault", [
            "When the felled, fruitless tree is uprooted by a storm Sakka arranges, the grieving "
            "deity is asked a pointed question: did you stand by a tree's duty? A tree's duty, "
            "Sakka explains, is to let anyone take root, bark, leaves, flowers, or fruit as "
            "needed, without displeasure &mdash; even from someone who takes more than their "
            "share. The deity's fault was not misjudging the one bad actor, but withdrawing "
            "shared abundance from everyone in response to one person's carelessness."]),
        ("The application, and the six teachers who follow", [
            "The Buddha states the parallel to Dhammika directly: were you standing by an "
            "ascetic's duty &mdash; not retaliating when abused &mdash; when the lay followers "
            "banished you? Dhammika admits he was not. The Buddha then names six ancient "
            "teachers, each with hundreds of disciples, and states that insulting any one of "
            "them with malicious intent brims with wickedness &mdash; but insulting a single "
            "individual &ldquo;accomplished in view,&rdquo; a fellow spiritual companion, brims "
            "with even more, because &ldquo;any injury done by those outside of the Buddhist "
            "community does not compare with what is done to one's own spiritual "
            "companions.&rdquo;"]),
    ],
    terms=[
        ("assaddhamma",
         "not directly named in this English rendering but the implicit charge against "
         "Dhammika's own conduct: behavior contrary to the true teaching, specifically "
         "retaliation."),
        ("samaṇadhamma",
         "&ldquo;an ascetic's duty&rdquo; &mdash; the specific standard Dhammika is asked "
         "whether he upheld, defined as not retaliating when abused, annoyed, or argued with."),
        ("rukkhadhamma",
         "&ldquo;a tree's duty&rdquo; &mdash; Sakka's parallel standard for the tree-deity: "
         "letting all take what they need from roots, bark, leaves, flowers, or fruit without "
         "displeasure."),
        ("suppatiṭṭhita",
         "&ldquo;well planted&rdquo; &mdash; the name of King Koravya's royal banyan tree, "
         "before it lost its fruit and was later restored."),
        ("diṭṭhisampanna",
         "&ldquo;accomplished in view&rdquo; &mdash; the discourse's term for the single "
         "individual whose insult brims with even more wickedness than insulting six famous "
         "non-Buddhist teachers together."),
    ],
    text_intro=(
        "The discourse in full: Dhammika's repeated banishment, the bird simile, the banyan "
        "tree parable, and its direct application. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Banished from seven monasteries"),
        ("p", "&sect;1", "an6.54:1.1-6.13"),
        ("h3", "The bird released from a ship"),
        ("p", "&sect;2", "an6.54:7.1-8.6"),
        ("h3", "The banyan tree, and Sakka's storm"),
        ("p", "&sect;3", "an6.54:9.1-13.7"),
        ("h3", "The application, and six ancient teachers"),
        ("p", "&sect;4", "an6.54:13.8-19.10"),
        ("h3", "The closing verses"),
        ("p", "&sect;5", "an6.54:20.1-29.4"),
    ],
    quiz=[
        {"q": "Why is Venerable Dhammika banished from all seven monasteries in his native "
              "land?",
         "opts": [
             "For breaking a monastic precept related to food",
             "For abusing, insulting, and harassing visiting mendicants, causing them to leave "
             "each monastery",
             "For refusing to teach the Dhamma",
             "For traveling without permission"],
         "correct": 1,
         "expl": "A pattern repeated at each of seven monasteries in turn, before total "
                 "banishment."},
        {"q": "What does the bird-released-from-a-ship simile suggest about Dhammika's arrival "
              "at the Buddha?",
         "opts": [
             "That he sought out the Buddha as a special honor from the start",
             "That coming to the Buddha was the last remaining option after every other place "
             "had been exhausted, like a bird returning to the ship only when it finds no land "
             "anywhere",
             "That the Buddha specifically summoned him",
             "That the bird symbolizes Dhammika's psychic powers"],
         "correct": 1,
         "expl": "A notably unflattering opening to the teaching that follows."},
        {"q": "What happened to King Koravya's banyan tree, and why?",
         "opts": [
             "It was cut down by woodcutters for timber",
             "Its resident deity, angered that one person ate his fill and carelessly broke off "
             "a branch, wished the tree would bear no more fruit for anyone",
             "It died of natural causes over many years",
             "It was struck by lightning with no prior cause"],
         "correct": 1,
         "expl": "One person's carelessness led the deity to withdraw abundance from the entire "
                 "community."},
        {"q": "According to Sakka, what was the tree-deity's actual fault?",
         "opts": [
             "Failing to identify the bad actor and punish them directly",
             "Not standing by a tree's duty — withdrawing shared abundance from everyone in "
             "response to one person's carelessness, rather than tolerating what was taken "
             "without displeasure",
             "Being too generous with the tree's fruit",
             "Allowing animals to eat the fruit at all"],
         "correct": 1,
         "expl": "A tree's duty is to let all take what they need without becoming displeased, "
                 "even from someone taking more than their share."},
        {"q": "How does the Buddha apply this parable directly to Dhammika?",
         "opts": [
             "He declares the parable unrelated to Dhammika's situation",
             "He asks whether Dhammika was standing by an ascetic's duty — not retaliating when "
             "abused — when the lay followers banished him; Dhammika admits he was not",
             "He praises Dhammika's conduct as entirely justified",
             "He tells Dhammika to return and confront the lay followers"],
         "correct": 1,
         "expl": "A direct parallel: the tree-deity's overreaction mirrors Dhammika's own "
                 "retaliation against visiting mendicants."},
        {"q": "What claim does the Buddha make about insulting the six ancient teachers versus "
              "insulting a single individual 'accomplished in view'?",
         "opts": [
             "Insulting the six teachers is always worse",
             "Insulting a single individual accomplished in view — a fellow spiritual "
             "companion — brims with even more wickedness, because injury from outside the "
             "community doesn't compare to injury done within it",
             "Both are equally wrong, with no distinction",
             "Neither is considered wrong at all"],
         "correct": 1,
         "expl": "A pointed claim about harm done within one's own spiritual community."},
        {"q": "What is <em>samaṇadhamma</em>, an ascetic's duty, defined as in this discourse?",
         "opts": [
             "Begging for alms daily",
             "Not retaliating — not abusing, annoying, or arguing back — when abused, annoyed, "
             "or argued with by someone else",
             "Living in complete silence",
             "Teaching the Dhamma to as many people as possible"],
         "correct": 1,
         "expl": "The specific standard Dhammika is asked whether he upheld."},
        {"q": "Where is AN 6.54 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, on Vulture's Peak Mountain",
             "The land of the Cetis, at Sahajāti",
             "Near Kimbilā"],
         "correct": 1,
         "expl": "The location Dhammika finally reaches after being banished from all seven "
                 "monasteries."},
        {"q": "What happens to the banyan tree after Sakka's second storm?",
         "opts": [
             "It remains destroyed permanently",
             "It is raised back up and the bark of its roots is healed, once the deity commits "
             "to standing by a tree's duty",
             "A new tree grows in its place",
             "The tree is moved to a different location"],
         "correct": 1,
         "expl": "Restoration follows the deity's genuine commitment to the standard Sakka "
                 "named."},
        {"q": "What makes AN 6.54 distinctive within this chapter, according to the guide?",
         "opts": [
             "It is the shortest discourse in the chapter",
             "It is the longest and most narratively complex discourse in the chapter, closing "
             "the First Fifty on an extended parable rather than a formula",
             "It is the only discourse spoken by a deity",
             "It contains no verse content at all"],
         "correct": 1,
         "expl": "A capstone narrative closing out the Sixes' first major structural division."},
    ],
    marginalia=[
        ("A repeated pattern", [
            "banished from one",
            "monastery after another —",
            "seven, then all at once",
        ]),
        ("The banyan tree", [
            "shared by all, until",
            "one careless act —",
            "the deity withholds it all",
        ]),
        ("A tree's actual duty", [
            "let all take what they need",
            "without displeasure —",
            "not withdraw everything",
        ]),
        ("Closing the First Fifty", [
            "AN 6.1&ndash;54 complete —",
            "the Second Fifty begins",
            "at AN 6.55, Mahāvagga",
        ]),
    ],
    further=[
        '<a href="%s/an6.54/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.53.html">AN 6.53 &middot; Diligence</a> &mdash; previous, closing this '
        "chapter's run of brahmin dialogues.",
        '<a href="an-6.43.html">AN 6.43 &middot; The Giant</a> &mdash; this '
        "chapter&rsquo;s opening, for contrast with where it closes.",
    ],
)


# --------------------------------------------------------------------------- #
# Chapter 6 — Mahāvagga (AN 6.55–64), opening the Second Fifty
# --------------------------------------------------------------------------- #
VAGGA_6 = "<em>Mahāvagga</em> &mdash; the sixth chapter of the Sixes, opening the Second Fifty"


# --------------------------------------------------------------------------- #
# AN 6.55 — Soṇasutta
# --------------------------------------------------------------------------- #
page(
    55, "Soṇa", "With Soṇa",
    vagga=VAGGA_6,
    meta_title="AN 6.55 — With Soṇa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Soṇasutta, opening "
        "the Second Fifty as the Buddha uses a harp's strings to teach a discouraged mendicant "
        "the balance of energy, ending in Soṇa's own declaration of six qualities. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain, and the Cool Grove"),
        ("Speakers", "The Buddha, addressing Venerable Soṇa; then Soṇa himself, declaring his "
                     "own attainment"),
        ("Form", "A private discouragement read by the Buddha, a harp simile, and Soṇa's own "
                 "closing declaration of six dedications"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The harp-string simile for balancing energy recurs widely across "
                              "Buddhist meditation literature, including the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; an accessible narrative "
                       "opening the Second Fifty, closing on six precisely defined dedications"),
    ],
    why=(
        "Soṇa, privately discouraged despite being &ldquo;one of the Buddha's most energetic "
        "disciples,&rdquo; is on the verge of giving up the training entirely when the Buddha "
        "appears before him and, rather than arguing against the thought directly, asks about "
        "something Soṇa already understands from lay life: a harp's strings, unplayable both "
        "too tight and too slack. The discourse that opens the Sixes' Second Fifty is a story "
        "of exactly the kind of adjustment, not abandonment, that discouragement calls for."),
    guide=[
        ("The teaching in one sentence", [
            "Energy that is too forceful leads to restlessness, and energy that is too slack "
            "leads to laziness, so a discouraged practitioner should seek balance between them "
            "rather than concluding the path itself has failed."]),
        ("A thought read directly, not confessed", [
            "The Buddha does not wait for Soṇa to admit his discouragement; he simply appears "
            "before him, having &ldquo;known Venerable Soṇa's train of thought,&rdquo; and "
            "states it back to him almost word for word. This framing matters: Soṇa is not "
            "praised for confessing a struggle, nor is his private doubt treated as itself a "
            "failing to be corrected before anything else can be taught."]),
        ("A simile drawn from Soṇa's own former life", [
            "Rather than offering an abstract teaching on effort, the Buddha reaches for "
            "something specific to Soṇa's own background as a skilled harp player before "
            "ordaining. The simile works because it does not need to be explained from "
            "scratch &mdash; Soṇa already knows, from direct experience, exactly what an "
            "over-tightened or over-slackened string sounds like."]),
        ("Six dedications, declared only after attainment", [
            "The discourse's second half belongs to Soṇa, now perfected, describing the "
            "arahant as dedicated to six things: renunciation, seclusion, kindness, the ending "
            "of craving, the ending of grasping, and mental clarity. Crucially, Soṇa "
            "pre-empts a misreading of each: dedication to renunciation is not mere faith, "
            "dedication to seclusion is not a taste for solitude's comforts, dedication to "
            "kindness (following precepts) is not rule-following for its own sake &mdash; each "
            "is instead traced back to the actual absence of greed, hate, and delusion."]),
        ("The mountain simile closing the discourse", [
            "Soṇa's own closing verses picture a solid mass of rock, unmoved by storms from any "
            "direction, as the freed mind remains unmoved by whatever compelling sights, "
            "sounds, or ideas arise. The image directly answers the discourse's opening "
            "problem: where Soṇa's energy was once unbalanced enough to nearly end his "
            "practice, the freed mind he eventually reaches is pictured as beyond that kind of "
            "disturbance altogether."]),
    ],
    terms=[
        ("vīriyasamatā",
         "&ldquo;balance of energy&rdquo; &mdash; what the Buddha instructs Soṇa to seek, "
         "between forceful restlessness and slack laziness."),
        ("indriyānaṁ samataṁ",
         "&ldquo;a balance of the faculties&rdquo; &mdash; the fuller instruction given "
         "alongside energy and serenity."),
        ("nekkhamma, paviveka, abyāpajjha, taṇhākkhaya, upādānakkhaya, "
         "cetaso apariyādānatā",
         "&ldquo;renunciation, seclusion, kindness, the ending of craving, the ending of "
         "grasping, mental clarity&rdquo; &mdash; Soṇa's own six dedications, each traced to "
         "the ending of greed, hate, and delusion rather than to any external motive."),
        ("khīṇāsava",
         "&ldquo;one whose defilements are ended&rdquo; &mdash; the state Soṇa describes and "
         "has himself reached by the discourse's second half."),
        ("selo yathā ekaghano",
         "&ldquo;like a mountain, one solid mass of rock&rdquo; &mdash; the closing simile for "
         "the freed mind's imperturbability."),
    ],
    text_intro=(
        "The discourse in full: Soṇa's discouragement, the harp simile, and his own closing "
        "declaration of six dedications. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Soṇa's discouragement"),
        ("p", "&sect;1", "an6.55:1.1-1.7"),
        ("h3", "The harp simile"),
        ("p", "&sect;2", "an6.55:3.1-7.4"),
        ("h3", "Soṇa's attainment, and his six dedications"),
        ("p", "&sect;3", "an6.55:8.1-16.1"),
        ("h3", "The mountain simile, in prose and verse"),
        ("p", "&sect;4", "an6.55:17.1-22.4"),
    ],
    quiz=[
        {"q": "What thought discourages Soṇa at the discourse's opening?",
         "opts": [
             "That he has never been taught properly",
             "That despite being one of the Buddha's most energetic disciples, his mind is not "
             "yet freed, and he might as well resign and enjoy his family's wealth instead",
             "That the Buddha does not approve of him",
             "That he wishes to become a teacher of others"],
         "correct": 1,
         "expl": "A private, unspoken discouragement the Buddha reads directly rather than "
                 "waiting for a confession."},
        {"q": "What simile does the Buddha use to address Soṇa's discouragement?",
         "opts": [
             "A river flowing to the sea",
             "A harp's strings, unplayable when tuned too tight or too slack",
             "A tree bearing fruit",
             "A boat crossing a flood"],
         "correct": 1,
         "expl": "Drawn specifically from Soṇa's own background as a skilled harp player "
                 "before ordaining."},
        {"q": "What balance does the Buddha instruct Soṇa to seek?",
         "opts": [
             "Between faith and doubt",
             "Between energy and serenity, avoiding both forceful restlessness and slack "
             "laziness",
             "Between solitude and company",
             "Between speech and silence"],
         "correct": 1,
         "expl": "Too-forceful energy leads to restlessness; too-slack energy leads to "
                 "laziness."},
        {"q": "What six things does Soṇa describe an arahant as dedicated to, once he has "
              "himself attained?",
         "opts": [
             "The five faculties plus liberation",
             "Renunciation, seclusion, kindness, the ending of craving, the ending of grasping, "
             "and mental clarity",
             "Faith, energy, mindfulness, immersion, and wisdom",
             "Seeing, listening, acquisition, training, service, recollection"],
         "correct": 1,
         "expl": "Six dedications, each traced to the actual ending of greed, hate, and "
                 "delusion."},
        {"q": "What misreading does Soṇa pre-empt for each of the six dedications?",
         "opts": [
             "That they are impossible to achieve",
             "That each is motivated by something external — mere faith, enjoying comfort, or "
             "rule-following — rather than the genuine absence of greed, hate, and delusion",
             "That they contradict each other",
             "That only mendicants, not laypeople, can understand them"],
         "correct": 1,
         "expl": "Soṇa insists each dedication reflects an actual inner state, not an outward "
                 "performance."},
        {"q": "What image closes the discourse?",
         "opts": [
             "A lotus growing in water",
             "A mountain, one solid mass of rock, unmoved by storms from any direction",
             "A fire going out for lack of fuel",
             "A bird returning to a ship"],
         "correct": 1,
         "expl": "Directly answering the opening problem of imbalanced, unsettled energy."},
        {"q": "Where does this discourse's central dialogue take place?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "The Cool Grove near Rājagaha, where the Buddha appears before Soṇa by psychic "
             "power",
             "Ñātika, in the brick house",
             "Varanasi, at Isipatana"],
         "correct": 1,
         "expl": "The Buddha travels there specifically upon reading Soṇa's discouraged "
                 "thought."},
        {"q": "How does the Buddha come to know Soṇa's discouraged thought?",
         "opts": [
             "Soṇa writes him a letter",
             "The Buddha simply 'knew Venerable Soṇa's train of thought' and appeared before "
             "him directly",
             "A deity reports it to the Buddha",
             "Soṇa confesses it to another mendicant first"],
         "correct": 1,
         "expl": "No confession is required before the teaching begins."},
        {"q": "What does Soṇa do after attaining perfection?",
         "opts": [
             "He keeps it private and tells no one",
             "He goes to the Buddha specifically to declare his enlightenment in the Buddha's "
             "presence",
             "He leaves the monastic order",
             "He immediately begins teaching other mendicants"],
         "correct": 1,
         "expl": "A deliberate act of declaration, not an accidental discovery by others."},
        {"q": "What does <em>vīriyasamatā</em> mean?",
         "opts": ["Excess of energy", "Balance of energy", "Absence of energy", "A type of "
                  "meditative absorption"],
         "correct": 1,
         "expl": "The specific quality the Buddha's harp simile is meant to illustrate."},
    ],
    marginalia=[
        ("The harp simile", [
            "too tight: restlessness",
            "too slack: laziness",
            "balanced: resonant",
        ]),
        ("Six dedications", [
            "renunciation &middot; seclusion",
            "kindness &middot; end of craving",
            "end of grasping &middot; clarity",
        ]),
        ("Each traced inward", [
            "not faith, not comfort,",
            "not rule-following —",
            "the actual end of greed",
        ]),
        ("Cross-references", [
            "AN 6.54 &middot; the First Fifty's close",
        ]),
    ],
    further=[
        '<a href="%s/an6.55/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.56.html">AN 6.56 &middot; With Phagguna</a> &mdash; next, a visit to a '
        "dying mendicant.",
        '<a href="an-6.54.html">AN 6.54 &middot; About Dhammika</a> &mdash; previous, closing '
        "the First Fifty.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.56 — Phagguṇasutta
# --------------------------------------------------------------------------- #
page(
    56, "Phagguṇa", "With Phagguna",
    vagga=VAGGA_6,
    meta_title="AN 6.56 — With Phagguna | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Phagguṇasutta, in "
        "which the Buddha visits a dying mendicant, describes his pain in graphic detail, and "
        "his death prompts a teaching on six benefits of hearing the teaching at the right "
        "time. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", "Venerable Ānanda, the Buddha, and the dying Venerable Phagguna"),
        ("Form", "A sickbed visit with graphically described pain, a death, and the Buddha's "
                 "explanation built from six parallel cases"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Sickbed teachings that free a dying mendicant's mind recur "
                              "across the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; emotionally direct, worth "
                       "reading without flinching from its graphic description of pain"),
    ],
    why=(
        "At Ānanda's request, the Buddha visits the gravely ill Phagguna, whose description of "
        "his own suffering is unusually visceral for this collection &mdash; winds like a "
        "drill in his skull, a strap tightening around his head, a butcher's cleaver in his "
        "belly, burning coals against his skin. The Buddha teaches him anyway, and not long "
        "after leaving, learns that Phagguna has died &mdash; with, unexpectedly, "
        "&ldquo;bright and clear&rdquo; faculties, because the teaching heard that afternoon "
        "freed his mind from the five lower fetters before death arrived."),
    guide=[
        ("The teaching in one sentence", [
            "There are six benefits to hearing the teaching and examining its meaning at "
            "exactly the right time, illustrated by Phagguna's own case: a mendicant whose mind "
            "is not yet freed can still be freed from the five lower fetters, or a mendicant "
            "already free of those fetters can be freed with the supreme ending of "
            "attachments, depending on whether they hear the Realized One, a disciple, or "
            "simply recollect the teaching for themselves at the moment of death."]),
        ("Pain described without euphemism", [
            "Phagguna's four similes for his own suffering &mdash; a drill in the skull, a "
            "tightening strap, a butcher's cleaver, burning coals &mdash; are graphic by this "
            "collection's usual standard. The discourse does not soften or summarize this "
            "description; it is given in full, twice (once in Phagguna's own words, framed by "
            "the discourse's structure as worth recording precisely as spoken)."]),
        ("A visit that does not promise a cure", [
            "The Buddha's greeting &mdash; hoping the pain is fading, not growing &mdash; is "
            "met with Phagguna's flat denial: it is growing, not fading. Nothing in the "
            "discourse suggests the Buddha's teaching relieves the physical pain itself; what "
            "it does, learned only afterward, is free Phagguna's mind from fetters before his "
            "death, a different kind of outcome from physical healing."]),
        ("Six benefits, crossing two dimensions", [
            "The Buddha's closing analysis crosses two variables: whether the mendicant's mind "
            "is freed from the five lower fetters but not yet fully liberated, or not yet freed "
            "from those fetters at all; and whether, at the time of death, they encounter the "
            "Realized One directly, a disciple, or only their own memorized understanding of "
            "the teaching. Three encounters times two starting conditions produces the six "
            "named benefits, Phagguna's own case falling into the first."]),
        ("An answer given only after the death it explains", [
            "Structurally, the discourse withholds its explanatory framework until after "
            "Phagguna has already died: Ānanda reports the bright, clear faculties as a "
            "puzzling detail, and only then does the Buddha supply the six-case analysis that "
            "makes sense of it. The teaching arrives as retrospective explanation, not advance "
            "instruction Phagguna himself could have used to anticipate his own outcome."]),
    ],
    terms=[
        ("orambhāgiyāni saṁyojanāni",
         "&ldquo;the five lower fetters&rdquo; &mdash; what Phagguna's mind was freed from "
         "upon hearing the Buddha's teaching, shortly before his death."),
        ("kālena dhammassavana",
         "&ldquo;hearing the teaching at the right time&rdquo; &mdash; the discourse's own "
         "title concept, naming the timing that makes the six benefits possible."),
        ("anupādā parinibbāna",
         "not a single compound named directly in this translation but the sense of "
         "&ldquo;the supreme ending of attachments&rdquo; &mdash; the deeper freedom described "
         "for a mind already free of the five lower fetters."),
        ("vippasannāni indriyāni",
         "&ldquo;faculties bright and clear&rdquo; &mdash; the detail Ānanda reports about "
         "Phagguna's death, prompting the Buddha's explanation."),
        ("Sallakattā",
         "not a term from this discourse directly, but the surgical, graphic register of "
         "Phagguna's own four similes for physical pain."),
    ],
    text_intro=(
        "The discourse in full: the Buddha's visit, Phagguna's graphic description of pain, "
        "his death, and the six benefits explained afterward. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Buddha visits the dying Phagguna"),
        ("p", "&sect;1", "an6.56:1.1-2.2"),
        ("h3", "Phagguna's pain, described in full"),
        ("p", "&sect;2", "an6.56:3.1-6.3"),
        ("h3", "Phagguna's death, and the Buddha's explanation"),
        ("p", "&sect;3", "an6.56:7.1-8.3"),
        ("h3", "Six benefits of hearing the teaching at the right time"),
        ("p", "&sect;4", "an6.56:9.1-15.1"),
    ],
    quiz=[
        {"q": "Why does the Buddha visit Phagguna?",
         "opts": [
             "To perform a healing ritual",
             "At Ānanda's request, out of sympathy for Phagguna, who is sick, suffering, and "
             "gravely ill",
             "To formally expel him from the Saṅgha",
             "To ask him a doctrinal question"],
         "correct": 1,
         "expl": "A sickbed visit prompted by Ānanda's direct appeal."},
        {"q": "How does Phagguna describe his pain?",
         "opts": [
             "In vague, minimal terms",
             "In four graphic similes: a drill in his skull, a tightening strap, a butcher's "
             "cleaver in his belly, burning coals against his skin",
             "He denies being in any pain at all",
             "Only in a single brief sentence"],
         "correct": 1,
         "expl": "Unusually visceral description, given in full without softening."},
        {"q": "Does the Buddha's teaching relieve Phagguna's physical pain?",
         "opts": [
             "Yes, the pain vanishes immediately",
             "Nothing in the discourse suggests physical relief — what it accomplishes, learned "
             "only afterward, is freeing his mind from fetters before death",
             "The discourse does not address whether the pain changed",
             "Phagguna's pain worsens as a result of the teaching"],
         "correct": 1,
         "expl": "A different kind of outcome from physical healing."},
        {"q": "What happens to Phagguna soon after the Buddha leaves?",
         "opts": [
             "He recovers fully",
             "He dies, with his faculties described as 'bright and clear' at the moment of "
             "death",
             "He asks to see the Buddha again",
             "He renounces the training"],
         "correct": 1,
         "expl": "A detail Ānanda reports back to the Buddha, prompting the explanatory "
                 "teaching."},
        {"q": "What two variables does the Buddha's six-benefit analysis cross?",
         "opts": [
             "Age and gender",
             "Whether the mind is freed from the five lower fetters or not yet, and whether the "
             "dying mendicant encounters the Realized One, a disciple, or only their own "
             "memorized understanding",
             "Wealth and social status",
             "Location and time of day"],
         "correct": 1,
         "expl": "Two starting conditions times three kinds of encounter produces six named "
                 "benefits."},
        {"q": "When does the Buddha supply his explanatory six-case analysis?",
         "opts": [
             "Before visiting Phagguna, as advance instruction",
             "Only after Phagguna has already died, as retrospective explanation for the "
             "puzzling detail of his bright, clear faculties",
             "The analysis is never given in this discourse",
             "Phagguna receives the explanation himself before dying"],
         "correct": 1,
         "expl": "The teaching arrives as an answer to what already happened, not a guide "
                 "Phagguna could have used in advance."},
        {"q": "What are 'the five lower fetters' (orambhāgiyāni saṁyojanāni) in this discourse?",
         "opts": [
             "A synonym for physical illness",
             "A standard set of bindings a mendicant's mind can be freed from upon hearing the "
             "teaching, as happened for Phagguna",
             "A term for lay precepts",
             "A description of Phagguna's specific symptoms"],
         "correct": 1,
         "expl": "What Phagguna's mind was freed from shortly before his death."},
        {"q": "Is a setting stated for AN 6.56?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Sahajāti"],
         "correct": 1,
         "expl": "A bare narrative beginning mid-scene, with no fresh location given."},
        {"q": "How does the Buddha respond when he first hears of Phagguna's death?",
         "opts": [
             "With surprise and confusion",
             "With a direct explanation: 'why shouldn't his faculties be bright and clear? His "
             "mind was freed from the five lower fetters when he heard that teaching'",
             "By denying the report",
             "By blaming Ānanda for the death"],
         "correct": 1,
         "expl": "An immediate, confident explanation rather than surprise."},
        {"q": "What did Phagguna do when he first saw the Buddha approaching?",
         "opts": [
             "He got up to greet him formally",
             "He stirred in his cot, and the Buddha told him not to get up, saying he would sit "
             "on another seat instead",
             "He turned away and refused to see the Buddha",
             "He was unconscious and did not notice"],
         "correct": 1,
         "expl": "A small, humane detail preceding the discourse's larger teaching."},
    ],
    marginalia=[
        ("Pain, described fully", [
            "a drill in the skull",
            "a tightening strap",
            "a cleaver &middot; burning coals",
        ]),
        ("Six benefits", [
            "freed from lower fetters,",
            "or freed with the",
            "supreme ending — × 3 encounters",
        ]),
        ("Explained only after", [
            "not advance instruction —",
            "an answer to what",
            "had already happened",
        ]),
        ("Cross-references", [
            "AN 6.55 &middot; previous, balance of energy",
        ]),
    ],
    further=[
        '<a href="%s/an6.56/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.57.html">AN 6.57 &middot; The Six Classes of Rebirth</a> &mdash; next, '
        "the Buddha's response to a rival teacher's classification.",
        '<a href="an-6.55.html">AN 6.55 &middot; With Soṇa</a> &mdash; previous, a different '
        "register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.57 — Chaḷabhijātisutta
# --------------------------------------------------------------------------- #
page(
    57, "Chaḷabhijāti", "The Six Classes of Rebirth",
    vagga=VAGGA_6,
    meta_title="AN 6.57 — The Six Classes of Rebirth | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Chaḷabhijātisutta, in "
        "which the Buddha rejects a rival teacher's caste-based classification of livelihoods "
        "and proposes his own six classes based entirely on conduct and its result. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, on Vulture's Peak Mountain"),
        ("Speakers", "Venerable Ānanda, reporting another teacher's doctrine; then the Buddha, "
                     "rejecting it and proposing his own"),
        ("Form", "A report of a rival classification, a sharp simile of illegitimate "
                 "authority, and the Buddha's own six-fold system based on conduct"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Rejections of caste- or livelihood-based hierarchies of worth "
                              "recur across the Chinese Āgamas as a recognizable feature of "
                              "early Buddhist ethical teaching; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;#9734;&#9734; &mdash; historically dense, naming a "
                       "real rival teacher and real other ascetic movements by name"),
    ],
    why=(
        "Ānanda reports a system taught by Pūraṇa Kassapa, a historically attested rival "
        "teacher of the Buddha's own time: six classes of rebirth, colored black through white, "
        "sorting people by livelihood and sectarian affiliation, with certain named ascetic "
        "leaders placed at the very top as &ldquo;ultimate white.&rdquo; The Buddha's response "
        "is sharp &mdash; he compares Pūraṇa's system to forcing an unwanted purchase on a poor "
        "person &mdash; and he proposes an entirely different six-fold system of his own, based "
        "not on birth or sect but purely on conduct and its consequence."),
    guide=[
        ("The teaching in one sentence", [
            "Rather than Pūraṇa Kassapa's six classes sorted by livelihood and sectarian "
            "identity, the Buddha describes six classes defined by the crossing of two "
            "variables &mdash; being born into a &lsquo;dark&rsquo; (low, difficult) or "
            "&lsquo;bright&rsquo; (privileged, comfortable) family &mdash; with three possible "
            "results: a dark result (bad conduct, bad rebirth), a bright result (good conduct, "
            "good rebirth), or extinguishment, available from either starting condition through "
            "renunciation and the development of mindfulness and the awakening factors."]),
        ("Naming a real historical rival directly", [
            "Pūraṇa Kassapa is not a fictional interlocutor invented for this discourse; he is "
            "one of the six well-known non-Buddhist teachers named repeatedly across the early "
            "canon, associated elsewhere with a doctrine of moral inaction. This discourse "
            "treats his classification system as worth engaging directly and by name, rather "
            "than dismissing it in the abstract."]),
        ("A pointed simile about consent and authority", [
            "The Buddha's objection to Pūraṇa's system is not first about its content but "
            "about its authority: &ldquo;did the whole world authorize Pūraṇa Kassapa to "
            "describe these six classes?&rdquo; His simile &mdash; forcing a purchase of meat "
            "on someone too poor to refuse &mdash; frames Pūraṇa's classification as an "
            "imposition made without the consent of the very ascetics and brahmins it ranks, "
            "a criticism of illegitimate authority as much as of the content itself."]),
        ("What the Buddha's own system actually replaces", [
            "Pūraṇa's system sorted people by occupation and sectarian membership: butchers and "
            "hunters at the bottom, certain named ascetic leaders at the very top, with entire "
            "categories of people permanently assigned by birth or affiliation. The Buddha's "
            "own six classes instead cross birth circumstance with subsequent conduct, and "
            "crucially include extinguishment as available from either a difficult or "
            "privileged starting family &mdash; nothing about a person's birth family fixes "
            "their ultimate outcome."]),
        ("Reading this discourse honestly, without smoothing", [
            "This discourse names, without elaboration or apology, occupations it groups "
            "together in a &ldquo;dark class&rdquo; &mdash; slaughterers, hunters, bandits, "
            "executioners, jailers &mdash; language that reads as harsh by any standard, "
            "ancient or modern. What distinguishes the Buddha's system from Pūraṇa's, on its "
            "own terms, is that this initial family circumstance is explicitly not the final "
            "word: the discourse states directly that someone born into this same "
            "circumstance can still give rise to a bright result or to extinguishment through "
            "their own subsequent conduct, a possibility Pūraṇa's caste-based system, as "
            "reported here, does not offer."]),
    ],
    terms=[
        ("chaḷabhijāti",
         "&ldquo;six classes of rebirth&rdquo; &mdash; the discourse's title, shared between "
         "Pūraṇa Kassapa's rejected system and the Buddha's own replacement."),
        ("kaṇhābhijāti, sukkābhijāti",
         "&ldquo;dark class, bright class&rdquo; &mdash; the Buddha's own two starting "
         "conditions, based on family circumstance at birth, not occupation or sect."),
        ("kaṇhaṁ vipākaṁ, sukkaṁ vipākaṁ, nibbānaṁ",
         "&ldquo;dark result, bright result, extinguishment&rdquo; &mdash; the three possible "
         "outcomes crossed with each starting class to produce the Buddha's six-fold system."),
        ("pūraṇo kassapo",
         "one of the six well-known non-Buddhist teachers of the Buddha's own era, named here "
         "directly as the source of the rejected classification."),
        ("bojjhaṅga",
         "&ldquo;awakening factor&rdquo; &mdash; among the qualities developed by someone from "
         "either starting class who goes forth and gives rise to extinguishment."),
    ],
    text_intro=(
        "The discourse in full: Ānanda's report of Pūraṇa Kassapa's system, the Buddha's "
        "rejection of it, and his own six classes. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda reports Pūraṇa Kassapa's six classes"),
        ("p", "&sect;1", "an6.57:1.1-8.1"),
        ("h3", "The Buddha's rejection, and his own classes named"),
        ("p", "&sect;2", "an6.57:9.1-10.11"),
        ("h3", "Each class explained: dark and bright, three results each"),
        ("p", "&sect;3", "an6.57:11.1-17.1"),
    ],
    quiz=[
        {"q": "Who is Pūraṇa Kassapa, and what does Ānanda report about him?",
         "opts": [
             "A fictional figure invented for this discourse",
             "A historically attested rival teacher of the Buddha's era, one of six well-known "
             "non-Buddhist teachers, who describes six classes of rebirth sorted by livelihood "
             "and sect",
             "A senior disciple of the Buddha",
             "A deity who visits the Buddha"],
         "correct": 1,
         "expl": "A real rival teacher engaged directly and by name, not a hypothetical "
                 "opponent."},
        {"q": "What is the Buddha's first objection to Pūraṇa's system?",
         "opts": [
             "That the content is factually wrong",
             "A question about authority: did the whole world authorize Pūraṇa to describe "
             "these classes? — illustrated by a simile of forcing a purchase on someone too "
             "poor to refuse",
             "That Pūraṇa is not a real teacher",
             "That six classes is the wrong number"],
         "correct": 1,
         "expl": "A criticism of illegitimate authority and lack of consent, before addressing "
                 "content."},
        {"q": "What two variables does the Buddha's own six-fold system cross?",
         "opts": [
             "Wealth and intelligence",
             "Being born into a 'dark' (difficult) or 'bright' (privileged) family, with three "
             "possible results: dark result, bright result, or extinguishment",
             "Age and gender",
             "Occupation and sect membership, matching Pūraṇa's system exactly"],
         "correct": 1,
         "expl": "Two starting conditions × three outcomes = six classes, replacing Pūraṇa's "
                 "occupation-based sorting."},
        {"q": "What is the crucial difference the guide identifies between the Buddha's system "
              "and Pūraṇa's, on its own terms?",
         "opts": [
             "There is no meaningful difference between the two systems",
             "The Buddha's system explicitly allows someone born into a difficult family "
             "circumstance to still reach a bright result or extinguishment through their own "
             "conduct — a possibility Pūraṇa's reported system does not offer",
             "The Buddha's system uses entirely different vocabulary with the same underlying "
             "logic",
             "Pūraṇa's system is actually more flexible than the Buddha's"],
         "correct": 1,
         "expl": "Birth circumstance is a starting point, not a fixed final verdict, in the "
                 "Buddha's version."},
        {"q": "How does the guide characterize the language used to describe the 'dark class' "
              "occupations?",
         "opts": [
             "It softens or omits the harsh language entirely",
             "It presents the discourse's language honestly, without smoothing it over, while "
             "noting what distinguishes the Buddha's system from Pūraṇa's on the question of "
             "whether birth fixes final outcome",
             "It argues the translation is inaccurate",
             "It claims this passage should be disregarded entirely"],
         "correct": 1,
         "expl": "Consistent with this guide's established practice of reading difficult "
                 "passages plainly at AN 6.18 and elsewhere."},
        {"q": "What does <em>bojjhaṅga</em> mean?",
         "opts": [
             "Awakening factor — one of the qualities developed on the path to extinguishment "
             "from either starting class", "A caste designation", "A type of livelihood", "A "
             "term for family wealth"],
         "correct": 0,
         "expl": "Part of what someone from either the dark or bright class develops if they "
                 "go forth and reach extinguishment."},
        {"q": "Where is AN 6.57 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Rājagaha, on Vulture's Peak Mountain",
             "Ñātika, in the brick house",
             "Varanasi, at Isipatana"],
         "correct": 1,
         "expl": "A fresh, specific setting for this dialogue between Ānanda and the Buddha."},
        {"q": "What occupations does Pūraṇa's system, as reported, place in the 'black' class?",
         "opts": [
             "Merchants and farmers",
             "Slaughterers, hunters, fishers, bandits, executioners, butchers, and jailers",
             "Kings and their ministers",
             "Ascetics and brahmins generally"],
         "correct": 1,
         "expl": "The rejected system's lowest-ranked occupational category."},
        {"q": "Who does Pūraṇa's system place at 'ultimate white,' the very top?",
         "opts": [
             "The Buddha himself",
             "Named ascetic leaders including Nanda Vaccha, Kisa Saṅkicca, and Gosāla",
             "Kings and aristocrats",
             "Wealthy brahmin priests"],
         "correct": 1,
         "expl": "Specific historical figures named directly in the reported classification."},
        {"q": "What allows extinguishment in the Buddha's own six-class system?",
         "opts": [
             "Being born into the bright class only",
             "Going forth, giving up the five hindrances, establishing mindfulness, and "
             "developing the awakening factors — available from either the dark or bright "
             "starting class",
             "Being born into the dark class only",
             "Wealth accumulated over a lifetime"],
         "correct": 1,
         "expl": "A path open regardless of birth circumstance, unlike Pūraṇa's fixed "
                 "hierarchy."},
    ],
    marginalia=[
        ("Pūraṇa's system", [
            "black &middot; blue &middot; red",
            "yellow &middot; white",
            "&middot; ultimate white",
        ]),
        ("The Buddha's system", [
            "dark or bright family ×",
            "dark result, bright result,",
            "or extinguishment",
        ]),
        ("The real difference", [
            "birth is a starting point,",
            "not a fixed verdict —",
            "conduct still decides",
        ]),
        ("Cross-references", [
            "AN 6.18 &middot; another honestly-read hard text",
        ]),
    ],
    further=[
        '<a href="%s/an6.57/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.58.html">AN 6.58 &middot; Defilements</a> &mdash; next, six methods for '
        "giving up defilements.",
        '<a href="an-6.56.html">AN 6.56 &middot; With Phagguna</a> &mdash; previous, a '
        "sickbed teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.58 — Āsavasutta
# --------------------------------------------------------------------------- #
page(
    58, "Āsava", "Defilements",
    vagga=VAGGA_6,
    meta_title="AN 6.58 — Defilements | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Āsavasutta, which "
        "names six distinct methods for giving up defilements — restraint, using, enduring, "
        "avoiding, getting rid, and developing — each matched to a different kind of "
        "obstruction. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "The worthiness formula attached to six distinct methods, each defined and "
                 "illustrated in turn"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "This sixfold method for giving up defilements corresponds "
                              "closely to MN 2's sevenfold version, and recurs in related form "
                              "across the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a practical taxonomy worth "
                       "reading for what distinguishes each method from the others"),
    ],
    why=(
        "AN 6.58 returns to the fourfold worthiness formula that opened this whole nipāta at "
        "AN 6.1, now attached to six distinct methods for giving up defilements &mdash; not "
        "one technique applied uniformly, but six different approaches, each matched "
        "specifically to the kind of obstruction it addresses. Restraint suits one situation, "
        "endurance another, avoidance a third; the discourse treats defilements as requiring "
        "different tools depending on their nature, not a single universal remedy."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant worthy of offerings has given up defilements by six distinct methods "
            "&mdash; restraint of the sense faculties, rational use of requisites, endurance of "
            "discomfort, avoidance of danger, actively getting rid of arisen bad thoughts, and "
            "developing the awakening factors &mdash; each method suited to a different kind of "
            "defilement."]),
        ("Restraint: preventing before contact", [
            "The first method, restraining the six sense faculties through rational "
            "reflection, addresses defilements before they arise at all &mdash; the "
            "&ldquo;distressing and feverish defilements that might arise&rdquo; in someone "
            "without restraint simply do not arise when restraint is present. This is "
            "prevention, not response."]),
        ("Using: reframing necessity through reflection", [
            "The second method does not describe abstaining from robes, food, lodging, or "
            "medicine, but using them with rational reflection on their actual purpose "
            "&mdash; robes only against cold, heat, and insects; food only to sustain the body "
            "and support practice, explicitly not for &ldquo;fun, indulgence, adornment, or "
            "decoration.&rdquo; The defilement addressed here is not the use of requisites but "
            "the unreflective attachment that can attach to their use."]),
        ("Enduring, avoiding, and getting rid: three different postures toward difficulty", [
            "Enduring concerns discomforts that must simply be borne &mdash; cold, heat, "
            "hunger, physical pain, harsh criticism. Avoiding concerns dangers better "
            "sidestepped entirely &mdash; wild animals, dangerous terrain, bad company. Getting "
            "rid concerns thoughts already arisen &mdash; sensual, malicious, or cruel thoughts "
            "&mdash; that must be actively eliminated rather than endured or avoided. The "
            "discourse keeps these three methods distinct rather than treating &ldquo;dealing "
            "with difficulty&rdquo; as one undifferentiated response."]),
        ("Developing: the constructive method closing the list", [
            "Where the first five methods are largely protective or corrective, the sixth "
            "&mdash; developing the seven awakening factors, from mindfulness through "
            "equanimity &mdash; is purely constructive, cultivating qualities that rely on "
            "&ldquo;seclusion, fading away, and cessation&rdquo; and ripen as letting go. The "
            "list closes not on defense but on active cultivation."]),
    ],
    terms=[
        ("āsava",
         "&ldquo;defilement,&rdquo; &ldquo;influx&rdquo; &mdash; what the discourse's six "
         "methods are each said to give up, in different ways."),
        ("saṁvarā pahātabbā",
         "&ldquo;defilements that should be given up by restraint&rdquo; &mdash; the first "
         "method, addressing the six sense faculties."),
        ("paṭisevanā pahātabbā",
         "&ldquo;defilements that should be given up by using&rdquo; &mdash; the second "
         "method, concerning rational reflection on the four requisites."),
        ("vinodanā pahātabbā",
         "&ldquo;defilements that should be given up by getting rid&rdquo; &mdash; the fifth "
         "method, concerning bad thoughts already arisen."),
        ("bhāvanā pahātabbā",
         "&ldquo;defilements that should be given up by developing&rdquo; &mdash; the sixth "
         "and final method, cultivating the seven awakening factors."),
    ],
    text_intro=(
        "The discourse in full: the six methods for giving up defilements, each defined and "
        "illustrated. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The worthiness formula, and the six methods named"),
        ("p", "&sect;1", "an6.58:1.1-2.7"),
        ("h3", "Restraint and using"),
        ("p", "&sect;2", "an6.58:3.1-4.11"),
        ("h3", "Enduring, avoiding, and getting rid"),
        ("p", "&sect;3", "an6.58:5.1-7.7"),
        ("h3", "Developing, and the conclusion"),
        ("p", "&sect;4", "an6.58:8.1-9.1"),
    ],
    quiz=[
        {"q": "What six methods for giving up defilements does this discourse name?",
         "opts": [
             "Restraint, using, enduring, avoiding, getting rid, and developing",
             "Faith, energy, mindfulness, immersion, wisdom, and liberation",
             "Danger, suffering, disease, boil, chain, bog",
             "Seeing, listening, acquisition, training, and service"],
         "correct": 0,
         "expl": "Six distinct approaches, each matched to a different kind of obstruction."},
        {"q": "What does the 'restraint' method address, and when?",
         "opts": [
             "Thoughts already arisen, requiring active elimination",
             "Defilements before they arise at all, through restraint of the six sense "
             "faculties — prevention, not response",
             "Physical discomfort that must be endured",
             "External dangers to be sidestepped"],
         "correct": 1,
         "expl": "The first method, addressing contact with sense objects before defilement can "
                 "arise."},
        {"q": "What does the 'using' method actually concern?",
         "opts": [
             "Abstaining entirely from robes, food, lodging, and medicine",
             "Using the four requisites with rational reflection on their actual purpose, "
             "addressing unreflective attachment rather than use itself",
             "Sharing requisites with other mendicants",
             "Refusing all gifts from lay donors"],
         "correct": 1,
         "expl": "Food, for instance, used only to sustain the body and support practice, not "
                 "for indulgence or decoration."},
        {"q": "How does the guide distinguish 'enduring,' 'avoiding,' and 'getting rid' from "
              "one another?",
         "opts": [
             "They are treated as identical, interchangeable responses",
             "Enduring concerns discomforts that must be borne; avoiding concerns dangers to be "
             "sidestepped; getting rid concerns thoughts already arisen requiring active "
             "elimination",
             "All three concern only physical dangers",
             "Only one of the three is actually distinct from the others"],
         "correct": 1,
         "expl": "Three different postures toward difficulty, kept deliberately separate."},
        {"q": "What makes the sixth method, 'developing,' different from the first five?",
         "opts": [
             "It is identical in structure to the other five",
             "It is purely constructive rather than protective or corrective, cultivating the "
             "seven awakening factors that ripen as letting go",
             "It applies only to lay followers",
             "It requires no effort at all"],
         "correct": 1,
         "expl": "The list closes on active cultivation, not defense or correction."},
        {"q": "What does <em>āsava</em> mean?",
         "opts": ["Liberation", "Defilement, influx", "Recollection", "Worthiness"],
         "correct": 1,
         "expl": "What all six methods in this discourse are each said to give up, differently."},
        {"q": "Is a setting stated for AN 6.58?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare formula returning to the worthiness formula first met at AN 6.1."},
        {"q": "What formula does this discourse reuse from the very start of this nipāta?",
         "opts": [
             "The six recollections",
             "The fourfold worthiness formula — worthy of offerings, hospitality, donation, and "
             "veneration",
             "The six sense doors",
             "The five hindrances"],
         "correct": 1,
         "expl": "First met at AN 6.1, now closing this six-method teaching on defilements."},
        {"q": "What kinds of thoughts does the 'getting rid' method specifically target?",
         "opts": [
             "Only thoughts about food",
             "Sensual, malicious, or cruel thoughts that have already arisen",
             "Thoughts about the weather",
             "Only thoughts about other mendicants"],
         "correct": 1,
         "expl": "The fifth method, requiring active elimination rather than mere endurance."},
        {"q": "What does the discourse say is used against 'dangers' in the avoiding method?",
         "opts": [
             "Physical force",
             "Rational reflection to sidestep wild animals, dangerous terrain, bad seats, bad "
             "neighborhoods, and bad friends entirely",
             "Formal debate",
             "Meditation on the danger itself"],
         "correct": 1,
         "expl": "The third method, addressing hazards better avoided than endured or resisted."},
    ],
    marginalia=[
        ("Six methods", [
            "restraint &middot; using",
            "enduring &middot; avoiding",
            "getting rid &middot; developing",
        ]),
        ("Different tools", [
            "for different problems —",
            "not one universal",
            "remedy applied uniformly",
        ]),
        ("Protective, then constructive", [
            "first five: defense",
            "and correction",
            "sixth: active cultivation",
        ]),
        ("Cross-references", [
            "AN 6.1 &middot; the worthiness formula's origin",
        ]),
    ],
    further=[
        '<a href="%s/an6.58/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.59.html">AN 6.59 &middot; With Dārukammika</a> &mdash; next, the Buddha '
        "corrects a householder's assumptions about giving.",
        '<a href="an-6.57.html">AN 6.57 &middot; The Six Classes of Rebirth</a> &mdash; '
        "previous, a different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.59 — Dārukammikasutta
# --------------------------------------------------------------------------- #
page(
    59, "Dārukammika", "With Dārukammika",
    vagga=VAGGA_6,
    meta_title="AN 6.59 — With Dārukammika | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dārukammikasutta, "
        "where the Buddha tells a householder that his comfortable lay life makes it hard to "
        "judge who is truly perfected, and names six pairs of mendicant circumstances instead. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Ñātika, in the brick house"),
        ("Speakers", "The householder Dārukammika, and the Buddha"),
        ("Form", "A householder's report of his giving practice, a direct correction, and six "
                 "paired circumstances each judged by conduct rather than category"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Warnings against judging mendicants by their category of "
                              "practice (forest-dwelling, robes worn, etc.) recur across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; a pointed correction of a "
                       "well-meaning but mistaken assumption"),
    ],
    why=(
        "Dārukammika describes his family's giving practice with evident pride: gifts reserved "
        "for mendicants who are perfected or on the path to it, living in the wilderness, "
        "eating only almsfood, wearing rag robes. The Buddha's response is a direct, gentle "
        "correction &mdash; as a layman enjoying sandalwood, garlands, and currency, it is "
        "genuinely hard for Dārukammika to know who is actually perfected, because none of "
        "the outward markers he trusts (wilderness dwelling, rag robes, almsfood alone) "
        "actually settle the question."),
    guide=[
        ("The teaching in one sentence", [
            "None of six outward mendicant categories &mdash; wilderness dwelling, "
            "village dwelling, eating only almsfood, accepting invitations, wearing rag robes, "
            "or wearing robes offered by householders &mdash; determines whether a mendicant is "
            "praiseworthy or reprehensible; what determines it, in every category, is whether "
            "that mendicant is restless and undisciplined or mindful and composed."]),
        ("A gentle but direct correction of a donor's confidence", [
            "The Buddha does not reject Dārukammika's generosity or his intention; he "
            "specifically challenges the criteria Dārukammika uses to select recipients, "
            "pointing out that a comfortable lay life &mdash; sandalwood, garlands, gold "
            "&mdash; makes it &ldquo;hard for you to know who is perfected or on the path to "
            "perfection&rdquo; simply because that lay life gives no direct access to another "
            "person's inner state."]),
        ("Six categories, one shared criterion applied to each", [
            "The Buddha runs through six mendicant circumstances in parallel &mdash; wilderness "
            "or village dwelling, eating only almsfood or accepting invitations, wearing rag "
            "robes or householder-donated robes &mdash; and for every single one, states the "
            "identical structure: if the mendicant is &ldquo;restless, insolent, fickle, "
            "scurrilous, loose-tongued,&rdquo; they are reprehensible regardless of category; "
            "if they have &ldquo;established mindfulness, situational awareness and "
            "immersion,&rdquo; they are praiseworthy regardless of category."]),
        ("Undermining, not reversing, a simple hierarchy", [
            "The discourse does not argue that village-dwelling or householder-robed "
            "mendicants are actually better than their wilderness or rag-robed counterparts "
            "&mdash; that would simply invert the mistake. It insists instead that the category "
            "itself carries no information at all about the individual's actual conduct, in "
            "either direction."]),
        ("A conversion built on correction, not doctrine", [
            "The discourse closes with the Buddha's direct encouragement &mdash; "
            "&ldquo;go ahead, householder, give gifts to the Saṅgha&rdquo; &mdash; and "
            "Dārukammika's resolution to do so from that day forward. Unlike several other "
            "conversions in this chapter and the last, this one follows not a doctrinal "
            "argument or a demonstrated meditative point but a practical correction of how to "
            "select whom to give to."]),
    ],
    terms=[
        ("āraññika, gāmantavihārī",
         "&ldquo;wilderness-dwelling, village-dwelling&rdquo; &mdash; the first pair of "
         "circumstances the Buddha addresses, neither inherently praiseworthy nor "
         "reprehensible."),
        ("piṇḍapātika, nemantanika",
         "&ldquo;eating only almsfood, accepting invitations&rdquo; &mdash; the second pair, "
         "again judged by conduct rather than category."),
        ("paṁsukūlika, gahapaticīvaradhara",
         "&ldquo;wearing rag robes, wearing robes offered by householders&rdquo; &mdash; the "
         "third and final pair."),
        ("uddhata unnaḷa capala mukhara vikiṇṇavāca",
         "&ldquo;restless, insolent, fickle, scurrilous, loose-tongued&rdquo; &mdash; the "
         "repeated description of what makes any mendicant, regardless of category, "
         "reprehensible."),
        ("upaṭṭhitasati sampajāna samāhita ekaggacitta saṁvutindriya",
         "&ldquo;established mindfulness, situational awareness, immersion, unified mind, "
         "restrained faculties&rdquo; &mdash; the repeated description of what makes any "
         "mendicant praiseworthy."),
    ],
    text_intro=(
        "The discourse in full: Dārukammika's report, the Buddha's correction, and his six "
        "paired categories. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Dārukammika's giving practice"),
        ("p", "&sect;1", "an6.59:1.1-2.1"),
        ("h3", "Wilderness and village; almsfood and invitations"),
        ("p", "&sect;2", "an6.59:3.1-6.4"),
        ("h3", "Rag robes and householder-donated robes; the conclusion"),
        ("p", "&sect;3", "an6.59:7.1-9.4"),
    ],
    quiz=[
        {"q": "What criteria does Dārukammika describe using to select recipients of his "
              "family's gifts?",
         "opts": [
             "Wealth and social standing",
             "Being perfected or on the path to it, living in the wilderness, eating only "
             "almsfood, and wearing rag robes",
             "Age and seniority alone",
             "Personal friendship"],
         "correct": 1,
         "expl": "A set of outward markers Dārukammika trusts as indicators of spiritual "
                 "attainment."},
        {"q": "How does the Buddha respond to these criteria?",
         "opts": [
             "He fully endorses them as reliable",
             "He points out that Dārukammika's comfortable lay life makes it genuinely hard for "
             "him to know who is actually perfected, since none of these outward markers "
             "settle the question",
             "He rejects Dārukammika's generosity entirely",
             "He refuses to discuss the matter"],
         "correct": 1,
         "expl": "A direct but gentle correction of the criteria, not a rejection of giving "
                 "itself."},
        {"q": "What six mendicant circumstances does the Buddha address in pairs?",
         "opts": [
             "Age, gender, wealth, health, education, and nationality",
             "Wilderness or village dwelling, almsfood or accepted invitations, rag robes or "
             "householder-donated robes",
             "The five faculties plus liberation",
             "Six different meditation techniques"],
         "correct": 1,
         "expl": "Three pairs of outward circumstances, each judged by the same underlying "
                 "criterion."},
        {"q": "What single criterion determines whether a mendicant in any of these six "
              "categories is praiseworthy or reprehensible?",
         "opts": [
             "Which specific category they belong to",
             "Whether they are restless, insolent, and undisciplined, or mindful, aware, and "
             "composed — identical in every category",
             "How long they have been ordained",
             "How much wealth their family has"],
         "correct": 1,
         "expl": "The category itself carries no information; conduct is what actually "
                 "distinguishes mendicants."},
        {"q": "Does the discourse argue that village-dwelling or comfortably-robed mendicants "
              "are actually superior to wilderness-dwelling, rag-robed ones?",
         "opts": [
             "Yes, it reverses the usual hierarchy",
             "No — it insists the category itself carries no information about conduct in "
             "either direction, rather than simply inverting the original mistake",
             "It declares wilderness dwelling forbidden",
             "It does not address this question"],
         "correct": 1,
         "expl": "A rejection of category-based judgment altogether, not a reversal of it."},
        {"q": "How does this discourse end?",
         "opts": [
             "With Dārukammika refusing to give any more gifts",
             "With the Buddha's direct encouragement to give to the Saṅgha, and Dārukammika's "
             "resolution to do so from that day forward",
             "With an unresolved disagreement",
             "With Dārukammika converting to a different teacher"],
         "correct": 1,
         "expl": "A conversion built on practical correction rather than doctrinal argument or "
                 "demonstrated meditative attainment."},
        {"q": "Where is AN 6.59 set?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house",
             "Sāvatthī, in Jeta's Grove",
             "Varanasi, at Isipatana"],
         "correct": 1,
         "expl": "A specific, named location for this householder dialogue."},
        {"q": "What does <em>uddhata unnaḷa capala mukhara vikiṇṇavāca</em> describe?",
         "opts": [
             "The praiseworthy mendicant",
             "The reprehensible mendicant — restless, insolent, fickle, scurrilous, "
             "loose-tongued",
             "A layperson's virtues",
             "A specific meditative attainment"],
         "correct": 1,
         "expl": "The repeated negative description applied identically across all six "
                 "categories."},
        {"q": "What lifestyle details does the Buddha use to characterize Dārukammika's own "
              "position?",
         "opts": [
             "Living as an ascetic himself",
             "Enjoying sensual pleasures, living with children, using imported sandalwood, "
             "wearing garlands and makeup, and accepting gold and currency",
             "Living in extreme poverty",
             "Having no family at all"],
         "correct": 1,
         "expl": "The comfortable lay circumstances that the Buddha says make it hard for him "
                 "to judge others' inner attainment."},
        {"q": "What broader point does this discourse make about judging spiritual attainment?",
         "opts": [
             "That it is always possible to judge correctly from outward signs",
             "That outward category — where someone lives, what they eat, what they wear — "
             "does not reliably indicate inner attainment; conduct within any category is what "
             "actually matters",
             "That only mendicants can judge other mendicants",
             "That giving gifts is pointless since attainment can't be verified"],
         "correct": 1,
         "expl": "A consistent theme with AN 6.44's warning against judging individuals by "
                 "outward comparison."},
    ],
    marginalia=[
        ("Six paired circumstances", [
            "wilderness / village",
            "almsfood / invitations",
            "rag robes / donated robes",
        ]),
        ("One real criterion", [
            "restless &amp; undisciplined:",
            "reprehensible, always",
            "mindful &amp; composed: praised",
        ]),
        ("Not a reversal", [
            "category carries no",
            "information either way —",
            "conduct alone decides",
        ]),
        ("Cross-references", [
            "AN 6.44 &middot; a related caution on judgment",
        ]),
    ],
    further=[
        '<a href="%s/an6.59/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.60.html">AN 6.60 &middot; With Hatthisāriputta</a> &mdash; next, a '
        "mendicant who resigns and later returns.",
        '<a href="an-6.58.html">AN 6.58 &middot; Defilements</a> &mdash; previous, a different '
        "register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.60 — Hatthisāriputtasutta
# --------------------------------------------------------------------------- #
page(
    60, "Hatthisāriputta", "With Hatthisāriputta",
    vagga=VAGGA_6,
    meta_title="AN 6.60 — With Hatthisāriputta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Hatthisāriputtasutta, "
        "in which Mahākoṭṭhita uses seven similes to warn that meditative attainment is no "
        "guarantee against relapse, before the mendicant he warned about proves it. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Varanasi, at Isipatana, in the deer park"),
        ("Speakers", "Venerable Mahākoṭṭhita, Venerable Citta Hatthisāriputta, and their "
                     "companions; then the Buddha"),
        ("Form", "An interruption, a rebuke, a defense, a long chain of paired examples with "
                 "matching similes, and a narrative confirmation"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "Warnings that meditative attainment alone does not guarantee "
                              "against relapse recur across the Chinese Āgamas; this reading "
                              "guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;#9734;&#9734; &mdash; a long discourse whose "
                       "argument depends on tracking seven parallel similes across escalating "
                       "attainments"),
    ],
    why=(
        "When a junior mendicant interrupts senior mendicants discussing the teaching, and his "
        "companions defend him as too astute to be rebuked, Mahākoṭṭhita responds with an "
        "unusually long argument: seven similes, each showing that a temporary absence of a "
        "problem does not mean the problem cannot return, applied across an escalating series "
        "of attainments up to the fourth absorption and the signless immersion. The discourse's "
        "final section confirms the warning was accurate &mdash; and adds an outcome its own "
        "argument did not fully predict."),
    guide=[
        ("The teaching in one sentence", [
            "Even a mendicant who has attained deep meditative states, up to the signless "
            "immersion of the heart, can still resign the training and return to lay life if "
            "they grow overconfident and mix too closely with others, because none of these "
            "attainments, on their own, permanently guarantees against relapse."]),
        ("Seven similes, one shared logical structure", [
            "An ox penned up can still break out and invade crops; dust settled by rain can "
            "still reappear once the ground dries; a pond's silt-free clarity after rain can "
            "return to murk; satisfaction after a good meal fades and appetite returns; a "
            "still lake can be stirred by a sudden storm; crickets silenced by an army's noise "
            "resume once the army departs. Each simile makes the identical point about a "
            "different kind of temporary absence, applied in turn to gentleness of "
            "temperament, then to each of the four absorptions, then to the signless "
            "immersion."]),
        ("A defense that misses the actual point", [
            "Citta Hatthisāriputta's companions defend him as &ldquo;astute&hellip; quite "
            "capable of talking about the teachings with the senior mendicants&rdquo; &mdash; "
            "answering a claim about capability with evidence about intelligence. "
            "Mahākoṭṭhita's reply does not dispute Citta's intelligence at all; his point "
            "throughout is that intellectual capability and even genuine meditative attainment "
            "are simply not the same thing as being safe from relapse."]),
        ("The warning confirmed, then complicated", [
            "Citta Hatthisāriputta does eventually resign the training, exactly as "
            "Mahākoṭṭhita's argument predicted. But the discourse does not end there: the "
            "Buddha's own response &mdash; &ldquo;soon Citta will remember renunciation&rdquo; "
            "&mdash; adds an outcome the seven similes, focused entirely on decline, had not "
            "themselves addressed. Citta does return, re-ordains, and reaches full awakening, "
            "an ending that complicates a straightforward reading of the warning as final or "
            "conclusive about his prospects."]),
        ("Mahākoṭṭhita's own epistemic honesty", [
            "Asked afterward whether he knew this would happen through mind-reading or through "
            "a deity's report, Mahākoṭṭhita answers both are true &mdash; he does not claim a "
            "single, simpler source for his prediction, and the discourse does not resolve "
            "which knowledge was decisive. This detail keeps the discourse's authority "
            "grounded in specific, named claims rather than a vague appeal to general wisdom."]),
    ],
    terms=[
        ("na sukaraṁ etaṁ aññena aparassa cetasā ceto paricca jānituṁ",
         "&ldquo;it's not easy to know this for those who don't encompass another's "
         "mind&rdquo; &mdash; Mahākoṭṭhita's opening qualification, framing his own knowledge "
         "as unusual rather than ordinarily available."),
        ("animittā cetovimutti",
         "&ldquo;the signless immersion of the heart&rdquo; &mdash; the final and most "
         "advanced attainment named in the sequence of similes, already met at AN 6.13 as one "
         "of the six elements of escape."),
        ("sikkhaṁ paccakkhāya hīnāyāvattissati",
         "&ldquo;will resign the training and return to a lesser life&rdquo; &mdash; the "
         "repeated outcome each simile in the sequence warns against."),
        ("cetopariyañāṇa",
         "&ldquo;knowledge encompassing another's mind&rdquo; &mdash; one of the two sources "
         "Mahākoṭṭhita names for his prediction about Citta."),
        ("nekkhammaṁ anussarissati",
         "&ldquo;will remember renunciation&rdquo; &mdash; the Buddha's own prediction, made "
         "immediately after Citta's departure, of his eventual return."),
    ],
    text_intro=(
        "The discourse in full: the interruption, Mahākoṭṭhita's seven similes, and Citta "
        "Hatthisāriputta's departure and return. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "An interruption, a rebuke, and a defense"),
        ("p", "&sect;1", "an6.60:1.1-2.5"),
        ("h3", "The ox, the dust, and the pond: three similes"),
        ("p", "&sect;2", "an6.60:3.1-6.11"),
        ("h3", "The lake and the crickets: two more similes"),
        ("p", "&sect;3", "an6.60:7.1-8.13"),
        ("h3", "Citta's departure, and his return and awakening"),
        ("p", "&sect;4", "an6.60:9.1-11.4"),
    ],
    quiz=[
        {"q": "What prompts Mahākoṭṭhita's rebuke of Citta Hatthisāriputta?",
         "opts": [
             "Citta broke a monastic precept",
             "Citta interrupted senior mendicants who were discussing the teachings",
             "Citta refused to eat almsfood",
             "Citta insulted the Buddha directly"],
         "correct": 1,
         "expl": "A breach of conversational conduct among senior mendicants."},
        {"q": "How do Citta's companions defend him?",
         "opts": [
             "By denying he interrupted anyone",
             "By calling him astute and quite capable of discussing the teachings with senior "
             "mendicants",
             "By threatening Mahākoṭṭhita",
             "By apologizing on Citta's behalf"],
         "correct": 1,
         "expl": "A defense based on intelligence, which Mahākoṭṭhita's response reframes as "
                 "beside the point."},
        {"q": "What shared logical structure do Mahākoṭṭhita's seven similes follow?",
         "opts": [
             "Each shows a permanent, irreversible change",
             "Each shows a temporary absence of a problem (an ox penned, dust settled, a pond "
             "cleared) that does not guarantee the problem cannot return",
             "Each shows two unrelated events happening simultaneously",
             "Each shows a debate between two figures"],
         "correct": 1,
         "expl": "Applied to gentleness of temperament, then each of the four absorptions, then "
                 "the signless immersion."},
        {"q": "What does Mahākoṭṭhita's argument actually dispute about Citta?",
         "opts": [
             "His intelligence",
             "Not his intelligence or even his genuine attainment, but the assumption that "
             "capability or attainment alone guarantees safety from relapse",
             "His sincerity in wanting to practice",
             "His right to be a mendicant at all"],
         "correct": 1,
         "expl": "A distinction between capability/attainment and permanent safety from "
                 "decline."},
        {"q": "What happens to Citta, confirming Mahākoṭṭhita's warning?",
         "opts": [
             "He becomes a senior teacher",
             "He eventually resigns the training and returns to lay life, exactly as predicted",
             "He is expelled from the Saṅgha",
             "Nothing happens to him"],
         "correct": 1,
         "expl": "The narrative confirms the warning's accuracy."},
        {"q": "How does the discourse complicate a simple reading of the warning as final?",
         "opts": [
             "It doesn't — the discourse ends on Citta's departure",
             "The Buddha predicts Citta will 'remember renunciation,' and Citta does return, "
             "re-ordains, and reaches full awakening — an outcome the seven similes, focused on "
             "decline, hadn't themselves addressed",
             "Citta never actually returns",
             "The Buddha declares Mahākoṭṭhita's warning mistaken"],
         "correct": 1,
         "expl": "An ending that goes beyond what the decline-focused similes alone predicted."},
        {"q": "What two sources does Mahākoṭṭhita name for his knowledge of Citta's eventual "
              "fate?",
         "opts": [
             "Only mind-reading",
             "Both encompassing Citta's mind directly and being told by deities",
             "Only a deity's report",
             "He refuses to say"],
         "correct": 1,
         "expl": "He does not simplify his claim to a single source, keeping the discourse's "
                 "authority specific rather than vague."},
        {"q": "Where is AN 6.60 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Varanasi, at Isipatana, in the deer park",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "The location where the senior mendicants were gathered discussing the "
                 "teachings."},
        {"q": "What does <em>animittā cetovimutti</em> mean, and where else has this series met "
              "it?",
         "opts": [
             "'The four absorptions' — first met at AN 6.1",
             "'The signless immersion of the heart' — already met at AN 6.13 as one of the six "
             "elements of escape",
             "'Mind-reading' — first met at AN 6.2",
             "'Recollection of the deities' — first met at AN 6.9"],
         "correct": 1,
         "expl": "The most advanced attainment in this discourse's sequence, cross-referenced "
                 "with an earlier discourse in this nipāta."},
        {"q": "What is the final attainment named before Citta's own resignation in the "
              "sequence of similes?",
         "opts": [
             "The first absorption only",
             "The signless immersion of the heart, following all four absorptions",
             "Gentleness of temperament alone",
             "Recollection of past lives"],
         "correct": 1,
         "expl": "The escalating sequence culminates in the most advanced state named, "
                 "immediately before the narrative confirms the warning."},
    ],
    marginalia=[
        ("Seven similes", [
            "penned ox &middot; settled dust",
            "cleared pond &middot; full appetite",
            "still lake &middot; silenced crickets",
        ]),
        ("Not about intelligence", [
            "Mahākoṭṭhita never disputes",
            "Citta's capability —",
            "only its guarantee"],
        ),
        ("Confirmed, then complicated", [
            "Citta does resign —",
            "but also returns,",
            "re-ordains, awakens"
        ]),
        ("Cross-references", [
            "AN 6.13 &middot; the signless release defined",
        ]),
    ],
    further=[
        '<a href="%s/an6.60/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.61.html">AN 6.61 &middot; In the Middle</a> &mdash; next, senior '
        "mendicants debating a verse from another text.",
        '<a href="an-6.59.html">AN 6.59 &middot; With Dārukammika</a> &mdash; previous, a '
        "different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.61 — Majjhesutta
# --------------------------------------------------------------------------- #
page(
    61, "Majjhe", "In the Middle",
    vagga=VAGGA_6,
    meta_title="AN 6.61 — In the Middle | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Majjhesutta, in which "
        "senior mendicants offer six different, equally valid readings of one cryptic verse "
        "before the Buddha confirms all as well spoken and adds his own intended reading. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Varanasi, at Isipatana, in the deer park"),
        ("Speakers", "Several unnamed senior mendicants, in turn; then the Buddha"),
        ("Form", "A quoted verse, six independent interpretations offered in sequence, and the "
                 "Buddha's own confirming and completing answer"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Multiple valid readings of a single cryptic verse recur as a "
                              "recognized interpretive pattern across Buddhist commentarial "
                              "literature broadly, including in the Chinese tradition; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;#9734;&#9734; &mdash; abstract and interpretively "
                       "demanding, rewarding careful attention to what each of the six readings "
                       "actually substitutes"),
    ],
    why=(
        "Senior mendicants recall a terse verse from &lsquo;The Way to the Far Shore,&rsquo; "
        "asking about a great man who has &ldquo;known both ends&rdquo; and is &ldquo;not "
        "stuck in the middle,&rdquo; escaping something called &ldquo;the seamstress.&rdquo; "
        "Six mendicants, one after another, propose six different readings of what the two "
        "ends and the middle actually refer to. Rather than picking a winner, the Buddha "
        "confirms that all six &ldquo;spoken well in a way&rdquo; &mdash; before revealing "
        "which reading he himself had originally intended."),
    guide=[
        ("The teaching in one sentence", [
            "A quoted verse about a great man who knows &ldquo;both ends,&rdquo; is not stuck "
            "in the &ldquo;middle,&rdquo; and escapes &ldquo;the seamstress&rdquo; (craving) "
            "admits at least six valid readings &mdash; contact, time, feeling, name-and-form, "
            "the sense fields, or substantial reality &mdash; each substituting different "
            "content into the verse's fixed structure while preserving craving as the constant "
            "&ldquo;seamstress&rdquo; weaving continued existence."]),
        ("A fixed structure, six different fillings", [
            "Every one of the six proposed readings keeps the verse's underlying grammar "
            "identical: one end, a second end, a middle located between or arising from them, "
            "and craving as the seamstress weaving rebirth. What changes is only which "
            "specific triad of terms fills that structure &mdash; contact/origin of contact/"
            "cessation of contact; past/future/present; pleasant feeling/painful feeling/"
            "neutral feeling; name/form/consciousness; interior sense fields/exterior sense "
            "fields/consciousness; substantial reality/its origin/its cessation."]),
        ("A verdict without a single winner", [
            "Asked directly &ldquo;who has spoken well?&rdquo; the Buddha's answer is not to "
            "rank the six proposals but to say &ldquo;you've all spoken well in a way.&rdquo; "
            "This is a genuinely unusual outcome for a doctrinal dispute in this collection "
            "&mdash; not a resolution that declares winners and losers, but a confirmation that "
            "several distinct readings can each be valid applications of one underlying "
            "principle."]),
        ("The Buddha's own reading, given last", [
            "Having validated all six, the Buddha then states which reading he himself "
            "intended when composing the verse: contact as one end, the origin of contact as "
            "the second, and the cessation of contact as the middle. His own answer is not "
            "presented as overriding the other five, but as the specific case he &ldquo;was "
            "referring to&rdquo; &mdash; one true reading among several, rather than the sole "
            "true reading that makes the others simply wrong."]),
        ("What 'the seamstress' names, across every reading", [
            "The one element every proposed reading keeps identical is craving "
            "(<em>taṇhā</em>) as &ldquo;the seamstress,&rdquo; explicitly explained as what "
            "&ldquo;weaves one to being regenerated in one state of existence or "
            "another.&rdquo; Whatever pair of ends and middle a reading proposes, the verse's "
            "actual claim about what needs to be escaped &mdash; craving itself &mdash; does "
            "not change."]),
    ],
    terms=[
        ("pārāyana",
         "&ldquo;The Way to the Far Shore&rdquo; &mdash; the text this discourse's verse is "
         "quoted from, a well-known collection of verses elsewhere in the canon."),
        ("metteyyapañha",
         "&ldquo;The Questions of Metteyya&rdquo; &mdash; the specific section within the "
         "Pārāyana this verse belongs to."),
        ("ubhante viditvā",
         "&ldquo;having known both ends&rdquo; &mdash; the verse's central phrase, given at "
         "least six distinct valid readings across this discourse."),
        ("majjhe na līyati",
         "&ldquo;not stuck in the middle&rdquo; &mdash; the second key phrase, likewise given "
         "multiple readings."),
        ("taṇhaṁ tantavāyaṁ",
         "&ldquo;craving, the seamstress&rdquo; &mdash; the term held constant across every one "
         "of the six proposed interpretations."),
    ],
    text_intro=(
        "The discourse in full: the quoted verse, six independent readings, and the Buddha's "
        "confirmation and own reading. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The verse, recalled and questioned"),
        ("p", "&sect;1", "an6.61:1.1-3.1"),
        ("h3", "Six mendicants, six readings"),
        ("p", "&sect;2", "an6.61:3.2-8.4"),
        ("h3", "The Buddha's confirmation, and his own reading"),
        ("p", "&sect;3", "an6.61:9.1-12.6"),
    ],
    quiz=[
        {"q": "What verse do the senior mendicants recall and question?",
         "opts": [
             "A verse about the six recollections",
             "A verse from 'The Way to the Far Shore,' about a great man who has 'known both "
             "ends' and is 'not stuck in the middle,' escaping 'the seamstress'",
             "A verse about the six sense doors",
             "A verse warning against sleep"],
         "correct": 1,
         "expl": "A cryptic verse whose precise meaning is not immediately obvious."},
        {"q": "How many different readings do the mendicants propose?",
         "opts": [
             "One agreed reading", "Six independent readings, one from each of six mendicants "
             "in turn", "Two competing readings", "Ten readings"],
         "correct": 1,
         "expl": "Contact, time, feeling, name-and-form, the sense fields, and substantial "
                 "reality."},
        {"q": "What stays constant across all six proposed readings?",
         "opts": [
             "Nothing — each reading is completely unrelated to the others",
             "The verse's underlying structure (one end, a second end, a middle) and craving as "
             "'the seamstress' weaving continued existence",
             "Only the word 'middle'",
             "The specific content of what the 'ends' refer to"],
         "correct": 1,
         "expl": "A fixed grammar, filled with six different sets of terms."},
        {"q": "How does the Buddha respond when asked who spoke well?",
         "opts": [
             "He declares one mendicant correct and the other five wrong",
             "He confirms that all six 'spoke well in a way,' without ranking them",
             "He refuses to answer",
             "He says none of them understood the verse"],
         "correct": 1,
         "expl": "A genuinely unusual outcome — validation of multiple readings rather than a "
                 "single declared winner."},
        {"q": "What does the Buddha do after confirming all six readings?",
         "opts": [
             "Nothing further — the discourse ends there",
             "He states his own originally intended reading: contact as one end, its origin as "
             "the second, and its cessation as the middle",
             "He retracts his approval of the other five readings",
             "He asks the mendicants to vote on the best reading"],
         "correct": 1,
         "expl": "Presented as one true reading among several, not the sole correct one."},
        {"q": "What does 'the seamstress' represent, across every proposed reading?",
         "opts": [
             "Ignorance", "Craving (taṇhā), explicitly explained as what weaves one to "
             "continued existence", "Hatred", "Wrong view"],
         "correct": 1,
         "expl": "The one element every reading keeps identical, regardless of what fills the "
                 "'ends' and 'middle.'"},
        {"q": "What text is this verse quoted from?",
         "opts": [
             "The Dhammapada",
             "'The Way to the Far Shore' (Pārāyana), specifically 'The Questions of Metteyya'",
             "The Vinaya",
             "A text composed specifically for this discourse"],
         "correct": 1,
         "expl": "A well-known collection of verses referenced elsewhere in the canon."},
        {"q": "Where is AN 6.61 set?",
         "opts": [
             "Sāvatthī, in Jeta's Grove",
             "Varanasi, at Isipatana, in the deer park",
             "Rājagaha, on Vulture's Peak",
             "Ñātika, in the brick house"],
         "correct": 1,
         "expl": "The same location as AN 6.60, another discourse involving senior mendicants "
                 "in discussion."},
        {"q": "What is one of the six proposed readings of 'one end' and 'the second end'?",
         "opts": [
             "Only physical pain and physical pleasure",
             "The past and the future (with the present as the middle)",
             "Only night and day",
             "Only true and false"],
         "correct": 1,
         "expl": "One of six distinct triads proposed, each substituted into the same verse "
                 "structure."},
        {"q": "How do the mendicants decide to resolve their disagreement?",
         "opts": [
             "By continuing to argue among themselves",
             "By agreeing to go to the Buddha together and remember his answer as authoritative",
             "By voting",
             "By each keeping their own private interpretation"],
         "correct": 1,
         "expl": "A deliberate decision to seek the Buddha's own account rather than settle it "
                 "among themselves."},
    ],
    marginalia=[
        ("Six readings", [
            "contact &middot; time",
            "feeling &middot; name-form",
            "sense fields &middot; reality",
        ]),
        ("One fixed structure", [
            "end + end + middle,",
            "craving as the",
            "seamstress, throughout",
        ]),
        ("No single winner", [
            "'you've all spoken",
            "well in a way' —",
            "then his own reading",
        ]),
        ("Cross-references", [
            "AN 6.13 &middot; another discourse on release",
        ]),
    ],
    further=[
        '<a href="%s/an6.61/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.62.html">AN 6.62 &middot; Knowledge of the Faculties of Persons</a> '
        "&mdash; next, the Buddha's analysis of six kinds of individuals.",
        '<a href="an-6.60.html">AN 6.60 &middot; With Hatthisāriputta</a> &mdash; previous, a '
        "different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.62 — Purisindriyañāṇasutta
# --------------------------------------------------------------------------- #
page(
    62, "Purisindriyañāṇa", "Knowledge of the Faculties of Persons",
    vagga=VAGGA_6,
    # an-6.63.html is an already-published page, not part of this module's
    # PAGES; chain() would otherwise skip straight from 6.62 to 6.64. Set the
    # hand-off explicitly here and mirror it with prev= on AN 6.64's page(),
    # matching the mid-run old-page splice used for AN 4.13 and AN 6.15/17.
    next=("an-6.63.html", "AN 6.63 &middot; Penetrative"),
    meta_title="AN 6.62 — Knowledge of the Faculties of Persons | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Purisindriyañāṇasutta, "
        "where the Buddha explains his declaration of Devadatta's fate, then analyzes six "
        "kinds of individuals by watching which of their qualities is about to prevail. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "A town of the Kosalans, Daṇḍakappaka, and the nearby Aciravatī River"),
        ("Speakers", "An unnamed mendicant, Venerable Ānanda, and the Buddha"),
        ("Form", "A reported question, a sharp correction, a sewer simile, and six paired "
                 "individuals with matching similes"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "The Buddha's declaration about Devadatta's fate and its "
                              "explanation recur across the Chinese Āgamas and Vinaya "
                              "literature; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;#9734;&#9734; &mdash; a difficult discourse "
                       "concerning the Buddha's harshest recorded judgment, read directly "
                       "rather than softened"),
    ],
    why=(
        "A mendicant questions whether the Buddha's declaration that Devadatta was bound for "
        "hell &ldquo;for an eon, irredeemable&rdquo; was made after real deliberation or was "
        "merely a manner of speaking. The Buddha's response is uncharacteristically severe "
        "&mdash; he calls the questioner foolish or junior, and states that no other individual "
        "has ever received such wholehearted deliberation before a declaration. What follows is "
        "not a retraction but an explanation, and then a genuine teaching: how the Buddha reads "
        "a mind's trajectory, illustrated across six paired individuals."),
    guide=[
        ("The teaching in one sentence", [
            "The Buddha reads not just an individual's present mix of skillful and unskillful "
            "qualities but which quality's root is intact or broken, using that trajectory "
            "&mdash; not a snapshot &mdash; to predict whether they are liable to decline, not "
            "liable to decline, or, in Devadatta's specific case, already without a single "
            "fraction of goodness remaining."]),
        ("A difficult declaration, defended rather than softened", [
            "This guide states plainly what the discourse itself states: the Buddha declared "
            "Devadatta bound for hell for a full eon, irredeemable, and defends this as the "
            "single most carefully deliberated judgment he had ever made about any individual. "
            "The sewer simile that follows &mdash; searching all around someone submerged in "
            "feces for even a hair's-tip of unstained skin, and finding none &mdash; is "
            "offered as the discourse's own image for what total absence of remaining goodness "
            "looks like, not a softer metaphor substituted for a harsh conclusion."]),
        ("Six individuals, distinguished by trajectory, not snapshot", [
            "The Buddha's fuller teaching, prompted by this exchange, moves past Devadatta's "
            "single case to a general method: watching not merely whether skillful and "
            "unskillful qualities are both present, but which one's underlying root is "
            "&ldquo;unbroken&rdquo; and likely to grow, versus &ldquo;about to be totally "
            "destroyed.&rdquo; A first group of three individuals is judged by whether their "
            "skillful or unskillful root remains simply unbroken; a second group of three, "
            "added at Ānanda's own request, is judged by whether that root is unbroken but "
            "already nearing collapse."]),
        ("Twelve similes for six individuals, doubled for precision", [
            "The first three individuals are illustrated with seed-and-field similes: seeds "
            "sown in fertile ground will grow if intact, will not grow on bare rock regardless "
            "of quality, and spoiled seeds will not grow even in fertile ground. The second "
            "three, describing individuals whose relevant root is not just present but "
            "&ldquo;about to be totally destroyed,&rdquo; receive an entirely different set of "
            "similes &mdash; embers on rock versus embers on kindling, sunset versus sunrise, "
            "cooling coals &mdash; images of momentum and imminent tipping points rather than "
            "static growing conditions."]),
        ("A knowledge explicitly claimed as the Buddha's own, not a general method", [
            "The discourse frames this entire analysis as &ldquo;the Realized One's knowledges "
            "of the faculties of persons,&rdquo; introduced specifically because the original "
            "mendicant's doubt implied ordinary uncertainty applied to a case where the Buddha "
            "claims none existed. The teaching does not offer this six-fold reading as a "
            "method any observer could reliably apply; it is presented as what encompassing "
            "another's mind directly makes possible, which is exactly the capacity the "
            "questioning mendicant lacked."]),
    ],
    terms=[
        ("purisindriyañāṇa",
         "&ldquo;knowledge of the faculties of persons&rdquo; &mdash; the discourse's own "
         "title, naming the Buddha's capacity to read an individual's trajectory."),
        ("kusalamūla, akusalamūla",
         "&ldquo;skillful root, unskillful root&rdquo; &mdash; what the Buddha's six-fold "
         "analysis actually tracks, rather than a simple present-tense inventory of qualities."),
        ("na anupi ekaṁ vālaggamattaṁ",
         "&ldquo;not even a fraction of a hair's tip&rdquo; &mdash; the discourse's repeated "
         "phrase for a complete, total absence of the relevant quality, used of Devadatta and "
         "of the sixth individual alike."),
        ("gūthakūpa",
         "&ldquo;sewer,&rdquo; &ldquo;cesspit&rdquo; &mdash; the discourse's own graphic image "
         "for what total absence of goodness looks like, not softened in translation."),
        ("cetopariyaṁ ñatvā",
         "&ldquo;encompassing [a person's] mind, having known it&rdquo; &mdash; the stated "
         "basis of the Buddha's knowledge throughout this discourse's six-fold analysis."),
    ],
    text_intro=(
        "The discourse in full: the question about Devadatta, the Buddha's severe response and "
        "explanation, and his analysis of six individuals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A question about Devadatta"),
        ("p", "&sect;1", "an6.62:2.1-3.1"),
        ("h3", "The Buddha's response, and the sewer simile"),
        ("p", "&sect;2", "an6.62:4.1-5.8"),
        ("h3", "Three individuals, judged by an unbroken root"),
        ("p", "&sect;3", "an6.62:7.1-9.11"),
        ("h3", "Three more, judged by a root nearing collapse"),
        ("p", "&sect;4", "an6.62:10.1-13.2"),
    ],
    quiz=[
        {"q": "What question does an unnamed mendicant raise, reported to the Buddha by "
              "Ānanda?",
         "opts": [
             "Whether Devadatta ever actually existed",
             "Whether the Buddha's declaration that Devadatta was bound for hell for an eon, "
             "irredeemable, was made after real deliberation or was just a manner of speaking",
             "Whether Devadatta deserved forgiveness",
             "Whether hell itself exists"],
         "correct": 1,
         "expl": "A question implying ordinary uncertainty about an unusually severe "
                 "declaration."},
        {"q": "How does the Buddha respond to this question?",
         "opts": [
             "Mildly, treating it as a reasonable point",
             "Sharply — calling the questioner foolish or junior, and stating no other "
             "individual received such wholehearted deliberation before a declaration",
             "By retracting the original declaration",
             "By refusing to discuss Devadatta further"],
         "correct": 1,
         "expl": "An uncharacteristically severe response, defended rather than softened."},
        {"q": "What does the sewer simile illustrate?",
         "opts": [
             "The general unpleasantness of hell",
             "What total absence of remaining goodness looks like — searching all around "
             "someone submerged in feces and finding not even a hair's-tip of unstained skin",
             "A warning against physical uncleanliness",
             "A metaphor for meditation practice"],
         "correct": 1,
         "expl": "The discourse's own graphic image, presented without softening."},
        {"q": "What does the Buddha's six-fold analysis of individuals actually track?",
         "opts": [
             "Only the present-tense mix of skillful and unskillful qualities",
             "Which quality's underlying root is unbroken and likely to grow, versus about to "
             "be destroyed — trajectory, not a static snapshot",
             "Only a person's stated intentions",
             "Only outward behavior, not inner qualities"],
         "correct": 1,
         "expl": "A more dynamic analysis than simply cataloging present qualities."},
        {"q": "How are the second three individuals different from the first three?",
         "opts": [
             "They are identical, simply repeated",
             "Their relevant root is not merely present or absent but 'about to be totally "
             "destroyed' — illustrated with different similes of momentum and imminent tipping "
             "points, like embers and sunset/sunrise",
             "They apply only to lay followers",
             "They describe only fully awakened individuals"],
         "correct": 1,
         "expl": "Added at Ānanda's own request, with an entirely different set of similes."},
        {"q": "What kind of similes illustrate the first three individuals?",
         "opts": [
             "Similes of momentum and imminent change",
             "Seed-and-field similes: seeds in fertile ground, seeds on bare rock, spoiled "
             "seeds in fertile ground",
             "Water and fire similes exclusively",
             "No similes are given for these three"],
         "correct": 1,
         "expl": "Static growing-condition images, distinct from the second group's momentum "
                 "images."},
        {"q": "How does the discourse frame this entire six-fold analysis?",
         "opts": [
             "As a general method any careful observer could reliably apply",
             "As 'the Realized One's knowledges of the faculties of persons' — a capacity "
             "specifically tied to encompassing another's mind directly, which the original "
             "questioning mendicant lacked",
             "As a purely hypothetical exercise with no real application",
             "As advice for laypeople judging mendicants"],
         "correct": 1,
         "expl": "Presented as the Buddha's own specific capacity, not a general-purpose "
                 "technique."},
        {"q": "Where does this discourse's narrative take place?",
         "opts": [
             "Rājagaha, on Vulture's Peak",
             "A town of the Kosalans named Daṇḍakappaka, and the nearby Aciravatī River",
             "Sāvatthī, in Jeta's Grove",
             "Varanasi, at Isipatana"],
         "correct": 1,
         "expl": "The setting where Ānanda and other mendicants had gone to bathe."},
        {"q": "What does <em>kusalamūla</em> mean?",
         "opts": ["Unskillful root", "Skillful root", "A type of meditative absorption", "A "
                  "term for hell"],
         "correct": 1,
         "expl": "One of the two roots the Buddha's six-fold analysis tracks."},
        {"q": "How does this discourse treat its difficult content, according to the guide?",
         "opts": [
             "It softens or omits the severe declaration about Devadatta",
             "It states plainly what the discourse itself states, without softening the "
             "declaration or the sewer simile, consistent with this guide's practice at AN 6.18 "
             "and AN 6.57",
             "It argues the translation must be mistaken",
             "It refuses to engage with the difficult content at all"],
         "correct": 1,
         "expl": "A direct, honest reading rather than a smoothed-over paraphrase."},
    ],
    marginalia=[
        ("The Devadatta question", [
            "a manner of speaking,",
            "or real deliberation? —",
            "the Buddha: the latter"
        ]),
        ("Six individuals", [
            "3 judged by an",
            "unbroken root, 3 by",
            "a root near collapse"
        ]),
        ("Trajectory, not snapshot", [
            "not just what qualities",
            "are present now —",
            "which way they're heading"
        ]),
        ("Cross-references", [
            "AN 6.18 &middot; another hard text, read plainly",
            "AN 6.63 &middot; next, an earlier-published page",
        ]),
    ],
    further=[
        '<a href="%s/an6.62/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.64.html">AN 6.64 &middot; The Lion&rsquo;s Roar</a> &mdash; further '
        "ahead, past the already-published AN 6.63.",
        '<a href="an-6.61.html">AN 6.61 &middot; In the Middle</a> &mdash; previous, a '
        "different register of teaching.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.64 — Sīhanādasutta
# --------------------------------------------------------------------------- #
page(
    64, "Sīhanāda", "The Lion&rsquo;s Roar",
    vagga=VAGGA_6,
    prev=("an-6.63.html", "AN 6.63 &middot; Penetrative"),
    meta_title="AN 6.64 — The Lion's Roar | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sīhanādasutta, "
        "closing this chapter with the six powers that let the Buddha claim the bull's place "
        "and roar his lion's roar — each, he insists, available only through immersion. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Six named powers, each restated as answerable to questioners, closing on a "
                 "single unifying claim about immersion"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The ten powers of a Realized One (as opposed to this "
                              "discourse's six) are the more commonly cited number elsewhere in "
                              "the canon and across the Chinese Āgamas; this reading guide does "
                              "not assert why this discourse states six rather than ten"),
        ("Difficulty", "&starf;&starf;#9734;&#9734;&#9734; &mdash; closes this chapter with a "
                       "confident, almost declarative register distinct from most of the "
                       "chapter's dialogues"),
    ],
    why=(
        "AN 6.64 closes this chapter on the Buddha's own claimed authority, stated in the "
        "first person and without an interlocutor prompting it: six powers that let him "
        "&ldquo;claim the bull's place, roar his lion's roar in the assemblies, and turn the "
        "divine wheel.&rdquo; Elsewhere in the canon this same claim is more commonly made with "
        "ten powers rather than six; this discourse's shorter list and its closing insistence "
        "that every one of the six depends on immersion give it a distinct emphasis."),
    guide=[
        ("The teaching in one sentence", [
            "Six powers &mdash; true knowledge of the possible and impossible, of karmic "
            "results, of the absorptions and their corruption or purification, of past lives, "
            "of beings' passing and rebirth, and of the ending of defilements &mdash; let the "
            "Realized One claim the foremost place and answer any question on these six "
            "matters, and every one of the six, the discourse insists, belongs only to those "
            "with immersion."]),
        ("A declarative register, unlike most of this chapter", [
            "Where most of this chapter's discourses are dialogues &mdash; a mendicant's "
            "question, a householder's puzzle, senior mendicants debating &mdash; AN 6.64 is "
            "stated flatly in the first person with no interlocutor at all. The Buddha simply "
            "asserts what he possesses and what it enables, a register closer to declaration "
            "than exchange."]),
        ("Six powers, then the same six restated as answerable", [
            "The discourse's structure repeats each of the six twice: first as a power the "
            "Buddha possesses, then, in a second pass, as a subject on which &ldquo;if others "
            "come to the Realized One and ask questions&hellip; the Realized One answers them "
            "in whatever manner he has truly known it.&rdquo; The doubling emphasizes that "
            "these are not merely private attainments but capacities specifically tested "
            "against outside questioning."]),
        ("A shorter list than the canon's more familiar ten", [
            "Readers familiar with the ten <em>tathāgatabala</em> named more prominently "
            "elsewhere in the canon will notice this discourse states only six. The six named "
            "here overlap substantially with a subset of the fuller ten-power list "
            "&mdash; this discourse does not explain the difference in count, and this guide "
            "does not speculate about it beyond noting the variation exists."]),
        ("One closing claim unifying all six", [
            "The discourse's final line makes a single, sweeping claim about all six powers "
            "together: &ldquo;immersion is the path. No immersion is the wrong path.&rdquo; "
            "Every one of the six specific knowledges named &mdash; from the possible and "
            "impossible to the ending of defilements &mdash; is said to be &ldquo;for those "
            "with immersion, not for those without immersion,&rdquo; a single unifying "
            "precondition closing a discourse otherwise built from six distinct items."]),
    ],
    terms=[
        ("tathāgatabala",
         "&ldquo;power of a Realized One&rdquo; &mdash; the discourse's own term for each of "
         "the six capacities named."),
        ("āsabhaṁ ṭhānaṁ",
         "&ldquo;the bull's place&rdquo; &mdash; the foremost position the Buddha claims on "
         "the strength of these six powers."),
        ("sīhanādaṁ nadati",
         "&ldquo;roars his lion's roar&rdquo; &mdash; the discourse's own title, an image of "
         "confident, unafraid proclamation in a public assembly."),
        ("ṭhānañca ṭhānato aṭṭhānañca aṭṭhānato",
         "&ldquo;the possible as possible and the impossible as impossible&rdquo; &mdash; the "
         "first of the six named powers."),
        ("samādhi maggo, asamādhi kummaggo",
         "&ldquo;immersion is the path, no immersion is the wrong path&rdquo; &mdash; the "
         "discourse's closing claim, unifying all six powers under one precondition."),
    ],
    text_intro=(
        "The discourse in full: the six powers of a Realized One, restated as answerable to "
        "questioners, and the closing claim about immersion. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The six powers named"),
        ("p", "&sect;1", "an6.64:1.1-6.3"),
        ("h3", "The same six, restated as answerable to questioners"),
        ("p", "&sect;2", "an6.64:7.1-12.2"),
        ("h3", "The closing claim: immersion is the path"),
        ("p", "&sect;3", "an6.64:13.1-13.7"),
    ],
    quiz=[
        {"q": "What does the Buddha claim these six powers let him do?",
         "opts": [
             "Only meditate more deeply than others",
             "Claim the bull's place, roar his lion's roar in the assemblies, and turn the "
             "divine wheel",
             "Only teach privately, never in public",
             "Avoid ever being questioned"],
         "correct": 1,
         "expl": "A claim of foremost authority, stated confidently in the first person."},
        {"q": "How does this discourse's register differ from most of this chapter's "
              "discourses, according to the guide?",
         "opts": [
             "It is identical — a dialogue with a questioning interlocutor",
             "It is declarative rather than dialogic — stated flatly in the first person with "
             "no interlocutor prompting it",
             "It is spoken by a deity, not the Buddha",
             "It is the only verse-only discourse in the chapter"],
         "correct": 1,
         "expl": "A register closer to declaration than exchange, unlike the surrounding "
                 "dialogues."},
        {"q": "How is each of the six powers treated twice in this discourse?",
         "opts": [
             "Once as a power possessed, and once as a subject the Buddha answers questions "
             "about when others come and ask",
             "Once in Pāli and once in translation",
             "Once by the Buddha and once by a disciple",
             "The six powers are named only once, not repeated"],
         "correct": 1,
         "expl": "A doubling that emphasizes these as tested, answerable capacities, not merely "
                 "private attainments."},
        {"q": "What does the guide note about this discourse's list of six powers compared to "
              "elsewhere in the canon?",
         "opts": [
             "It matches the canon's usual count exactly",
             "The canon more commonly names ten powers (tathāgatabala) elsewhere; this "
             "discourse's six overlap with a subset, and the guide does not speculate about "
             "the reason for the shorter count",
             "This is the only place powers are ever mentioned",
             "The ten-power list contradicts this six-power list"],
         "correct": 1,
         "expl": "A noted variation, without unfounded speculation about its cause."},
        {"q": "What single claim closes the discourse, unifying all six powers?",
         "opts": [
             "That the six powers are unrelated to each other",
             "'Immersion is the path. No immersion is the wrong path' — every power is said to "
             "belong only to those with immersion",
             "That only the Buddha can ever possess any of these six powers",
             "That the six powers are optional for awakening"],
         "correct": 1,
         "expl": "A single unifying precondition closing a discourse built from six distinct "
                 "items."},
        {"q": "What is the first of the six named powers?",
         "opts": [
             "Recollection of past lives",
             "True understanding of the possible as possible and the impossible as impossible",
             "Clairvoyance of beings' passing and rebirth",
             "The ending of defilements"],
         "correct": 1,
         "expl": "The opening power in the discourse's list."},
        {"q": "What does <em>sīhanādaṁ nadati</em> mean, and what does it give this discourse?",
         "opts": [
             "'Whispers quietly' — the discourse's title names its restraint",
             "'Roars his lion's roar' — an image of confident, unafraid proclamation in a "
             "public assembly, giving the discourse its title",
             "'Remains silent' — the discourse never actually speaks",
             "A term unrelated to the discourse's title"],
         "correct": 1,
         "expl": "The discourse's own title and central image."},
        {"q": "Is a setting stated for AN 6.64?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare, declarative formula with no scene given."},
        {"q": "What does the sixth power name?",
         "opts": [
             "Knowledge of karmic results only",
             "The Buddha's own realization of undefiled freedom of heart and freedom by "
             "wisdom, through the ending of defilements",
             "Knowledge of the possible and impossible",
             "Clairaudience"],
         "correct": 1,
         "expl": "The final and culminating power in the list of six."},
        {"q": "What closes this chapter, and what opens the next?",
         "opts": [
             "AN 6.64 closes Mahāvagga; the next chapter continues the Second Fifty with "
             "further discourses in the Devatāvagga",
             "This is the final discourse of the entire Sixes nipāta",
             "AN 6.64 is followed immediately by the Sevens",
             "There is no chapter after this one"],
         "correct": 0,
         "expl": "Chapter 6 of 13 in the Sixes, with the Second Fifty's remaining chapters "
                 "still ahead."},
    ],
    marginalia=[
        ("Six powers", [
            "possible/impossible",
            "karmic results &middot; jhānas",
            "past lives &middot; rebirth",
            "end of defilements",
        ]),
        ("Doubled treatment", [
            "each power possessed,",
            "then answered when",
            "others come and ask",
        ]),
        ("The closing claim", [
            "'immersion is the path,",
            "no immersion is",
            "the wrong path'",
        ]),
        ("Cross-references", [
            "AN 6.62 &middot; previous, reading a person's mind",
        ]),
    ],
    further=[
        '<a href="%s/an6.64/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.63.html">AN 6.63 &middot; Penetrative</a> &mdash; previous, an '
        "earlier-published page in this chapter.",
        '<a href="an-6.55.html">AN 6.55 &middot; With Soṇa</a> &mdash; this chapter&rsquo;s '
        "opening, for contrast with where it closes.",
    ],
)


# --------------------------------------------------------------------------- #
# Chapter 7 — Devatāvagga (AN 6.65–74), continuing the Second Fifty
# --------------------------------------------------------------------------- #
# Not to be confused with Chapter 4, also titled Devatāvagga (AN 6.31-42),
# opening the First Fifty. SuttaCentral's uid for this chapter is
# an6-dutiyapannasaka-devatavagga; the two chapters share a title but no
# content.
VAGGA_7 = "<em>Devatāvagga</em> &mdash; the seventh chapter of the Sixes, continuing the Second Fifty"


# --------------------------------------------------------------------------- #
# AN 6.65 — Anāgāmiphalasutta
# --------------------------------------------------------------------------- #
page(
    65, "Anāgāmiphala", "The Fruit of Non-Return",
    vagga=VAGGA_7,
    meta_title="AN 6.65 — The Fruit of Non-Return | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Anāgāmiphalasutta, "
        "opening the Sixes' seventh chapter with six things that block the fruit of "
        "non-return, and their six reversals. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, in a single short "
                 "discourse"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This decline/non-decline list format recurs widely across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "opening a chapter that shares its title with an earlier, unrelated one"),
    ],
    why=(
        "This is the second chapter in the Sixes titled &lsquo;Deities&rsquo;: Chapter 4 "
        "(AN 6.31&ndash;42) opened the First Fifty under the same name, and this chapter opens "
        "the Second Fifty's continuation under it again &mdash; a fresh, unrelated set of ten "
        "discourses. As with Chapter 4's opener, no deity appears here at all: the discourse is "
        "a bare pair of six-item lists naming what blocks, and what enables, the fruit of "
        "non-return, the third of the four fixed milestones of awakening."),
    guide=[
        ("The teaching in one sentence", [
            "Without giving up lack of faith, conscience, and prudence, and laziness, "
            "unmindfulness, and witlessness, non-return cannot be realized; giving up all six "
            "makes it realizable."]),
        ("Six absences, not six active faults", [
            "Every item on this list names a missing quality rather than a present vice: "
            "assaddhiya (lack of faith), ahirika (lack of conscience), anottappa (lack of "
            "prudence), kosajja (laziness), pamāda (negligence/unmindfulness), and duppaññatā "
            "(witlessness, poor wisdom). The teaching is framed as a set of gaps to fill, not "
            "temptations to resist."]),
        ("Why non-return specifically", [
            "Non-return (anāgāmitā) is reached by fully ending the five lower fetters, and its "
            "holder is reborn no more into this sense-desire realm. Pairing that specific "
            "milestone with this particular six-item list suggests these six absences are read "
            "as blocking exactly the kind of settled clarity non-return requires, rather than "
            "describing awakening in general."]),
        ("A second chapter of the same name, opening bare", [
            "Chapter 4 opened with AN 6.31, also deity-free despite its title, saving its "
            "actual deity for the discourse right after. This chapter follows the identical "
            "shape at a larger scale: it opens on a bare formula and waits until AN 6.69, its "
            "central discourse, before a deity actually appears."]),
    ],
    terms=[
        ("anāgāmiphala",
         "&ldquo;the fruit of non-return&rdquo; &mdash; the discourse's own title, the third of "
         "the four fixed milestones of awakening."),
        ("assaddhiya, ahirika, anottappa",
         "&ldquo;lack of faith, lack of conscience, lack of prudence&rdquo; &mdash; the first "
         "three of the six blocking qualities, each a named absence rather than a vice."),
        ("kosajja, pamāda, duppaññatā",
         "&ldquo;laziness, negligence, witlessness&rdquo; &mdash; the remaining three blocking "
         "qualities, closing the list."),
        ("anāgāmī",
         "&ldquo;non-returner&rdquo; &mdash; one who has ended the five lower fetters and will "
         "not be reborn again into the sense-desire realm."),
        ("Devatāvagga",
         "&ldquo;the Chapter on Deities&rdquo; &mdash; this chapter's title, shared with the "
         "earlier and unrelated Chapter 4 (AN 6.31&ndash;42)."),
    ],
    text_intro=(
        "The discourse in full: six things that block the fruit of non-return, and their six "
        "reversals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that block non-return"),
        ("p", "&sect;1", "an6.65:1.1-1.4"),
        ("h3", "Six things that enable it"),
        ("p", "&sect;2", "an6.65:2.1-2.4"),
    ],
    quiz=[
        {"q": "What milestone of awakening does this discourse's six-item list concern?",
         "opts": [
             "Stream-entry, the first milestone",
             "Non-return (anāgāmitā), the third of the four fixed milestones",
             "Arahantship, the final milestone",
             "No specific milestone is named"],
         "correct": 1,
         "expl": "The discourse's own title, Anāgāmiphalasutta."},
        {"q": "What do all six items on this discourse's list have in common, according to the "
              "guide?",
         "opts": [
             "Each is a specific act of wrongdoing",
             "Each names a missing quality — an absence to fill, not a vice to resist",
             "Each is a physical practice",
             "Each is a stage of jhāna"],
         "correct": 1,
         "expl": "Lack of faith, lack of conscience, lack of prudence, laziness, negligence, "
                 "and witlessness — six named absences."},
        {"q": "How is non-return itself defined, according to the guide?",
         "opts": [
             "Complete freedom from all future rebirth of any kind",
             "Reached by fully ending the five lower fetters; its holder is reborn no more into "
             "the sense-desire realm",
             "A temporary attainment lost through negligence",
             "Identical to stream-entry"],
         "correct": 1,
         "expl": "The third of the four fixed milestones, short of full arahantship."},
        {"q": "What is notable about this chapter's title compared to Chapter 4?",
         "opts": [
             "They are the same chapter, split across two parts of the collection",
             "Both are titled Devatāvagga, 'Chapter on Deities', but the two are unrelated in "
             "content — this one continuing the Second Fifty",
             "This chapter has no title at all",
             "Chapter 4's title was later corrected to remove 'Devatāvagga'"],
         "correct": 1,
         "expl": "A shared title across two distinct, unrelated chapters of the Sixes."},
        {"q": "Does a deity appear in AN 6.65, despite the chapter's title?",
         "opts": [
             "Yes, at the discourse's opening",
             "No — as with Chapter 4's opener, the discourse is a bare formula; a deity appears "
             "only later, at AN 6.69",
             "Yes, but only in a closing verse",
             "Multiple deities appear throughout"],
         "correct": 1,
         "expl": "The chapter's actual deity is saved for its central discourse."},
        {"q": "What does <em>duppaññatā</em> mean?",
         "opts": ["Excessive wisdom", "Witlessness, poor wisdom", "Perfect concentration", "Generosity"],
         "correct": 1,
         "expl": "The sixth and final item on the blocking list."},
        {"q": "Is a setting stated for AN 6.65?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, matching the chapter's other formulaic openings."},
        {"q": "What is the discourse's entire structure?",
         "opts": [
             "A narrated story with named characters",
             "Two matched six-item lists — the blocking six, then their direct reversal — with "
             "no elaboration",
             "A dialogue between two mendicants",
             "A set of verses only"],
         "correct": 1,
         "expl": "Cause and reversal, stated back to back with no further explanation."},
        {"q": "What three qualities open the six-item list?",
         "opts": [
             "Faith, energy, mindfulness",
             "Lack of faith, lack of conscience, lack of prudence",
             "Generosity, ethics, meditation",
             "Sensual desire, ill will, doubt"],
         "correct": 1,
         "expl": "Assaddhiya, ahirika, anottappa — the first three of six named absences."},
    ],
    marginalia=[
        ("Six blocking absences", [
            "faith &middot; conscience",
            "prudence &middot; laziness",
            "negligence &middot; witlessness",
        ]),
        ("The milestone at stake", [
            "anāgāmiphala —",
            "non-return, the third",
            "of four fixed stages",
        ]),
        ("A shared chapter title", [
            "Ch. 4 and Ch. 7 both",
            "'Devatāvagga', but",
            "wholly unrelated content",
        ]),
        ("Cross-references", [
            "AN 6.31 &middot; the earlier, same-named chapter's opener",
            "AN 6.64 &middot; previous, closing Mahāvagga",
        ]),
    ],
    further=[
        '<a href="%s/an6.65/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.31.html">AN 6.31 &middot; A Trainee</a> &mdash; the earlier chapter of '
        "the same name, opening the First Fifty; distinct in content despite the shared title.",
        '<a href="an-6.64.html">AN 6.64 &middot; The Lion&rsquo;s Roar</a> &mdash; previous, '
        "closing Mahāvagga.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.66 — Arahattasutta
# --------------------------------------------------------------------------- #
page(
    66, "Arahatta", "Perfection",
    vagga=VAGGA_7,
    meta_title="AN 6.66 — Perfection | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Arahattasutta, "
        "naming six things that block arahantship, close in shape to AN 6.65 but not "
        "identical in content. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, immediately "
                 "following AN 6.65's identical shape"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This decline/non-decline list format recurs widely across the "
                              "Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, easy "
                       "to mistake for a repeat of AN 6.65 without checking its actual list"),
    ],
    why=(
        "AN 6.66 repeats AN 6.65's exact shape &mdash; two six-item lists, blocking and "
        "enabling &mdash; one step further along the path, naming what blocks perfection "
        "(arahantta) rather than non-return. A reader who assumes the list itself is also "
        "repeated would be wrong: only one item, lack of faith, is shared between the two; the "
        "other five are entirely different."),
    guide=[
        ("The teaching in one sentence", [
            "Without giving up dullness, drowsiness, restlessness, remorse, lack of faith, and "
            "negligence, perfection cannot be realized; giving up all six makes it realizable."]),
        ("Only one item repeats from AN 6.65", [
            "AN 6.65's list was lack of faith, lack of conscience, lack of prudence, laziness, "
            "negligence, and witlessness. This discourse's list is dullness, drowsiness, "
            "restlessness, remorse, lack of faith, and negligence. Checked term by term, only "
            "lack of faith (assaddhiya) and negligence (pamāda) reappear; the other four items "
            "in each list are distinct. Two consecutive discourses in the same shape, naming "
            "six things each, are not thereby naming the same six things."]),
        ("Four of the five hindrances, named by pairs", [
            "Dullness and drowsiness (thīna-middha) and restlessness and remorse "
            "(uddhacca-kukkucca) are two of the five classic hindrances to meditation, here "
            "named individually rather than as the usual paired compounds. Doubt and sensual "
            "desire, the remaining two hindrances, are absent from this particular list."]),
        ("A higher milestone, a different obstruction", [
            "Where AN 6.65 named ethical and attentional deficits blocking non-return, this "
            "discourse's list leans toward specifically meditative hindrances (dullness, "
            "drowsiness, restlessness, remorse) blocking the final milestone. The shift in "
            "content between two structurally identical discourses tracks a shift in what is "
            "actually being obstructed."]),
    ],
    terms=[
        ("arahatta",
         "&ldquo;perfection,&rdquo; arahantship &mdash; the discourse's own title, the fourth "
         "and final milestone of awakening."),
        ("thīna-middha",
         "&ldquo;dullness and drowsiness&rdquo; &mdash; one of the five classic hindrances, "
         "named here as two separate list items."),
        ("uddhacca-kukkucca",
         "&ldquo;restlessness and remorse&rdquo; &mdash; another of the five hindrances, "
         "likewise split into two items here."),
        ("assaddhiya",
         "&ldquo;lack of faith&rdquo; &mdash; the one item genuinely shared with AN 6.65's "
         "list."),
        ("pamāda",
         "&ldquo;negligence&rdquo; &mdash; the other item shared with AN 6.65; the remaining "
         "four items in each list are distinct."),
    ],
    text_intro=(
        "The discourse in full: six things that block perfection, and their six reversals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that block perfection"),
        ("p", "&sect;1", "an6.66:1.1-1.4"),
        ("h3", "Six things that enable it"),
        ("p", "&sect;2", "an6.66:2.1-2.4"),
    ],
    quiz=[
        {"q": "What milestone does AN 6.66's list concern?",
         "opts": [
             "Non-return, the same milestone as AN 6.65",
             "Perfection (arahatta), the fourth and final milestone of awakening",
             "Stream-entry, the first milestone",
             "No milestone is specified"],
         "correct": 1,
         "expl": "The discourse's own title, Arahattasutta."},
        {"q": "How many of AN 6.66's six items are genuinely shared with AN 6.65's list, "
              "checked term by term?",
         "opts": [
             "All six — the two lists are identical",
             "Only two: lack of faith and negligence; the other four items in each list differ",
             "None at all",
             "Four of the six"],
         "correct": 1,
         "expl": "A close look shows only assaddhiya and pamāda recur; dullness, drowsiness, "
                 "restlessness, and remorse are new to this discourse."},
        {"q": "What caution does the guide draw from this partial overlap?",
         "opts": [
             "That the two discourses should be read as one teaching",
             "That two consecutive, structurally identical discourses naming six things each "
             "are not thereby naming the same six things",
             "That AN 6.66 is a corrupted copy of AN 6.65",
             "That the overlap proves both lists are equally important"],
         "correct": 1,
         "expl": "Shared shape does not guarantee shared content — checked here term by term."},
        {"q": "Which classic hindrances appear, split into individual list items, in AN 6.66?",
         "opts": [
             "Sensual desire and doubt",
             "Dullness-drowsiness and restlessness-remorse",
             "All five hindrances at once",
             "None — this list names no hindrances"],
         "correct": 1,
         "expl": "Two of the five classic hindrances, each split into two separate list items."},
        {"q": "Which two of the five classic hindrances are absent from this list?",
         "opts": [
             "Dullness and drowsiness",
             "Doubt and sensual desire",
             "Restlessness and remorse",
             "None are absent — all five appear"],
         "correct": 1,
         "expl": "Only four of the five hindrances' components appear, plus lack of faith and "
                 "negligence."},
        {"q": "According to the guide, how does this list's character differ from AN 6.65's?",
         "opts": [
             "It is identical in character",
             "It leans toward specifically meditative hindrances, tracking a shift toward what "
             "blocks the final milestone rather than non-return",
             "It concerns only ethical conduct",
             "It concerns only social relationships"],
         "correct": 1,
         "expl": "A shift in content tracking a shift in what is actually being obstructed."},
        {"q": "Is a setting stated for AN 6.66?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, matching AN 6.65 immediately before it."},
        {"q": "What does <em>uddhacca-kukkucca</em> mean?",
         "opts": ["Dullness and drowsiness", "Restlessness and remorse", "Doubt and desire", "Faith and confidence"],
         "correct": 1,
         "expl": "One of the five hindrances, named individually in this list."},
        {"q": "What is the discourse's overall structure?",
         "opts": [
             "A narrated story",
             "Two matched six-item lists, blocking and enabling, with no elaboration — the same "
             "bare shape as AN 6.65",
             "A dialogue with a deity",
             "A set of verses only"],
         "correct": 1,
         "expl": "Structurally identical to AN 6.65, though not identical in content."},
    ],
    marginalia=[
        ("Six blocking items", [
            "dullness &middot; drowsiness",
            "restlessness &middot; remorse",
            "lack of faith &middot; negligence",
        ]),
        ("Only two overlap with 6.65", [
            "lack of faith,",
            "and negligence —",
            "the other four differ",
        ]),
        ("Same shape, different list", [
            "identical structure,",
            "checked term by term:",
            "not the same six things",
        ]),
        ("Cross-references", [
            "AN 6.65 &middot; previous, the shape this discourse repeats",
        ]),
    ],
    further=[
        '<a href="%s/an6.66/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.65.html">AN 6.65 &middot; The Fruit of Non-Return</a> &mdash; previous, '
        "the discourse whose shape this one repeats without repeating its content.",
        '<a href="an-6.67.html">AN 6.67 &middot; Friends</a> &mdash; next, a chained argument '
        "rather than a bare list.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.67 — Mittasutta
# --------------------------------------------------------------------------- #
page(
    67, "Mitta", "Friends",
    vagga=VAGGA_7,
    meta_title="AN 6.67 — Friends | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mittasutta, tracing a "
        "four-link chain from bad friendship down to the impossibility of giving up sensual "
        "desire, and the same chain reversed. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A four-link causal chain, stated once as blockage and once as its direct "
                 "reversal"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The theme of good and bad friendship as decisive for practice "
                              "recurs widely across the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a chain argument rather "
                       "than a flat list, requiring the reader to track each link's dependency "
                       "on the one before it"),
    ],
    why=(
        "Where AN 6.65 and 6.66 each laid six items side by side with no stated relationship "
        "between them, AN 6.67 links four items in a strict dependency chain: bad friendship "
        "blocks fulfilling the supplementary regulations, which blocks fulfilling a trainee's "
        "practice, which blocks fulfilling ethics, which blocks giving up sensual desire and "
        "the desire for rebirth in the form and formless realms. Each failure is not merely "
        "correlated with the next but stated as its precondition."),
    guide=[
        ("The teaching in one sentence", [
            "Bad friendship makes it impossible to fulfill the supplementary regulations, which "
            "makes it impossible to fulfill a trainee's practice, which makes it impossible to "
            "fulfill ethics, which makes it impossible to give up sensual desire and the desire "
            "for rebirth in the form and formless realms; good friendship reverses every link."]),
        ("A chain, not a list", [
            "Each of the four links names one thing as impossible without the thing before it, "
            "rather than presenting four independent items the way AN 6.65 and 6.66 did. The "
            "reader is meant to trace cause through cause, ending at the chain's final and most "
            "consequential term: giving up desire for rebirth in any of the three realms."]),
        ("Friendship named first, not last", [
            "Of everything that could open a chain ending in freedom from rebirth, this "
            "discourse opens with something as ordinary as who a mendicant spends time with, "
            "&ldquo;frequenting, accompanying, and attending&rdquo; them and &ldquo;following "
            "their example.&rdquo; The choice suggests companionship is treated here not as a "
            "minor social preference but as the first domino in a chain reaching all the way to "
            "liberation."]),
        ("What the supplementary regulations are", [
            "The &ldquo;practice dealing with the supplementary regulations&rdquo; "
            "(abhisamācārikā dhammā) names the detailed rules of conduct beyond the core "
            "precepts &mdash; etiquette, decorum, the small disciplines of communal monastic "
            "life. The chain's claim is that these small disciplines, easy to dismiss as "
            "peripheral, are the very foundation the rest of the chain depends on."]),
        ("Three realms, one closing term", [
            "The chain's final link does not stop at sensual desire alone but names the desire "
            "for rebirth in the realm of luminous form and the formless realm as well &mdash; "
            "the three domains a fully freed mind has let go of. The chain that began with "
            "ordinary companionship ends at the outer edge of the entire cosmos as this "
            "literature maps it."]),
    ],
    terms=[
        ("mitta",
         "&ldquo;friend&rdquo; &mdash; the discourse's own title, and its opening term."),
        ("abhisamācārikā dhammā",
         "&ldquo;the practice dealing with the supplementary regulations&rdquo; &mdash; detailed "
         "rules of conduct beyond the core precepts, the chain's first dependent link."),
        ("sekhā dhammā",
         "&ldquo;the practice of a trainee&rdquo; &mdash; the chain's second link, echoing the "
         "sekha already defined at AN 5.1 and AN 6.31 earlier in this series."),
        ("sīla",
         "&ldquo;ethics&rdquo; &mdash; the chain's third link, on which the final release from "
         "desire depends."),
        ("rūpūpapatti, arūpūpapatti",
         "&ldquo;rebirth in the realm of luminous form, rebirth in the formless realm&rdquo; "
         "&mdash; named alongside sensual desire as what the completed chain allows one to give "
         "up."),
    ],
    text_intro=(
        "The discourse in full: the four-link chain that begins with bad friendship, and the "
        "same chain reversed. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The chain that begins with bad friends"),
        ("p", "&sect;1", "an6.67:1.1-1.4"),
        ("h3", "The same chain, reversed"),
        ("p", "&sect;2", "an6.67:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does AN 6.67's structure differ from AN 6.65 and 6.66's?",
         "opts": [
             "It is a bare six-item list, like the two before it",
             "It is a four-link causal chain, where each item is stated as impossible without "
             "the one before it, rather than independent items side by side",
             "It contains no list or chain at all",
             "It repeats AN 6.65's exact list"],
         "correct": 1,
         "expl": "A dependency chain, not a flat list of unrelated items."},
        {"q": "What opens the chain?",
         "opts": [
             "Lack of faith",
             "Bad friendship — frequenting, accompanying, attending, and following the example "
             "of bad friends and companions",
             "Failure to meditate",
             "Breaking a specific precept"],
         "correct": 1,
         "expl": "Ordinary companionship, treated as the chain's first domino."},
        {"q": "What does 'the practice dealing with the supplementary regulations' "
              "(abhisamācārikā dhammā) refer to?",
         "opts": [
             "The four core precepts only",
             "Detailed rules of conduct beyond the core precepts — etiquette, decorum, the "
             "small disciplines of communal life",
             "Rules for laypeople exclusively",
             "A separate scripture unrelated to monastic conduct"],
         "correct": 1,
         "expl": "Small disciplines the chain treats as foundational, not peripheral."},
        {"q": "What does the chain's final link name, beyond sensual desire alone?",
         "opts": [
             "Nothing further — sensual desire is the only thing named",
             "The desire for rebirth in the realm of luminous form and the formless realm as "
             "well",
             "Desire for food and sleep",
             "Desire for social status"],
         "correct": 1,
         "expl": "All three realms this literature maps — sensual, form, and formless."},
        {"q": "What is the chain's second link, after the supplementary regulations?",
         "opts": [
             "Immersion",
             "Fulfilling the practice of a trainee (sekhā dhammā)",
             "Fulfilling wisdom directly",
             "Renouncing lay life"],
         "correct": 1,
         "expl": "Echoing the sekha already defined earlier in this series."},
        {"q": "What is the chain's third link, before the final release from desire?",
         "opts": ["Immersion", "Ethics (sīla)", "Faith", "Generosity"],
         "correct": 1,
         "expl": "Ethics is what the chain's final release from desire is said to depend on."},
        {"q": "How does the guide characterize the choice to open this chain with friendship?",
         "opts": [
             "As an arbitrary, unimportant detail",
             "As treating something as ordinary as companionship as the first domino in a chain "
             "reaching all the way to liberation",
             "As a mistake in the text",
             "As applying only to lay followers"],
         "correct": 1,
         "expl": "Companionship as foundational, not a minor social preference."},
        {"q": "Is a setting stated for AN 6.67?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, matching the two discourses before it."},
        {"q": "What is the discourse's overall method?",
         "opts": [
             "A narrated story with named characters",
             "A four-link dependency chain, stated once as blockage and once reversed, with no "
             "further elaboration",
             "A dialogue with a deity",
             "A set of verses only"],
         "correct": 1,
         "expl": "Chain and reversal, back to back, in the same compressed style as this "
                 "chapter's other formulaic discourses."},
    ],
    marginalia=[
        ("The four-link chain", [
            "bad friends &rarr;",
            "no supplementary rules &rarr;",
            "no trainee's practice &rarr;",
            "no ethics &rarr; no release",
        ]),
        ("Friendship first", [
            "ordinary companionship",
            "as the first domino",
            "reaching to liberation",
        ]),
        ("Three realms, closed together", [
            "sensual desire,",
            "form, and formless —",
            "all released at the chain's end",
        ]),
        ("Cross-references", [
            "AN 6.66 &middot; previous, a bare list rather than a chain",
        ]),
    ],
    further=[
        '<a href="%s/an6.67/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.66.html">AN 6.66 &middot; Perfection</a> &mdash; previous, a flat '
        "six-item list rather than a dependency chain.",
        '<a href="an-6.68.html">AN 6.68 &middot; Enjoying Company</a> &mdash; next, a longer '
        "six-link chain on the same underlying theme of company kept.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.68 — Saṅgaṇikārāmasutta
# --------------------------------------------------------------------------- #
page(
    68, "Saṅgaṇikārāma", "Enjoying Company",
    vagga=VAGGA_7,
    meta_title="AN 6.68 — Enjoying Company | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saṅgaṇikārāmasutta, "
        "tracing a six-link chain from enjoying company down to the impossibility of realizing "
        "extinguishment, and the same chain reversed. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A six-link causal chain, longer than AN 6.67's four, stated once as blockage "
                 "and once as its direct reversal"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The theme of solitude as a precondition for insight recurs "
                              "widely across the Chinese Āgamas; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a longer chain than AN "
                       "6.67's, ending at extinguishment itself rather than at the giving up of "
                       "desire"),
    ],
    why=(
        "AN 6.68 extends AN 6.67's chain form to six links instead of four, and pushes the "
        "final term further: not the giving up of desire for the three realms, but the direct "
        "realization of extinguishment (nibbāna) itself. The chain again opens with something "
        "social &mdash; not friendship this time, but a taste for company and crowds &mdash; "
        "and traces it all the way to the fetters and their ending."),
    guide=[
        ("The teaching in one sentence", [
            "Enjoying company blocks taking pleasure in solitude, which blocks learning the "
            "mind's patterns, which blocks right view, which blocks right immersion, which "
            "blocks giving up the fetters, which blocks realizing extinguishment; not enjoying "
            "company reverses every link."]),
        ("Six links, not four", [
            "Compared to AN 6.67's four-link chain, this discourse adds two further links "
            "&mdash; right view leading to right immersion, and the fetters' ending leading to "
            "extinguishment &mdash; extending the argument's reach all the way to the final "
            "goal rather than stopping at the giving up of desire."]),
        ("Solitude as the second link, not the first", [
            "The chain does not claim company itself directly blocks extinguishment; it first "
            "blocks solitude, and only through the loss of that solitude does everything "
            "further become unreachable. The argument is not against company as such but "
            "against company as it displaces the specific condition &mdash; being alone in "
            "seclusion &mdash; that lets the mind's patterns become visible in the first place."]),
        ("Learning the mind before fulfilling right view", [
            "Between solitude and right view sits a link easy to pass over: learning "
            "&ldquo;the patterns of the mind&rdquo; (cittassa nimittaṁ). The chain implies right "
            "view is not reached by reasoning alone but by first coming to know, through "
            "solitude, what one's own mind actually does &mdash; a precondition stated before "
            "view, immersion, or the fetters' ending are even mentioned."]),
        ("A companion piece to AN 6.67, not a repeat", [
            "Both discourses open on a social theme and close on liberation through a strict "
            "dependency chain, but neither the opening term (friends versus company) nor the "
            "closing term (giving up desire versus realizing extinguishment) is shared between "
            "them. They stand as two variations on chain-argument form, not one teaching told "
            "twice."]),
    ],
    terms=[
        ("saṅgaṇikārāma",
         "&ldquo;one who enjoys company and crowds&rdquo; &mdash; the discourse's own title and "
         "opening term."),
        ("paṭisallāna",
         "&ldquo;seclusion,&rdquo; solitude &mdash; the chain's first dependent link, lost when "
         "company is preferred."),
        ("cittassa nimittaṁ",
         "&ldquo;the patterns of the mind&rdquo; &mdash; what solitude allows one to learn, the "
         "chain's second link."),
        ("sammādiṭṭhi, sammāsamādhi",
         "&ldquo;right view, right immersion&rdquo; &mdash; the chain's third and fourth links, "
         "the two elements of the path named explicitly."),
        ("saṁyojana, nibbāna",
         "&ldquo;the fetters, extinguishment&rdquo; &mdash; the chain's final two links, ending "
         "at the same goal named at the close of the AN 6.55 mountain simile earlier in this "
         "chapter."),
    ],
    text_intro=(
        "The discourse in full: the six-link chain that begins with enjoying company, and the "
        "same chain reversed. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The chain that begins with enjoying company"),
        ("p", "&sect;1", "an6.68:1.1-1.6"),
        ("h3", "The same chain, reversed"),
        ("p", "&sect;2", "an6.68:2.1-2.6"),
    ],
    quiz=[
        {"q": "How many links does AN 6.68's chain have, compared to AN 6.67's four?",
         "opts": ["Three", "Five", "Six", "Eight"],
         "correct": 2,
         "expl": "Two more links than AN 6.67, ending at extinguishment rather than the giving "
                 "up of desire."},
        {"q": "What opens AN 6.68's chain?",
         "opts": [
             "Bad friendship, the same opening term as AN 6.67",
             "Enjoying company and groups, loving them and liking to enjoy them",
             "Lack of faith",
             "Breaking a specific precept"],
         "correct": 1,
         "expl": "A distinct opening term from AN 6.67's, despite the shared chain structure."},
        {"q": "According to the guide, what is the chain's first dependent link — what does "
              "enjoying company block directly?",
         "opts": [
             "Right view, directly",
             "Taking pleasure in being alone in seclusion (paṭisallāna)",
             "Ethics",
             "Faith"],
         "correct": 1,
         "expl": "Company blocks solitude first; everything further depends on that loss."},
        {"q": "What does the guide say sits between solitude and right view in the chain?",
         "opts": [
             "Nothing — solitude leads directly to right view",
             "Learning 'the patterns of the mind' (cittassa nimittaṁ), a precondition easy to "
             "pass over",
             "A period of fasting",
             "Ordination itself"],
         "correct": 1,
         "expl": "The chain implies right view depends on first coming to know one's own mind "
                 "through solitude."},
        {"q": "What is the chain's final term, beyond the fetters' ending?",
         "opts": [
             "Giving up desire for the three realms, as in AN 6.67",
             "Realizing extinguishment (nibbāna) directly",
             "Rebirth as a deity",
             "Nothing further is named"],
         "correct": 1,
         "expl": "A further reach than AN 6.67's closing term."},
        {"q": "According to the guide, is this discourse a repeat of AN 6.67's teaching?",
         "opts": [
             "Yes, word for word",
             "No — the two share chain-argument form but neither the opening nor closing terms "
             "are the same",
             "Yes, but only the closing term is shared",
             "Yes, but only the opening term is shared"],
         "correct": 1,
         "expl": "Two variations on the same compositional device, not one teaching told twice."},
        {"q": "What two path-factors are named explicitly within the chain?",
         "opts": [
             "Right speech and right action",
             "Right view and right immersion",
             "Right mindfulness and right effort",
             "Right livelihood and right resolve"],
         "correct": 1,
         "expl": "Sammādiṭṭhi and sammāsamādhi, the chain's third and fourth links."},
        {"q": "Is a setting stated for AN 6.68?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other formulaic discourses."},
        {"q": "What does the guide say the chain is actually arguing against?",
         "opts": [
             "Company as such, in every circumstance",
             "Not company as such, but company as it displaces the specific condition of "
             "solitude that lets the mind's patterns become visible",
             "Any form of social contact whatsoever",
             "Specifically the company of laypeople"],
         "correct": 1,
         "expl": "A targeted claim about what solitude enables, not a blanket rejection of "
                 "company."},
    ],
    marginalia=[
        ("The six-link chain", [
            "company &rarr; no solitude",
            "&rarr; no mind's patterns",
            "&rarr; no right view &rarr; no",
            "immersion &rarr; no release",
        ]),
        ("Longer than AN 6.67", [
            "six links, not four —",
            "ending at nibbāna,",
            "not merely desire's end",
        ]),
        ("Not against company itself", [
            "the target is solitude",
            "displaced, not company",
            "condemned outright",
        ]),
        ("Cross-references", [
            "AN 6.67 &middot; previous, the shorter four-link companion chain",
            "AN 6.69 &middot; next, where a deity finally appears",
        ]),
    ],
    further=[
        '<a href="%s/an6.68/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.67.html">AN 6.67 &middot; Friends</a> &mdash; previous, the shorter '
        "four-link companion chain.",
        '<a href="an-6.69.html">AN 6.69 &middot; A God</a> &mdash; next, where this '
        "chapter&rsquo;s title finally earns its name.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.69 — Devatāsutta
# --------------------------------------------------------------------------- #
page(
    69, "Devatā", "A God",
    vagga=VAGGA_7,
    meta_title="AN 6.69 — A God | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Devatāsutta, this "
        "chapter's namesake discourse, in which a deity names six things that prevent a "
        "mendicant's decline, and Sāriputta explains their detailed meaning. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Jeta's Grove, Anāthapiṇḍika's monastery — implied by the deity "
                    "&ldquo;lighting up the entire Jeta's Grove,&rdquo; without a separate "
                    "opening formula naming Sāvatthī directly"),
        ("Speakers", "An unnamed glorious deity, then the Buddha retelling its visit to the "
                     "mendicants, then Venerable Sāriputta explaining its brief statement in "
                     "detail, confirmed by the Buddha"),
        ("Form", "A nighttime visitation, the Buddha's next-morning retelling, and a "
                 "brief-statement/detailed-explanation exchange with Sāriputta"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Nighttime deity visitations delivering brief verses or lists to "
                              "the Buddha recur widely across the Saṁyutta and its Chinese "
                              "Āgama parallels; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the chapter's longest and "
                       "most structurally layered discourse, repeating its six-item core "
                       "formula four times across three narrators"),
    ],
    why=(
        "This is the discourse the chapter is actually named for: a glorious deity visits the "
        "Buddha by night and names six things that prevent a mendicant's decline &mdash; "
        "respect for the Teacher, the teaching, the Saṅgha, and the training, being easy to "
        "admonish, and good friendship. The Buddha retells the visit to the mendicants the next "
        "morning, and Sāriputta then supplies the detailed meaning of what the deity stated in "
        "brief, confirmed word for word by the Buddha himself."),
    guide=[
        ("The teaching in one sentence", [
            "Respect for the Teacher, the teaching, the Saṅgha, and the training, being easy to "
            "admonish, and good friendship together prevent a mendicant's decline, and each is "
            "fulfilled not merely by holding it privately but by practicing it, encouraging "
            "others toward it, and praising others who already have it."]),
        ("Another variant of a formula this series has now met several times", [
            "A near-identical six-item respect formula &mdash; for the Teacher, the teaching, "
            "the Saṅgha, and the training, plus two further items &mdash; was already met three "
            "times earlier in this chapter's First Fifty, at AN 6.32, 6.33, and 6.40, with a "
            "different fifth-and-sixth pair each time (diligence and hospitality; conscience "
            "and prudence; diligence and hospitality again, applied to all four assemblies). "
            "Checked in Pāli, this discourse's own fifth and sixth items are sovacassatā (being "
            "easy to admonish) and kalyāṇamittatā (good friendship) &mdash; a fourth distinct "
            "pairing, not a repeat of any of the three before it."]),
        ("A brief statement, given three full retellings", [
            "The deity states its six items once to the Buddha; the Buddha restates them "
            "verbatim to the mendicants the next morning; and the discourse's core formula for "
            "how each item is fulfilled &mdash; personally holding it, encouraging others "
            "toward it, and praising others who have it &mdash; is then given twice more, once "
            "by Sāriputta and once again by the Buddha confirming it word for word. Four full "
            "statements of essentially the same six-item content sit inside one discourse."]),
        ("Three parts to fulfilling each item", [
            "Sāriputta's explanation gives each of the six items the identical treatment: a "
            "mendicant personally holds it, praises holding it, encourages other mendicants who "
            "lack it to take it up, and praises those who already have it &ldquo;at the right "
            "time, truthfully and correctly.&rdquo; Respect, on this reading, is not simply a "
            "private disposition but something actively modeled, taught, and publicly "
            "recognized in others."]),
        ("The Buddha's confirmation, not correction", [
            "When the Buddha responds to Sāriputta's explanation, he does not add, subtract, or "
            "revise a single item &mdash; he repeats it in full and calls it &ldquo;good, "
            "good.&rdquo; The discourse ends not on new content but on an exact echo, a "
            "structure this series has also met with Ānanda and Mahākaccāna in earlier "
            "explanation-discourses of the Sixes."]),
    ],
    terms=[
        ("satthugāravatā, dhammagāravatā, saṅghagāravatā, sikkhāgāravatā",
         "&ldquo;respect for the Teacher, for the teaching, for the Saṅgha, for the "
         "training&rdquo; &mdash; the first four items, shared with the formula's earlier "
         "appearances at AN 6.32/6.33/6.40."),
        ("sovacassatā",
         "&ldquo;being easy to admonish&rdquo; &mdash; this discourse's own fifth item, "
         "distinct from every earlier version of the formula in this chapter."),
        ("kalyāṇamittatā",
         "&ldquo;good friendship&rdquo; &mdash; the sixth and closing item, echoing this "
         "chapter's own AN 6.67 on friendship, though the two discourses are otherwise "
         "unconnected."),
        ("aparihānāya saṁvattanti",
         "&ldquo;lead to non-decline&rdquo; &mdash; the deity's own framing of what these six "
         "things accomplish for a mendicant."),
        ("saṅkhittena bhāsitassa vitthārena attho",
         "&ldquo;the detailed meaning of what was stated in brief&rdquo; &mdash; the exact "
         "exchange Sāriputta undertakes, a recognizable genre within the Numbered Discourses."),
    ],
    text_intro=(
        "The discourse in full: the deity's nighttime visit, the Buddha's retelling, and "
        "Sāriputta's detailed explanation, confirmed by the Buddha. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A deity's nighttime visit"),
        ("p", "&sect;1", "an6.69:1.1-1.8"),
        ("h3", "The Buddha retells it to the mendicants"),
        ("p", "&sect;2", "an6.69:2.1-2.8"),
        ("h3", "Sāriputta's detailed explanation"),
        ("p", "&sect;3", "an6.69:3.1-3.13"),
        ("h3", "The Buddha's confirmation, restated in full"),
        ("p", "&sect;4", "an6.69:4.1-4.13"),
    ],
    quiz=[
        {"q": "Why is this discourse the chapter's namesake, unlike AN 6.65–68 before it?",
         "opts": [
             "It is not — no discourse in this chapter concerns a deity",
             "It is the first discourse in the chapter where an actual deity appears, visiting "
             "the Buddha by night",
             "It is the chapter's longest discourse for unrelated reasons",
             "It was composed later than the others"],
         "correct": 1,
         "expl": "AN 6.65–68 were all deity-free, bare formulas and chains."},
        {"q": "What six things does the deity name as preventing a mendicant's decline?",
         "opts": [
             "The five faculties plus liberation",
             "Respect for the Teacher, the teaching, the Saṅgha, and the training, being easy "
             "to admonish, and good friendship",
             "Faith, energy, mindfulness, immersion, and wisdom",
             "The four causes of decline named at AN 6.31"],
         "correct": 1,
         "expl": "Stated once by the deity, then restated three more times across the "
                 "discourse."},
        {"q": "This is the fourth time a similar 'respect' formula appears in this chapter of "
              "the Sixes. What varies each time, according to the guide?",
         "opts": [
             "Nothing — all four versions are word-for-word identical",
             "The first four items (respect for Teacher/teaching/Saṅgha/training) stay "
             "constant, but the fifth and sixth items differ each time — here, being easy to "
             "admonish and good friendship, checked in Pāli against the three earlier versions",
             "The formula has never appeared before in this chapter",
             "Only the setting changes; the content is always identical"],
         "correct": 1,
         "expl": "A fourth distinct pairing, not a repeat of AN 6.32, 6.33, or 6.40's fifth and "
                 "sixth items."},
        {"q": "How many times does the discourse's core six-item content get stated in full or "
              "near-full, across all three speakers?",
         "opts": ["Once", "Twice", "Four times — the deity, the Buddha's retelling, Sāriputta's "
                          "explanation, and the Buddha's confirmation", "Ten times"],
         "correct": 2,
         "expl": "A brief statement given three further full retellings within one discourse."},
        {"q": "According to Sāriputta's explanation, what three things does fulfilling each "
              "item involve?",
         "opts": [
             "Only holding it privately, with nothing further required",
             "Personally holding it, encouraging others who lack it to take it up, and praising "
             "others who already have it, at the right time and truthfully",
             "Only teaching it to laypeople",
             "Renouncing it publicly before taking it up again"],
         "correct": 1,
         "expl": "A three-part treatment applied identically to all six items."},
        {"q": "How does the Buddha respond to Sāriputta's explanation?",
         "opts": [
             "He corrects several points",
             "He repeats it in full, unchanged, and calls it 'good, good'",
             "He rejects it and offers his own different explanation",
             "He remains silent"],
         "correct": 1,
         "expl": "Confirmation by exact echo, not correction."},
        {"q": "Is Sāvatthī explicitly named as this discourse's setting?",
         "opts": [
             "Yes, in an opening formula",
             "No — the setting is only implied by the deity 'lighting up the entire Jeta's "
             "Grove'",
             "No location is implied anywhere in the text",
             "Yes, but only in the closing lines"],
         "correct": 1,
         "expl": "No separate formula names Sāvatthī directly; the location is inferred from "
                 "the deity's description."},
        {"q": "What does <em>kalyāṇamittatā</em> mean, and where else has it appeared in this "
              "chapter?",
         "opts": [
             "'Solitude' — appearing nowhere else in this chapter",
             "'Good friendship' — echoing AN 6.67's theme, though the two discourses are "
             "otherwise unconnected",
             "'Ethics' — appearing at AN 6.31",
             "A term unique to this discourse with no echo elsewhere"],
         "correct": 1,
         "expl": "The chain in AN 6.67 also concerned friendship, though the two discourses "
                 "share no other content."},
        {"q": "What genre does Sāriputta's exchange with the Buddha belong to, according to the "
              "guide?",
         "opts": [
             "A unique, one-off literary device",
             "A recognizable genre within the Numbered Discourses: expanding a brief statement "
             "into its detailed meaning",
             "A form found only outside the Numbered Discourses",
             "A form of formal debate"],
         "correct": 1,
         "expl": "Brief statement, then detailed explanation — a pattern this series has met in "
                 "earlier explanation-discourses of the Sixes."},
        {"q": "How does the deity depart after speaking?",
         "opts": [
             "It simply disappears without ceremony",
             "It bows and respectfully circles the Buddha, keeping him on its right, before "
             "vanishing right there",
             "It asks the Buddha a further question first",
             "It remains present for the rest of the discourse"],
         "correct": 1,
         "expl": "A standard formula for a deity's respectful departure after the Buddha's "
                 "silent approval."},
    ],
    marginalia=[
        ("Six things preventing decline", [
            "respect for Teacher,",
            "teaching, Saṅgha, training;",
            "easy to admonish; good friends",
        ]),
        ("A fourth respect formula", [
            "first four items constant,",
            "fifth/sixth differ each time —",
            "checked in Pāli, not assumed",
        ]),
        ("Four retellings, one discourse", [
            "deity &rarr; Buddha &rarr;",
            "Sāriputta &rarr; Buddha again,",
            "confirmed word for word",
        ]),
        ("Cross-references", [
            "AN 6.32/6.33/6.40 &middot; earlier variants of this formula, First Fifty",
            "AN 6.67 &middot; this chapter's own discourse on friendship",
        ]),
    ],
    further=[
        '<a href="%s/an6.69/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.68.html">AN 6.68 &middot; Enjoying Company</a> &mdash; previous, the '
        "chain leading up to this chapter's namesake discourse.",
        '<a href="an-6.32.html">AN 6.32 &middot; Respect</a> &mdash; an earlier version of '
        "this discourse&rsquo;s core formula, First Fifty, with a different fifth and sixth "
        "item.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.70 — Samādhisutta
# --------------------------------------------------------------------------- #
page(
    70, "Samādhi", "Immersion",
    vagga=VAGGA_7,
    meta_title="AN 6.70 — Immersion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Samādhisutta, naming "
        "immersion as the single precondition for the six higher knowledges, from psychic "
        "power to the ending of defilements. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single precondition (immersion) unlocking an enumerated list of six higher "
                 "knowledges, stated once as impossibility and once as possibility"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The six higher knowledges (chaḷabhiññā) as a standard set recur "
                              "widely across the Chinese Āgamas and Abhidharma literature; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a single-cause argument, "
                       "but with a long and vivid enumeration of psychic powers at its center"),
    ],
    why=(
        "AN 6.70 returns to a single-precondition structure last seen in this chapter's chains, "
        "but collapses it to one cause unlocking six results at once: without immersion that is "
        "&ldquo;peaceful, refined, tranquil, and unified,&rdquo; none of the six higher "
        "knowledges &mdash; psychic power, clairaudience, mind-reading, past-life recollection, "
        "clairvoyance of rebirth, and the ending of defilements &mdash; is possible; with it, "
        "all six are."),
    guide=[
        ("The teaching in one sentence", [
            "Without immersion that is peaceful, refined, tranquil, and unified, none of the "
            "six higher knowledges can be attained; with such immersion, all six become "
            "possible."]),
        ("The six higher knowledges, named in full", [
            "The list running through this discourse is the standard chaḷabhiññā: psychic "
            "power (multiplying oneself, passing through walls, walking on water, touching the "
            "sun and moon); clairaudience; reading others' minds; recollecting past lives; "
            "clairvoyance into how beings pass on according to their deeds; and the "
            "undefiled freedom of heart and wisdom through the ending of defilements — the only "
            "one of the six that marks full awakening rather than an extraordinary capacity."]),
        ("One cause, not six separate ones", [
            "Unlike AN 6.65 and 6.66's six independent blocking items, or AN 6.67 and 6.68's "
            "multi-link chains, this discourse names a single precondition &mdash; immersion "
            "&mdash; and simply repeats it as the requirement behind each of the six results in "
            "turn. The structure is closer to one cause radiating into six effects than to a "
            "chain or a list of equals."]),
        ("Five worldly powers, and one that is not", [
            "The discourse's own sixth item stands apart from the first five: where psychic "
            "power, clairaudience, mind-reading, past-life recollection, and clairvoyance are "
            "extraordinary capacities a mind might in principle misuse, the ending of "
            "defilements is described elsewhere in this literature as available only to one "
            "already free of greed, hatred, and delusion. Grouping it as a sixth item alongside "
            "five feats risks obscuring that it alone marks liberation rather than power."]),
        ("Why 'peaceful, refined, tranquil, and unified'", [
            "The discourse's opening qualifies immersion with four terms rather than naming it "
            "bare, distinguishing the kind of concentration meant here from any merely "
            "one-pointed absorption that might lack the settled quality these four words "
            "together describe."]),
    ],
    terms=[
        ("samādhi santo paṇīto passaddhaladdho ekodibhāvādhigato",
         "&ldquo;immersion that is peaceful, refined, tranquil, and unified&rdquo; &mdash; the "
         "discourse's single precondition, qualified by four terms rather than named bare."),
        ("iddhividha",
         "&ldquo;the many kinds of psychic power&rdquo; &mdash; the first and most vividly "
         "described of the six higher knowledges."),
        ("dibbasota",
         "&ldquo;clairaudience,&rdquo; the divine ear &mdash; the second higher knowledge, "
         "hearing both human and heavenly sounds."),
        ("pubbenivāsānussati",
         "&ldquo;recollection of past lives&rdquo; &mdash; the fourth higher knowledge, "
         "recalling one's own former lives with features and details."),
        ("āsavānaṁ khaya",
         "&ldquo;the ending of defilements&rdquo; &mdash; the sixth and final higher knowledge, "
         "the only one of the six that marks full awakening rather than an extraordinary "
         "capacity."),
    ],
    text_intro=(
        "The discourse in full: the six higher knowledges, each declared impossible without "
        "immersion and possible with it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Without immersion"),
        ("p", "&sect;1", "an6.70:1.1-1.8"),
        ("h3", "With immersion"),
        ("p", "&sect;2", "an6.70:2.1-2.8"),
    ],
    quiz=[
        {"q": "What single precondition does this discourse claim unlocks all six higher "
              "knowledges?",
         "opts": [
             "Faith alone",
             "Immersion that is peaceful, refined, tranquil, and unified",
             "Ethics alone",
             "Extensive scriptural learning"],
         "correct": 1,
         "expl": "One cause, qualified by four terms, behind all six results."},
        {"q": "How does this discourse's structure differ from AN 6.67 and 6.68's chains, "
              "according to the guide?",
         "opts": [
             "It is identical — another multi-link dependency chain",
             "It names one single precondition radiating into six results, rather than a "
             "sequence of links each depending on the one before it",
             "It contains no causal claim at all",
             "It reverses the direction of AN 6.67's chain"],
         "correct": 1,
         "expl": "One cause behind six effects, not a chain of sequential dependencies."},
        {"q": "What is the first of the six higher knowledges named?",
         "opts": [
             "The ending of defilements",
             "Psychic power — multiplying oneself, passing through walls, walking on water, "
             "touching the sun and moon",
             "Clairaudience",
             "Recollection of past lives"],
         "correct": 1,
         "expl": "The most vividly described of the six, opening the list."},
        {"q": "According to the guide, how does the sixth higher knowledge differ from the "
              "first five?",
         "opts": [
             "It does not differ at all — all six are equivalent capacities",
             "The first five are extraordinary capacities that could in principle be misused; "
             "the sixth, ending defilements, marks liberation rather than mere power",
             "The sixth is easier to attain than the first five",
             "The sixth requires no immersion at all"],
         "correct": 1,
         "expl": "A distinction the guide flags as easy to blur if the six are read as "
                 "equivalent items on one list."},
        {"q": "What does <em>dibbasota</em> refer to?",
         "opts": ["Reading others' minds", "Clairaudience, the divine ear", "Recollection of past lives", "Psychic power"],
         "correct": 1,
         "expl": "The second of the six higher knowledges — hearing both human and heavenly "
                 "sounds."},
        {"q": "Why does the discourse qualify immersion with four terms rather than naming it "
              "bare?",
         "opts": [
             "For poetic effect only, with no distinguishing purpose",
             "To distinguish the settled kind of concentration meant here from any merely "
             "one-pointed absorption lacking that same quality",
             "Because the four terms are unrelated to immersion",
             "To match a fixed formula used nowhere else in the canon"],
         "correct": 1,
         "expl": "'Peaceful, refined, tranquil, and unified' together specify a particular "
                 "quality of concentration."},
        {"q": "Is a setting stated for AN 6.70?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other list-form discourses."},
        {"q": "What does the fourth higher knowledge, past-life recollection, involve according "
              "to the discourse?",
         "opts": [
             "Predicting others' future rebirths only",
             "Recollecting many kinds of one's own past lives, with features and details",
             "Reading the minds of deities specifically",
             "Only recalling the immediately preceding life"],
         "correct": 1,
         "expl": "One's own former lives, recalled in detail, not others' futures."},
        {"q": "What is the standard name in this literature for the set of six knowledges "
              "listed here?",
         "opts": ["The four foundations", "Chaḷabhiññā, the six higher knowledges", "The five hindrances", "The seven factors"],
         "correct": 1,
         "expl": "A standard enumerated set recurring across the Numbered Discourses and "
                 "Abhidharma literature."},
    ],
    marginalia=[
        ("One cause, six effects", [
            "immersion — peaceful,",
            "refined, tranquil, unified —",
            "unlocks all six knowledges",
        ]),
        ("The six higher knowledges", [
            "psychic power &middot; clairaudience",
            "mind-reading &middot; past lives",
            "rebirth &middot; end of defilements",
        ]),
        ("Five powers, one liberation", [
            "the sixth item alone",
            "marks awakening —",
            "not merely a feat",
        ]),
        ("Cross-references", [
            "AN 6.67/6.68 &middot; earlier, multi-link chains rather than one cause radiating "
            "out",
        ]),
    ],
    further=[
        '<a href="%s/an6.70/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.69.html">AN 6.69 &middot; A God</a> &mdash; previous, this '
        "chapter&rsquo;s namesake discourse.",
        '<a href="an-6.71.html">AN 6.71 &middot; Capable of Realizing</a> &mdash; next, a '
        "shorter, more abstract single-cause discourse.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.71 — Sakkhibhabbasutta
# --------------------------------------------------------------------------- #
page(
    71, "Sakkhibhabba", "Capable of Realizing",
    vagga=VAGGA_7,
    meta_title="AN 6.71 — Capable of Realizing | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sakkhibhabbasutta, "
        "naming six abstract qualities of discernment and diligence that make realization "
        "possible or impossible. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single abstract quality (fourfold discernment plus diligent practice), "
                 "stated once as blocking realization and once as enabling it"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This theme of discernment as a precondition for realization "
                              "recurs widely across the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief but abstract, naming "
                       "no concrete practice, only categories of discernment"),
    ],
    why=(
        "AN 6.71 is the most abstract discourse in this chapter so far: it names no concrete "
        "practice, hindrance, or virtue, only a capacity to discern which qualities make "
        "things worse, which keep them steady, which lead to distinction, and which lead to "
        "penetration &mdash; paired with actually practicing carefully and doing what is "
        "suitable. Without both together, &ldquo;anything that can be realized&rdquo; remains "
        "out of reach, however close at hand it may be."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who cannot discern which qualities worsen, steady, distinguish, or "
            "penetrate, and who does not practice carefully and suitably, cannot realize "
            "anything realizable; discerning correctly and practicing accordingly makes "
            "realization possible."]),
        ("Four categories of discernment, not four separate teachings", [
            "&ldquo;What makes things worse, what keeps things steady, what leads to "
            "distinction, and what leads to penetration&rdquo; (hānabhāgiya, ṭhitibhāgiya, "
            "visesabhāgiya, nibbedhabhāgiya) is itself a fixed fourfold analytical set applied "
            "elsewhere in the canon to jhāna and other attainments, naming the direction a "
            "given quality tends to push practice rather than naming any specific quality "
            "itself."]),
        ("Discernment alone is not enough", [
            "The discourse pairs true understanding of these four directions with a second, "
            "separate requirement: practicing carefully (sakkaccakārī) and doing what is "
            "suitable (sappāyakārī). Knowing which way a quality tends does not by itself "
            "realize anything; the discourse insists on both correct discernment and matching "
            "conduct."]),
        ("'Since each and every one is within range'", [
            "The discourse's repeated closing clause &mdash; that whatever is realizable is "
            "&ldquo;within range&rdquo; (āyāpathe) &mdash; suggests the obstacle this discourse "
            "addresses is not distance from the goal but a failure of orientation: what blocks "
            "realization is not that it lies too far off, but that without this fourfold "
            "discernment and careful practice, a mendicant cannot find their way to what is "
            "already close at hand."]),
        ("A companion in miniature to AN 6.72", [
            "This discourse's structure &mdash; a single abstract quality, stated once as "
            "blockage and once as enablement, over a bare four-line list &mdash; is repeated "
            "immediately in AN 6.72, applied there specifically to skill in immersion rather "
            "than to realization in general."]),
    ],
    terms=[
        ("sakkhibhabba",
         "&ldquo;capable of realizing,&rdquo; &ldquo;fit to witness&rdquo; &mdash; the "
         "discourse's own title."),
        ("hānabhāgiya, ṭhitibhāgiya",
         "&ldquo;conducive to decline, conducive to stability&rdquo; &mdash; the first two of a "
         "fixed fourfold analytical set applied elsewhere in the canon to jhāna and other "
         "attainments."),
        ("visesabhāgiya, nibbedhabhāgiya",
         "&ldquo;conducive to distinction, conducive to penetration&rdquo; &mdash; the "
         "remaining two of the same fourfold set."),
        ("sakkaccakārī, sappāyakārī",
         "&ldquo;one who practices carefully, one who does what is suitable&rdquo; &mdash; the "
         "second, separate requirement paired with discernment."),
        ("āyāpathe",
         "&ldquo;within range,&rdquo; within reach &mdash; the discourse's repeated closing "
         "clause, framing the obstacle as one of orientation rather than distance."),
    ],
    text_intro=(
        "The discourse in full: the fourfold discernment and careful practice that make "
        "realization possible or impossible. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six qualities that make realization impossible"),
        ("p", "&sect;1", "an6.71:1.1-1.4"),
        ("h3", "Six qualities that make it possible"),
        ("p", "&sect;2", "an6.71:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does this discourse say makes 'anything that can be realized' unreachable?",
         "opts": [
             "Physical distance from a teacher",
             "Failing to discern what makes things worse, steady, distinguished, or penetrated, "
             "combined with not practicing carefully or suitably",
             "Lack of scriptural learning specifically",
             "Old age"],
         "correct": 1,
         "expl": "A failure of discernment and matching conduct, not a fixed list of specific "
                 "practices."},
        {"q": "What is the fourfold set named in this discourse (hānabhāgiya, ṭhitibhāgiya, "
              "visesabhāgiya, nibbedhabhāgiya)?",
         "opts": [
             "Four separate meditation techniques",
             "A fixed analytical set naming the direction a quality tends to push practice — "
             "toward decline, stability, distinction, or penetration — applied elsewhere to "
             "jhāna and other attainments",
             "The four noble truths",
             "The five hindrances"],
         "correct": 1,
         "expl": "A category of analysis, not a specific teaching unique to this discourse."},
        {"q": "According to the guide, is discernment alone sufficient for realization here?",
         "opts": [
             "Yes, discernment alone is described as sufficient",
             "No — the discourse pairs correct discernment with a second, separate requirement: "
             "practicing carefully and doing what is suitable",
             "No — only careful practice matters, discernment is irrelevant",
             "The discourse does not address this question"],
         "correct": 1,
         "expl": "Both discernment and matching conduct are required together."},
        {"q": "What does the discourse's repeated phrase 'within range' (āyāpathe) suggest, "
              "according to the guide?",
         "opts": [
             "That realization is extremely distant and difficult",
             "That the obstacle is a failure of orientation, not distance — what is realizable "
             "is already close at hand",
             "That only certain mendicants are ever within range",
             "That the phrase is a scribal error"],
         "correct": 1,
         "expl": "Framing the block as one of finding the way, not covering distance."},
        {"q": "What discourse immediately follows and repeats this one's structure in "
              "miniature, according to the guide?",
         "opts": [
             "AN 6.65", "AN 6.72, applied specifically to skill in immersion", "AN 6.31", "AN 6.55"],
         "correct": 1,
         "expl": "The same bare blockage/enablement shape, applied to a narrower target."},
        {"q": "What does <em>sakkaccakārī</em> mean?",
         "opts": ["One who is easily discouraged", "One who practices carefully", "One who teaches others", "One who meditates only briefly"],
         "correct": 1,
         "expl": "Careful practice, paired with discernment as the discourse's second "
                 "requirement."},
        {"q": "Is a setting stated for AN 6.71?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other abstract discourses."},
        {"q": "What is the discourse's overall method?",
         "opts": [
             "A narrated story with named characters",
             "A single abstract quality — fourfold discernment plus careful practice — stated "
             "once as blockage and once as enablement",
             "A dialogue with a deity",
             "An extended simile"],
         "correct": 1,
         "expl": "The chapter's most abstract discourse, naming no concrete practice or "
                 "hindrance."},
        {"q": "What does <em>visesabhāgiya</em> mean?",
         "opts": ["Conducive to decline", "Conducive to distinction", "Conducive to stability", "Conducive to doubt"],
         "correct": 1,
         "expl": "The third of the fourfold analytical set named in this discourse."},
    ],
    marginalia=[
        ("A fourfold discernment", [
            "decline &middot; stability",
            "distinction &middot; penetration —",
            "plus careful, suitable practice",
        ]),
        ("Orientation, not distance", [
            "'within range' —",
            "the obstacle is finding",
            "the way, not covering it",
        ]),
        ("This chapter's most abstract", [
            "no concrete practice named,",
            "only categories of",
            "discernment and conduct",
        ]),
        ("Cross-references", [
            "AN 6.72 &middot; next, the same shape applied to immersion specifically",
        ]),
    ],
    further=[
        '<a href="%s/an6.71/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.70.html">AN 6.70 &middot; Immersion</a> &mdash; previous, one cause '
        "radiating into six higher knowledges.",
        '<a href="an-6.72.html">AN 6.72 &middot; Strength</a> &mdash; next, this '
        "discourse&rsquo;s own shape narrowed to skill in immersion.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.72 — Balasutta
# --------------------------------------------------------------------------- #
page(
    72, "Bala", "Strength",
    vagga=VAGGA_7,
    meta_title="AN 6.72 — Strength | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Balasutta, naming six "
        "qualities — three skills in immersion plus careful, persistent, suitable practice — "
        "that produce or prevent strength in immersion. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single target quality (skill in immersion, threefold, plus diligent "
                 "practice), stated once as blocking strength and once as producing it — "
                 "AN 6.71's shape narrowed to one specific skill"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The theme of skill across entering, remaining in, and emerging "
                              "from meditative states recurs widely across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; concrete and readable, "
                       "naming three specific meditative skills rather than abstract "
                       "categories"),
    ],
    why=(
        "AN 6.72 takes AN 6.71's bare abstract shape and applies it to one specific capacity: "
        "strength in immersion, produced by three named skills &mdash; entering, remaining in, "
        "and emerging from immersion &mdash; together with practicing carefully, persistently, "
        "and suitably. Where AN 6.71 spoke of realization in the widest possible terms, this "
        "discourse narrows the same structure to something concrete and specifically "
        "meditative."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant unskilled in entering, remaining in, and emerging from immersion, who "
            "does not practice carefully and persistently, cannot attain strength in immersion; "
            "skill in all three plus diligent practice makes that strength attainable."]),
        ("Three skills, not one", [
            "Unlike AN 6.70, which treated immersion as a single unqualified precondition, this "
            "discourse breaks meditative skill into three separate competencies: entering "
            "immersion (samāpajjana), remaining in it (ṭhāna), and emerging from it "
            "(vuṭṭhāna). A mendicant could plausibly be skilled at entering immersion while "
            "still lacking skill at the other two; the discourse names all three as required "
            "together."]),
        ("Persistence added to AN 6.71's careful and suitable practice", [
            "AN 6.71 named practicing carefully (sakkaccakārī) and suitably (sappāyakārī) as "
            "its second requirement. This discourse adds a third: persistently (āsevanakārī) "
            "&mdash; naming sustained repetition specifically, where AN 6.71's more general "
            "formula did not."]),
        ("A specific application of AN 6.71's general structure", [
            "This discourse's title, &lsquo;Strength,&rsquo; names the specific result AN 6.71 "
            "left unspecified as &ldquo;anything that can be realized.&rdquo; Read together, the "
            "two discourses model the same reasoning applied at two different levels of "
            "generality: one covering realization broadly, the other narrowed to strength in "
            "immersion specifically."]),
        ("Skill as a matter of degree, not presence or absence", [
            "Naming skill in entering, remaining, and emerging separately implies these are "
            "capacities that develop with practice and can be partial, not switches that are "
            "simply on or off. The discourse's closing requirement of persistent practice fits "
            "this reading: strength in immersion is treated as something built over time, not "
            "granted all at once."]),
    ],
    terms=[
        ("bala",
         "&ldquo;strength&rdquo; &mdash; the discourse's own title, here specifically strength "
         "in immersion."),
        ("samāpajjana, ṭhāna, vuṭṭhāna",
         "&ldquo;entering, remaining in, emerging from&rdquo; immersion &mdash; the three "
         "distinct skills this discourse names as required together."),
        ("sakkaccakārī, āsevanakārī, sappāyakārī",
         "&ldquo;one who practices carefully, persistently, and suitably&rdquo; &mdash; the "
         "discourse's second requirement, adding persistence to AN 6.71's careful and suitable "
         "practice."),
        ("samādhibala",
         "&ldquo;strength in immersion&rdquo; &mdash; the specific attainment this discourse "
         "concerns, narrower than AN 6.71's unspecified realization."),
        ("samādhikusala",
         "&ldquo;skilled in immersion&rdquo; &mdash; the general quality this discourse breaks "
         "into three separate, named competencies."),
    ],
    text_intro=(
        "The discourse in full: three skills in immersion plus careful, persistent, suitable "
        "practice, and their absence. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six qualities that prevent strength in immersion"),
        ("p", "&sect;1", "an6.72:1.1-1.4"),
        ("h3", "Six qualities that produce it"),
        ("p", "&sect;2", "an6.72:2.1-2.4"),
    ],
    quiz=[
        {"q": "What specific attainment does AN 6.72 concern, narrower than AN 6.71's "
              "'anything that can be realized'?",
         "opts": ["Ethical purity", "Strength in immersion (samādhibala)", "Scriptural mastery", "Physical health"],
         "correct": 1,
         "expl": "The discourse's own title, and a specific application of AN 6.71's general "
                 "shape."},
        {"q": "What three skills does the discourse name as required together?",
         "opts": [
             "Faith, energy, and mindfulness",
             "Entering, remaining in, and emerging from immersion",
             "Generosity, ethics, and meditation",
             "Speaking, listening, and reflecting"],
         "correct": 1,
         "expl": "Samāpajjana, ṭhāna, and vuṭṭhāna — three distinct competencies, not one "
                 "general skill."},
        {"q": "Why does the guide say all three skills are named separately, rather than as "
              "one unqualified 'skill in immersion'?",
         "opts": [
             "For stylistic variety only",
             "Because a mendicant could plausibly be skilled at one, such as entering, while "
             "still lacking the other two",
             "Because the three skills are actually identical",
             "The guide does not address this"],
         "correct": 1,
         "expl": "Three separable competencies, all required together for strength in "
                 "immersion."},
        {"q": "What third requirement does this discourse add to AN 6.71's careful and "
              "suitable practice?",
         "opts": [
             "Practicing with a group of at least four others",
             "Practicing persistently (āsevanakārī)",
             "Practicing only at night",
             "Practicing without any instruction"],
         "correct": 1,
         "expl": "Sustained repetition specifically, absent from AN 6.71's more general "
                 "formula."},
        {"q": "How does the guide relate AN 6.72 to AN 6.71?",
         "opts": [
             "As two unrelated, independent teachings",
             "As the same reasoning applied at two levels of generality — AN 6.71 covering "
             "realization broadly, AN 6.72 narrowed to strength in immersion specifically",
             "As directly contradictory teachings",
             "As two versions of exactly the same discourse"],
         "correct": 1,
         "expl": "AN 6.72's title names the specific result AN 6.71 left unspecified."},
        {"q": "What does the guide say about skill in entering, remaining, and emerging, based "
              "on how the discourse treats them?",
         "opts": [
             "They are binary — either fully present or entirely absent",
             "They are treated as capacities that develop with practice and can be partial, not "
             "simple on/off switches",
             "They cannot be developed through practice at all",
             "They apply only to advanced meditators"],
         "correct": 1,
         "expl": "The closing requirement of persistent practice fits a picture of gradual "
                 "development."},
        {"q": "Is a setting stated for AN 6.72?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, matching AN 6.71 immediately before it."},
        {"q": "What does <em>vuṭṭhāna</em> mean?",
         "opts": ["Entering immersion", "Remaining in immersion", "Emerging from immersion", "Avoiding immersion"],
         "correct": 2,
         "expl": "The third of the three named skills — emerging from immersion."},
        {"q": "How does this discourse's difficulty compare to AN 6.71's, according to the "
              "guide?",
         "opts": [
             "It is more abstract and harder to follow",
             "It is more concrete and readable, naming three specific meditative skills rather "
             "than abstract categories",
             "The two are identical in difficulty",
             "This discourse names no skills at all"],
         "correct": 1,
         "expl": "A specific, concrete application of AN 6.71's more abstract structure."},
    ],
    marginalia=[
        ("Three skills in immersion", [
            "entering &middot; remaining",
            "&middot; emerging — all three",
            "required together",
        ]),
        ("Persistence, newly added", [
            "careful, persistent,",
            "suitable practice —",
            "a third term beyond AN 6.71",
        ]),
        ("The general made specific", [
            "AN 6.71: realization,",
            "broadly — AN 6.72:",
            "strength in immersion",
        ]),
        ("Cross-references", [
            "AN 6.71 &middot; previous, the same shape in its general form",
        ]),
    ],
    further=[
        '<a href="%s/an6.72/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.71.html">AN 6.71 &middot; Capable of Realizing</a> &mdash; previous, '
        "the same structure in its most general form.",
        '<a href="an-6.73.html">AN 6.73 &middot; First Absorption (1st)</a> &mdash; next, '
        "a return to concrete named hindrances.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.73 — Paṭhamatajjhānasutta
# --------------------------------------------------------------------------- #
page(
    73, "Paṭhamatajjhāna", "First Absorption (1st)",
    vagga=VAGGA_7,
    meta_title="AN 6.73 — First Absorption (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamatajjhānasutta, "
        "naming the five hindrances plus a sixth clause on wisdom as what must be given up to "
        "enter the first absorption. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A named six-item list — the five hindrances plus a wisdom clause — stated "
                 "once as blocking the first absorption and once as its reversal"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The five hindrances (nīvaraṇa) as a standard list recur "
                              "throughout the Chinese Āgamas and Abhidharma literature; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a familiar list from "
                       "elsewhere in the canon, but paired here with a distinct sixth clause on "
                       "wisdom"),
    ],
    why=(
        "AN 6.73 is the first of a paired set closing this chapter, both titled &lsquo;First "
        "Absorption&rsquo; and both naming six things that must be given up to enter the first "
        "jhāna. This discourse's six are the five classic hindrances &mdash; sensual desire, "
        "ill will, dullness and drowsiness, restlessness and remorse, and doubt &mdash; named "
        "together as one list, plus a sixth: the drawbacks of sensual pleasures not yet "
        "&ldquo;truly seen clearly with right wisdom.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "Without giving up the five hindrances and seeing clearly, with right wisdom, the "
            "drawbacks of sensual pleasures, the first absorption cannot be entered; giving up "
            "all six makes it attainable."]),
        ("Five hindrances treated as one list item plus a wisdom clause", [
            "Where AN 6.66 earlier in this chapter split two hindrance-pairs into separate list "
            "items, this discourse names all five hindrances together as a single item, then "
            "adds a sixth, distinct requirement: that the drawbacks of sensual pleasures "
            "actually be seen with wisdom, not merely suppressed or avoided."]),
        ("Suppression is not the same as seeing", [
            "The sixth item's insistence on wisdom (paññāya) implies that giving up the five "
            "hindrances by will or restraint alone, without also seeing their drawbacks "
            "clearly, is not what this discourse means by the phrase &ldquo;giving up.&rdquo; "
            "The first absorption's entry is tied here to insight into why sensual pleasure is "
            "unsatisfying, not merely to its temporary absence."]),
        ("A companion discourse waiting immediately after", [
            "AN 6.74, sharing this discourse's exact title and closing formula, names an "
            "entirely different six things &mdash; three kinds of thought and three kinds of "
            "perception &mdash; as blocking the same first absorption. Two discourses, same "
            "target, same title, and (as with AN 6.65/6.66 earlier in this chapter) different "
            "content, not a restatement."]),
        ("Why the hindrances specifically block the first jhāna", [
            "Each of the five hindrances is described elsewhere in the canon as directly "
            "opposed to one of the first absorption's own factors &mdash; sensual desire and "
            "ill will opposing applied and sustained thought's settling, restlessness and "
            "doubt opposing rapture and bliss, dullness opposing one-pointedness &mdash; though "
            "this discourse itself does not spell out that correspondence explicitly."]),
    ],
    terms=[
        ("kāmacchanda, byāpāda",
         "&ldquo;desire for sensual pleasures, ill will&rdquo; &mdash; the first two of the "
         "five classic hindrances named in this discourse."),
        ("thīnamiddha, uddhaccakukkucca, vicikicchā",
         "&ldquo;dullness and drowsiness, restlessness and remorse, doubt&rdquo; &mdash; the "
         "remaining three hindrances, completing the standard set of five."),
        ("kāmānaṁ ādīnavo paññāya sudiṭṭho",
         "&ldquo;the drawbacks of sensual pleasures truly seen clearly with wisdom&rdquo; "
         "&mdash; the discourse's sixth, distinct requirement, beyond the five hindrances "
         "themselves."),
        ("paṭhamaṁ jhānaṁ",
         "&ldquo;the first absorption&rdquo; &mdash; the attainment both this discourse and AN "
         "6.74 concern, though naming two different sets of six obstacles to it."),
        ("nīvaraṇa",
         "&ldquo;hindrance&rdquo; &mdash; the standard term for the five-item set named "
         "together here as this discourse's first list item."),
    ],
    text_intro=(
        "The discourse in full: the five hindrances plus a sixth clause on wisdom, given up to "
        "enter the first absorption. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Without giving up six qualities"),
        ("p", "&sect;1", "an6.73:1.1-1.5"),
        ("h3", "After giving up six qualities"),
        ("p", "&sect;2", "an6.73:2.1-2.5"),
    ],
    quiz=[
        {"q": "What five items does this discourse name together as its first list item?",
         "opts": [
             "The five faculties",
             "The five classic hindrances: sensual desire, ill will, dullness and drowsiness, "
             "restlessness and remorse, and doubt",
             "The five aggregates",
             "The five precepts"],
         "correct": 1,
         "expl": "Named together as one item, unlike AN 6.66's earlier split treatment of two "
                 "hindrance-pairs."},
        {"q": "What is this discourse's sixth, distinct requirement beyond the five hindrances?",
         "opts": [
             "A specific posture for meditation",
             "That the drawbacks of sensual pleasures be truly seen clearly with right wisdom",
             "Complete silence for seven days",
             "Formal ordination"],
         "correct": 1,
         "expl": "A wisdom clause, not merely the hindrances' suppression."},
        {"q": "According to the guide, what does the sixth item's insistence on wisdom imply?",
         "opts": [
             "That giving up the hindrances by will alone, without seeing their drawbacks "
             "clearly, is not what this discourse means by 'giving up'",
             "That wisdom is unrelated to the five hindrances",
             "That the five hindrances are optional",
             "That wisdom alone, without giving up any hindrance, is sufficient"],
         "correct": 0,
         "expl": "Entry to the first absorption is tied to insight, not merely temporary "
                 "absence of the hindrances."},
        {"q": "What does AN 6.74, immediately following, name as blocking the same first "
              "absorption?",
         "opts": [
             "The identical five hindrances, restated",
             "An entirely different six things — three kinds of thought and three kinds of "
             "perception",
             "Nothing — AN 6.74 concerns a different attainment entirely",
             "The four noble truths"],
         "correct": 1,
         "expl": "Same title, same target attainment, but different content — not a "
                 "restatement."},
        {"q": "What earlier discourse in this chapter is cited as a contrast in how the "
              "hindrances are grouped?",
         "opts": [
             "AN 6.65, which grouped them identically",
             "AN 6.66, which split two hindrance-pairs into separate list items rather than "
             "naming all five together",
             "AN 6.69, which does not mention hindrances",
             "AN 6.70, which lists ten hindrances"],
         "correct": 1,
         "expl": "AN 6.66 treated dullness-drowsiness and restlessness-remorse as separate "
                 "items; this discourse groups all five as one."},
        {"q": "Is a setting stated for AN 6.73?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other list-form discourses."},
        {"q": "What does <em>vicikicchā</em> mean?",
         "opts": ["Ill will", "Doubt", "Restlessness", "Drowsiness"],
         "correct": 1,
         "expl": "The fifth of the five classic hindrances named in this discourse."},
        {"q": "According to the guide, why might the five hindrances specifically block the "
              "first jhāna?",
         "opts": [
             "For reasons entirely unrelated to jhāna's own factors",
             "Each hindrance is described elsewhere in the canon as directly opposed to one of "
             "the first absorption's own factors, though this discourse itself does not spell "
             "out the correspondence",
             "The discourse explicitly explains each pairing in detail",
             "There is no relationship between the hindrances and jhāna"],
         "correct": 1,
         "expl": "A connection drawn from elsewhere in the canon, not stated explicitly in this "
                 "particular discourse."},
        {"q": "What attainment do both AN 6.73 and AN 6.74 concern?",
         "opts": ["The fruit of non-return", "The first absorption (paṭhamaṁ jhānaṁ)", "Arahantship", "Stream-entry"],
         "correct": 1,
         "expl": "A shared target attainment, named identically in both discourses' titles."},
    ],
    marginalia=[
        ("Five hindrances, one item", [
            "sensual desire &middot; ill will",
            "dullness &middot; restlessness",
            "&middot; doubt — grouped as one",
        ]),
        ("A sixth clause: wisdom", [
            "drawbacks of sensual",
            "pleasure truly seen —",
            "not merely suppressed",
        ]),
        ("A paired discourse follows", [
            "AN 6.74: same target,",
            "same title, different",
            "six obstacles named",
        ]),
        ("Cross-references", [
            "AN 6.66 &middot; earlier, hindrance-pairs split into separate items",
            "AN 6.74 &middot; next, this discourse's titled companion",
        ]),
    ],
    further=[
        '<a href="%s/an6.73/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.72.html">AN 6.72 &middot; Strength</a> &mdash; previous, three named '
        "skills in immersion.",
        '<a href="an-6.74.html">AN 6.74 &middot; First Absorption (2nd)</a> &mdash; next, '
        "this discourse's titled companion, closing the chapter.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.74 — Dutiyatajjhānasutta
# --------------------------------------------------------------------------- #
page(
    74, "Dutiyatajjhāna", "First Absorption (2nd)",
    vagga=VAGGA_7,
    meta_title="AN 6.74 — First Absorption (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyatajjhānasutta, "
        "closing the chapter with three kinds of thought and three kinds of perception given "
        "up to enter the first absorption. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A named six-item list — three kinds of thought, three kinds of perception — "
                 "stated once as blocking the first absorption and once as its reversal"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The threefold thought/perception pairing (sensual, malicious, "
                              "cruel) recurs across the Chinese Āgamas' treatment of right "
                              "thought; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and tightly "
                       "patterned, closing the chapter on a compact six-item list"),
    ],
    why=(
        "AN 6.74 closes both this chapter and the pair it forms with AN 6.73: sharing the exact "
        "same title and the same target attainment, the first absorption, it names an entirely "
        "different six things &mdash; three kinds of thought (sensual, malicious, cruel) and "
        "the matching three kinds of perception &mdash; as what must be given up. As with AN "
        "6.65/6.66 earlier in this chapter, a shared title and target here mask genuinely "
        "different content."),
    guide=[
        ("The teaching in one sentence", [
            "Without giving up sensual, malicious, and cruel thoughts, and sensual, malicious, "
            "and cruel perceptions, the first absorption cannot be entered; giving up all six "
            "makes it attainable."]),
        ("Thought and perception, paired three by three", [
            "The list is built from two matched triads rather than six independent items: "
            "kāmavitakka, byāpādavitakka, vihiṁsāvitakka (sensual, malicious, and cruel "
            "thought) and their perceptual counterparts kāmasaññā, byāpādasaññā, "
            "vihiṁsāsaññā. The structure suggests thought and perception are treated here as "
            "two layers of the same three underlying tendencies, not six unrelated items."]),
        ("No wisdom clause, unlike AN 6.73", [
            "Where AN 6.73 closed its list of hindrances with an explicit sixth requirement "
            "&mdash; seeing sensual pleasure's drawbacks with wisdom &mdash; this discourse's "
            "six items are symmetrical throughout, three thoughts and three perceptions, with "
            "no separate wisdom clause appended. The two discourses reach the same target "
            "attainment by different routes, one ending on an explicit insight requirement, "
            "the other on a purely structural threefold-times-two list."]),
        ("Thought as the coarser register, perception as the subtler", [
            "Vitakka (thought) is elsewhere in the canon the more active, verbal register of "
            "mental activity, while saññā (perception) names the more basic act of recognizing "
            "or labeling experience. Naming both registers together implies that giving up "
            "sensual, malicious, and cruel tendencies at the level of active thought is not "
            "sufficient on its own if the same three tendencies persist at the more basic level "
            "of how experience is perceived and labeled."]),
        ("Closing the chapter, and opening onto Arahattavagga", [
            "AN 6.74 is this chapter's tenth and final discourse. The Sixes continue "
            "immediately with Chapter 8, Arahattavagga (AN 6.75&ndash;84), not yet built in "
            "this series; this page's own navigation, following the earlier pattern set at the "
            "close of Mahāvagga, points ahead to the nearest already-published page beyond the "
            "Sixes until that chapter is written."]),
    ],
    terms=[
        ("kāmavitakka, byāpādavitakka, vihiṁsāvitakka",
         "&ldquo;sensual, malicious, and cruel thought&rdquo; &mdash; the first triad in this "
         "discourse's list, the more active, verbal register of mental activity."),
        ("kāmasaññā, byāpādasaññā, vihiṁsāsaññā",
         "&ldquo;sensual, malicious, and cruel perception&rdquo; &mdash; the matching triad, "
         "naming the same three tendencies at the more basic level of recognizing and labeling "
         "experience."),
        ("vitakka",
         "&ldquo;thought,&rdquo; applied thought &mdash; also the first factor of the very "
         "absorption this discourse concerns, though this list's three thoughts are what must "
         "be given up, not that factor itself."),
        ("saññā",
         "&ldquo;perception&rdquo; &mdash; one of the five aggregates, here specified in three "
         "unwholesome forms to be relinquished."),
        ("paṭhamaṁ jhānaṁ",
         "&ldquo;the first absorption&rdquo; &mdash; the same target attainment named in AN "
         "6.73's title, reached here by a structurally different six-item list."),
    ],
    text_intro=(
        "The discourse in full: three kinds of thought and three matching kinds of perception, "
        "given up to enter the first absorption. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Without giving up six qualities"),
        ("p", "&sect;1", "an6.74:1.1-1.4"),
        ("h3", "After giving up six qualities"),
        ("p", "&sect;2", "an6.74:2.1-2.4"),
    ],
    quiz=[
        {"q": "What six things does AN 6.74 name as blocking the first absorption?",
         "opts": [
             "The five hindrances plus a wisdom clause, as in AN 6.73",
             "Three kinds of thought — sensual, malicious, cruel — and three matching kinds of "
             "perception",
             "Lack of faith, conscience, and prudence",
             "The four noble truths"],
         "correct": 1,
         "expl": "An entirely different list from AN 6.73's, despite sharing the same title and "
                 "target attainment."},
        {"q": "How does the guide describe the list's internal structure?",
         "opts": [
             "Six entirely independent, unrelated items",
             "Two matched triads — three kinds of thought and their three matching kinds of "
             "perception — naming the same three underlying tendencies at two levels",
             "A single item repeated six times",
             "A random assortment with no discernible pattern"],
         "correct": 1,
         "expl": "Thought and perception as two layers of the same three tendencies, not six "
                 "unrelated items."},
        {"q": "How does this discourse's list differ from AN 6.73's in structure, according to "
              "the guide?",
         "opts": [
             "They are structured identically, both with a sixth wisdom clause",
             "This discourse's six items are symmetrical throughout — three thoughts, three "
             "perceptions — with no separate wisdom clause, unlike AN 6.73's explicit sixth "
             "requirement",
             "This discourse has no clear structure at all",
             "AN 6.73 has no wisdom clause either"],
         "correct": 1,
         "expl": "Two different routes to the same target attainment."},
        {"q": "What does the guide say vitakka (thought) and saññā (perception) represent, "
              "read together in this list?",
         "opts": [
             "Two unrelated mental faculties with no connection",
             "Two registers of mental activity — thought as more active and verbal, perception "
             "as the more basic act of recognizing and labeling experience",
             "Two names for the exact same thing with no distinction",
             "A distinction found nowhere else in the canon"],
         "correct": 1,
         "expl": "Giving up unwholesome tendencies at the level of thought alone is not "
                 "sufficient if the same tendencies persist at the level of perception."},
        {"q": "What chapter does the Sixes continue with immediately after this one, according "
              "to the guide?",
         "opts": [
             "Chapter 4, Devatāvagga, repeated",
             "Chapter 8, Arahattavagga (AN 6.75–84), not yet built in this series",
             "The Sevens begin immediately",
             "There is no further chapter"],
         "correct": 1,
         "expl": "This chapter's tenth and final discourse, closing Devatāvagga."},
        {"q": "Is a setting stated for AN 6.74?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other list-form discourses."},
        {"q": "What does <em>vihiṁsāvitakka</em> mean?",
         "opts": ["Sensual thought", "Malicious thought", "Cruel thought", "Peaceful thought"],
         "correct": 2,
         "expl": "The third of the three kinds of thought named in this discourse's list."},
        {"q": "What familiar role does vitakka (thought) play elsewhere, beyond this "
              "discourse's list of things to give up?",
         "opts": [
             "It plays no other role anywhere in the canon",
             "It is also the first factor of the first absorption itself, though this "
             "discourse's three thoughts are what must be relinquished, not that factor",
             "It is identical to the fifth hindrance, doubt",
             "It only ever appears in this one discourse"],
         "correct": 1,
         "expl": "A term doing double duty — named as an obstacle here, and as a jhāna factor "
                 "elsewhere."},
        {"q": "What connects AN 6.65/6.66 earlier in this chapter to AN 6.73/6.74 at its close, "
              "according to the guide's overall pattern?",
         "opts": [
             "Nothing — they are unrelated pairs",
             "Both are pairs sharing a title and target while masking genuinely different "
             "content underneath",
             "Both pairs use exactly the same six-item list",
             "Both pairs concern deities specifically"],
         "correct": 1,
         "expl": "A recurring shape across this chapter: shared surface, different underlying "
                 "content, checked term by term rather than assumed."},
    ],
    marginalia=[
        ("Two matched triads", [
            "sensual, malicious,",
            "cruel — as thought,",
            "then again as perception",
        ]),
        ("No wisdom clause here", [
            "unlike AN 6.73 —",
            "purely structural,",
            "thought and perception paired",
        ]),
        ("Closing the chapter", [
            "tenth and final discourse",
            "of Devatāvagga,",
            "Second Fifty's Chapter 7",
        ]),
        ("Cross-references", [
            "AN 6.73 &middot; previous, this discourse's titled companion",
            "AN 6.65/6.66 &middot; earlier, a matching shared-title/different-content pair",
        ]),
    ],
    further=[
        '<a href="%s/an6.74/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.73.html">AN 6.73 &middot; First Absorption (1st)</a> &mdash; previous, '
        "the same target attainment reached by a different six-item list.",
        '<a href="an-6.55.html">AN 6.55 &middot; With Soṇa</a> &mdash; back to the Second '
        "Fifty's opening, for contrast with the chapter now closing.",
    ],
)


# --------------------------------------------------------------------------- #
# Chapter 8 — Arahattavagga (AN 6.75–84), continuing the Second Fifty
# --------------------------------------------------------------------------- #
VAGGA_8 = "<em>Arahattavagga</em> &mdash; the eighth chapter of the Sixes, continuing the Second Fifty"


# --------------------------------------------------------------------------- #
# AN 6.75 — Dukkhasutta
# --------------------------------------------------------------------------- #
page(
    75, "Dukkha", "Suffering",
    vagga=VAGGA_8,
    meta_title="AN 6.75 — Suffering | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dukkhasutta, opening "
        "the Sixes' eighth chapter with the same blocking list as AN 6.74 but a different "
        "target and an explicit positive reversal. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal — the reversal "
                 "naming positive replacements rather than simple negation"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The thought/perception triad of renunciation, good will, and "
                              "harmlessness recurs widely across the Chinese Āgamas' treatment "
                              "of right thought; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "opening a new chapter with a list already met at this chapter's own "
                       "predecessor"),
    ],
    why=(
        "AN 6.75 opens Chapter 8, &lsquo;Perfection,&rsquo; with a list checked word for word "
        "against AN 6.74's closing discourse: the same six unwholesome thoughts and perceptions "
        "&mdash; sensual, malicious, and cruel &mdash; block not the first absorption this time, "
        "but a happy present life and a good rebirth. And where AN 6.74 stated its reversal as "
        "bare negation, this discourse names the positive replacements outright: renunciation, "
        "good will, and harmlessness."),
    guide=[
        ("The teaching in one sentence", [
            "Sensual, malicious, and cruel thoughts and perceptions bring an unhappy life and a "
            "bad rebirth; thoughts and perceptions of renunciation, good will, and harmlessness "
            "bring a happy life and a good rebirth."]),
        ("The same blocking list, a different target", [
            "Checked term by term, this discourse's blocking list &mdash; kāma/byāpāda/vihiṁsā "
            "thought and perception &mdash; is identical to AN 6.74's, which closed the "
            "previous chapter. There, the stake was the first absorption; here, it is ordinary "
            "present-life happiness and future rebirth. The same six items are read as "
            "consequential for two different outcomes across two different chapters."]),
        ("A reversal that names its replacement, not just its absence", [
            "AN 6.74 reversed its list by simply repeating &ldquo;after giving up these six "
            "qualities.&rdquo; This discourse instead names what replaces each unwholesome item: "
            "renunciation (nekkhamma) replacing sensual thought, good will (abyāpāda) replacing "
            "malice, and harmlessness (avihiṁsā) replacing cruelty &mdash; the positive triad "
            "already named as Soṇa's own dedications' foundation earlier in this collection."]),
        ("Stakes stated twice: this life and the next", [
            "Both halves of the discourse name two consequences together &mdash; how a "
            "mendicant lives now (&ldquo;with distress, anguish, and fever&rdquo; or without "
            "them) and what follows at death. The teaching does not treat present unhappiness "
            "and future rebirth as separate questions but as two faces of the same six "
            "qualities."]),
    ],
    terms=[
        ("kāmavitakka, byāpādavitakka, vihiṁsāvitakka",
         "&ldquo;sensual, malicious, and cruel thought&rdquo; &mdash; identical to AN 6.74's "
         "blocking list, here applied to present happiness and rebirth rather than the first "
         "absorption."),
        ("nekkhammavitakka, abyāpādavitakka, avihiṁsāvitakka",
         "&ldquo;thoughts of renunciation, good will, and harmlessness&rdquo; &mdash; the "
         "explicit positive replacements this discourse names, where AN 6.74 gave only "
         "negation."),
        ("sadaraṁ sāghātaṁ sapariḷāhaṁ",
         "&ldquo;with distress, anguish, and fever&rdquo; &mdash; the present-life consequence "
         "of the unwholesome six, stated alongside the future consequence of rebirth."),
        ("kāyassa bhedā paraṁ maraṇā",
         "&ldquo;when the body breaks up, after death&rdquo; &mdash; the standard formula "
         "introducing the discourse's second, future-facing consequence."),
        ("duggati, sugati",
         "&ldquo;bad rebirth, good rebirth&rdquo; &mdash; the two destinations this discourse's "
         "two lists respectively lead toward."),
    ],
    text_intro=(
        "The discourse in full: six qualities leading to present suffering and bad rebirth, and "
        "their six replacements leading to happiness and good rebirth. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six qualities leading to suffering"),
        ("p", "&sect;1", "an6.75:1.1-1.4"),
        ("h3", "Six qualities leading to happiness"),
        ("p", "&sect;2", "an6.75:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does AN 6.75's blocking list compare to AN 6.74's, checked term by term?",
         "opts": [
             "Entirely different content",
             "Identical — the same sensual, malicious, and cruel thoughts and perceptions — but "
             "applied to a different target",
             "Only partially overlapping, sharing three of six items",
             "The two discourses share no relationship at all"],
         "correct": 1,
         "expl": "The same six items read as consequential for two different outcomes across "
                 "two different chapters."},
        {"q": "What does this discourse's blocking list lead to, unlike AN 6.74's?",
         "opts": [
             "The first absorption specifically, as in AN 6.74",
             "An unhappy present life and a bad rebirth, rather than blocking a specific "
             "meditative attainment",
             "Nothing — the list has no stated consequence here",
             "Rebirth as a deity specifically"],
         "correct": 1,
         "expl": "A shift from a specific meditative attainment to ordinary present-life "
                 "happiness and future rebirth."},
        {"q": "How does this discourse's reversal differ from AN 6.74's, according to the "
              "guide?",
         "opts": [
             "It is identical, simply restating 'after giving up these six qualities'",
             "It names explicit positive replacements — renunciation, good will, and "
             "harmlessness — rather than only negating the unwholesome six",
             "It provides no reversal at all",
             "It reverses only three of the six items"],
         "correct": 1,
         "expl": "Positive replacements named outright, not mere absence of the unwholesome "
                 "triad."},
        {"q": "What two consequences does each half of the discourse name together?",
         "opts": [
             "Only a future rebirth, with no present-life consequence",
             "How a mendicant lives now (with or without distress, anguish, and fever) and what "
             "follows at death",
             "Only present-life happiness, with no rebirth consequence",
             "Consequences for other mendicants only, not oneself"],
         "correct": 1,
         "expl": "Present unhappiness/happiness and future rebirth treated as two faces of the "
                 "same six qualities."},
        {"q": "What does this chapter's title, Arahattavagga, translate as?",
         "opts": ["The Chapter on Deities", "The Chapter on Perfection", "The Chapter on Immersion", "The Chapter on Friendship"],
         "correct": 1,
         "expl": "This chapter's own title, matching AN 6.76's discourse title exactly."},
        {"q": "Where else in this collection have renunciation, good will, and harmlessness "
              "appeared as a positive triad, according to the guide?",
         "opts": [
             "Nowhere else in this collection",
             "As part of the foundation of Soṇa's own dedications, earlier in this series",
             "Only in the Tens, not the Sixes",
             "As the five hindrances' direct opposites"],
         "correct": 1,
         "expl": "A positive triad this series has met before, not introduced fresh here."},
        {"q": "Is a setting stated for AN 6.75?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, opening this new chapter."},
        {"q": "What does <em>avihiṁsāvitakka</em> mean?",
         "opts": ["Cruel thought", "Thought of harmlessness", "Malicious thought", "Sensual thought"],
         "correct": 1,
         "expl": "The third of the three positive replacement thoughts named in this "
                 "discourse."},
    ],
    marginalia=[
        ("Same blocking list as 6.74", [
            "sensual, malicious,",
            "cruel — thought and",
            "perception, checked term by term",
        ]),
        ("A different target this time", [
            "not the first absorption —",
            "present happiness",
            "and future rebirth",
        ]),
        ("A named, not merely negated, reversal", [
            "renunciation, good will,",
            "harmlessness — replacing,",
            "not just removing",
        ]),
        ("Cross-references", [
            "AN 6.74 &middot; previous, source of this discourse's blocking list",
        ]),
    ],
    further=[
        '<a href="%s/an6.75/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.74.html">AN 6.74 &middot; First Absorption (2nd)</a> &mdash; previous, '
        "source of this discourse's blocking list, applied there to a different target.",
        '<a href="an-6.76.html">AN 6.76 &middot; Perfection</a> &mdash; next, sharing its '
        "title with AN 6.66 but not its content.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.76 — Arahattasutta
# --------------------------------------------------------------------------- #
page(
    76, "Arahatta", "Perfection",
    vagga=VAGGA_8,
    meta_title="AN 6.76 — Perfection | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for this chapter's own "
        "Arahattasutta, naming six kinds of conceit and its opposites, sharing its title with "
        "AN 6.66 but nothing of its content. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The theme of conceit (māna) in its several forms recurs widely "
                              "across the Chinese Āgamas and Abhidharma literature; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "sharing its exact title with an earlier, unrelated discourse"),
    ],
    why=(
        "This is the second discourse in this series titled &lsquo;Perfection&rsquo; "
        "(Arahattasutta) &mdash; AN 6.66, in the earlier Devatāvagga, was the first. Checked "
        "term by term, the two share nothing beyond a title and the fact that this chapter, "
        "Arahattavagga, is itself named for the same word: this discourse's blocking list is "
        "six varieties of conceit, not AN 6.66's meditative hindrances plus lack of faith."),
    guide=[
        ("The teaching in one sentence", [
            "Without giving up conceit, an inferiority complex, a superiority complex, "
            "overestimation, obstinacy, and groveling, perfection cannot be realized; giving up "
            "all six makes it realizable."]),
        ("A second, unrelated 'Perfection'", [
            "AN 6.66's six blocking items were dullness, drowsiness, restlessness, remorse, "
            "lack of faith, and negligence — meditative hindrances plus one ethical deficit. "
            "This discourse's six are entirely different: varieties of conceit and its inverse "
            "distortions. Sharing a title twice within one collection, as already seen with "
            "this chapter's own name matching AN 6.76's title, is not evidence of shared "
            "content."]),
        ("Six faces of one underlying distortion", [
            "Rather than six unrelated items, the list reads as six ways self-assessment can go "
            "wrong: conceit (māna, thinking oneself better), an inferiority complex (omāna, "
            "thinking oneself worse), a superiority complex (atimāna, an inflated version of "
            "conceit), overestimation (adhimāna, mistaking attainment not yet reached for "
            "attainment achieved), obstinacy (thambha), and groveling (sārambha, or self-abasing "
            "excess). Each names a different way the measuring of oneself against others, or "
            "against one's own attainment, can distort."]),
        ("Why conceit specifically obstructs perfection", [
            "Arahantship is elsewhere in this literature described as the uprooting of the very "
            "conceit &lsquo;I am&rsquo; (asmimāna) at its subtlest level; this discourse's list "
            "of six conceit-variants can be read as naming the coarser and more easily "
            "recognized forms that same underlying tendency takes before it is fully "
            "uprooted."]),
    ],
    terms=[
        ("māna",
         "&ldquo;conceit&rdquo; &mdash; thinking oneself better than another, the first and "
         "namesake item of this discourse's six varieties."),
        ("omāna, atimāna",
         "&ldquo;an inferiority complex, a superiority complex&rdquo; &mdash; thinking oneself "
         "worse, and an inflated form of conceit, the second and third items."),
        ("adhimāna",
         "&ldquo;overestimation&rdquo; &mdash; mistaking an attainment not yet reached for one "
         "already achieved, the fourth item."),
        ("thambha, sārambha",
         "&ldquo;obstinacy, groveling&rdquo; &mdash; the fifth and sixth items, closing the "
         "list."),
        ("asmimāna",
         "&ldquo;the conceit &lsquo;I am&rsquo;&rdquo; &mdash; the subtlest form of conceit, "
         "described elsewhere as fully uprooted only at arahantship itself."),
    ],
    text_intro=(
        "The discourse in full: six varieties of conceit that block perfection, and their six "
        "reversals. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that block perfection"),
        ("p", "&sect;1", "an6.76:1.1-1.4"),
        ("h3", "Six things that enable it"),
        ("p", "&sect;2", "an6.76:2.1-2.4"),
    ],
    quiz=[
        {"q": "What earlier discourse in this series shares this discourse's exact title, "
              "'Perfection' (Arahattasutta)?",
         "opts": ["AN 6.31", "AN 6.66, in the earlier Devatāvagga", "AN 6.55", "There is no earlier discourse with this title"],
         "correct": 1,
         "expl": "A second, unrelated discourse of the same name within this collection."},
        {"q": "How much content is shared between AN 6.66 and AN 6.76, checked term by term?",
         "opts": [
             "All six blocking items are identical",
             "Nothing beyond the shared title — AN 6.66 named meditative hindrances plus lack "
             "of faith, while this discourse names six varieties of conceit",
             "Half of the six items overlap",
             "Only the reversal half is shared"],
         "correct": 1,
         "expl": "A title shared twice is not evidence of shared content."},
        {"q": "What six things does this discourse actually name as blocking perfection?",
         "opts": [
             "Dullness, drowsiness, restlessness, remorse, lack of faith, negligence",
             "Conceit, an inferiority complex, a superiority complex, overestimation, "
             "obstinacy, and groveling",
             "The five hindrances plus doubt",
             "Lack of faith, conscience, prudence, laziness, unmindfulness, witlessness"],
         "correct": 1,
         "expl": "Six varieties of conceit and its distortions, unrelated to AN 6.66's list."},
        {"q": "According to the guide, what unifies these six items?",
         "opts": [
             "They are six unrelated ethical faults with no common thread",
             "They read as six ways self-assessment against oneself or others can go wrong, "
             "from conceit to overestimation to obstinacy",
             "They are six stages of a single meditation technique",
             "They apply only to lay followers"],
         "correct": 1,
         "expl": "Six faces of one underlying distortion in how one measures oneself."},
        {"q": "What does <em>adhimāna</em> mean?",
         "opts": [
             "Thinking oneself worse than others",
             "Mistaking an attainment not yet reached for one already achieved",
             "Complete freedom from all conceit",
             "An inflated form of ordinary conceit"],
         "correct": 1,
         "expl": "The fourth item, a specific and easily overlooked form of overestimation."},
        {"q": "How does the guide connect this discourse's list to arahantship itself?",
         "opts": [
             "It sees no connection at all",
             "Arahantship is described elsewhere as uprooting the conceit 'I am' (asmimāna) at "
             "its subtlest level, and this list can be read as naming its coarser, earlier "
             "forms",
             "The list describes something unrelated to conceit entirely",
             "Only lay followers experience any of these six items"],
         "correct": 1,
         "expl": "Coarser, more easily recognized forms of the same tendency finally uprooted "
                 "at full awakening."},
        {"q": "Is a setting stated for AN 6.76?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, matching AN 6.75 immediately before it."},
        {"q": "What does <em>thambha</em> mean?",
         "opts": ["Groveling", "Obstinacy", "Overestimation", "An inferiority complex"],
         "correct": 1,
         "expl": "The fifth item on this discourse's six-item list."},
    ],
    marginalia=[
        ("Six varieties of conceit", [
            "conceit &middot; inferiority",
            "&middot; superiority complex",
            "overestimation &middot; obstinacy &middot; groveling",
        ]),
        ("A shared title, no shared content", [
            "AN 6.66 and AN 6.76",
            "both 'Perfection' —",
            "entirely different lists",
        ]),
        ("Coarser forms of asmimāna", [
            "the conceit 'I am',",
            "fully uprooted only",
            "at arahantship itself",
        ]),
        ("Cross-references", [
            "AN 6.66 &middot; the earlier, unrelated discourse of the same title",
            "AN 6.75 &middot; previous, opening this chapter",
        ]),
    ],
    further=[
        '<a href="%s/an6.76/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.66.html">AN 6.66 &middot; Perfection</a> &mdash; the earlier, unrelated '
        "discourse of the same title.",
        '<a href="an-6.77.html">AN 6.77 &middot; Superhuman States</a> &mdash; next, a '
        "different six-item list on the same chapter's theme.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.77 — Uttarimanussadhammasutta
# --------------------------------------------------------------------------- #
page(
    77, "Uttarimanussadhamma", "Superhuman States",
    vagga=VAGGA_8,
    meta_title="AN 6.77 — Superhuman States | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Uttarimanussadhammasutta, naming six conduct-level obstacles to a superhuman "
        "distinction in knowledge and vision. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of unguarded senses and excess in eating with "
                              "failure to progress recurs widely across the Chinese Āgamas' "
                              "monastic-conduct material; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "returning to concrete conduct after two discourses on inward states"),
    ],
    why=(
        "After AN 6.75's thoughts and AN 6.76's conceit, this discourse returns to the register "
        "of concrete daily conduct: lack of mindfulness and situational awareness, not "
        "guarding the sense doors, eating too much, fawning, and flattery block a "
        "&ldquo;superhuman distinction in knowledge and vision worthy of the noble ones&rdquo; "
        "&mdash; the discourse's own term for realizations beyond the ordinary human range."),
    guide=[
        ("The teaching in one sentence", [
            "Without giving up lack of mindfulness and situational awareness, unguarded senses, "
            "eating too much, fawning, and flattery, a superhuman distinction in knowledge and "
            "vision cannot be realized; giving up all these makes it realizable."]),
        ("Familiar items from elsewhere in this series", [
            "Not guarding the sense doors and eating without moderation already appeared "
            "together at AN 6.31's list of a trainee's causes of decline, in the earlier First "
            "Fifty. Their reappearance here, applied to a different and more elevated target, "
            "shows the same conduct-level failures treated as consequential across more than "
            "one register of attainment."]),
        ("Two items naming insincerity specifically", [
            "Fawning (lapanā) and flattery (unnaḷā, sometimes rendered differently across "
            "translations) close the list with something distinct from the other four: not a "
            "failure of restraint but a failure of honesty in how one presents oneself to "
            "others, suggesting the superhuman distinction this discourse concerns is blocked "
            "as much by self-presentation as by sense-discipline."]),
        ("'Superhuman' as this discourse's own term, not an overclaim", [
            "Uttarimanussadhamma, &ldquo;superhuman state,&rdquo; is the discourse's own "
            "technical term for meditative and realizational attainments beyond the ordinary "
            "human range — the same term whose false claim is treated with particular gravity "
            "elsewhere in the monastic code, underscoring how seriously this list's stakes are "
            "meant to be taken."]),
    ],
    terms=[
        ("uttarimanussadhamma",
         "&ldquo;superhuman state&rdquo; &mdash; the discourse's own term for attainments "
         "beyond the ordinary human range, whose false claim carries particular gravity "
         "elsewhere in the monastic code."),
        ("satisampajañña",
         "&ldquo;mindfulness and situational awareness&rdquo; &mdash; the first item, whose "
         "lack opens this discourse's list."),
        ("indriyesu aguttadvāratā, bhojane amattaññutā",
         "&ldquo;not guarding the sense doors, eating without moderation&rdquo; &mdash; two "
         "items already met at AN 6.31 in the earlier First Fifty, applied here to a different "
         "target."),
        ("lapanā",
         "&ldquo;fawning&rdquo; &mdash; one of two closing items naming a failure of honest "
         "self-presentation rather than restraint."),
        ("ariyānaṁ ñāṇadassanavisesa",
         "&ldquo;a distinction in knowledge and vision worthy of the noble ones&rdquo; &mdash; "
         "the full formula this discourse's six items are said to block."),
    ],
    text_intro=(
        "The discourse in full: six conduct-level obstacles to a superhuman distinction in "
        "knowledge and vision, and their reversal. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that block superhuman distinction"),
        ("p", "&sect;1", "an6.77:1.1-1.4"),
        ("h3", "Six things that enable it"),
        ("p", "&sect;2", "an6.77:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does 'uttarimanussadhamma' mean, and what is notable about the term?",
         "opts": [
             "'Ordinary human state' — a term of no particular gravity",
             "'Superhuman state' — the discourse's own term for attainments beyond the "
             "ordinary human range, whose false claim carries particular gravity elsewhere in "
             "the monastic code",
             "A term applying only to deities, never to mendicants",
             "A term meaning simply 'good conduct'"],
         "correct": 1,
         "expl": "This discourse's own technical term, not an informal description."},
        {"q": "Which two items on this discourse's list already appeared together at AN 6.31?",
         "opts": [
             "Lack of mindfulness and fawning",
             "Not guarding the sense doors, and eating without moderation",
             "Flattery and situational awareness",
             "None of the six items appeared earlier in this series"],
         "correct": 1,
         "expl": "Met earlier at AN 6.31's list of a trainee's causes of decline, in the First "
                 "Fifty, now applied to a different and more elevated target."},
        {"q": "What do the two closing items, fawning and flattery, name that the other four "
              "do not, according to the guide?",
         "opts": [
             "Nothing distinct — all six are the same kind of failure",
             "A failure of honest self-presentation to others, rather than a failure of "
             "restraint",
             "A failure specific to lay followers only",
             "A form of physical illness"],
         "correct": 1,
         "expl": "Insincerity in self-presentation, distinct from sense-discipline or "
                 "moderation."},
        {"q": "What attainment does this discourse's six-item list block?",
         "opts": [
             "The first absorption specifically",
             "A superhuman distinction in knowledge and vision worthy of the noble ones",
             "Ordinary ethical conduct",
             "Rebirth as a human being"],
         "correct": 1,
         "expl": "The discourse's own stated stakes, named explicitly in both halves."},
        {"q": "Is a setting stated for AN 6.77?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other formulaic discourses."},
        {"q": "What does <em>satisampajañña</em> mean?",
         "opts": ["Fawning and flattery", "Mindfulness and situational awareness", "Eating in moderation", "Guarding the sense doors"],
         "correct": 1,
         "expl": "The first item, whose lack opens this discourse's list."},
        {"q": "How does the guide characterize this discourse's register compared to AN 6.75 "
              "and 6.76?",
         "opts": [
             "Identical in register — all three concern inward mental states only",
             "A return to concrete daily conduct, after AN 6.75's thoughts and AN 6.76's "
             "conceit",
             "This discourse concerns only doctrinal categories, unlike the two before it",
             "There is no meaningful difference in register between the three"],
         "correct": 1,
         "expl": "Sense-discipline, eating, and honest self-presentation — concrete conduct, "
                 "not inward states."},
        {"q": "What is the discourse's overall structure?",
         "opts": [
             "A narrated story",
             "Two matched six-item lists, blockage and reversal, with no further elaboration",
             "A dialogue with a deity",
             "A set of verses only"],
         "correct": 1,
         "expl": "The same compressed shape as this chapter's other formulaic discourses."},
    ],
    marginalia=[
        ("Six conduct-level obstacles", [
            "no mindfulness &middot; unguarded",
            "senses &middot; overeating",
            "&middot; fawning &middot; flattery",
        ]),
        ("Two items recur from AN 6.31", [
            "unguarded senses,",
            "immoderate eating —",
            "same conduct, higher stakes",
        ]),
        ("A term of particular gravity", [
            "uttarimanussadhamma —",
            "false claim treated gravely",
            "elsewhere in the code",
        ]),
        ("Cross-references", [
            "AN 6.31 &middot; earlier, source of two shared items, First Fifty",
            "AN 6.76 &middot; previous, six varieties of conceit",
        ]),
    ],
    further=[
        '<a href="%s/an6.77/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.76.html">AN 6.76 &middot; Perfection</a> &mdash; previous, six '
        "varieties of conceit.",
        '<a href="an-6.78.html">AN 6.78 &middot; Joy and Happiness</a> &mdash; next, a single '
        "six-item list with no separate reversal half.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.78 — Sukhasomanassasutta
# --------------------------------------------------------------------------- #
page(
    78, "Sukhasomanassa", "Joy and Happiness",
    vagga=VAGGA_8,
    meta_title="AN 6.78 — Joy and Happiness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Sukhasomanassasutta, naming six things a mendicant delights in that bring joy and lay "
        "the groundwork for ending the defilements. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single six-item list stated only positively, with no paired negative half "
                 "— the first such discourse in this chapter"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of joy in the teaching with laying the groundwork "
                              "for liberation recurs widely across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and entirely "
                       "positive, the first one-sided list in this chapter"),
    ],
    why=(
        "Every discourse in this chapter so far has paired a blocking list with its reversal. "
        "AN 6.78 breaks that pattern: it states only what a mendicant who enjoys six things "
        "&mdash; the teaching, meditation, giving up, seclusion, kindness, and "
        "non-proliferation &mdash; experiences, with no corresponding list of what blocks joy "
        "stated separately."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who enjoys the teaching, meditation, giving up, seclusion, kindness, "
            "and non-proliferation is full of joy and happiness in this very life, having laid "
            "the groundwork for ending the defilements."]),
        ("The chapter's first one-sided list", [
            "Every discourse from AN 6.75 through 6.77 named a blocking six paired with an "
            "enabling six. This discourse states only the positive side, with no explicit "
            "negative list given for contrast — the implicit opposite (not enjoying these six "
            "things) is left for the reader to infer rather than spelled out."]),
        ("Six objects of delight, not six practices", [
            "The list names what a mendicant enjoys (abhirati) rather than six practices to be "
            "performed: the teaching (dhamma), meditation (bhāvanā), giving up (pahāna), "
            "seclusion (paviveka), kindness (abyāpajjha, sometimes rendered "
            "&ldquo;non-affliction&rdquo;), and non-proliferation (nippapañca) &mdash; the "
            "last of these the same term whose relishing was the decisive item at AN 6.14 and "
            "6.15, here inverted from a trap to a source of joy."]),
        ("Present joy as groundwork, not proof, of liberation", [
            "The discourse is careful to state its outcome in two parts: joy and happiness "
            "&ldquo;in this very life,&rdquo; and separately, having &ldquo;laid the groundwork "
            "for ending the defilements&rdquo; &mdash; a foundation, not the ending itself. The "
            "six delights bring a felt happiness now and a condition favorable to further "
            "progress, without the discourse claiming that progress has already been "
            "completed."]),
    ],
    terms=[
        ("abhirati",
         "&ldquo;enjoyment, delight&rdquo; &mdash; the discourse's own framing for its six-item "
         "list, delight rather than duty."),
        ("nippapañca",
         "&ldquo;non-proliferation&rdquo; &mdash; the sixth and closing item, the same term "
         "whose relishing (the opposite orientation) was the decisive trap named at AN 6.14 "
         "and 6.15 earlier in this series."),
        ("pahāna, paviveka",
         "&ldquo;giving up, seclusion&rdquo; &mdash; the third and fourth items, echoing "
         "seclusion's role as a precondition already met in AN 6.68's chain earlier in this "
         "collection."),
        ("abyāpajjha",
         "&ldquo;kindness,&rdquo; non-affliction &mdash; the fifth item, echoing the same term "
         "among Soṇa's own six dedications at AN 6.55."),
        ("āsavakkhayāya ca padhāniyaṅgaṁ",
         "&ldquo;laid the groundwork for ending the defilements&rdquo; &mdash; the discourse's "
         "second, distinct outcome, a foundation rather than a claim of completed liberation."),
    ],
    text_intro=(
        "The discourse in full: six things a mendicant delights in, bringing joy and laying "
        "the groundwork for ending the defilements. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things a mendicant delights in"),
        ("p", "&sect;1", "an6.78:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does AN 6.78's structure break the pattern set by AN 6.75 through 6.77?",
         "opts": [
             "It follows the identical blockage/reversal pattern",
             "It states only a positive, one-sided list, with no explicit paired negative list "
             "of what blocks joy",
             "It contains no list at all",
             "It reverses the usual order, stating the reversal first"],
         "correct": 1,
         "expl": "The chapter's first discourse without a stated negative half."},
        {"q": "What six things does a mendicant enjoy, according to this discourse?",
         "opts": [
             "Faith, energy, mindfulness, immersion, wisdom, and liberation",
             "The teaching, meditation, giving up, seclusion, kindness, and non-proliferation",
             "Food, sleep, company, talk, work, and possessions",
             "The five hindrances and their absence"],
         "correct": 1,
         "expl": "Six objects of delight, not six practices to perform."},
        {"q": "Where else in this series has 'non-proliferation' (papañca/nippapañca) appeared, "
              "and how does its role differ here?",
         "opts": [
             "Nowhere else in this series",
             "At AN 6.14 and 6.15, where relishing proliferation was the decisive trap; here "
             "the same term appears inverted, as a source of joy rather than a danger",
             "Only as a synonym for the five hindrances",
             "As a term unrelated to proliferation"],
         "correct": 1,
         "expl": "The same term's opposite orientation, from trap to delight."},
        {"q": "What two distinct outcomes does the discourse name?",
         "opts": [
             "Only future rebirth, with no present-life consequence",
             "Joy and happiness in this very life, and separately, having laid the groundwork "
             "for ending the defilements",
             "Only the complete ending of defilements",
             "Wealth and social status"],
         "correct": 1,
         "expl": "A felt present happiness and a foundation for further progress, not a claim "
                 "of completed liberation."},
        {"q": "Is a setting stated for AN 6.78?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other discourses."},
        {"q": "What does <em>abyāpajjha</em> mean, and where else has it appeared in this "
              "series?",
         "opts": [
             "'Cruelty' — appearing nowhere else",
             "'Kindness,' non-affliction — echoing one of Soṇa's own six dedications at AN 6.55",
             "'Wisdom' — appearing at AN 6.31",
             "A term unique to this discourse"],
         "correct": 1,
         "expl": "A term this series has already met, applied here as one of six objects of "
                 "delight."},
        {"q": "What is 'the groundwork for ending the defilements,' according to the guide?",
         "opts": [
             "A claim that the defilements have already been fully ended",
             "A foundation favorable to further progress, distinct from the ending itself",
             "An unrelated, separate attainment",
             "A synonym for the first absorption"],
         "correct": 1,
         "expl": "Careful phrasing distinguishing groundwork laid from completion claimed."},
    ],
    marginalia=[
        ("Six objects of delight", [
            "the teaching &middot; meditation",
            "giving up &middot; seclusion",
            "kindness &middot; non-proliferation",
        ]),
        ("The chapter's first one-sided list", [
            "no paired negative —",
            "only what a mendicant",
            "enjoys, stated once",
        ]),
        ("Nippapañca, inverted", [
            "at AN 6.14/6.15, a trap —",
            "here, delighted in",
            "as a source of joy",
        ]),
        ("Cross-references", [
            "AN 6.14/6.15 &middot; earlier, where the same term named a danger, not a delight",
        ]),
    ],
    further=[
        '<a href="%s/an6.78/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.77.html">AN 6.77 &middot; Superhuman States</a> &mdash; previous, a '
        "paired blockage/reversal list, unlike this discourse's single positive one.",
        '<a href="an-6.79.html">AN 6.79 &middot; Achievement</a> &mdash; next, a return to '
        "the paired blockage/reversal pattern.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.79 — Adhigamasutta
# --------------------------------------------------------------------------- #
page(
    79, "Adhigama", "Achievement",
    vagga=VAGGA_8,
    meta_title="AN 6.79 — Achievement | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Adhigamasutta, "
        "naming three skills plus three practical habits that determine whether skillful "
        "qualities can be acquired or increased. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, returning to this "
                 "chapter's paired pattern after AN 6.78's single positive list"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The theme of skill in progress and regress as conditions for "
                              "further development recurs widely across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; abstract in its first half, "
                       "naming categories of skill rather than concrete practices"),
    ],
    why=(
        "AN 6.79 returns to this chapter's paired blockage/reversal pattern after AN 6.78's "
        "single list, and shares a structural family resemblance with AN 6.71 earlier in this "
        "collection: a mendicant's ability to &ldquo;acquire more skillful qualities or "
        "increase the skillful qualities they've already acquired&rdquo; depends on three "
        "kinds of skill &mdash; in progress, regress, and means &mdash; joined to three "
        "further habits of enthusiasm, protection, and persistence."),
    guide=[
        ("The teaching in one sentence", [
            "Without skill in progress, regress, and means, and without generating enthusiasm, "
            "protecting what's achieved, and persisting in the task, a mendicant cannot acquire "
            "or increase skillful qualities; possessing all six makes that acquisition and "
            "increase possible."]),
        ("Three skills of discernment, three habits of practice", [
            "The list splits cleanly into two halves of three: knowing what constitutes "
            "progress (āyakusala), regress (apāyakusala), and the means to develop further "
            "(upāyakusala) is a matter of discernment, while generating enthusiasm, protecting "
            "what has been achieved, and persisting in the task is a matter of sustained "
            "effort. Neither half alone is stated as sufficient."]),
        ("A structural cousin of AN 6.71", [
            "This discourse's shape closely resembles AN 6.71's fourfold-discernment-plus-"
            "careful-practice structure earlier in this chapter's predecessor, though the "
            "specific categories named differ: AN 6.71 spoke of what worsens, steadies, "
            "distinguishes, and penetrates a given quality, while this discourse speaks of "
            "progress, regress, and means toward acquiring skillful qualities generally."]),
        ("Protecting, not only acquiring", [
            "The discourse's third practical habit &mdash; protecting skillful qualities "
            "already achieved (anurakkhaṇā) &mdash; treats what has already been gained as "
            "something that can still be lost without ongoing care, not as a permanent "
            "possession once attained."]),
    ],
    terms=[
        ("āyakusala, apāyakusala, upāyakusala",
         "&ldquo;skilled in progress, skilled in regress, skilled in means&rdquo; &mdash; the "
         "first three, discernment-based items."),
        ("chandaṁ janeti",
         "&ldquo;generates enthusiasm&rdquo; &mdash; the fourth item, aimed at skillful "
         "qualities not yet achieved."),
        ("anurakkhaṇā",
         "&ldquo;protection&rdquo; &mdash; the fifth item, guarding skillful qualities already "
         "achieved rather than assuming them secure."),
        ("sātaccakiriyā",
         "&ldquo;persisting in the task&rdquo; &mdash; the sixth and closing item."),
        ("kusala dhamma",
         "&ldquo;skillful qualities&rdquo; &mdash; the discourse's own general term for what is "
         "to be acquired and increased, left unspecified as to particular content."),
    ],
    text_intro=(
        "The discourse in full: three skills of discernment and three habits of practice that "
        "determine whether skillful qualities can be acquired or increased. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that prevent acquiring skillful qualities"),
        ("p", "&sect;1", "an6.79:1.1-1.4"),
        ("h3", "Six things that enable it"),
        ("p", "&sect;2", "an6.79:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse's list divide into two halves, according to the guide?",
         "opts": [
             "Six identical items, not divisible into halves",
             "Three items of discernment (progress, regress, means) and three items of "
             "sustained practice (enthusiasm, protection, persistence)",
             "Three ethical items and three doctrinal items",
             "The list has no internal division"],
         "correct": 1,
         "expl": "Discernment alone, or effort alone, is not stated as sufficient — both "
                 "halves are required."},
        {"q": "What does this discourse's list determine, according to its opening line?",
         "opts": [
             "Whether a mendicant can enter the first absorption",
             "Whether a mendicant can acquire more skillful qualities, or increase the "
             "skillful qualities already acquired",
             "Whether a mendicant is reborn well",
             "Whether a mendicant can teach others"],
         "correct": 1,
         "expl": "The discourse's own stated stakes, general rather than tied to one specific "
                 "attainment."},
        {"q": "What earlier discourse does this one structurally resemble, according to the "
              "guide?",
         "opts": [
             "AN 6.55, With Soṇa",
             "AN 6.71, Capable of Realizing — though the specific categories named differ "
             "between the two",
             "AN 6.69, A God",
             "AN 6.31, A Trainee"],
         "correct": 1,
         "expl": "A shared discernment-plus-practice structure, applied to different specific "
                 "categories."},
        {"q": "What does 'protecting' skillful qualities already achieved imply, according to "
              "the guide?",
         "opts": [
             "That once achieved, skillful qualities can never be lost",
             "That what has already been gained can still be lost without ongoing care, not a "
             "permanent possession once attained",
             "That protection is unnecessary once enthusiasm is present",
             "That only newly acquired qualities need protecting"],
         "correct": 1,
         "expl": "Ongoing care treated as necessary, not a one-time achievement."},
        {"q": "Is a setting stated for AN 6.79?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other formulaic discourses."},
        {"q": "What does <em>upāyakusala</em> mean?",
         "opts": ["Skilled in regress", "Skilled in means", "Skilled in progress", "Skilled in teaching"],
         "correct": 1,
         "expl": "The third of the three discernment-based items."},
        {"q": "How does this discourse's structure compare to AN 6.78, immediately before it?",
         "opts": [
             "Identical — both are one-sided positive lists",
             "A return to the paired blockage/reversal pattern, after AN 6.78's single "
             "positive list broke from it",
             "This discourse also has no reversal half",
             "There is no relationship between the two"],
         "correct": 1,
         "expl": "The chapter's default paired pattern resumes here."},
    ],
    marginalia=[
        ("Three skills, three habits", [
            "progress &middot; regress",
            "&middot; means — plus enthusiasm,",
            "protection, persistence",
        ]),
        ("A structural cousin", [
            "of AN 6.71's",
            "discernment-plus-practice",
            "shape, different categories",
        ]),
        ("Gains still need guarding", [
            "protection named",
            "as its own item —",
            "nothing is permanent by default",
        ]),
        ("Cross-references", [
            "AN 6.71 &middot; earlier, the structurally similar discourse",
            "AN 6.78 &middot; previous, the chapter's one exception to this pattern",
        ]),
    ],
    further=[
        '<a href="%s/an6.79/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.78.html">AN 6.78 &middot; Joy and Happiness</a> &mdash; previous, the '
        "chapter's one one-sided list.",
        '<a href="an-6.80.html">AN 6.80 &middot; Greatness</a> &mdash; next, another '
        "single-list discourse, positive throughout.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.80 — Mahantattasutta
# --------------------------------------------------------------------------- #
page(
    80, "Mahantatta", "Greatness",
    vagga=VAGGA_8,
    meta_title="AN 6.80 — Greatness | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Mahantattasutta, "
        "naming six qualities of energetic engagement that soon bring great and abundant good "
        "qualities. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "A single six-item list stated only positively, like AN 6.78, with no paired "
                 "negative half"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The imagery of being 'full of light' as a description of "
                              "energetic practice recurs widely across the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and entirely "
                       "positive, this chapter's second one-sided list"),
    ],
    why=(
        "AN 6.80 is this chapter's second one-sided list, after AN 6.78: a mendicant who is "
        "&ldquo;full of light, full of practice, full of inspiration, and full of eagerness,&rdquo; "
        "who does not slack off in developing skillful qualities, and who &ldquo;reaches "
        "further,&rdquo; soon acquires great and abundant good qualities &mdash; stated once, "
        "with no separate negative list given."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant full of light, practice, inspiration, and eagerness, who does not "
            "slack off in developing skillful qualities and reaches further, soon acquires "
            "great and abundant good qualities."]),
        ("Four qualities of fullness, then two of momentum", [
            "The list's first four items &mdash; full of light (obhāsabahula), practice, "
            "inspiration, and eagerness &mdash; describe an inward state of energetic "
            "readiness, while the closing two &mdash; not slacking off, and reaching further "
            "&mdash; describe sustained forward motion. The list moves from inner condition to "
            "outward momentum across its six items."]),
        ("'Full of light' as figurative energy, not literal vision", [
            "Obhāsabahula, &ldquo;full of light,&rdquo; is read in this tradition as figurative "
            "&mdash; a mind bright with energetic clarity &mdash; rather than a claim of "
            "literally perceiving light, distinguishing it from the specific visual phenomena "
            "described in some meditation manuals as arising during concentrated practice."]),
        ("The chapter's second exception, not a coincidence", [
            "That both of this chapter's one-sided discourses, AN 6.78 and AN 6.80, describe "
            "positive inward states &mdash; joy and delight in one case, energetic brightness "
            "in the other &mdash; rather than conduct to be corrected, suggests the paired "
            "blockage/reversal form is reserved in this chapter for items that can plausibly go "
            "wrong, while purely energetic or joyful qualities are simply described without a "
            "stated opposite."]),
    ],
    terms=[
        ("mahantatta",
         "&ldquo;greatness&rdquo; &mdash; the discourse's own title, the outcome its six "
         "qualities are said to soon produce."),
        ("obhāsabahula",
         "&ldquo;full of light&rdquo; &mdash; the first item, read figuratively as energetic "
         "mental clarity rather than a literal visual phenomenon."),
        ("ussoḷhībahula",
         "&ldquo;full of practice,&rdquo; full of exertion &mdash; the second item, naming "
         "sustained effort directly."),
        ("uttari appaṭivāṇī",
         "&ldquo;they reach further&rdquo; &mdash; the sixth and closing item, naming outward "
         "momentum rather than an inward state."),
        ("kusala dhamma",
         "&ldquo;skillful qualities&rdquo; &mdash; the same general term used at AN 6.79, here "
         "described as developed without slacking off rather than merely acquired."),
    ],
    text_intro=(
        "The discourse in full: six qualities of energetic engagement that soon bring great "
        "and abundant good qualities. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six qualities that bring greatness"),
        ("p", "&sect;1", "an6.80:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does AN 6.80's structure compare to AN 6.78's, and to the rest of this "
              "chapter?",
         "opts": [
             "It follows the usual paired blockage/reversal pattern",
             "Like AN 6.78, it is a one-sided positive list with no paired negative half — "
             "this chapter's second such exception",
             "It has no list at all",
             "It is identical in content to AN 6.78"],
         "correct": 1,
         "expl": "The chapter's second one-sided discourse, after AN 6.78."},
        {"q": "What does <em>obhāsabahula</em> mean, and how is it read according to the "
              "guide?",
         "opts": [
             "'Full of darkness' — a description of ignorance to be overcome",
             "'Full of light' — read figuratively as energetic mental clarity, not a literal "
             "visual phenomenon",
             "A term with no clear meaning",
             "'Full of doubt'"],
         "correct": 1,
         "expl": "Figurative brightness of mind, distinguished from literal visual experiences "
                 "described elsewhere in meditation manuals."},
        {"q": "How does the guide describe the list's internal movement across its six items?",
         "opts": [
             "No discernible movement — six unrelated items",
             "From an inward state of energetic readiness (the first four items) to sustained "
             "outward momentum (the closing two)",
             "From outward momentum to inward stillness",
             "The items are presented in random order with no pattern"],
         "correct": 1,
         "expl": "Inner condition, then forward motion — a directional structure across the "
                 "list."},
        {"q": "What does the guide suggest connects AN 6.78 and AN 6.80 as this chapter's two "
              "one-sided discourses?",
         "opts": [
             "Nothing — the two are unrelated coincidences",
             "Both describe positive inward states rather than conduct to be corrected, "
             "suggesting the paired form is reserved for items that can plausibly go wrong",
             "Both concern only deities",
             "Both are the chapter's longest discourses"],
         "correct": 1,
         "expl": "A plausible pattern: purely joyful or energetic qualities described without a "
                 "stated opposite."},
        {"q": "Is a setting stated for AN 6.80?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other discourses."},
        {"q": "What does the discourse's sixth and final item, 'they reach further,' describe?",
         "opts": [
             "An inward state of energetic readiness",
             "Outward momentum, sustained forward progress rather than an inner condition",
             "A specific meditative attainment",
             "A form of physical travel"],
         "correct": 1,
         "expl": "The closing item shifts from inward fullness to outward, sustained motion."},
        {"q": "What outcome does this discourse's six-item list produce?",
         "opts": [
             "Only the first absorption",
             "Great and abundant good qualities, acquired soon",
             "Rebirth as a deity specifically",
             "Freedom from all future teaching duties"],
         "correct": 1,
         "expl": "The discourse's own stated and immediate outcome."},
    ],
    marginalia=[
        ("Four qualities, then momentum", [
            "full of light, practice,",
            "inspiration, eagerness —",
            "then: no slacking, reaching further",
        ]),
        ("Light as figurative clarity", [
            "not a literal vision —",
            "a mind bright with",
            "energetic readiness",
        ]),
        ("This chapter's second exception", [
            "AN 6.78 and 6.80:",
            "both positive states,",
            "neither paired with a reversal",
        ]),
        ("Cross-references", [
            "AN 6.78 &middot; earlier, this chapter's other one-sided list",
            "AN 6.79 &middot; previous, a return to the paired pattern",
        ]),
    ],
    further=[
        '<a href="%s/an6.80/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.79.html">AN 6.79 &middot; Achievement</a> &mdash; previous, a paired '
        "blockage/reversal discourse.",
        '<a href="an-6.81.html">AN 6.81 &middot; Hell (1st)</a> &mdash; next, the first of a '
        "titled pair on hell and heaven.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.81 — Paṭhamanirayasutta
# --------------------------------------------------------------------------- #
page(
    81, "Paṭhamaniraya", "Hell (1st)",
    vagga=VAGGA_8,
    meta_title="AN 6.81 — Hell (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Paṭhamanirayasutta, "
        "naming four acts plus corrupt wishes and wrong view as what delivers someone to hell "
        "or heaven. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, opening a titled "
                 "pair with AN 6.82"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The four acts of killing, stealing, sexual misconduct, and "
                              "lying as a fixed ethical core recur throughout the Chinese "
                              "Āgamas' precept material; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and direct, naming "
                       "familiar precept-breaking acts rather than abstract categories"),
    ],
    why=(
        "AN 6.81 shifts register again: rather than meditative attainment or the acquisition "
        "of skillful qualities, its stakes are stated as bluntly as this collection ever states "
        "them &mdash; placed in hell, or in heaven, &ldquo;as if delivered there.&rdquo; Four "
        "familiar acts (killing, stealing, sexual misconduct, lying) are joined by two further "
        "items, corrupt wishes and wrong view, closing the list on an internal disposition "
        "rather than a further outward act."),
    guide=[
        ("The teaching in one sentence", [
            "Killing, stealing, sexual misconduct, and lying, joined by corrupt wishes and "
            "wrong view, places someone in hell; abstaining from the four acts, joined by few "
            "desires and right view, places someone in heaven."]),
        ("Four acts, but not the standard five precepts", [
            "The list's first four items match four of the five lay precepts, but the fifth "
            "precept &mdash; abstaining from intoxicants &mdash; is absent, replaced instead by "
            "two items of internal disposition: corrupt wishes (pāpicchā) and wrong view "
            "(micchādiṭṭhi). The list's structure is four outward acts plus two inward "
            "orientations, not the standard five precepts restated."]),
        ("'As if delivered there' — an unusually direct formula", [
            "The phrase &ldquo;placed... as if delivered there&rdquo; (nikkhitto evaṁ "
            "nirayeti) states the connection between conduct and destination with unusual "
            "bluntness for this collection, framing rebirth almost as an automatic mechanical "
            "consequence rather than a probabilistic tendency."]),
        ("A titled pair with AN 6.82", [
            "This discourse and its immediate successor share the identical opening and "
            "closing formula and the identical first four items &mdash; killing, stealing, "
            "sexual misconduct, and lying &mdash; differing only in their fifth and sixth "
            "items: corrupt wishes and wrong view here, versus greed and rudeness in AN 6.82. "
            "The pairing recalls this collection's other &lsquo;first/second&rsquo; pairs, such "
            "as AN 6.73/6.74, where a shared title and target conceal a genuine difference in "
            "content."]),
    ],
    terms=[
        ("pāṇātipāta, adinnādāna, kāmesumicchācāra, musāvāda",
         "&ldquo;killing living creatures, stealing, sexual misconduct, lying&rdquo; &mdash; "
         "the first four items, matching four of the five standard lay precepts."),
        ("pāpicchā",
         "&ldquo;corrupt wishes&rdquo; &mdash; the fifth item, an inward orientation rather "
         "than an outward act."),
        ("micchādiṭṭhi",
         "&ldquo;wrong view&rdquo; &mdash; the sixth and closing item, this discourse's own "
         "term for the disposition that (with AN 6.82) most distinguishes it from its paired "
         "companion."),
        ("appicchā, sammādiṭṭhi",
         "&ldquo;few desires, right view&rdquo; &mdash; the reversal's fifth and sixth items, "
         "the direct opposites of corrupt wishes and wrong view."),
        ("nikkhitto evaṁ nirayeti / saggeti",
         "&ldquo;placed in hell / heaven, as if delivered there&rdquo; &mdash; the discourse's "
         "own unusually direct formula connecting conduct to destination."),
    ],
    text_intro=(
        "The discourse in full: four acts plus corrupt wishes and wrong view delivering "
        "someone to hell, and their reversal delivering someone to heaven. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that deliver someone to hell"),
        ("p", "&sect;1", "an6.81:1.1-1.4"),
        ("h3", "Six things that deliver someone to heaven"),
        ("p", "&sect;2", "an6.81:2.1-2.4"),
    ],
    quiz=[
        {"q": "What four acts open this discourse's six-item list?",
         "opts": [
             "The five lay precepts in full",
             "Killing living creatures, stealing, sexual misconduct, and lying",
             "Fawning, flattery, laziness, and negligence",
             "The four kinds of unwholesome thought"],
         "correct": 1,
         "expl": "Matching four of the five standard lay precepts, but not all five."},
        {"q": "Which standard lay precept is notably absent from this discourse's list, "
              "according to the guide?",
         "opts": [
             "Not killing living creatures",
             "Abstaining from intoxicants — replaced instead by corrupt wishes and wrong view",
             "Not stealing",
             "Not lying"],
         "correct": 1,
         "expl": "Four acts plus two inward orientations, not the five precepts restated."},
        {"q": "How does the guide describe the discourse's formula 'placed in hell, as if "
              "delivered there'?",
         "opts": [
             "As vague and non-committal about the connection between conduct and destination",
             "As unusually direct, framing rebirth almost as an automatic mechanical "
             "consequence rather than a probabilistic tendency",
             "As a metaphor with no bearing on actual rebirth",
             "As identical in phrasing to every other discourse in this collection"],
         "correct": 1,
         "expl": "Blunt phrasing, distinct in directness from much of this collection's other "
                 "formulas."},
        {"q": "How does AN 6.81 differ from its immediate companion, AN 6.82, according to the "
              "guide?",
         "opts": [
             "The two are word-for-word identical",
             "They share an identical opening/closing formula and first four items, differing "
             "only in their fifth and sixth items — corrupt wishes and wrong view here, versus "
             "greed and rudeness there",
             "They concern entirely unrelated topics",
             "AN 6.82 has no reversal half"],
         "correct": 1,
         "expl": "A titled pair recalling AN 6.73/6.74's shared-title, different-content "
                 "structure."},
        {"q": "What does <em>pāpicchā</em> mean?",
         "opts": ["Wrong view", "Corrupt wishes", "Few desires", "Right view"],
         "correct": 1,
         "expl": "The fifth item, an inward disposition rather than an outward act."},
        {"q": "Is a setting stated for AN 6.81?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Ñātika"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other discourses."},
        {"q": "What are the reversal's fifth and sixth items?",
         "opts": [
             "Greed and rudeness",
             "Few desires and right view",
             "Faith and wisdom",
             "Generosity and ethics"],
         "correct": 1,
         "expl": "The direct opposites of corrupt wishes and wrong view."},
    ],
    marginalia=[
        ("Four acts, two orientations", [
            "killing &middot; stealing",
            "&middot; misconduct &middot; lying —",
            "plus corrupt wishes, wrong view",
        ]),
        ("Not the five precepts", [
            "intoxicants absent —",
            "replaced by two",
            "inward dispositions",
        ]),
        ("A blunt formula", [
            "'as if delivered there' —",
            "unusually direct",
            "for this collection",
        ]),
        ("Cross-references", [
            "AN 6.82 &middot; next, this discourse's titled companion",
            "AN 6.73/6.74 &middot; earlier, a similar shared-title pair",
        ]),
    ],
    further=[
        '<a href="%s/an6.81/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.80.html">AN 6.80 &middot; Greatness</a> &mdash; previous, this '
        "chapter's other one-sided positive list.",
        '<a href="an-6.82.html">AN 6.82 &middot; Hell (2nd)</a> &mdash; next, this '
        "discourse&rsquo;s titled companion, differing in its fifth and sixth items.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.82 — Dutiyanirayasutta
# --------------------------------------------------------------------------- #
page(
    82, "Dutiyaniraya", "Hell (2nd)",
    vagga=VAGGA_8,
    meta_title="AN 6.82 — Hell (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dutiyanirayasutta, "
        "sharing AN 6.81's four acts and formula but closing on greed and rudeness rather than "
        "corrupt wishes and wrong view. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, closing the "
                 "titled pair opened by AN 6.81"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of greed with rudeness as a joint obstacle recurs in "
                              "related forms across the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and direct, sharing "
                       "four of six items with the discourse immediately before it"),
    ],
    why=(
        "AN 6.82 repeats AN 6.81's opening formula, closing formula, and first four items "
        "&mdash; killing, stealing, sexual misconduct, lying &mdash; word for word, changing "
        "only the fifth and sixth: greed (giddha) and rudeness (anādariya) here, in place of "
        "corrupt wishes and wrong view. Checked side by side, the two discourses are near "
        "duplicates with one deliberate substitution."),
    guide=[
        ("The teaching in one sentence", [
            "Killing, stealing, sexual misconduct, and lying, joined by greed and rudeness, "
            "places someone in hell; abstaining from the four acts, joined by lack of greed "
            "and courtesy, places someone in heaven."]),
        ("Four items shared exactly, two items substituted", [
            "Checked term by term against AN 6.81, the first four items of both lists are "
            "identical. Only the fifth and sixth change: AN 6.81 closed on corrupt wishes and "
            "wrong view, an internal orientation toward wanting and toward truth; this "
            "discourse closes on greed and rudeness, an internal orientation toward "
            "possessions and toward other people."]),
        ("From doctrinal wrongness to interpersonal coarseness", [
            "Where AN 6.81's closing pair concerned wrong view, a distinctly doctrinal failure, "
            "this discourse's closing pair concerns rudeness (anādariya), a failure of ordinary "
            "consideration toward others. The two discourses, read together, suggest hell is "
            "reached by more than one route beyond the shared four acts &mdash; through "
            "distorted belief, or through simple lack of regard for other people."]),
        ("Why the canon keeps such close pairs", [
            "As with AN 6.73/6.74 and AN 6.65/6.66 earlier in this collection, near-duplicate "
            "discourses differing in only one or two items are not redundancy to smooth over "
            "but a technique this series has now met repeatedly: the shared frame lets a small "
            "substitution carry the entire weight of what differs between the two teachings."]),
    ],
    terms=[
        ("pāṇātipāta, adinnādāna, kāmesumicchācāra, musāvāda",
         "&ldquo;killing living creatures, stealing, sexual misconduct, lying&rdquo; &mdash; "
         "identical to AN 6.81's first four items."),
        ("giddha",
         "&ldquo;greedy&rdquo; &mdash; the fifth item here, replacing AN 6.81's corrupt "
         "wishes."),
        ("anādariya",
         "&ldquo;rude,&rdquo; lacking consideration &mdash; the sixth and closing item, "
         "replacing AN 6.81's wrong view."),
        ("agiddha, sādariya",
         "&ldquo;not greedy, considerate&rdquo; &mdash; the reversal's fifth and sixth items, "
         "the direct opposites closing this discourse's heaven-bound list."),
        ("nikkhitto evaṁ nirayeti / saggeti",
         "&ldquo;placed in hell / heaven, as if delivered there&rdquo; &mdash; identical to AN "
         "6.81's formula, unchanged between the two discourses."),
    ],
    text_intro=(
        "The discourse in full: four acts plus greed and rudeness delivering someone to hell, "
        "and their reversal delivering someone to heaven. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that deliver someone to hell"),
        ("p", "&sect;1", "an6.82:1.1-1.4"),
        ("h3", "Six things that deliver someone to heaven"),
        ("p", "&sect;2", "an6.82:2.1-2.4"),
    ],
    quiz=[
        {"q": "How many of AN 6.82's six items are identical to AN 6.81's, checked term by "
              "term?",
         "opts": ["None", "The first four — killing, stealing, sexual misconduct, and lying", "All six", "Only two"],
         "correct": 1,
         "expl": "Near-duplicate discourses, differing only in their fifth and sixth items."},
        {"q": "What replaces AN 6.81's 'corrupt wishes and wrong view' in this discourse's "
              "list?",
         "opts": [
             "Laziness and negligence",
             "Greed (giddha) and rudeness (anādariya)",
             "Doubt and restlessness",
             "Fawning and flattery"],
         "correct": 1,
         "expl": "One deliberate substitution, carrying the entire difference between the two "
                 "discourses."},
        {"q": "How does the guide characterize the shift from AN 6.81's closing pair to this "
              "discourse's?",
         "opts": [
             "No meaningful difference at all",
             "A shift from a doctrinal failure (wrong view) to a failure of ordinary "
             "consideration toward others (rudeness)",
             "A shift from ethical conduct to meditative attainment",
             "A shift toward praising greed as acceptable"],
         "correct": 1,
         "expl": "Two different routes to the same destination, beyond the shared four acts."},
        {"q": "According to the guide, what does this discourse's relationship to AN 6.81 "
              "illustrate?",
         "opts": [
             "A copying error in the source text",
             "A technique this collection has used repeatedly — a shared frame letting a small "
             "substitution carry the entire weight of what differs between two teachings",
             "That the two discourses should be merged into one",
             "That only one of the two is considered authoritative"],
         "correct": 1,
         "expl": "A device already met at AN 6.65/6.66 and AN 6.73/6.74 earlier in this "
                 "collection."},
        {"q": "Is a setting stated for AN 6.82?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Isipatana"],
         "correct": 1,
         "expl": "A bare formula, identical in form to AN 6.81's."},
        {"q": "What does <em>anādariya</em> mean?",
         "opts": ["Greed", "Rudeness, lacking consideration", "Wrong view", "Corrupt wishes"],
         "correct": 1,
         "expl": "The sixth and closing item, replacing AN 6.81's wrong view."},
        {"q": "What is identical between AN 6.81 and AN 6.82's opening and closing formulas?",
         "opts": [
             "Nothing is shared between the two",
             "Both formulas are word for word identical — 'placed in hell/heaven, as if "
             "delivered there'",
             "Only the opening formula is shared",
             "Only the closing formula is shared"],
         "correct": 1,
         "expl": "An unchanged shared frame around the one substituted pair of items."},
    ],
    marginalia=[
        ("Four items shared exactly", [
            "killing &middot; stealing",
            "&middot; misconduct &middot; lying —",
            "identical to AN 6.81",
        ]),
        ("One substitution", [
            "wrong view &rarr; rudeness,",
            "corrupt wishes &rarr; greed —",
            "the entire difference",
        ]),
        ("Two routes to hell", [
            "distorted belief,",
            "or plain lack of regard",
            "for other people",
        ]),
        ("Cross-references", [
            "AN 6.81 &middot; previous, this discourse's near-duplicate companion",
        ]),
    ],
    further=[
        '<a href="%s/an6.82/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.81.html">AN 6.81 &middot; Hell (1st)</a> &mdash; previous, this '
        "discourse's near-duplicate companion.",
        '<a href="an-6.83.html">AN 6.83 &middot; The Best Thing</a> &mdash; next, a return to '
        "this chapter's own theme of perfection.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.83 — Aggadhammasutta
# --------------------------------------------------------------------------- #
page(
    83, "Aggadhamma", "The Best Thing",
    vagga=VAGGA_8,
    meta_title="AN 6.83 — The Best Thing | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Aggadhammasutta, "
        "naming five qualities plus concern for body and life as what blocks or enables "
        "perfection, the best thing. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, returning to this "
                 "chapter's own theme of perfection"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of faith, conscience, prudence, energy, and wisdom "
                              "as a fixed positive set recurs widely across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a familiar five-item set "
                       "from elsewhere in the canon, paired here with a distinct sixth item on "
                       "attachment to body and life"),
    ],
    why=(
        "AN 6.83 returns explicitly to this chapter's own title: &ldquo;a mendicant with six "
        "qualities can't realize the best thing, perfection&rdquo; &mdash; aggaṁ arahattaṁ, the "
        "discourse's own doubled phrase for the same attainment named throughout this chapter. "
        "Its blocking list combines a familiar five-item set (faithless, shameless, imprudent, "
        "lazy, witless) with a sixth, distinct item: being concerned with one's own body and "
        "life."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant who is faithless, shameless, imprudent, lazy, and witless, and "
            "concerned with their body and life, cannot realize perfection; one who is "
            "faithful, conscientious, prudent, energetic, and wise, with no such concern, can."]),
        ("A five-item set met before, with wisdom replacing conscience's usual partner", [
            "Faith, conscience, prudence, energy, and wisdom form a recognizable positive set "
            "across this literature, close in shape to the five spiritual faculties "
            "(indriya) though not identical to them term for term — here energy stands in "
            "where the more familiar formula names mindfulness or immersion."]),
        ("A sixth item naming attachment, not a fault of conduct", [
            "&ldquo;Concerned with their body and their life&rdquo; (kāyasitāya jīvitasitāya) "
            "names something categorically different from the other five: not a missing virtue "
            "but an attachment actively held, the fear of losing body and life that the "
            "reversal's &ldquo;no concern&rdquo; directly answers."]),
        ("'The best thing' as this discourse's own doubled phrase", [
            "Aggadhamma, &ldquo;the best thing,&rdquo; is glossed by the discourse itself as "
            "arahatta, perfection &mdash; the same term titling this entire chapter and shared "
            "with AN 6.66 and AN 6.76. A fourth discourse in this collection converges on the "
            "same target attainment while, checked term by term, naming its own distinct "
            "six-item path to blocking or enabling it."]),
    ],
    terms=[
        ("assaddha, ahirika, anottappī, kusīta, duppañña",
         "&ldquo;faithless, shameless, imprudent, lazy, witless&rdquo; &mdash; the first five "
         "items, a recognizable positive/negative set close in shape to the five spiritual "
         "faculties though not identical to them term for term."),
        ("kāyasitāya jīvitasitāya",
         "&ldquo;concerned with their body and their life&rdquo; &mdash; the sixth item, "
         "naming an attachment actively held rather than a missing virtue."),
        ("aggadhamma",
         "&ldquo;the best thing&rdquo; &mdash; the discourse's own title, glossed within the "
         "text itself as arahatta, perfection."),
        ("saddha, hirimā, ottappī, āraddhavīriya, paññavā",
         "&ldquo;faithful, conscientious, prudent, energetic, wise&rdquo; &mdash; the "
         "reversal's first five items, direct opposites of the blocking set."),
        ("anapekkho kāyena jīvitena",
         "&ldquo;with no concern for body or life&rdquo; &mdash; the reversal's sixth item, "
         "directly answering the blocking list's attachment."),
    ],
    text_intro=(
        "The discourse in full: five qualities plus concern for body and life blocking "
        "perfection, and their reversal enabling it. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that block perfection"),
        ("p", "&sect;1", "an6.83:1.1-1.4"),
        ("h3", "Six things that enable it"),
        ("p", "&sect;2", "an6.83:2.1-2.4"),
    ],
    quiz=[
        {"q": "What does this discourse's title, 'the best thing' (aggadhamma), refer to, "
              "according to the discourse itself?",
         "opts": [
             "An unspecified, unnamed attainment",
             "Arahatta, perfection — the same term titling this entire chapter",
             "The first absorption specifically",
             "Rebirth as a deity"],
         "correct": 1,
         "expl": "Glossed within the text itself, converging with AN 6.66 and AN 6.76 on the "
                 "same target attainment."},
        {"q": "What five items open this discourse's blocking list?",
         "opts": [
             "The five hindrances",
             "Faithless, shameless, imprudent, lazy, and witless",
             "Killing, stealing, sexual misconduct, lying, and drinking",
             "Dullness, drowsiness, restlessness, remorse, and doubt"],
         "correct": 1,
         "expl": "A recognizable positive/negative set close in shape to the five spiritual "
                 "faculties."},
        {"q": "How does the guide describe the sixth item, concern for body and life, compared "
              "to the first five?",
         "opts": [
             "Identical in kind to the first five — a missing virtue",
             "Categorically different — an attachment actively held, rather than a missing "
             "virtue",
             "Unrelated to the discourse's overall teaching",
             "A synonym for laziness"],
         "correct": 1,
         "expl": "Fear of losing body and life, directly answered by the reversal's stated "
                 "absence of that concern."},
        {"q": "How many discourses in this collection have now converged on 'perfection' "
              "(arahatta) as their target attainment while naming distinct blocking lists?",
         "opts": [
             "Only this one",
             "At least four — AN 6.66, AN 6.76, and now AN 6.83, each with checked, distinct "
             "content",
             "Every discourse in the entire collection",
             "Exactly two"],
         "correct": 1,
         "expl": "A recurring target, reached (or blocked) by genuinely different routes each "
                 "time."},
        {"q": "Is a setting stated for AN 6.83?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Vesālī"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other discourses."},
        {"q": "What does <em>anottappī</em> mean?",
         "opts": ["Faithless", "Imprudent", "Lazy", "Witless"],
         "correct": 1,
         "expl": "The third of the five items opening this discourse's blocking list."},
        {"q": "What does the reversal's sixth item, 'no concern for body or life,' directly "
              "answer?",
         "opts": [
             "The blocking list's laziness specifically",
             "The blocking list's attachment to body and life, its sixth item",
             "Nothing — the reversal has only five items",
             "The blocking list's lack of faith"],
         "correct": 1,
         "expl": "A direct structural opposite, item for item, including the sixth."},
    ],
    marginalia=[
        ("Five familiar items", [
            "faithless &middot; shameless",
            "&middot; imprudent &middot; lazy",
            "&middot; witless — close to the five faculties",
        ]),
        ("A sixth item: attachment", [
            "concern for body",
            "and life — held, not",
            "merely a missing virtue",
        ]),
        ("A fourth 'perfection'", [
            "aggadhamma glossed",
            "as arahatta —",
            "same target, distinct list",
        ]),
        ("Cross-references", [
            "AN 6.66/6.76 &middot; earlier, other discourses converging on the same target",
            "AN 6.82 &middot; previous, closing the hell/heaven pair",
        ]),
    ],
    further=[
        '<a href="%s/an6.83/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.82.html">AN 6.82 &middot; Hell (2nd)</a> &mdash; previous, closing the '
        "hell/heaven pair.",
        '<a href="an-6.84.html">AN 6.84 &middot; Day and Night</a> &mdash; next, closing this '
        "chapter on growth and decline.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 6.84 — Rattidivasasutta
# --------------------------------------------------------------------------- #
page(
    84, "Rattidivasa", "Day and Night",
    vagga=VAGGA_8,
    meta_title="AN 6.84 — Day and Night | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Rattidivasasutta, "
        "closing this chapter with six qualities determining growth or decline in skillful "
        "qualities day and night. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_NONE),
        ("Speakers", SPEAKER),
        ("Form", "Two matched six-item lists, cause and its direct reversal, closing this "
                 "chapter"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The pairing of contentment with the four requisites and the "
                              "four faithful/ethical/mindful/wise qualities recurs widely "
                              "across the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and formulaic, "
                       "closing the chapter on a compact six-item list"),
    ],
    why=(
        "AN 6.84 closes Arahattavagga with a discourse pairing having many desires and "
        "discontent with the four requisites &mdash; robes, almsfood, lodgings, and medicine "
        "&mdash; against four further qualities (faithless, unethical, unmindful, witless), "
        "and states the stakes in an unusual temporal frame: growth or decline in skillful "
        "qualities, measured &ldquo;whether by day or by night.&rdquo;"),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant with many desires, discontent with any kind of robes, almsfood, "
            "lodgings, and medicine, and faithless, unethical, unmindful, and witless, can "
            "expect decline rather than growth in skillful qualities, day or night; the "
            "reversal of all six brings growth rather than decline."]),
        ("Contentment named first, ethical qualities following", [
            "The list opens not with an ethical failing but with a disposition toward "
            "material provisions: many desires (mahiccha) and discontent (asantuṭṭha) with "
            "&ldquo;any kind&rdquo; of the four basic requisites. Only after this does the list "
            "turn to faith, ethics, mindfulness, and wisdom &mdash; suggesting contentment with "
            "material provision is treated here as a precondition for the more familiar "
            "ethical qualities that follow it, not a separate, unrelated concern."]),
        ("'Whether by day or by night' — an unusual temporal frame", [
            "Most discourses in this chapter state their outcome without any temporal "
            "qualification. This discourse's closing phrase, &ldquo;whether by day or by "
            "night&rdquo; (rattiṁ vā divā vā), makes explicit what is elsewhere left implicit: "
            "that growth or decline in skillful qualities is not confined to formal meditation "
            "sessions but proceeds continuously, at every hour."]),
        ("Closing the chapter on the same register it opened with", [
            "Arahattavagga opened at AN 6.75 with thoughts and perceptions determining present "
            "happiness and future rebirth, and closes here with contentment and ethical "
            "qualities determining growth or decline across all hours &mdash; both discourses "
            "framing their six items as operating continuously, in the texture of an ordinary "
            "day, rather than only within formal practice."]),
    ],
    terms=[
        ("mahiccha, asantuṭṭha",
         "&ldquo;many desires, discontent&rdquo; &mdash; the first two items, naming a "
         "disposition toward material provisions rather than an ethical failing directly."),
        ("cīvara, piṇḍapāta, senāsana, gilānappaccayabhesajjaparikkhāra",
         "&ldquo;robes, almsfood, lodgings, medicines and supplies for the sick&rdquo; &mdash; "
         "the four basic requisites, named in full as what a discontented mendicant is "
         "dissatisfied with."),
        ("assaddha, dussīla, muṭṭhassati, duppañña",
         "&ldquo;faithless, unethical, unmindful, witless&rdquo; &mdash; the remaining four "
         "items, following the material disposition named first."),
        ("rattiṁ vā divā vā",
         "&ldquo;whether by day or by night&rdquo; &mdash; the discourse's own closing "
         "temporal frame, making explicit that growth or decline proceeds continuously."),
        ("appiccha, santuṭṭha",
         "&ldquo;few desires, content&rdquo; &mdash; the reversal's first two items, the direct "
         "opposites opening this discourse's growth-bound list."),
    ],
    text_intro=(
        "The discourse in full: contentment and four ethical qualities determining growth or "
        "decline in skillful qualities, day and night. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Six things that bring decline"),
        ("p", "&sect;1", "an6.84:1.1-1.4"),
        ("h3", "Six things that bring growth"),
        ("p", "&sect;2", "an6.84:2.1-2.4"),
    ],
    quiz=[
        {"q": "What two items open this discourse's list, before its four ethical qualities?",
         "opts": [
             "Faithlessness and unethical conduct",
             "Many desires and discontent with any kind of the four requisites",
             "Lack of mindfulness and wisdom",
             "Killing and stealing"],
         "correct": 1,
         "expl": "A disposition toward material provisions, named before the more familiar "
                 "ethical qualities."},
        {"q": "According to the guide, what does opening the list with contentment (rather "
              "than an ethical quality) suggest?",
         "opts": [
             "That contentment is unrelated to the rest of the list",
             "That contentment with material provision is treated as a precondition for the "
             "ethical qualities that follow, not a separate concern",
             "That the list is presented in a random, meaningless order",
             "That ethical qualities are more important than contentment"],
         "correct": 1,
         "expl": "A structural ordering that implies precondition, not mere coincidence."},
        {"q": "What does the discourse's closing phrase 'whether by day or by night' make "
              "explicit, according to the guide?",
         "opts": [
             "That growth or decline only occurs during formal meditation sessions",
             "That growth or decline in skillful qualities proceeds continuously, at every "
             "hour, not confined to formal practice",
             "That the teaching applies only to nighttime practice",
             "Nothing — the phrase is purely decorative"],
         "correct": 1,
         "expl": "An unusual temporal frame most other discourses in this chapter leave "
                 "implicit."},
        {"q": "How does the guide connect this discourse to AN 6.75, which opened the chapter?",
         "opts": [
             "No connection is drawn between the two",
             "Both frame their six items as operating continuously, in the texture of an "
             "ordinary day, rather than only within formal practice",
             "AN 6.75 and AN 6.84 share an identical six-item list",
             "AN 6.84 directly contradicts AN 6.75's teaching"],
         "correct": 1,
         "expl": "A chapter bookended by two discourses concerned with continuous, ordinary-life "
                 "operation rather than formal practice alone."},
        {"q": "What four requisites are named in full in this discourse?",
         "opts": [
             "Food, water, shelter, and clothing",
             "Robes, almsfood, lodgings, and medicines and supplies for the sick",
             "Faith, ethics, mindfulness, and wisdom",
             "The four noble truths"],
         "correct": 1,
         "expl": "The standard four basic requisites of monastic life."},
        {"q": "Is a setting stated for AN 6.84?",
         "opts": ["Yes, at Sāvatthī", "No — none is stated", "Yes, at Rājagaha", "Yes, at Kimbilā"],
         "correct": 1,
         "expl": "A bare formula, matching this chapter's other discourses, closing "
                 "Arahattavagga."},
        {"q": "What does <em>muṭṭhassati</em> mean?",
         "opts": ["Faithless", "Unmindful", "Witless", "Unethical"],
         "correct": 1,
         "expl": "The third of the four ethical qualities following the two material-disposition "
                 "items."},
    ],
    marginalia=[
        ("Contentment, then ethics", [
            "many desires,",
            "discontent — then faith,",
            "ethics, mindfulness, wisdom",
        ]),
        ("A continuous frame", [
            "'whether by day",
            "or by night' —",
            "growth or decline, every hour",
        ]),
        ("Bookending the chapter", [
            "AN 6.75 opened on",
            "continuous operation;",
            "AN 6.84 closes the same way",
        ]),
        ("Cross-references", [
            "AN 6.75 &middot; the chapter's opening discourse, on the same continuous register",
            "AN 6.83 &middot; previous, this chapter's own 'perfection' discourse",
        ]),
    ],
    further=[
        '<a href="%s/an6.84/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-6.83.html">AN 6.83 &middot; The Best Thing</a> &mdash; previous, this '
        "chapter's own discourse on perfection.",
        '<a href="an-6.75.html">AN 6.75 &middot; Suffering</a> &mdash; back to this chapter’s '
        "opening, for contrast with the chapter now closing.",
    ],
)
