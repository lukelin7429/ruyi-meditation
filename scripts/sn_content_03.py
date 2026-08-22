# -*- coding: utf-8 -*-
"""Khandhavagga — The Book of the Aggregates (SN 22-34). One discourse per
page, with merged pages for peyyāla (formula-repetition) ranges wherever
bilara-data itself stores them as a single file."""

SC = "https://suttacentral.net"

INDEX_HEADING = "III. Khandhavagga — The Book of the Aggregates"
# SN 22.1 (Nakulapitusutta), SN 22.59 (Anattalakkhaṇasutta, the Buddha's
# second sermon), and SN 22.87 (Vakkalisutta) were published before this
# series began working in order, in the earlier twenty-page selection; they
# are listed in the index by INDEX_EXTRA and are not generated here. Unlike
# Book I (SN 1.1) or Book II (SN 12.1/12.2), none of Book III's pre-existing
# pages cluster at the book's own opening except SN 22.1 itself -- SN 22.59
# and SN 22.87 sit mid-sequence, inside vaggas this module has not reached
# yet (Upayavagga and Theravagga respectively), so they will need the same
# "fragile junction" treatment Book II discovered at SN 12.15/12.61/12.65/
# 15.3: once a vagga containing one of them is generated, sn_build.py's
# auto-chain will skip straight over the pre-existing page, and its
# neighbours' prev/next must be hand-patched after every single build.
#
# Systematic coverage of this book starts at SN 22.2, the first discourse of
# Nakulapituvagga not already published. HEAD is that nearest already-
# published page immediately before this module's first new page (SN 22.1
# itself). TAIL points at the nearest already-published page beyond
# whatever this module currently covers -- moved forward as later vaggas
# are completed, exactly as sn_content_01.py's and sn_content_02.py's TAIL
# were moved across the course of Books I and II. It starts at SN 22.59,
# the nearest already-published page beyond Nakulapituvagga (SN 22.1-11).
#
# One additional one-time step this module needs that earlier books did
# not: SN 22.1's own "next" link, a static field baked into its already-
# built HTML file, still points to SN 22.59 (the old three-page placeholder
# chain from the original twenty-page selection). sn_index.py's hand-off
# only ever repatches mod.TAIL's prev link, never mod.HEAD's next link, so
# SN 22.1.html's next must be hand-edited once, right now, to point to
# SN 22.2 -- the same one-time fix Book I and Book II's own HEAD pages
# (SN 1.1, SN 12.1, SN 12.2) evidently received when each book began.
HEAD = ("sn-22.1.html", "SN 22.1 &middot; Nakula&rsquo;s Father")
TAIL = ("sn-22.59.html", "SN 22.59 &middot; The Characteristic of Not-Self")
INDEX_EXTRA = [
    ("sn-22.1", "Nakulapitā", "Nakula's Father"),
    ("sn-22.59", "Anattalakkhaṇa", "The Characteristic of Not-Self"),
    ("sn-22.87", "Vakkali", "With Vakkali"),
]

PAGES = []


def page(samyutta, num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Khandhavagga.

    Same two-parameter signature as sn_content_01.py's and
    sn_content_02.py's page() (samyutta, then discourse number), since this
    book spans several independently numbered saṃyuttas (SN 22, 23, 24...)
    just as Books I and II did.
    """
    d = {
        "slug": "sn-%d.%d" % (samyutta, num),
        "index_pali": pali,
        "nav_title": title,
        "source": "sn%d/sn%d.%d" % (samyutta, samyutta, num),
        "crumb": "SN %d.%d" % (samyutta, num),
        "number_line": "Saṃyutta Nikāya &middot; Discourse %d.%d" % (samyutta, num),
        "title": title,
        "subtitle": "<em>%ssutta</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


def page_range(samyutta, lo, hi, pali, title, **kw):
    """Scaffolding for a single page covering a merged range of discourse
    numbers (a peyyāla block bilara-data itself stores as one file)."""
    d = {
        "slug": "sn-%d.%d-%d" % (samyutta, lo, hi),
        "index_pali": pali,
        "nav_title": title,
        "source": "sn%d/sn%d.%d-%d" % (samyutta, samyutta, lo, hi),
        "crumb": "SN %d.%d&ndash;%d" % (samyutta, lo, hi),
        "number_line": "Saṃyutta Nikāya &middot; Discourses %d.%d&ndash;%d" % (samyutta, lo, hi),
        "title": title,
        "subtitle": "<em>%ssutta</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d
# --------------------------------------------------------------------------- #
# SN 22.2 — Devadahasutta
# --------------------------------------------------------------------------- #
page(
    22, 2, "Devadaha", "At Devadaha",
    vagga="Nakulapituvagga",
    meta_title="SN 22.2 — At Devadaha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Devadahasutta &mdash; Sāriputta drills a group of "
        "mendicants heading abroad on exactly how to field a hostile "
        "question about what the Buddha teaches. Opens Khandhavagga's "
        "first new discourse. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "The land of the Sakyans, at Devadaha"),
        ("Speakers", "The Buddha briefly, then Venerable Sāriputta at "
                     "length, addressing mendicants departing for a "
                     "western land"),
        ("Form", "A rehearsal &mdash; the Buddha sends the travelers "
                 "to Sāriputta, who drills them through an escalating "
                 "three-question interrogation an astute outsider "
                 "might pose"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "plainly structured as a rehearsed script, "
                       "easy to follow despite the escalating "
                       "questions"),
    ],
    why=(
        "This discourse is a training session for missionaries. A "
        "group of mendicants ask the Buddha's leave to relocate to a "
        "western land, and instead of simply granting it, he sends "
        "them to Sāriputta first &mdash; because astute strangers in "
        "unfamiliar territory will interrogate them, and they need to "
        "be able to answer without misrepresenting him. What follows "
        "is Sāriputta's rehearsal of exactly that interrogation, three "
        "rounds deep: what does your teacher teach, regarding what, "
        "and what drawback did he see that makes him teach it. Each "
        "answer only earns the right to a harder follow-up question. "
        "It is one of the clearest windows in the canon onto how the "
        "earliest community expected its traveling teachers to present "
        "the doctrine under real scrutiny, rather than to a friendly "
        "home audience."
    ),
    guide=[
        ("A relocation request becomes a rehearsal", [
            "Several mendicants tell the Buddha they wish to take up "
            "residence in a western land. He does not simply approve "
            "or refuse &mdash; he asks whether they have taken leave "
            "of Sāriputta first. They have not, so he sends them to "
            "do so, praising Sāriputta as astute (paṇḍito) and a "
            "supporter of his fellow mendicants (anuggāhako "
            "sabrahmacārīnaṁ). The request for permission to travel "
            "quietly turns into a request for preparation.",
        ]),
        ("Three rounds, each harder than the last", [
            "Sāriputta anticipates that astute questioners &mdash; "
            "aristocrats, brahmins, householders, and ascetics alike "
            "&mdash; will not stop at one question. Round one: "
            "&ldquo;what does your teacher teach?&rdquo; Answer: the "
            "removal of desire and lust (chandarāgavinaya). Round "
            "two: &ldquo;regarding what?&rdquo; Answer: regarding "
            "form, feeling, perception, choices, and consciousness "
            "&mdash; the five aggregates. Round three, doubled: "
            "&ldquo;what drawback did he see&rdquo; that makes him "
            "teach removal, and &ldquo;what benefit&rdquo; does he "
            "see in it. The drawback answer and the benefit answer "
            "are mirror images of each other, built from the same "
            "vocabulary run in opposite directions.",
        ]),
        ("The drawback and the benefit, in the same words", [
            "The drawback: someone not free of greed, desire, "
            "fondness, thirst, passion, and craving for an aggregate "
            "suffers sorrow, lamentation, pain, sadness, and distress "
            "when that aggregate decays and perishes &mdash; because "
            "it certainly will. The benefit: someone who is free of "
            "that same list does not suffer that same list when the "
            "same decay happens. Nothing changes about the aggregates "
            "themselves between the two answers; what changes is "
            "whether the hearer's greed for them is still attached "
            "when they perish, which they perish regardless.",
        ]),
        ("A closing argument that never mentions rebirth doctrine", [
            "The discourse ends on a short, deliberately practical "
            "argument, addressed to the traveling mendicants "
            "directly rather than staged as part of the rehearsed "
            "outsider dialogue: if living by unskillful qualities "
            "actually produced a happy, untroubled present life and "
            "a good rebirth, the Buddha would not praise giving them "
            "up; and if living by skillful qualities actually "
            "produced an unhappy present life and a bad rebirth, he "
            "would not praise taking them up. Since neither of those "
            "counterfactuals holds, the praise follows. It is an "
            "argument from consequences that a skeptical outsider "
            "could weigh without first accepting any of the Buddha's "
            "metaphysics.",
        ]),
    ],
    terms=[
        ("chandarāgavinayakkhāyī",
         "&ldquo;one who explains the removal of desire and "
         "lust&rdquo; &mdash; the standing one-line summary of what "
         "the Buddha teaches, given as round one's answer."),
        ("paṇḍitā&hellip;vīmaṁsakā",
         "&ldquo;astute&hellip;inquisitive&rdquo; &mdash; how "
         "Sāriputta characterizes the questioners the travelers "
         "should expect, justifying the rehearsal's escalating "
         "difficulty."),
        ("ādīnava",
         "&ldquo;drawback&rdquo; &mdash; round three's first "
         "question, asking what fault the Buddha saw in the "
         "aggregates that led him to teach their relinquishment."),
        ("ānisaṁsa",
         "&ldquo;benefit&rdquo; &mdash; round three's second "
         "question, the mirror image of ādīnava, asking what is "
         "gained by relinquishing them instead."),
        ("apalokito",
         "&ldquo;taken leave of&rdquo; &mdash; the Buddha's opening "
         "question to the travelers, redirecting the entire "
         "discourse toward Sāriputta before any doctrine is taught."),
    ],
    text_intro=(
        "The discourse in full. Two short peyyāla compressions in "
        "the source (the list of four questioner-types, and the "
        "aggregate-by-aggregate repetition in round two) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.2:1.1-2.5"),
        ("p", "&sect;2", "sn22.2:3.1-3.5"),
        ("p", "&sect;3", "sn22.2:4.1-4.4"),
        ("p", "&sect;4", "sn22.2:5.1-5.5"),
        ("p", "&sect;5", "sn22.2:6.1-6.6"),
        ("p", "&sect;6", "sn22.2:7.1-7.10"),
        ("p", "&sect;7", "sn22.2:8.1-8.20"),
        ("p", "&sect;8", "sn22.2:9.1-9.18"),
        ("p", "&sect;9", "sn22.2:10.1-11.2"),
        ("p", "&sect;10", "sn22.2:12.1-12.2"),
    ],
    quiz=[
        {"q": "Why does the Buddha send the departing mendicants to Sāriputta instead of simply granting their request?",
         "opts": [
             "Because astute questioners abroad will interrogate them, and they need to be able to answer accurately",
             "Because only Sāriputta has authority to approve travel",
             "Because the Buddha is displeased with their request",
             "Because Sāriputta needs their help on an unrelated errand"],
         "correct": 0,
         "expl": "The Buddha explicitly frames it as preparation for facing inquisitive outsiders."},
        {"q": "What is Sāriputta's answer to round one, \"what does your teacher teach\"?",
         "opts": [
             "The removal of desire and lust",
             "The existence of an eternal self",
             "Strict ascetic practice above all else",
             "Devotion to a particular deity"],
         "correct": 0,
         "expl": "Chandarāgavinaya — the standing one-line summary given first."},
        {"q": "What is the answer to round two, \"regarding what\"?",
         "opts": [
             "The five aggregates: form, feeling, perception, choices, and consciousness",
             "The four noble truths only",
             "The physical body alone",
             "Wealth and possessions"],
         "correct": 0,
         "expl": "Each aggregate is named in turn as the object of the removal."},
        {"q": "What is the \"drawback\" (ādīnava) given for craving an aggregate?",
         "opts": [
             "Sorrow, lamentation, pain, sadness, and distress arise when it decays and perishes",
             "It slows physical growth",
             "It attracts social criticism",
             "It shortens the lifespan"],
         "correct": 0,
         "expl": "Because the aggregate will decay regardless of whether one is attached to it."},
        {"q": "What is the \"benefit\" (ānisaṁsa) of being rid of craving for an aggregate?",
         "opts": [
             "The same decay happens, but it no longer gives rise to sorrow and distress",
             "The aggregate itself stops decaying",
             "One is reborn immediately in a heavenly realm",
             "One gains supernatural powers"],
         "correct": 0,
         "expl": "The aggregate's fate is unchanged; only the response to it changes."},
        {"q": "How does the discourse characterize the questioners the travelers should expect?",
         "opts": [
             "Astute and inquisitive, across several social classes",
             "Uniformly hostile and violent",
             "Only interested in political matters",
             "Uninterested in philosophical questions"],
         "correct": 0,
         "expl": "Aristocrats, brahmins, householders, and ascetics are all named as potential questioners."},
        {"q": "What closing argument does Sāriputta give for why the Buddha praises giving up unskillful qualities?",
         "opts": [
             "If it did not lead to a happier present life and a good rebirth, the Buddha would not praise it",
             "Because scripture commands it without further reason",
             "Because unskillful qualities are illegal",
             "Because ancestors disapproved of them"],
         "correct": 0,
         "expl": "An argument from actual consequences, addressed directly to the travelers."},
        {"q": "Where is the Buddha staying when this discourse takes place?",
         "opts": [
             "Devadaha, in the land of the Sakyans",
             "Sāvatthī, Jeta's Grove",
             "Rājagaha, Vulture's Peak",
             "Vesālī, the Great Wood"],
         "correct": 0,
         "expl": "One of the few discourses in this saṃyutta not set at Sāvatthī."},
        {"q": "How does the Buddha describe Sāriputta when sending the travelers to him?",
         "opts": [
             "Astute, and a supporter of his fellow mendicants",
             "The most senior in ordination",
             "The strictest keeper of monastic rules",
             "Skilled above all in debate with outsiders"],
         "correct": 0,
         "expl": "Paṇḍito, anuggāhako sabrahmacārīnaṁ — praise tied directly to why he is the right person to consult."},
        {"q": "What position does this discourse hold within Nakulapituvagga?",
         "opts": [
             "The first new discourse generated after the vagga's pre-existing opening page, SN 22.1",
             "The vagga's final discourse",
             "An isolated discourse unconnected to the vagga",
             "A discourse added centuries after the rest of the vagga"],
         "correct": 0,
         "expl": "Opens Khandhavagga's systematic coverage, immediately after SN 22.1."},
    ],
    marginalia=[
        ("A travel request that becomes a training session", [
            "not granted outright &mdash;",
            "redirected to preparation first",
        ]),
        ("Three rounds, each harder than the one before", [
            "what, regarding what, why &mdash;",
            "escalating scrutiny rehearsed in advance",
        ]),
        ("Same words, opposite direction", [
            "drawback and benefit &mdash;",
            "built from an identical vocabulary list",
        ]),
        ("An argument outsiders could weigh on their own terms", [
            "consequences, not metaphysics &mdash;",
            "closing appeal needs no prior belief",
        ]),
    ],
    further=[
        '<a href="%s/sn22.2/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.1.html">SN 22.1 &middot; Nakula&rsquo;s '
        "Father</a> &mdash; the vagga's pre-existing opening "
        "discourse, on keeping a healthy mind through illness.",
        '<a href="sn-22.3.html">SN 22.3 &middot; With '
        "Hāliddikāni</a> &mdash; the next discourse, Mahākaccāna's "
        "detailed exegesis of a different brief verse.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.3 — Hāliddikānisutta
# --------------------------------------------------------------------------- #
page(
    22, 3, "Hāliddikāni", "With Hāliddikāni",
    vagga="Nakulapituvagga",
    meta_title="SN 22.3 — With Hāliddikāni | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Hāliddikānisutta &mdash; Mahākaccāna's line-by-line "
        "exegesis of a compressed verse from the Aṭṭhakavagga, using "
        "the aggregates as a shelter and the six sense fields as "
        "abodes. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Steep Mountain, near Kuraraghara, in the land of "
                    "the Avantis"),
        ("Speakers", "The householder Hāliddikāni questions Venerable "
                     "Mahākaccāna, who answers at length"),
        ("Form", "A householder quotes a brief verse the Buddha gave "
                 "elsewhere and asks for its detailed meaning; a "
                 "senior disciple supplies a term-by-term gloss"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "dense exegesis built from four separate "
                       "questions layered over one verse"),
    ],
    why=(
        "Venerable Mahākaccāna was named by the Buddha as foremost "
        "among disciples at explaining in detail what the Buddha said "
        "in brief, and this discourse is that gift on full display. A "
        "householder brings him four lines of verse from &ldquo;The "
        "Questions of Māgandiya&rdquo; &mdash; part of the Aṭṭhakavagga, "
        "itself among the oldest strata of the Pali canon &mdash; and "
        "asks what they mean in detail. Mahākaccāna answers by taking "
        "the verse apart image by image: a migrant leaving their "
        "bastion, wandering without abode, not getting close to town, "
        "rid of sensual pleasures, not expecting, not arguing. Each "
        "image gets its own question-and-answer pair, and each pair "
        "is built from the five aggregates or the six sense fields. It "
        "is a compact demonstration of how the earliest community "
        "read its own most compressed verse, line by line, in "
        "ordinary discourse."
    ),
    guide=[
        ("A verse quoted, and a question about its detail", [
            "Hāliddikāni recites four lines the Buddha spoke in "
            "&ldquo;The Questions of Māgandiya&rdquo;: a sage leaves "
            "their bastion to migrate without abode, does not get "
            "close to anyone in town, is rid of sensual pleasures, "
            "does not expect, and does not argue. He asks Mahākaccāna "
            "how to understand this brief statement's detailed "
            "meaning &mdash; the same kind of request Sāriputta "
            "fielded in SN 22.2, now put to a different senior "
            "disciple over different material.",
        ]),
        ("Bastion and abode: the aggregates and the six fields", [
            "Mahākaccāna glosses &ldquo;bastion&rdquo; (nivesana) as "
            "each of the five aggregates functioning as a shelter for "
            "consciousness: one whose consciousness is shackled by "
            "greed for an aggregate is a migrant going from bastion "
            "to bastion, while the Realized One &mdash; who has cut "
            "off desire for each aggregate at the root, like a palm "
            "stump, unable to arise again &mdash; is a migrant with "
            "no bastion. He then glosses &ldquo;abode&rdquo; "
            "(āyatana) separately, this time over the six sense "
            "fields (sights, sounds, smells, tastes, touches, "
            "thoughts) rather than the five aggregates &mdash; the "
            "same shackled/cut-off-at-the-root structure applied to a "
            "different classification of experience.",
        ]),
        ("Four more images, four more short glosses", [
            "The remaining phrases each get a brief, self-contained "
            "answer: getting close to people in town means mixing "
            "closely with laypeople, sharing their joys and sorrows "
            "and getting involved in their business; not getting "
            "close means the opposite. Being rid of sensual pleasures "
            "means being free of greed, desire, fondness, thirst, "
            "passion, and craving for them. Expecting means wishing "
            "for a particular form, feeling, perception, choices, or "
            "consciousness in the future; not expecting is the "
            "absence of that wish. Arguing is spelled out as a "
            "specific, almost theatrical script of debate one-upmanship.",
        ]),
        ("A verbatim script of how monastics used to argue", [
            "The discourse's most vivid moment is its description of "
            "&ldquo;arguing with people&rdquo;: a taunting back-and-"
            "forth &mdash; you don't understand this teaching, I do; "
            "you're practicing wrong, I'm practicing right; you said "
            "last what should have come first; your doctrine is "
            "refuted, go save it if you can. It reads as a specific, "
            "recognizable social type rather than an abstraction, and "
            "its very concreteness is what makes &ldquo;not arguing&rdquo; "
            "legible as an actual, describable restraint rather than "
            "a vague ideal.",
        ]),
    ],
    terms=[
        ("nivesana",
         "&ldquo;bastion&rdquo; &mdash; glossed here as each of the "
         "five aggregates functioning as a shelter that consciousness "
         "can be shackled to by greed."),
        ("āyatana",
         "&ldquo;abode&rdquo; &mdash; glossed here as the six sense "
         "fields (sights through thoughts), a second classification "
         "layered onto the same verse's second image."),
        ("chinnamūla&hellip;tālāvatthukata",
         "&ldquo;cut off at the root&hellip;made like a palm "
         "stump&rdquo; &mdash; the recurring formula for how the "
         "Realized One has ended desire, so it cannot arise again."),
        ("gāmakathaṁ opāyati",
         "&ldquo;gets close to people in town&rdquo; &mdash; mixing "
         "closely with laypeople's joys, sorrows, and business, the "
         "condition Mahākaccāna glosses as its own separate question."),
        ("vādānuvādaṁ āpajjati",
         "&ldquo;argues with people&rdquo; &mdash; the verse's final "
         "phrase, illustrated with a specific, quoted script of "
         "debate taunts rather than left as an abstraction."),
    ],
    text_intro=(
        "The discourse in full. One elided repetition (the four "
        "questioner-types recurring from SN 22.2, and the "
        "sense-field-by-sense-field repetition) is given exactly as "
        "bilara-data preserves it. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.3:1.1-3.1"),
        ("p", "&sect;2", "sn22.3:4.1-4.9"),
        ("p", "&sect;3", "sn22.3:5.1-5.9"),
        ("p", "&sect;4", "sn22.3:6.1-6.8"),
        ("p", "&sect;5", "sn22.3:7.1-7.10"),
        ("p", "&sect;6", "sn22.3:8.1-9.3"),
        ("p", "&sect;7", "sn22.3:10.1-11.3"),
        ("p", "&sect;8", "sn22.3:12.1-13.4"),
        ("p", "&sect;9", "sn22.3:14.1-15.4"),
        ("p", "&sect;10", "sn22.3:16.1-17.4"),
    ],
    quiz=[
        {"q": "What kind of text does Hāliddikāni ask Mahākaccāna to explain?",
         "opts": [
             "A brief verse the Buddha spoke in \"The Questions of Māgandiya\"",
             "A monastic rule about travel",
             "A list of the Buddha's past lives",
             "An unrelated folk proverb"],
         "correct": 0,
         "expl": "Part of the Aṭṭhakavagga, quoted and then unpacked in detail."},
        {"q": "How does Mahākaccāna gloss \"bastion\" (nivesana) in the verse?",
         "opts": [
             "As each of the five aggregates, functioning as a shelter for consciousness",
             "As a literal fortress the Buddha once lived in",
             "As the monastic robe",
             "As a specific city in the Avanti region"],
         "correct": 0,
         "expl": "Consciousness shackled by greed for an aggregate is a \"migrant\" tied to that bastion."},
        {"q": "How does he gloss \"abode\" (āyatana) in the same verse?",
         "opts": [
             "As the six sense fields — sights, sounds, smells, tastes, touches, and thoughts",
             "As the aggregates again, repeating the previous answer",
             "As physical dwelling places such as monasteries",
             "As the four elements"],
         "correct": 0,
         "expl": "A second, distinct classification layered onto the verse's second image."},
        {"q": "What formula describes how the Realized One has given up desire for each aggregate?",
         "opts": [
             "Cut off at the root, made like a palm stump, unable to arise again",
             "Suppressed temporarily through willpower",
             "Transformed into a different, subtler desire",
             "Left unresolved but ignored"],
         "correct": 0,
         "expl": "A complete-ending formula, not mere suppression."},
        {"q": "What does \"getting close to people in town\" mean in Mahākaccāna's gloss?",
         "opts": [
             "Mixing closely with laypeople, sharing their joys and sorrows, getting involved in their business",
             "Simply walking through a town on alms round",
             "Accepting invitations to formal meals",
             "Teaching the Dhamma to householders"],
         "correct": 0,
         "expl": "A specific kind of emotional and practical entanglement, not mere physical proximity."},
        {"q": "What does \"arguing with people\" look like in the discourse's own quoted script?",
         "opts": [
             "A taunting exchange: you don't understand, I do; you're wrong, I'm right; your doctrine is refuted",
             "A calm, respectful philosophical debate",
             "A purely written exchange of letters",
             "A formal courtroom-style proceeding"],
         "correct": 0,
         "expl": "Vivid, specific one-upmanship, not an abstraction."},
        {"q": "What does \"expecting\" mean in this discourse's gloss?",
         "opts": [
             "Wishing for a particular form, feeling, perception, choices, or consciousness in the future",
             "Planning a future journey",
             "Hoping for good weather",
             "Anticipating a meal"],
         "correct": 0,
         "expl": "A subtle craving for a specific future configuration of the aggregates."},
        {"q": "Where does this discourse take place?",
         "opts": [
             "Steep Mountain, near Kuraraghara, in the land of the Avantis",
             "Sāvatthī, Jeta's Grove",
             "Rājagaha, Vulture's Peak",
             "Kapilavatthu, the Great Wood"],
         "correct": 0,
         "expl": "A setting outside the usual Sāvatthī/Rājagaha rotation."},
        {"q": "What honor did the Buddha give Mahākaccāna, relevant to this discourse's form?",
         "opts": [
             "Foremost among disciples at explaining in detail what was said in brief",
             "Foremost in monastic discipline",
             "Foremost in meditative absorption",
             "Foremost in teaching laypeople exclusively"],
         "correct": 0,
         "expl": "Exactly the skill this discourse demonstrates on a compressed verse."},
        {"q": "How does the next discourse, SN 22.4, relate to this one?",
         "opts": [
             "Same setting and questioner, a different Buddha verse given the same detailed treatment",
             "An unrelated discourse from a different collection",
             "A direct sequel narrating what happened after this conversation",
             "A refutation of this discourse's conclusions"],
         "correct": 0,
         "expl": "Hāliddikāni returns with a second verse, from \"The Questions of Sakka\"."},
    ],
    marginalia=[
        ("One verse, four images, four separate glosses", [
            "bastion, abode, town, arguing &mdash;",
            "each phrase earning its own question",
        ]),
        ("Two classifications for two different images", [
            "aggregates for bastion &mdash;",
            "sense fields for abode, not repeated",
        ]),
        ("Arguing given a script, not an abstraction", [
            "taunt for taunt, quoted directly &mdash;",
            "restraint made legible by its opposite",
        ]),
        ("The etadagga disciple, doing exactly his named skill", [
            "foremost at detail from brevity &mdash;",
            "reputation and performance matching exactly",
        ]),
    ],
    further=[
        '<a href="%s/sn22.3/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.2.html">SN 22.2 &middot; At Devadaha</a> '
        "&mdash; the previous discourse, Sāriputta's rehearsed "
        "answers for a different kind of outsider scrutiny.",
        '<a href="sn-22.4.html">SN 22.4 &middot; Hāliddikāni '
        "(2nd)</a> &mdash; the same householder returns with a "
        "second verse for Mahākaccāna to unpack.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.4 — Dutiyahāliddikānisutta
# --------------------------------------------------------------------------- #
page(
    22, 4, "Dutiyahāliddikāni", "Hāliddikāni (2nd)",
    vagga="Nakulapituvagga",
    meta_title="SN 22.4 — Hāliddikāni (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyahāliddikānisutta &mdash; Mahākaccāna glosses a "
        "second verse, this one from \"The Questions of Sakka,\" on "
        "what it means for the mind to be well freed. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Steep Mountain, near Kuraraghara, in the land of "
                    "the Avantis"),
        ("Speakers", "The householder Hāliddikāni questions Venerable "
                     "Mahākaccāna a second time"),
        ("Form", "The same request-and-gloss structure as SN 22.3, "
                 "compressed to a single question over a shorter "
                 "verse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "shorter and simpler than SN 22.3, a single "
                       "gloss rather than four"),
    ],
    why=(
        "Where SN 22.3 needed four separate glosses to unpack a "
        "four-line verse, this discourse needs only one, because its "
        "source verse asks a single question: what does it mean for "
        "ascetics and brahmins freed by craving's ending to have "
        "reached &ldquo;the ultimate goal&rdquo;? The verse comes "
        "from &ldquo;The Questions of Sakka&rdquo; (Sakkapañha, "
        "corresponding to DN 21), spoken originally to the king of "
        "the gods. Mahākaccāna's answer is compact: it is the ending "
        "of desire, greed, relishing, and craving for each of the "
        "five aggregates that counts as the mind being &ldquo;well "
        "freed&rdquo; (suvimuttacitta). Paired with SN 22.3, this "
        "discourse shows the same disciple's gloss-by-detail method "
        "working at two different scales &mdash; four images or one."
    ),
    guide=[
        ("A shorter verse, a single question", [
            "Hāliddikāni returns to Mahākaccāna with a second brief "
            "statement, this time from &ldquo;The Questions of "
            "Sakka&rdquo;: ascetics and brahmins freed by the ending "
            "of craving have reached the ultimate goal, the ultimate "
            "sanctuary from the yoke, the ultimate spiritual life, "
            "the ultimate end, and are best among gods and humans. "
            "Unlike SN 22.3's four separate images, this verse poses "
            "one compressed claim, and Mahākaccāna's answer meets it "
            "with one compressed gloss.",
        ]),
        ("The mind called \"well freed\"", [
            "Mahākaccāna's answer takes each aggregate in turn: "
            "consider any desire, greed, relishing, and craving for "
            "the form element, together with any attraction, "
            "grasping, mental fixation, insistence, and underlying "
            "tendencies toward it. With the ending, fading away, "
            "cessation, giving up, and letting go of that whole "
            "cluster, the mind is said to be well freed. The same "
            "sentence then repeats for feeling, perception, choices, "
            "and consciousness &mdash; five aggregates, one recurring "
            "formula, one recurring verdict.",
        ]),
        ("Two glosses of the same verb, side by side", [
            "Read together, SN 22.3 and SN 22.4 gloss two different "
            "things the Aṭṭhakavagga and its neighboring verse "
            "collections say about the freed mind: SN 22.3's verse "
            "described what such a person is not tied to (bastion, "
            "abode, town, expectation, argument); SN 22.4's verse "
            "describes what such a person has positively reached "
            "(the ultimate goal, sanctuary, spiritual life, end). "
            "Mahākaccāna's method stays constant across both: locate "
            "the aggregates underneath the verse's abstract praise "
            "or restraint, and show exactly what ending or absence "
            "of craving toward each one amounts to.",
        ]),
        ("A borrowed verse, not an ordinary teaching", [
            "Both of Hāliddikāni's questions share a structure worth "
            "noticing: he does not ask Mahākaccāna to teach him "
            "something new, but to explain something the Buddha "
            "already said elsewhere, in a different collection, to a "
            "different audience (Māgandiya in one case, Sakka, king "
            "of the gods, in the other). This discourse and SN 22.3 "
            "together function as a small window onto how verses "
            "traveled between collections and got unpacked in prose "
            "by name disciples once removed from their original "
            "setting.",
        ]),
    ],
    terms=[
        ("suvimuttacitta",
         "&ldquo;well freed&rdquo; mind &mdash; the verdict "
         "Mahākaccāna's gloss arrives at for each aggregate once "
         "craving toward it has fully ended."),
        ("accantaniṭṭha",
         "&ldquo;ultimate end&rdquo; &mdash; one of the four honorific "
         "titles the quoted verse gives those freed by craving's "
         "ending, alongside ultimate goal, sanctuary, and spiritual "
         "life."),
        ("yogakkhema",
         "&ldquo;sanctuary from the yoke&rdquo; &mdash; a term for "
         "safety from the bonds (sensuality, existence, views, "
         "ignorance) that yoke beings to continued wandering."),
        ("anusaya",
         "&ldquo;underlying tendency&rdquo; &mdash; part of the full "
         "cluster (alongside attraction, grasping, mental fixation, "
         "and insistence) that must end for the mind to count as "
         "well freed."),
        ("Sakkapañha",
         "&ldquo;The Questions of Sakka&rdquo; &mdash; the source "
         "collection of this discourse's quoted verse, corresponding "
         "to DN 21, originally addressed to the king of the gods."),
    ],
    text_intro=(
        "The discourse in full. One elided repetition (the "
        "aggregate-by-aggregate gloss, spelled out once for form and "
        "then compressed for the remaining four) is given exactly as "
        "bilara-data preserves it. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.4:1.1-2.1"),
        ("p", "&sect;2", "sn22.4:3.1-3.1"),
        ("p", "&sect;3", "sn22.4:4.1-4.4"),
        ("p", "&sect;4", "sn22.4:5.1-5.2"),
    ],
    quiz=[
        {"q": "Which collection is this discourse's quoted verse drawn from?",
         "opts": [
             "\"The Questions of Sakka\", corresponding to DN 21",
             "\"The Questions of Māgandiya\", from the Aṭṭhakavagga",
             "The Dhammapada",
             "The Vinaya Piṭaka"],
         "correct": 0,
         "expl": "A different source from SN 22.3's Aṭṭhakavagga verse, originally addressed to Sakka, king of the gods."},
        {"q": "What does the quoted verse claim about those freed by craving's ending?",
         "opts": [
             "They have reached the ultimate goal, sanctuary, spiritual life, and end, and are best among gods and humans",
             "They will be reborn as gods immediately",
             "They no longer need to practice meditation",
             "They become invisible to ordinary people"],
         "correct": 0,
         "expl": "Four honorific titles applied to the craving-free mind."},
        {"q": "What does Mahākaccāna's gloss identify as needing to end for the mind to be \"well freed\"?",
         "opts": [
             "Desire, greed, relishing, craving, attraction, grasping, mental fixation, insistence, and underlying tendencies toward each aggregate",
             "Only sensory contact with the outside world",
             "The physical body itself",
             "Speech and physical action alone"],
         "correct": 0,
         "expl": "A full cluster of attachment-related terms, applied aggregate by aggregate."},
        {"q": "How does this discourse's structure compare to SN 22.3's?",
         "opts": [
             "A single compressed gloss for a single compressed verse, versus four separate glosses for four images",
             "It is far longer and more elaborate than SN 22.3",
             "It rejects the method used in SN 22.3",
             "It has no relationship to SN 22.3 at all"],
         "correct": 0,
         "expl": "Same questioner, same method, applied at a smaller scale."},
        {"q": "What term names \"safety from the bonds\" that yoke beings to continued wandering?",
         "opts": [
             "Yogakkhema",
             "Suvimuttacitta",
             "Anusaya",
             "Accantaniṭṭha"],
         "correct": 0,
         "expl": "One of the four ultimate titles the verse applies to the freed."},
        {"q": "Who questions Mahākaccāna in this discourse?",
         "opts": [
             "The householder Hāliddikāni, returning a second time",
             "A newly introduced questioner unrelated to SN 22.3",
             "The Buddha himself",
             "Venerable Sāriputta"],
         "correct": 0,
         "expl": "Continuity with SN 22.3's questioner and setting."},
        {"q": "What structural pattern do SN 22.3 and SN 22.4 share?",
         "opts": [
             "A brief verse spoken elsewhere by the Buddha, quoted and then unpacked in detail by Mahākaccāna",
             "Both are entirely narrative with no verse quoted",
             "Both concern a dispute between two monks",
             "Both are addressed to a king rather than a householder"],
         "correct": 0,
         "expl": "The recurring request-and-gloss form binding this small pair together."},
        {"q": "Where does this discourse take place?",
         "opts": [
             "Steep Mountain, near Kuraraghara, in the land of the Avantis",
             "Sāvatthī, Jeta's Grove",
             "Rājagaha, Vulture's Peak",
             "Vesālī, the Great Wood"],
         "correct": 0,
         "expl": "Same setting as SN 22.3."},
        {"q": "What happens to the aggregate-by-aggregate gloss after form is spelled out in full?",
         "opts": [
             "It is elided for feeling, perception, choices, and consciousness, following the same pattern",
             "It stops entirely after form",
             "It is spelled out in full for every aggregate individually",
             "It switches to a completely different formula"],
         "correct": 0,
         "expl": "A standard peyyāla compression, preserved as-is in the source."},
        {"q": "How does the next discourse, SN 22.5, shift the topic?",
         "opts": [
             "From glossing borrowed verses to a direct teaching on developing immersion (samādhi)",
             "To a narrative about the Buddha's own past life",
             "To an unrelated discussion of monastic robes",
             "To a repeat of SN 22.4's own content"],
         "correct": 0,
         "expl": "A shift from exegesis to direct instruction, closing this small Hāliddikāni pair."},
    ],
    marginalia=[
        ("A shorter verse, a single gloss", [
            "one claim, not four images &mdash;",
            "Mahākaccāna's method at smaller scale",
        ]),
        ("Ending, not merely absence", [
            "desire, greed, relishing, craving &mdash;",
            "the full cluster named and dissolved",
        ]),
        ("Praise unpacked the same way as restraint", [
            "SN 22.3's not-tied-to &mdash;",
            "SN 22.4's positively-reached, one method",
        ]),
        ("A verse borrowed from a different audience", [
            "spoken once to Sakka &mdash;",
            "explained here to an ordinary householder",
        ]),
    ],
    further=[
        '<a href="%s/sn22.4/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.3.html">SN 22.3 &middot; With '
        "Hāliddikāni</a> &mdash; the previous discourse, the same "
        "questioner's first verse and Mahākaccāna's four-part gloss.",
        '<a href="sn-22.5.html">SN 22.5 &middot; Development of '
        "Immersion</a> &mdash; the next discourse, a direct teaching "
        "linking the aggregates to the full chain of dependent "
        "origination.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.5 — Samādhisutta
# --------------------------------------------------------------------------- #
page(
    22, 5, "Samādhi", "Development of Immersion",
    vagga="Nakulapituvagga",
    meta_title="SN 22.5 — Development of Immersion | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Samādhisutta &mdash; the Buddha ties true understanding "
        "of the five aggregates to the full twelve-link chain of "
        "dependent origination, run forward as origin and backward as "
        "ending. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's "
                    "monastery"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A direct teaching defining the origin and ending of "
                 "the five aggregates through the vocabulary of "
                 "relishing, grasping, and dependent origination"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "assumes familiarity with the twelve-link "
                       "chain from Book II's Nidānavagga"),
    ],
    why=(
        "This discourse is where Khandhavagga's own subject matter "
        "&mdash; the five aggregates &mdash; is explicitly welded "
        "onto the twelve-link chain of dependent origination that "
        "occupied the whole of Book II. The Buddha instructs the "
        "mendicants to develop immersion (samādhi), because a "
        "mendicant with immersion truly understands the origin and "
        "ending of the aggregates. What counts as their origin turns "
        "out to be the same mechanism SN 12's Nidānavagga spent nine "
        "vaggas tracing: approving, welcoming, and clinging to an "
        "aggregate gives rise to relishing; relishing is grasping; "
        "grasping conditions continued existence, continued existence "
        "conditions rebirth, and rebirth conditions the whole mass of "
        "suffering. Run the same chain without the approving and "
        "clinging, and the whole mass of suffering ceases instead. "
        "The pivot between the two books is a single word: nandi, "
        "relishing."
    ),
    guide=[
        ("A one-line instruction, then a definition of understanding", [
            "The Buddha's instruction is brief: develop immersion. Its "
            "payoff is stated just as briefly &mdash; a mendicant who "
            "has immersion truly understands, and what they truly "
            "understand is named precisely as the origin and ending "
            "of the five aggregates. The discourse does not describe "
            "immersion's technique at all; it is entirely about what "
            "immersion is claimed to make visible, not how to attain it.",
        ]),
        ("Origin: approving, welcoming, clinging", [
            "The origin of the aggregates is glossed as a mendicant "
            "approving, welcoming, and keeping clinging to them. This "
            "gives rise to relishing (nandi); relishing of an "
            "aggregate is itself grasping (upādāna); grasping is a "
            "requirement for continued existence (bhava); continued "
            "existence is a requirement for rebirth (jāti); and "
            "rebirth is a requirement for old age and death, sorrow, "
            "lamentation, pain, sadness, and distress to come to be "
            "&mdash; the same closing formula, &ldquo;this entire "
            "mass of suffering,&rdquo; that closed SN 12.3's chain "
            "in Book II.",
        ]),
        ("Ending: the identical chain, run in reverse", [
            "The ending of the aggregates is defined as the mirror "
            "image: a mendicant who does not approve, welcome, or "
            "keep clinging finds that relishing ceases as a result; "
            "when relishing ceases, grasping ceases; and the chain "
            "collapses backward through continued existence and "
            "rebirth until the entire mass of suffering ceases. "
            "Nothing about the aggregates themselves changes between "
            "the two descriptions &mdash; only whether relishing "
            "arises toward them.",
        ]),
        ("Why this discourse sits first among the vagga's teaching pair", [
            "This discourse and the one immediately after it (SN "
            "22.6) share an identical structure down to the wording, "
            "differing only in naming samādhi versus paṭisallāna "
            "(retreat) as the quality to be developed &mdash; strong "
            "evidence that in this milieu the two practices were "
            "understood to produce the same insight into the "
            "aggregates' arising and passing, whichever door a "
            "mendicant enters by.",
        ]),
    ],
    terms=[
        ("samādhi",
         "&ldquo;immersion&rdquo; &mdash; the single practice this "
         "discourse instructs mendicants to develop, said to make "
         "true understanding of the aggregates possible."),
        ("nandi",
         "&ldquo;relishing&rdquo; &mdash; the pivot word connecting "
         "approving/welcoming/clinging to full-blown grasping; the "
         "hinge between this book's aggregates and Book II's chain."),
        ("upādāna",
         "&ldquo;grasping&rdquo; &mdash; what relishing of an "
         "aggregate is said to amount to, and the link that conditions "
         "continued existence in the onward chain."),
        ("bhava",
         "&ldquo;continued existence&rdquo; &mdash; the link "
         "conditioned by grasping and itself conditioning rebirth, "
         "carried over directly from the Nidānavagga's own vocabulary."),
        ("kevalassa dukkhakkhandhassa",
         "&ldquo;this entire mass of suffering&rdquo; &mdash; the "
         "chain's closing phrase for both origin and ending, identical "
         "in wording to SN 12.3's closing phrase in Book II."),
    ],
    text_intro=(
        "The discourse in full. Two elided repetitions (the "
        "aggregate-by-aggregate expansion for both origin and "
        "ending) are given exactly as bilara-data preserves them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.5:1.1-1.7"),
        ("p", "&sect;2", "sn22.5:2.1-2.2"),
        ("p", "&sect;3", "sn22.5:3.1-3.8"),
        ("p", "&sect;4", "sn22.5:4.1-4.10"),
        ("p", "&sect;5", "sn22.5:5.1-5.5"),
        ("p", "&sect;6", "sn22.5:6.1-6.4"),
        ("p", "&sect;7", "sn22.5:7.1-8.6"),
        ("p", "&sect;8", "sn22.5:9.1-9.1"),
        ("p", "&sect;9", "sn22.5:10.1-10.2"),
        ("p", "&sect;10", "sn22.5:11.1-11.4"),
        ("p", "&sect;11", "sn22.5:12.1-12.1"),
    ],
    quiz=[
        {"q": "What does the Buddha instruct the mendicants to develop in this discourse?",
         "opts": [
             "Immersion (samādhi)",
             "Generosity toward laypeople",
             "Memorization of the discourses",
             "Physical endurance"],
         "correct": 0,
         "expl": "The discourse's sole instruction, with true understanding of the aggregates as its stated payoff."},
        {"q": "What does a mendicant with immersion truly understand, according to this discourse?",
         "opts": [
             "The origin and ending of form, feeling, perception, choices, and consciousness",
             "The precise date of their own death",
             "The location of hidden treasure",
             "Foreign languages"],
         "correct": 0,
         "expl": "Named directly and precisely, without further elaboration on the technique of immersion itself."},
        {"q": "What gives rise to the origin of the aggregates, according to this discourse?",
         "opts": [
             "Approving, welcoming, and keeping clinging to them",
             "Simply perceiving them with the senses",
             "Physical old age",
             "External weather conditions"],
         "correct": 0,
         "expl": "This triad of approving/welcoming/clinging gives rise to relishing, the chain's first true pivot."},
        {"q": "What is \"relishing\" (nandi) of an aggregate said to be, in this discourse's chain?",
         "opts": [
             "Grasping (upādāna)",
             "Old age and death directly",
             "A form of physical pleasure only",
             "Unrelated to the aggregates"],
         "correct": 0,
         "expl": "The pivot equation connecting the aggregates directly to the dependent-origination chain."},
        {"q": "What happens to the chain when a mendicant does not approve, welcome, or cling?",
         "opts": [
             "Relishing ceases, and the chain collapses backward until the entire mass of suffering ceases",
             "The aggregates themselves disappear entirely",
             "Nothing changes at all",
             "A new, different chain begins"],
         "correct": 0,
         "expl": "The mirror image of the origin chain, run in reverse rather than describing a different mechanism."},
        {"q": "How does this discourse connect to Book II (Nidānavagga), which the site completed just before Khandhavagga?",
         "opts": [
             "It uses the same twelve-link chain and closing formula, now applied explicitly to the five aggregates",
             "It explicitly rejects Book II's teaching on dependent origination",
             "It has no connection to Book II at all",
             "It only mentions Book II by name without using its content"],
         "correct": 0,
         "expl": "Nandi (relishing) is the hinge word linking the two books' subject matter directly."},
        {"q": "What is the discourse's closing phrase for both the origin and ending of suffering?",
         "opts": [
             "\"This entire mass of suffering\"",
             "\"The eternal wheel of becoming\"",
             "\"The realm of the gods\"",
             "\"The path beyond return\""],
         "correct": 0,
         "expl": "Identical in wording to SN 12.3's closing phrase from Book II."},
        {"q": "How does this discourse's structure compare to the discourse immediately after it, SN 22.6?",
         "opts": [
             "Nearly identical in wording, differing mainly in naming samādhi versus paṭisallāna (retreat) as the quality to develop",
             "Completely unrelated in both wording and content",
             "SN 22.6 explicitly contradicts this discourse",
             "SN 22.6 is far longer and more detailed"],
         "correct": 0,
         "expl": "SN 22.6 is in fact a peyyāla stub explicitly referring back to this discourse for its full wording."},
        {"q": "Where does this discourse take place?",
         "opts": [
             "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's monastery",
             "Steep Mountain, near Kuraraghara",
             "Devadaha, in the land of the Sakyans",
             "Rājagaha, Vulture's Peak"],
         "correct": 0,
         "expl": "The default setting for most of this saṃyutta's discourses, resuming after two set elsewhere."},
        {"q": "Who is the sole speaker in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "Venerable Mahākaccāna",
             "The householder Hāliddikāni"],
         "correct": 0,
         "expl": "A shift back to direct instruction after two discourses of disciple-led exegesis."},
    ],
    marginalia=[
        ("One instruction, one stated payoff", [
            "develop immersion &mdash;",
            "true understanding of the aggregates follows",
        ]),
        ("Relishing: the hinge word", [
            "aggregates on one side &mdash;",
            "the whole twelve-link chain on the other",
        ]),
        ("Same chain, opposite direction", [
            "clinging builds it up &mdash;",
            "not clinging collapses it the same way",
        ]),
        ("A closing phrase carried over from Book II", [
            "this entire mass of suffering &mdash;",
            "identical wording, new subject matter",
        ]),
    ],
    further=[
        '<a href="%s/sn22.5/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.4.html">SN 22.4 &middot; Hāliddikāni '
        "(2nd)</a> &mdash; the previous discourse, closing this "
        "vagga's pair of exegetical dialogues.",
        '<a href="sn-22.6.html">SN 22.6 &middot; Retreat</a> '
        "&mdash; the next discourse, an almost word-for-word "
        "companion naming paṭisallāna instead of samādhi.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.6 — Paṭisallāṇasutta
# --------------------------------------------------------------------------- #
page(
    22, 6, "Paṭisallāṇa", "Retreat",
    vagga="Nakulapituvagga",
    meta_title="SN 22.6 — Retreat | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭisallāṇasutta &mdash; a brief companion to SN 22.5, "
        "naming solitary retreat rather than immersion, and pointing "
        "back to the previous discourse for its full wording. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A peyyāla stub &mdash; the opening line only, with "
                 "the source itself instructing readers to fill in "
                 "the rest from the previous discourse"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the shortest discourse in this vagga, "
                       "understood only alongside SN 22.5"),
    ],
    why=(
        "This is one of the plainest peyyāla stubs in the collection: "
        "bilara-data preserves only the opening line &mdash; develop "
        "retreat (paṭisallāna); a mendicant in retreat truly "
        "understands; what do they truly understand; the origin and "
        "ending of the five aggregates &mdash; followed by a direct "
        "editorial instruction, &ldquo;tell in full as in the "
        "previous discourse.&rdquo; Nothing is fabricated to fill the "
        "gap here; the discourse is read exactly as short as the "
        "source leaves it, because its brevity is itself the point "
        "worth noticing: whoever assembled this pair of discourses "
        "considered paṭisallāna's full explanation so identical to "
        "samādhi's that writing it out twice was unnecessary."
    ),
    guide=[
        ("A single swapped word, and an editorial shortcut", [
            "The discourse opens with the same four-part structure "
            "as SN 22.5 &mdash; instruction, claim of true "
            "understanding, question, and the aggregates named as "
            "the answer &mdash; but swaps paṭisallāna (retreat) in "
            "for samādhi (immersion) as the quality to be developed. "
            "Rather than restating the rest of the chain (approving, "
            "welcoming, clinging, relishing, grasping, and onward), "
            "the source simply instructs the reader: tell in full as "
            "in the previous discourse.",
        ]),
        ("What the editorial note itself reveals", [
            "This kind of instruction, &ldquo;tell in full as in the "
            "previous discourse,&rdquo; is a genuine feature of how "
            "this material was preserved and transmitted, not an "
            "editorial addition made for this website. It appears "
            "elsewhere in the canon wherever reciters judged that two "
            "discourses shared identical content apart from one "
            "swapped term, and it is quoted here exactly as the "
            "source gives it rather than expanded into invented "
            "prose, matching this project's practice with other "
            "short peyyāla stubs encountered earlier in the "
            "Saṃyutta Nikāya.",
        ]),
        ("Immersion and retreat, treated as functionally equivalent", [
            "Taken together with SN 22.5, this discourse's brevity "
            "makes an implicit claim worth sitting with: that "
            "developing immersion and developing solitary retreat "
            "were understood, at least by whoever paired these two "
            "discourses, to deliver the identical result &mdash; true "
            "understanding of how the five aggregates arise and "
            "cease. The practices are named separately, but the "
            "insight they unlock is treated as one and the same.",
        ]),
        ("A companion pair closing before the vagga's midpoint", [
            "With this discourse, the vagga has now paired its "
            "central teaching (SN 22.5's aggregates-and-dependent-"
            "origination chain) with a matching restatement, before "
            "moving on to the different diagnostic vocabulary of "
            "anxiety and grasping in SN 22.7 and SN 22.8. The "
            "pairing device itself &mdash; full statement, then a "
            "one-word-swapped stub &mdash; recurs elsewhere in this "
            "saṃyutta and is worth watching for.",
        ]),
    ],
    terms=[
        ("paṭisallāna",
         "&ldquo;retreat&rdquo; or &ldquo;seclusion&rdquo; &mdash; "
         "the quality this discourse instructs mendicants to develop, "
         "standing in for samādhi from the previous discourse."),
        ("peyyāla",
         "the formal term for a passage the source itself elides, "
         "instructing the reciter or reader to supply the full "
         "wording from elsewhere &mdash; exactly what this discourse "
         "consists of."),
        ("vitthāretabbaṁ",
         "&ldquo;should be told in full&rdquo; &mdash; the closing "
         "editorial instruction's operative verb, directing readers "
         "back to SN 22.5."),
        ("purimasuttasadisaṁ",
         "&ldquo;like the previous discourse&rdquo; &mdash; the sense "
         "of the closing instruction, even though the exact Pali "
         "wording given in translation is the shorter &ldquo;tell in "
         "full as in the previous discourse.&rdquo;"),
        ("samādhi",
         "&ldquo;immersion&rdquo; &mdash; the term this discourse "
         "replaces with paṭisallāna, carried over by cross-reference "
         "rather than restated, from SN 22.5."),
    ],
    text_intro=(
        "The discourse in full &mdash; genuinely this short in the "
        "source, including its closing editorial instruction, given "
        "exactly as bilara-data preserves it rather than expanded. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.6:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does this discourse instruct mendicants to develop, in place of SN 22.5's samādhi?",
         "opts": [
             "Retreat (paṭisallāna)",
             "Generosity",
             "Physical strength",
             "Skill in debate"],
         "correct": 0,
         "expl": "The one substantive change from the previous discourse's wording."},
        {"q": "How does the source itself handle the rest of the discourse's content?",
         "opts": [
             "With an explicit editorial note: \"tell in full as in the previous discourse\"",
             "By spelling out the entire chain a second time in full",
             "By omitting any indication that content is missing",
             "By replacing it with an entirely unrelated teaching"],
         "correct": 0,
         "expl": "A genuine transmission feature, not an omission introduced by this reading guide."},
        {"q": "What does this reading guide do with the editorial shortcut, rather than filling in the missing content itself?",
         "opts": [
             "Quotes it exactly as the source gives it, without fabricating the elided material",
             "Reconstructs the full chain from SN 22.5 and presents it as this discourse's own text",
             "Skips the discourse entirely",
             "Invents new content unrelated to SN 22.5"],
         "correct": 0,
         "expl": "Consistent with this project's practice on other short peyyāla stubs elsewhere in the Saṃyutta Nikāya."},
        {"q": "What does a mendicant \"in retreat\" truly understand, according to this discourse's stated claim?",
         "opts": [
             "The origin and ending of form, feeling, perception, choices, and consciousness",
             "The exact hour of their future death",
             "Foreign customs and languages",
             "The layout of distant monasteries"],
         "correct": 0,
         "expl": "Identical wording to SN 22.5's claim, just with paṭisallāna substituted for samādhi."},
        {"q": "What does this discourse's brevity implicitly suggest about immersion and retreat?",
         "opts": [
             "That developing either one was understood to deliver the identical insight into the aggregates",
             "That retreat is a lesser, incomplete version of immersion",
             "That the two practices are entirely unrelated",
             "That retreat was considered more important than immersion"],
         "correct": 0,
         "expl": "Pairing the two under one shared explanation treats them as functionally equivalent here."},
        {"q": "What formal term describes a passage the source elides and instructs the reader to fill in from elsewhere?",
         "opts": [
             "Peyyāla",
             "Uddāna",
             "Vagga",
             "Nikāya"],
         "correct": 0,
         "expl": "The technical term for exactly this kind of compression, seen throughout the Saṃyutta and Aṅguttara Nikāyas."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Steep Mountain, near Kuraraghara",
             "Devadaha",
             "Rājagaha"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.5."},
        {"q": "How does this discourse's pairing device (full statement, then a one-word-swapped stub) relate to the rest of the saṃyutta?",
         "opts": [
             "It recurs elsewhere in the saṃyutta and is worth watching for again",
             "It appears nowhere else in the entire Saṃyutta Nikāya",
             "It is unique to Khandhavagga among all five books",
             "It only ever appears once, in this exact pair"],
         "correct": 0,
         "expl": "A structural device the reading guide flags for recognition in later vaggas."},
        {"q": "What comes immediately after this discourse in the vagga?",
         "opts": [
             "SN 22.7, shifting to the diagnostic vocabulary of anxiety caused by grasping",
             "SN 22.1, looping back to the vagga's opening discourse",
             "A discourse from an entirely different saṃyutta",
             "The vagga's closing uddāna, with no further discourses"],
         "correct": 0,
         "expl": "A change in topic and vocabulary, moving from origin/ending to anxiety and grasping."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "The householder Hāliddikāni",
             "Venerable Mahākaccāna"],
         "correct": 0,
         "expl": "Consistent with SN 22.5, a direct teaching rather than a disciple-led dialogue."},
    ],
    marginalia=[
        ("One word swapped, nothing else restated", [
            "retreat in place of immersion &mdash;",
            "the rest simply pointed back to SN 22.5",
        ]),
        ("A genuine feature of transmission, not an omission", [
            "\"tell in full as before\" &mdash;",
            "reciters' own shorthand, preserved as-is",
        ]),
        ("Brevity itself as the content worth noting", [
            "the shortest page in this vagga &mdash;",
            "its shortness is the finding, not a gap",
        ]),
        ("Two practices, one claimed result", [
            "immersion or retreat &mdash;",
            "either door opens onto the same understanding",
        ]),
    ],
    further=[
        '<a href="%s/sn22.6/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.5.html">SN 22.5 &middot; Development of '
        "Immersion</a> &mdash; the discourse this one's editorial "
        "note points back to for its full wording.",
        '<a href="sn-22.7.html">SN 22.7 &middot; Anxiety Because of '
        "Grasping</a> &mdash; the next discourse, shifting to a new "
        "diagnostic vocabulary for the same five aggregates.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.7 — Upādāparitassanāsutta
# --------------------------------------------------------------------------- #
page(
    22, 7, "Upādāparitassanā", "Anxiety Because of Grasping",
    vagga="Nakulapituvagga",
    meta_title="SN 22.7 — Anxiety Because of Grasping | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Upādāparitassanāsutta &mdash; the classic fourfold "
        "formula for self-identification with each aggregate, and "
        "how it produces anxiety the moment that aggregate decays. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A direct teaching contrasting an unlearned ordinary "
                 "person and a learned noble disciple, using an "
                 "identical fourfold formula applied to each of the "
                 "five aggregates"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "the classic twenty-fold identity-view formula, "
                       "compressed here to one instance per aggregate"),
    ],
    why=(
        "This discourse gives one of the most structurally important "
        "formulas in the entire aggregates literature: the four ways "
        "a person can identify with any given aggregate &mdash; "
        "regarding it as self, self as possessing it, it as within "
        "self, or self as within it. Applied across all five "
        "aggregates, this produces the famous twenty varieties of "
        "identity view (sakkāyadiṭṭhi) referenced throughout the "
        "canon, though this discourse states the formula once per "
        "aggregate rather than spelling out all twenty variants "
        "individually. What makes the discourse more than a doctrinal "
        "list is its diagnosis of consequence: an aggregate held in "
        "any of these four ways will still decay, and when it does, "
        "consciousness &ldquo;latches on&rdquo; to that decay, "
        "producing the anxiety named in the title. Remove the "
        "identification, and the identical decay produces no such "
        "anxiety."
    ),
    guide=[
        ("A promise to teach both directions at once", [
            "The Buddha opens by naming his subject precisely: how "
            "grasping leads to anxiety, and how not grasping leads to "
            "freedom from anxiety. The two halves of the discourse "
            "that follow are built as strict mirror images of each "
            "other, sentence for sentence, so that the mechanism "
            "producing anxiety and the mechanism producing its "
            "absence can be compared directly rather than described "
            "separately.",
        ]),
        ("The fourfold formula for identifying with an aggregate", [
            "An unlearned ordinary person &mdash; one who has not "
            "seen the noble ones or been trained in their teaching "
            "&mdash; regards form as self, self as having form, form "
            "in self, or self in form. This same four-part formula "
            "then applies in turn to feeling, perception, choices, "
            "and consciousness. It is the canon's standard analysis "
            "of how identity view can attach to any one of the five "
            "aggregates in four distinct configurations.",
        ]),
        ("Decay is certain; the anxiety is not", [
            "Whichever of the four configurations someone holds, the "
            "aggregate in question decays and perishes regardless "
            "&mdash; the discourse does not claim identification "
            "prevents decay. What identification produces is a "
            "specific downstream event: consciousness &ldquo;latches "
            "on&rdquo; to that perishing, and anxieties born of this "
            "latching, arising in accordance with natural principles, "
            "occupy the mind. The result is fear, worry, concern, and "
            "anxiety &mdash; not because the aggregate perished, but "
            "because consciousness was still attached when it did.",
        ]),
        ("The identical decay, without the identification", [
            "A learned noble disciple who has seen the noble ones "
            "does not regard any aggregate in any of the four ways. "
            "When that same aggregate decays and perishes &mdash; the "
            "decay itself is not denied or avoided &mdash; "
            "consciousness does not latch on to the perishing, no "
            "anxieties occupy the mind, and no fear, worry, concern, "
            "or anxiety follows. The discourse's entire argument turns "
            "on this precise point: the event (decay) is held "
            "constant across both halves, and only the presence or "
            "absence of identification changes the outcome.",
        ]),
    ],
    terms=[
        ("rūpaṁ attato samanupassati",
         "&ldquo;regards form as self&rdquo; &mdash; the first of "
         "four configurations in the identity-view formula, repeated "
         "for each of the five aggregates."),
        ("attānaṁ vā rūpavantaṁ",
         "&ldquo;self as having form&rdquo; &mdash; the formula's "
         "second configuration, distinct from simple identification."),
        ("upādāya paritassanā",
         "&ldquo;anxiety because of grasping&rdquo; &mdash; this "
         "discourse's title phrase, naming the specific downstream "
         "consequence the whole teaching is built to explain."),
        ("upāyāso",
         "&ldquo;distress&rdquo; &mdash; the last item in the closing "
         "list of reactions (frightened, worried, concerned, and "
         "anxious) that follows from consciousness latching on to an "
         "aggregate's perishing."),
        ("dhammatā",
         "&ldquo;natural principle&rdquo; &mdash; the standard the "
         "discourse invokes for why these anxieties arise as they "
         "do, once identification and decay coincide."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same fourfold "
        "formula spelled out in full for form and consciousness) are "
        "given exactly as bilara-data preserves them. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.7:1.1-1.5"),
        ("p", "&sect;2", "sn22.7:2.1-2.7"),
        ("p", "&sect;3", "sn22.7:3.1-4.2"),
        ("p", "&sect;4", "sn22.7:5.1-5.6"),
        ("p", "&sect;5", "sn22.7:6.1-6.7"),
        ("p", "&sect;6", "sn22.7:7.1-8.2"),
        ("p", "&sect;7", "sn22.7:9.1-9.6"),
    ],
    quiz=[
        {"q": "What two things does the Buddha announce he will teach at the start of this discourse?",
         "opts": [
             "How grasping leads to anxiety, and how not grasping leads to freedom from anxiety",
             "How to gain psychic powers",
             "The history of the monastic order",
             "How to resolve disputes between monks"],
         "correct": 0,
         "expl": "The two mirror-image halves that structure the entire discourse."},
        {"q": "What is the fourfold formula an unlearned ordinary person applies to an aggregate?",
         "opts": [
             "Regarding it as self, self as having it, it in self, or self in it",
             "Regarding it as permanent, impermanent, both, or neither",
             "Regarding it as pleasant, painful, neutral, or unknown",
             "Regarding it as physical, mental, both, or neither"],
         "correct": 0,
         "expl": "The classic fourfold identity-view configuration, applied here to each of the five aggregates."},
        {"q": "According to this discourse, does identifying with an aggregate prevent its decay?",
         "opts": [
             "No — the aggregate decays and perishes regardless of identification",
             "Yes — identification permanently stabilizes the aggregate",
             "Only for aggregates other than form",
             "The discourse does not address this question"],
         "correct": 0,
         "expl": "Decay is held constant; only the presence of anxiety changes."},
        {"q": "What does consciousness do when an identified-with aggregate decays, according to this discourse?",
         "opts": [
             "It \"latches on\" to the perishing, giving rise to anxieties",
             "It immediately ceases to exist",
             "It transfers into a different aggregate",
             "It becomes permanently stable"],
         "correct": 0,
         "expl": "This latching is the precise mechanism the discourse identifies as producing anxiety."},
        {"q": "What happens when a learned noble disciple's aggregate decays, since they do not identify with it?",
         "opts": [
             "Consciousness does not latch on to the perishing, and no anxiety arises",
             "The aggregate does not decay at all",
             "A different, worse form of anxiety arises instead",
             "The disciple becomes unconscious"],
         "correct": 0,
         "expl": "The decay is identical; only the absence of identification changes the outcome."},
        {"q": "What standard does the discourse invoke for why these anxieties arise?",
         "opts": [
             "Dhammatā, \"natural principle\"",
             "Royal decree",
             "Ancient custom alone",
             "Random chance"],
         "correct": 0,
         "expl": "A recurring appeal to lawlike regularity rather than arbitrary punishment."},
        {"q": "Who is contrasted with the unlearned ordinary person in this discourse?",
         "opts": [
             "A learned noble disciple who has seen the noble ones and trained in their teaching",
             "A king",
             "A different unlearned ordinary person",
             "An animal"],
         "correct": 0,
         "expl": "The discourse's structural contrast, mirrored sentence for sentence across both halves."},
        {"q": "How many aggregates does the fourfold formula apply to in this discourse?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only form and consciousness"],
         "correct": 0,
         "expl": "Form and consciousness are spelled out in full; feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "How does this discourse relate to the paired discourse immediately after it, SN 22.8?",
         "opts": [
             "Both share the same title and topic, but SN 22.8 uses a simpler three-phrase formula instead of the fourfold one",
             "SN 22.8 is entirely unrelated in content",
             "SN 22.8 directly refutes this discourse's claims",
             "SN 22.8 is a much longer, more elaborate version of this discourse"],
         "correct": 0,
         "expl": "A matched pair using two different but related diagnostic formulas for the same underlying claim."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Steep Mountain, near Kuraraghara",
             "Devadaha",
             "Rājagaha"],
         "correct": 0,
         "expl": "The default setting resumed after SN 22.2 through 22.4's other locations."},
    ],
    marginalia=[
        ("A twenty-fold formula, compressed to one pass each", [
            "self, has, in-self, self-in &mdash;",
            "one instance per aggregate, not all twenty spelled out",
        ]),
        ("Decay held constant across both halves", [
            "the aggregate perishes either way &mdash;",
            "only the anxiety differs",
        ]),
        ("\"Latches on\": the precise mechanism named", [
            "not decay itself &mdash;",
            "consciousness's grip on the decaying",
        ]),
        ("Two mirror halves, sentence for sentence", [
            "unlearned person, then noble disciple &mdash;",
            "identical structure, opposite outcome",
        ]),
    ],
    further=[
        '<a href="%s/sn22.7/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.6.html">SN 22.6 &middot; Retreat</a> '
        "&mdash; the previous discourse, closing the vagga's "
        "immersion/retreat teaching pair.",
        '<a href="sn-22.8.html">SN 22.8 &middot; Anxiety Because of '
        "Grasping (2nd)</a> &mdash; the next discourse, the same "
        "diagnosis restated with a simpler three-phrase formula.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.8 — Dutiyaupādāparitassanāsutta
# --------------------------------------------------------------------------- #
page(
    22, 8, "Dutiyaupādāparitassanā", "Anxiety Because of Grasping (2nd)",
    vagga="Nakulapituvagga",
    meta_title="SN 22.8 — Anxiety Because of Grasping (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaupādāparitassanāsutta &mdash; the same diagnosis "
        "as SN 22.7, restated with the shorter \"this is mine, I am "
        "this, this is my self\" formula. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A direct restatement of SN 22.7's contrast, using "
                 "a shorter three-phrase formula in place of the "
                 "previous discourse's fourfold one"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "shorter and more direct than SN 22.7, though "
                       "best read as its companion"),
    ],
    why=(
        "This discourse makes the same claim as SN 22.7 &mdash; "
        "grasping leads to anxiety, freedom from grasping leads to "
        "freedom from anxiety &mdash; but reaches it through a "
        "shorter, more colloquial formula: &ldquo;this is mine, I am "
        "this, this is my self,&rdquo; applied to each aggregate in "
        "turn. Where SN 22.7 spelled out the technical four-way "
        "logical structure of identity view, this discourse gives the "
        "same underlying attitude in the plain first-person voice a "
        "person might actually use about their own body or mind. Read "
        "together, the pair shows the aggregates literature working "
        "at two registers at once: a precise doctrinal formula for "
        "analysis, and an ordinary self-talk formula for recognition "
        "in daily experience."
    ),
    guide=[
        ("The same two-part promise, restated", [
            "As in SN 22.7, the Buddha opens by naming both halves of "
            "his subject together: how grasping leads to anxiety, and "
            "how not grasping leads to freedom from anxiety. The "
            "repetition of this exact framing across two consecutive "
            "discourses signals that what follows is a deliberate "
            "restatement, not a new topic.",
        ]),
        ("\"This is mine, I am this, this is my self\"", [
            "An unlearned ordinary person regards each aggregate with "
            "this three-part claim: mama (mine, a claim of "
            "possession), eso'ham asmi (I am this, a claim of "
            "identity), and eso me attā (this is my self, a claim of "
            "essential selfhood). The three phrases are not presented "
            "as logically distinct configurations the way SN 22.7's "
            "fourfold formula was; they read instead as three ways of "
            "voicing the same underlying grip.",
        ]),
        ("A more direct route to the same sorrow", [
            "When an aggregate held with this claim decays and "
            "perishes, the result named here is simply &ldquo;sorrow, "
            "lamentation, pain, sadness, and distress&rdquo; &mdash; "
            "the discourse skips SN 22.7's intermediate step of "
            "consciousness &ldquo;latching on&rdquo; to the "
            "perishing, moving straight from the claim to its painful "
            "consequence. This is a shorter causal account than SN "
            "22.7's, not a contradictory one.",
        ]),
        ("Two formulas, one lesson repeated at two speeds", [
            "A learned noble disciple regards each aggregate with the "
            "negated version &mdash; &ldquo;this is not mine, I am "
            "not this, this is not my self&rdquo; &mdash; and when "
            "that aggregate decays, no sorrow, lamentation, pain, "
            "sadness, or distress arises. Placed immediately after SN "
            "22.7, this discourse functions as a compressed, more "
            "memorable version of the same lesson, well suited to "
            "recitation or to a listener less prepared for SN 22.7's "
            "more technical fourfold analysis.",
        ]),
    ],
    terms=[
        ("etaṁ mama",
         "&ldquo;this is mine&rdquo; &mdash; the first of the three "
         "phrases, a claim of possession over an aggregate."),
        ("esohamasmi",
         "&ldquo;I am this&rdquo; &mdash; the second phrase, a claim "
         "of direct identity rather than mere possession."),
        ("eso me attā",
         "&ldquo;this is my self&rdquo; &mdash; the third phrase, a "
         "claim of essential, core selfhood."),
        ("sokaparidevadukkhadomanassupāyāsā",
         "&ldquo;sorrow, lamentation, pain, sadness, and distress&rdquo; "
         "&mdash; the standard compound naming the consequence that "
         "follows directly from the threefold claim, once its object "
         "decays."),
        ("n'etaṁ mama, nesohamasmi, na meso attā",
         "&ldquo;this is not mine, I am not this, this is not my "
         "self&rdquo; &mdash; the negated formula the learned noble "
         "disciple applies instead, producing the discourse's "
         "opposite outcome."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same threefold "
        "formula spelled out in full for form and consciousness) are "
        "given exactly as bilara-data preserves them. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.8:1.1-1.7"),
        ("p", "&sect;2", "sn22.8:1.8-1.14"),
        ("p", "&sect;3", "sn22.8:2.1-2.4"),
        ("p", "&sect;4", "sn22.8:2.5-2.11"),
    ],
    quiz=[
        {"q": "What three-phrase formula does an unlearned ordinary person apply to each aggregate in this discourse?",
         "opts": [
             "\"This is mine, I am this, this is my self\"",
             "\"This is permanent, stable, and reliable\"",
             "\"This is pleasant, desirable, and worth keeping\"",
             "\"This belongs to the community, not to me\""],
         "correct": 0,
         "expl": "A shorter, more colloquial formula than SN 22.7's four-way configuration."},
        {"q": "How does this discourse's causal account differ from SN 22.7's?",
         "opts": [
             "It moves directly from the claim to sorrow and distress, skipping SN 22.7's step of consciousness \"latching on\"",
             "It denies that decay causes any suffering at all",
             "It claims a completely different aggregate is responsible",
             "It reverses SN 22.7's conclusion entirely"],
         "correct": 0,
         "expl": "A shorter causal chain, not a contradictory one — the discourses complement rather than conflict."},
        {"q": "What formula does the learned noble disciple use instead?",
         "opts": [
             "\"This is not mine, I am not this, this is not my self\"",
             "\"This is mine, but only temporarily\"",
             "\"This is neither mine nor not mine\"",
             "\"This is beyond description\""],
         "correct": 0,
         "expl": "The direct negation of the ordinary person's threefold claim."},
        {"q": "What happens when a noble disciple's aggregate decays, given the negated formula?",
         "opts": [
             "No sorrow, lamentation, pain, sadness, or distress arises",
             "A different, milder form of sorrow arises",
             "The aggregate does not decay",
             "The disciple becomes anxious about the decay of others"],
         "correct": 0,
         "expl": "The mirror-image outcome to the ordinary person's suffering."},
        {"q": "What relationship does this discourse have to SN 22.7?",
         "opts": [
             "A restatement of the same claim using a shorter, more colloquial formula",
             "A direct refutation of SN 22.7's conclusions",
             "An entirely unrelated topic placed nearby by coincidence",
             "A narrative sequel describing what happened after SN 22.7"],
         "correct": 0,
         "expl": "Both discourses share the same title, opening framing, and underlying claim."},
        {"q": "What does \"esohamasmi\" mean?",
         "opts": [
             "\"I am this\"",
             "\"This is mine\"",
             "\"This is my self\"",
             "\"This is not mine\""],
         "correct": 0,
         "expl": "The second of the three claims, distinct from mere possession."},
        {"q": "How many aggregates does the threefold formula apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only feeling and perception",
             "Only consciousness"],
         "correct": 0,
         "expl": "Form and consciousness are spelled out in full; feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Steep Mountain, near Kuraraghara",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.7."},
        {"q": "What register does this discourse's formula read in, compared to SN 22.7's?",
         "opts": [
             "A plainer, first-person voice, closer to ordinary self-talk than SN 22.7's technical logical structure",
             "A far more abstract and technical register than SN 22.7",
             "An identical register, word for word",
             "A poetic, verse-based register"],
         "correct": 0,
         "expl": "The pair works at two different registers on the same underlying claim."},
        {"q": "What follows this discourse, closing the vagga's middle section?",
         "opts": [
             "SN 22.9, the first of a three-discourse set on impermanence, suffering, and not-self across past, present, and future",
             "A return to SN 22.2's rehearsal format",
             "The vagga's closing uddāna",
             "A discourse from an entirely different saṃyutta"],
         "correct": 0,
         "expl": "A shift to a new triplet closing out Nakulapituvagga."},
    ],
    marginalia=[
        ("Four configurations, or three plain phrases", [
            "SN 22.7's logical structure &mdash;",
            "this discourse's ordinary first-person voice",
        ]),
        ("A shorter causal chain to the same sorrow", [
            "claim straight to distress &mdash;",
            "no intermediate \"latching on\" named",
        ]),
        ("Negation as the entire remedy", [
            "not mine, not I, not self &mdash;",
            "three words reversed, one outcome reversed",
        ]),
        ("A pair working at two speeds", [
            "technical analysis, then plain recitation &mdash;",
            "same lesson, two registers",
        ]),
    ],
    further=[
        '<a href="%s/sn22.8/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.7.html">SN 22.7 &middot; Anxiety Because of '
        "Grasping</a> &mdash; the previous discourse, the same claim "
        "in its fuller fourfold formula.",
        '<a href="sn-22.9.html">SN 22.9 &middot; Impermanence in the '
        "Three Times</a> &mdash; the next discourse, opening a new "
        "triplet on the three marks across past, present, and future.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.9 — Kālattayaaniccasutta
# --------------------------------------------------------------------------- #
page(
    22, 9, "Kālattayaanicca", "Impermanence in the Three Times",
    vagga="Nakulapituvagga",
    meta_title="SN 22.9 — Impermanence in the Three Times | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kālattayaaniccasutta &mdash; the first of a closing "
        "triplet, arguing that past and future aggregates are "
        "impermanent, let alone the present. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A compact a fortiori argument, run once for each of "
                 "the five aggregates, opening a three-discourse set "
                 "that closes the vagga"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a short, tightly patterned argument, easy to "
                       "follow once its logical shape is seen"),
    ],
    why=(
        "This discourse opens the vagga's closing triplet, and its "
        "argument has a distinctive shape worth noticing on its own "
        "terms: rather than simply asserting that the aggregates are "
        "impermanent, it argues from the stronger case to the weaker "
        "one. Past and future form is impermanent &mdash; "
        "&ldquo;let alone the present.&rdquo; If even form already "
        "gone or not yet arisen counts as impermanent, present form, "
        "actually here and changing in front of one, is impermanence "
        "even more obviously. This same a fortiori structure then "
        "governs the two discourses that follow, applied to suffering "
        "and to not-self in turn, closing Nakulapituvagga with the "
        "three marks (tilakkhaṇa) run once each across all three "
        "times."
    ),
    guide=[
        ("An argument, not just an assertion", [
            "The discourse's key move is grammatical as much as "
            "doctrinal: &ldquo;form of the past and future is "
            "impermanent, let alone the present&rdquo; (pageva "
            "paccuppannassa) argues from a claim about the "
            "less-obviously-relevant cases (past, future) to the "
            "more obviously relevant one (present), rather than the "
            "reverse. A listener who might resist a direct claim "
            "about their present experience is first walked through "
            "the less contentious cases of what is already gone and "
            "what has not yet come.",
        ]),
        ("What follows from seeing this", [
            "A learned noble disciple who sees this threefold "
            "impermanence responds with three specific practices, "
            "named in sequence: not being concerned with past form, "
            "not looking forward to enjoying future form, and "
            "practicing for disillusionment, dispassion, and "
            "cessation regarding present form. Each of the three "
            "times gets its own distinct practical response, not one "
            "generic attitude applied uniformly.",
        ]),
        ("The same argument, run for all five aggregates", [
            "The discourse repeats this exact structure &mdash; "
            "impermanence claim, then the three practices &mdash; "
            "for feeling, perception, and choices (elided in the "
            "source, following the pattern already spelled out for "
            "form), before spelling consciousness out in full again "
            "at the close. The repetition itself is part of the "
            "point: the same reasoning applies uniformly across all "
            "five aggregates, with no exception carved out for any "
            "one of them.",
        ]),
        ("A closing triplet built on the three marks", [
            "This discourse, together with SN 22.10 and SN 22.11 "
            "immediately after it, forms a matched set applying the "
            "identical &ldquo;past and future&hellip;let alone the "
            "present&rdquo; argument to each of the three marks in "
            "turn: impermanence here, suffering next, not-self last. "
            "The three discourses share every word of their structure "
            "apart from the single term that changes, making the set "
            "easiest to read together rather than in isolation.",
        ]),
    ],
    terms=[
        ("atītānāgataṁ&hellip;anicca",
         "&ldquo;past and future&hellip;is impermanent&rdquo; &mdash; "
         "the discourse's opening claim, deliberately about the two "
         "times other than the present."),
        ("pageva paccuppannassa",
         "&ldquo;let alone the present&rdquo; &mdash; the argument's "
         "hinge phrase, moving from the less contentious past/future "
         "claim to the more directly relevant present case."),
        ("anapekkho",
         "&ldquo;not concerned with&rdquo; &mdash; the practice "
         "recommended toward past form, once its impermanence is "
         "seen."),
        ("nābhinandati",
         "&ldquo;doesn't look forward to enjoying&rdquo; &mdash; the "
         "practice recommended toward future form, distinct from the "
         "practice recommended toward the past."),
        ("nibbidāya virāgāya nirodhāya",
         "&ldquo;for disillusionment, dispassion, and cessation&rdquo; "
         "&mdash; the standard three-part practice recommended toward "
         "present form specifically, not toward past or future form."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same argument "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.9:1.1-1.9"),
        ("p", "&sect;2", "sn22.9:1.14-1.18"),
    ],
    quiz=[
        {"q": "What argument structure does this discourse use for form's impermanence?",
         "opts": [
             "Past and future form is impermanent, \"let alone\" the more obviously relevant present",
             "Only present form is discussed, with no mention of past or future",
             "Future form alone is claimed to be impermanent",
             "The discourse denies that form is impermanent at all"],
         "correct": 0,
         "expl": "An a fortiori move from the less contentious cases to the more directly relevant one."},
        {"q": "What three practices does a learned noble disciple take up toward form, once its impermanence is seen?",
         "opts": [
             "Not concerned with past form, not looking forward to future form, and practicing for disillusionment regarding present form",
             "Avoiding all contact with form entirely",
             "Memorizing every past instance of form",
             "Predicting exactly what future form will look like"],
         "correct": 0,
         "expl": "Each of the three times receives a distinct practical response."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and feeling",
             "Only consciousness"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided in the source but follow the same pattern spelled out for form and consciousness."},
        {"q": "What relationship does this discourse have to SN 22.10 and SN 22.11?",
         "opts": [
             "A matched triplet applying the identical argument to suffering and not-self in turn",
             "An unrelated discourse with no connection to either",
             "A direct refutation of both later discourses",
             "A much longer discourse that the other two merely summarize"],
         "correct": 0,
         "expl": "Three discourses sharing identical structure, differing only in the single mark named."},
        {"q": "What is the recommended practice toward present form specifically?",
         "opts": [
             "Practicing for disillusionment, dispassion, and cessation",
             "Simply ignoring it entirely",
             "Actively cultivating attachment to it",
             "Only observing it without any further practice"],
         "correct": 0,
         "expl": "A distinct three-part practice, different from the practices recommended toward past and future form."},
        {"q": "What set of three discourses does this one open, closing Nakulapituvagga?",
         "opts": [
             "A triplet on the three marks (impermanence, suffering, not-self) across the three times",
             "A triplet on the four noble truths",
             "A triplet on monastic discipline",
             "A triplet on the six sense fields"],
         "correct": 0,
         "expl": "Impermanence, suffering, and not-self, each run once across past, present, and future."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Steep Mountain, near Kuraraghara",
             "Rājagaha"],
         "correct": 0,
         "expl": "The default setting for most of this vagga's discourses."},
        {"q": "Why does the argument begin with past and future rather than the present directly?",
         "opts": [
             "To first secure agreement on the less contentious cases before extending the claim to the present",
             "Because the present is considered irrelevant to the teaching",
             "Because past and future are easier for listeners to verify directly",
             "Purely for stylistic variation, with no argumentative purpose"],
         "correct": 0,
         "expl": "An a fortiori strategy: if even the past/future cases hold, the present case holds all the more."},
        {"q": "Does this discourse claim that past and future form no longer exist or are unreal?",
         "opts": [
             "No — it argues about their impermanence, not their unreality",
             "Yes — it explicitly denies the reality of past and future form",
             "The discourse is silent on this question entirely",
             "It claims only present form is real"],
         "correct": 0,
         "expl": "The claim is about impermanence as a shared property across all three times, not about existence or non-existence."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "Venerable Mahākaccāna",
             "The householder Hāliddikāni"],
         "correct": 0,
         "expl": "A direct teaching, consistent with the vagga's other Sāvatthī-set discourses."},
    ],
    marginalia=[
        ("An argument from the weaker case to the stronger", [
            "past and future first &mdash;",
            "present follows all the more obviously",
        ]),
        ("Three times, three distinct practices", [
            "not concerned, not looking forward, disillusionment &mdash;",
            "no single generic attitude applied uniformly",
        ]),
        ("One structure, five aggregates", [
            "the same reasoning repeated &mdash;",
            "no exception carved out for any one",
        ]),
        ("The first third of a matched set", [
            "impermanence here &mdash;",
            "suffering and not-self to follow, same shape",
        ]),
    ],
    further=[
        '<a href="%s/sn22.9/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.8.html">SN 22.8 &middot; Anxiety Because of '
        "Grasping (2nd)</a> &mdash; the previous discourse, closing "
        "the vagga's pair on grasping and self-identification.",
        '<a href="sn-22.10.html">SN 22.10 &middot; Suffering in the '
        "Three Times</a> &mdash; the next discourse, the identical "
        "argument applied to suffering instead of impermanence.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.10 — Kālattayadukkhasutta
# --------------------------------------------------------------------------- #
page(
    22, 10, "Kālattayadukkha", "Suffering in the Three Times",
    vagga="Nakulapituvagga",
    meta_title="SN 22.10 — Suffering in the Three Times | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kālattayadukkhasutta &mdash; the second of the closing "
        "triplet, the identical argument from SN 22.9 restated for "
        "suffering rather than impermanence. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Word-for-word identical in structure to SN 22.9, "
                 "with \"suffering\" substituted for \"impermanent\""),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical reasoning to SN 22.9, straightforward "
                       "once that discourse's structure is understood"),
    ],
    why=(
        "This discourse is the middle term of the vagga's closing "
        "triplet, and its relationship to SN 22.9 is worth being "
        "explicit about: every sentence carries over unchanged except "
        "for the single substitution of &ldquo;suffering&rdquo; "
        "(dukkha) for &ldquo;impermanent&rdquo; (anicca). This is not "
        "laziness in the source material but a deliberate feature of "
        "how the three marks were taught &mdash; the same argument "
        "form, walked through three times with one term swapped each "
        "time, so that a listener internalizes the argument's shape "
        "independently of which particular mark is being established. "
        "Impermanence and suffering are also traditionally linked "
        "causally in the canon (what is impermanent is suffering "
        "precisely because it cannot be relied upon), so this "
        "discourse's placement immediately after SN 22.9 also traces "
        "that causal link structurally, one discourse per step."
    ),
    guide=[
        ("The identical scaffolding, one word changed", [
            "Every structural element from SN 22.9 recurs here without "
            "modification: the past-and-future-let-alone-the-present "
            "argument, the three distinct practices for the three "
            "times, and the aggregate-by-aggregate repetition. The "
            "only substantive change across the entire discourse is "
            "the single term at its center &mdash; dukkha, "
            "suffering, standing where anicca, impermanence, stood "
            "in the discourse just before it.",
        ]),
        ("Why suffering follows impermanence, not the reverse", [
            "The canon elsewhere states directly that what is "
            "impermanent is suffering (yad aniccaṁ taṁ dukkhaṁ), "
            "making SN 22.9's claim a premise this discourse's claim "
            "can be read as building on, rather than two unrelated "
            "assertions placed side by side. Something that changes "
            "and cannot be relied upon is, for that very reason, "
            "unsatisfactory to build a sense of security or "
            "permanent well-being on.",
        ]),
        ("The three practices, now aimed at suffering", [
            "As in SN 22.9, a learned noble disciple who sees this "
            "&mdash; now specifically that past and future form, "
            "and by extension present form, is suffering &mdash; is "
            "not concerned with past form, does not look forward to "
            "enjoying future form, and practices for disillusionment, "
            "dispassion, and cessation regarding present form. The "
            "practical response named is identical to SN 22.9's, "
            "because the shape of the problem being addressed (an "
            "aggregate someone might otherwise cling to) is the same.",
        ]),
        ("One step remaining in the triplet", [
            "With impermanence and suffering both established across "
            "all three times, the triplet's final step &mdash; SN "
            "22.11's argument for not-self &mdash; is left to close "
            "out both the vagga and, traditionally, the logical "
            "sequence of the three marks: what is impermanent is "
            "suffering, and what is suffering cannot reasonably be "
            "taken as self.",
        ]),
    ],
    terms=[
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; the single term substituted "
         "for anicca (impermanent) throughout this discourse, "
         "otherwise identical to SN 22.9."),
        ("yad aniccaṁ taṁ dukkhaṁ",
         "&ldquo;what is impermanent is suffering&rdquo; &mdash; the "
         "canon's standard formula linking the first two marks "
         "causally, relevant to why this discourse follows SN 22.9 "
         "rather than standing alone."),
        ("pageva paccuppannassa",
         "&ldquo;let alone the present&rdquo; &mdash; the same "
         "argument-hinge phrase carried over unchanged from SN 22.9."),
        ("anapekkho",
         "&ldquo;not concerned with&rdquo; &mdash; the same practice "
         "recommended toward past form, unchanged from SN 22.9."),
        ("nibbidāya virāgāya nirodhāya",
         "&ldquo;for disillusionment, dispassion, and cessation&rdquo; "
         "&mdash; the same three-part practice recommended toward "
         "present form, unchanged from SN 22.9."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same argument "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.10:1.1-1.9"),
        ("p", "&sect;2", "sn22.10:1.10-1.14"),
    ],
    quiz=[
        {"q": "What single word changes between SN 22.9 and this discourse?",
         "opts": [
             "\"Suffering\" (dukkha) replaces \"impermanent\" (anicca)",
             "\"Consciousness\" replaces \"form\"",
             "\"Past\" replaces \"future\"",
             "\"Learned\" replaces \"unlearned\""],
         "correct": 0,
         "expl": "Every other structural element carries over unchanged from the previous discourse."},
        {"q": "What canonical formula links impermanence and suffering, relevant to this discourse's placement?",
         "opts": [
             "\"What is impermanent is suffering\" (yad aniccaṁ taṁ dukkhaṁ)",
             "\"What is suffering is permanent\"",
             "\"What is self is not suffering\"",
             "\"What is form is not impermanent\""],
         "correct": 0,
         "expl": "A standard causal link explaining why this discourse follows SN 22.9 rather than standing independently."},
        {"q": "What argument structure does this discourse use, identical to SN 22.9's?",
         "opts": [
             "Past and future form is suffering, \"let alone\" the present",
             "Only present form is discussed",
             "Future form alone is claimed to be suffering",
             "The discourse denies any connection between form and suffering"],
         "correct": 0,
         "expl": "The same a fortiori move from the less contentious cases to the present case."},
        {"q": "What three practices does a learned noble disciple take up, identical to SN 22.9's recommendations?",
         "opts": [
             "Not concerned with past form, not looking forward to future form, practicing for disillusionment regarding present form",
             "A completely different set of practices unique to this discourse",
             "Avoiding all five aggregates permanently",
             "Only meditating on the present moment"],
         "correct": 0,
         "expl": "The practical response is unchanged because the underlying problem (clinging to an aggregate) is the same."},
        {"q": "What triplet does this discourse belong to?",
         "opts": [
             "A matched set on impermanence, suffering, and not-self across the three times, closing Nakulapituvagga",
             "A triplet on the four noble truths",
             "A triplet on the six sense fields",
             "A triplet on monastic robes"],
         "correct": 0,
         "expl": "The middle term of the vagga's closing three-discourse set."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and feeling",
             "Only consciousness"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern spelled out for form and consciousness."},
        {"q": "What discourse comes immediately after this one, closing the triplet?",
         "opts": [
             "SN 22.11, applying the identical argument to not-self",
             "SN 22.1, looping back to the vagga's opening",
             "A discourse from an entirely different saṃyutta",
             "The vagga's closing uddāna, with no further discourse"],
         "correct": 0,
         "expl": "Not-self is the third and final mark in the traditional sequence."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Steep Mountain, near Kuraraghara",
             "Rājagaha"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.9."},
        {"q": "Why might this discourse and SN 22.9 be considered a deliberate teaching device rather than mere repetition?",
         "opts": [
             "Repeating an argument's shape with one term swapped helps a listener internalize the argument independently of the particular mark",
             "The similarity is entirely accidental and has no pedagogical purpose",
             "It exists only because the compilers ran out of new material",
             "It exists to pad the length of the collection"],
         "correct": 0,
         "expl": "A recognized teaching pattern in this literature, seen elsewhere in this saṃyutta's paired discourses."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Sāriputta",
             "Venerable Mahākaccāna",
             "The householder Hāliddikāni"],
         "correct": 0,
         "expl": "A direct teaching, consistent with SN 22.9."},
    ],
    marginalia=[
        ("One term swapped, everything else identical", [
            "suffering stands where impermanence stood &mdash;",
            "the same scaffolding carries the new claim",
        ]),
        ("A causal link, not a coincidence", [
            "what is impermanent is suffering &mdash;",
            "this discourse builds on the one before it",
        ]),
        ("The same three practices, aimed at a new mark", [
            "not concerned, not looking forward, disillusionment &mdash;",
            "unchanged because the underlying problem is unchanged",
        ]),
        ("The middle term of three", [
            "impermanence secured, suffering now secured &mdash;",
            "not-self remains for the triplet's close",
        ]),
    ],
    further=[
        '<a href="%s/sn22.10/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.9.html">SN 22.9 &middot; Impermanence in the '
        "Three Times</a> &mdash; the previous discourse, the "
        "identical argument applied to impermanence.",
        '<a href="sn-22.11.html">SN 22.11 &middot; Not-Self in the '
        "Three Times</a> &mdash; the next discourse, closing both the "
        "triplet and Nakulapituvagga with not-self.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.11 — Kālattayaanattasutta
# --------------------------------------------------------------------------- #
page(
    22, 11, "Kālattayaanatta", "Not-Self in the Three Times",
    vagga="Nakulapituvagga",
    meta_title="SN 22.11 — Not-Self in the Three Times | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Kālattayaanattasutta &mdash; the closing discourse of "
        "the triplet and of Nakulapituvagga, the identical argument "
        "applied to not-self. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The third and final term of the triplet, identical "
                 "in structure to SN 22.9 and SN 22.10, substituting "
                 "\"not-self\" for the previous discourses' terms"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "identical reasoning to SN 22.9-10, closing "
                       "the vagga's own logical sequence"),
    ],
    why=(
        "This discourse completes the vagga's closing triplet and, "
        "with it, all three of the classic marks (tilakkhaṇa) run "
        "once each across past, present, and future: impermanence in "
        "SN 22.9, suffering in SN 22.10, and now not-self here. The "
        "traditional logical chain that links the three &mdash; what "
        "is impermanent is suffering, and what is suffering is not "
        "fit to be regarded as self, since a genuine self could not "
        "be a source of the very suffering it belonged to &mdash; "
        "arrives at its conclusion in the discourse's closing term. "
        "It is a fitting close to Nakulapituvagga as a whole: the "
        "vagga opened with SN 22.1's practical advice on keeping the "
        "mind healthy through a body's decline, and closes here with "
        "the doctrinal argument for exactly why identifying that "
        "body, or any of the five aggregates, as a fixed self was "
        "never sound to begin with."
    ),
    guide=[
        ("The third and final substitution", [
            "As with SN 22.10's relation to SN 22.9, every structural "
            "element of this discourse recurs from the two before it "
            "unchanged, with &ldquo;not-self&rdquo; (anattā) now "
            "standing in the position &ldquo;impermanent&rdquo; and "
            "&ldquo;suffering&rdquo; occupied in turn. The "
            "past-and-future-let-alone-the-present argument, and the "
            "three practices toward each of the three times, both "
            "carry over exactly.",
        ]),
        ("Why not-self follows from suffering", [
            "The traditional reasoning linking suffering to not-self "
            "runs: whatever is suffering, and subject to change, "
            "cannot reasonably be regarded as &ldquo;this is mine, I "
            "am this, this is my self&rdquo; &mdash; language "
            "directly recalling SN 22.8's threefold formula earlier "
            "in this same vagga &mdash; because something that is "
            "genuinely one's own self should not itself be a source "
            "of affliction one cannot control. This discourse does "
            "not spell that reasoning out explicitly, but its "
            "placement as the triplet's third term, after "
            "impermanence and suffering have both already been "
            "established, assumes it.",
        ]),
        ("The same three practices, now closing the argument", [
            "A learned noble disciple who sees that past and future "
            "form &mdash; and therefore present form, all the more "
            "obviously &mdash; is not-self responds exactly as in the "
            "previous two discourses: not concerned with past form, "
            "not looking forward to enjoying future form, and "
            "practicing for disillusionment, dispassion, and "
            "cessation regarding present form. The practical upshot "
            "of seeing all three marks turns out to be a single "
            "consistent response, not three different responses "
            "stacked on top of each other.",
        ]),
        ("A vagga closing where it began", [
            "Nakulapituvagga opened with an old man asking how to "
            "keep a healthy mind while his body declined, and "
            "Sāriputta's answer in SN 22.1 turned on exactly the "
            "self-identification the vagga's middle discourses (SN "
            "22.7-8) and this closing triplet analyze in full: "
            "regarding the aggregates as self is what makes their "
            "inevitable change into a source of anxiety and grief. "
            "This discourse closes the vagga by giving the fullest, "
            "most systematic version of the argument for why that "
            "identification was never warranted &mdash; not because "
            "the aggregates are worthless, but because they were "
            "never a fixed self to begin with.",
        ]),
    ],
    terms=[
        ("anattā",
         "&ldquo;not-self&rdquo; &mdash; the third of the three "
         "marks, and the term substituted here for anicca and dukkha "
         "in the two discourses before it."),
        ("pageva paccuppannassa",
         "&ldquo;let alone the present&rdquo; &mdash; the same "
         "argument-hinge phrase carried over unchanged from SN 22.9 "
         "and SN 22.10."),
        ("yaṁ dukkhaṁ tadanattā",
         "&ldquo;what is suffering is not-self&rdquo; &mdash; the "
         "traditional formula completing the three marks' logical "
         "chain, assumed by this discourse's placement though not "
         "spelled out within it."),
        ("nibbidāya virāgāya nirodhāya",
         "&ldquo;for disillusionment, dispassion, and cessation&rdquo; "
         "&mdash; the same three-part practice recommended toward "
         "present form, unchanged across all three discourses in the "
         "triplet."),
        ("tilakkhaṇa",
         "the &ldquo;three marks&rdquo; &mdash; impermanence, "
         "suffering, and not-self, together forming the traditional "
         "name for the pattern this closing triplet completes."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same argument "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.11:1.1-1.9"),
        ("p", "&sect;2", "sn22.11:1.10-1.14"),
    ],
    quiz=[
        {"q": "What term does this discourse substitute for the previous two discourses' \"impermanent\" and \"suffering\"?",
         "opts": [
             "Not-self (anattā)",
             "Permanent",
             "Blissful",
             "Self"],
         "correct": 0,
         "expl": "The third and final mark, closing the triplet's sequence."},
        {"q": "What traditional reasoning links suffering to not-self, assumed by this discourse's placement?",
         "opts": [
             "Whatever is suffering and subject to change cannot reasonably be regarded as one's own self",
             "Whatever is not-self must also be permanent",
             "Whatever is suffering must be actively sought out",
             "There is no traditional link between the two marks"],
         "correct": 0,
         "expl": "A genuine self should not itself be a source of uncontrollable affliction."},
        {"q": "What argument structure does this discourse use, identical to SN 22.9 and SN 22.10?",
         "opts": [
             "Past and future form is not-self, \"let alone\" the present",
             "Only present form is discussed",
             "Future form alone is claimed to be not-self",
             "The discourse denies any connection between form and self"],
         "correct": 0,
         "expl": "The same a fortiori move carried over unchanged from the previous two discourses."},
        {"q": "What three practices does a learned noble disciple take up, identical to the previous two discourses?",
         "opts": [
             "Not concerned with past form, not looking forward to future form, practicing for disillusionment regarding present form",
             "A completely new set of practices unique to this discourse",
             "Rejecting all five aggregates as illusory",
             "Only meditating on emptiness directly"],
         "correct": 0,
         "expl": "The identical practical response as SN 22.9 and SN 22.10, since the underlying problem is unchanged."},
        {"q": "What triplet does this discourse complete?",
         "opts": [
             "The three marks — impermanence, suffering, and not-self — each run once across past, present, and future",
             "A triplet on the four noble truths",
             "A triplet on the six sense fields",
             "A triplet on monastic ordination"],
         "correct": 0,
         "expl": "Tilakkhaṇa, the traditional name for this pattern, is now fully completed."},
        {"q": "How does this discourse's closing connect back to SN 22.1, the vagga's opening discourse?",
         "opts": [
             "It gives the systematic argument for why regarding the aggregates as self — the source of SN 22.1's anxieties — was never warranted",
             "It directly contradicts SN 22.1's teaching",
             "It has no meaningful connection to SN 22.1",
             "It repeats SN 22.1's narrative content verbatim"],
         "correct": 0,
         "expl": "The vagga closes where it opened, now with the full doctrinal argument in place."},
        {"q": "What formula from earlier in this vagga does the not-self reasoning recall?",
         "opts": [
             "SN 22.8's \"this is mine, I am this, this is my self\"",
             "SN 22.2's three-round interrogation",
             "SN 22.3's bastion-and-abode imagery",
             "SN 22.5's twelve-link chain"],
         "correct": 0,
         "expl": "The not-self argument directly targets the same threefold identification SN 22.8 analyzed earlier."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern spelled out for form and consciousness."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Steep Mountain, near Kuraraghara",
             "Rājagaha"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.9 and SN 22.10."},
        {"q": "What follows this discourse, moving beyond Nakulapituvagga?",
         "opts": [
             "SN 22.12, opening Aniccavagga, the vagga's second chapter",
             "A return to SN 22.1",
             "The end of the entire Khandhavagga",
             "A discourse from an entirely different saṃyutta"],
         "correct": 0,
         "expl": "The book's own systematic coverage continues into its next chapter."},
    ],
    marginalia=[
        ("The third substitution, completing a chain", [
            "not-self stands where suffering stood &mdash;",
            "the same scaffolding carries the final term",
        ]),
        ("A reasoning assumed, not spelled out", [
            "suffering to not-self &mdash;",
            "no genuine self affliction cannot control",
        ]),
        ("One response to all three marks", [
            "not concerned, not looking forward, disillusionment &mdash;",
            "a single consistent practice, not three stacked ones",
        ]),
        ("The vagga closing where it opened", [
            "SN 22.1's anxious old man &mdash;",
            "this discourse's full argument for why",
        ]),
    ],
    further=[
        '<a href="%s/sn22.11/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.10.html">SN 22.10 &middot; Suffering in the '
        "Three Times</a> &mdash; the previous discourse, the same "
        "argument applied to suffering.",
        '<a href="sn-22.1.html">SN 22.1 &middot; Nakula&rsquo;s '
        "Father</a> &mdash; the vagga's opening discourse, whose "
        "practical advice this closing argument now grounds "
        "doctrinally.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.12 — Aniccasutta
# --------------------------------------------------------------------------- #
page(
    22, 12, "Anicca", "Impermanence",
    vagga="Aniccavagga",
    meta_title="SN 22.12 — Impermanence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Aniccasutta &mdash; the shortest complete statement of "
        "the path from seeing impermanence to full liberation, "
        "opening Aniccavagga. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A single sentence naming the aggregates as "
                 "impermanent, followed by the canon's standard "
                 "four-step liberation formula in full"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and direct, though its final formula "
                       "repays slow reading"),
    ],
    why=(
        "This discourse opens Aniccavagga with what may be the "
        "shortest complete map from a single observation to full "
        "liberation found anywhere in the collection. Five aggregates "
        "are impermanent; seeing this, disillusionment arises; "
        "disillusionment fades desire; fading desire frees the mind; "
        "and freedom is known as freedom, closing with the arahant's "
        "own declaration &mdash; rebirth ended, the spiritual journey "
        "completed, nothing further to be done. No narrative frames "
        "it, no questioner interrupts it, and no argument defends its "
        "first premise. It is presented as something to be simply "
        "seen, and the discourse's entire structure is the sequence "
        "of what seeing it sets in motion."
    ),
    guide=[
        ("One premise, stated once", [
            "The discourse's sole factual claim is compact: form, "
            "feeling, perception, choices, and consciousness are "
            "impermanent. Unlike SN 22.9's opening discourse in the "
            "previous vagga, there is no argument here from past and "
            "future to present, no a fortiori structure &mdash; the "
            "claim is simply stated, addressed directly to a present "
            "audience already assumed capable of seeing it for "
            "themselves.",
        ]),
        ("The four-step chain from seeing to freedom", [
            "What follows is the canon's standard liberation "
            "sequence, given here in one of its clearest, least "
            "adorned forms: seeing impermanence, a learned noble "
            "disciple grows disillusioned (nibbindati); being "
            "disillusioned, desire fades away (virajjati); when "
            "desire fades, they are freed (vimuccati); and once "
            "freed, they know they are freed (vimuttasmiṁ "
            "vimuttamiti ñāṇaṁ hoti). Each step in the chain "
            "depends strictly on the one before it, with no step "
            "skipped or reordered.",
        ]),
        ("The arahant's own words, quoted directly", [
            "The discourse closes by quoting, rather than merely "
            "describing, what the freed person understands about "
            "themselves: &ldquo;rebirth is ended, the spiritual "
            "journey has been completed, what had to be done has "
            "been done, there is nothing further for this "
            "place.&rdquo; This four-part declaration (khīṇā jāti, "
            "vusitaṁ brahmacariyaṁ, kataṁ karaṇīyaṁ, nāparaṁ "
            "itthattāyāti pajānāti) recurs throughout the canon as "
            "the standard marker of arahantship, and its appearance "
            "here, attached to nothing more than seeing the "
            "aggregates' impermanence, states plainly how much this "
            "single observation is held to accomplish.",
        ]),
        ("A pattern the whole vagga will now vary", [
            "This discourse's shape &mdash; premise, disillusionment, "
            "freedom, declaration &mdash; is the template the rest of "
            "Aniccavagga works variations on: the same chain repeated "
            "for suffering and not-self directly (SN 22.13-14), then "
            "compressed and progressively shortened (SN 22.15-17), "
            "then extended to each aggregate's cause (SN 22.18-20), "
            "before the vagga closes with Ānanda's direct question "
            "about what all of this &ldquo;cessation&rdquo; actually "
            "refers to (SN 22.21).",
        ]),
    ],
    terms=[
        ("nibbindati",
         "&ldquo;grows disillusioned&rdquo; &mdash; the first "
         "consequence of seeing impermanence, the chain's opening "
         "link."),
        ("virajjati",
         "&ldquo;desire fades away&rdquo; &mdash; the second link, "
         "following directly from disillusionment."),
        ("vimuccati",
         "&ldquo;is freed&rdquo; &mdash; the third link, the "
         "liberation itself, following from desire's fading."),
        ("vimuttasmiṁ vimuttamiti ñāṇaṁ",
         "&ldquo;when freed, they know they're freed&rdquo; &mdash; "
         "the fourth link, a reflexive knowledge of one's own freedom, "
         "distinct from the freedom itself."),
        ("khīṇā jāti&hellip;nāparaṁ itthattāya",
         "&ldquo;rebirth is ended&hellip;nothing further for this "
         "place&rdquo; &mdash; the standard four-part arahant "
         "declaration, quoted directly rather than merely referenced."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.12:1.1-1.7"),
    ],
    quiz=[
        {"q": "What single claim opens this discourse?",
         "opts": [
             "Form, feeling, perception, choices, and consciousness are impermanent",
             "The mind is eternal and unchanging",
             "Only form among the aggregates is impermanent",
             "Impermanence applies only to physical objects, not to the mind"],
         "correct": 0,
         "expl": "Stated once, directly, without argument or narrative framing."},
        {"q": "What is the first step in the chain that follows from seeing this impermanence?",
         "opts": [
             "A learned noble disciple grows disillusioned",
             "They immediately die",
             "They begin arguing with others",
             "They seek out a teacher"],
         "correct": 0,
         "expl": "Nibbindati, disillusionment, the chain's opening link."},
        {"q": "What follows disillusionment in the chain?",
         "opts": [
             "Desire fades away",
             "A new, stronger desire arises",
             "The disciple forgets the teaching",
             "Physical illness"],
         "correct": 0,
         "expl": "Virajjati, the second link, following strictly from the first."},
        {"q": "What follows the fading of desire?",
         "opts": [
             "They are freed",
             "They become a teacher",
             "They are reborn immediately",
             "They lose all memory"],
         "correct": 0,
         "expl": "Vimuccati, the third link — liberation itself."},
        {"q": "What is the fourth and final step in the chain?",
         "opts": [
             "When freed, they know they are freed",
             "They forget they were ever bound",
             "They begin the chain over again",
             "They teach the chain to others immediately"],
         "correct": 0,
         "expl": "A reflexive knowledge of one's own freedom, distinct from the freedom itself."},
        {"q": "What four-part declaration closes the discourse?",
         "opts": [
             "\"Rebirth is ended, the spiritual journey has been completed, what had to be done has been done, there is nothing further for this place\"",
             "\"I have seen the truth and shall now teach it to all\"",
             "\"The aggregates have been destroyed forever\"",
             "\"I shall return in a future life to help others\""],
         "correct": 0,
         "expl": "The canon's standard arahant declaration, quoted directly."},
        {"q": "How does this discourse's structure differ from SN 22.9's opening argument in the previous vagga?",
         "opts": [
             "It states the impermanence claim directly with no a fortiori argument from past and future",
             "It is much longer and more elaborate than SN 22.9",
             "It rejects SN 22.9's conclusion entirely",
             "It only concerns future aggregates, not present ones"],
         "correct": 0,
         "expl": "A simpler, more direct presentation than the previous vagga's argued case."},
        {"q": "How many aggregates does this discourse's chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "All five are named together in the opening claim."},
        {"q": "What role does this discourse play in the vagga's overall structure?",
         "opts": [
             "It sets the template pattern that SN 22.13-21 will vary and extend",
             "It is an isolated discourse with no relation to what follows",
             "It contradicts the discourses that follow it",
             "It is the vagga's closing discourse, not its opening one"],
         "correct": 0,
         "expl": "The rest of Aniccavagga works variations on this discourse's shape."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Steep Mountain, near Kuraraghara",
             "Rājagaha"],
         "correct": 0,
         "expl": "The default setting continuing from Nakulapituvagga."},
    ],
    marginalia=[
        ("One premise, no argument attached", [
            "impermanence simply stated &mdash;",
            "assumed visible to the present audience",
        ]),
        ("Four links, each depending on the last", [
            "disillusion, fade, free, know &mdash;",
            "no step skipped or reordered",
        ]),
        ("The arahant's own words, quoted directly", [
            "not described but spoken &mdash;",
            "the standard declaration in full",
        ]),
        ("A template the vagga will now vary", [
            "this shape repeated, shortened, extended &mdash;",
            "nine more discourses building on it",
        ]),
    ],
    further=[
        '<a href="%s/sn22.12/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.11.html">SN 22.11 &middot; Not-Self in the '
        "Three Times</a> &mdash; the previous discourse, closing "
        "Nakulapituvagga.",
        '<a href="sn-22.13.html">SN 22.13 &middot; Suffering</a> '
        "&mdash; the next discourse, the identical chain applied to "
        "suffering instead of impermanence.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.13 — Dukkhasutta
# --------------------------------------------------------------------------- #
page(
    22, 13, "Dukkha", "Suffering",
    vagga="Aniccavagga",
    meta_title="SN 22.13 — Suffering | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dukkhasutta &mdash; SN 22.12's liberation chain restated "
        "for suffering, elided almost entirely in the source. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.12's structure restated with \"suffering\" "
                 "substituted for \"impermanent,\" reduced in the "
                 "source to its two changed lines"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the shortest discourse in the vagga so far, "
                       "read alongside SN 22.12"),
    ],
    why=(
        "Where SN 22.12 spelled out its four-step liberation chain "
        "in full, this discourse is compressed by the source itself "
        "to almost nothing: the aggregates are named as suffering "
        "rather than impermanent, and everything else &mdash; "
        "disillusionment, fading desire, freedom, the arahant's "
        "declaration &mdash; is elided with a bare ellipsis, trusting "
        "the reader's memory of the discourse immediately before it. "
        "This brevity is itself informative: whoever compiled this "
        "material judged the chain from &ldquo;seeing X&rdquo; to "
        "&ldquo;freed, knowing they are freed&rdquo; robust enough to "
        "survive substituting a different starting premise without "
        "needing to be rewritten each time."
    ),
    guide=[
        ("The premise changes; nothing else needs to be said", [
            "The discourse's only substantive content is its opening "
            "claim: the five aggregates are suffering. Everything "
            "that follows in SN 22.12 &mdash; disillusionment, "
            "fading desire, freedom, and the arahant's four-part "
            "declaration &mdash; is represented here only by a bare "
            "&ldquo;seeing this &hellip;&rdquo; and a closing "
            "ellipsis pointing back to &ldquo;there is nothing "
            "further for this place.&rdquo;",
        ]),
        ("A genuine feature of the source, not a shortcut taken here", [
            "As with SN 22.6 earlier in this book, this elision is "
            "preserved exactly as bilara-data gives it rather than "
            "expanded with invented prose. The pattern recurs "
            "throughout this vagga: SN 22.12 states the full chain "
            "once, and the discourses that share its shape lean on "
            "that full statement rather than repeating it.",
        ]),
        ("Suffering as a premise on its own terms", [
            "Even compressed this far, the discourse still makes a "
            "distinct claim worth pausing on: the aggregates "
            "themselves &mdash; not merely one's relationship to "
            "them, as in SN 22.7-8's grasping-based analysis &mdash; "
            "are directly named as suffering (dukkha), the second of "
            "the three marks, standing on its own rather than "
            "derived from impermanence the way the traditional "
            "sequence (what is impermanent is suffering) would "
            "suggest.",
        ]),
        ("The second of three direct statements", [
            "This discourse is the middle term of Aniccavagga's "
            "opening triplet &mdash; impermanence in SN 22.12, "
            "suffering here, not-self in SN 22.14 immediately after "
            "&mdash; each stating one mark of the three directly and "
            "without argument, in contrast to the more elaborate "
            "reasoning SN 22.15-20 will build later in the same "
            "vagga.",
        ]),
    ],
    terms=[
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; the term substituted for "
         "anicca (impermanent) in this discourse's opening claim, "
         "otherwise identical to SN 22.12."),
        ("peyyāla",
         "the technical term for an elided passage like this "
         "discourse's, where the source points back to a fuller "
         "statement rather than repeating it."),
        ("nibbindati",
         "&ldquo;grows disillusioned&rdquo; &mdash; the first link "
         "of the chain, present here only by cross-reference to SN "
         "22.12."),
        ("vimuccati",
         "&ldquo;is freed&rdquo; &mdash; the third link, likewise "
         "elided but assumed by the discourse's closing ellipsis."),
        ("nāparaṁ itthattāya",
         "&ldquo;nothing further for this place&rdquo; &mdash; the "
         "closing phrase of the arahant declaration, the only part "
         "of it directly quoted even in this compressed form."),
    ],
    text_intro=(
        "The discourse in full &mdash; genuinely this short in the "
        "source, its ellipses given exactly as bilara-data preserves "
        "them rather than expanded from SN 22.12. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.13:1.1-1.4"),
    ],
    quiz=[
        {"q": "What is this discourse's only substantive change from SN 22.12?",
         "opts": [
             "\"Suffering\" replaces \"impermanent\" as the claim made about the aggregates",
             "It adds an entirely new liberation chain",
             "It names only one aggregate instead of all five",
             "It denies SN 22.12's conclusion"],
         "correct": 0,
         "expl": "Everything else is elided by cross-reference to the previous discourse."},
        {"q": "How does the source handle the rest of the discourse's content?",
         "opts": [
             "With a bare ellipsis pointing back to SN 22.12's full statement",
             "By spelling out the entire chain again in full",
             "By replacing it with unrelated content",
             "By omitting any indication that content is missing"],
         "correct": 0,
         "expl": "A genuine peyyāla feature of the source material."},
        {"q": "What does this discourse's brevity suggest about the underlying liberation chain?",
         "opts": [
             "It was considered robust enough to survive substituting a different opening premise without rewriting",
             "It was considered unimportant and rarely used",
             "It only applies to impermanence, not to other premises",
             "It was added later and considered less authoritative"],
         "correct": 0,
         "expl": "The chain's structure stays fixed while its starting premise varies."},
        {"q": "How does this discourse's claim differ from SN 22.7-8's earlier analysis of grasping?",
         "opts": [
             "It names the aggregates themselves as suffering, rather than analyzing one's grasping relationship to them",
             "It denies that grasping has anything to do with suffering",
             "It only concerns consciousness, unlike SN 22.7-8",
             "It reaches the opposite conclusion from SN 22.7-8"],
         "correct": 0,
         "expl": "A direct claim about the aggregates' nature, distinct from the grasping-based diagnosis earlier in the book."},
        {"q": "What position does this discourse hold in Aniccavagga's opening triplet?",
         "opts": [
             "The middle term, between impermanence (SN 22.12) and not-self (SN 22.14)",
             "The triplet's final term",
             "The triplet's opening term",
             "It does not belong to any triplet"],
         "correct": 0,
         "expl": "Impermanence, suffering, not-self — each stated directly in turn."},
        {"q": "How does this discourse's directness compare to SN 22.15-20 later in the vagga?",
         "opts": [
             "It states its mark directly without argument, unlike the more elaborate reasoning built up later",
             "It is far more elaborate and argued than SN 22.15-20",
             "It uses the exact same reasoning as SN 22.18-20",
             "There is no meaningful difference between them"],
         "correct": 0,
         "expl": "SN 22.12-14 state; SN 22.15-20 build progressively more elaborate arguments."},
        {"q": "Does this project's reading guide reconstruct the elided content and present it as this discourse's own text?",
         "opts": [
             "No — it quotes the ellipsis exactly as the source gives it",
             "Yes — the full chain is reconstructed and presented as original",
             "The elided content is replaced with unrelated material",
             "The discourse is skipped entirely"],
         "correct": 0,
         "expl": "Consistent with this project's practice on other short peyyāla stubs."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.12."},
        {"q": "How many aggregates does this discourse's claim apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Named together as a group, as in SN 22.12."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.14, completing the triplet with not-self",
             "SN 22.1, looping back to the book's opening",
             "A discourse from a different saṃyutta",
             "The vagga's closing uddāna"],
         "correct": 0,
         "expl": "Not-self is the third term of the opening triplet."},
    ],
    marginalia=[
        ("One word changed, everything else pointed back", [
            "suffering stands where impermanence stood &mdash;",
            "the chain itself left unrepeated",
        ]),
        ("Brevity as a structural signal", [
            "the shortest page so far &mdash;",
            "a chain considered robust enough not to restate",
        ]),
        ("The aggregates themselves, not merely grasping at them", [
            "a direct claim, not a relational one &mdash;",
            "distinct from SN 22.7-8's earlier diagnosis",
        ]),
        ("The middle term of three direct statements", [
            "impermanence, suffering, not-self &mdash;",
            "argument arrives only later in the vagga",
        ]),
    ],
    further=[
        '<a href="%s/sn22.13/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.12.html">SN 22.12 &middot; Impermanence</a> '
        "&mdash; the previous discourse, whose full chain this one "
        "elides by cross-reference.",
        '<a href="sn-22.14.html">SN 22.14 &middot; Not-Self</a> '
        "&mdash; the next discourse, completing the opening triplet.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.14 — Anattasutta
# --------------------------------------------------------------------------- #
page(
    22, 14, "Anatta", "Not-Self",
    vagga="Aniccavagga",
    meta_title="SN 22.14 — Not-Self | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Anattasutta &mdash; the third term of Aniccavagga's "
        "opening triplet, completing impermanence, suffering, and "
        "not-self stated directly in turn. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.12's full chain restated in full, with "
                 "\"not-self\" substituted for \"impermanent\""),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and direct, completing the triplet's "
                       "third and final mark"),
    ],
    why=(
        "This discourse completes Aniccavagga's opening triplet, "
        "and unlike SN 22.13 immediately before it, its source gives "
        "the full chain a second time rather than eliding it &mdash; "
        "form, feeling, perception, choices, and consciousness are "
        "not-self; seeing this, disillusionment; disillusionment, "
        "fading desire; fading desire, freedom; freedom, the "
        "knowledge of freedom; and the complete arahant declaration "
        "closing it out. With all three marks now stated directly, "
        "the vagga's next six discourses (SN 22.15-20) will show how "
        "the three marks logically depend on one another and extend "
        "the same reasoning to each aggregate's cause, before SN "
        "22.21 closes the vagga with Ānanda's direct question about "
        "what all of it ultimately points toward."
    ),
    guide=[
        ("Not-self, stated as directly as the two marks before it", [
            "The discourse opens exactly as SN 22.12 did, with a "
            "single unargued claim: form, feeling, perception, "
            "choices, and consciousness are not-self (anattā). No "
            "reasoning connects this claim back to impermanence or "
            "suffering here &mdash; each of the triplet's three "
            "discourses stands as its own direct assertion, though "
            "SN 22.15 immediately after this vagga's next three will "
            "supply the logical connection the direct statements "
            "leave implicit.",
        ]),
        ("The full chain restated, not elided", [
            "Unlike SN 22.13's compressed treatment of suffering, "
            "this discourse's source spells the entire four-step "
            "chain out again in full: disillusionment, fading "
            "desire, freedom, and the knowledge of freedom, closing "
            "with the complete arahant declaration quoted word for "
            "word as in SN 22.12. There is no consistent rule "
            "governing which discourses in this vagga get the full "
            "restatement and which get elided; both patterns appear "
            "side by side.",
        ]),
        ("Three marks, three identical outcomes", [
            "Read together, SN 22.12, SN 22.13, and SN 22.14 make an "
            "implicit claim worth noticing on its own: whichever of "
            "the three marks a disciple sees clearly in the "
            "aggregates &mdash; impermanence, suffering, or not-self "
            "&mdash; the same four-step chain and the same final "
            "liberation follow. The three marks are not three "
            "separate paths requiring three separate trainings; "
            "seeing any one of them clearly is presented as "
            "sufficient.",
        ]),
        ("What the triplet sets up for the rest of the vagga", [
            "With all three marks now on the table as independent "
            "direct claims, the vagga turns next to showing how they "
            "relate to one another logically (SN 22.15-17, deriving "
            "not-self from suffering and suffering from impermanence) "
            "and then to each aggregate's cause (SN 22.18-20, arguing "
            "that what arises from an impermanent, suffering, or "
            "not-self cause cannot itself be otherwise) &mdash; moving "
            "from assertion to argument across the vagga's middle "
            "stretch.",
        ]),
    ],
    terms=[
        ("anattā",
         "&ldquo;not-self&rdquo; &mdash; the third mark, stated here "
         "directly as the discourse's opening claim, without argument "
         "connecting it to the two marks before it."),
        ("nibbindati",
         "&ldquo;grows disillusioned&rdquo; &mdash; the chain's "
         "opening link, spelled out again here in full rather than "
         "elided as in SN 22.13."),
        ("vimuccati",
         "&ldquo;is freed&rdquo; &mdash; the third link, restated in "
         "full."),
        ("vimuttasmiṁ vimuttamiti ñāṇaṁ",
         "&ldquo;when freed, they know they're freed&rdquo; &mdash; "
         "the fourth link, restated in full, identical in wording to "
         "SN 22.12."),
        ("khīṇā jāti&hellip;nāparaṁ itthattāya",
         "&ldquo;rebirth is ended&hellip;nothing further for this "
         "place&rdquo; &mdash; the arahant declaration, quoted "
         "directly a second time, word for word as in SN 22.12."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.14:1.1-1.5"),
    ],
    quiz=[
        {"q": "What claim opens this discourse?",
         "opts": [
             "Form, feeling, perception, choices, and consciousness are not-self",
             "Only the mind is not-self; the body is a genuine self",
             "Not-self applies only to consciousness among the aggregates",
             "The aggregates possess a hidden, unchanging self"],
         "correct": 0,
         "expl": "Stated directly, without argument connecting it to impermanence or suffering."},
        {"q": "How does this discourse's treatment of the chain compare to SN 22.13's?",
         "opts": [
             "It restates the full four-step chain, unlike SN 22.13's elided version",
             "It elides the chain even more than SN 22.13 did",
             "It uses a completely different chain from SN 22.12-13",
             "It omits the arahant declaration entirely"],
         "correct": 0,
         "expl": "No consistent rule governs which discourses in this vagga get full restatement versus elision."},
        {"q": "What does the triplet formed by SN 22.12, 22.13, and 22.14 implicitly suggest?",
         "opts": [
             "Seeing any one of the three marks clearly leads to the same liberation, not three separate trainings",
             "Only impermanence leads to liberation; suffering and not-self do not",
             "All three marks must be seen simultaneously or none is effective",
             "The three marks contradict one another"],
         "correct": 0,
         "expl": "The same four-step chain and same outcome follow regardless of which mark is seen."},
        {"q": "What do the six discourses immediately after this triplet (SN 22.15-20) do?",
         "opts": [
             "Show how the three marks logically relate to one another and extend the reasoning to each aggregate's cause",
             "Repeat this triplet's exact content without variation",
             "Reject the triplet's conclusions entirely",
             "Introduce an entirely unrelated topic"],
         "correct": 0,
         "expl": "Moving from direct assertion to explicit argument across the vagga's middle stretch."},
        {"q": "What four-part declaration closes this discourse?",
         "opts": [
             "\"Rebirth is ended, the spiritual journey has been completed, what had to be done has been done, there is nothing further for this place\"",
             "\"I have overcome all suffering forever\"",
             "\"The self has been found at last\"",
             "\"I shall teach this to all beings without exception\""],
         "correct": 0,
         "expl": "Identical in wording to SN 22.12's closing declaration."},
        {"q": "How many aggregates does this discourse's opening claim apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Named together as a group, as in SN 22.12 and SN 22.13."},
        {"q": "What position does this discourse hold in Aniccavagga's opening triplet?",
         "opts": [
             "The third and final term, completing impermanence and suffering",
             "The triplet's opening term",
             "The triplet's middle term",
             "It does not belong to the triplet"],
         "correct": 0,
         "expl": "Not-self closes the direct-statement triplet that opens the vagga."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.12 and SN 22.13."},
        {"q": "What comes immediately after this discourse, closing this triplet?",
         "opts": [
             "SN 22.15, deriving the three marks' logical connection to one another",
             "A return to SN 22.1",
             "A discourse from a different saṃyutta",
             "The vagga's closing uddāna"],
         "correct": 0,
         "expl": "SN 22.15 begins the vagga's next sub-group, spelling out the marks' logical chain."},
        {"q": "Who speaks in this discourse?",
         "opts": [
             "The Buddha, addressing the assembled mendicants",
             "Venerable Ānanda",
             "Venerable Sāriputta",
             "The householder Hāliddikāni"],
         "correct": 0,
         "expl": "A direct teaching, consistent with SN 22.12 and SN 22.13."},
    ],
    marginalia=[
        ("The third mark, as directly stated as the first two", [
            "not-self, unargued &mdash;",
            "no connection to impermanence or suffering drawn yet",
        ]),
        ("Restated in full, not elided this time", [
            "no consistent pattern &mdash;",
            "full and compressed forms sit side by side",
        ]),
        ("Three marks, one outcome each", [
            "any one seen clearly suffices &mdash;",
            "not three separate trainings",
        ]),
        ("Where the vagga turns from statement to argument", [
            "assertion complete &mdash;",
            "the logical connections come next",
        ]),
    ],
    further=[
        '<a href="%s/sn22.14/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.13.html">SN 22.13 &middot; Suffering</a> '
        "&mdash; the previous discourse, the middle term of this "
        "triplet.",
        '<a href="sn-22.15.html">SN 22.15 &middot; That Which is '
        "Impermanent</a> &mdash; the next discourse, deriving the "
        "three marks' logical connection to one another.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.15 — Yadaniccasutta
# --------------------------------------------------------------------------- #
page(
    22, 15, "Yadanicca", "That Which is Impermanent",
    vagga="Aniccavagga",
    meta_title="SN 22.15 — That Which is Impermanent | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Yadaniccasutta &mdash; the logical chain linking "
        "impermanence to suffering to not-self to the classic "
        "\"not mine, not I, not myself\" contemplation, spelled out "
        "in full. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A four-step logical chain (impermanent, therefore "
                 "suffering, therefore not-self, therefore to be seen "
                 "as not mine) run once in full for each aggregate"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "opens the vagga's most explicitly logical "
                       "sub-section"),
    ],
    why=(
        "Where SN 22.12-14 stated each of the three marks as an "
        "independent, unargued claim, this discourse is where the "
        "vagga finally spells out how they connect: form is "
        "impermanent; what's impermanent is suffering; what's "
        "suffering is not-self; and what's not-self should be seen "
        "with right understanding as &ldquo;this is not mine, I am "
        "not this, this is not my self.&rdquo; The chain runs in one "
        "direction only &mdash; from impermanence toward the "
        "negation of self &mdash; and it is this exact four-link "
        "sequence that SN 22.16 and SN 22.17 will each shorten by "
        "one step, entering the chain progressively further along."
    ),
    guide=[
        ("The logical chain, spelled out for the first time", [
            "This is the first discourse in the book to state "
            "outright the reasoning that SN 22.12-14 left implicit: "
            "impermanence entails suffering, suffering entails "
            "not-self, and not-self entails a specific way of seeing "
            "&mdash; &ldquo;this is not mine, I am not this, this is "
            "not my self,&rdquo; the exact negated formula SN 22.8's "
            "learned noble disciple used earlier in the book. Each "
            "link depends on the one before it, run through once in "
            "full for form and then for each remaining aggregate.",
        ]),
        ("Why the chain moves in only one direction", [
            "The chain argues impermanent &rarr; suffering &rarr; "
            "not-self &rarr; not-mine, never the reverse. This "
            "direction matters: it is not claimed that everything "
            "not-self is therefore suffering, or that everything "
            "suffering is therefore impermanent (both claims would "
            "be false &mdash; nibbāna is sometimes discussed "
            "elsewhere as not-self without being suffering). The "
            "argument works specifically because form, feeling, "
            "perception, choices, and consciousness are already known "
            "to be impermanent, and the chain traces only what "
            "follows from that starting point.",
        ]),
        ("An instruction, not merely a description", [
            "The chain's final link is phrased as a prescription "
            "rather than an observation: what is not-self "
            "&ldquo;should be truly seen with right understanding "
            "like this&rdquo; (yathābhūtaṁ sammappaññāya daṭṭhabbaṁ) "
            "&mdash; naming a specific practice (seeing) rather than "
            "simply stating a further fact. The three marks are "
            "presented here as building toward something to be done, "
            "not only something to be known.",
        ]),
        ("Opening a matched trio of decreasing length", [
            "This discourse states all four links in full for every "
            "aggregate. SN 22.16 immediately after it will begin one "
            "link further along the chain, at suffering rather than "
            "impermanence, and SN 22.17 will begin at not-self "
            "itself &mdash; the same destination reached from three "
            "different, progressively shorter starting points, worth "
            "reading as a matched set rather than as three unrelated "
            "discourses.",
        ]),
    ],
    terms=[
        ("yad aniccaṁ taṁ dukkhaṁ",
         "&ldquo;what is impermanent is suffering&rdquo; &mdash; the "
         "chain's first link, the canonical formula already invoked "
         "by name in the previous vagga's reading guides."),
        ("yaṁ dukkhaṁ tadanattā",
         "&ldquo;what is suffering is not-self&rdquo; &mdash; the "
         "chain's second link, completing the traditional three-mark "
         "sequence."),
        ("yathābhūtaṁ sammappaññāya daṭṭhabbaṁ",
         "&ldquo;should be truly seen with right understanding&rdquo; "
         "&mdash; the chain's final, prescriptive link, naming a "
         "practice rather than stating a further fact."),
        ("n'etaṁ mama, nesohamasmi, na meso attā",
         "&ldquo;this is not mine, I am not this, this is not my "
         "self&rdquo; &mdash; the exact content of that seeing, "
         "identical to SN 22.8's negated formula earlier in the book."),
        ("tilakkhaṇa",
         "the &ldquo;three marks&rdquo; &mdash; impermanence, "
         "suffering, and not-self, whose logical interdependence this "
         "discourse states explicitly for the first time in the book."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same four-link "
        "chain spelled out in full for form and consciousness) are "
        "given exactly as bilara-data preserves them. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.15:1.1-1.5"),
        ("p", "&sect;2", "sn22.15:1.12-1.17"),
    ],
    quiz=[
        {"q": "What four-step chain does this discourse spell out for the first time?",
         "opts": [
             "Impermanent leads to suffering, suffering leads to not-self, not-self leads to seeing \"this is not mine\"",
             "Not-self leads to suffering, suffering leads to impermanence",
             "A chain with no logical connection between its steps",
             "Impermanence leads directly to freedom, skipping the other marks"],
         "correct": 0,
         "expl": "The reasoning SN 22.12-14 left implicit as three separate direct claims."},
        {"q": "In which direction does this discourse's chain run?",
         "opts": [
             "From impermanence toward the negation of self only, not in reverse",
             "In both directions equally",
             "From not-self back to impermanence only",
             "The direction is left unspecified"],
         "correct": 0,
         "expl": "The argument works specifically starting from the known impermanence of the aggregates."},
        {"q": "What is the chain's final link phrased as?",
         "opts": [
             "A prescription to see something in a specific way, not merely a further fact",
             "A question left unanswered",
             "A denial of everything stated before it",
             "An unrelated new topic"],
         "correct": 0,
         "expl": "Yathābhūtaṁ sammappaññāya daṭṭhabbaṁ — naming a practice, not just adding information."},
        {"q": "What exact formula does the chain's final link specify?",
         "opts": [
             "\"This is not mine, I am not this, this is not my self\"",
             "\"This is mine, I am this, this is my self\"",
             "\"This is neither mine nor not mine\"",
             "\"This cannot be described in words\""],
         "correct": 0,
         "expl": "Identical to SN 22.8's negated formula from earlier in the book."},
        {"q": "How does this discourse relate to SN 22.16 and SN 22.17 immediately after it?",
         "opts": [
             "They form a matched trio, each starting the chain one link further along and progressively shorter",
             "They are unrelated discourses with no connection to this one",
             "They directly contradict this discourse's conclusions",
             "They repeat this discourse's exact wording without variation"],
         "correct": 0,
         "expl": "SN 22.16 begins at suffering; SN 22.17 begins at not-self itself."},
        {"q": "Why does the discourse not claim the chain also runs in reverse?",
         "opts": [
             "Because not everything not-self is suffering, and not everything suffering is impermanent — the reverse claims would be false",
             "Because reverse claims were never considered by the tradition",
             "Because the discourse explicitly states the reverse is also true",
             "There is no reason given; the direction is arbitrary"],
         "correct": 0,
         "expl": "The chain works specifically because the aggregates are already known to be impermanent."},
        {"q": "How many aggregates does this discourse's chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What formula from earlier in the book does this discourse's final link recall?",
         "opts": [
             "SN 22.8's negated \"this is not mine\" formula",
             "SN 22.2's three-round interrogation",
             "SN 22.3's bastion-and-abode imagery",
             "SN 22.5's twelve-link chain"],
         "correct": 0,
         "expl": "The identical negated formula, now reached through explicit logical argument rather than direct instruction."},
        {"q": "What comes immediately after this discourse?",
         "opts": [
             "SN 22.16, beginning the same chain one link further along, at suffering",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The second term of this three-discourse matched set."},
    ],
    marginalia=[
        ("The chain finally made explicit", [
            "impermanent to suffering to not-self &mdash;",
            "reasoning left implicit in the triplet before it",
        ]),
        ("One direction only", [
            "not everything not-self is suffering &mdash;",
            "the argument starts specifically from impermanence",
        ]),
        ("A prescription, not just a further fact", [
            "should be truly seen &mdash;",
            "naming a practice, not only a conclusion",
        ]),
        ("The first of three, longest to shortest", [
            "all four links stated in full &mdash;",
            "SN 22.16-17 will each shorten the entry point",
        ]),
    ],
    further=[
        '<a href="%s/sn22.15/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.14.html">SN 22.14 &middot; Not-Self</a> '
        "&mdash; the previous discourse, closing the vagga's opening "
        "triplet of direct statements.",
        '<a href="sn-22.16.html">SN 22.16 &middot; That Which is '
        "Suffering</a> &mdash; the next discourse, the same chain "
        "beginning one link further along.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.16 — Yaṁdukkhasutta
# --------------------------------------------------------------------------- #
page(
    22, 16, "Yaṁdukkha", "That Which is Suffering",
    vagga="Aniccavagga",
    meta_title="SN 22.16 — That Which is Suffering | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Yaṁdukkhasutta &mdash; SN 22.15's chain restarted one "
        "link along, beginning from suffering rather than "
        "impermanence. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.15's chain, now entered at its second link "
                 "&mdash; \"suffering\" as the starting premise "
                 "rather than \"impermanent\""),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "shorter than SN 22.15, best read as its "
                       "continuation"),
    ],
    why=(
        "This discourse is the second term of the vagga's telescoping "
        "trio, and its relationship to SN 22.15 is precise: rather "
        "than beginning &ldquo;form is impermanent,&rdquo; it begins "
        "one link further into the same chain, at &ldquo;form is "
        "suffering.&rdquo; What is suffering is not-self, and what "
        "is not-self should be seen as not mine &mdash; the same two "
        "remaining links from SN 22.15, now presented as a "
        "self-contained three-link argument rather than referring "
        "back to impermanence at all. Suffering, not impermanence, is "
        "treated here as a premise that can simply be granted on its "
        "own terms."
    ),
    guide=[
        ("The same chain, entered one step later", [
            "SN 22.15 opened with impermanence and worked through "
            "three further links to reach &ldquo;not mine.&rdquo; "
            "This discourse opens instead with suffering directly "
            "&mdash; form is suffering &mdash; and needs only two "
            "further links, suffering to not-self and not-self to "
            "the negated formula, to reach the identical destination.",
        ]),
        ("Suffering standing as its own starting point", [
            "By opening with suffering rather than deriving it from "
            "impermanence, this discourse treats the aggregates' "
            "suffering as something a listener can grant directly, "
            "without first needing to be walked through why "
            "impermanent things are suffering. This mirrors the "
            "earlier triplet's own structure (SN 22.12-14), where "
            "each mark was likewise stated as an independent, "
            "unargued claim rather than derived from the others.",
        ]),
        ("A telescoping structure, not a repetition", [
            "Read next to SN 22.15, this discourse's shorter form is "
            "not simply padding removed from a longer original; it "
            "represents a genuinely different entry point into the "
            "same underlying argument, useful to a listener who "
            "already accepts that the aggregates are suffering "
            "without needing the impermanence premise spelled out "
            "first. The two discourses complement rather than "
            "duplicate one another.",
        ]),
        ("One link remaining before the trio closes", [
            "With impermanence-as-starting-point (SN 22.15) and "
            "suffering-as-starting-point (SN 22.16) both now given, "
            "only the shortest possible entry &mdash; not-self "
            "itself, with no prior link to establish at all &mdash; "
            "remains for SN 22.17 to complete the set.",
        ]),
    ],
    terms=[
        ("yaṁ dukkhaṁ tadanattā",
         "&ldquo;what is suffering is not-self&rdquo; &mdash; this "
         "discourse's opening logical step, the same second link SN "
         "22.15 used, now serving as the chain's starting point."),
        ("yathābhūtaṁ sammappaññāya daṭṭhabbaṁ",
         "&ldquo;should be truly seen with right understanding&rdquo; "
         "&mdash; the chain's closing prescriptive link, unchanged "
         "from SN 22.15."),
        ("n'etaṁ mama, nesohamasmi, na meso attā",
         "&ldquo;this is not mine, I am not this, this is not my "
         "self&rdquo; &mdash; the destination both this discourse and "
         "SN 22.15 arrive at, reached by two links here instead of "
         "three."),
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; here treated as a starting "
         "premise granted directly, rather than derived from "
         "impermanence as SN 22.15's fuller chain did."),
        ("tilakkhaṇa",
         "the &ldquo;three marks&rdquo; &mdash; this discourse using "
         "only the second and third of the three, having skipped the "
         "first entirely."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same three-link "
        "chain spelled out in full for form and consciousness) are "
        "given exactly as bilara-data preserves them. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.16:1.1-1.4"),
        ("p", "&sect;2", "sn22.16:1.8-1.10"),
    ],
    quiz=[
        {"q": "How does this discourse's opening differ from SN 22.15's?",
         "opts": [
             "It begins with \"form is suffering\" directly, skipping the impermanence premise",
             "It begins with an entirely unrelated claim",
             "It denies that form is suffering",
             "It repeats SN 22.15's opening word for word"],
         "correct": 0,
         "expl": "The same chain, entered one link further along."},
        {"q": "How many links does this discourse's chain contain, compared to SN 22.15's four?",
         "opts": [
             "Two — suffering to not-self, and not-self to the negated formula",
             "Five, one more than SN 22.15",
             "Zero — the discourse contains no chain at all",
             "The same four links as SN 22.15, unchanged"],
         "correct": 0,
         "expl": "A shorter chain reaching the same destination as SN 22.15."},
        {"q": "What does this discourse's structure suggest about suffering as a premise?",
         "opts": [
             "That it can be granted directly, without first deriving it from impermanence",
             "That suffering cannot be discussed without impermanence",
             "That suffering is less important than impermanence",
             "That suffering only applies to some aggregates, not all five"],
         "correct": 0,
         "expl": "Mirroring how SN 22.12-14 each stated their mark as an independent, unargued claim."},
        {"q": "What formula does this discourse's chain still arrive at, identical to SN 22.15's?",
         "opts": [
             "\"This is not mine, I am not this, this is not my self\"",
             "\"This is mine, I am this, this is my self\"",
             "\"This is beyond all description\"",
             "\"This is both self and not-self\""],
         "correct": 0,
         "expl": "The same destination, reached by a shorter route."},
        {"q": "How does this discourse relate to SN 22.17 immediately after it?",
         "opts": [
             "SN 22.17 will shorten the chain even further, beginning directly from not-self",
             "SN 22.17 will lengthen the chain instead",
             "SN 22.17 contradicts this discourse's conclusions",
             "SN 22.17 is entirely unrelated to this discourse"],
         "correct": 0,
         "expl": "The third and shortest term of the vagga's telescoping trio."},
        {"q": "Is this discourse's shorter form best understood as padding removed, or as a distinct entry point?",
         "opts": [
             "A distinct entry point, useful to a listener who already grants that the aggregates are suffering",
             "Simply padding removed with no independent purpose",
             "A scribal error that shortened the original text",
             "An entirely unrelated discourse mistakenly placed here"],
         "correct": 0,
         "expl": "The two discourses complement rather than duplicate one another."},
        {"q": "How many aggregates does this discourse's chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What position does this discourse hold in the vagga's telescoping trio?",
         "opts": [
             "The second term, between SN 22.15 (impermanence) and SN 22.17 (not-self)",
             "The trio's opening term",
             "The trio's final term",
             "It does not belong to the trio"],
         "correct": 0,
         "expl": "Each of the three discourses enters the same underlying chain at a progressively later point."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.17, the shortest entry point, beginning directly from not-self",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Completing the trio's progression from longest to shortest."},
    ],
    marginalia=[
        ("Entering the chain one step later", [
            "suffering as the starting point &mdash;",
            "impermanence's derivation simply skipped",
        ]),
        ("A shorter route to the same destination", [
            "two links instead of four &mdash;",
            "\"not mine, not I, not self\" reached either way",
        ]),
        ("A distinct entry point, not mere repetition", [
            "useful to one who already grants suffering &mdash;",
            "complementing SN 22.15, not duplicating it",
        ]),
        ("The middle term of a telescoping trio", [
            "longer chain, shorter chain, shortest chain &mdash;",
            "one link remaining for SN 22.17 to close",
        ]),
    ],
    further=[
        '<a href="%s/sn22.16/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.15.html">SN 22.15 &middot; That Which is '
        "Impermanent</a> &mdash; the previous discourse, the same "
        "chain entered one link earlier.",
        '<a href="sn-22.17.html">SN 22.17 &middot; That Which is '
        "Not-Self</a> &mdash; the next discourse, the shortest entry "
        "point, closing the trio.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.17 — Yadanattāsutta
# --------------------------------------------------------------------------- #
page(
    22, 17, "Yadanattā", "That Which is Not-Self",
    vagga="Aniccavagga",
    meta_title="SN 22.17 — That Which is Not-Self | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Yadanattāsutta &mdash; the shortest entry point into the "
        "chain, beginning and ending with not-self alone, closing the "
        "vagga's telescoping trio. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The shortest possible entry into SN 22.15's chain "
                 "&mdash; a single link, not-self directly to the "
                 "negated formula"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the shortest and simplest of the trio, best "
                       "read as its conclusion"),
    ],
    why=(
        "This discourse closes the telescoping trio SN 22.15 opened: "
        "where that discourse needed four links and SN 22.16 needed "
        "two, this one needs only a single step &mdash; form is "
        "not-self, and what's not-self should be seen with right "
        "understanding as not mine, not I, not myself. Nothing "
        "precedes the not-self claim here; it is granted outright, "
        "exactly as impermanence was granted outright in SN 22.15 "
        "and suffering in SN 22.16. Read as a set, the three "
        "discourses demonstrate that whichever of the three marks a "
        "listener is prepared to grant as a starting point, the same "
        "single destination &mdash; seeing the aggregates as not "
        "mine &mdash; is reachable from it."
    ),
    guide=[
        ("The shortest possible chain", [
            "This discourse's argument has only one step: form is "
            "not-self, and what's not-self should be truly seen with "
            "right understanding as &ldquo;this is not mine, I am "
            "not this, this is not my self.&rdquo; No claim about "
            "impermanence or suffering appears at all &mdash; the "
            "chain simply starts at its own final premise and moves "
            "directly to the prescribed way of seeing.",
        ]),
        ("Completing the trio's progression", [
            "Set beside SN 22.15 (four links, starting from "
            "impermanence) and SN 22.16 (two links, starting from "
            "suffering), this discourse completes a deliberate "
            "progression: the same destination, reached by "
            "successively shorter routes, each entering the "
            "underlying chain one link further along than the last. "
            "The three together function as a kind of demonstration "
            "that the argument's strength does not depend on which "
            "of the three marks a listener starts from.",
        ]),
        ("A destination reachable from any starting point", [
            "Taken as a set with SN 22.15 and SN 22.16, this trio "
            "makes an implicit claim about the three marks' "
            "relationship worth stating plainly: impermanence, "
            "suffering, and not-self are presented as different "
            "doors onto the identical room, not as three separate "
            "insights each requiring its own independent training. "
            "Whichever mark is clearest to a given listener at a "
            "given moment, that same listener can be led from it to "
            "the same &ldquo;not mine&rdquo; understanding.",
        ]),
        ("What follows: extending the argument to each cause", [
            "With this trio complete, the vagga turns next to a "
            "different kind of extension in SN 22.18-20: rather than "
            "shortening the chain further, those three discourses "
            "lengthen the argument outward, from each aggregate "
            "itself to the cause that produces it, arguing that an "
            "effect produced by an impermanent, suffering, or "
            "not-self cause cannot itself be otherwise.",
        ]),
    ],
    terms=[
        ("anattā",
         "&ldquo;not-self&rdquo; &mdash; granted here outright as "
         "the discourse's sole starting premise, with no prior "
         "impermanence or suffering claim leading into it."),
        ("yathābhūtaṁ sammappaññāya daṭṭhabbaṁ",
         "&ldquo;should be truly seen with right understanding&rdquo; "
         "&mdash; the single remaining link, unchanged in wording "
         "from SN 22.15 and SN 22.16."),
        ("n'etaṁ mama, nesohamasmi, na meso attā",
         "&ldquo;this is not mine, I am not this, this is not my "
         "self&rdquo; &mdash; the shared destination of all three "
         "discourses in this trio, reached here in a single step."),
        ("tilakkhaṇa",
         "the &ldquo;three marks&rdquo; &mdash; this discourse using "
         "only the third, having granted it directly rather than "
         "deriving it from the first two."),
        ("hetu paccaya",
         "&ldquo;cause and reason&rdquo; &mdash; the vocabulary the "
         "next three discourses (SN 22.18-20) will introduce, "
         "extending this trio's reasoning to what produces each "
         "aggregate rather than the aggregate alone."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same single-link "
        "chain spelled out in full for form and consciousness) are "
        "given exactly as bilara-data preserves them. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.17:1.1-1.3"),
        ("p", "&sect;2", "sn22.17:1.7-1.8"),
    ],
    quiz=[
        {"q": "How many logical links does this discourse's chain contain?",
         "opts": [
             "One — not-self directly to the negated formula",
             "Four, the same as SN 22.15",
             "Two, the same as SN 22.16",
             "Zero — no chain is given at all"],
         "correct": 0,
         "expl": "The shortest entry point in the trio, with no impermanence or suffering premise stated."},
        {"q": "How does this discourse complete the trio formed with SN 22.15 and SN 22.16?",
         "opts": [
             "As the shortest of three progressively shorter routes to the same destination",
             "As a contradiction of the previous two discourses",
             "As an unrelated discourse placed here by coincidence",
             "As a longer, more elaborate version than the previous two"],
         "correct": 0,
         "expl": "Four links, then two links, then one link, all reaching the identical negated formula."},
        {"q": "What does the trio as a whole suggest about the three marks' relationship?",
         "opts": [
             "They function as different entry points onto the same understanding, not three separate independent trainings",
             "Only not-self is a valid starting point for this teaching",
             "The three marks contradict one another",
             "Impermanence must always be established before the other two marks can be taught"],
         "correct": 0,
         "expl": "Whichever mark is clearest to a listener, the same destination is reachable from it."},
        {"q": "What formula does this discourse's single link lead to?",
         "opts": [
             "\"This is not mine, I am not this, this is not my self\"",
             "\"This is mine, I am this, this is my self\"",
             "\"Self and not-self are the same thing\"",
             "\"Nothing can be truly known\""],
         "correct": 0,
         "expl": "The identical destination reached by SN 22.15 and SN 22.16 through longer routes."},
        {"q": "What do the three discourses immediately after this trio (SN 22.18-20) do differently?",
         "opts": [
             "They extend the argument outward to each aggregate's cause, rather than shortening the chain further",
             "They repeat this trio's exact content without change",
             "They reject the trio's conclusions entirely",
             "They introduce a completely unrelated topic"],
         "correct": 0,
         "expl": "A shift from shortening the entry point to lengthening the argument's scope."},
        {"q": "How many aggregates does this discourse's chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What position does this discourse hold in the vagga's telescoping trio?",
         "opts": [
             "The third and final term, the shortest of the three",
             "The trio's opening term",
             "The trio's middle term",
             "It does not belong to the trio"],
         "correct": 0,
         "expl": "SN 22.15 (four links), SN 22.16 (two links), and this discourse (one link) form the complete set."},
        {"q": "Does this discourse claim that impermanence or suffering are false?",
         "opts": [
             "No — it simply does not state them, granting not-self directly instead",
             "Yes — it explicitly denies both",
             "It claims only impermanence is false",
             "It claims only suffering is false"],
         "correct": 0,
         "expl": "The absence of a premise is not the same as denying it; the discourse simply enters the argument later."},
        {"q": "What comes immediately after this discourse, closing the trio?",
         "opts": [
             "SN 22.18, extending the argument to each aggregate's cause",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The vagga's next sub-group begins with SN 22.18."},
    ],
    marginalia=[
        ("The shortest entry point of the three", [
            "not-self granted outright &mdash;",
            "no prior link stated at all",
        ]),
        ("Four links, two links, one link", [
            "the same destination each time &mdash;",
            "a deliberate progression, not repetition",
        ]),
        ("Different doors onto the same room", [
            "impermanence, suffering, or not-self &mdash;",
            "any one sufficient as a starting point",
        ]),
        ("Where the vagga turns from shortening to extending", [
            "trio complete &mdash;",
            "SN 22.18-20 will lengthen the argument outward instead",
        ]),
    ],
    further=[
        '<a href="%s/sn22.17/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.16.html">SN 22.16 &middot; That Which is '
        "Suffering</a> &mdash; the previous discourse, the same "
        "chain entered one link earlier.",
        '<a href="sn-22.18.html">SN 22.18 &middot; Impermanence With '
        "Its Cause</a> &mdash; the next discourse, extending the "
        "argument to what produces each aggregate.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.18 — Hetusutta (Impermanence)
# --------------------------------------------------------------------------- #
page(
    22, 18, "Anicca Hetu", "Impermanence With Its Cause",
    vagga="Aniccavagga",
    meta_title="SN 22.18 — Impermanence With Its Cause | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Hetusutta &mdash; extending impermanence past the "
        "aggregates themselves to their cause, arguing an "
        "impermanent-produced effect cannot itself be permanent. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A short causal argument: the aggregates are "
                 "impermanent, their cause is also impermanent, "
                 "therefore what they produce cannot be permanent"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "introduces a new argument form not used "
                       "earlier in this vagga"),
    ],
    why=(
        "The five preceding discourses in this vagga (SN 22.12-17) "
        "all concerned the aggregates directly &mdash; whether they "
        "are impermanent, suffering, or not-self, and how those "
        "claims connect. This discourse opens a new line of argument "
        "entirely: it reaches behind the aggregates to their cause. "
        "Form is impermanent, and the cause and reason that gives "
        "rise to form is also impermanent &mdash; so, the discourse "
        "asks, since form is produced by something impermanent, how "
        "could form itself be permanent? An effect cannot outrank "
        "its own cause in stability; something arising from "
        "impermanent conditions inherits that impermanence by the "
        "very fact of its arising."
    ),
    guide=[
        ("A new kind of argument for an old conclusion", [
            "The discourse reaches the same conclusion as SN "
            "22.12-17 &mdash; the aggregates are impermanent &mdash; "
            "but by an entirely different route. Rather than simply "
            "observing that form changes, it points to what produces "
            "form in the first place and observes that this cause is "
            "impermanent too, then asks a rhetorical question rather "
            "than making a further assertion: since form is produced "
            "by what is impermanent, how could it be permanent?",
        ]),
        ("An argument from what a thing depends on", [
            "The reasoning here works by a kind of inheritance: "
            "whatever arises dependent on impermanent conditions "
            "cannot itself escape those conditions' instability, "
            "because its very existence is conditioned by something "
            "already unstable. This connects the vagga's material "
            "back to the broader framework of dependent origination "
            "(paṭicca-samuppāda) explored at length in Book II, now "
            "applied specifically to the causal relationship between "
            "an aggregate and whatever gives rise to it.",
        ]),
        ("A rhetorical question, not a further claim", [
            "The discourse's closing move for each aggregate is "
            "phrased as a question rather than a flat statement "
            "&mdash; &ldquo;how could it be permanent?&rdquo; "
            "&mdash; inviting the listener to complete the inference "
            "themselves rather than being handed the conclusion "
            "outright. This is a small but distinctive shift in "
            "register from the direct assertions of SN 22.12-17.",
        ]),
        ("Opening a matched trio parallel to the one before it", [
            "This discourse begins a second telescoping-style trio, "
            "structurally parallel to SN 22.15-17 but applying the "
            "cause-based argument to each of the three marks in turn: "
            "impermanence here, suffering in SN 22.19, and not-self "
            "in SN 22.20. Each of the three shares this discourse's "
            "exact rhetorical-question structure, differing only in "
            "which mark and which corresponding opposite (permanent, "
            "happiness, self) is being ruled out.",
        ]),
    ],
    terms=[
        ("hetu paccaya",
         "&ldquo;cause and reason&rdquo; &mdash; the phrase naming "
         "what produces each aggregate, the discourse's new focus "
         "beyond the aggregate itself."),
        ("uppanna",
         "&ldquo;produced&rdquo; or &ldquo;arisen&rdquo; &mdash; the "
         "relationship between an aggregate and its impermanent "
         "cause, central to the discourse's inheritance argument."),
        ("kuto niccaṁ bhavissati",
         "&ldquo;how could it be permanent?&rdquo; &mdash; the "
         "discourse's closing rhetorical question, inviting the "
         "listener to complete the inference rather than stating the "
         "conclusion outright."),
        ("paṭicca-samuppāda",
         "&ldquo;dependent origination&rdquo; &mdash; the broader "
         "framework from Book II this discourse's causal reasoning "
         "connects back to, now applied to a single aggregate's "
         "relationship to its cause."),
        ("anicca",
         "&ldquo;impermanent&rdquo; &mdash; here applied twice over, "
         "to both an aggregate and, distinctly, to whatever produces "
         "that aggregate."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same causal "
        "argument spelled out in full for form and consciousness) "
        "are given exactly as bilara-data preserves them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.18:1.1-1.4"),
        ("p", "&sect;2", "sn22.18:1.12-1.16"),
    ],
    quiz=[
        {"q": "What new element does this discourse introduce, not present in SN 22.12-17?",
         "opts": [
             "An argument about the cause that produces each aggregate, not just the aggregate itself",
             "A claim that the aggregates are permanent after all",
             "A rejection of the three marks entirely",
             "A narrative involving a named questioner"],
         "correct": 0,
         "expl": "The discourse reaches behind the aggregates to what produces them."},
        {"q": "What does this discourse claim about the cause that produces form?",
         "opts": [
             "It is also impermanent",
             "It is permanent and unchanging",
             "It does not exist",
             "It is identical to form itself"],
         "correct": 0,
         "expl": "The cause shares the same impermanence as its effect."},
        {"q": "How is the discourse's conclusion phrased?",
         "opts": [
             "As a rhetorical question: \"how could it be permanent?\"",
             "As a flat, direct assertion with no question",
             "As a denial that any conclusion can be drawn",
             "As a question the Buddha refuses to answer"],
         "correct": 0,
         "expl": "Inviting the listener to complete the inference themselves."},
        {"q": "What broader framework does this discourse's causal reasoning connect back to?",
         "opts": [
             "Dependent origination (paṭicca-samuppāda) from Book II",
             "The Vinaya rules for monastic conduct",
             "The geography of ancient India",
             "The biography of the Buddha's early life"],
         "correct": 0,
         "expl": "Now applied specifically to an aggregate's relationship to its cause."},
        {"q": "What relationship does this discourse claim between an effect and an impermanent cause?",
         "opts": [
             "The effect inherits the cause's instability, since its existence depends on that unstable condition",
             "The effect is entirely independent of its cause's nature",
             "The effect must be more stable than its cause",
             "There is no meaningful relationship between the two"],
         "correct": 0,
         "expl": "An argument from inheritance, not mere coincidence."},
        {"q": "How does this discourse's structure compare to SN 22.15-17?",
         "opts": [
             "It opens a new, parallel trio applying cause-based reasoning to each of the three marks",
             "It is identical in structure to SN 22.15-17",
             "It rejects everything argued in SN 22.15-17",
             "It has no relationship to SN 22.15-17 at all"],
         "correct": 0,
         "expl": "SN 22.18-20 mirror SN 22.15-17's structure while introducing the cause-based argument."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.19, applying the identical cause-based argument to suffering",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The second term of the parallel cause-based trio."},
        {"q": "Does this discourse claim the aggregates' cause is a permanent, unchanging first cause?",
         "opts": [
             "No — the cause itself is explicitly said to be impermanent",
             "Yes — it claims the cause is eternal",
             "The discourse is silent on the cause's nature",
             "It claims the cause is identical to nibbāna"],
         "correct": 0,
         "expl": "The argument depends precisely on the cause sharing the effect's impermanence."},
    ],
    marginalia=[
        ("Reaching behind the aggregate to its cause", [
            "not just form itself &mdash;",
            "what produces form, examined too",
        ]),
        ("A question, not a further assertion", [
            "how could it be permanent? &mdash;",
            "the listener completes the inference",
        ]),
        ("Instability inherited from an unstable source", [
            "an effect cannot outrank its cause &mdash;",
            "connecting back to dependent origination",
        ]),
        ("A second trio, parallel to the first", [
            "cause-based reasoning, three marks &mdash;",
            "SN 22.19-20 will complete the set",
        ]),
    ],
    further=[
        '<a href="%s/sn22.18/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.17.html">SN 22.17 &middot; That Which is '
        "Not-Self</a> &mdash; the previous discourse, closing the "
        "vagga's first telescoping trio.",
        '<a href="sn-22.19.html">SN 22.19 &middot; Suffering With '
        "Its Cause</a> &mdash; the next discourse, the identical "
        "cause-based argument applied to suffering.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.19 — Dutiyahetusutta (Suffering)
# --------------------------------------------------------------------------- #
page(
    22, 19, "Dukkha Hetu", "Suffering With Its Cause",
    vagga="Aniccavagga",
    meta_title="SN 22.19 — Suffering With Its Cause | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyahetusutta &mdash; SN 22.18's cause-based argument "
        "restated for suffering, asking how what arises from "
        "suffering could be happiness. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.18's cause-based argument restated, "
                 "substituting suffering for impermanence and "
                 "happiness for permanence"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "identical reasoning to SN 22.18, read as its "
                       "direct continuation"),
    ],
    why=(
        "This discourse carries SN 22.18's cause-based argument over "
        "to the second mark, with a small but telling shift in "
        "vocabulary: where SN 22.18 asked how something produced by "
        "an impermanent cause could be permanent, this discourse "
        "asks how something produced by a suffering cause could be "
        "happiness (sukha). The paired opposite changes &mdash; not "
        "impermanent/permanent, but suffering/happiness &mdash; "
        "showing that the underlying argument form (an effect cannot "
        "outrank its cause) is flexible enough to pair suffering "
        "against its own natural opposite rather than reusing "
        "permanence a second time."
    ),
    guide=[
        ("The same inheritance argument, a new pairing", [
            "As in SN 22.18, form is named as sharing a quality "
            "&mdash; here, suffering &mdash; with the cause that "
            "produces it, and the discourse asks a closing rhetorical "
            "question: since form is produced by what is suffering, "
            "how could it be happiness? The argument's shape is "
            "identical to SN 22.18's; only the mark and its opposite "
            "have changed.",
        ]),
        ("Why happiness, not permanence, is the ruled-out opposite", [
            "This discourse's choice of sukha (happiness) rather "
            "than reusing SN 22.18's nicca (permanence) as the ruled-"
            "out term shows the argument tracking each mark's own "
            "natural contrary rather than mechanically repeating a "
            "single opposite across all three discourses. Suffering's "
            "proper opposite is happiness, just as impermanence's "
            "proper opposite was permanence, and not-self's proper "
            "opposite (in SN 22.20 next) will be self.",
        ]),
        ("Suffering inherited, not merely coincidental", [
            "The claim is not that an aggregate produced by a "
            "suffering cause merely happens also to be suffering, but "
            "that it could not be otherwise &mdash; the same "
            "inheritance logic from SN 22.18, now applied to this "
            "mark. Whatever depends for its existence on something "
            "already unsatisfactory cannot on its own escape into "
            "genuine happiness.",
        ]),
        ("The trio's middle term", [
            "This discourse occupies the same position in its trio "
            "(SN 22.18-20) that SN 22.13 occupied in the earlier "
            "direct-statement triplet (SN 22.12-14) &mdash; the "
            "second of three parallel discourses, applying an "
            "established argument form to suffering after "
            "impermanence and before not-self.",
        ]),
    ],
    terms=[
        ("hetu paccaya",
         "&ldquo;cause and reason&rdquo; &mdash; the same phrase "
         "from SN 22.18, here naming what produces the aggregate as "
         "itself suffering."),
        ("sukha",
         "&ldquo;happiness&rdquo; &mdash; the ruled-out opposite in "
         "this discourse, replacing SN 22.18's &ldquo;permanent&rdquo; "
         "as suffering's own natural contrary."),
        ("kuto sukhaṁ bhavissati",
         "&ldquo;how could it be happiness?&rdquo; &mdash; this "
         "discourse's closing rhetorical question, parallel in form "
         "to SN 22.18's &ldquo;how could it be permanent?&rdquo;"),
        ("dukkha",
         "&ldquo;suffering&rdquo; &mdash; applied twice over, to both "
         "an aggregate and, distinctly, to whatever produces that "
         "aggregate."),
        ("uppanna",
         "&ldquo;produced&rdquo; or &ldquo;arisen&rdquo; &mdash; the "
         "same inheritance relationship from SN 22.18, unchanged in "
         "this discourse's argument."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same causal "
        "argument spelled out in full for form and consciousness) "
        "are given exactly as bilara-data preserves them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.19:1.1-1.4"),
        ("p", "&sect;2", "sn22.19:1.8-1.12"),
    ],
    quiz=[
        {"q": "What ruled-out opposite does this discourse use, replacing SN 22.18's \"permanent\"?",
         "opts": [
             "Happiness (sukha)",
             "Self",
             "Consciousness",
             "Freedom"],
         "correct": 0,
         "expl": "Suffering's own natural contrary, rather than a repeated use of permanence."},
        {"q": "What does this discourse claim about the cause that produces form?",
         "opts": [
             "It is also suffering",
             "It is happiness",
             "It does not exist",
             "It is unrelated to form's own nature"],
         "correct": 0,
         "expl": "The cause shares the same quality of suffering as its effect."},
        {"q": "How is the discourse's conclusion phrased?",
         "opts": [
             "As a rhetorical question: \"how could it be happiness?\"",
             "As a flat, direct assertion with no question",
             "As a denial that any conclusion can be drawn",
             "As an unrelated new claim"],
         "correct": 0,
         "expl": "Parallel in form to SN 22.18's closing question."},
        {"q": "What does this discourse's choice of opposite (happiness, not permanence) demonstrate?",
         "opts": [
             "The argument tracks each mark's own natural contrary rather than mechanically repeating one opposite",
             "The argument is inconsistent and poorly constructed",
             "Happiness and permanence are considered identical in this reasoning",
             "The discourse rejects SN 22.18's argument entirely"],
         "correct": 0,
         "expl": "Suffering's proper opposite is happiness, just as impermanence's proper opposite was permanence."},
        {"q": "What position does this discourse hold in its trio, SN 22.18-20?",
         "opts": [
             "The middle term, between impermanence (SN 22.18) and not-self (SN 22.20)",
             "The trio's opening term",
             "The trio's final term",
             "It does not belong to the trio"],
         "correct": 0,
         "expl": "Occupying the same position SN 22.13 held in the earlier direct-statement triplet."},
        {"q": "What underlying logic does this discourse share with SN 22.18?",
         "opts": [
             "An effect cannot outrank its cause — what arises from an unsatisfactory cause cannot itself be genuinely happy",
             "An entirely different, unrelated logic",
             "A denial that causes and effects are related at all",
             "A claim that happiness and suffering are identical"],
         "correct": 0,
         "expl": "The same inheritance argument, now applied to suffering."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.20, applying the identical cause-based argument to not-self",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The final term of the parallel cause-based trio."},
        {"q": "Does this discourse claim that suffering itself is the cause of happiness?",
         "opts": [
             "No — it argues the opposite, that a suffering cause cannot produce genuine happiness",
             "Yes — that is the discourse's central claim",
             "The discourse takes no position on this question",
             "It claims suffering and happiness alternate randomly"],
         "correct": 0,
         "expl": "The argument rules out happiness as a possible outcome of a suffering cause."},
    ],
    marginalia=[
        ("The same argument, a new natural opposite", [
            "happiness ruled out, not permanence &mdash;",
            "each mark paired against its own contrary",
        ]),
        ("Suffering inherited, not coincidental", [
            "an unsatisfactory cause &mdash;",
            "cannot produce a genuinely happy effect",
        ]),
        ("The trio's middle term again", [
            "impermanence, suffering, not-self &mdash;",
            "the same position SN 22.13 held earlier",
        ]),
        ("One term remaining before the trio closes", [
            "cause-based reasoning, two marks down &mdash;",
            "not-self left for SN 22.20",
        ]),
    ],
    further=[
        '<a href="%s/sn22.19/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.18.html">SN 22.18 &middot; Impermanence With '
        "Its Cause</a> &mdash; the previous discourse, the same "
        "argument applied to impermanence.",
        '<a href="sn-22.20.html">SN 22.20 &middot; Not-Self With Its '
        "Cause</a> &mdash; the next discourse, closing the trio with "
        "not-self.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.20 — Tatiyahetusutta (Not-Self)
# --------------------------------------------------------------------------- #
page(
    22, 20, "Anatta Hetu", "Not-Self With Its Cause",
    vagga="Aniccavagga",
    meta_title="SN 22.20 — Not-Self With Its Cause | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Tatiyahetusutta &mdash; the cause-based trio's closing "
        "term, asking how what arises from a not-self cause could "
        "itself be self. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.18-19's cause-based argument completed, "
                 "substituting not-self for impermanence and "
                 "suffering, and self for their opposites"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "identical reasoning to SN 22.18-19, closing "
                       "the cause-based trio"),
    ],
    why=(
        "This discourse closes the cause-based trio SN 22.18 opened, "
        "and its conclusion is arguably the sharpest of the three: "
        "since form is produced by what is not-self, how could it be "
        "self? Where SN 22.18 ruled out permanence and SN 22.19 ruled "
        "out happiness, this discourse rules out self itself &mdash; "
        "directly foreclosing the very possibility SN 22.7-8 examined "
        "earlier in the book, that an aggregate might be identified "
        "with under any of the fourfold or threefold formulas. If "
        "even an aggregate's cause is not-self, nothing about the "
        "aggregate's own arising could smuggle a genuine self back in."
    ),
    guide=[
        ("The trio's final substitution", [
            "As in SN 22.18-19, form is named as sharing a quality "
            "&mdash; here, not-self &mdash; with the cause that "
            "produces it, closing with the rhetorical question: since "
            "form is produced by what is not-self, how could it be "
            "self? The argument's shape is identical across all three "
            "discourses; only the mark and its ruled-out opposite "
            "change.",
        ]),
        ("Foreclosing self at the level of causation itself", [
            "This discourse's conclusion connects directly back to "
            "SN 22.7-8's earlier analysis of identity view: those "
            "discourses examined the various ways a person might "
            "regard an aggregate as self, self as having it, or as "
            "mine. This discourse forecloses the possibility one "
            "level earlier, at the aggregate's own causation &mdash; "
            "if what produces form is itself not a self, form's own "
            "arising offers no opening for a genuine self to be "
            "found in it.",
        ]),
        ("Completing a matched pair of trios", [
            "With this discourse, the vagga has now built two "
            "parallel three-discourse sets on an identical underlying "
            "template: SN 22.15-17 telescoped a single logical chain "
            "into progressively shorter entry points, while SN "
            "22.18-20 held the argument's length constant and instead "
            "varied which of the three marks, paired against its own "
            "proper opposite, was being ruled out at the level of "
            "cause.",
        ]),
        ("One discourse remaining to close the vagga", [
            "With impermanence, suffering, and not-self now argued "
            "both directly (SN 22.12-14), through logical derivation "
            "(SN 22.15-17), and through causation (SN 22.18-20), the "
            "vagga has one discourse left: SN 22.21, where Ānanda "
            "asks the Buddha directly what all of this &ldquo;cessation&rdquo; "
            "the preceding twenty discourses have been building "
            "toward actually refers to.",
        ]),
    ],
    terms=[
        ("hetu paccaya",
         "&ldquo;cause and reason&rdquo; &mdash; the same phrase "
         "from SN 22.18-19, here naming what produces the aggregate "
         "as itself not-self."),
        ("attā",
         "&ldquo;self&rdquo; &mdash; the ruled-out opposite in this "
         "discourse, completing the trio's sequence of permanent, "
         "happiness, and now self."),
        ("kuto attā bhavissati",
         "&ldquo;how could it be self?&rdquo; &mdash; this "
         "discourse's closing rhetorical question, the sharpest of "
         "the trio's three parallel conclusions."),
        ("anattā",
         "&ldquo;not-self&rdquo; &mdash; applied twice over, to both "
         "an aggregate and, distinctly, to whatever produces that "
         "aggregate."),
        ("sakkāyadiṭṭhi",
         "&ldquo;identity view&rdquo; &mdash; the broader doctrine "
         "SN 22.7-8 examined earlier in the book, which this "
         "discourse's causal argument forecloses one level further "
         "back, at the aggregate's own arising."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same causal "
        "argument spelled out in full for form and consciousness) "
        "are given exactly as bilara-data preserves them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.20:1.1-1.4"),
        ("p", "&sect;2", "sn22.20:1.8-1.12"),
    ],
    quiz=[
        {"q": "What ruled-out opposite does this discourse use, completing the trio's sequence?",
         "opts": [
             "Self (attā)",
             "Happiness",
             "Permanence",
             "Consciousness"],
         "correct": 0,
         "expl": "Completing the sequence permanent (SN 22.18), happiness (SN 22.19), self (this discourse)."},
        {"q": "What does this discourse claim about the cause that produces form?",
         "opts": [
             "It is also not-self",
             "It is a genuine, permanent self",
             "It does not exist",
             "It is unrelated to form's own nature"],
         "correct": 0,
         "expl": "The cause shares the same not-self quality as its effect."},
        {"q": "How is the discourse's conclusion phrased?",
         "opts": [
             "As a rhetorical question: \"how could it be self?\"",
             "As a flat, direct assertion with no question",
             "As a denial that any conclusion can be drawn",
             "As an unrelated new claim"],
         "correct": 0,
         "expl": "Parallel in form to SN 22.18 and SN 22.19's closing questions."},
        {"q": "How does this discourse's conclusion connect back to SN 22.7-8 earlier in the book?",
         "opts": [
             "It forecloses self one level further back, at the aggregate's own causation, rather than merely at the aggregate itself",
             "It directly contradicts SN 22.7-8's conclusions",
             "It has no meaningful connection to SN 22.7-8",
             "It repeats SN 22.7-8's exact wording"],
         "correct": 0,
         "expl": "If what produces form is itself not a self, form's own arising offers no opening for a genuine self."},
        {"q": "What position does this discourse hold in its trio, SN 22.18-20?",
         "opts": [
             "The third and final term, closing the cause-based trio",
             "The trio's opening term",
             "The trio's middle term",
             "It does not belong to the trio"],
         "correct": 0,
         "expl": "Completing impermanence (SN 22.18) and suffering (SN 22.19) with not-self."},
        {"q": "How do SN 22.15-17 and SN 22.18-20 differ as a pair of matched trios?",
         "opts": [
             "SN 22.15-17 shortens the chain's entry point; SN 22.18-20 holds the chain's length constant and varies the ruled-out opposite",
             "Both trios use exactly the same argument with no variation",
             "SN 22.18-20 shortens the chain; SN 22.15-17 varies the opposite",
             "The two trios are entirely unrelated to one another"],
         "correct": 0,
         "expl": "Two different structural devices applied to the same three marks."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What discourse comes immediately after this one, closing the vagga?",
         "opts": [
             "SN 22.21, Ānanda's direct question about what \"cessation\" refers to",
             "A return to SN 22.12",
             "A discourse from a different saṃyutta",
             "SN 22.22, opening the next vagga"],
         "correct": 0,
         "expl": "The vagga's own closing discourse, immediately before Bhāravagga begins at SN 22.22."},
        {"q": "What has the vagga now argued impermanence, suffering, and not-self through, across its twenty discourses so far?",
         "opts": [
             "Direct statement, logical derivation, and causation, in three successive stages",
             "Only direct statement, repeated twenty times without variation",
             "Only narrative dialogue, with no direct teaching",
             "A single unified argument with no internal structure"],
         "correct": 0,
         "expl": "SN 22.12-14 (direct), SN 22.15-17 (derivation), SN 22.18-20 (causation)."},
    ],
    marginalia=[
        ("The sharpest of the three ruled-out opposites", [
            "self itself denied &mdash;",
            "not merely permanence or happiness",
        ]),
        ("Foreclosing self at the level of causation", [
            "not just the aggregate itself &mdash;",
            "what produces it, ruled out too",
        ]),
        ("Two trios, two different devices", [
            "shortening the chain, or varying the opposite &mdash;",
            "the same three marks, argued two ways",
        ]),
        ("Twenty discourses, three argument forms", [
            "stated, derived, and now caused &mdash;",
            "one discourse left to name what it all points to",
        ]),
    ],
    further=[
        '<a href="%s/sn22.20/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.19.html">SN 22.19 &middot; Suffering With '
        "Its Cause</a> &mdash; the previous discourse, the same "
        "argument applied to suffering.",
        '<a href="sn-22.21.html">SN 22.21 &middot; With Ānanda</a> '
        "&mdash; the next discourse, closing the vagga with a direct "
        "question about what \"cessation\" refers to.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.21 — Ānandasutta
# --------------------------------------------------------------------------- #
page(
    22, 21, "Ānanda", "With Ānanda",
    vagga="Aniccavagga",
    meta_title="SN 22.21 — With Ānanda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Ānandasutta &mdash; Ānanda asks directly what "
        "\"cessation\" refers to, and the Buddha names it precisely "
        "as the ending of the five aggregates, closing Aniccavagga. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "Venerable Ānanda questions the Buddha directly"),
        ("Form", "A short question-and-answer dialogue, closing the "
                 "vagga by naming precisely what the preceding twenty "
                 "discourses' arguments were all building toward"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a plain question with a precisely worded "
                       "answer, best read as the vagga's summation"),
    ],
    why=(
        "After twenty discourses arguing that the five aggregates "
        "are impermanent, suffering, and not-self &mdash; directly, "
        "by logical derivation, and through their causes &mdash; "
        "this closing discourse steps back and asks the plainest "
        "possible question. Ānanda goes to the Buddha and asks: "
        "people speak of &ldquo;cessation&rdquo; (nirodha) &mdash; "
        "the cessation of what things does this refer to? The "
        "Buddha's answer names the aggregates precisely, and adds a "
        "five-term description of their nature &mdash; impermanent, "
        "conditioned, dependently originated, liable to end, vanish, "
        "fade away, and cease &mdash; that reads as a compact summary "
        "of everything Aniccavagga has spent the preceding twenty "
        "discourses establishing."
    ),
    guide=[
        ("A question about vocabulary, not about doctrine", [
            "Ānanda's question is disarmingly direct: &ldquo;they "
            "speak of &lsquo;cessation.&rsquo; The cessation of what "
            "things does this refer to?&rdquo; He is not asking "
            "whether cessation is real, or how to attain it, or what "
            "it feels like &mdash; he is asking what the word itself "
            "picks out, treating &ldquo;cessation&rdquo; as a term "
            "already in wide circulation that nonetheless needs its "
            "referent pinned down precisely.",
        ]),
        ("An answer naming the aggregates directly", [
            "The Buddha's answer is exact rather than general: form "
            "is impermanent, conditioned, dependently originated, "
            "liable to end, vanish, fade away, and cease &mdash; and "
            "its cessation is what &ldquo;cessation&rdquo; refers to. "
            "The same five-term description and the same closing "
            "identification repeat for feeling, perception, choices, "
            "and consciousness. Cessation, in other words, is not a "
            "separate metaphysical event happening somewhere else; it "
            "is simply what happens to these five things, described "
            "with maximal precision.",
        ]),
        ("A five-term description doing the work of twenty discourses", [
            "The five terms applied to each aggregate &mdash; "
            "impermanent, conditioned, dependently originated, liable "
            "to end, vanish, fade away, and cease &mdash; gather up "
            "in a single compact phrase what SN 22.12-20 spent twenty "
            "discourses establishing from multiple angles: "
            "impermanence stated directly, derived logically, and "
            "traced to its cause. &ldquo;Conditioned&rdquo; "
            "(saṅkhata) and &ldquo;dependently originated&rdquo; "
            "(paṭiccasamuppanna) specifically recall SN 22.18-20's "
            "causal argument, naming the aggregates' dependent status "
            "explicitly rather than leaving it implicit.",
        ]),
        ("A fitting close to the vagga's own name", [
            "Aniccavagga &mdash; the &ldquo;impermanence chapter&rdquo; "
            "&mdash; closes with a discourse that defines, with "
            "unusual precision, the single word toward which all its "
            "argument had been pointing: not merely that the "
            "aggregates change, but that their ending is exactly what "
            "the entire tradition means when it speaks of "
            "&ldquo;cessation.&rdquo; The vagga that opened with SN "
            "22.12's compact four-step chain from seeing impermanence "
            "to full freedom closes by naming, with equal compactness, "
            "the precise target that freedom consists in reaching.",
        ]),
    ],
    terms=[
        ("nirodha",
         "&ldquo;cessation&rdquo; &mdash; the term Ānanda asks the "
         "Buddha to define precisely, and the word this discourse's "
         "entire dialogue turns on."),
        ("saṅkhata",
         "&ldquo;conditioned&rdquo; &mdash; one of the five "
         "descriptive terms the Buddha applies to each aggregate, "
         "naming its dependent, constructed nature."),
        ("paṭiccasamuppanna",
         "&ldquo;dependently originated&rdquo; &mdash; a second "
         "descriptive term, directly recalling SN 22.18-20's "
         "cause-based argument earlier in this vagga."),
        ("khayadhamma&hellip;vayadhamma&hellip;virāgadhamma&hellip;nirodhadhamma",
         "&ldquo;liable to end&hellip;vanish&hellip;fade "
         "away&hellip;cease&rdquo; &mdash; the remaining terms in the "
         "five-part description, each naming a distinct facet of the "
         "same underlying impermanence."),
        ("tassa nirodho",
         "&ldquo;its cessation&rdquo; &mdash; the Buddha's precise "
         "answer to Ānanda's question, identifying &ldquo;cessation&rdquo; "
         "directly with each aggregate's own ending."),
    ],
    text_intro=(
        "The discourse in full. Two elided repetitions (feeling and "
        "choices, each following the same five-term description "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.21:1.1-1.6"),
        ("p", "&sect;2", "sn22.21:1.12-1.14"),
    ],
    quiz=[
        {"q": "What question does Ānanda ask the Buddha at the start of this discourse?",
         "opts": [
             "People speak of \"cessation\" — the cessation of what things does this refer to?",
             "How long does it take to attain liberation?",
             "Why do the aggregates exist at all?",
             "What happens to an arahant after death?"],
         "correct": 0,
         "expl": "A question about the precise referent of a term already in circulation."},
        {"q": "What does the Buddha's answer identify \"cessation\" with?",
         "opts": [
             "The cessation of the five aggregates specifically",
             "The cessation of the physical universe",
             "A future event unrelated to the aggregates",
             "The cessation of the Buddha's own teaching"],
         "correct": 0,
         "expl": "Nirodha is identified directly with each aggregate's own ending."},
        {"q": "What five-term description does the Buddha apply to each aggregate?",
         "opts": [
             "Impermanent, conditioned, dependently originated, liable to end, vanish, fade away, and cease",
             "Eternal, unconditioned, self-caused, stable, and unchanging",
             "Pleasant, painful, neutral, physical, and mental",
             "Visible, invisible, tangible, intangible, and conceptual"],
         "correct": 0,
         "expl": "A compact summary gathering up the vagga's preceding twenty discourses' arguments."},
        {"q": "Which two terms in this description specifically recall SN 22.18-20's earlier cause-based argument?",
         "opts": [
             "\"Conditioned\" and \"dependently originated\"",
             "\"Liable to end\" and \"vanish\"",
             "\"Fade away\" and \"cease\"",
             "None of the terms relate to SN 22.18-20"],
         "correct": 0,
         "expl": "Saṅkhata and paṭiccasamuppanna name the aggregates' dependent status explicitly."},
        {"q": "How does this discourse's question differ from questions about whether cessation is real or how to attain it?",
         "opts": [
             "It is a question about vocabulary — what the term \"cessation\" itself picks out",
             "It denies that cessation exists at all",
             "It asks for a detailed meditation technique",
             "It challenges the Buddha's authority to define the term"],
         "correct": 0,
         "expl": "Ānanda treats \"cessation\" as an existing term needing its referent pinned down precisely."},
        {"q": "What role does this discourse play in closing Aniccavagga?",
         "opts": [
             "It names precisely the single target all twenty preceding discourses' arguments were pointing toward",
             "It contradicts everything argued in the preceding twenty discourses",
             "It introduces an entirely new, unrelated topic",
             "It has no summarizing function within the vagga"],
         "correct": 0,
         "expl": "A fitting close to a vagga whose very name, Aniccavagga, means \"the impermanence chapter.\""},
        {"q": "How many aggregates does the Buddha's answer apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Feeling and choices are elided but follow the same pattern spelled out for form and consciousness."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "Who questions the Buddha in this discourse?",
         "opts": [
             "Venerable Ānanda",
             "Venerable Sāriputta",
             "The householder Hāliddikāni",
             "Venerable Mahākaccāna"],
         "correct": 0,
         "expl": "A shift from the impersonal direct teachings of SN 22.12-20 to a named questioner."},
        {"q": "What comes immediately after this discourse, moving beyond Aniccavagga?",
         "opts": [
             "SN 22.22, opening Bhāravagga, the vagga's third chapter",
             "A return to SN 22.1",
             "The end of the entire Khandhavagga",
             "A discourse from an entirely different saṃyutta"],
         "correct": 0,
         "expl": "The book's own systematic coverage continues into its next chapter."},
    ],
    marginalia=[
        ("A question about a word, not a doctrine", [
            "what does \"cessation\" refer to? &mdash;",
            "pinning down a term already in wide use",
        ]),
        ("Cessation identified directly with the aggregates", [
            "not a separate event elsewhere &mdash;",
            "simply what happens to these five things",
        ]),
        ("Five terms gathering up twenty discourses' worth of argument", [
            "conditioned, dependently originated &mdash;",
            "recalling the cause-based trio directly",
        ]),
        ("The vagga's own name, precisely defined at its close", [
            "Aniccavagga, the impermanence chapter &mdash;",
            "closing by naming impermanence's exact target",
        ]),
    ],
    further=[
        '<a href="%s/sn22.21/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.20.html">SN 22.20 &middot; Not-Self With Its '
        "Cause</a> &mdash; the previous discourse, closing the "
        "cause-based trio.",
        '<a href="sn-22.12.html">SN 22.12 &middot; Impermanence</a> '
        "&mdash; the vagga's opening discourse, whose compact chain "
        "this closing dialogue now names with equal precision.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.22 — Bhārasutta
# --------------------------------------------------------------------------- #
page(
    22, 22, "Bhāra", "The Burden of Responsibility",
    vagga="Bhāravagga",
    meta_title="SN 22.22 — The Burden of Responsibility | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Bhārasutta &mdash; the aggregates named a burden, the "
        "individual its bearer, craving its taking up, and craving's "
        "ending its putting down, closing with a famous verse. Opens "
        "Bhāravagga. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Four terms defined in sequence &mdash; burden, "
                 "bearer, taking up, putting down &mdash; followed by "
                 "a closing verse restating the same four terms in "
                 "poetry"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a compact and famous discourse, its imagery "
                       "doing much of the explanatory work"),
    ],
    why=(
        "This is the discourse that gives Bhāravagga its name, and "
        "it supplies one of the canon's most vivid and durable images "
        "for the five aggregates: a physical burden, carried, taken "
        "up, and capable of being set down. The Buddha defines four "
        "terms in strict sequence &mdash; the burden itself (the five "
        "grasping aggregates), the bearer of the burden (the "
        "individual, named by whatever name and clan they happen to "
        "have), the taking up of the burden (craving), and the "
        "putting down of the burden (craving's ending) &mdash; before "
        "restating the same four terms as a closing verse. Few "
        "discourses in this saṃyutta compress so much doctrinal "
        "content into so ordinary and physically graspable an image."
    ),
    guide=[
        ("Four terms, defined in one strict sequence", [
            "The Buddha announces he will teach four things together: "
            "the burden, its bearer, the taking up of the burden, and "
            "the putting down of the burden. Each is then defined in "
            "turn, with no digression between them &mdash; a "
            "structure that reads almost like a glossary, four "
            "entries long, building toward the closing verse that "
            "restates all four at once.",
        ]),
        ("The burden and its bearer, kept distinct", [
            "The burden itself is named plainly: the five grasping "
            "aggregates (pañcupādānakkhandhā) &mdash; form, feeling, "
            "perception, choices, and consciousness, each modified by "
            "the same &ldquo;grasping&rdquo; qualifier that "
            "distinguishes this discourse's vocabulary from the "
            "bare khandha terminology used elsewhere in the book. "
            "The bearer of the burden is, notably, not defined as an "
            "abstraction but as &ldquo;the individual&hellip;the "
            "venerable of such and such name and clan&rdquo; &mdash; "
            "a person with an ordinary name, carrying an "
            "extraordinarily heavy load.",
        ]),
        ("Taking up and putting down, both named as craving", [
            "The taking up of the burden is craving (taṇhā) that "
            "leads to future lives, spelled out in its familiar "
            "threefold form: craving for sensual pleasures, for "
            "existence, and for nonexistence &mdash; the same three "
            "types this vagga's own SN 22.31 will name again as the "
            "&ldquo;root of gloom.&rdquo; The putting down of the "
            "burden is defined as nothing more or less than that "
            "exact craving's fading away and cessation with nothing "
            "left over.",
        ]),
        ("A closing verse restating the whole teaching in miniature", [
            "The discourse closes by shifting into verse, restating "
            "the same four definitions in four compact lines: the "
            "aggregates are indeed burdens, the individual bears "
            "them, taking up the burden is suffering in the world, "
            "and putting it down is happiness. The final two lines "
            "add an image not present in the prose section at all "
            "&mdash; one who puts the burden down &ldquo;without "
            "taking up another&rdquo; has plucked out craving root "
            "and all, and is &ldquo;hungerless, quenched&rdquo; "
            "(nicchāto parinibbuto) &mdash; closing the discourse on "
            "the very word, parinibbuto, that names full liberation.",
        ]),
    ],
    terms=[
        ("pañcupādānakkhandhā",
         "&ldquo;the five grasping aggregates&rdquo; &mdash; this "
         "discourse's own name for &ldquo;the burden,&rdquo; "
         "distinguishing them from the bare aggregates by the "
         "grasping qualifier."),
        ("puggala",
         "&ldquo;the individual&rdquo; &mdash; the bearer of the "
         "burden, defined here concretely as a named person rather "
         "than as an abstraction."),
        ("bhārādāna",
         "&ldquo;the taking up of the burden&rdquo; &mdash; craving "
         "in its threefold form, leading to future lives."),
        ("bhāranikkhepana",
         "&ldquo;the putting down of the burden&rdquo; &mdash; that "
         "same craving's fading away and cessation with nothing left "
         "over."),
        ("nicchāto parinibbuto",
         "&ldquo;hungerless, quenched&rdquo; &mdash; the closing "
         "verse's final image, describing one who has put the burden "
         "down without taking up another."),
    ],
    text_intro=(
        "The discourse in full, including its closing verse. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.22:1.1-1.8"),
        ("p", "&sect;2", "sn22.22:2.1-2.4"),
        ("p", "&sect;3", "sn22.22:3.1-3.4"),
        ("p", "&sect;4", "sn22.22:4.1-4.3"),
        ("p", "&sect;5", "sn22.22:5.1-5.2"),
        ("p", "&sect;6", "sn22.22:6.1-6.4"),
        ("p", "&sect;7", "sn22.22:7.1-7.4"),
    ],
    quiz=[
        {"q": "What four terms does the Buddha announce he will teach at the start of this discourse?",
         "opts": [
             "The burden, the bearer of the burden, the taking up of the burden, and the putting down of the burden",
             "Birth, aging, illness, and death",
             "The four noble truths",
             "The four elements"],
         "correct": 0,
         "expl": "Defined in strict sequence, then restated together as a closing verse."},
        {"q": "What is named as \"the burden\" itself?",
         "opts": [
             "The five grasping aggregates",
             "A physical object the Buddha once carried",
             "The monastic robe",
             "The weight of past misdeeds only"],
         "correct": 0,
         "expl": "Pañcupādānakkhandhā — form, feeling, perception, choices, and consciousness, each marked as \"grasping.\""},
        {"q": "Who is named as \"the bearer of the burden\"?",
         "opts": [
             "The individual, named concretely by name and clan",
             "The gods collectively",
             "The Buddha alone",
             "No one — the burden has no bearer"],
         "correct": 0,
         "expl": "Defined as an ordinary named person, not an abstraction."},
        {"q": "What is defined as \"the taking up of the burden\"?",
         "opts": [
             "Craving in its threefold form: for sensual pleasures, existence, and nonexistence",
             "Physical exercise",
             "Formal ordination",
             "Sitting meditation"],
         "correct": 0,
         "expl": "Taṇhā leading to future lives — the same threefold craving named elsewhere in this vagga."},
        {"q": "What is defined as \"the putting down of the burden\"?",
         "opts": [
             "That same craving's fading away and cessation with nothing left over",
             "A different, unrelated form of craving",
             "Physical death",
             "Renouncing the aggregates while still craving them"],
         "correct": 0,
         "expl": "Craving's own ending, not the aggregates' destruction."},
        {"q": "What image does the closing verse add that the prose definitions did not include?",
         "opts": [
             "One who puts the burden down without taking up another is described as \"hungerless, quenched\"",
             "An image of a mountain being carried",
             "A description of the burden's exact physical weight",
             "A warning against ever setting the burden down"],
         "correct": 0,
         "expl": "Nicchāto parinibbuto — closing on the word for full liberation."},
        {"q": "How does the verse describe \"taking up the burden\" and \"putting it down\"?",
         "opts": [
             "Taking it up is suffering in the world; putting it down is happiness",
             "Both are described as equally neutral",
             "Taking it up is happiness; putting it down is suffering",
             "Neither is evaluated at all"],
         "correct": 0,
         "expl": "A direct moral contrast drawn in the closing verse."},
        {"q": "What later discourse in this same vagga names the identical threefold craving as \"the root of gloom\"?",
         "opts": [
             "SN 22.31",
             "SN 22.23",
             "SN 22.29",
             "SN 22.32"],
         "correct": 0,
         "expl": "The same craving for sensual pleasures, existence, and nonexistence recurs by name."},
        {"q": "How many aggregates does the discourse's definition of \"the burden\" include?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "All five, each qualified as \"grasping.\""},
        {"q": "What position does this discourse hold in Bhāravagga?",
         "opts": [
             "The opening discourse, giving the vagga its name",
             "The vagga's closing discourse",
             "The vagga's middle discourse",
             "It does not belong to this vagga"],
         "correct": 0,
         "expl": "Bhāravagga, \"the burden chapter,\" is named directly after this discourse's central image."},
    ],
    marginalia=[
        ("Four terms, one strict sequence", [
            "burden, bearer, taking up, putting down &mdash;",
            "a glossary built toward its own closing verse",
        ]),
        ("A named person carrying an extraordinary load", [
            "not an abstraction &mdash;",
            "\"the venerable of such and such name\"",
        ]),
        ("Taking up and putting down, both craving", [
            "the same craving, two directions &mdash;",
            "arising and ending named symmetrically",
        ]),
        ("Closing on the word for liberation itself", [
            "hungerless, quenched &mdash;",
            "parinibbuto, the discourse's final word",
        ]),
    ],
    further=[
        '<a href="%s/sn22.22/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.21.html">SN 22.21 &middot; With Ānanda</a> '
        "&mdash; the previous discourse, closing Aniccavagga.",
        '<a href="sn-22.23.html">SN 22.23 &middot; Complete '
        "Understanding</a> &mdash; the next discourse, a short "
        "companion pair of definitions.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.23 — Pariññasutta
# --------------------------------------------------------------------------- #
page(
    22, 23, "Pariññā", "Complete Understanding",
    vagga="Bhāravagga",
    meta_title="SN 22.23 — Complete Understanding | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Pariññasutta &mdash; a short paired definition, naming "
        "the aggregates as what should be completely understood and "
        "defining complete understanding as greed, hate, and "
        "delusion's ending. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Two terms defined as a matched pair, in the same "
                 "glossary-like style as SN 22.22"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and direct, its two definitions worth "
                       "sitting with despite their brevity"),
    ],
    why=(
        "This discourse is shorter than SN 22.22 but shares its "
        "structure closely: two terms, defined one after the other. "
        "What should be completely understood (pariññeyyā dhammā) "
        "is named plainly as the five aggregates. And complete "
        "understanding (pariññā) itself is defined, perhaps "
        "surprisingly given how technical the term can sound "
        "elsewhere in Abhidhamma-adjacent literature, in the "
        "plainest possible terms: the ending of greed, hate, and "
        "delusion. The object of understanding and the content of "
        "understanding are both named without elaboration, leaving "
        "the definition's compactness to do the teaching."
    ),
    guide=[
        ("What should be completely understood, named plainly", [
            "The discourse's first half answers its own question "
            "directly: the things that should be completely "
            "understood are form, feeling, perception, choices, and "
            "consciousness &mdash; the five aggregates, named here "
            "without the &ldquo;grasping&rdquo; qualifier SN 22.22 "
            "used for &ldquo;the burden.&rdquo;",
        ]),
        ("Complete understanding defined by its result, not its process", [
            "The discourse's second half is the more striking "
            "definition: complete understanding itself is defined "
            "not as a cognitive achievement, a specific insight, or a "
            "meditative attainment, but as the ending of the three "
            "root poisons &mdash; greed, hate, and delusion (rāga, "
            "dosa, moha). Understanding, on this definition, is "
            "measured by what it removes rather than by what "
            "additional knowledge it supplies.",
        ]),
        ("A companion piece to SN 22.22's burden imagery", [
            "Read next to SN 22.22, this discourse can be seen as "
            "supplying the cognitive counterpart to that discourse's "
            "physical imagery: where SN 22.22 described craving's "
            "taking up and putting down using the concrete image of a "
            "carried burden, this discourse names the same underlying "
            "process in more abstract, definitional terms &mdash; "
            "what must be understood, and what understanding itself "
            "consists in.",
        ]),
        ("A pattern the vagga will return to", [
            "This discourse's two-part definitional structure "
            "recurs in miniature throughout the rest of Bhāravagga "
            "&mdash; SN 22.31's gloom and its root, and SN 22.32's "
            "brittle and not-brittle, both share this same short, "
            "paired-definition form, distinct from the longer "
            "narrative or argued discourses elsewhere in the vagga.",
        ]),
    ],
    terms=[
        ("pariññeyyā dhammā",
         "&ldquo;the things that should be completely "
         "understood&rdquo; &mdash; named directly as the five "
         "aggregates, without the &ldquo;grasping&rdquo; qualifier "
         "SN 22.22 used."),
        ("pariññā",
         "&ldquo;complete understanding&rdquo; &mdash; defined here "
         "not as a cognitive process but by its result: the ending of "
         "greed, hate, and delusion."),
        ("rāga",
         "&ldquo;greed&rdquo; &mdash; the first of the three root "
         "poisons whose ending constitutes complete understanding."),
        ("dosa",
         "&ldquo;hate&rdquo; &mdash; the second of the three root "
         "poisons."),
        ("moha",
         "&ldquo;delusion&rdquo; &mdash; the third of the three root "
         "poisons, completing the standard triad found throughout the "
         "canon."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.23:1.1-1.9"),
    ],
    quiz=[
        {"q": "What does this discourse name as \"the things that should be completely understood\"?",
         "opts": [
             "Form, feeling, perception, choices, and consciousness",
             "Only the physical body",
             "The Buddha's biography",
             "The rules of monastic discipline"],
         "correct": 0,
         "expl": "The five aggregates, named without the \"grasping\" qualifier used in SN 22.22."},
        {"q": "How is \"complete understanding\" (pariññā) itself defined in this discourse?",
         "opts": [
             "As the ending of greed, hate, and delusion",
             "As a specific meditative absorption",
             "As the ability to recite scripture from memory",
             "As agreement with a particular philosophical position"],
         "correct": 0,
         "expl": "Defined by its result — what it removes — rather than by a cognitive process."},
        {"q": "What three root poisons does this discourse name?",
         "opts": [
             "Greed (rāga), hate (dosa), and delusion (moha)",
             "Fear, anger, and pride",
             "Doubt, restlessness, and sloth",
             "Craving, aversion, and ignorance of a different kind entirely"],
         "correct": 0,
         "expl": "The standard triad found throughout the canon."},
        {"q": "How does this discourse's structure compare to SN 22.22's?",
         "opts": [
             "A shorter, two-term version of the same glossary-like definitional style",
             "A narrative discourse with no definitions at all",
             "A direct contradiction of SN 22.22",
             "An entirely unrelated form, using verse throughout"],
         "correct": 0,
         "expl": "Two terms defined in sequence, mirroring SN 22.22's four-term structure at smaller scale."},
        {"q": "What relationship can this discourse be read as having to SN 22.22's burden imagery?",
         "opts": [
             "A cognitive counterpart, naming in abstract terms what SN 22.22 described with a physical image",
             "A direct rejection of SN 22.22's teaching",
             "An unrelated discourse on an entirely different topic",
             "A narrative sequel describing events after SN 22.22"],
         "correct": 0,
         "expl": "Both discourses concern the same underlying process, in different registers."},
        {"q": "Which other discourses in this vagga share this discourse's short, paired-definition structure?",
         "opts": [
             "SN 22.31 (gloom and its root) and SN 22.32 (brittle and not-brittle)",
             "SN 22.26-28, the gratification trio",
             "SN 22.22, the burden discourse, which has four terms instead of two",
             "No other discourse in the vagga shares this structure"],
         "correct": 0,
         "expl": "A recurring short definitional form distinct from the vagga's longer discourses."},
        {"q": "How many aggregates does this discourse's definition include?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Named together as a group."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "The default setting for most of this vagga's discourses."},
        {"q": "What does this discourse's definition of understanding by its result, rather than its process, emphasize?",
         "opts": [
             "That genuine understanding is measured by what it removes, not by additional knowledge gained",
             "That understanding requires years of scholarly study",
             "That understanding is impossible to define at all",
             "That understanding is identical to simple memorization"],
         "correct": 0,
         "expl": "A striking definitional choice worth sitting with despite the discourse's brevity."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.24, on directly knowing and completely understanding the aggregates",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "SN 22.24 extends the same vocabulary of understanding into a positive/negative argument."},
    ],
    marginalia=[
        ("Two terms, the same glossary style as SN 22.22", [
            "what to understand, and understanding itself &mdash;",
            "a shorter companion definition",
        ]),
        ("Defined by what it removes", [
            "not a further fact gained &mdash;",
            "greed, hate, delusion ended instead",
        ]),
        ("A cognitive counterpart to a physical image", [
            "SN 22.22's burden, carried and set down &mdash;",
            "this discourse's abstract, definitional register",
        ]),
        ("A short form recurring later in the vagga", [
            "paired definitions again in SN 22.31, 22.32 &mdash;",
            "distinct from the vagga's longer discourses",
        ]),
    ],
    further=[
        '<a href="%s/sn22.23/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.22.html">SN 22.22 &middot; The Burden of '
        "Responsibility</a> &mdash; the previous discourse, opening "
        "this vagga's own defining image.",
        '<a href="sn-22.24.html">SN 22.24 &middot; Directly '
        "Knowing</a> &mdash; the next discourse, an argued case for "
        "why understanding the aggregates matters.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.24 — Abhijānasutta
# --------------------------------------------------------------------------- #
page(
    22, 24, "Abhijāna", "Directly Knowing",
    vagga="Bhāravagga",
    meta_title="SN 22.24 — Directly Knowing | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Abhijānasutta &mdash; a mirrored positive/negative "
        "argument naming four conditions, all required together, for "
        "ending suffering. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A single sentence stated in negative form, then "
                 "restated in positive form, both times naming four "
                 "conditions jointly required"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "one compound sentence repeated twice, worth "
                       "reading slowly for its four joint conditions"),
    ],
    why=(
        "This discourse names four things that must happen "
        "together, not any one alone, for suffering to end: directly "
        "knowing (abhijānaṁ) an aggregate, completely understanding "
        "(parijānaṁ) it, having dispassion (virajjaṁ) for it, and "
        "giving it up (pajahaṁ). The discourse states this claim "
        "twice, first as a negative &mdash; without all four, you "
        "cannot end suffering &mdash; and then as its exact positive "
        "mirror &mdash; by doing all four, you can. The repetition is "
        "not padding; it makes explicit that these four are being "
        "presented as jointly necessary, not as four independent "
        "paths any one of which would suffice on its own."
    ),
    guide=[
        ("Four conditions named as a single compound requirement", [
            "The discourse's negative half states plainly: without "
            "directly knowing and completely understanding form, "
            "without dispassion for it and giving it up, you cannot "
            "end suffering. All four verbs &mdash; directly knowing, "
            "completely understanding, having dispassion, giving up "
            "&mdash; are bound together in one sentence, none singled "
            "out as sufficient on its own.",
        ]),
        ("A mirror image, not a new claim", [
            "The positive half restates the identical four conditions "
            "in the identical order, simply reversing the negation: "
            "by directly knowing and completely understanding form, "
            "having dispassion for it and giving it up, you can end "
            "suffering. Nothing is added or removed between the two "
            "halves &mdash; the discourse's entire argument consists "
            "in this single reversal.",
        ]),
        ("How this discourse's vocabulary connects to the rest of the vagga", [
            "&ldquo;Directly knowing&rdquo; and &ldquo;completely "
            "understanding&rdquo; directly recall SN 22.23's "
            "definitions immediately before this discourse &mdash; "
            "pariññā, understanding, was defined there as the ending "
            "of greed, hate, and delusion. This discourse now shows "
            "why that understanding matters practically: it is one of "
            "four jointly necessary steps, not a free-standing "
            "achievement complete in itself.",
        ]),
        ("Why four steps, not one", [
            "The discourse's insistence on all four conditions "
            "together, rather than treating any single one as "
            "sufficient, is itself a claim worth noting: knowing an "
            "aggregate's nature (directly knowing, completely "
            "understanding) does not by itself guarantee the "
            "affective and volitional response (dispassion, giving "
            "up) that liberation from suffering requires. Cognitive "
            "clarity and letting go are presented as distinct, "
            "equally necessary achievements.",
        ]),
    ],
    terms=[
        ("abhijānaṁ",
         "&ldquo;directly knowing&rdquo; &mdash; the first of four "
         "conditions this discourse names as jointly necessary for "
         "ending suffering."),
        ("parijānaṁ",
         "&ldquo;completely understanding&rdquo; &mdash; the second "
         "condition, the same pariññā defined in SN 22.23 immediately "
         "before this discourse."),
        ("virajjaṁ",
         "&ldquo;having dispassion&rdquo; &mdash; the third "
         "condition, marking a shift from cognitive knowing to "
         "affective release."),
        ("pajahaṁ",
         "&ldquo;giving up&rdquo; &mdash; the fourth condition, the "
         "volitional completion of the sequence."),
        ("dukkhassa antakiriyā",
         "&ldquo;ending of suffering&rdquo; &mdash; the outcome this "
         "discourse claims depends on all four conditions together, "
         "stated first negatively and then as its positive mirror."),
    ],
    text_intro=(
        "The discourse in full. Four elided repetitions in each half "
        "(feeling, perception, and choices spelled out in full for "
        "form and consciousness, in both the negative and positive "
        "statements) are given exactly as bilara-data preserves them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.24:1.1-1.6"),
        ("p", "&sect;2", "sn22.24:1.7-1.11"),
    ],
    quiz=[
        {"q": "What four conditions does this discourse name as jointly necessary for ending suffering?",
         "opts": [
             "Directly knowing, completely understanding, having dispassion for, and giving up an aggregate",
             "Generosity, ethics, patience, and wisdom",
             "Birth, aging, illness, and death",
             "Faith, energy, mindfulness, and concentration"],
         "correct": 0,
         "expl": "Bound together in one sentence, none presented as sufficient alone."},
        {"q": "How is the discourse's claim structured?",
         "opts": [
             "Stated first as a negative (without all four, you cannot end suffering), then as its exact positive mirror",
             "Stated only once, in positive form",
             "Stated as a question the Buddha leaves unanswered",
             "Stated as a narrative dialogue between two disciples"],
         "correct": 0,
         "expl": "The repetition makes explicit that the four conditions are jointly necessary."},
        {"q": "How does this discourse's vocabulary connect to SN 22.23 immediately before it?",
         "opts": [
             "\"Directly knowing\" and \"completely understanding\" directly recall SN 22.23's definition of pariññā",
             "There is no connection between the two discourses",
             "This discourse explicitly rejects SN 22.23's definition",
             "SN 22.23 is about an entirely different topic, the six sense fields"],
         "correct": 0,
         "expl": "This discourse shows why the understanding SN 22.23 defined matters practically."},
        {"q": "What does the discourse's insistence on all four conditions together, rather than any one alone, suggest?",
         "opts": [
             "That cognitive clarity and letting go are distinct, equally necessary achievements",
             "That only cognitive knowledge is required, and the rest follows automatically",
             "That only volitional effort is required, with no need for understanding",
             "That the four conditions are actually identical to one another"],
         "correct": 0,
         "expl": "Knowing an aggregate's nature does not by itself guarantee dispassion and giving up."},
        {"q": "What is the third of the four named conditions?",
         "opts": [
             "Having dispassion (virajjaṁ)",
             "Directly knowing (abhijānaṁ)",
             "Completely understanding (parijānaṁ)",
             "Giving up (pajahaṁ)"],
         "correct": 0,
         "expl": "Marking a shift from cognitive knowing to affective release, third in the sequence."},
        {"q": "What is the fourth and final condition named?",
         "opts": [
             "Giving up (pajahaṁ)",
             "Directly knowing (abhijānaṁ)",
             "Having dispassion (virajjaṁ)",
             "Completely understanding (parijānaṁ)"],
         "correct": 0,
         "expl": "The volitional completion of the four-step sequence."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "Is the positive half of this discourse a new claim, or a mirror of the negative half?",
         "opts": [
             "A precise mirror, restating the identical four conditions in the identical order with the negation simply reversed",
             "An entirely new and different claim",
             "A partial restatement that adds a fifth condition",
             "A rejection of the negative half's claim"],
         "correct": 0,
         "expl": "Nothing is added or removed between the two halves."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.25, on giving up desire and greed for the aggregates",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "SN 22.25 continues the vagga's vocabulary of giving up applied to desire and greed specifically."},
    ],
    marginalia=[
        ("Four conditions, bound together as one requirement", [
            "know, understand, dispassion, give up &mdash;",
            "none presented as sufficient alone",
        ]),
        ("A mirror, not a new argument", [
            "negative stated first &mdash;",
            "positive simply reverses the same four terms",
        ]),
        ("Understanding shown to matter practically", [
            "SN 22.23's pariññā, defined &mdash;",
            "this discourse: why it is necessary, not sufficient",
        ]),
        ("Knowing and letting go, kept distinct", [
            "cognitive clarity alone is not enough &mdash;",
            "dispassion and giving up named separately",
        ]),
    ],
    further=[
        '<a href="%s/sn22.24/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.23.html">SN 22.23 &middot; Complete '
        "Understanding</a> &mdash; the previous discourse, whose "
        "definition of pariññā this one shows to be practically "
        "necessary.",
        '<a href="sn-22.25.html">SN 22.25 &middot; Desire and '
        "Greed</a> &mdash; the next discourse, giving up desire and "
        "greed for each aggregate directly.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.25 — Chandarāgasutta
# --------------------------------------------------------------------------- #
page(
    22, 25, "Chandarāga", "Desire and Greed",
    vagga="Bhāravagga",
    meta_title="SN 22.25 — Desire and Greed | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Chandarāgasutta &mdash; a compact instruction to give up "
        "desire and greed for each aggregate, using the recurring "
        "\"cut off at the root\" formula. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A single instruction repeated once per aggregate, "
                 "each time paired with the recurring \"cut off at "
                 "the root\" formula"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and direct, its formula already "
                       "familiar from SN 22.3 earlier in the book"),
    ],
    why=(
        "This discourse is one of the plainest instructions in the "
        "vagga: give up desire and greed (chandarāga) for form, and "
        "that form will be given up, cut off at the root, made like "
        "a palm stump, obliterated, and unable to arise in the "
        "future. The same instruction and the same formula repeat "
        "for each remaining aggregate. The &ldquo;cut off at the "
        "root, made like a palm stump&rdquo; image is not new to "
        "this discourse &mdash; it appeared earlier in the book, in "
        "SN 22.3's description of how the Realized One has given up "
        "desire for each aggregate &mdash; but here it is offered "
        "directly as an instruction to the listener, not as a "
        "description of what the Buddha has already accomplished."
    ),
    guide=[
        ("An instruction, addressed to the listener directly", [
            "Where SN 22.3 described the Realized One's already-"
            "completed abandonment of desire using this same "
            "formula, this discourse addresses the mendicants "
            "directly in the imperative: give up desire and greed "
            "for form. The formula's content is unchanged, but its "
            "grammatical mood shifts from description to instruction.",
        ]),
        ("The formula's consequence, stated as an automatic result", [
            "The discourse frames what follows the instruction not as "
            "a further step requiring separate effort, but as an "
            "automatic consequence: give up desire and greed, "
            "&ldquo;thus that form will be given up, cut off at the "
            "root, made like a palm stump, obliterated, and unable to "
            "arise in the future.&rdquo; The single act of giving up "
            "desire is presented as sufficient on its own to produce "
            "this complete, irreversible result.",
        ]),
        ("A formula recurring across the book, now given as instruction", [
            "This exact phrase &mdash; cut off at the root, made like "
            "a palm stump, obliterated, unable to arise in the "
            "future &mdash; is one of the book's most recognizable "
            "recurring formulas, appearing already in SN 22.3's "
            "description of the Realized One. Its reappearance here, "
            "now addressed to an ordinary listener as something to be "
            "done rather than as an accomplished fact about the "
            "Buddha, extends the formula's reach from description to "
            "practice.",
        ]),
        ("A short, direct discourse between two more elaborate ones", [
            "Positioned between SN 22.24's four-condition argument "
            "and SN 22.26's extended first-person narrative about the "
            "Buddha's own pre-awakening reflection, this discourse's "
            "brevity and directness offer a brief pause &mdash; a "
            "single clear instruction, unadorned by argument or "
            "narrative, before the vagga's tone shifts again.",
        ]),
    ],
    terms=[
        ("chandarāga",
         "&ldquo;desire and greed&rdquo; &mdash; the discourse's "
         "title and its sole object of instruction, to be given up "
         "for each aggregate."),
        ("pahīna",
         "&ldquo;given up&rdquo; &mdash; the first term in the "
         "formula describing what happens to an aggregate once "
         "desire and greed for it are relinquished."),
        ("ucchinnamūla",
         "&ldquo;cut off at the root&rdquo; &mdash; part of the same "
         "recurring formula, first seen in this book at SN 22.3, "
         "describing complete rather than partial ending."),
        ("tālāvatthukata",
         "&ldquo;made like a palm stump&rdquo; &mdash; a tree cut so "
         "low it cannot regrow, the formula's central image for "
         "irreversibility."),
        ("āyatiṁ anuppādadhamma",
         "&ldquo;unable to arise in the future&rdquo; &mdash; the "
         "formula's closing term, specifying that what has been given "
         "up this way cannot recur."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same "
        "instruction and formula spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.25:1.1-1.3"),
        ("p", "&sect;2", "sn22.25:1.10-1.11"),
    ],
    quiz=[
        {"q": "What instruction does this discourse give for each aggregate?",
         "opts": [
             "Give up desire and greed for it",
             "Meditate on it in detail for many hours",
             "Discuss it with a teacher before acting",
             "Avoid all contact with it entirely"],
         "correct": 0,
         "expl": "Chandarāga — desire and greed — named as the sole object of instruction."},
        {"q": "What formula describes the result of giving up desire and greed for an aggregate?",
         "opts": [
             "Given up, cut off at the root, made like a palm stump, obliterated, unable to arise in the future",
             "Transformed into a different, subtler aggregate",
             "Temporarily suppressed but likely to return",
             "Left unchanged but no longer relevant"],
         "correct": 0,
         "expl": "A formula for complete, irreversible ending, not partial suppression."},
        {"q": "Where did this exact formula first appear earlier in the book?",
         "opts": [
             "SN 22.3, describing the Realized One's completed abandonment of desire",
             "SN 22.1, the book's opening discourse",
             "SN 22.12, opening Aniccavagga",
             "This formula appears here for the first time"],
         "correct": 0,
         "expl": "SN 22.3 used the identical formula to describe an already-accomplished fact about the Buddha."},
        {"q": "How does this discourse's use of the formula differ from SN 22.3's?",
         "opts": [
             "It addresses the listener directly as an instruction, rather than describing the Buddha's completed accomplishment",
             "It uses an entirely different formula with no relation to SN 22.3",
             "It denies that the formula from SN 22.3 is accurate",
             "It applies only to form, unlike SN 22.3's broader scope"],
         "correct": 0,
         "expl": "A shift in grammatical mood, from description to instruction, with the formula's content unchanged."},
        {"q": "How is the formula's result presented in relation to the instruction to give up desire?",
         "opts": [
             "As an automatic consequence, not requiring a separate additional step",
             "As an unrelated event that may or may not follow",
             "As something requiring years of additional practice",
             "As impossible to actually achieve"],
         "correct": 0,
         "expl": "The single act of giving up desire is presented as sufficient to produce the complete result."},
        {"q": "What position does this discourse hold between SN 22.24 and SN 22.26?",
         "opts": [
             "A short, direct instruction offering a brief pause between two more elaborate discourses",
             "The vagga's longest and most elaborate discourse",
             "An unrelated digression with no connection to its neighbors",
             "A direct contradiction of both surrounding discourses"],
         "correct": 0,
         "expl": "Positioned between SN 22.24's argument and SN 22.26's extended narrative."},
        {"q": "How many aggregates does this discourse's instruction apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What image does \"made like a palm stump\" convey?",
         "opts": [
             "A tree cut so low it cannot regrow, conveying irreversibility",
             "A tree that regrows quickly after cutting",
             "A tree that was never cut at all",
             "An unrelated agricultural practice"],
         "correct": 0,
         "expl": "The formula's central image for the completeness of the ending described."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.26, the Buddha's first-person account of his own pre-awakening reflection on the aggregates",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Opening the vagga's gratification/drawback/escape trio."},
    ],
    marginalia=[
        ("The same formula, now an instruction", [
            "SN 22.3 described it accomplished &mdash;",
            "this discourse asks the listener to do it",
        ]),
        ("A single act, a complete automatic result", [
            "give up desire &mdash;",
            "the rest follows without a separate step",
        ]),
        ("Cut off at the root, made like a palm stump", [
            "a recurring formula across the book &mdash;",
            "irreversibility as its central image",
        ]),
        ("A brief pause between two longer discourses", [
            "short and direct &mdash;",
            "before the vagga's tone shifts to narrative",
        ]),
    ],
    further=[
        '<a href="%s/sn22.25/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.24.html">SN 22.24 &middot; Directly '
        "Knowing</a> &mdash; the previous discourse, naming giving "
        "up as one of four jointly necessary conditions.",
        '<a href="sn-22.26.html">SN 22.26 &middot; Gratification</a> '
        "&mdash; the next discourse, the Buddha's own first-person "
        "pre-awakening reflection on the aggregates.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.26 — Assādasutta
# --------------------------------------------------------------------------- #
page(
    22, 26, "Assāda", "Gratification",
    vagga="Bhāravagga",
    meta_title="SN 22.26 — Gratification | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Assādasutta &mdash; the Buddha's own first-person "
        "account of the pre-awakening reflection that led him to "
        "discover gratification, drawback, and escape in each "
        "aggregate. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha, recounting his own pre-awakening "
                     "reflection in the first person"),
        ("Form", "An autobiographical narrative recalling a specific "
                 "line of inquiry pursued before awakening, closing "
                 "with the standard declaration of enlightenment"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a first-person narrative introducing a "
                       "three-part analytical framework used "
                       "throughout the rest of this vagga"),
    ],
    why=(
        "This discourse is a rare first-person window onto the "
        "Buddha's own reasoning before his awakening. He recalls "
        "asking himself, while still unawakened but intent on "
        "awakening, what the gratification (assāda), drawback "
        "(ādīnava), and escape (nissaraṇa) are with respect to each "
        "aggregate &mdash; and then recounts the answers he arrived "
        "at himself: pleasure and happiness are an aggregate's "
        "gratification; its impermanence, suffering, and "
        "perishability are its drawback; and removing desire and "
        "greed for it is the escape. Crucially, the discourse states "
        "explicitly that the Buddha withheld his announcement of "
        "awakening until this exact three-part understanding was "
        "complete &mdash; making this triad, on the discourse's own "
        "account, the specific content of what awakening consisted in."
    ),
    guide=[
        ("A question the Buddha asked himself before awakening", [
            "The discourse opens with an unusual first-person "
            "framing: &ldquo;before my awakening &mdash; when I was "
            "still unawakened but intent on awakening &mdash; I "
            "thought&rdquo; a specific question about each "
            "aggregate's gratification, drawback, and escape. This "
            "kind of explicit autobiographical recollection of a "
            "pre-awakening line of inquiry is relatively rare in the "
            "canon, and it frames what follows as the Buddha's own "
            "discovery rather than as instruction handed down to "
            "others.",
        ]),
        ("Three answers, found by his own reflection", [
            "The Buddha recounts finding his own answer to each "
            "part of the question: the pleasure and happiness that "
            "arise from an aggregate are its gratification; that same "
            "aggregate's impermanence, suffering, and liability to "
            "perish are its drawback; and removing and giving up "
            "desire and greed for it is the escape. All three terms "
            "are given for each of the five aggregates in turn.",
        ]),
        ("Awakening withheld until the triad was complete", [
            "The discourse's most striking claim comes after the "
            "three-part analysis: as long as the Buddha did not "
            "truly understand the five grasping aggregates' "
            "gratification, drawback, and escape &ldquo;for what "
            "they are,&rdquo; he did not announce his awakening to "
            "the world &mdash; but once he did understand them this "
            "way, he did announce it. This makes the gratification/"
            "drawback/escape triad, by the discourse's own account, "
            "the specific content that made the difference between "
            "withholding and announcing supreme awakening.",
        ]),
        ("A framework the vagga will now use twice more", [
            "This same assāda/ādīnava/nissaraṇa triad recurs in the "
            "two discourses immediately after this one, each "
            "presenting it from a different angle: SN 22.27 restates "
            "it as an active search (&ldquo;I went in search of "
            "&hellip; and I found it&rdquo;), and SN 22.28 extends it "
            "outward from the Buddha's own experience to a universal "
            "claim about all sentient beings.",
        ]),
    ],
    terms=[
        ("assāda",
         "&ldquo;gratification&rdquo; &mdash; the pleasure and "
         "happiness that arise from an aggregate, the first term of "
         "the triad this discourse introduces."),
        ("ādīnava",
         "&ldquo;drawback&rdquo; &mdash; an aggregate's impermanence, "
         "suffering, and liability to perish, the triad's second term."),
        ("nissaraṇa",
         "&ldquo;escape&rdquo; &mdash; removing and giving up desire "
         "and greed for an aggregate, the triad's third and final "
         "term."),
        ("anuttaraṁ sammāsambodhiṁ",
         "&ldquo;supreme perfect awakening&rdquo; &mdash; what the "
         "Buddha declares he would not announce until the "
         "gratification/drawback/escape triad was fully understood "
         "for all five aggregates."),
        ("akuppā me vimutti",
         "&ldquo;my freedom is unshakable&rdquo; &mdash; part of the "
         "discourse's closing declaration, the same knowledge and "
         "vision the Buddha reports arising once his understanding "
         "was complete."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same three-part "
        "reflection spelled out in full for form and consciousness) "
        "are given exactly as bilara-data preserves them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.26:1.2-1.11"),
        ("p", "&sect;2", "sn22.26:1.19-1.21"),
        ("p", "&sect;3", "sn22.26:2.1-2.2"),
        ("p", "&sect;4", "sn22.26:2.4-2.5"),
    ],
    quiz=[
        {"q": "What question does the Buddha recall asking himself before his awakening?",
         "opts": [
             "What is the gratification, drawback, and escape when it comes to each aggregate?",
             "How many aggregates are there in total?",
             "Which teacher should he study under next?",
             "How long would awakening take to achieve?"],
         "correct": 0,
         "expl": "An explicit first-person recollection of a pre-awakening line of inquiry."},
        {"q": "What does the Buddha identify as an aggregate's \"gratification\" (assāda)?",
         "opts": [
             "The pleasure and happiness that arise from it",
             "Its complete absence of any positive quality",
             "Its usefulness for physical survival alone",
             "Its social status value"],
         "correct": 0,
         "expl": "The first term of the triad, found through his own reflection."},
        {"q": "What does the Buddha identify as an aggregate's \"drawback\" (ādīnava)?",
         "opts": [
             "Its impermanence, suffering, and liability to perish",
             "Its color and physical appearance",
             "Its usefulness to other people",
             "Its cost in monetary terms"],
         "correct": 0,
         "expl": "The second term of the triad."},
        {"q": "What does the Buddha identify as an aggregate's \"escape\" (nissaraṇa)?",
         "opts": [
             "Removing and giving up desire and greed for it",
             "Physically destroying the aggregate",
             "Ignoring the aggregate entirely without further reflection",
             "Transferring attachment to a different aggregate"],
         "correct": 0,
         "expl": "The third and final term, completing the triad."},
        {"q": "What claim does the discourse make about when the Buddha announced his awakening?",
         "opts": [
             "He withheld announcing it until he truly understood the gratification/drawback/escape triad for all five aggregates",
             "He announced it immediately upon first sitting under the tree",
             "He never formally announced his awakening at all",
             "He announced it before understanding the aggregates at all"],
         "correct": 0,
         "expl": "Making the triad, by the discourse's own account, the specific content that made the difference."},
        {"q": "How do SN 22.27 and SN 22.28 relate to this discourse?",
         "opts": [
             "Both use the same gratification/drawback/escape triad, presented from different angles",
             "Both directly contradict this discourse's conclusions",
             "Neither has any relationship to this discourse",
             "Both replace the triad with an entirely different framework"],
         "correct": 0,
         "expl": "SN 22.27 as active search, SN 22.28 as a universal claim about all sentient beings."},
        {"q": "How many aggregates does the Buddha's reflection apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern spelled out for form and consciousness."},
        {"q": "What closing declaration follows the Buddha's account of his awakening?",
         "opts": [
             "\"My freedom is unshakable; this is my last rebirth; now there'll be no more future lives\"",
             "\"I shall now teach for eighty years without rest\"",
             "\"The aggregates no longer exist for anyone\"",
             "\"All beings are now automatically free\""],
         "correct": 0,
         "expl": "The standard arahant-declaration language, here applied to the Buddha's own awakening."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Under the Bodhi tree, narrated as it happened"],
         "correct": 0,
         "expl": "The teaching itself is given at Sāvatthī, though its content recalls events before awakening."},
        {"q": "Is this kind of explicit first-person pre-awakening recollection common in the canon?",
         "opts": [
             "No — this reading guide describes it as relatively rare",
             "Yes — every discourse in this saṃyutta uses this framing",
             "It is the only form of narration used anywhere in the canon",
             "The discourse itself claims to be unique in all literature"],
         "correct": 0,
         "expl": "Most discourses instruct mendicants directly rather than recalling the Buddha's own pre-awakening reasoning."},
    ],
    marginalia=[
        ("A question asked before awakening, not after", [
            "\"when I was still unawakened\" &mdash;",
            "a rare first-person window onto the search itself",
        ]),
        ("Three terms, one for each facet", [
            "gratification, drawback, escape &mdash;",
            "found by his own reflection, not received",
        ]),
        ("Awakening withheld until the triad was complete", [
            "not announced immediately &mdash;",
            "this exact understanding named as the difference",
        ]),
        ("A framework the vagga will use twice more", [
            "search, and universal application follow &mdash;",
            "SN 22.27-28 build on this discourse directly",
        ]),
    ],
    further=[
        '<a href="%s/sn22.26/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.25.html">SN 22.25 &middot; Desire and '
        "Greed</a> &mdash; the previous discourse, a direct "
        "instruction using a different recurring formula.",
        '<a href="sn-22.27.html">SN 22.27 &middot; Gratification '
        "(2nd)</a> &mdash; the next discourse, the same triad "
        "restated as an active search.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.27 — Dutiyaassādasutta
# --------------------------------------------------------------------------- #
page(
    22, 27, "Dutiyaassāda", "Gratification (2nd)",
    vagga="Bhāravagga",
    meta_title="SN 22.27 — Gratification (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaassādasutta &mdash; SN 22.26's triad restated in "
        "the language of active search: going in search of "
        "gratification, drawback, and escape, and finding each. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha, again recounting his own "
                     "pre-awakening effort in the first person"),
        ("Form", "The same gratification/drawback/escape triad as "
                 "SN 22.26, now cast as a deliberate, effortful "
                 "search rather than a spontaneous reflection"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "best read directly after SN 22.26, whose "
                       "triad it restates in a new register"),
    ],
    why=(
        "This discourse restates SN 22.26's exact three-part "
        "framework &mdash; gratification, drawback, and escape "
        "&mdash; but changes its verbs in a way that shifts the "
        "whole discourse's character: rather than recalling a "
        "moment of reflection (&ldquo;I thought&rdquo;), the Buddha "
        "describes active, effortful search &mdash; &ldquo;I went in "
        "search of form's gratification, and I found it. I've seen "
        "clearly with wisdom the full extent of form's "
        "gratification.&rdquo; The same three-part pattern repeats "
        "for drawback and escape, and then again for each remaining "
        "aggregate. Where SN 22.26 emphasized the content of what "
        "was understood, this discourse emphasizes the effort of "
        "seeking it out."
    ),
    guide=[
        ("The same triad, a different verb of engagement", [
            "SN 22.26 used &ldquo;I thought&rdquo; and &ldquo;it "
            "occurred to me&rdquo; &mdash; verbs of reflection. This "
            "discourse instead uses &ldquo;I went in search "
            "of&hellip;and I found it&rdquo; &mdash; verbs of active "
            "pursuit and discovery. Both discourses arrive at the "
            "identical three terms (gratification, drawback, escape) "
            "for the identical five aggregates, but the manner of "
            "arriving at them is described quite differently.",
        ]),
        ("A claim of thoroughness, added to each term", [
            "Beyond simply finding each of the three, this discourse "
            "adds a further claim not present in SN 22.26's wording: "
            "&ldquo;I've seen clearly with wisdom the full extent of "
            "form's gratification&rdquo; &mdash; specifying not just "
            "that the search succeeded, but that what was found was "
            "grasped in its complete scope (yāvatā), leaving nothing "
            "further to discover.",
        ]),
        ("The same closing declaration, unchanged", [
            "As in SN 22.26, this discourse closes by stating that "
            "the Buddha withheld his announcement of awakening until "
            "this understanding &mdash; now described as a "
            "thoroughly searched-out and completely seen "
            "understanding &mdash; was in place for all five "
            "aggregates, followed by the identical knowledge-and-"
            "vision declaration that closed the previous discourse.",
        ]),
        ("Two discourses, two aspects of one achievement", [
            "Read as a pair, SN 22.26 and this discourse present "
            "awakening's content from two angles: SN 22.26 as "
            "something reflected on and understood, this discourse "
            "as something actively sought, found, and seen in full. "
            "Neither discourse is more authoritative than the other; "
            "together they present a fuller picture of what the "
            "search for awakening involved than either would alone.",
        ]),
    ],
    terms=[
        ("pariyesanaṁ acariṁ",
         "&ldquo;I went in search of&rdquo; &mdash; this discourse's "
         "distinctive verb of active pursuit, replacing SN 22.26's "
         "language of reflection."),
        ("adhigamā",
         "&ldquo;I found it&rdquo; &mdash; the result of the search, "
         "paired with each of the three terms in turn."),
        ("yāvatā&hellip;paññāya sudiṭṭhaṁ",
         "&ldquo;I've seen clearly with wisdom the full extent "
         "of&hellip;&rdquo; &mdash; a claim of thoroughness added to "
         "each term, not present in SN 22.26's wording."),
        ("assāda, ādīnava, nissaraṇa",
         "&ldquo;gratification, drawback, escape&rdquo; &mdash; the "
         "same three terms from SN 22.26, unchanged in content though "
         "differently framed."),
        ("akuppā me vimutti",
         "&ldquo;my freedom is unshakable&rdquo; &mdash; the same "
         "closing declaration that closed SN 22.26, repeated here "
         "unchanged."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same "
        "search-and-discovery pattern spelled out in full for form "
        "and consciousness) are given exactly as bilara-data "
        "preserves them. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.27:1.2-1.10"),
        ("p", "&sect;2", "sn22.27:1.20-1.22"),
        ("p", "&sect;3", "sn22.27:1.23-1.26"),
    ],
    quiz=[
        {"q": "What verb of engagement does this discourse use, differing from SN 22.26's \"I thought\"?",
         "opts": [
             "\"I went in search of... and I found it\"",
             "\"I was told by another\"",
             "\"I dreamed of\"",
             "\"I inherited the knowledge from a past life\""],
         "correct": 0,
         "expl": "Verbs of active pursuit and discovery, replacing SN 22.26's language of reflection."},
        {"q": "What three terms does this discourse's search apply to, identical to SN 22.26?",
         "opts": [
             "Gratification, drawback, and escape",
             "Birth, aging, and death",
             "Generosity, ethics, and wisdom",
             "Form, feeling, and perception only"],
         "correct": 0,
         "expl": "The same triad from SN 22.26, unchanged in content."},
        {"q": "What additional claim does this discourse add to each term, not present in SN 22.26?",
         "opts": [
             "\"I've seen clearly with wisdom the full extent of it\"",
             "A claim that the search took exactly seven years",
             "A claim that another teacher confirmed the finding",
             "A denial that the search was ever completed"],
         "correct": 0,
         "expl": "A claim of thoroughness — grasping the term's complete scope, not just finding it."},
        {"q": "How does this discourse's closing declaration compare to SN 22.26's?",
         "opts": [
             "Identical — the same knowledge-and-vision declaration, and the same claim about withholding awakening's announcement",
             "Completely different, with no shared wording",
             "This discourse omits the closing declaration entirely",
             "This discourse adds an entirely new fourth term"],
         "correct": 0,
         "expl": "The same closing content, framed after a differently described search."},
        {"q": "How can SN 22.26 and this discourse be read together as a pair?",
         "opts": [
             "As two aspects of one achievement — reflection and understanding, versus active search and thorough seeing",
             "As direct contradictions of one another",
             "As entirely unrelated discourses placed together by coincidence",
             "As one discourse being a later forgery of the other"],
         "correct": 0,
         "expl": "Together they present a fuller picture than either discourse alone."},
        {"q": "How many aggregates does this discourse's search apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern spelled out for form and consciousness."},
        {"q": "What does \"yāvatā\" (the full extent) specify in this discourse's claim?",
         "opts": [
             "That what was found was grasped in its complete scope, leaving nothing further to discover",
             "That the search covered only a small portion of the topic",
             "That the search was abandoned before completion",
             "That the search applies only to advanced practitioners"],
         "correct": 0,
         "expl": "A claim of thoroughness distinguishing this discourse from SN 22.26's simpler statement."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Under the Bodhi tree, narrated as it happened"],
         "correct": 0,
         "expl": "The teaching is given at Sāvatthī, though its content recalls the pre-awakening search."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.28, extending the triad to a universal claim about all sentient beings",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The third term of the vagga's gratification/drawback/escape trio."},
        {"q": "Does this discourse present a different set of three terms from SN 22.26?",
         "opts": [
             "No — the identical three terms, gratification, drawback, and escape",
             "Yes — an entirely different set of terms",
             "It presents only two of the three terms",
             "It adds a fourth term not found in SN 22.26"],
         "correct": 0,
         "expl": "The content is unchanged; only the framing verbs differ."},
    ],
    marginalia=[
        ("Reflection becomes active search", [
            "\"I thought\" becomes \"I went in search of\" &mdash;",
            "the same triad, a different verb of engagement",
        ]),
        ("A claim of thoroughness added", [
            "not just found, but seen in full extent &mdash;",
            "nothing further left to discover",
        ]),
        ("The same closing declaration, unchanged", [
            "unshakable freedom, last rebirth &mdash;",
            "identical wording to SN 22.26's close",
        ]),
        ("Two aspects of one achievement", [
            "reflection, then active search &mdash;",
            "neither more authoritative than the other",
        ]),
    ],
    further=[
        '<a href="%s/sn22.27/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.26.html">SN 22.26 &middot; Gratification</a> '
        "&mdash; the previous discourse, the same triad framed as "
        "reflection rather than search.",
        '<a href="sn-22.28.html">SN 22.28 &middot; Gratification '
        "(3rd)</a> &mdash; the next discourse, extending the triad "
        "to a universal claim about all sentient beings.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.28 — Tatiyaassādasutta
# --------------------------------------------------------------------------- #
page(
    22, 28, "Tatiyaassāda", "Gratification (3rd)",
    vagga="Bhāravagga",
    meta_title="SN 22.28 — Gratification (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Tatiyaassādasutta &mdash; the gratification/drawback/"
        "escape triad extended from the Buddha's own case to a "
        "universal claim about all sentient beings. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants in the third person, about sentient "
                     "beings generally"),
        ("Form", "A conditional argument (\"if there were no X, "
                 "beings wouldn't Y — but since there is X, beings "
                 "do Y\") applied to each term of the triad in turn"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "closes the trio by generalizing beyond the "
                       "Buddha's own first-person case"),
    ],
    why=(
        "This discourse closes the vagga's gratification/drawback/"
        "escape trio by making a move neither SN 22.26 nor SN 22.27 "
        "made: it steps entirely out of the first person. Rather "
        "than recounting what the Buddha himself thought, sought, or "
        "found, this discourse states a universal conditional claim "
        "about all sentient beings: if there were no gratification "
        "in form, beings would not be aroused by it &mdash; but "
        "since there is, they are. If form had no drawback, beings "
        "would not grow disillusioned with it &mdash; but since it "
        "has one, they do. If there were no escape from form, beings "
        "could not escape it &mdash; but since there is, they can. "
        "The same three-part reasoning generalizes the Buddha's own "
        "discovery into a claim about how the aggregates function "
        "for anyone at all."
    ),
    guide=[
        ("From one person's discovery to a general claim", [
            "SN 22.26 and SN 22.27 both concerned the Buddha's own "
            "path to awakening, told in the first person. This "
            "discourse instead makes a claim in the third person "
            "about sentient beings (sattā) generally &mdash; not "
            "what the Buddha found, but what the existence of "
            "gratification, drawback, and escape makes possible for "
            "anyone at all.",
        ]),
        ("A conditional structure, run for each term of the triad", [
            "Each of the three terms gets the identical conditional "
            "treatment: a counterfactual clause (if there were no "
            "gratification in form) followed by its negative "
            "consequence (beings would not be aroused by it), then "
            "the actual case (but since there is gratification) "
            "followed by its actual consequence (beings are aroused "
            "by it). This pattern repeats for drawback (disillusioned) "
            "and escape (able to escape), for each aggregate in turn.",
        ]),
        ("Why beings are drawn to what will also let them go", [
            "The argument's structure makes a point worth sitting "
            "with: an aggregate's gratification is precisely what "
            "explains why beings are drawn toward it in the first "
            "place, and its drawback is precisely what explains why "
            "that same attraction eventually gives way to "
            "disillusionment. Gratification and drawback are not "
            "presented as competing forces but as two real features "
            "of the same aggregates, each doing real explanatory "
            "work at a different stage.",
        ]),
        ("The trio's closing statement", [
            "The discourse closes not with the personal knowledge-"
            "and-vision declaration that ended SN 22.26 and SN "
            "22.27, but with a general statement about escaping the "
            "world: as long as sentient beings do not truly "
            "understand this triad, they have not escaped the world "
            "and do not live liberated with a mind free of limits; "
            "once they do understand it, they have. The trio thus "
            "moves from the Buddha's own case (SN 22.26-27) to "
            "everyone's case (this discourse), closing on the same "
            "understanding made available in principle to any being "
            "at all.",
        ]),
    ],
    terms=[
        ("sattā",
         "&ldquo;sentient beings&rdquo; &mdash; this discourse's "
         "subject, replacing the first-person &ldquo;I&rdquo; of SN "
         "22.26-27 with a general third-person claim."),
        ("abhinandeyyuṁ",
         "&ldquo;would be aroused by it&rdquo; &mdash; the "
         "consequence attached to gratification's presence, part of "
         "the discourse's conditional structure."),
        ("nibbindeyyuṁ",
         "&ldquo;would grow disillusioned&rdquo; &mdash; the "
         "consequence attached to drawback's presence, the same "
         "verb used in the liberation chain elsewhere in this book."),
        ("nissareyyuṁ",
         "&ldquo;would escape&rdquo; &mdash; the consequence attached "
         "to escape's presence, completing the discourse's threefold "
         "conditional structure."),
        ("vippamuttacetasā",
         "&ldquo;with a mind free of limits&rdquo; &mdash; part of "
         "the discourse's closing description of what understanding "
         "this triad makes possible for any sentient being."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same "
        "conditional structure spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.28:1.2-1.7"),
        ("p", "&sect;2", "sn22.28:1.13-1.17"),
        ("p", "&sect;3", "sn22.28:2.1-2.3"),
    ],
    quiz=[
        {"q": "How does this discourse's subject differ from SN 22.26 and SN 22.27?",
         "opts": [
             "It concerns sentient beings generally, in the third person, rather than the Buddha's own first-person case",
             "It concerns only the Buddha's closest disciples",
             "It concerns only animals, not humans",
             "It concerns only future generations, not present beings"],
         "correct": 0,
         "expl": "A shift from first-person narrative to a general third-person claim."},
        {"q": "What conditional structure does this discourse use for gratification?",
         "opts": [
             "\"If there were no gratification in form, beings wouldn't be aroused by it — but since there is, they are\"",
             "\"Gratification is entirely imaginary and has no real effect\"",
             "\"Gratification only affects a small minority of beings\"",
             "\"Gratification cannot be discussed in conditional terms\""],
         "correct": 0,
         "expl": "A counterfactual paired with the actual case, repeated for each term of the triad."},
        {"q": "What does the discourse claim explains why beings grow disillusioned with an aggregate?",
         "opts": [
             "The aggregate's drawback — if it had none, beings would not grow disillusioned",
             "Random chance with no underlying explanation",
             "External punishment imposed by others",
             "A decision made before birth"],
         "correct": 0,
         "expl": "The same conditional structure applied to drawback specifically."},
        {"q": "What relationship does the discourse suggest between gratification and drawback?",
         "opts": [
             "Both are real features of the same aggregates, each doing explanatory work at a different stage",
             "Gratification is real but drawback is entirely illusory",
             "The two are unrelated and never coexist",
             "Drawback always precedes gratification in time"],
         "correct": 0,
         "expl": "Gratification explains initial attraction; drawback explains eventual disillusionment."},
        {"q": "How does this discourse's closing differ from SN 22.26 and SN 22.27's?",
         "opts": [
             "It closes with a general statement about beings escaping the world, not the Buddha's personal knowledge-and-vision declaration",
             "It closes identically to both previous discourses",
             "It omits any closing statement entirely",
             "It closes with a warning rather than a positive statement"],
         "correct": 0,
         "expl": "The trio moves from the Buddha's own case to everyone's case."},
        {"q": "What does the discourse claim about beings who do not understand the triad?",
         "opts": [
             "They have not escaped the world and do not live liberated with a mind free of limits",
             "They are automatically reborn as animals",
             "They cannot ever learn the teaching in any future life",
             "They are punished directly by the Buddha"],
         "correct": 0,
         "expl": "A general claim about the consequence of not understanding gratification, drawback, and escape."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "How does this discourse complete the trio formed with SN 22.26 and SN 22.27?",
         "opts": [
             "As the third term, generalizing the Buddha's own first-person discovery into a universal claim",
             "As an unrelated discourse with no connection to the trio",
             "As a direct refutation of the previous two discourses",
             "As a simple repetition of SN 22.27 with no new content"],
         "correct": 0,
         "expl": "Reflection (SN 22.26), active search (SN 22.27), and now universal application (this discourse)."},
        {"q": "What discourse comes immediately after this one, closing the trio?",
         "opts": [
             "SN 22.29, on taking pleasure in the aggregates as taking pleasure in suffering",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The vagga continues with a new short discourse on pleasure and suffering."},
    ],
    marginalia=[
        ("From the Buddha's case to every being's case", [
            "first person, then third person &mdash;",
            "one discovery generalized into a universal claim",
        ]),
        ("A counterfactual, paired with the actual", [
            "if there were none, beings would not &mdash;",
            "but since there is, they do",
        ]),
        ("Attraction and disillusionment, both explained", [
            "gratification draws beings in &mdash;",
            "drawback is what eventually lets them go",
        ]),
        ("The trio's closing term", [
            "reflection, search, universal claim &mdash;",
            "three angles on one triad, now complete",
        ]),
    ],
    further=[
        '<a href="%s/sn22.28/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.27.html">SN 22.27 &middot; Gratification '
        "(2nd)</a> &mdash; the previous discourse, the same triad "
        "framed as the Buddha's own active search.",
        '<a href="sn-22.29.html">SN 22.29 &middot; Taking '
        "Pleasure</a> &mdash; the next discourse, on taking pleasure "
        "in an aggregate as taking pleasure in suffering itself.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.29 — Abhinandanasutta
# --------------------------------------------------------------------------- #
page(
    22, 29, "Abhinandana", "Taking Pleasure",
    vagga="Bhāravagga",
    meta_title="SN 22.29 — Taking Pleasure | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Abhinandanasutta &mdash; a compact chained argument: "
        "taking pleasure in an aggregate is taking pleasure in "
        "suffering itself, and freedom follows only from not doing "
        "so. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A two-step chained equation, run once in the "
                 "negative direction and once in the positive, for "
                 "each aggregate"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and tightly patterned, worth reading "
                       "slowly for its chained equation"),
    ],
    why=(
        "This discourse collapses two separate ideas &mdash; taking "
        "pleasure in an aggregate, and the aggregate's own nature as "
        "suffering &mdash; into a single unbroken equation: if you "
        "take pleasure in form, you take pleasure in suffering; and "
        "if you take pleasure in suffering, you are not free from "
        "suffering. The chain is then reversed for the discourse's "
        "second half: if you do not take pleasure in form, you do "
        "not take pleasure in suffering; and if you do not take "
        "pleasure in suffering, you are free from suffering. The "
        "argument's entire force rests on identifying &ldquo;taking "
        "pleasure in form&rdquo; with &ldquo;taking pleasure in "
        "suffering&rdquo; directly, rather than treating them as two "
        "separate facts that merely happen to correlate."
    ),
    guide=[
        ("An identity, not merely a correlation", [
            "The discourse's opening move is stated as a direct "
            "equation rather than a causal claim: &ldquo;if you take "
            "pleasure in form, you take pleasure in suffering&rdquo; "
            "&mdash; not &ldquo;taking pleasure in form leads to "
            "suffering&rdquo; but an identification of the two acts "
            "as the same act, differently described. This follows "
            "directly from the earlier vagga material (SN 22.13, and "
            "SN 22.15-17's chain) establishing that the aggregates "
            "simply are suffering.",
        ]),
        ("A second link, chained onto the first", [
            "The discourse does not stop at the first equation; it "
            "adds a second: &ldquo;if you take pleasure in suffering, "
            "you're not free from suffering, I say.&rdquo; The "
            "explicit &ldquo;I say&rdquo; (vadāmi) marks this second "
            "link as the Buddha's own direct claim rather than a "
            "further logical derivation, giving the two-step chain a "
            "personal authority distinct from a purely impersonal "
            "argument.",
        ]),
        ("The identical chain, run in reverse", [
            "The discourse's second half simply negates every term "
            "of the first: not taking pleasure in form means not "
            "taking pleasure in suffering, and not taking pleasure in "
            "suffering means being free from suffering. As with "
            "several other discourses in this book, the negative "
            "half adds no new content &mdash; it is included to make "
            "explicit that both directions of the equation hold, not "
            "only the direction warning against pleasure.",
        ]),
        ("A short discourse doing compact, careful work", [
            "Despite its brevity, this discourse performs a precise "
            "philosophical function: it forecloses a possible "
            "objection to the earlier claim that the aggregates are "
            "suffering &mdash; namely, that one could take pleasure "
            "in something that is nonetheless suffering without "
            "thereby being caught by that suffering. This discourse "
            "denies exactly that possibility, identifying the two "
            "acts as one.",
        ]),
    ],
    terms=[
        ("abhinandati",
         "&ldquo;takes pleasure in&rdquo; &mdash; the discourse's "
         "title verb, applied to each aggregate and, by the "
         "discourse's own equation, to suffering itself."),
        ("dukkhaṁ so abhinandati",
         "&ldquo;you take pleasure in suffering&rdquo; &mdash; the "
         "discourse's central identification, not a separate "
         "consequence but the same act redescribed."),
        ("vadāmi",
         "&ldquo;I say&rdquo; &mdash; marking the discourse's second "
         "link (pleasure in suffering means no freedom from "
         "suffering) as the Buddha's own direct claim."),
        ("dukkhā aparimutto",
         "&ldquo;not free from suffering&rdquo; &mdash; the negative "
         "half's conclusion, mirrored by its positive opposite in the "
         "discourse's second half."),
        ("na dukkhā parimutto",
         "&ldquo;free from suffering&rdquo; &mdash; the positive "
         "half's conclusion, reached simply by negating every term of "
         "the first half's chain."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each half "
        "(feeling, perception, and choices, each following the same "
        "chained equation spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.29:1.2-1.3"),
        ("p", "&sect;2", "sn22.29:1.7-1.8"),
        ("p", "&sect;3", "sn22.29:1.9-1.10"),
        ("p", "&sect;4", "sn22.29:1.14-1.15"),
    ],
    quiz=[
        {"q": "What does this discourse claim about taking pleasure in form?",
         "opts": [
             "It is identical to taking pleasure in suffering, not merely correlated with it",
             "It is entirely unrelated to suffering",
             "It only sometimes leads to suffering, depending on circumstances",
             "It is the only path to genuine happiness"],
         "correct": 0,
         "expl": "A direct equation, stated as an identity rather than a causal claim."},
        {"q": "What second link does the discourse chain onto the first?",
         "opts": [
             "If you take pleasure in suffering, you are not free from suffering",
             "If you take pleasure in suffering, you become free from suffering",
             "Taking pleasure in suffering has no further consequence",
             "Taking pleasure in suffering only affects consciousness, not the other aggregates"],
         "correct": 0,
         "expl": "Marked with the Buddha's explicit \"I say\" (vadāmi), giving it personal authority."},
        {"q": "What does the discourse's second half do with the first half's chain?",
         "opts": [
             "Negates every term, producing the exact mirror-image positive chain",
             "Adds an entirely new fourth term",
             "Contradicts the first half's conclusion",
             "Repeats the first half without any change"],
         "correct": 0,
         "expl": "Not taking pleasure in form means not taking pleasure in suffering, and freedom follows."},
        {"q": "What possible objection does this discourse's identification of pleasure and suffering foreclose?",
         "opts": [
             "That one could take pleasure in something that is suffering without being caught by that suffering",
             "That suffering does not really exist",
             "That the aggregates are permanent",
             "That pleasure is always morally wrong to experience"],
         "correct": 0,
         "expl": "The discourse denies this possibility by identifying the two acts as one."},
        {"q": "How does this discourse connect to earlier material in this book (SN 22.13, SN 22.15-17)?",
         "opts": [
             "It builds directly on their established claim that the aggregates are suffering",
             "It directly contradicts their conclusions",
             "It has no relationship to any earlier discourse",
             "It replaces their claims with an entirely new framework"],
         "correct": 0,
         "expl": "The identity between pleasure-in-form and pleasure-in-suffering depends on form already being suffering."},
        {"q": "How many aggregates does this discourse's chained equation apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What does the discourse's negative half add that is not already implied by the positive half?",
         "opts": [
             "Nothing new — it makes explicit that both directions of the equation hold",
             "An entirely different conclusion about a different aggregate",
             "A denial of the positive half's claim",
             "A new fourth term not present in the positive half"],
         "correct": 0,
         "expl": "Included for explicitness, following the same pattern as other paired discourses in this book."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.30, on the arising and cessation of the aggregates using disease-related vocabulary",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The vagga continues with a discourse using distinctive medical imagery."},
        {"q": "Is the claim in this discourse presented as a causal chain or an identity?",
         "opts": [
             "An identity — the same act described in two different ways, not two separate facts that merely correlate",
             "A purely causal chain with no identity claim at all",
             "Neither — the discourse makes no logical claim of any kind",
             "A statistical correlation observed across many cases"],
         "correct": 0,
         "expl": "The discourse's force rests on this identification rather than a weaker causal claim."},
    ],
    marginalia=[
        ("An identity, not a mere correlation", [
            "pleasure in form is pleasure in suffering &mdash;",
            "the same act, differently described",
        ]),
        ("A second link marked with the Buddha's own voice", [
            "\"I say\" &mdash;",
            "personal authority, not just logical derivation",
        ]),
        ("The chain reversed, term for term", [
            "not taking pleasure, not caught by suffering &mdash;",
            "freedom follows the identical structure",
        ]),
        ("A possible escape route, closed off", [
            "no pleasure-in-suffering without being caught &mdash;",
            "compact work for so short a discourse",
        ]),
    ],
    further=[
        '<a href="%s/sn22.29/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.28.html">SN 22.28 &middot; Gratification '
        "(3rd)</a> &mdash; the previous discourse, closing the "
        "vagga's gratification/drawback/escape trio.",
        '<a href="sn-22.30.html">SN 22.30 &middot; Arising</a> '
        "&mdash; the next discourse, using distinctive medical "
        "imagery for the aggregates' arising and cessation.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.30 — Uppādasutta
# --------------------------------------------------------------------------- #
page(
    22, 30, "Uppāda", "Arising",
    vagga="Bhāravagga",
    meta_title="SN 22.30 — Arising | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Uppādasutta &mdash; the aggregates' arising and "
        "cessation described in distinctive medical vocabulary, as "
        "the arising and cessation of disease itself. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A single equation stated for arising, then its "
                 "mirror stated for cessation, using disease-related "
                 "vocabulary distinctive within this vagga"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "notable chiefly for its distinctive medical "
                       "vocabulary among this vagga's discourses"),
    ],
    why=(
        "Most discourses in this saṃyutta describe the aggregates' "
        "arising and ending using the vocabulary of suffering "
        "directly &mdash; sorrow, lamentation, pain, distress. This "
        "discourse reaches instead for the vocabulary of illness: "
        "the arising, continuation, and manifestation of form is "
        "described as &ldquo;the arising of suffering, the "
        "continuation of diseases (rogānaṁ ṭhiti), and the "
        "manifestation of old age and death&rdquo; &mdash; and its "
        "cessation, correspondingly, as suffering's cessation, "
        "disease's settling, and old age and death's disappearance. "
        "Casting the aggregates' very arising as something already "
        "diagnosable, already symptomatic, is a distinctive framing "
        "not repeated elsewhere in this vagga."
    ),
    guide=[
        ("Arising described in the vocabulary of disease", [
            "The discourse's opening claim pairs three verbs "
            "(arising, continuation, manifestation and regeneration) "
            "with three matching consequences: the arising of "
            "suffering, the continuation of diseases, and the "
            "manifestation of old age and death. This three-part "
            "correspondence is more elaborate than the simple "
            "arising/ceasing pairs found in most of this vagga's "
            "other discourses.",
        ]),
        ("Cessation as recovery, not merely absence", [
            "The discourse's second half mirrors the first exactly: "
            "the cessation, settling, and disappearance of form is "
            "the cessation of suffering, the settling of diseases, "
            "and the disappearance of old age and death. The "
            "vocabulary of &ldquo;settling&rdquo; (vūpasama), "
            "applied specifically to disease, reads almost like a "
            "description of convalescence &mdash; not simply an "
            "absence of symptoms but a settling-down process.",
        ]),
        ("A single discourse's distinctive vocabulary choice", [
            "This medical framing &mdash; disease arising and "
            "settling, rather than the more familiar sorrow-"
            "lamentation-pain-distress formula used elsewhere in this "
            "book &mdash; does not recur in the discourses "
            "immediately before or after this one. Its appearance "
            "here, once, is worth noting as one of several distinct "
            "vocabularies this saṃyutta uses to describe the same "
            "underlying claim about the aggregates' arising and "
            "ending.",
        ]),
        ("Old age and death named without further elaboration", [
            "Unlike SN 22.5's earlier discourse, which traced the "
            "aggregates' arising through the full twelve-link chain "
            "of dependent origination to reach old age and death, "
            "this discourse simply names old age and death directly "
            "as part of its threefold consequence, without spelling "
            "out any intervening links. The connection is asserted "
            "rather than argued.",
        ]),
    ],
    terms=[
        ("uppāda",
         "&ldquo;arising&rdquo; &mdash; the discourse's title term, "
         "paired here with continuation and manifestation as three "
         "aspects of an aggregate's coming to be."),
        ("rogānaṁ ṭhiti",
         "&ldquo;the continuation of diseases&rdquo; &mdash; this "
         "discourse's distinctive medical vocabulary, not repeated "
         "elsewhere in this vagga's other discourses."),
        ("jarāmaraṇassa pātubhāvo",
         "&ldquo;the manifestation of old age and death&rdquo; "
         "&mdash; named directly here without the intervening links "
         "SN 22.5 traced through dependent origination."),
        ("vūpasama",
         "&ldquo;settling&rdquo; &mdash; the term applied specifically "
         "to disease's cessation, suggesting a process of "
         "convalescence rather than mere absence."),
        ("dukkhassa nirodho",
         "&ldquo;the cessation of suffering&rdquo; &mdash; paired in "
         "this discourse with disease's settling and old age and "
         "death's disappearance, as the threefold mirror of the "
         "opening claim."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each half "
        "(feeling, perception, and choices, each following the same "
        "threefold correspondence spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.30:1.2-1.2"),
        ("p", "&sect;2", "sn22.30:1.6-1.6"),
        ("p", "&sect;3", "sn22.30:1.7-1.7"),
        ("p", "&sect;4", "sn22.30:1.11-1.11"),
    ],
    quiz=[
        {"q": "What vocabulary does this discourse use for the aggregates' arising, distinctive within this vagga?",
         "opts": [
             "The vocabulary of disease — the continuation of diseases, and the manifestation of old age and death",
             "The vocabulary of warfare and conquest",
             "The vocabulary of financial debt",
             "The vocabulary of weather and climate"],
         "correct": 0,
         "expl": "Rogānaṁ ṭhiti — a medical framing not repeated elsewhere in this vagga."},
        {"q": "What three-part correspondence does the discourse's opening claim make?",
         "opts": [
             "Arising, continuation, and manifestation of an aggregate correspond to suffering's arising, disease's continuation, and old age/death's manifestation",
             "A correspondence between form and consciousness only",
             "A correspondence between the aggregates and the six sense fields",
             "No correspondence is made — the discourse simply lists five aggregates"],
         "correct": 0,
         "expl": "A more elaborate three-part structure than the simple arising/ceasing pairs used elsewhere."},
        {"q": "What term describes disease's cessation in this discourse?",
         "opts": [
             "Vūpasama, \"settling\" — suggesting convalescence rather than mere absence",
             "Uppāda, \"arising\"",
             "Pātubhāva, \"manifestation\"",
             "Bhava, \"continued existence\""],
         "correct": 0,
         "expl": "A term that reads almost like a description of recovery, not simply symptom absence."},
        {"q": "How does this discourse's treatment of old age and death differ from SN 22.5's earlier discourse?",
         "opts": [
             "This discourse names old age and death directly without spelling out the intervening links of dependent origination",
             "This discourse denies any connection between the aggregates and old age and death",
             "This discourse uses the exact same twelve-link chain as SN 22.5",
             "This discourse claims old age and death are unrelated to the aggregates entirely"],
         "correct": 0,
         "expl": "The connection is asserted directly rather than argued through the full causal chain."},
        {"q": "How does the discourse's second half relate to its first half?",
         "opts": [
             "It mirrors the first half exactly, describing cessation, settling, and disappearance in place of arising, continuation, and manifestation",
             "It contradicts the first half entirely",
             "It introduces an entirely unrelated new claim",
             "It simply repeats the first half word for word with no change"],
         "correct": 0,
         "expl": "A precise structural mirror, term for term."},
        {"q": "Is this discourse's medical vocabulary repeated in the discourses immediately before or after it?",
         "opts": [
             "No — this reading guide notes it as a distinctive, non-repeated vocabulary choice",
             "Yes — every discourse in Bhāravagga uses this same vocabulary",
             "Yes — it is repeated in every discourse in the entire saṃyutta",
             "The discourse itself claims to be quoting an earlier text"],
         "correct": 0,
         "expl": "One of several distinct vocabularies this saṃyutta uses to describe the same underlying claim."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What does \"manifestation\" (pātubhāva) describe in this discourse's opening claim?",
         "opts": [
             "One of three aspects, alongside arising and continuation, of an aggregate's coming to be",
             "A separate, unrelated fourth term",
             "A term used only in the discourse's second half",
             "A term describing only consciousness, not the other aggregates"],
         "correct": 0,
         "expl": "Part of the threefold structure applied to each aggregate."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.31, on gloom and its root",
             "A return to SN 22.12",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Returning to the short, paired-definition style seen earlier in SN 22.23."},
    ],
    marginalia=[
        ("A one-time medical framing", [
            "disease, not the usual sorrow-lamentation formula &mdash;",
            "not repeated elsewhere in this vagga",
        ]),
        ("Settling, not merely absence", [
            "vūpasama, convalescence's own vocabulary &mdash;",
            "cessation described as a process",
        ]),
        ("Old age and death, named without the chain spelled out", [
            "unlike SN 22.5's full twelve links &mdash;",
            "the connection simply asserted here",
        ]),
        ("A precise mirror between arising and ceasing", [
            "three terms, then their three opposites &mdash;",
            "structure carried exactly across both halves",
        ]),
    ],
    further=[
        '<a href="%s/sn22.30/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.29.html">SN 22.29 &middot; Taking '
        "Pleasure</a> &mdash; the previous discourse, a short "
        "chained equation on pleasure and suffering.",
        '<a href="sn-22.31.html">SN 22.31 &middot; The Root of '
        "Gloom</a> &mdash; the next discourse, returning to the "
        "short paired-definition style seen in SN 22.23.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.31 — Aghamūlasutta
# --------------------------------------------------------------------------- #
page(
    22, 31, "Aghamūla", "The Root of Gloom",
    vagga="Bhāravagga",
    meta_title="SN 22.31 — The Root of Gloom | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Aghamūlasutta &mdash; the aggregates named as gloom "
        "itself, and craving named as gloom's root, using the exact "
        "threefold craving formula from SN 22.22. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Two terms defined as a matched pair, in the same "
                 "short glossary style as SN 22.23"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief, its force carried by the word "
                       "\"gloom\" itself"),
    ],
    why=(
        "This discourse returns to the short, two-term definitional "
        "style of SN 22.23 earlier in the vagga, but with a "
        "distinctive and unusually stark word choice: agha, "
        "&ldquo;gloom&rdquo; or &ldquo;misery.&rdquo; The five "
        "aggregates are named directly as gloom itself, and the root "
        "of that gloom is named as the identical threefold craving "
        "&mdash; for sensual pleasures, for existence, and for "
        "nonexistence &mdash; that SN 22.22 named as &ldquo;the "
        "taking up of the burden.&rdquo; Reading this discourse "
        "alongside SN 22.22 shows the same underlying claim about "
        "craving's role given two different images across the vagga: "
        "burden and bearer in one discourse, gloom and its root in "
        "another."
    ),
    guide=[
        ("Gloom, named directly as the aggregates themselves", [
            "The discourse's first definition is stark and "
            "unqualified: form, feeling, perception, choices, and "
            "consciousness are gloom (agha). Unlike many of this "
            "vagga's discourses, which describe the aggregates as "
            "leading to suffering or as suffering's proper "
            "characterization under certain conditions, this "
            "discourse simply identifies them with gloom outright, "
            "with no further qualification.",
        ]),
        ("The identical threefold craving from SN 22.22", [
            "The root of gloom is defined using language that "
            "matches SN 22.22's definition of &ldquo;the taking up of "
            "the burden&rdquo; almost word for word: craving that "
            "leads to future lives, mixed up with relishing and "
            "greed, taking pleasure wherever it alights &mdash; that "
            "is, craving for sensual pleasures, for existence, and "
            "for nonexistence. The repetition of this exact formula "
            "across two discourses in the same vagga is a deliberate "
            "echo, not a coincidence.",
        ]),
        ("Two images, one underlying claim", [
            "Where SN 22.22 cast the same craving as what a bearer "
            "&ldquo;takes up&rdquo; along with a physical burden, "
            "this discourse casts it as the root from which gloom "
            "grows &mdash; a different metaphor (weight carried, "
            "versus a plant's root system) applied to the identical "
            "underlying doctrinal content. Reading the two discourses "
            "together shows how this vagga varies its imagery while "
            "keeping its core claims about craving constant.",
        ]),
        ("A word chosen for its weight", [
            "&ldquo;Agha&rdquo; is a stronger, more visceral term "
            "than the more common dukkha used throughout most of "
            "this book &mdash; closer to &ldquo;misery&rdquo; or "
            "&ldquo;affliction&rdquo; than to the more clinical-"
            "sounding &ldquo;suffering.&rdquo; Its use here, applied "
            "directly and without qualification to the five "
            "aggregates themselves, gives this brief discourse an "
            "unusually blunt emotional register despite its "
            "definitional brevity.",
        ]),
    ],
    terms=[
        ("agha",
         "&ldquo;gloom&rdquo; or &ldquo;misery&rdquo; &mdash; this "
         "discourse's title term, applied directly to the five "
         "aggregates without qualification."),
        ("aghamūla",
         "&ldquo;the root of gloom&rdquo; &mdash; defined as craving, "
         "using language matching SN 22.22's definition of the "
         "taking up of the burden almost word for word."),
        ("ponobhavikā taṇhā",
         "&ldquo;craving that leads to future lives&rdquo; &mdash; "
         "the discourse's core term, identical in wording to SN "
         "22.22's earlier definition."),
        ("kāmataṇhā, bhavataṇhā, vibhavataṇhā",
         "&ldquo;craving for sensual pleasures, existence, and "
         "nonexistence&rdquo; &mdash; the standard threefold "
         "breakdown of craving, repeated here from SN 22.22."),
        ("nandirāgasahagatā",
         "&ldquo;mixed up with relishing and greed&rdquo; &mdash; "
         "part of the shared definitional formula connecting this "
         "discourse directly to SN 22.22's."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.31:1.1-1.10"),
    ],
    quiz=[
        {"q": "What word does this discourse use to name the aggregates directly, distinct from the more common \"suffering\"?",
         "opts": [
             "Agha, \"gloom\" or \"misery\"",
             "Nirodha, \"cessation\"",
             "Assāda, \"gratification\"",
             "Bhāra, \"burden\""],
         "correct": 0,
         "expl": "A stronger, more visceral term than the clinical-sounding dukkha used elsewhere."},
        {"q": "What is defined as \"the root of gloom\"?",
         "opts": [
             "Craving — the identical threefold craving from SN 22.22",
             "The Buddha's own teaching",
             "Physical pain alone",
             "Ignorance of monastic rules"],
         "correct": 0,
         "expl": "Craving for sensual pleasures, existence, and nonexistence, worded almost identically to SN 22.22."},
        {"q": "How does this discourse's definition of craving compare to SN 22.22's \"taking up of the burden\"?",
         "opts": [
             "Nearly word for word identical",
             "Completely different, sharing no vocabulary",
             "This discourse denies that craving plays any role",
             "This discourse defines a different, unrelated concept entirely"],
         "correct": 0,
         "expl": "A deliberate echo across two discourses in the same vagga."},
        {"q": "What two different images does this vagga use for the same underlying claim about craving?",
         "opts": [
             "A burden taken up and put down (SN 22.22), and a root from which gloom grows (this discourse)",
             "A river and a mountain",
             "A fire and a flood",
             "A boat and a bridge"],
         "correct": 0,
         "expl": "Different metaphors applied to the identical doctrinal content."},
        {"q": "How does this discourse's structure compare to SN 22.23 earlier in the vagga?",
         "opts": [
             "The same short, two-term definitional style",
             "An entirely different, much longer narrative structure",
             "A direct contradiction of SN 22.23's method",
             "This discourse has no structural similarity to any other in the vagga"],
         "correct": 0,
         "expl": "A recurring short definitional form used at several points in Bhāravagga."},
        {"q": "How many aggregates does this discourse's definition of \"gloom\" include?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Named together as a group."},
        {"q": "What three types of craving does this discourse name?",
         "opts": [
             "Craving for sensual pleasures, existence, and nonexistence",
             "Craving for food, shelter, and companionship",
             "Craving for wisdom, ethics, and concentration",
             "Craving for power, fame, and wealth"],
         "correct": 0,
         "expl": "The standard threefold breakdown found throughout the canon."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "Does this discourse qualify its claim that the aggregates are gloom, or state it outright?",
         "opts": [
             "It states it outright, with no further qualification",
             "It qualifies the claim extensively with several conditions",
             "It denies the claim entirely",
             "It applies the claim only to form, not the other aggregates"],
         "correct": 0,
         "expl": "A stark, unqualified identification, distinctive within this vagga's mostly more measured claims."},
        {"q": "What discourse comes immediately after this one, closing the vagga?",
         "opts": [
             "SN 22.32, on what is brittle and what is not brittle",
             "A return to SN 22.12",
             "A discourse from a different saṃyutta",
             "SN 22.33, opening the next vagga"],
         "correct": 0,
         "expl": "The vagga's final discourse, closing with a similar short paired definition."},
    ],
    marginalia=[
        ("A stronger word than the usual \"suffering\"", [
            "agha, gloom or misery &mdash;",
            "applied to the aggregates without qualification",
        ]),
        ("The identical craving, worded almost the same", [
            "matching SN 22.22 nearly verbatim &mdash;",
            "a deliberate echo across the vagga",
        ]),
        ("A root, not a burden", [
            "two different images &mdash;",
            "one unchanged underlying claim about craving",
        ]),
        ("Brevity carrying unusual emotional weight", [
            "a short definitional discourse &mdash;",
            "its single word choice doing the heavy lifting",
        ]),
    ],
    further=[
        '<a href="%s/sn22.31/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.30.html">SN 22.30 &middot; Arising</a> '
        "&mdash; the previous discourse, using distinctive medical "
        "vocabulary for the aggregates' arising and cessation.",
        '<a href="sn-22.32.html">SN 22.32 &middot; Brittle</a> '
        "&mdash; the next discourse, closing the vagga with a final "
        "short paired definition.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.32 — Pabhaṅgusutta
# --------------------------------------------------------------------------- #
page(
    22, 32, "Pabhaṅgu", "Brittle",
    vagga="Bhāravagga",
    meta_title="SN 22.32 — Brittle | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Pabhaṅgusutta &mdash; the aggregates named brittle, "
        "their cessation named not brittle, closing Bhāravagga on a "
        "final compact contrast. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A single contrast &mdash; brittle versus not "
                 "brittle &mdash; run once for each aggregate, "
                 "closing the vagga"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the vagga's shortest closing discourse, its "
                       "single image doing all the work"),
    ],
    why=(
        "This discourse closes Bhāravagga with its shortest and most "
        "concentrated image yet: pabhaṅgu, &ldquo;brittle&rdquo; "
        "&mdash; liable to break, crumble, or shatter. Form is "
        "brittle, the discourse states, but its cessation, settling, "
        "and ending is not brittle. The same contrast repeats for "
        "each remaining aggregate. Unlike SN 22.30's disease imagery "
        "or SN 22.31's gloom, brittleness names a physical property "
        "&mdash; a susceptibility to breaking under pressure or "
        "impact &mdash; giving the vagga's closing discourse a "
        "distinctly tactile, almost mundane image to end on, after "
        "eleven discourses ranging from the burden of SN 22.22 to "
        "the Buddha's own pre-awakening search in SN 22.26-28."
    ),
    guide=[
        ("A physical property, applied to the aggregates directly", [
            "The discourse's core claim is compact: form is brittle "
            "(pabhaṅgu). Unlike gloom (agha) in SN 22.31 or "
            "suffering (dukkha) used throughout the book, brittleness "
            "names a specific physical vulnerability &mdash; the "
            "tendency to break, crack, or shatter under strain "
            "&mdash; rather than a state of distress or affliction.",
        ]),
        ("Only cessation, not the aggregate, escapes the property", [
            "The discourse's second half draws a precise contrast: "
            "form's cessation, settling, and ending (nirodha, "
            "vūpasama, atthaṅgama) is not brittle. The aggregate "
            "itself is fragile and liable to break; what is not "
            "fragile, by this discourse's own account, is not some "
            "more durable version of the aggregate but its ending "
            "&mdash; the one thing about form that does not itself "
            "break down further.",
        ]),
        ("A closing image distinct from everything before it in the vagga", [
            "This discourse's brittleness imagery is not repeated "
            "anywhere else in Bhāravagga, joining SN 22.22's burden, "
            "SN 22.30's disease, and SN 22.31's gloom as one more "
            "distinct metaphor this vagga uses for the same "
            "underlying claim about the aggregates' vulnerability and "
            "their ending's freedom from that vulnerability.",
        ]),
        ("The vagga's closing note, compact rather than dramatic", [
            "Bhāravagga opened with SN 22.22's elaborate four-term "
            "burden imagery and closing verse, and included two "
            "extended first-person narratives (SN 22.26-27) recalling "
            "the Buddha's own pre-awakening search. It closes instead "
            "on this discourse's plainest possible contrast &mdash; "
            "brittle, not brittle &mdash; ending the vagga not with a "
            "dramatic flourish but with its shortest and most "
            "understated discourse.",
        ]),
    ],
    terms=[
        ("pabhaṅgu",
         "&ldquo;brittle&rdquo; &mdash; this discourse's title term "
         "and its central claim about each aggregate, a physical "
         "property distinct from the emotional or medical vocabulary "
         "used in nearby discourses."),
        ("nirodha",
         "&ldquo;cessation&rdquo; &mdash; the first of three terms "
         "describing what is, by contrast, not brittle."),
        ("vūpasama",
         "&ldquo;settling&rdquo; &mdash; the second term, the same "
         "word SN 22.30 applied specifically to disease's cessation."),
        ("atthaṅgama",
         "&ldquo;ending&rdquo; &mdash; the third and final term "
         "describing what is not brittle, completing the discourse's "
         "threefold description of cessation."),
        ("appabhaṅgu",
         "&ldquo;not brittle&rdquo; &mdash; the discourse's negated "
         "term, applied specifically and only to an aggregate's "
         "cessation, never to the aggregate itself."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same brittle/"
        "not-brittle contrast spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.32:1.1-1.6"),
        ("p", "&sect;2", "sn22.32:1.12-1.13"),
    ],
    quiz=[
        {"q": "What physical property does this discourse's title term, pabhaṅgu, name?",
         "opts": [
             "Brittleness — liable to break, crumble, or shatter",
             "Heaviness, like a physical burden",
             "Illness or disease",
             "Emotional gloom or misery"],
         "correct": 0,
         "expl": "A physical vulnerability, distinct from the emotional and medical vocabulary used in nearby discourses."},
        {"q": "What does the discourse claim is not brittle?",
         "opts": [
             "An aggregate's cessation, settling, and ending",
             "A more durable, permanent version of the aggregate itself",
             "Nothing — the discourse claims everything is brittle",
             "Only consciousness, unlike the other four aggregates"],
         "correct": 0,
         "expl": "The aggregate itself remains fragile; only its ending is described as not brittle."},
        {"q": "How does this discourse's imagery relate to SN 22.22, 22.30, and 22.31 earlier in the vagga?",
         "opts": [
             "It is one more distinct metaphor for the same underlying claim, joining burden, disease, and gloom",
             "It directly contradicts all three earlier discourses",
             "It repeats SN 22.31's exact wording without change",
             "It has no relationship to any earlier discourse in the vagga"],
         "correct": 0,
         "expl": "Four different images across the vagga, one consistent underlying claim about the aggregates."},
        {"q": "What three terms describe what is \"not brittle\" in this discourse?",
         "opts": [
             "Cessation, settling, and ending",
             "Arising, continuation, and manifestation",
             "Gratification, drawback, and escape",
             "Greed, hate, and delusion"],
         "correct": 0,
         "expl": "Nirodha, vūpasama, and atthaṅgama, applied specifically to an aggregate's ending."},
        {"q": "How does this discourse's tone compare to the vagga's opening discourse, SN 22.22?",
         "opts": [
             "More compact and understated, closing the vagga without a dramatic flourish",
             "Far more elaborate and dramatic than SN 22.22",
             "Identical in tone and length to SN 22.22",
             "This discourse rejects everything SN 22.22 established"],
         "correct": 0,
         "expl": "The vagga's shortest and most understated discourse, closing on a plain contrast."},
        {"q": "How many aggregates does this discourse's contrast apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What word, used in SN 22.30 for disease's cessation, reappears in this discourse?",
         "opts": [
             "Vūpasama, \"settling\"",
             "Agha, \"gloom\"",
             "Bhāra, \"burden\"",
             "Assāda, \"gratification\""],
         "correct": 0,
         "expl": "Applied here to an aggregate's own ending, echoing SN 22.30's medical vocabulary."},
        {"q": "What position does this discourse hold in Bhāravagga?",
         "opts": [
             "The vagga's closing discourse",
             "The vagga's opening discourse",
             "The vagga's middle discourse",
             "It does not belong to this vagga"],
         "correct": 0,
         "expl": "Ending the vagga on its most compact, understated contrast."},
        {"q": "What comes immediately after this discourse, moving beyond Bhāravagga?",
         "opts": [
             "SN 22.33, opening Natumhākavagga, the vagga's fourth chapter",
             "A return to SN 22.22",
             "The end of the entire Khandhavagga",
             "A discourse from an entirely different saṃyutta"],
         "correct": 0,
         "expl": "The book's own systematic coverage continues into its next chapter."},
    ],
    marginalia=[
        ("A physical property, not an emotional one", [
            "brittle, liable to break &mdash;",
            "distinct from gloom, disease, or burden",
        ]),
        ("Only the ending escapes the fragility", [
            "not a sturdier aggregate &mdash;",
            "cessation itself is what is not brittle",
        ]),
        ("A fourth distinct image in this vagga", [
            "burden, disease, gloom, brittleness &mdash;",
            "one claim, four different metaphors",
        ]),
        ("The vagga's quietest close", [
            "no dramatic flourish &mdash;",
            "the shortest discourse ending the longest set of images",
        ]),
    ],
    further=[
        '<a href="%s/sn22.32/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.31.html">SN 22.31 &middot; The Root of '
        "Gloom</a> &mdash; the previous discourse, sharing this "
        "discourse's short paired-definition style.",
        '<a href="sn-22.22.html">SN 22.22 &middot; The Burden of '
        "Responsibility</a> &mdash; the vagga's opening discourse, "
        "whose elaborate imagery this closing discourse's brevity "
        "now contrasts with.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.33 — Natumhākasutta
# --------------------------------------------------------------------------- #
page(
    22, 33, "Natumhāka", "It's Not Yours",
    vagga="Natumhākavagga",
    meta_title="SN 22.33 — It's Not Yours | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Natumhākasutta &mdash; give up what isn't yours, "
        "illustrated by the famous simile of the grass, sticks, and "
        "leaves in Jeta's Grove. Opens Natumhākavagga. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's "
                    "monastery"),
        ("Speakers", "The Buddha, in dialogue with the assembled "
                     "mendicants"),
        ("Form", "A direct instruction, then a famous simile drawn "
                 "from the immediate physical surroundings, then the "
                 "same instruction restated"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "the simile does most of the explanatory work, "
                       "making the argument unusually vivid"),
    ],
    why=(
        "This discourse opens Natumhākavagga and supplies one of the "
        "book's most immediate and physically grounded similes. "
        "Rather than reasoning abstractly about why the aggregates "
        "aren't self, the Buddha points to something literally lying "
        "on the ground around the assembly: the grass, sticks, "
        "branches, and leaves scattered through Jeta's Grove itself. "
        "If someone carried them off, burned them, or did whatever "
        "they liked with them, would the mendicants think, "
        "&ldquo;this person is doing this to us&rdquo;? Of course "
        "not &mdash; because that material is neither self nor "
        "belonging to self. The discourse then applies the identical "
        "logic to the five aggregates: give them up, precisely "
        "because they stand in the same relation to a person as "
        "Jeta's Grove's fallen leaves do."
    ),
    guide=[
        ("An instruction stated before its justification", [
            "The discourse opens with the bare instruction: give up "
            "what isn't yours, and doing so will be for your welfare "
            "and happiness. This is stated for each aggregate in turn "
            "before any explanation is offered &mdash; the listener "
            "is told what to do first, and only then shown why.",
        ]),
        ("A simile drawn from the immediate surroundings", [
            "Rather than reaching for an abstract comparison, the "
            "Buddha points directly at the physical setting: suppose "
            "someone carried off, burned, or otherwise did as they "
            "pleased with the grass, sticks, branches, and leaves "
            "scattered through Jeta's Grove &mdash; the very place "
            "where this teaching is being given. Would the "
            "mendicants think &ldquo;this person is carrying us off, "
            "burning us&rdquo;? The question is rhetorical, and the "
            "mendicants' own answer supplies the reasoning: no, "
            "because that material is &ldquo;neither self nor "
            "belonging to self.&rdquo;",
        ]),
        ("The same logic applied directly to the aggregates", [
            "The discourse closes by mapping the simile back onto its "
            "target with no remaining gap: &ldquo;in the same way, "
            "mendicants, form isn't yours: give it up.&rdquo; The "
            "aggregates are placed in precisely the same category as "
            "the fallen leaves &mdash; something present, usable, and "
            "even valuable in its own way, but not something whose "
            "handling by outside forces constitutes an assault on a "
            "self.",
        ]),
        ("A vagga named for its opening instruction, not its simile", [
            "Despite the vividness of the Jeta's Grove image, "
            "Natumhākavagga takes its name from the discourse's "
            "plainer opening phrase &mdash; &ldquo;it's not "
            "yours&rdquo; &mdash; rather than from the simile itself. "
            "This pattern (vagga named after a discourse's core claim "
            "rather than its most memorable illustration) recurs "
            "elsewhere in this saṃyutta, and is worth noting alongside "
            "Bhāravagga's own naming after SN 22.22's central image.",
        ]),
    ],
    terms=[
        ("na tumhākaṁ",
         "&ldquo;it's not yours&rdquo; &mdash; the discourse's title "
         "phrase and the vagga's own name, applied to each aggregate "
         "in turn."),
        ("pajahatha",
         "&ldquo;give up&rdquo; &mdash; the discourse's central "
         "imperative verb, addressed directly to the mendicants."),
        ("hitāya sukhāya",
         "&ldquo;for welfare and happiness&rdquo; &mdash; the "
         "promised result of giving up what isn't one's own, repeated "
         "after every instruction."),
        ("tiṇakaṭṭhasākhāpalāsa",
         "&ldquo;grass, sticks, branches, and leaves&rdquo; &mdash; "
         "the specific physical material the simile points to, drawn "
         "from the immediate setting of Jeta's Grove itself."),
        ("na attā na attaniya",
         "&ldquo;neither self nor belonging to self&rdquo; &mdash; "
         "the mendicants' own explanation for why the grove's fallen "
         "material provokes no sense of personal assault, mapped "
         "directly onto the aggregates."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each half "
        "(feeling, perception, and choices, each following the same "
        "instruction and simile spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.33:1.1-1.6"),
        ("p", "&sect;2", "sn22.33:1.12-1.13"),
        ("p", "&sect;3", "sn22.33:2.1-2.6"),
        ("p", "&sect;4", "sn22.33:2.7-2.8"),
        ("p", "&sect;5", "sn22.33:2.13-2.14"),
    ],
    quiz=[
        {"q": "What instruction opens this discourse?",
         "opts": [
             "Give up what's not yours, for your welfare and happiness",
             "Never leave the monastery grounds",
             "Give away all your possessions to laypeople",
             "Study every discourse the Buddha has given"],
         "correct": 0,
         "expl": "Stated for each aggregate before any explanation is offered."},
        {"q": "What physical objects does the Buddha's simile point to?",
         "opts": [
             "The grass, sticks, branches, and leaves scattered through Jeta's Grove itself",
             "The monastic robes worn by the mendicants",
             "A specific relic kept in the monastery",
             "Coins and other valuables"],
         "correct": 0,
         "expl": "Drawn directly from the immediate physical surroundings of the teaching itself."},
        {"q": "Why do the mendicants say they wouldn't feel assaulted if someone burned or carried off that material?",
         "opts": [
             "Because it is neither self nor belonging to self",
             "Because it has no monetary value",
             "Because the material technically belongs to someone else already",
             "Because mendicants are forbidden from having opinions on the matter"],
         "correct": 0,
         "expl": "Na attā na attaniya — the mendicants' own reasoning, then mapped directly onto the aggregates."},
        {"q": "How does the discourse close its argument?",
         "opts": [
             "By mapping the simile directly onto the aggregates: \"in the same way, form isn't yours: give it up\"",
             "By denying that the simile applies to the aggregates at all",
             "By introducing an entirely new, unrelated argument",
             "By leaving the connection between simile and aggregates unstated"],
         "correct": 0,
         "expl": "No remaining gap between the illustration and its target."},
        {"q": "What does Natumhākavagga take its name from?",
         "opts": [
             "This discourse's plainer opening phrase, \"it's not yours,\" rather than its vivid simile",
             "The exact wording of the simile itself",
             "A different discourse entirely, later in the vagga",
             "The name of a specific mendicant mentioned in the text"],
         "correct": 0,
         "expl": "A naming pattern (core claim over memorable illustration) seen elsewhere in this saṃyutta."},
        {"q": "How many aggregates does this discourse's instruction apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī, Jeta's Grove, Anāthapiṇḍika's monastery",
             "Devadaha",
             "Rājagaha, Vulture's Peak",
             "Kapilavatthu"],
         "correct": 0,
         "expl": "The specific setting is essential to the simile's immediacy — the grove itself is the example."},
        {"q": "What promised result follows from giving up what isn't yours?",
         "opts": [
             "Welfare and happiness",
             "Immediate rebirth as a deity",
             "Physical strength and long life",
             "Public recognition and honor"],
         "correct": 0,
         "expl": "Hitāya sukhāya, repeated after every instance of the instruction."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.34, a shorter companion restating the same instruction without the simile",
             "A return to SN 22.22",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "A shorter paired discourse, mirroring the vagga's opening instruction."},
        {"q": "Is the simile in this discourse an abstract comparison or drawn from the immediate setting?",
         "opts": [
             "Drawn directly from the immediate physical setting — the grove where the teaching is actually being given",
             "A purely abstract, hypothetical comparison with no connection to the setting",
             "A comparison to a distant, unnamed location",
             "A comparison to events from a past life"],
         "correct": 0,
         "expl": "Its immediacy is part of what makes the simile unusually vivid and persuasive."},
    ],
    marginalia=[
        ("An instruction given before its reason", [
            "give up what's not yours &mdash;",
            "the explanation follows only afterward",
        ]),
        ("A simile drawn from the ground underfoot", [
            "grass, sticks, leaves of this very grove &mdash;",
            "not an abstract, distant comparison",
        ]),
        ("Neither self nor belonging to self", [
            "the mendicants' own reasoning &mdash;",
            "mapped directly onto the five aggregates",
        ]),
        ("A vagga named for its claim, not its image", [
            "\"it's not yours,\" not \"the grove's leaves\" &mdash;",
            "the same pattern as Bhāravagga's own naming",
        ]),
    ],
    further=[
        '<a href="%s/sn22.33/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.32.html">SN 22.32 &middot; Brittle</a> '
        "&mdash; the previous discourse, closing Bhāravagga.",
        '<a href="sn-22.34.html">SN 22.34 &middot; It&rsquo;s Not '
        "Yours (2nd)</a> &mdash; the next discourse, the same "
        "instruction restated without the simile.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.34 — Dutiyanatumhākasutta
# --------------------------------------------------------------------------- #
page(
    22, 34, "Dutiyanatumhāka", "It's Not Yours (2nd)",
    vagga="Natumhākavagga",
    meta_title="SN 22.34 — It's Not Yours (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyanatumhākasutta &mdash; SN 22.33's instruction "
        "restated without its famous simile, closing on the bare "
        "imperative alone. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The identical instruction from SN 22.33, stripped "
                 "of its Jeta's Grove simile and closing with the "
                 "bare imperative restated once more"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and direct, best read as SN 22.33's "
                       "companion"),
    ],
    why=(
        "This discourse gives the identical instruction as SN 22.33 "
        "&mdash; give up what isn't yours, for your welfare and "
        "happiness, applied to each aggregate in turn &mdash; but "
        "omits the grass-and-leaves simile entirely. Where SN 22.33 "
        "spent roughly half its length illustrating why the "
        "aggregates aren't self, this discourse simply states the "
        "instruction, states it again for each aggregate, and closes "
        "by repeating the bare imperative once more without any "
        "supporting image at all. The comparison between the two "
        "discourses shows how the same content could be delivered "
        "either with or without its illustrative apparatus."
    ),
    guide=[
        ("The identical instruction, no simile attached", [
            "Every clause of this discourse's instruction matches SN "
            "22.33 exactly &mdash; give up what isn't yours, for your "
            "welfare and happiness, applied in turn to form, feeling, "
            "perception, choices, and consciousness. What is missing "
            "is the entire second half of SN 22.33: no grove, no "
            "grass and sticks, no rhetorical question to the "
            "assembled mendicants.",
        ]),
        ("A closing repetition standing in for the simile", [
            "In place of SN 22.33's illustrative closing section, "
            "this discourse simply repeats its own opening "
            "instruction once more: &ldquo;give up what's not yours. "
            "Giving it up will be for your welfare and "
            "happiness.&rdquo; The repetition itself, rather than an "
            "image, provides the discourse's sense of closure.",
        ]),
        ("What the comparison with SN 22.33 reveals", [
            "Reading these two discourses side by side shows that the "
            "instruction to give up the aggregates did not, in this "
            "tradition, require the Jeta's Grove simile to stand on "
            "its own &mdash; the bare imperative was evidently "
            "considered a complete teaching in itself, with the "
            "simile functioning as an optional, vivid elaboration "
            "rather than a logically necessary component.",
        ]),
        ("A short companion opening the vagga's second half of its opening pair", [
            "As the second of Natumhākavagga's own two &ldquo;it's not "
            "yours&rdquo; discourses, this brief companion sets the "
            "pattern the vagga's remaining pairs (SN 22.35-36's "
            "mendicant narrative, SN 22.37-38's Ānanda dialogue) will "
            "also follow &mdash; a fuller first discourse followed by "
            "a shorter or differently elaborated second.",
        ]),
    ],
    terms=[
        ("na tumhākaṁ",
         "&ldquo;it's not yours&rdquo; &mdash; the same title phrase "
         "as SN 22.33, unchanged here despite the missing simile."),
        ("pajahatha",
         "&ldquo;give up&rdquo; &mdash; the discourse's central "
         "imperative verb, identical to SN 22.33's."),
        ("hitāya sukhāya",
         "&ldquo;for welfare and happiness&rdquo; &mdash; the "
         "promised result, repeated at both the instruction's first "
         "statement and its closing repetition."),
        ("peyyāla",
         "the technical term for the kind of source-level compression "
         "seen in SN 22.6 and SN 22.13 earlier in this book, though "
         "this discourse is not itself elided &mdash; it is simply "
         "shorter by design, lacking a simile rather than eliding one."),
        ("tiṇakaṭṭhasākhāpalāsa",
         "&ldquo;grass, sticks, branches, and leaves&rdquo; &mdash; "
         "SN 22.33's simile material, entirely absent from this "
         "discourse's shorter form."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same instruction "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.34:1.1-1.6"),
        ("p", "&sect;2", "sn22.34:1.10-1.13"),
    ],
    quiz=[
        {"q": "How does this discourse's instruction compare to SN 22.33's?",
         "opts": [
             "Identical in every clause, applied to each aggregate in turn",
             "Entirely different, using a new set of terms",
             "A direct contradiction of SN 22.33",
             "Shorter because it applies to only three of the five aggregates"],
         "correct": 0,
         "expl": "Every clause matches SN 22.33 exactly."},
        {"q": "What is missing from this discourse that SN 22.33 included?",
         "opts": [
             "The Jeta's Grove simile of grass, sticks, branches, and leaves",
             "The instruction to give up the aggregates",
             "The mention of the aggregate \"form\"",
             "The setting at Sāvatthī"],
         "correct": 0,
         "expl": "The entire illustrative second half of SN 22.33 is absent here."},
        {"q": "What does this discourse use in place of the simile to provide closure?",
         "opts": [
             "A repetition of its own opening instruction",
             "A new, different simile",
             "A question left unanswered",
             "A narrative about a mendicant's later attainment"],
         "correct": 0,
         "expl": "The instruction repeated once more stands in for illustrative content."},
        {"q": "What does comparing SN 22.33 and this discourse reveal about the simile's role?",
         "opts": [
             "The simile functioned as an optional, vivid elaboration rather than a logically necessary component",
             "The simile was considered essential and this discourse is therefore incomplete",
             "The two discourses are considered contradictory by the tradition",
             "The simile only applies to some aggregates, not all five"],
         "correct": 0,
         "expl": "The bare imperative was evidently a complete teaching on its own."},
        {"q": "What pattern does this pair (SN 22.33-34) set for the rest of the vagga?",
         "opts": [
             "A fuller first discourse followed by a shorter or differently elaborated second, repeated in later pairs",
             "No pattern — each subsequent pair is entirely unrelated in structure",
             "A pattern of increasingly longer discourses with no shortening",
             "A pattern where the second discourse always contradicts the first"],
         "correct": 0,
         "expl": "SN 22.35-36 and SN 22.37-38 follow a similar fuller-then-varied structure."},
        {"q": "How many aggregates does this discourse's instruction apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.33, without the grove-specific simile detail."},
        {"q": "What promised result follows from giving up what isn't yours in this discourse?",
         "opts": [
             "Welfare and happiness",
             "Immediate ordination as a senior monk",
             "Physical invulnerability",
             "Public praise from laypeople"],
         "correct": 0,
         "expl": "Hitāya sukhāya, identical to SN 22.33's wording."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.35, a narrative about a mendicant requesting a brief teaching",
             "A return to SN 22.22",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Opening the vagga's second pair, a narrative structure distinct from this discourse's bare instruction."},
        {"q": "Is this discourse itself an elided peyyāla stub, or a complete discourse that is simply shorter by design?",
         "opts": [
             "A complete discourse, shorter by design rather than an elided compression of a longer original",
             "An elided peyyāla stub identical in kind to SN 22.6 or SN 22.13",
             "An incomplete fragment missing from the source entirely",
             "A later scribal addition not part of the original collection"],
         "correct": 0,
         "expl": "Unlike SN 22.6 or SN 22.13, this discourse is not eliding a fuller statement given elsewhere in identical form."},
    ],
    marginalia=[
        ("The identical instruction, the simile removed", [
            "every clause matches SN 22.33 &mdash;",
            "the grove, the grass, the leaves all absent",
        ]),
        ("Repetition standing in for illustration", [
            "the instruction stated twice &mdash;",
            "no image needed to close the discourse",
        ]),
        ("An optional elaboration, not a requirement", [
            "the bare imperative sufficed on its own &mdash;",
            "the simile was vivid, not logically necessary",
        ]),
        ("Setting the vagga's pairing pattern", [
            "fuller discourse, then a shorter companion &mdash;",
            "repeated again in the pairs that follow",
        ]),
    ],
    further=[
        '<a href="%s/sn22.34/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.33.html">SN 22.33 &middot; It&rsquo;s Not '
        "Yours</a> &mdash; the previous discourse, the same "
        "instruction with the Jeta's Grove simile attached.",
        '<a href="sn-22.35.html">SN 22.35 &middot; A Mendicant</a> '
        "&mdash; the next discourse, a narrative about a mendicant's "
        "request for a teaching in brief.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.35 — Bhikkhusutta
# --------------------------------------------------------------------------- #
page(
    22, 35, "Bhikkhu", "A Mendicant",
    vagga="Natumhākavagga",
    meta_title="SN 22.35 — A Mendicant | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Bhikkhusutta &mdash; an unnamed mendicant requests a "
        "brief teaching, explains its detailed meaning correctly, "
        "and attains arahantship soon after. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "An unnamed mendicant questions the Buddha and "
                     "then explains the teaching back to him"),
        ("Form", "The classic \"teaching in brief\" narrative: a "
                 "compact statement, a request for its detailed "
                 "meaning, a correct answer confirmed, and a report "
                 "of the mendicant's subsequent attainment"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a compact formula (\"reckoned by\") carrying "
                       "unusually dense implications"),
    ],
    why=(
        "This discourse follows one of the canon's most recognizable "
        "narrative templates: an unnamed mendicant asks the Buddha "
        "for a teaching &ldquo;in brief,&rdquo; intending to go off "
        "and practice alone in solitude. The Buddha gives a "
        "deliberately compressed formula &mdash; &ldquo;you're "
        "reckoned by what you have an underlying tendency for; "
        "you're not reckoned by what you have no underlying tendency "
        "for&rdquo; &mdash; and then, remarkably, asks the mendicant "
        "to explain its detailed meaning back to him before the "
        "mendicant has even left. The mendicant does so correctly, "
        "receives confirmation, departs to practice alone, and "
        "&ldquo;soon&rdquo; attains full liberation. The discourse "
        "thus enacts, in miniature, the entire arc from teaching to "
        "realization within a single narrative."
    ),
    guide=[
        ("A request framed around solitary practice", [
            "The mendicant's request is specific: teach me in brief, "
            "so that, having heard it, I can go live alone, "
            "withdrawn, diligent, keen, and resolute. This framing "
            "&mdash; brevity in service of solitary application, "
            "rather than brevity for its own sake &mdash; recurs "
            "throughout this genre of discourse and signals that what "
            "follows is meant to be a complete, self-sufficient "
            "meditation instruction rather than merely a summary.",
        ]),
        ("A formula built on a single technical term", [
            "The Buddha's brief teaching turns entirely on one word: "
            "anusaya, &ldquo;underlying tendency&rdquo; (the same "
            "term for the latent dispositions toward greed, "
            "aversion, and views that persist beneath the surface of "
            "ordinary awareness). You are &ldquo;reckoned by&rdquo; "
            "&mdash; identified with, categorized under &mdash; "
            "whatever you have this latent tendency toward, and not "
            "reckoned by whatever you have no such tendency toward.",
        ]),
        ("The mendicant tested on his own understanding, immediately", [
            "Unusually, the Buddha does not simply confirm "
            "understanding after the mendicant departs and returns "
            "&mdash; he asks the mendicant to demonstrate "
            "comprehension on the spot: &ldquo;but how do you see "
            "the detailed meaning of my brief statement?&rdquo; The "
            "mendicant answers by applying the formula to each of the "
            "five aggregates in turn, and the Buddha repeats the "
            "mendicant's own answer back verbatim as confirmation "
            "&mdash; a structure that gives the listener's own "
            "articulation equal standing with the Buddha's original "
            "statement.",
        ]),
        ("A narrative arc compressed into one short discourse", [
            "The discourse closes by narrating what happened next: "
            "the mendicant bowed, departed, and &ldquo;soon&rdquo; "
            "realized the supreme goal of the spiritual life, closing "
            "with the same four-part arahant declaration used "
            "throughout this book. Few discourses in this vagga carry "
            "a listener from initial request through confirmed "
            "understanding to full liberation within a single, "
            "self-contained narrative arc this compact.",
        ]),
    ],
    terms=[
        ("saṅkhittena",
         "&ldquo;in brief&rdquo; &mdash; the mendicant's explicit "
         "request, framing the entire discourse as an instance of "
         "this recurring genre."),
        ("anusaya",
         "&ldquo;underlying tendency&rdquo; &mdash; the single "
         "technical term the Buddha's brief formula turns on, naming "
         "latent dispositions beneath ordinary awareness."),
        ("saṅkhaṁ gacchati",
         "&ldquo;is reckoned by&rdquo; &mdash; the formula's key "
         "verb, meaning to be identified with or categorized under "
         "something."),
        ("eko vūpakaṭṭho appamatto ātāpī pahitatto",
         "&ldquo;alone, withdrawn, diligent, keen, and resolute&rdquo; "
         "&mdash; the standard description of solitary meditative "
         "effort, naming what the mendicant intends to do once "
         "taught."),
        ("khīṇā jāti&hellip;nāparaṁ itthattāya",
         "&ldquo;rebirth is ended&hellip;nothing further for this "
         "place&rdquo; &mdash; the standard arahant declaration, "
         "closing the narrative with the mendicant's own attainment."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each of "
        "the discourse's two parallel expositions (feeling, "
        "perception, and choices, each following the same formula "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.35:1.1-1.7"),
        ("p", "&sect;2", "sn22.35:2.1-2.2"),
        ("p", "&sect;3", "sn22.35:2.7-2.7"),
        ("p", "&sect;4", "sn22.35:2.12-2.12"),
        ("p", "&sect;5", "sn22.35:3.1-3.3"),
        ("p", "&sect;6", "sn22.35:4.1-4.1"),
        ("p", "&sect;7", "sn22.35:5.1-5.3"),
    ],
    quiz=[
        {"q": "What does the mendicant ask the Buddha for at the discourse's start?",
         "opts": [
             "A teaching in brief, so he can go practice alone in solitude",
             "Permission to travel to a distant land",
             "A formal debate with another teacher",
             "A detailed multi-year course of study"],
         "correct": 0,
         "expl": "Brevity framed explicitly in service of solitary application, not summary for its own sake."},
        {"q": "What single technical term does the Buddha's brief formula turn on?",
         "opts": [
             "Anusaya, \"underlying tendency\"",
             "Nirodha, \"cessation\"",
             "Assāda, \"gratification\"",
             "Pariññā, \"complete understanding\""],
         "correct": 0,
         "expl": "The latent dispositions that persist beneath ordinary awareness."},
        {"q": "What does the Buddha ask the mendicant to do immediately after giving the brief formula?",
         "opts": [
             "Explain its detailed meaning back to him on the spot",
             "Leave immediately without further discussion",
             "Repeat the formula word for word without explanation",
             "Debate the formula's validity with other mendicants"],
         "correct": 0,
         "expl": "An unusual immediate test of comprehension, rather than confirmation after later practice."},
        {"q": "How does the mendicant apply the formula in his answer?",
         "opts": [
             "To each of the five aggregates in turn — reckoned by an underlying tendency for it, not reckoned without one",
             "Only to the aggregate of consciousness",
             "By rejecting the formula as unclear",
             "By asking the Buddha to clarify further before answering"],
         "correct": 0,
         "expl": "A direct application of anusaya across form, feeling, perception, choices, and consciousness."},
        {"q": "How does the Buddha respond to the mendicant's explanation?",
         "opts": [
             "By repeating the mendicant's own answer back verbatim as confirmation",
             "By correcting several errors in the explanation",
             "By giving an entirely different, unrelated answer",
             "By remaining silent and giving no response"],
         "correct": 0,
         "expl": "Giving the mendicant's own articulation equal standing with the Buddha's original statement."},
        {"q": "What happens to the mendicant after he departs to practice alone?",
         "opts": [
             "He soon realizes the supreme goal of the spiritual life and becomes an arahant",
             "He returns to ask further questions without attaining anything",
             "He abandons the practice shortly afterward",
             "He teaches the formula to other mendicants instead of practicing it himself"],
         "correct": 0,
         "expl": "The full arahant declaration closes the discourse's narrative arc."},
        {"q": "What description names the mendicant's intended manner of practice?",
         "opts": [
             "Alone, withdrawn, diligent, keen, and resolute",
             "Surrounded by a large community of supporters",
             "Traveling constantly between different regions",
             "Engaged primarily in scholarly debate"],
         "correct": 0,
         "expl": "The standard formula for solitary meditative effort."},
        {"q": "How many aggregates does the formula apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "The default setting for most of this vagga's discourses."},
        {"q": "How does this discourse's structure compare to SN 22.3's earlier exegetical dialogue?",
         "opts": [
             "A similar pattern — a brief statement given, then unpacked in detail — but this time ending with a report of the questioner's own attainment",
             "Entirely unrelated in structure",
             "A direct contradiction of SN 22.3's method",
             "Identical in every detail, including the questioner's identity"],
         "correct": 0,
         "expl": "Both follow the request-and-gloss pattern, but this discourse adds a narrative of subsequent liberation."},
    ],
    marginalia=[
        ("Brevity requested for a specific purpose", [
            "not summary for its own sake &mdash;",
            "meant for immediate solitary application",
        ]),
        ("One technical term carrying the whole formula", [
            "anusaya, underlying tendency &mdash;",
            "reckoned by what lingers beneath awareness",
        ]),
        ("Tested on the spot, not after practice", [
            "explain it back immediately &mdash;",
            "confirmation before the mendicant even leaves",
        ]),
        ("A complete arc in one short discourse", [
            "request, formula, confirmation, attainment &mdash;",
            "teaching to liberation within a single narrative",
        ]),
    ],
    further=[
        '<a href="%s/sn22.35/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.34.html">SN 22.34 &middot; It&rsquo;s Not '
        "Yours (2nd)</a> &mdash; the previous discourse, closing the "
        "vagga's opening pair.",
        '<a href="sn-22.36.html">SN 22.36 &middot; A Mendicant '
        "(2nd)</a> &mdash; the next discourse, the same narrative "
        "with a two-step version of the formula.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.36 — Dutiyabhikkhusutta
# --------------------------------------------------------------------------- #
page(
    22, 36, "Dutiyabhikkhu", "A Mendicant (2nd)",
    vagga="Natumhākavagga",
    meta_title="SN 22.36 — A Mendicant (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyabhikkhusutta &mdash; SN 22.35's narrative repeated "
        "with a two-step version of the formula, adding \"measured "
        "against\" between tendency and being reckoned. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "An unnamed mendicant questions the Buddha and "
                     "then explains the teaching back to him"),
        ("Form", "The identical narrative template as SN 22.35, with "
                 "a formula extended by one additional intermediate "
                 "step"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "best read directly after SN 22.35, whose "
                       "formula it extends by one link"),
    ],
    why=(
        "This discourse repeats SN 22.35's narrative almost exactly "
        "&mdash; a mendicant requests a teaching in brief in order to "
        "practice alone, explains its meaning correctly, and attains "
        "arahantship &mdash; but the formula itself gains one "
        "additional step. Where SN 22.35 said simply &ldquo;you're "
        "reckoned by what you have an underlying tendency for,&rdquo; "
        "this discourse inserts an intermediate link: &ldquo;you're "
        "measured against what you have an underlying tendency for, "
        "and you're reckoned by what you're measured against.&rdquo; "
        "The destination is identical; the path to it now has one "
        "more visible step."
    ),
    guide=[
        ("The same narrative, told again in full", [
            "Every element of SN 22.35's story recurs here: an "
            "unnamed mendicant's request for a brief teaching meant "
            "for solitary practice, the Buddha's compact formula, the "
            "mendicant's correct explanation, the Buddha's "
            "confirmation, and the mendicant's departure and "
            "subsequent attainment. The narrative frame is repeated "
            "in full rather than elided, even though its content is "
            "so close to SN 22.35's.",
        ]),
        ("One additional link inserted into the formula", [
            "SN 22.35's formula moved directly from underlying "
            "tendency to being reckoned. This discourse inserts an "
            "intermediate term: &ldquo;you're measured against "
            "(saṅkhaṁ gacchati is now paired with a second verb) "
            "what you have an underlying tendency for, and you're "
            "reckoned by what you're measured against.&rdquo; The "
            "chain now has two links rather than one, though both "
            "discourses arrive at the identical outcome.",
        ]),
        ("Why the extra step might matter", [
            "The additional intermediate term makes explicit "
            "something SN 22.35 left implicit: that being "
            "&ldquo;reckoned by&rdquo; something is not a direct, "
            "unmediated consequence of having an underlying tendency "
            "toward it, but passes through an intervening state of "
            "being &ldquo;measured against&rdquo; it first. Whether "
            "this represents a genuinely distinct doctrinal nuance or "
            "simply an alternative way of unpacking the same "
            "relationship, the text does not say &mdash; but the "
            "deliberate insertion of a new term is worth noticing "
            "rather than passing over.",
        ]),
        ("A pair demonstrating variation within a fixed template", [
            "Read together, SN 22.35 and this discourse show the "
            "&ldquo;brief teaching&rdquo; narrative template "
            "accommodating small but deliberate variation in its "
            "doctrinal content while keeping its narrative frame "
            "completely fixed &mdash; the same pattern already seen "
            "in this vagga's SN 22.33-34 pair, where the narrative "
            "frame stayed fixed while the illustrative material "
            "varied instead.",
        ]),
    ],
    terms=[
        ("anusaya",
         "&ldquo;underlying tendency&rdquo; &mdash; the same starting "
         "term as SN 22.35, unchanged in this discourse's extended "
         "formula."),
        ("saṅkhaṁ gacchati",
         "&ldquo;measured against&rdquo; &mdash; the new intermediate "
         "term this discourse inserts between underlying tendency and "
         "being reckoned."),
        ("tena saṅkhyaṁ gacchati",
         "&ldquo;reckoned by what you're measured against&rdquo; "
         "&mdash; the formula's final step, now explicitly derived "
         "from the intermediate \"measured against\" rather than "
         "directly from the underlying tendency."),
        ("saṅkhittena",
         "&ldquo;in brief&rdquo; &mdash; the mendicant's request, "
         "identical in wording to SN 22.35's."),
        ("arahataṁ ahosi",
         "&ldquo;became one of the perfected&rdquo; &mdash; the "
         "discourse's closing description of the mendicant's "
         "attainment, phrased slightly differently from SN 22.35's "
         "fuller declaration but naming the identical outcome."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each of "
        "the discourse's two parallel expositions (feeling, "
        "perception, and choices, each following the same extended "
        "formula spelled out in full for form and consciousness) are "
        "given exactly as bilara-data preserves them. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.36:1.1-1.8"),
        ("p", "&sect;2", "sn22.36:2.1-2.3"),
        ("p", "&sect;3", "sn22.36:2.9-2.10"),
        ("p", "&sect;4", "sn22.36:3.1-3.4"),
        ("p", "&sect;5", "sn22.36:3.18-3.18"),
    ],
    quiz=[
        {"q": "How does this discourse's narrative compare to SN 22.35's?",
         "opts": [
             "Nearly identical — the same request, formula pattern, confirmation, and attainment",
             "Entirely different, with a new questioner and setting",
             "A direct contradiction of SN 22.35's narrative",
             "Much shorter, omitting the mendicant's subsequent attainment"],
         "correct": 0,
         "expl": "The full narrative frame is repeated, even though the formula's content differs slightly."},
        {"q": "What new intermediate term does this discourse insert into the formula?",
         "opts": [
             "\"Measured against\" — between having an underlying tendency and being reckoned",
             "\"Completely understood\" — replacing \"reckoned\" entirely",
             "\"Given up\" — replacing \"underlying tendency\" entirely",
             "No new term is inserted; the formula is identical to SN 22.35's"],
         "correct": 0,
         "expl": "A two-step chain in place of SN 22.35's direct, single-step formula."},
        {"q": "Do the two versions of the formula (SN 22.35's and this discourse's) arrive at different conclusions?",
         "opts": [
             "No — both arrive at the identical outcome, despite the extra intermediate step",
             "Yes — this discourse concludes the opposite of SN 22.35",
             "Yes — this discourse applies only to some aggregates",
             "The discourse leaves the conclusion entirely open"],
         "correct": 0,
         "expl": "The destination is unchanged; only the visible path to it gains one more step."},
        {"q": "What does the additional intermediate term make explicit, that SN 22.35 left implicit?",
         "opts": [
             "That being \"reckoned by\" something passes through an intervening state of being \"measured against\" it",
             "That the formula applies to only one aggregate",
             "That underlying tendency has no relationship to being reckoned at all",
             "That the mendicant's attainment was accidental"],
         "correct": 0,
         "expl": "A deliberate insertion worth noticing, whether or not it represents a genuinely distinct doctrinal nuance."},
        {"q": "What other pair in this vagga shows a similar pattern of narrative frame fixed, content varied?",
         "opts": [
             "SN 22.33-34, where the narrative frame stayed fixed while the illustrative material varied",
             "SN 22.26-28, which uses an entirely different structure",
             "SN 22.22, which has no companion pair at all",
             "No other discourse in the vagga shows this pattern"],
         "correct": 0,
         "expl": "A recurring pattern of fixed template accommodating small doctrinal variation."},
        {"q": "How many aggregates does this discourse's extended formula apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.35."},
        {"q": "What does the mendicant ask the Buddha for at the discourse's start?",
         "opts": [
             "A teaching in brief, so he can go practice alone in solitude",
             "Formal permission to found a new monastery",
             "Assistance translating a text into a foreign language",
             "A debate with a rival teacher"],
         "correct": 0,
         "expl": "Identical in wording to SN 22.35's opening request."},
        {"q": "How does the Buddha respond to the mendicant's explanation of the extended formula?",
         "opts": [
             "By repeating the mendicant's own answer back as confirmation, as in SN 22.35",
             "By correcting the mendicant's explanation extensively",
             "By declining to comment on the explanation",
             "By giving an entirely different, unrelated teaching instead"],
         "correct": 0,
         "expl": "The same confirmation pattern as SN 22.35, adapted to the extended formula."},
        {"q": "What happens to the mendicant after departing to practice alone?",
         "opts": [
             "He becomes one of the perfected (an arahant)",
             "He returns without having attained anything",
             "He abandons monastic life entirely",
             "He is not mentioned again in the discourse"],
         "correct": 0,
         "expl": "The identical outcome to SN 22.35, closing the vagga's second matched pair."},
    ],
    marginalia=[
        ("The same story, told again in full", [
            "not elided this time &mdash;",
            "request, formula, confirmation, attainment repeated",
        ]),
        ("One new link in the chain", [
            "measured against, inserted &mdash;",
            "between tendency and being reckoned",
        ]),
        ("The same destination, one more visible step", [
            "outcome unchanged &mdash;",
            "the path to it now spelled out further",
        ]),
        ("A fixed template, small deliberate variation", [
            "echoing SN 22.33-34's own pattern &mdash;",
            "narrative constant, formula content adjusted",
        ]),
    ],
    further=[
        '<a href="%s/sn22.36/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.35.html">SN 22.35 &middot; A Mendicant</a> '
        "&mdash; the previous discourse, the same narrative with the "
        "formula's simpler, single-step version.",
        '<a href="sn-22.37.html">SN 22.37 &middot; With Ānanda</a> '
        "&mdash; the next discourse, the Buddha rehearsing an answer "
        "with Ānanda directly.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.37 — Ānandasutta
# --------------------------------------------------------------------------- #
page(
    22, 37, "Ānanda", "With Ānanda",
    vagga="Natumhākavagga",
    meta_title="SN 22.37 — With Ānanda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Ānandasutta &mdash; the Buddha rehearses with Ānanda how "
        "to answer a hypothetical question about the aggregates' "
        "arising, vanishing, and change while persisting. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha, coaching Venerable Ānanda through a "
                     "hypothetical question and its answer"),
        ("Form", "A rehearsal dialogue: the Buddha poses a "
                 "hypothetical question, Ānanda answers, and the "
                 "Buddha confirms the answer word for word"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "a compact rehearsal, best read alongside SN "
                       "22.2's similar training scene earlier in the "
                       "book"),
    ],
    why=(
        "This discourse recalls SN 22.2's rehearsal scene from "
        "earlier in the book, but scaled down to a single exchange "
        "between the Buddha and Ānanda alone. The Buddha poses a "
        "hypothetical: suppose someone asked you, Ānanda, what "
        "things show evident arising, evident vanishing, and evident "
        "change while persisting &mdash; how would you answer? "
        "Ānanda gives his answer &mdash; the five aggregates, each "
        "shown in turn to display all three characteristics &mdash; "
        "and the Buddha confirms it by repeating the same words back "
        "as instruction: &ldquo;that's how you should answer such a "
        "question.&rdquo; The discourse functions as a compact "
        "training exercise in real time, with the Buddha's own "
        "closest attendant as its subject."
    ),
    guide=[
        ("A hypothetical question, posed as practice", [
            "Rather than asking Ānanda a direct doctrinal question, "
            "the Buddha frames his question as a rehearsal for a "
            "future encounter: &ldquo;suppose they were to ask "
            "you&hellip;how would you answer?&rdquo; This framing "
            "treats the exchange explicitly as preparation for "
            "Ānanda's own future teaching role, echoing SN 22.2's "
            "similar concern with equipping mendicants to answer "
            "outsiders' questions accurately.",
        ]),
        ("Three characteristics named together for each aggregate", [
            "Ānanda's answer names, for each of the five aggregates "
            "in turn, three simultaneously evident features: its "
            "arising is evident, its vanishing is evident, and its "
            "change while persisting is evident. This threefold "
            "description &mdash; arising, vanishing, and change while "
            "persisting &mdash; captures impermanence not as a single "
            "abstract property but as three concretely observable "
            "facets of the same ongoing process.",
        ]),
        ("Confirmation by exact repetition", [
            "The Buddha's response to Ānanda's answer is not a "
            "paraphrase or elaboration but a word-for-word repetition "
            "of what Ānanda has just said, closing with an explicit "
            "instruction: &ldquo;that's how you should answer such a "
            "question.&rdquo; This exact-repetition pattern, seen "
            "already in SN 22.35's confirmation of the unnamed "
            "mendicant's answer, appears again here between the "
            "Buddha and his closest personal attendant.",
        ]),
        ("A shorter companion piece to SN 22.38", [
            "This discourse presents its three characteristics "
            "(arising, vanishing, change while persisting) in a "
            "single present-tense statement, without dividing them "
            "across past, future, and present as SN 22.38 immediately "
            "after it will do. Read together, the two discourses show "
            "the same core observation given first in its simplest "
            "form and then in its fully time-differentiated version.",
        ]),
    ],
    terms=[
        ("uppādo paññāyati",
         "&ldquo;arising is evident&rdquo; &mdash; the first of "
         "three characteristics this discourse names for each "
         "aggregate."),
        ("vayo paññāyati",
         "&ldquo;vanishing is evident&rdquo; &mdash; the second "
         "characteristic, paired with arising as an equally observable "
         "feature."),
        ("ṭhitassa aññathattaṁ paññāyati",
         "&ldquo;change while persisting is evident&rdquo; &mdash; "
         "the third characteristic, naming impermanence's presence "
         "even during an aggregate's apparent continuation."),
        ("sace maṁ evaṁ puccheyyuṁ",
         "&ldquo;suppose they were to ask you&rdquo; &mdash; the "
         "Buddha's framing device, treating the exchange as rehearsal "
         "for a future real encounter."),
        ("evameva kho, ānanda, byākareyyāsi",
         "&ldquo;that's how you should answer such a question&rdquo; "
         "&mdash; the Buddha's closing confirmation, an explicit "
         "instruction rather than mere approval."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each "
        "exchange (feeling, perception, and choices, each following "
        "the same threefold description spelled out in full for form "
        "and consciousness) are given exactly as bilara-data "
        "preserves them. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.37:2.1-2.6"),
        ("p", "&sect;2", "sn22.37:2.7-2.12"),
        ("p", "&sect;3", "sn22.37:3.1-3.7"),
        ("p", "&sect;4", "sn22.37:3.8-3.8"),
    ],
    quiz=[
        {"q": "How does the Buddha frame his question to Ānanda?",
         "opts": [
             "As a hypothetical rehearsal: \"suppose they were to ask you... how would you answer?\"",
             "As a direct accusation of wrongdoing",
             "As an unrelated question about monastic robes",
             "As a request to translate a text"],
         "correct": 0,
         "expl": "Explicitly framed as preparation for a future real encounter."},
        {"q": "What three characteristics does Ānanda's answer name for each aggregate?",
         "opts": [
             "Arising is evident, vanishing is evident, and change while persisting is evident",
             "Pleasant, painful, and neutral",
             "Past, future, and present",
             "Physical, mental, and spiritual"],
         "correct": 0,
         "expl": "Impermanence captured as three concretely observable facets of one process."},
        {"q": "How does the Buddha respond to Ānanda's answer?",
         "opts": [
             "By repeating it word for word as confirmation, with an explicit instruction to answer this way",
             "By correcting several errors in the answer",
             "By giving an entirely different answer instead",
             "By declining to comment"],
         "correct": 0,
         "expl": "The same exact-repetition confirmation pattern seen in SN 22.35."},
        {"q": "How does this discourse's structure recall SN 22.2 earlier in the book?",
         "opts": [
             "Both concern rehearsing an answer in preparation for future questioning by others",
             "Both are set at Devadaha rather than Sāvatthī",
             "Both involve Sāriputta rather than Ānanda",
             "There is no meaningful connection between the two discourses"],
         "correct": 0,
         "expl": "A shared concern with equipping a listener to answer outsiders accurately."},
        {"q": "How does this discourse's three characteristics differ from SN 22.38's treatment?",
         "opts": [
             "This discourse gives them in a single present-tense statement, while SN 22.38 divides them across past, future, and present",
             "This discourse uses entirely different characteristics from SN 22.38",
             "SN 22.38 uses only one characteristic instead of three",
             "There is no relationship between the two discourses"],
         "correct": 0,
         "expl": "The simpler form here, the fully time-differentiated version next."},
        {"q": "How many aggregates does Ānanda's answer apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "The default setting for most of this vagga's discourses."},
        {"q": "Who is being coached in this discourse?",
         "opts": [
             "Venerable Ānanda",
             "An unnamed mendicant",
             "The householder Hāliddikāni",
             "Venerable Sāriputta"],
         "correct": 0,
         "expl": "The Buddha's own closest personal attendant, distinct from SN 22.35-36's unnamed mendicant."},
        {"q": "What does \"change while persisting is evident\" describe?",
         "opts": [
             "Impermanence's presence even during an aggregate's apparent continuation",
             "An aggregate's complete disappearance",
             "An aggregate that has not yet arisen",
             "A permanent, unchanging quality of the aggregate"],
         "correct": 0,
         "expl": "A third facet of impermanence distinct from simple arising and vanishing."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.38, extending the same characteristics across past, future, and present",
             "A return to SN 22.22",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "A fuller, time-differentiated companion to this discourse."},
    ],
    marginalia=[
        ("A question framed as rehearsal", [
            "\"suppose they were to ask you\" &mdash;",
            "preparation for a future real encounter",
        ]),
        ("Three facets of one impermanence", [
            "arising, vanishing, change while persisting &mdash;",
            "not one abstract property but three observable ones",
        ]),
        ("Confirmation by exact repetition", [
            "the same words handed back &mdash;",
            "an instruction, not just approval",
        ]),
        ("The simpler half of a two-discourse pair", [
            "present tense only &mdash;",
            "SN 22.38 will add past and future",
        ]),
    ],
    further=[
        '<a href="%s/sn22.37/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.36.html">SN 22.36 &middot; A Mendicant '
        "(2nd)</a> &mdash; the previous discourse, closing the "
        "vagga's second matched pair.",
        '<a href="sn-22.38.html">SN 22.38 &middot; With Ānanda '
        "(2nd)</a> &mdash; the next discourse, the same rehearsal "
        "extended across past, future, and present.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.38 — Dutiyaānandasutta
# --------------------------------------------------------------------------- #
page(
    22, 38, "Dutiyaānanda", "With Ānanda (2nd)",
    vagga="Natumhākavagga",
    meta_title="SN 22.38 — With Ānanda (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaānandasutta &mdash; SN 22.37's rehearsal extended "
        "across past, future, and present, describing the aggregates "
        "at every stage of their existence. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha, coaching Venerable Ānanda through a "
                     "more elaborate hypothetical question"),
        ("Form", "The same rehearsal structure as SN 22.37, now "
                 "divided across three explicit time frames: past, "
                 "future, and present"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "more elaborate than SN 22.37, worth reading "
                       "as its direct continuation"),
    ],
    why=(
        "This discourse takes SN 22.37's single present-tense "
        "observation and unfolds it across all three times. The "
        "Buddha's hypothetical question grows correspondingly more "
        "elaborate: what things showed evident arising, vanishing, "
        "and change while persisting; what things will show these; "
        "and what things show them now? Ānanda's answer supplies "
        "three parallel descriptions &mdash; whatever form has "
        "passed, ceased, and perished showed these three "
        "characteristics; whatever form is not yet born will show "
        "them; and whatever form has been born and appeared shows "
        "them currently. The three-times structure makes explicit "
        "what SN 22.37 left as a single snapshot: that impermanence "
        "characterizes the aggregates not only now but at every point "
        "along their entire existence, actual or potential."
    ),
    guide=[
        ("A question tripled across three time frames", [
            "Where SN 22.37 asked a single question, this discourse "
            "asks essentially the same question three times over, "
            "once for each time frame: what showed these "
            "characteristics in the past, what will show them in the "
            "future, and what shows them now. The Buddha poses all "
            "three variations together before Ānanda answers, giving "
            "the hypothetical exchange a more elaborate, formally "
            "structured shape than SN 22.37's single exchange.",
        ]),
        ("The past described through what has already ended", [
            "Ānanda's answer for the past time frame is phrased "
            "distinctively: whatever form &ldquo;has passed, ceased, "
            "and perished&rdquo; showed evident arising, vanishing, "
            "and change while persisting. The past is characterized "
            "not by what it once was in the present moment of its "
            "occurrence, but specifically by its having already come "
            "to an end &mdash; impermanence applied retrospectively.",
        ]),
        ("The future described through what has not yet appeared", [
            "The future time frame is described correspondingly: "
            "whatever form &ldquo;is not yet born, and has not yet "
            "appeared&rdquo; will show the same three characteristics "
            "once it does arise. This is a striking claim in its own "
            "right &mdash; that impermanence can be predicated in "
            "advance of something that does not yet exist, simply on "
            "the grounds that whatever eventually arises will be "
            "subject to the same three-part pattern.",
        ]),
        ("The present described through what has already appeared", [
            "The present time frame completes the set: whatever form "
            "&ldquo;has been born, and has appeared&rdquo; shows "
            "these three characteristics now, in the ordinary sense "
            "already familiar from SN 22.37. Taken together, all "
            "three time frames close the same argumentative gap the "
            "earlier vagga discourse SN 22.9 opened &mdash; that "
            "impermanence holds &ldquo;in the three times,&rdquo; not "
            "merely in whichever moment happens to be observed "
            "directly.",
        ]),
    ],
    terms=[
        ("atītaṁ addhānaṁ",
         "&ldquo;the past&rdquo; &mdash; the first of the three time "
         "frames this discourse's question and answer are divided "
         "across."),
        ("anāgataṁ addhānaṁ",
         "&ldquo;the future&rdquo; &mdash; the second time frame, "
         "describing what has not yet come to be."),
        ("paccuppannaṁ addhānaṁ",
         "&ldquo;the present&rdquo; &mdash; the third time frame, "
         "matching SN 22.37's original single-time observation."),
        ("atītaṁ niruddhaṁ vipariṇataṁ",
         "&ldquo;has passed, ceased, and perished&rdquo; &mdash; the "
         "distinctive phrasing describing form's past occurrence, "
         "characterized by its having already ended."),
        ("anuppannaṁ apātubhūtaṁ",
         "&ldquo;not yet born, and has not yet appeared&rdquo; "
         "&mdash; the phrasing describing form's future occurrence, "
         "predicating impermanence of something not yet existing."),
    ],
    text_intro=(
        "The discourse in full. Elided repetitions in each of the "
        "three time-frame expositions (feeling, perception, and "
        "choices, each following the same pattern spelled out in full "
        "for form and consciousness) are given exactly as bilara-data "
        "preserves them. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.38:2.1-2.5"),
        ("p", "&sect;2", "sn22.38:2.11-2.20"),
        ("p", "&sect;3", "sn22.38:3.1-3.10"),
        ("p", "&sect;4", "sn22.38:4.1-4.9"),
        ("p", "&sect;5", "sn22.38:5.1-5.9"),
        ("p", "&sect;6", "sn22.38:6.1-6.8"),
        ("p", "&sect;7", "sn22.38:7.1-7.9"),
    ],
    quiz=[
        {"q": "How does this discourse's question differ from SN 22.37's?",
         "opts": [
             "It asks the same question three times, once each for the past, future, and present",
             "It asks an entirely different, unrelated question",
             "It asks only about the future, omitting past and present",
             "It is identical in every respect to SN 22.37's question"],
         "correct": 0,
         "expl": "A more elaborate, formally structured shape than SN 22.37's single exchange."},
        {"q": "How is form's past occurrence described in Ānanda's answer?",
         "opts": [
             "As having \"passed, ceased, and perished\"",
             "As having \"never truly existed\"",
             "As \"identical to its present form\"",
             "As \"unknowable and undescribable\""],
         "correct": 0,
         "expl": "Characterized by its having already come to an end, applied retrospectively."},
        {"q": "How is form's future occurrence described?",
         "opts": [
             "As \"not yet born, and has not yet appeared\"",
             "As \"already fully formed but hidden\"",
             "As \"impossible to ever arise\"",
             "As \"identical to consciousness\""],
         "correct": 0,
         "expl": "A striking claim — predicating impermanence of something that does not yet exist."},
        {"q": "What claim does describing the future this way make?",
         "opts": [
             "That whatever eventually arises will be subject to the same three-part impermanence pattern",
             "That the future does not actually exist in any sense",
             "That impermanence applies only to the present, never the future",
             "That the future is entirely unpredictable and cannot be described at all"],
         "correct": 0,
         "expl": "Impermanence predicated in advance of something not yet existing."},
        {"q": "How does this discourse relate to SN 22.9's earlier \"three times\" argument in this book?",
         "opts": [
             "Both establish that impermanence holds across past, future, and present, not just in observed moments",
             "This discourse directly contradicts SN 22.9's conclusions",
             "The two discourses concern entirely unrelated topics",
             "SN 22.9 concerns only the future, unlike this discourse"],
         "correct": 0,
         "expl": "Closing the same argumentative gap SN 22.9 opened in Aniccavagga."},
        {"q": "How many aggregates does this discourse's three-times structure apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.37."},
        {"q": "Who is being coached in this discourse?",
         "opts": [
             "Venerable Ānanda",
             "An unnamed mendicant",
             "The householder Hāliddikāni",
             "Venerable Sāriputta"],
         "correct": 0,
         "expl": "The same rehearsal partner as SN 22.37."},
        {"q": "How does the Buddha respond to Ānanda's three-part answer?",
         "opts": [
             "By repeating it in full, confirming each of the three time frames in turn",
             "By correcting the past and future sections only",
             "By rejecting the future section as invalid",
             "By giving no response at all"],
         "correct": 0,
         "expl": "The same confirmation pattern as SN 22.37, extended across all three time frames."},
        {"q": "What relationship does this discourse have to SN 22.37?",
         "opts": [
             "A fuller, time-differentiated companion, unfolding SN 22.37's single observation across past, future, and present",
             "A direct contradiction of SN 22.37's claims",
             "An entirely unrelated discourse placed nearby by coincidence",
             "A shorter summary of SN 22.37 with content removed"],
         "correct": 0,
         "expl": "SN 22.37 gives the simpler, single-time version; this discourse expands it fully."},
    ],
    marginalia=[
        ("One question becomes three", [
            "past, future, present, asked in turn &mdash;",
            "a more elaborate rehearsal than SN 22.37's single exchange",
        ]),
        ("The past described by its ending", [
            "passed, ceased, perished &mdash;",
            "impermanence applied retrospectively",
        ]),
        ("The future described before it exists", [
            "not yet born, not yet appeared &mdash;",
            "impermanence predicated in advance",
        ]),
        ("Closing the gap SN 22.9 opened", [
            "impermanence in all three times &mdash;",
            "not just in whichever moment is observed",
        ]),
    ],
    further=[
        '<a href="%s/sn22.38/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.37.html">SN 22.37 &middot; With Ānanda</a> '
        "&mdash; the previous discourse, the same rehearsal in its "
        "simpler, single-time form.",
        '<a href="sn-22.39.html">SN 22.39 &middot; In Line With the '
        "Teaching</a> &mdash; the next discourse, opening the vagga's "
        "closing quartet on disillusionment and the three marks.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.39 — Anudhammasutta
# --------------------------------------------------------------------------- #
page(
    22, 39, "Anudhamma", "In Line With the Teaching",
    vagga="Natumhākavagga",
    meta_title="SN 22.39 — In Line With the Teaching | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Anudhammasutta &mdash; the full chain from disillusionment "
        "to complete understanding to freedom, closing on the fullest "
        "description of liberation in the vagga. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A single chain of three steps, opening the vagga's "
                 "closing quartet"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "opens a quartet whose remaining three "
                       "discourses vary this one's opening step"),
    ],
    why=(
        "This discourse opens the vagga's closing quartet by naming "
        "what &ldquo;practicing in line with the teaching&rdquo; "
        "(dhammānudhammapaṭipanna) actually consists of: living full "
        "of disillusionment for the five aggregates. Disillusionment "
        "leads to complete understanding; complete understanding "
        "leads to freedom from the aggregates; and that freedom is, "
        "in turn, freedom from rebirth, old age, and death, and from "
        "the entire list of afflictions that follow from them "
        "&mdash; sorrow, lamentation, pain, sadness, and distress. "
        "The chain closes with the Buddha's own direct declaration: "
        "&ldquo;they're freed from suffering, I say.&rdquo; This "
        "discourse's full statement of the chain is what the three "
        "discourses immediately after it will each vary by a single "
        "opening term."
    ),
    guide=[
        ("A definition of \"practicing in line with the teaching\"", [
            "The discourse opens by naming its own subject precisely: "
            "when a mendicant is practicing in line with the teaching "
            "(anudhamma), this &mdash; what follows &mdash; is what "
            "that consists of. The definition is not left implicit; "
            "the discourse states outright that it is defining the "
            "term named in its own title.",
        ]),
        ("A three-step chain from disillusionment to freedom", [
            "The chain itself has three explicit steps: living full "
            "of disillusionment (nibbidābahula) for the five "
            "aggregates; from this, completely understanding "
            "(parijānāti) them; and from complete understanding, "
            "being freed (vimuccati) from them. Each step depends "
            "strictly on the one before it, in the same dependency "
            "structure seen in SN 22.12's earlier liberation chain.",
        ]),
        ("The fullest description of freedom in this vagga", [
            "Where many discourses in this book close on the compact "
            "phrase &ldquo;freed from suffering,&rdquo; this "
            "discourse spells out what that freedom specifically "
            "includes: freedom from rebirth, old age, and death, and "
            "from sorrow, lamentation, pain, sadness, and distress "
            "&mdash; the fullest single description of the aggregates "
            "of dukkha found together anywhere in Natumhākavagga, "
            "before compressing it all into the final summary "
            "&ldquo;they're freed from suffering, I say.&rdquo;",
        ]),
        ("A template the vagga's closing quartet will vary", [
            "This discourse's opening step &mdash; living full of "
            "disillusionment &mdash; is what the three discourses "
            "immediately after it will each replace with a different "
            "meditation practice: observing impermanence (SN 22.40), "
            "observing suffering (SN 22.41), and observing not-self "
            "(SN 22.42), each still leading to the identical closing "
            "declaration.",
        ]),
    ],
    terms=[
        ("anudhamma",
         "&ldquo;in line with the teaching&rdquo; &mdash; the "
         "discourse's title term and the practice it defines, naming "
         "correct conduct relative to the Dhamma as a whole."),
        ("nibbidābahula",
         "&ldquo;full of disillusionment&rdquo; &mdash; the chain's "
         "opening step, describing a sustained disposition rather "
         "than a single momentary insight."),
        ("parijānāti",
         "&ldquo;completely understands&rdquo; &mdash; the chain's "
         "second step, the same pariññā defined earlier in this vagga "
         "and in SN 22.23 within Bhāravagga."),
        ("vimuccati",
         "&ldquo;is freed&rdquo; &mdash; the chain's third and final "
         "step, the same verb used in SN 22.12's earlier liberation "
         "chain."),
        ("dukkhasmā parimuccati, vadāmi",
         "&ldquo;they're freed from suffering, I say&rdquo; &mdash; "
         "the discourse's closing declaration, marked with the "
         "Buddha's explicit personal voice, as in SN 22.29 earlier "
         "in this book."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.39:1.1-1.6"),
    ],
    quiz=[
        {"q": "What does this discourse define \"practicing in line with the teaching\" as consisting of?",
         "opts": [
             "Living full of disillusionment for the five aggregates, leading through complete understanding to freedom",
             "Reciting scripture daily without variation",
             "Following a strict schedule of physical exercise",
             "Avoiding all contact with other mendicants"],
         "correct": 0,
         "expl": "A three-step chain the discourse names and defines explicitly."},
        {"q": "What is the chain's first step?",
         "opts": [
             "Living full of disillusionment (nibbidābahula) for the aggregates",
             "Immediate freedom, with no preceding steps",
             "Physical austerity practices",
             "Formal debate with outsiders"],
         "correct": 0,
         "expl": "A sustained disposition, not a single momentary insight."},
        {"q": "What does disillusionment lead to in this chain?",
         "opts": [
             "Complete understanding (parijānāti) of the aggregates",
             "Immediate physical illness",
             "A return to ordinary lay life",
             "Increased attachment to the aggregates"],
         "correct": 0,
         "expl": "The chain's second step, depending strictly on the first."},
        {"q": "What does the discourse specify freedom from the aggregates ultimately includes?",
         "opts": [
             "Freedom from rebirth, old age, death, sorrow, lamentation, pain, sadness, and distress",
             "Freedom only from physical pain, with no mention of rebirth",
             "Freedom from monastic obligations specifically",
             "Freedom from all forms of speech"],
         "correct": 0,
         "expl": "The fullest single description of dukkha's components found together in this vagga."},
        {"q": "How does this discourse's closing declaration compare to SN 22.29's earlier in the book?",
         "opts": [
             "Both are marked with the Buddha's explicit personal voice, \"I say\" (vadāmi)",
             "This discourse contains no closing declaration at all",
             "SN 22.29 uses an entirely different closing formula",
             "The two discourses close with contradictory claims"],
         "correct": 0,
         "expl": "A shared marker of direct personal authority in both discourses."},
        {"q": "What role does this discourse play for the three discourses immediately after it?",
         "opts": [
             "It supplies the template each of them will vary by replacing the opening step with a different meditation practice",
             "It has no relationship to the discourses that follow",
             "It directly contradicts what SN 22.40-42 will teach",
             "It is a summary written after SN 22.40-42, not their template"],
         "correct": 0,
         "expl": "SN 22.40-42 each substitute a different observation for \"disillusionment\" while keeping the rest of the chain."},
        {"q": "How many aggregates does this discourse's chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Named together as a group throughout the chain."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What is the chain's third and final step?",
         "opts": [
             "Being freed (vimuccati) from the aggregates",
             "Returning to disillusionment once more",
             "Teaching the chain to others exclusively",
             "A fourth, unnamed step not disclosed in the text"],
         "correct": 0,
         "expl": "The same verb used in SN 22.12's earlier liberation chain."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.40, replacing disillusionment with meditating observing impermanence",
             "A return to SN 22.22",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The second term of the vagga's closing quartet."},
    ],
    marginalia=[
        ("A term named and then defined outright", [
            "\"in line with the teaching\" &mdash;",
            "the discourse states plainly what it consists of",
        ]),
        ("Three steps, each depending on the last", [
            "disillusionment, understanding, freedom &mdash;",
            "the same dependency structure as SN 22.12",
        ]),
        ("The fullest single list of suffering in the vagga", [
            "rebirth, old age, death, sorrow &mdash;",
            "before compressing back into one closing phrase",
        ]),
        ("A template for three more variations", [
            "one opening step, soon to be swapped three times &mdash;",
            "SN 22.40-42 will each vary it once",
        ]),
    ],
    further=[
        '<a href="%s/sn22.39/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.38.html">SN 22.38 &middot; With Ānanda '
        "(2nd)</a> &mdash; the previous discourse, closing the "
        "vagga's Ānanda rehearsal pair.",
        '<a href="sn-22.40.html">SN 22.40 &middot; In Line With the '
        "Teaching (2nd)</a> &mdash; the next discourse, replacing "
        "disillusionment with observing impermanence directly.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.40 — Dutiyaanudhammasutta
# --------------------------------------------------------------------------- #
page(
    22, 40, "Dutiyaanudhamma", "In Line With the Teaching (2nd)",
    vagga="Natumhākavagga",
    meta_title="SN 22.40 — In Line With the Teaching (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaanudhammasutta &mdash; SN 22.39's chain elided down "
        "to a single swapped opening step: meditating observing "
        "impermanence in place of disillusionment. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.39's chain, elided by the source down to its "
                 "swapped opening step and closing declaration"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and elided, best read alongside SN "
                       "22.39's full statement"),
    ],
    why=(
        "This discourse takes SN 22.39's three-step chain and "
        "replaces its opening term with a specific meditation "
        "practice: rather than &ldquo;living full of "
        "disillusionment,&rdquo; mendicants should meditate observing "
        "impermanence (aniccānupassī) in the five aggregates. The "
        "source elides everything in between, marking the gap with a "
        "bare ellipsis before jumping straight to the closing "
        "declaration &mdash; &ldquo;they're freed from suffering, I "
        "say&rdquo; &mdash; trusting the reader to supply the "
        "intervening complete-understanding-then-freedom steps from "
        "SN 22.39 immediately before it."
    ),
    guide=[
        ("A meditation practice in place of a disposition", [
            "SN 22.39's opening step named a general disposition "
            "&mdash; being full of disillusionment. This discourse "
            "instead names a specific meditative activity: observing "
            "impermanence (aniccānupassī) directly in each aggregate. "
            "The shift is from a broad attitude to a named "
            "contemplative practice, though both are presented as "
            "leading to the identical outcome.",
        ]),
        ("A genuine elision, not a shortcut taken here", [
            "As with SN 22.6 and SN 22.13 earlier in this book, the "
            "gap between this discourse's opening clause and its "
            "closing declaration is a real feature of the source "
            "material, marked with an ellipsis in bilara-data itself "
            "rather than a compression introduced by this reading "
            "guide. The intervening complete-understanding-then-"
            "freedom steps are trusted to the reader's memory of SN "
            "22.39.",
        ]),
        ("The first of three variations on SN 22.39's template", [
            "This discourse is the first of the three variations SN "
            "22.39's own guide anticipated: observing impermanence "
            "here, observing suffering in SN 22.41 next, and "
            "observing not-self in SN 22.42 closing the vagga. All "
            "three keep SN 22.39's closing declaration completely "
            "unchanged, varying only the specific practice named at "
            "the chain's opening.",
        ]),
        ("Anudhamma's meaning sharpened by this variation", [
            "Read alongside SN 22.39, this discourse and its two "
            "companions suggest that &ldquo;practicing in line with "
            "the teaching&rdquo; is not a single fixed technique but "
            "a family of related practices &mdash; disillusionment, "
            "or any one of the three marks observed directly in "
            "meditation &mdash; each equally capable of leading "
            "through complete understanding to the identical freedom.",
        ]),
    ],
    terms=[
        ("aniccānupassī",
         "&ldquo;observing impermanence&rdquo; &mdash; the "
         "meditation practice this discourse substitutes for SN "
         "22.39's \"full of disillusionment.\""),
        ("peyyāla",
         "the technical term for this discourse's genuine source-"
         "level elision, the same kind of compression seen in SN "
         "22.6 and SN 22.13 earlier in the book."),
        ("dukkhasmā parimuccati, vadāmi",
         "&ldquo;they're freed from suffering, I say&rdquo; &mdash; "
         "the closing declaration, unchanged from SN 22.39."),
        ("anudhamma",
         "&ldquo;in line with the teaching&rdquo; &mdash; the vagga's "
         "closing quartet's shared subject, here shown to accommodate "
         "more than one specific practice."),
        ("tilakkhaṇa",
         "the &ldquo;three marks&rdquo; &mdash; impermanence, the "
         "first of the three this quartet will observe directly in "
         "turn."),
    ],
    text_intro=(
        "The discourse in full &mdash; genuinely this short in the "
        "source, its ellipsis given exactly as bilara-data preserves "
        "it rather than expanded from SN 22.39. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.40:1.2-1.3"),
    ],
    quiz=[
        {"q": "What practice does this discourse substitute for SN 22.39's \"full of disillusionment\"?",
         "opts": [
             "Meditating observing impermanence (aniccānupassī) in the aggregates",
             "Reciting the discourse from memory daily",
             "Formal debate with other mendicants",
             "Physical austerity practices"],
         "correct": 0,
         "expl": "A shift from a general disposition to a specific named meditative practice."},
        {"q": "How does the source handle the chain's remaining steps (complete understanding, freedom)?",
         "opts": [
             "With a genuine ellipsis, trusting the reader's memory of SN 22.39's full statement",
             "By spelling them out again in full",
             "By omitting them with no indication anything is missing",
             "By replacing them with an entirely different chain"],
         "correct": 0,
         "expl": "The same kind of source-level elision seen in SN 22.6 and SN 22.13."},
        {"q": "What closing declaration does this discourse retain unchanged from SN 22.39?",
         "opts": [
             "\"They're freed from suffering, I say\"",
             "\"They shall teach for eighty years without rest\"",
             "\"The aggregates cease to exist entirely\"",
             "An entirely different, new declaration"],
         "correct": 0,
         "expl": "Identical wording, closing the shortened chain."},
        {"q": "What position does this discourse hold in the vagga's closing quartet?",
         "opts": [
             "The first of three variations, following SN 22.39's template",
             "The quartet's final term",
             "It does not belong to the quartet",
             "The quartet's opening term, before SN 22.39"],
         "correct": 0,
         "expl": "SN 22.39 gives the full template; this discourse is the first of three variations on it."},
        {"q": "What does the existence of this variation suggest about \"practicing in line with the teaching\"?",
         "opts": [
             "That it is a family of related practices rather than a single fixed technique",
             "That only disillusionment counts as genuine practice",
             "That observing impermanence is invalid as a practice",
             "That the three marks cannot be meditated on directly"],
         "correct": 0,
         "expl": "Disillusionment or any of the three marks observed directly, each leading to the same freedom."},
        {"q": "How many aggregates does this discourse's practice apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Named together as a group, as in SN 22.39."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.39."},
        {"q": "Does this reading guide reconstruct the elided content and present it as this discourse's own text?",
         "opts": [
             "No — it quotes the ellipsis exactly as the source gives it",
             "Yes — the full chain is reconstructed and presented as original",
             "The elided content is replaced with unrelated material",
             "The discourse is skipped entirely"],
         "correct": 0,
         "expl": "Consistent with this project's practice on other short peyyāla stubs in this book."},
        {"q": "What term names the second of the three marks this quartet will observe, coming next in SN 22.41?",
         "opts": [
             "Suffering (dukkha)",
             "Consciousness",
             "Craving",
             "Grasping"],
         "correct": 0,
         "expl": "SN 22.41 follows this discourse, substituting observing suffering for observing impermanence."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.41, substituting observing suffering for observing impermanence",
             "A return to SN 22.22",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The third term of the vagga's closing quartet."},
    ],
    marginalia=[
        ("A named practice in place of a general disposition", [
            "observing impermanence directly &mdash;",
            "not just \"full of disillusionment\"",
        ]),
        ("A genuine elision, not this guide's shortcut", [
            "the source itself marks the gap &mdash;",
            "trusting the reader's memory of SN 22.39",
        ]),
        ("The same closing declaration, unchanged", [
            "freed from suffering, I say &mdash;",
            "identical wording across the whole quartet",
        ]),
        ("The first of three variations", [
            "impermanence here, suffering and not-self to follow &mdash;",
            "one template, three practices",
        ]),
    ],
    further=[
        '<a href="%s/sn22.40/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.39.html">SN 22.39 &middot; In Line With the '
        "Teaching</a> &mdash; the previous discourse, whose full "
        "chain this one elides by cross-reference.",
        '<a href="sn-22.41.html">SN 22.41 &middot; In Line With the '
        "Teaching (3rd)</a> &mdash; the next discourse, substituting "
        "observing suffering for observing impermanence.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.41 — Tatiyaanudhammasutta
# --------------------------------------------------------------------------- #
page(
    22, 41, "Tatiyaanudhamma", "In Line With the Teaching (3rd)",
    vagga="Natumhākavagga",
    meta_title="SN 22.41 — In Line With the Teaching (3rd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Tatiyaanudhammasutta &mdash; the quartet's third term, "
        "substituting observing suffering for observing impermanence "
        "as the practice \"in line with the teaching.\" From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.39's chain, elided identically to SN 22.40 "
                 "but with a different swapped opening step"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and elided, the third of the quartet's "
                       "matched variations"),
    ],
    why=(
        "This discourse continues the quartet SN 22.39 opened, "
        "substituting a second specific meditation practice for "
        "disillusionment: mendicants should meditate observing "
        "suffering (dukkhānupassī) in the five aggregates. As in SN "
        "22.40, the source elides everything between this opening "
        "clause and the closing declaration, trusting the reader to "
        "supply SN 22.39's intervening steps. The progression from "
        "impermanence (SN 22.40) to suffering (this discourse) "
        "follows the traditional order of the three marks, the same "
        "sequence already seen in this book's Aniccavagga."
    ),
    guide=[
        ("The quartet's second substituted practice", [
            "Following the pattern SN 22.40 established, this "
            "discourse swaps in a new opening term while leaving "
            "everything else in SN 22.39's template unchanged: "
            "mendicants should meditate observing suffering "
            "(dukkhānupassī) directly in each aggregate, rather than "
            "being generally &ldquo;full of disillusionment&rdquo; or "
            "observing impermanence as SN 22.40 specified.",
        ]),
        ("The traditional order of the three marks preserved", [
            "This quartet's sequence &mdash; impermanence (SN 22.40), "
            "suffering (this discourse), not-self (SN 22.42 to "
            "follow) &mdash; matches the traditional ordering of the "
            "three marks (tilakkhaṇa) already established earlier in "
            "this book, most notably in Aniccavagga's own SN 22.15-17 "
            "telescoping trio. The order is not arbitrary; it follows "
            "the standard logical sequence in which impermanence "
            "grounds suffering, which in turn grounds not-self.",
        ]),
        ("The identical elision pattern as SN 22.40", [
            "As with SN 22.40, this discourse's source material "
            "marks a genuine gap with an ellipsis between its opening "
            "clause and closing declaration, rather than spelling out "
            "the intervening complete-understanding-then-freedom "
            "steps a second time. The elision is preserved exactly as "
            "bilara-data gives it.",
        ]),
        ("One variation remaining before the quartet closes", [
            "With impermanence and suffering both now given as "
            "alternative opening practices, only not-self remains for "
            "SN 22.42 to complete the set &mdash; closing both this "
            "quartet and Natumhākavagga itself on the third and final "
            "mark.",
        ]),
    ],
    terms=[
        ("dukkhānupassī",
         "&ldquo;observing suffering&rdquo; &mdash; the meditation "
         "practice this discourse substitutes for SN 22.40's "
         "\"observing impermanence.\""),
        ("tilakkhaṇa",
         "the &ldquo;three marks&rdquo; &mdash; here in their "
         "traditional order, impermanence already given (SN 22.40), "
         "suffering given here, not-self still to come (SN 22.42)."),
        ("peyyāla",
         "the technical term for this discourse's genuine source-"
         "level elision, identical in kind to SN 22.40's."),
        ("dukkhasmā parimuccati, vadāmi",
         "&ldquo;they're freed from suffering, I say&rdquo; &mdash; "
         "the closing declaration, unchanged from SN 22.39 and SN "
         "22.40."),
        ("anudhamma",
         "&ldquo;in line with the teaching&rdquo; &mdash; the "
         "quartet's shared subject, here accommodating its second "
         "substituted practice."),
    ],
    text_intro=(
        "The discourse in full &mdash; genuinely this short in the "
        "source, its ellipsis given exactly as bilara-data preserves "
        "it rather than expanded from SN 22.39. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.41:1.2-1.3"),
    ],
    quiz=[
        {"q": "What practice does this discourse substitute for SN 22.39's opening step?",
         "opts": [
             "Meditating observing suffering (dukkhānupassī) in the aggregates",
             "Observing impermanence, identical to SN 22.40",
             "Formal recitation of monastic rules",
             "Physical labor and manual work"],
         "correct": 0,
         "expl": "The quartet's second substituted practice, following observing impermanence."},
        {"q": "What order do the three marks follow across SN 22.40-42?",
         "opts": [
             "The traditional order: impermanence, then suffering, then not-self",
             "A random, unordered sequence",
             "Not-self first, then suffering, then impermanence",
             "Suffering first, then not-self, then impermanence"],
         "correct": 0,
         "expl": "The same traditional sequence already established in this book's Aniccavagga."},
        {"q": "Why does this traditional order matter, according to this reading guide?",
         "opts": [
             "Impermanence grounds suffering, which in turn grounds not-self, in a standard logical sequence",
             "The order is entirely arbitrary and carries no significance",
             "Not-self must always come before impermanence for logical reasons",
             "The order reflects the sequence in which the discourses were physically written"],
         "correct": 0,
         "expl": "The same logical dependency already seen in SN 22.15-17's telescoping trio."},
        {"q": "How does the source handle the chain's remaining steps in this discourse?",
         "opts": [
             "With a genuine ellipsis, trusting the reader's memory of SN 22.39's full statement",
             "By spelling them out again in full",
             "By replacing them with an entirely new set of steps",
             "By omitting them with no indication anything is missing"],
         "correct": 0,
         "expl": "The identical elision pattern as SN 22.40."},
        {"q": "What closing declaration does this discourse retain, unchanged from SN 22.39 and SN 22.40?",
         "opts": [
             "\"They're freed from suffering, I say\"",
             "\"The path is now complete for all beings\"",
             "\"Suffering shall never end\"",
             "An entirely different, new declaration"],
         "correct": 0,
         "expl": "Identical wording across all four discourses in the quartet."},
        {"q": "How many aggregates does this discourse's practice apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Named together as a group, as in SN 22.39 and SN 22.40."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the rest of the quartet."},
        {"q": "What position does this discourse hold in the vagga's closing quartet?",
         "opts": [
             "The third term, between impermanence (SN 22.40) and not-self (SN 22.42)",
             "The quartet's opening term",
             "The quartet's final term",
             "It does not belong to the quartet"],
         "correct": 0,
         "expl": "The middle position among the three variation discourses."},
        {"q": "What discourse comes immediately after this one, closing the quartet and the vagga?",
         "opts": [
             "SN 22.42, substituting observing not-self for observing suffering",
             "A return to SN 22.22",
             "A discourse from a different saṃyutta",
             "SN 22.43, opening the next vagga"],
         "correct": 0,
         "expl": "The quartet's final term, completing the three marks."},
        {"q": "Does this reading guide reconstruct the elided content and present it as this discourse's own text?",
         "opts": [
             "No — it quotes the ellipsis exactly as the source gives it",
             "Yes — the full chain is reconstructed and presented as original",
             "The elided content is replaced with unrelated material",
             "The discourse is skipped entirely"],
         "correct": 0,
         "expl": "Consistent with this project's practice on other short peyyāla stubs in this book."},
    ],
    marginalia=[
        ("The quartet's second substituted practice", [
            "observing suffering directly &mdash;",
            "following observing impermanence in SN 22.40",
        ]),
        ("The traditional order of the three marks", [
            "impermanence grounds suffering &mdash;",
            "not arbitrary, but a standard logical sequence",
        ]),
        ("The same elision as SN 22.40", [
            "the source marks a genuine gap &mdash;",
            "trusting the reader's memory of SN 22.39",
        ]),
        ("One variation remaining", [
            "not-self left for SN 22.42 &mdash;",
            "closing the quartet and the vagga together",
        ]),
    ],
    further=[
        '<a href="%s/sn22.41/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.40.html">SN 22.40 &middot; In Line With the '
        "Teaching (2nd)</a> &mdash; the previous discourse, "
        "substituting observing impermanence.",
        '<a href="sn-22.42.html">SN 22.42 &middot; In Line With the '
        "Teaching (4th)</a> &mdash; the next discourse, closing the "
        "quartet and the vagga with observing not-self.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.42 — Catutthaanudhammasutta
# --------------------------------------------------------------------------- #
page(
    22, 42, "Catutthaanudhamma", "In Line With the Teaching (4th)",
    vagga="Natumhākavagga",
    meta_title="SN 22.42 — In Line With the Teaching (4th) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Catutthaanudhammasutta &mdash; the quartet's closing "
        "term, observing not-self, ending both the quartet and "
        "Natumhākavagga itself. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.39's chain, elided identically to SN 22.40-41 "
                 "but with the quartet's third and final swapped "
                 "opening step"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; "
                       "brief and elided, closing both the quartet "
                       "and the vagga"),
    ],
    why=(
        "This discourse closes both the quartet SN 22.39 opened and "
        "Natumhākavagga itself, completing the three marks with the "
        "last of the quartet's substituted practices: meditating "
        "observing not-self (anattānupassī) in the five aggregates. "
        "As in SN 22.40 and SN 22.41, everything between this opening "
        "clause and the closing declaration is elided by the source, "
        "trusting the reader's memory of SN 22.39's full template. "
        "With impermanence, suffering, and now not-self all given as "
        "equally valid opening practices leading to the identical "
        "freedom, the quartet closes having demonstrated that "
        "&ldquo;practicing in line with the teaching&rdquo; admits "
        "more than one door into the same result."
    ),
    guide=[
        ("The quartet's third and final substituted practice", [
            "Completing the sequence SN 22.40 and SN 22.41 began, "
            "this discourse names the last of the three marks: "
            "mendicants should meditate observing not-self "
            "(anattānupassī) directly in each aggregate. With this "
            "substitution, the quartet has now given all three marks "
            "&mdash; impermanence, suffering, not-self &mdash; each "
            "as an independently sufficient opening practice within "
            "the identical chain.",
        ]),
        ("A closing that completes rather than merely continues", [
            "Unlike SN 22.40 and SN 22.41, which each opened a new "
            "variation mid-sequence, this discourse closes the "
            "sequence &mdash; there is no fourth mark waiting to be "
            "substituted in a further discourse. The quartet's "
            "structure (one full statement, then three progressively "
            "shorter variations) is now complete.",
        ]),
        ("Natumhākavagga's own close, without a dramatic flourish", [
            "This discourse also closes the vagga itself, and does so "
            "with the same understated brevity that closed Bhāravagga "
            "in SN 22.32 &mdash; no closing verse, no narrative, no "
            "colophon naming the vagga's completion. The vagga simply "
            "ends on its shortest and most compressed page, the "
            "fourth in a row of near-identical short discourses.",
        ]),
        ("What the whole quartet demonstrates together", [
            "Read as a set, SN 22.39-42 make a claim about practice "
            "worth stating explicitly: &ldquo;practicing in line with "
            "the teaching&rdquo; is not tied to any single technique "
            "&mdash; disillusionment in general, or any one of the "
            "three specific marks observed directly in meditation, "
            "each leads through the identical chain of complete "
            "understanding to the identical freedom from suffering. "
            "The quartet's repetitive structure is itself the "
            "argument for this pluralism, not merely its illustration.",
        ]),
    ],
    terms=[
        ("anattānupassī",
         "&ldquo;observing not-self&rdquo; &mdash; the meditation "
         "practice this discourse substitutes for SN 22.41's "
         "\"observing suffering,\" completing the three marks."),
        ("tilakkhaṇa",
         "the &ldquo;three marks&rdquo; &mdash; impermanence, "
         "suffering, and now not-self, all three given across this "
         "quartet as independently sufficient starting points."),
        ("peyyāla",
         "the technical term for this discourse's genuine source-"
         "level elision, identical in kind to SN 22.40 and SN 22.41's."),
        ("dukkhasmā parimuccati, vadāmi",
         "&ldquo;they're freed from suffering, I say&rdquo; &mdash; "
         "the closing declaration, unchanged across all four "
         "discourses of the quartet."),
        ("anudhamma",
         "&ldquo;in line with the teaching&rdquo; &mdash; the "
         "quartet's shared subject, now shown across four discourses "
         "to accommodate multiple equally valid practices."),
    ],
    text_intro=(
        "The discourse in full &mdash; genuinely this short in the "
        "source, its ellipsis given exactly as bilara-data preserves "
        "it rather than expanded from SN 22.39. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.42:1.2-1.3"),
    ],
    quiz=[
        {"q": "What practice does this discourse substitute for SN 22.41's \"observing suffering\"?",
         "opts": [
             "Meditating observing not-self (anattānupassī) in the aggregates",
             "Observing impermanence, identical to SN 22.40",
             "A return to \"full of disillusionment,\" identical to SN 22.39",
             "Formal debate with outsiders"],
         "correct": 0,
         "expl": "The quartet's third and final substituted practice, completing the three marks."},
        {"q": "How does this discourse's role differ from SN 22.40 and SN 22.41's?",
         "opts": [
             "It closes the sequence, rather than opening a new mid-sequence variation",
             "It opens an entirely new, separate quartet",
             "It contradicts the conclusions of SN 22.40 and SN 22.41",
             "It has no relationship to the previous two discourses"],
         "correct": 0,
         "expl": "There is no fourth mark waiting to be substituted in a further discourse."},
        {"q": "How does this discourse close Natumhākavagga?",
         "opts": [
             "With understated brevity, no closing verse or narrative, similar to Bhāravagga's own close in SN 22.32",
             "With an elaborate closing verse naming the vagga's completion",
             "With a lengthy narrative describing the vagga's overall meaning",
             "With a formal colophon explicitly naming the vagga as finished"],
         "correct": 0,
         "expl": "The vagga simply ends on its shortest and most compressed page."},
        {"q": "What claim does the whole SN 22.39-42 quartet make about practice, taken together?",
         "opts": [
             "That \"practicing in line with the teaching\" is not tied to a single technique — several practices lead to the identical freedom",
             "That only observing not-self counts as genuine practice",
             "That the four practices are mutually exclusive and cannot be combined",
             "That disillusionment is invalid as a practice compared to the three marks"],
         "correct": 0,
         "expl": "The quartet's repetitive structure is itself the argument for this pluralism."},
        {"q": "How does the source handle the chain's remaining steps in this discourse?",
         "opts": [
             "With a genuine ellipsis, trusting the reader's memory of SN 22.39's full statement",
             "By spelling them out again in full",
             "By replacing them with an entirely different chain",
             "By omitting them with no indication anything is missing"],
         "correct": 0,
         "expl": "The identical elision pattern as SN 22.40 and SN 22.41."},
        {"q": "What closing declaration does this discourse retain, unchanged across the whole quartet?",
         "opts": [
             "\"They're freed from suffering, I say\"",
             "\"The vagga is now complete and closed\"",
             "\"Not-self is the only valid teaching\"",
             "An entirely different, new declaration"],
         "correct": 0,
         "expl": "Identical wording across all four discourses in the quartet."},
        {"q": "How many aggregates does this discourse's practice apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Named together as a group, as throughout the quartet."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the rest of the quartet."},
        {"q": "What position does this discourse hold in the vagga's closing quartet?",
         "opts": [
             "The fourth and final term, completing impermanence, suffering, and not-self",
             "The quartet's opening term",
             "The quartet's second term",
             "It does not belong to the quartet"],
         "correct": 0,
         "expl": "Closing the sequence SN 22.39 opened."},
        {"q": "What comes immediately after this discourse, moving beyond Natumhākavagga?",
         "opts": [
             "SN 22.43, opening Attadīpavagga, the vagga's fifth chapter",
             "A return to SN 22.33",
             "The end of the entire Khandhavagga",
             "A discourse from an entirely different saṃyutta"],
         "correct": 0,
         "expl": "The book's own systematic coverage continues into its next chapter."},
    ],
    marginalia=[
        ("The quartet's third and final substitution", [
            "observing not-self directly &mdash;",
            "completing impermanence and suffering",
        ]),
        ("A close, not another mid-sequence swap", [
            "no fourth mark remains &mdash;",
            "the sequence's structure now finished",
        ]),
        ("The vagga's quietest ending", [
            "no verse, no colophon &mdash;",
            "closing on its shortest, most compressed page",
        ]),
        ("Multiple doors onto one freedom", [
            "disillusionment, or any one mark &mdash;",
            "the quartet's repetition is itself the argument",
        ]),
    ],
    further=[
        '<a href="%s/sn22.42/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.41.html">SN 22.41 &middot; In Line With the '
        "Teaching (3rd)</a> &mdash; the previous discourse, "
        "substituting observing suffering.",
        '<a href="sn-22.39.html">SN 22.39 &middot; In Line With the '
        "Teaching</a> &mdash; the quartet's opening discourse, whose "
        "full chain this closing variation completes.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.43 — Attadīpasutta
# --------------------------------------------------------------------------- #
page(
    22, 43, "Attadīpa", "Be Your Own Island",
    vagga="Attadīpavagga",
    meta_title="SN 22.43 — Be Your Own Island | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Attadīpasutta &mdash; the famous \"be your own island\" "
        "instruction, tracing sorrow back to the fourfold "
        "self-identification with the aggregates. Opens Attadīpavagga. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A famous opening instruction, followed by a "
                 "rational inquiry into sorrow's origin and its "
                 "resolution"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "its opening line is famous, but the "
                       "discourse's argument is more intricate than "
                       "the line alone suggests"),
    ],
    why=(
        "This discourse opens Attadīpavagga with one of the most "
        "recognizable instructions in the entire canon: &ldquo;be "
        "your own island, your own refuge, with no other refuge. Let "
        "the teaching be your island and your refuge, with no other "
        "refuge&rdquo; &mdash; the same words, in a different "
        "narrative setting, that the Buddha famously gave Ānanda near "
        "the end of his life in the Mahāparinibbāna Sutta (DN 16). "
        "Here, though, the instruction is not a farewell but an "
        "opening move: having been told to be their own island, the "
        "mendicants are then told to examine rationally where sorrow, "
        "lamentation, pain, sadness, and distress actually come from "
        "&mdash; and the discourse supplies the answer through the "
        "same fourfold self-identification formula already seen in "
        "SN 22.7 earlier in this book."
    ),
    guide=[
        ("A famous instruction, given as a starting point for inquiry", [
            "The discourse's opening line &mdash; be your own island, "
            "your own refuge, with the teaching as that refuge "
            "&mdash; is not treated here as a conclusion to rest in "
            "but as the condition for a specific further task: once "
            "living this way, a mendicant should rationally examine "
            "where sorrow and its companions are actually born and "
            "produced. Refuge in oneself and the teaching is framed "
            "as what makes honest rational inquiry into suffering "
            "possible, not as a substitute for it.",
        ]),
        ("The same fourfold formula from SN 22.7, now answering a specific question", [
            "The discourse's answer to its own question recalls SN "
            "22.7's identity-view formula precisely: an unlearned "
            "ordinary person regards form as self, self as having "
            "form, form in self, or self in form (and likewise for "
            "the remaining four aggregates), and when that aggregate "
            "decays and perishes, sorrow and its companions arise. "
            "Where SN 22.7 was framed as a general teaching on "
            "anxiety, this discourse repurposes the identical formula "
            "specifically to answer the &ldquo;from what are they "
            "born&rdquo; question its own opening posed.",
        ]),
        ("A resolution that closes on the word for liberation itself", [
            "The discourse's resolution follows a similarly familiar "
            "path &mdash; understanding an aggregate's impermanence, "
            "its perishing, fading away, and cessation, and truly "
            "seeing with right understanding that all of it, past or "
            "present, is impermanent, suffering, and perishable "
            "&mdash; but closes with a distinctive phrase not used "
            "this way elsewhere in the vagga: a mendicant who lives "
            "without anxiety and therefore happily &ldquo;is said to "
            "be quenched (nibbuto) in that respect.&rdquo;",
        ]),
        ("A vagga named for self-reliance, opening on a chain of dependency", [
            "There is a pointed structural irony worth noticing in "
            "this discourse's placement as Attadīpavagga's opener: a "
            "vagga named for being one's own island and refuge opens "
            "by tracing sorrow to a person's dependent identification "
            "with aggregates that are not, in fact, a stable place to "
            "take refuge in at all. Genuine self-reliance, on this "
            "discourse's own account, requires first seeing through "
            "the false refuge the aggregates offer.",
        ]),
    ],
    terms=[
        ("attadīpa",
         "&ldquo;your own island&rdquo; &mdash; the discourse's title "
         "phrase and the vagga's own name, the same words given to "
         "Ānanda in DN 16's Mahāparinibbāna Sutta."),
        ("yoniso manasikāra",
         "&ldquo;rational examination&rdquo; &mdash; the specific "
         "practice this discourse instructs mendicants to undertake "
         "once living as their own island."),
        ("rūpaṁ attato samanupassati",
         "&ldquo;regards form as self&rdquo; &mdash; the same "
         "fourfold formula from SN 22.7, repurposed here to answer "
         "this discourse's own opening question."),
        ("aniccataṁ viditvā vayaṁ virāgaṁ nirodhaṁ",
         "&ldquo;understanding impermanence&hellip;its perishing, "
         "fading away, and cessation&rdquo; &mdash; the discourse's "
         "resolution, naming the specific understanding that gives up "
         "sorrow."),
        ("nibbuto",
         "&ldquo;quenched&rdquo; &mdash; the discourse's distinctive "
         "closing description of a mendicant who lives happily "
         "without anxiety."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each "
        "section (feeling, perception, and choices, each following "
        "the same formula spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.43:1.1-1.3"),
        ("p", "&sect;2", "sn22.43:2.1-2.5"),
        ("p", "&sect;3", "sn22.43:2.11-2.13"),
        ("p", "&sect;4", "sn22.43:3.1-3.2"),
        ("p", "&sect;5", "sn22.43:3.8-3.9"),
    ],
    quiz=[
        {"q": "What famous instruction opens this discourse?",
         "opts": [
             "Be your own island, your own refuge, with the teaching as that refuge",
             "Follow only what other monks tell you to do",
             "Never make any decisions without a teacher present",
             "Rely entirely on the local village for support"],
         "correct": 0,
         "expl": "The same words given to Ānanda in DN 16's Mahāparinibbāna Sutta."},
        {"q": "What are mendicants instructed to do once living as their own island?",
         "opts": [
             "Rationally examine where sorrow, lamentation, pain, sadness, and distress are born from",
             "Immediately stop all further inquiry",
             "Travel to a distant land for further study",
             "Recite the entire canon from memory"],
         "correct": 0,
         "expl": "Self-reliance is framed as what makes honest rational inquiry possible."},
        {"q": "What formula does this discourse use to answer its own question about sorrow's origin?",
         "opts": [
             "The same fourfold self-identification formula from SN 22.7",
             "An entirely new formula not used elsewhere in the book",
             "A formula concerning only physical illness",
             "A formula about disputes between monks"],
         "correct": 0,
         "expl": "Regarding an aggregate as self, self as having it, it in self, or self in it."},
        {"q": "What word does this discourse use to describe a mendicant who lives happily without anxiety?",
         "opts": [
             "Nibbuto, \"quenched\"",
             "Anusaya, \"underlying tendency\"",
             "Sakkāya, \"substantial reality\"",
             "Anudhamma, \"in line with the teaching\""],
         "correct": 0,
         "expl": "A distinctive closing description not used this way elsewhere in the vagga."},
        {"q": "What structural irony does this reading guide note about this discourse opening Attadīpavagga?",
         "opts": [
             "A vagga named for self-reliance opens by tracing sorrow to dependent identification with unstable aggregates",
             "The vagga is named for a discourse that appears much later, not this opening one",
             "The discourse contradicts the vagga's own title entirely",
             "There is no connection between the discourse and the vagga's name"],
         "correct": 0,
         "expl": "Genuine self-reliance requires seeing through the false refuge the aggregates offer."},
        {"q": "How does this discourse's resolution describe understanding an aggregate correctly?",
         "opts": [
             "Understanding its impermanence, perishing, fading away, and cessation",
             "Denying that the aggregate exists at all",
             "Avoiding all contact with the aggregate physically",
             "Transferring attention to a different aggregate entirely"],
         "correct": 0,
         "expl": "Truly seeing with right understanding that all of it, past or present, is impermanent, suffering, and perishable."},
        {"q": "How many aggregates does this discourse's formula apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Kusinārā, near the Buddha's final passing"],
         "correct": 0,
         "expl": "Unlike DN 16's deathbed setting, this discourse's identical opening words appear here in an ordinary Sāvatthī teaching."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.44, on the practice leading to substantial reality's origin and cessation",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Continuing with the same fourfold identity-view formula in a new technical framing."},
        {"q": "Does this discourse's opening instruction function as a conclusion or a starting point?",
         "opts": [
             "A starting point — the condition for a further rational inquiry the discourse then undertakes",
             "A conclusion with no further content following it",
             "An instruction the discourse immediately contradicts",
             "An isolated statement unconnected to what follows"],
         "correct": 0,
         "expl": "What makes honest rational inquiry into suffering possible, not a substitute for it."},
    ],
    marginalia=[
        ("A famous line, given here as a starting point", [
            "the same words as DN 16's deathbed scene &mdash;",
            "here, an opening move for rational inquiry",
        ]),
        ("SN 22.7's formula, repurposed to answer a question", [
            "self as form, form as self &mdash;",
            "now the specific answer to \"from what is sorrow born\"",
        ]),
        ("A closing word not used this way elsewhere", [
            "nibbuto, quenched &mdash;",
            "distinctive phrasing for this discourse's resolution",
        ]),
        ("A vagga named for self-reliance, opening on dependency", [
            "the aggregates offer a false refuge &mdash;",
            "genuine self-reliance sees through it first",
        ]),
    ],
    further=[
        '<a href="%s/sn22.43/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.42.html">SN 22.42 &middot; In Line With the '
        "Teaching (4th)</a> &mdash; the previous discourse, closing "
        "Natumhākavagga.",
        '<a href="sn-22.44.html">SN 22.44 &middot; Practice</a> '
        "&mdash; the next discourse, the same identity-view formula "
        "reframed through the technical term sakkāya.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.44 — Paṭipadāsutta
# --------------------------------------------------------------------------- #
page(
    22, 44, "Paṭipadā", "Practice",
    vagga="Attadīpavagga",
    meta_title="SN 22.44 — Practice | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Paṭipadāsutta &mdash; the fourfold identity-view formula "
        "reframed through the technical term sakkāya, naming the "
        "practices that lead to its origin and its cessation. From "
        "Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Two practices defined as a matched pair &mdash; the "
                 "practice leading to origin, and the practice "
                 "leading to cessation"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "introduces the technical term sakkāya, "
                       "central to identity-view terminology across "
                       "the canon"),
    ],
    why=(
        "This discourse takes the identical fourfold identity-view "
        "formula used in SN 22.43 immediately before it, and gives "
        "it a new technical name: sakkāya, rendered here as "
        "&ldquo;substantial reality&rdquo; and central throughout the "
        "canon to the compound term sakkāyadiṭṭhi, &ldquo;identity "
        "view.&rdquo; The discourse defines two practices as exact "
        "mirror opposites: the practice that leads to sakkāya's "
        "origin is precisely the fourfold self-identification with "
        "each aggregate; the practice that leads to its cessation is "
        "precisely the absence of that same identification. What "
        "changes between this discourse and SN 22.43 is not the "
        "content but the frame &mdash; here it is named as a "
        "&ldquo;practice&rdquo; (paṭipadā), giving the identical "
        "content a more procedural, path-oriented cast."
    ),
    guide=[
        ("Sakkāya, a technical term introduced without elaboration", [
            "The discourse's title question &mdash; what is the "
            "practice that leads to sakkāya's origin, and what leads "
            "to its cessation &mdash; introduces this canonically "
            "central term without pausing to define it separately; "
            "its meaning is instead supplied entirely by what "
            "follows, the fourfold self-identification formula. "
            "Sakkāya, on this discourse's own showing, simply is the "
            "state of regarding the aggregates as self in one of the "
            "four ways.",
        ]),
        ("The origin practice: the fourfold formula, named a practice", [
            "The practice leading to sakkāya's origin is defined as "
            "exactly the fourfold formula already seen in SN 22.7 and "
            "SN 22.43: regarding form as self, self as having form, "
            "form in self, or self in form, and likewise for the "
            "remaining aggregates. Calling this a &ldquo;practice&rdquo; "
            "(paṭipadā) is a distinctive framing choice &mdash; "
            "identity view is presented here not merely as a "
            "mistaken belief but as something actively practiced, "
            "with its own trajectory toward a result.",
        ]),
        ("The cessation practice: the identical formula, negated", [
            "The practice leading to sakkāya's cessation is defined "
            "as the exact negation: not regarding form as self, self "
            "as having form, form in self, or self in form, and "
            "likewise for the remaining aggregates. As in several "
            "other discourses across this book, the negative half "
            "adds no new content of its own &mdash; it establishes "
            "explicitly that both directions of the formula function "
            "as genuine practices, not merely that one is right and "
            "the other simply mistaken.",
        ]),
        ("A closing gloss naming the stakes precisely", [
            "Each half of the discourse closes with an explanatory "
            "gloss making the stakes explicit: this is called "
            "&ldquo;a way of regarding things that leads to the "
            "origin of suffering,&rdquo; and its opposite &ldquo;a "
            "way of regarding things that leads to the cessation of "
            "suffering.&rdquo; The technical vocabulary of sakkāya is "
            "thus anchored directly back to the plainer, more "
            "familiar vocabulary of dukkha used throughout the rest "
            "of the book.",
        ]),
    ],
    terms=[
        ("sakkāya",
         "&ldquo;substantial reality&rdquo; &mdash; the discourse's "
         "central technical term, central to sakkāyadiṭṭhi, "
         "\"identity view,\" throughout the canon."),
        ("sakkāyasamudayagāminī paṭipadā",
         "&ldquo;the practice that leads to the origin of substantial "
         "reality&rdquo; &mdash; the fourfold self-identification "
         "formula, here named as an active practice rather than "
         "merely a mistaken belief."),
        ("sakkāyanirodhagāminī paṭipadā",
         "&ldquo;the practice that leads to the cessation of "
         "substantial reality&rdquo; &mdash; the identical formula's "
         "exact negation."),
        ("rūpaṁ attato samanupassati",
         "&ldquo;regards form as self&rdquo; &mdash; the same "
         "fourfold formula from SN 22.7 and SN 22.43, unchanged in "
         "wording here."),
        ("dukkhasamudayagāminī&hellip;dukkhanirodhagāminī",
         "&ldquo;leads to the origin&hellip;cessation of "
         "suffering&rdquo; &mdash; the closing gloss anchoring the "
         "technical term sakkāya back to the plainer vocabulary of "
         "dukkha."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.44:1.1-1.4"),
        ("p", "&sect;2", "sn22.44:1.5-1.5"),
        ("p", "&sect;3", "sn22.44:1.10-1.12"),
        ("p", "&sect;4", "sn22.44:2.1-2.2"),
        ("p", "&sect;5", "sn22.44:2.3-2.3"),
        ("p", "&sect;6", "sn22.44:2.7-2.9"),
    ],
    quiz=[
        {"q": "What technical term does this discourse introduce, central to sakkāyadiṭṭhi throughout the canon?",
         "opts": [
             "Sakkāya, \"substantial reality\"",
             "Anusaya, \"underlying tendency\"",
             "Pariññā, \"complete understanding\"",
             "Anudhamma, \"in line with the teaching\""],
         "correct": 0,
         "expl": "Introduced without separate definition, its meaning supplied by the fourfold formula that follows."},
        {"q": "What is defined as \"the practice that leads to sakkāya's origin\"?",
         "opts": [
             "The fourfold self-identification formula from SN 22.7 and SN 22.43",
             "Physical austerity practices",
             "Formal debate with other ascetics",
             "An entirely new formula not used elsewhere in the book"],
         "correct": 0,
         "expl": "The identical formula, here framed as an active practice rather than a mistaken belief."},
        {"q": "What is defined as \"the practice that leads to sakkāya's cessation\"?",
         "opts": [
             "The exact negation of the origin-practice formula",
             "A completely different, unrelated formula",
             "Physical avoidance of all five aggregates",
             "Silence and refusal to answer questions"],
         "correct": 0,
         "expl": "Not regarding form as self, self as having form, form in self, or self in form, and likewise for the rest."},
        {"q": "What does calling identity view a \"practice\" (paṭipadā) suggest?",
         "opts": [
             "That it is something actively practiced, with its own trajectory toward a result, not merely a passive mistaken belief",
             "That it cannot be changed once adopted",
             "That it applies only to advanced meditators",
             "That it is unrelated to how a person actually lives"],
         "correct": 0,
         "expl": "A distinctive framing choice compared to SN 22.7 and SN 22.43's more descriptive presentation."},
        {"q": "What does each half of the discourse close with?",
         "opts": [
             "An explanatory gloss connecting sakkāya back to the plainer vocabulary of dukkha, suffering",
             "A closing verse in poetic form",
             "A narrative about a specific mendicant's attainment",
             "A rejection of everything stated before it"],
         "correct": 0,
         "expl": "\"A way of regarding things that leads to the origin/cessation of suffering.\""},
        {"q": "How does this discourse relate to SN 22.43 immediately before it?",
         "opts": [
             "The identical fourfold formula, reframed with new technical vocabulary (sakkāya, paṭipadā) rather than new content",
             "An entirely unrelated discourse on a different topic",
             "A direct contradiction of SN 22.43's conclusions",
             "A narrative sequel describing events after SN 22.43"],
         "correct": 0,
         "expl": "What changes is the frame, not the underlying content."},
        {"q": "How many aggregates does this discourse's formula apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.43."},
        {"q": "What distinguishes a \"learned noble disciple\" in this discourse's second half?",
         "opts": [
             "Having seen the noble ones and being skilled and trained in their teaching, they do not regard the aggregates as self",
             "Having memorized every discourse in the canon",
             "Having taken a formal vow of silence",
             "Having traveled to every major pilgrimage site"],
         "correct": 0,
         "expl": "The same contrast structure used throughout this book between the unlearned and the learned."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.45, using the three-marks logical chain from Aniccavagga with an extended closing sequence",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Returning to a chain-based argument rather than this discourse's paired-definition style."},
    ],
    marginalia=[
        ("A new technical term, defined by its formula alone", [
            "sakkāya &mdash;",
            "meaning supplied entirely by the fourfold identification",
        ]),
        ("Identity view named a practice, not just a belief", [
            "an active trajectory toward a result &mdash;",
            "not merely something passively mistaken",
        ]),
        ("The same formula, negated exactly", [
            "no new content in the negative half &mdash;",
            "both directions established as genuine practices",
        ]),
        ("Technical vocabulary anchored back to plain terms", [
            "sakkāya's origin and cessation &mdash;",
            "glossed directly as suffering's own",
        ]),
    ],
    further=[
        '<a href="%s/sn22.44/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.43.html">SN 22.43 &middot; Be Your Own '
        "Island</a> &mdash; the previous discourse, the same formula "
        "in its original framing.",
        '<a href="sn-22.45.html">SN 22.45 &middot; Impermanence</a> '
        "&mdash; the next discourse, the three-marks chain from "
        "Aniccavagga extended with a fuller closing sequence.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.45 — Aniccasutta
# --------------------------------------------------------------------------- #
page(
    22, 45, "Anicca", "Impermanence",
    vagga="Attadīpavagga",
    meta_title="SN 22.45 — Impermanence | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Aniccasutta &mdash; SN 22.15's three-marks chain "
        "extended into a fuller liberation sequence ending in "
        "personal extinguishment. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "The three-marks chain from Aniccavagga, extended "
                 "with a further multi-step liberation sequence"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "builds on SN 22.15's chain from Aniccavagga, "
                       "worth reading with that discourse in mind"),
    ],
    why=(
        "This discourse reaches back to SN 22.15's chain from "
        "Aniccavagga &mdash; form is impermanent, what's impermanent "
        "is suffering, what's suffering is not-self, and what's "
        "not-self should be seen as not mine &mdash; but does not "
        "stop where SN 22.15 stopped. It continues into a longer "
        "sequence: seeing this way, the mind becomes dispassionate "
        "and freed from defilements by not grasping; being free, it's "
        "stable; being stable, it's content; being content, one is "
        "not anxious; not being anxious, one personally becomes "
        "extinguished. The discourse thus links Aniccavagga's earlier "
        "logical chain to a fuller account of what actually follows "
        "from seeing it through to the end."
    ),
    guide=[
        ("The three-marks chain, reused rather than restated from scratch", [
            "The discourse's opening four steps &mdash; impermanent, "
            "therefore suffering, therefore not-self, therefore to be "
            "seen as not mine &mdash; are word for word identical to "
            "SN 22.15's chain from Aniccavagga. Rather than "
            "introducing new logical content, this discourse takes "
            "that established chain as its starting point and asks "
            "what happens next.",
        ]),
        ("A five-step continuation not given in SN 22.15", [
            "Where SN 22.15 stopped at &ldquo;this is not mine, I am "
            "not this, this is not my self,&rdquo; this discourse "
            "continues: the mind becomes dispassionate and freed from "
            "defilements by not grasping; being free, it's stable; "
            "being stable, it's content; being content, one is not "
            "anxious; not being anxious, one personally becomes "
            "extinguished (parinibbāyati). Each step depends strictly "
            "on the one before it, extending the earlier chain by "
            "five further links.",
        ]),
        ("A summary restatement applying to all five elements at once", [
            "After running through this extended chain for each "
            "aggregate individually, the discourse adds a further "
            "compressed restatement: if a mendicant's mind is "
            "dispassionate toward the form element, the feeling "
            "element, the perception element, the choices element, "
            "and the consciousness element, it is freed from "
            "defilements by not grasping &mdash; the same five-step "
            "sequence (stable, content, not anxious, personally "
            "extinguished) then follows once more, this time stated "
            "collectively rather than aggregate by aggregate.",
        ]),
        ("Closing on the same declaration that closed SN 22.12", [
            "The discourse ends with the identical four-part arahant "
            "declaration used to close SN 22.12 at the very start of "
            "Aniccavagga &mdash; rebirth ended, the spiritual journey "
            "completed, what had to be done done, nothing further for "
            "this place &mdash; tying this discourse's extended chain "
            "back to the book's most basic liberation formula even as "
            "it adds five new intervening steps that formula did not "
            "spell out.",
        ]),
    ],
    terms=[
        ("virāgā vimuccati anupādāya",
         "&ldquo;freed from defilements by not grasping&rdquo; "
         "&mdash; the first of the new steps this discourse adds "
         "beyond SN 22.15's chain."),
        ("ṭhitaṁ",
         "&ldquo;stable&rdquo; &mdash; the second new step, following "
         "directly from freedom."),
        ("santusitaṁ",
         "&ldquo;content&rdquo; &mdash; the third new step, following "
         "from stability."),
        ("aparitassaṁ",
         "&ldquo;not anxious&rdquo; &mdash; the fourth new step, "
         "recalling the vocabulary of paritassanā (anxiety) from SN "
         "22.7-8 earlier in the book."),
        ("paccattaññeva parinibbāyati",
         "&ldquo;personally becomes extinguished&rdquo; &mdash; the "
         "fifth and final new step, the discourse's furthest "
         "extension beyond SN 22.15's original chain."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in the "
        "aggregate-by-aggregate exposition (feeling, perception, and "
        "choices, each following the same extended chain spelled out "
        "in full for form and consciousness) are given exactly as "
        "bilara-data preserves them. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.45:1.2-1.6"),
        ("p", "&sect;2", "sn22.45:1.10-1.14"),
        ("p", "&sect;3", "sn22.45:1.15-1.19"),
        ("p", "&sect;4", "sn22.45:1.20-1.20"),
    ],
    quiz=[
        {"q": "What earlier discourse's chain does this discourse's opening four steps reuse word for word?",
         "opts": [
             "SN 22.15, from Aniccavagga",
             "SN 22.22, from Bhāravagga",
             "SN 22.35, from Natumhākavagga",
             "SN 22.1, the book's opening discourse"],
         "correct": 0,
         "expl": "Impermanent, therefore suffering, therefore not-self, therefore to be seen as not mine."},
        {"q": "What is the first of the new steps this discourse adds beyond SN 22.15's chain?",
         "opts": [
             "The mind becomes dispassionate and freed from defilements by not grasping",
             "The mendicant immediately teaches the chain to others",
             "The mendicant is reborn in a heavenly realm",
             "The mendicant returns to lay life"],
         "correct": 0,
         "expl": "The first of five new links extending SN 22.15's original four-step chain."},
        {"q": "What is the final step in this discourse's extended chain?",
         "opts": [
             "Personally becoming extinguished (parinibbāyati)",
             "Returning to the beginning of the chain",
             "Teaching the Dhamma to a large assembly",
             "A fourth aggregate not mentioned before"],
         "correct": 0,
         "expl": "The furthest point this discourse's chain reaches, following from being not anxious."},
        {"q": "What does the discourse add after running the extended chain aggregate by aggregate?",
         "opts": [
             "A compressed restatement applying the same sequence collectively to all five elements at once",
             "A denial that the chain applies to more than one aggregate",
             "An entirely new, unrelated argument",
             "A narrative describing a specific mendicant's experience"],
         "correct": 0,
         "expl": "Dispassion toward all five elements together, followed by the same stable-content-not anxious-extinguished sequence."},
        {"q": "What declaration closes this discourse, identical to SN 22.12's closing?",
         "opts": [
             "\"Rebirth is ended, the spiritual journey has been completed, what had to be done has been done, there is nothing further for this place\"",
             "\"The five aggregates no longer exist for anyone\"",
             "\"I shall now teach for eighty years without rest\"",
             "An entirely different, new declaration"],
         "correct": 0,
         "expl": "Tying this discourse's extended chain back to Aniccavagga's most basic liberation formula."},
        {"q": "What vocabulary does \"not anxious\" (aparitassaṁ) recall from earlier in the book?",
         "opts": [
             "SN 22.7-8's discussion of anxiety (paritassanā) caused by grasping",
             "SN 22.22's burden imagery",
             "SN 22.30's disease vocabulary",
             "SN 22.33's Jeta's Grove simile"],
         "correct": 0,
         "expl": "A deliberate echo of terminology used earlier in Khandhavagga."},
        {"q": "How many aggregates does this discourse's extended chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "How does this discourse relate to SN 22.15?",
         "opts": [
             "It takes SN 22.15's chain as an established starting point and extends it by five further steps",
             "It directly contradicts SN 22.15's conclusions",
             "It has no relationship to SN 22.15",
             "It shortens SN 22.15's chain rather than extending it"],
         "correct": 0,
         "expl": "Reusing established content rather than reintroducing new logical content."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.46, a shorter companion adding a different intervening reflection",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "A companion discourse building on the same chain with a distinct addition of its own."},
    ],
    marginalia=[
        ("An established chain reused, not restated from scratch", [
            "SN 22.15's four steps, word for word &mdash;",
            "this discourse asks what follows next",
        ]),
        ("Five new steps beyond \"not mine\"", [
            "dispassionate, freed, stable, content, not anxious &mdash;",
            "each depending strictly on the one before it",
        ]),
        ("Individual then collective, the same sequence twice", [
            "aggregate by aggregate, then all five at once &mdash;",
            "the identical five-step conclusion each time",
        ]),
        ("Extended content, the same closing declaration", [
            "tying back to SN 22.12's own close &mdash;",
            "five new links added to an old formula",
        ]),
    ],
    further=[
        '<a href="%s/sn22.45/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.44.html">SN 22.44 &middot; Practice</a> '
        "&mdash; the previous discourse, the identity-view formula "
        "framed through the term sakkāya.",
        '<a href="sn-22.46.html">SN 22.46 &middot; Impermanence '
        "(2nd)</a> &mdash; the next discourse, the same chain with a "
        "different intervening reflection on speculative views.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.46 — Dutiyaaniccasutta
# --------------------------------------------------------------------------- #
page(
    22, 46, "Dutiyaanicca", "Impermanence (2nd)",
    vagga="Attadīpavagga",
    meta_title="SN 22.46 — Impermanence (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyaaniccasutta &mdash; SN 22.45's chain with a "
        "distinctive insertion: giving up theories about the world's "
        "first beginning and final end. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.45's chain, with a distinctive intervening "
                 "reflection on speculative views replacing that "
                 "discourse's dispassion-freedom sequence's opening"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "its inserted reflection on speculative views "
                       "connects to a wider canonical debate"),
    ],
    why=(
        "This discourse repeats SN 22.45's opening three-marks chain "
        "exactly, but inserts a distinctive new reflection before "
        "reaching the same closing sequence: seeing truly with right "
        "understanding, a mendicant has no theories about the "
        "&ldquo;first beginning&rdquo; (pubbanta); not having "
        "theories about the first beginning, they have no theories "
        "about the &ldquo;final end&rdquo; (aparanta); and not having "
        "theories about the final end, they don't obstinately stick "
        "to them. This connects the chain to the canon's well-known "
        "cluster of speculative questions about the world's ultimate "
        "origin and destiny &mdash; questions the Buddha elsewhere "
        "famously declined to answer &mdash; treating freedom from "
        "such speculation as a direct consequence of seeing the "
        "aggregates rightly."
    ),
    guide=[
        ("The identical opening chain, once more", [
            "As in SN 22.45, this discourse opens with the "
            "established three-marks chain from SN 22.15: form is "
            "impermanent, what's impermanent is suffering, what's "
            "suffering is not-self, and what's not-self should be "
            "seen with right understanding as not mine, not I, not my "
            "self. The wording matches exactly, run through for each "
            "of the five aggregates.",
        ]),
        ("A new link about theories of beginning and end", [
            "Where SN 22.45 moved directly from &ldquo;not mine&rdquo; "
            "to dispassion, this discourse inserts three additional "
            "steps: seeing truly this way, a mendicant has no "
            "theories about the world's first beginning; having none "
            "about the first beginning, none about its final end "
            "either; and having none about the final end, they don't "
            "obstinately stick to any such theory. This chain of "
            "three connects directly to the canon's well-known set of "
            "unanswered questions (avyākata) about whether the world "
            "is eternal or not, finite or infinite.",
        ]),
        ("Freedom from speculation as a consequence, not a separate discipline", [
            "The discourse's structure implies something worth "
            "noting: freedom from speculative theorizing about "
            "ultimate origins and endings is presented here not as a "
            "separate meditative discipline requiring its own "
            "training, but as a direct, automatic consequence of "
            "correctly seeing the aggregates' impermanence, "
            "suffering, and not-self nature. Someone who no longer "
            "clings to the aggregates as self has, by that very fact, "
            "nothing left to build such speculative theories around.",
        ]),
        ("Rejoining SN 22.45's sequence and closing identically", [
            "After this inserted reflection, the discourse rejoins "
            "SN 22.45's sequence almost exactly &mdash; not "
            "misapprehending, the mind becomes dispassionate; freed, "
            "stable, content, not anxious, personally extinguished "
            "&mdash; and closes with the identical arahant "
            "declaration. The new material is inserted into an "
            "otherwise unchanged frame, rather than replacing any "
            "part of it.",
        ]),
    ],
    terms=[
        ("pubbantānudiṭṭhi",
         "&ldquo;theories about the first beginning&rdquo; &mdash; "
         "the first of the discourse's new inserted steps, connecting "
         "to the canon's cluster of unanswered speculative questions."),
        ("aparantānudiṭṭhi",
         "&ldquo;theories about the final end&rdquo; &mdash; the "
         "second inserted step, paired with theories of the first "
         "beginning."),
        ("na tadupādiyati",
         "&ldquo;doesn't obstinately stick to them&rdquo; &mdash; the "
         "third inserted step, describing the absence of clinging to "
         "either kind of theory."),
        ("avyākata",
         "&ldquo;undetermined&rdquo; or &ldquo;unanswered&rdquo; "
         "&mdash; the standard canonical term for questions like "
         "these about the world's ultimate origin and destiny, which "
         "this discourse's inserted reflection directly recalls."),
        ("paccattaññeva parinibbāyati",
         "&ldquo;personally becomes extinguished&rdquo; &mdash; the "
         "closing step, unchanged from SN 22.45, once the discourse "
         "rejoins its established sequence."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in the "
        "opening exposition (feeling, perception, and choices, each "
        "following the same chain spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.46:1.2-1.5"),
        ("p", "&sect;2", "sn22.46:1.9-1.12"),
        ("p", "&sect;3", "sn22.46:2.1-2.4"),
        ("p", "&sect;4", "sn22.46:2.9-2.10"),
    ],
    quiz=[
        {"q": "What does this discourse's opening chain repeat exactly from SN 22.45?",
         "opts": [
             "The three-marks chain: impermanent, therefore suffering, therefore not-self, therefore not mine",
             "An entirely new chain not seen before in the book",
             "A chain concerning only the aggregate of consciousness",
             "A narrative about a specific mendicant"],
         "correct": 0,
         "expl": "The same wording as SN 22.15 and SN 22.45's opening steps."},
        {"q": "What new steps does this discourse insert before reaching SN 22.45's closing sequence?",
         "opts": [
             "Having no theories about the world's first beginning or final end, and not obstinately sticking to such theories",
             "A new fourth aggregate not previously discussed",
             "A narrative describing a debate with outsiders",
             "A denial that the three marks apply to consciousness"],
         "correct": 0,
         "expl": "Pubbantānudiṭṭhi and aparantānudiṭṭhi, connecting to the canon's unanswered questions."},
        {"q": "What canonical category do \"theories about the first beginning and final end\" belong to?",
         "opts": [
             "Avyākata, the \"undetermined\" or \"unanswered\" questions the Buddha elsewhere declined to answer",
             "The four noble truths",
             "The Vinaya rules for monastic discipline",
             "The standard arahant declaration"],
         "correct": 0,
         "expl": "Questions about whether the world is eternal or not, finite or infinite, among others."},
        {"q": "How does this discourse present freedom from speculative theorizing?",
         "opts": [
             "As a direct, automatic consequence of correctly seeing the aggregates' impermanence, suffering, and not-self nature",
             "As an entirely separate meditative discipline requiring its own distinct training",
             "As something achieved only after freedom from speculation is first attained separately",
             "As unrelated to the three marks entirely"],
         "correct": 0,
         "expl": "Someone no longer clinging to the aggregates as self has nothing left to build such theories around."},
        {"q": "How does the discourse's structure treat the new inserted material?",
         "opts": [
             "Inserted into an otherwise unchanged frame, rather than replacing any part of SN 22.45's sequence",
             "As a complete replacement for SN 22.45's entire chain",
             "As contradicting everything in SN 22.45",
             "As an isolated addition disconnected from the rest of the discourse"],
         "correct": 0,
         "expl": "The discourse rejoins SN 22.45's sequence almost exactly after the inserted reflection."},
        {"q": "What closing declaration does this discourse retain, unchanged from SN 22.45?",
         "opts": [
             "The standard four-part arahant declaration",
             "A denial that liberation is possible",
             "A promise to teach the chain to future generations only",
             "An entirely different, new declaration"],
         "correct": 0,
         "expl": "Identical wording once the discourse rejoins SN 22.45's established sequence."},
        {"q": "How many aggregates does this discourse's chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.45."},
        {"q": "What relationship does this discourse have to SN 22.45?",
         "opts": [
             "A companion discourse sharing the same opening and closing but inserting distinctive new intervening content",
             "A direct contradiction of SN 22.45's claims",
             "An entirely unrelated discourse placed nearby by coincidence",
             "An exact word-for-word repetition with no differences at all"],
         "correct": 0,
         "expl": "The insertion about theories of beginning and end is this discourse's distinctive addition."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.47, showing that all views of self among ascetics and brahmins reduce to one of the five aggregates",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Continuing the vagga's exploration of identity view from a new angle."},
    ],
    marginalia=[
        ("The same chain, once more, word for word", [
            "impermanent, suffering, not-self, not mine &mdash;",
            "identical to SN 22.15 and SN 22.45",
        ]),
        ("Speculation about beginning and end, given up", [
            "the canon's own unanswered questions &mdash;",
            "connected here directly to seeing the aggregates rightly",
        ]),
        ("A consequence, not a separate discipline", [
            "nothing left to build theories around &mdash;",
            "freedom from speculation follows automatically",
        ]),
        ("New content inserted, the frame left intact", [
            "not a replacement &mdash;",
            "SN 22.45's sequence rejoined and closed identically",
        ]),
    ],
    further=[
        '<a href="%s/sn22.46/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.45.html">SN 22.45 &middot; Impermanence</a> '
        "&mdash; the previous discourse, the same chain without this "
        "discourse's inserted reflection.",
        '<a href="sn-22.47.html">SN 22.47 &middot; Ways of '
        "Regarding</a> &mdash; the next discourse, showing all "
        "self-views reduce to the five aggregates.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.47 — Samanupassanāsutta
# --------------------------------------------------------------------------- #
page(
    22, 47, "Samanupassanā", "Ways of Regarding",
    vagga="Attadīpavagga",
    meta_title="SN 22.47 — Ways of Regarding | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Samanupassanāsutta &mdash; every ascetic and brahmin's "
        "self-view reduces to one of the five aggregates, and the "
        "conceit \"I am\" is traced to ignorance touching the five "
        "faculties. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A sweeping general claim about all self-views, "
                 "followed by an analysis of the conceit \"I am\" and "
                 "its nine future-oriented variants"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; "
                       "one of the more doctrinally dense discourses "
                       "in the vagga, worth reading slowly"),
    ],
    why=(
        "This discourse opens with an unusually sweeping claim: "
        "whatever ascetics and brahmins regard various kinds of "
        "things as self, all of them, without exception, are "
        "regarding one or more of the five grasping aggregates. There "
        "is no self-view in the entire range of ascetic and brahmanic "
        "speculation, the discourse asserts, that falls outside this "
        "fivefold scheme. From there, the discourse traces the "
        "psychological mechanics of how this works: an unlearned "
        "ordinary person, not rid of the identity-view formula and "
        "the conceit &ldquo;I am,&rdquo; experiences the five "
        "faculties (eye through body) and, struck by feelings born of "
        "contact with ignorance, generates a specific list of nine "
        "self-referential and future-oriented thoughts &mdash; a list "
        "that appears, with variations, at several points across the "
        "canon's treatment of speculative views about personal "
        "continuity."
    ),
    guide=[
        ("A totalizing claim about the scope of self-view", [
            "The discourse's opening move covers extraordinary "
            "ground in a single sentence: every ascetic and brahmin "
            "who regards anything at all as self is, in every case, "
            "regarding the five grasping aggregates or one of them. "
            "This is not a claim about Buddhist practitioners "
            "specifically but about the entire field of contemporary "
            "religious and philosophical speculation on selfhood, "
            "asserting that it all reduces, without remainder, to the "
            "same fivefold classificatory scheme this book has been "
            "using throughout.",
        ]),
        ("From the fourfold formula to the conceit \"I am\"", [
            "The discourse then narrows to its psychological "
            "analysis: someone not rid of the fourfold "
            "self-identification formula is, by that very fact, not "
            "rid of the conceit &ldquo;I am&rdquo; (asmimāna). As "
            "long as that conceit persists, the five faculties (the "
            "eye, ear, nose, tongue, and body) are &ldquo;conceived&rdquo; "
            "&mdash; taken up as belonging to or constituting a self "
            "&mdash; along with the mind, ideas, and what the "
            "discourse calls &ldquo;the element of ignorance.&rdquo;",
        ]),
        ("A specific list of nine self-referential thoughts", [
            "Struck by feelings born of contact with ignorance, an "
            "unlearned ordinary person generates a specific sequence "
            "of nine thoughts: &lsquo;I am&rsquo;, &lsquo;I am "
            "this&rsquo;, &lsquo;I will be&rsquo;, &lsquo;I will not "
            "be&rsquo;, &lsquo;I will have form&rsquo;, &lsquo;I will "
            "be formless&rsquo;, &lsquo;I will be percipient&rsquo;, "
            "&lsquo;I will not be percipient&rsquo;, &lsquo;I will be "
            "neither percipient nor non-percipient&rsquo;. This "
            "sequence moves from a bare present-tense assertion of "
            "existence through increasingly specific speculations "
            "about the nature of a future self &mdash; embodied or "
            "formless, conscious or unconscious in various ways.",
        ]),
        ("The faculties stay put; only the response to them changes", [
            "The discourse's resolution is precise: the five "
            "faculties themselves &ldquo;stay right where they "
            "are&rdquo; &mdash; nothing about sensory experience "
            "itself needs to change. What changes for a learned "
            "noble disciple is that ignorance about them is given up "
            "and knowledge arises instead, and with that shift, none "
            "of the nine self-referential thoughts arises any longer. "
            "The problem, on this discourse's account, was never the "
            "faculties themselves but the ignorance interpreting them.",
        ]),
    ],
    terms=[
        ("yena yena hi maññanti tato taṁ hoti aññathā",
         "the discourse's opening scope claim &mdash; whatever "
         "self-view any ascetic or brahmin holds, it reduces to one "
         "or more of the five grasping aggregates."),
        ("asmimāna",
         "&ldquo;the conceit &lsquo;I am&rsquo;&rdquo; &mdash; the "
         "underlying self-referential conceit this discourse traces "
         "back to the fourfold identity-view formula."),
        ("avijjādhātu",
         "&ldquo;the element of ignorance&rdquo; &mdash; named "
         "alongside the five faculties and the mind as present when "
         "the conceit &ldquo;I am&rdquo; has not been given up."),
        ("avijjāsamphassajena vedayitena phuṭṭho",
         "&ldquo;struck by feelings born of contact with "
         "ignorance&rdquo; &mdash; the discourse's account of what "
         "immediately precedes the arising of the nine self-"
         "referential thoughts."),
        ("bhavissāmi, na bhavissāmi",
         "&ldquo;I will be&rdquo;, &ldquo;I will not be&rdquo; "
         "&mdash; two of the nine thoughts, moving speculation from "
         "the present into explicit future-oriented existential "
         "questions."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in the "
        "opening exposition (feeling, perception, and choices, each "
        "following the same formula spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.47:1.2-1.9"),
        ("p", "&sect;2", "sn22.47:2.1-2.13"),
        ("p", "&sect;3", "sn22.47:3.1-3.11"),
    ],
    quiz=[
        {"q": "What sweeping claim opens this discourse?",
         "opts": [
             "Every ascetic and brahmin's self-view reduces to one or more of the five grasping aggregates",
             "Only Buddhist practitioners hold mistaken self-views",
             "There is no such thing as a self-view anywhere",
             "Self-views vary too widely to be classified at all"],
         "correct": 0,
         "expl": "A totalizing claim covering the entire field of contemporary religious speculation on selfhood."},
        {"q": "What does the discourse claim persists as long as the fourfold identity-view formula is not given up?",
         "opts": [
             "The conceit \"I am\" (asmimāna)",
             "Physical illness",
             "Monastic obligations",
             "Access to the five faculties"],
         "correct": 0,
         "expl": "The conceit's persistence is tied directly to the fourfold formula's persistence."},
        {"q": "What precedes the arising of the nine self-referential thoughts, according to this discourse?",
         "opts": [
             "Being struck by feelings born of contact with ignorance",
             "A formal teaching from an outside instructor",
             "Physical exercise",
             "A dream experienced during sleep"],
         "correct": 0,
         "expl": "Avijjāsamphassajena vedayitena phuṭṭho — the discourse's precise causal account."},
        {"q": "What is the first of the nine thoughts this discourse lists?",
         "opts": [
             "\"I am\"",
             "\"I will be formless\"",
             "\"I will not be\"",
             "\"I am this\""],
         "correct": 0,
         "expl": "The bare present-tense assertion opening the sequence of nine."},
        {"q": "How does the sequence of nine thoughts develop as it continues?",
         "opts": [
             "From a bare present-tense assertion of existence to increasingly specific speculations about a future self",
             "It repeats the same single thought nine times without variation",
             "It moves from future speculation back to a denial of any self at all",
             "It concerns only physical form, not consciousness"],
         "correct": 0,
         "expl": "Embodied or formless, conscious or unconscious in various specific ways."},
        {"q": "What does this discourse claim happens to the five faculties for a learned noble disciple?",
         "opts": [
             "They stay right where they are — only the response to them changes",
             "They are physically destroyed",
             "They become permanently blocked from functioning",
             "They are replaced by an entirely new set of faculties"],
         "correct": 0,
         "expl": "The problem was never the faculties themselves but the ignorance interpreting them."},
        {"q": "What replaces ignorance for a learned noble disciple, according to this discourse?",
         "opts": [
             "Knowledge (vijjā)",
             "A stronger form of the same ignorance",
             "Complete sensory deprivation",
             "An entirely new set of faculties"],
         "correct": 0,
         "expl": "With ignorance's fading and knowledge's arising, none of the nine thoughts arises any longer."},
        {"q": "How many aggregates does this discourse's opening formula apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only consciousness",
             "Only feeling and perception"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.48, defining the technical distinction between the five aggregates and the five grasping aggregates",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "A precise doctrinal definition following this discourse's dense psychological analysis."},
    ],
    marginalia=[
        ("A claim covering the entire field of speculation", [
            "every ascetic and brahmin's self-view &mdash;",
            "all reducing to the same fivefold scheme",
        ]),
        ("The conceit \"I am\" traced to its root", [
            "not rid of the fourfold formula &mdash;",
            "not rid of asmimāna either",
        ]),
        ("Nine thoughts, moving from present to future", [
            "I am, I will be, I will have form &mdash;",
            "increasingly specific speculation about what follows",
        ]),
        ("The faculties untouched; only ignorance addressed", [
            "nothing about sensation itself changes &mdash;",
            "knowledge simply replaces what interpreted it wrongly",
        ]),
    ],
    further=[
        '<a href="%s/sn22.47/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.46.html">SN 22.46 &middot; Impermanence '
        "(2nd)</a> &mdash; the previous discourse, closing on "
        "freedom from speculative theories.",
        '<a href="sn-22.48.html">SN 22.48 &middot; Aggregates</a> '
        "&mdash; the next discourse, precisely defining the "
        "distinction between the five aggregates and the five "
        "grasping aggregates.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.48 — Khandhasutta
# --------------------------------------------------------------------------- #
page(
    22, 48, "Khandha", "Aggregates",
    vagga="Attadīpavagga",
    meta_title="SN 22.48 — Aggregates | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Khandhasutta &mdash; the canonical definition "
        "distinguishing the five aggregates in general from the five "
        "grasping aggregates specifically, using the same elevenfold "
        "formula as the Buddha's second sermon. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "Two precise definitions given as a matched pair, "
                 "using an elevenfold classificatory formula for each "
                 "aggregate"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a precise technical definition, worth "
                       "reading carefully for its exact scope"),
    ],
    why=(
        "This discourse supplies a distinction the book has largely "
        "left implicit until now: the difference between "
        "&ldquo;the five aggregates&rdquo; (pañcakkhandhā) as a "
        "general classificatory scheme covering every instance of "
        "form, feeling, perception, choices, and consciousness "
        "whatsoever, and &ldquo;the five grasping aggregates&rdquo; "
        "(pañcupādānakkhandhā) &mdash; the specific subset "
        "&ldquo;accompanied by defilements and fueling "
        "grasping&rdquo; that this saṃyutta's teachings on suffering "
        "actually target. Both definitions use the same elevenfold "
        "formula &mdash; past, future, or present; internal or "
        "external; coarse or fine; inferior or superior; far or near "
        "&mdash; the identical wording used in SN 22.59, the "
        "Buddha's famous second sermon already published elsewhere in "
        "this book, showing this formula functioning here as a "
        "precise technical definition rather than merely a rhetorical "
        "flourish."
    ),
    guide=[
        ("A distinction the book has assumed rather than stated", [
            "Throughout Khandhavagga, &ldquo;the aggregates&rdquo; and "
            "&ldquo;the grasping aggregates&rdquo; have often been "
            "used interchangeably in ordinary discussion. This "
            "discourse steps back to make the distinction explicit: "
            "the Buddha announces he will teach both the five "
            "aggregates and the five grasping aggregates as two "
            "separate, precisely defined categories.",
        ]),
        ("The five aggregates: a comprehensive classificatory scheme", [
            "The five aggregates are defined using an elevenfold "
            "formula applied to each: any kind of form at all "
            "&mdash; past, future, or present; internal or external; "
            "solid or subtle; inferior or superior; far or near "
            "&mdash; all of it together is called the aggregate of "
            "form. This definition is exhaustive by design: it "
            "covers every instance of form that could possibly exist, "
            "with no qualification about defilement or grasping "
            "attached to it.",
        ]),
        ("The five grasping aggregates: the same scope, one added qualifier", [
            "The five grasping aggregates use the identical elevenfold "
            "scope &mdash; past, future, or present, internal or "
            "external, and so on &mdash; but add one further "
            "qualification: form &ldquo;which is accompanied by "
            "defilements and fuels grasping.&rdquo; The two "
            "definitions are not different in their coverage of time, "
            "location, or scale; they differ specifically in whether "
            "defilement and grasping are attached to the form in "
            "question.",
        ]),
        ("The same formula already familiar from the Buddha's second sermon", [
            "This elevenfold formula &mdash; past, future, or "
            "present; internal or external; coarse or fine; inferior "
            "or superior; far or near &mdash; is the identical "
            "wording SN 22.59 (the Anattalakkhaṇa Sutta, the Buddha's "
            "second sermon, already published as one of this book's "
            "pre-existing pages) uses to specify exactly what "
            "&ldquo;all form&rdquo; must be seen as not-self. Seeing "
            "the formula here in its own dedicated definitional "
            "context clarifies what it is doing whenever it recurs "
            "elsewhere in the book: not decoration, but a precise "
            "specification of total scope.",
        ]),
    ],
    terms=[
        ("pañcakkhandhā",
         "&ldquo;the five aggregates&rdquo; &mdash; the general "
         "classificatory scheme covering every instance of form, "
         "feeling, perception, choices, and consciousness, with no "
         "qualification about defilement."),
        ("pañcupādānakkhandhā",
         "&ldquo;the five grasping aggregates&rdquo; &mdash; the "
         "specific subset accompanied by defilements and fueling "
         "grasping, the actual target of this saṃyutta's teachings on "
         "suffering."),
        ("atītānāgatapaccuppannaṁ, ajjhattaṁ vā bahiddhā vā",
         "&ldquo;past, future, or present; internal or external&rdquo; "
         "&mdash; the opening terms of the elevenfold formula applied "
         "to each aggregate."),
        ("oḷārikaṁ vā sukhumaṁ vā, hīnaṁ vā paṇītaṁ vā, yaṁ dūre santike vā",
         "&ldquo;coarse or fine; inferior or superior; far or "
         "near&rdquo; &mdash; the remaining terms of the elevenfold "
         "formula, completing its comprehensive scope."),
        ("sāsavaṁ upādāniyaṁ",
         "&ldquo;accompanied by defilements and fuels grasping&rdquo; "
         "&mdash; the single qualifying phrase distinguishing the "
         "grasping aggregates from the aggregates in general."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions in each "
        "definition (feeling, perception, and choices, each following "
        "the same elevenfold formula spelled out in full for form and "
        "consciousness) are given exactly as bilara-data preserves "
        "them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.48:1.1-1.5"),
        ("p", "&sect;2", "sn22.48:1.9-1.10"),
        ("p", "&sect;3", "sn22.48:2.1-2.2"),
        ("p", "&sect;4", "sn22.48:2.6-2.7"),
    ],
    quiz=[
        {"q": "What two categories does this discourse define as a matched pair?",
         "opts": [
             "The five aggregates in general, and the five grasping aggregates specifically",
             "The five aggregates and the six sense fields",
             "The five faculties and the five hindrances",
             "The four noble truths and the eightfold path"],
         "correct": 0,
         "expl": "A distinction the book has largely used interchangeably until this explicit definition."},
        {"q": "What elevenfold formula does the discourse use to define each aggregate's scope?",
         "opts": [
             "Past, future, or present; internal or external; coarse or fine; inferior or superior; far or near",
             "Pleasant, painful, or neutral only",
             "Physical, mental, or spiritual only",
             "Visible, audible, or tangible only"],
         "correct": 0,
         "expl": "An exhaustive scope covering every possible instance of an aggregate."},
        {"q": "What single additional qualifier distinguishes the grasping aggregates from the aggregates in general?",
         "opts": [
             "\"Accompanied by defilements and fuels grasping\"",
             "\"Existing only in the present moment\"",
             "\"Visible to the naked eye\"",
             "\"Belonging exclusively to advanced meditators\""],
         "correct": 0,
         "expl": "The two definitions share identical scope in time, location, and scale; they differ only in this one qualifier."},
        {"q": "Where else in this book does the identical elevenfold formula appear?",
         "opts": [
             "SN 22.59, the Buddha's second sermon (the Anattalakkhaṇa Sutta), already published as a pre-existing page",
             "SN 22.1, the book's opening discourse",
             "SN 22.22, the burden discourse",
             "Nowhere else in the book"],
         "correct": 0,
         "expl": "The identical wording specifies exactly what \"all form\" must be seen as not-self."},
        {"q": "What does recognizing this formula's recurrence clarify, according to this reading guide?",
         "opts": [
             "That the formula functions as a precise specification of total scope, not merely rhetorical decoration",
             "That the formula was added by later editors and is not original",
             "That the formula only applies to the aggregate of form",
             "That the formula contradicts SN 22.59's own usage"],
         "correct": 0,
         "expl": "Seeing it here in its own dedicated definitional context clarifies its function elsewhere."},
        {"q": "Does the definition of \"the five aggregates\" include any qualification about defilement?",
         "opts": [
             "No — it is a comprehensive scheme with no qualification about defilement or grasping attached",
             "Yes — it applies only to aggregates free of defilement",
             "Yes — it applies only to aggregates fully consumed by defilement",
             "The discourse does not address this question"],
         "correct": 0,
         "expl": "The general aggregates cover every instance of form, feeling, etc., regardless of defilement."},
        {"q": "How many aggregates does this discourse's definition cover?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Devadaha",
             "Rājagaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as the vagga's other discourses."},
        {"q": "How does this discourse relate to SN 22.47 immediately before it?",
         "opts": [
             "A precise doctrinal definition following that discourse's dense psychological analysis of self-view",
             "A direct contradiction of SN 22.47's claims",
             "An unrelated discourse on an entirely different topic",
             "A narrative sequel describing events after SN 22.47"],
         "correct": 0,
         "expl": "Moving from psychological analysis to precise technical definition."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.49, a dialogue with the householder Soṇa on comparing conceits",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Introducing a new named questioner into the vagga's discussion."},
    ],
    marginalia=[
        ("A distinction left implicit, now made explicit", [
            "aggregates in general vs. grasping aggregates &mdash;",
            "often used interchangeably until this definition",
        ]),
        ("The same elevenfold scope for both definitions", [
            "past, future, present; internal, external &mdash;",
            "coarse, fine; inferior, superior; far, near",
        ]),
        ("One qualifier makes all the difference", [
            "accompanied by defilements, fueling grasping &mdash;",
            "the sole distinction between the two categories",
        ]),
        ("The same formula as the second sermon", [
            "identical wording to SN 22.59 &mdash;",
            "a precise specification, not mere decoration",
        ]),
    ],
    further=[
        '<a href="%s/sn22.48/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.47.html">SN 22.47 &middot; Ways of '
        "Regarding</a> &mdash; the previous discourse, analyzing the "
        "conceit \"I am\" and its self-referential thoughts.",
        '<a href="sn-22.49.html">SN 22.49 &middot; With Soṇa</a> '
        "&mdash; the next discourse, the householder Soṇa questioned "
        "on comparing conceits based on the aggregates.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.49 — Soṇasutta
# --------------------------------------------------------------------------- #
page(
    22, 49, "Soṇa", "With Soṇa",
    vagga="Attadīpavagga",
    meta_title="SN 22.49 — With Soṇa | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Soṇasutta &mdash; the householder Soṇa questioned on the "
        "conceits \"better, equal, worse\" based on the aggregates, "
        "closing with the full liberation chain. From Ru-Yi "
        "Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, the Bamboo Grove, the squirrels' "
                    "feeding ground"),
        ("Speakers", "The Buddha, teaching the householder Soṇa, with "
                     "a Socratic question-and-answer exchange"),
        ("Form", "A teaching on comparing conceits, followed by a "
                 "direct dialogue confirming the conclusion, closing "
                 "with the standard liberation chain"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "combines several formulas already seen "
                       "separately elsewhere in the book into one "
                       "discourse"),
    ],
    why=(
        "This discourse addresses a specific, socially loaded form of "
        "self-view not named quite this way elsewhere in the book: "
        "the comparing conceits &mdash; &ldquo;I'm better,&rdquo; "
        "&ldquo;I'm equal,&rdquo; &ldquo;I'm worse&rdquo; &mdash; "
        "that ascetics and brahmins base on the aggregates, even "
        "while acknowledging the aggregates are impermanent, "
        "suffering, and perishable. Addressed to the householder "
        "Soṇa (a different individual from the well-known monk Soṇa "
        "Koḷivisa associated elsewhere with a strung-lute simile), the "
        "discourse moves from this diagnosis into a direct Socratic "
        "exchange, confirming step by step that what is impermanent "
        "is suffering and unfit to be regarded as self, before "
        "closing with SN 22.48's elevenfold formula and SN 22.12's "
        "full liberation chain in sequence."
    ),
    guide=[
        ("Comparing conceits, held even alongside acknowledged impermanence", [
            "The discourse's diagnosis is precise: ascetics and "
            "brahmins base judgments of &ldquo;I'm better,&rdquo; "
            "&ldquo;I'm equal,&rdquo; or &ldquo;I'm worse&rdquo; on "
            "form (and the remaining aggregates), even though that "
            "form is impermanent, suffering, and perishable. Holding "
            "such comparisons at all, whatever their direction, is "
            "named directly as &ldquo;a failure to see truly&rdquo; "
            "&mdash; not holding them, by contrast, is &ldquo;seeing "
            "truly.&rdquo;",
        ]),
        ("A direct question-and-answer exchange with Soṇa", [
            "Rather than simply asserting a conclusion, the Buddha "
            "walks Soṇa through the reasoning directly: is form "
            "permanent or impermanent? Impermanent. But if "
            "impermanent, is it suffering or happiness? Suffering. "
            "But if impermanent, suffering, and perishable, is it fit "
            "to be regarded as &lsquo;this is mine, I am this, this "
            "is my self&rsquo;? No. This exchange, repeated for each "
            "aggregate, gives Soṇa's own confirmed answers equal "
            "standing with the teaching's premises, the same dialogic "
            "structure already seen in SN 22.35's mendicant narrative.",
        ]),
        ("The elevenfold formula, now applied as a practical instruction", [
            "Having secured Soṇa's agreement, the Buddha instructs him "
            "to truly see &ldquo;any kind of form at all &mdash; past, "
            "future, or present; internal or external; solid or "
            "subtle; inferior or superior; far or near&rdquo; &mdash; "
            "the identical elevenfold scope SN 22.48 defined "
            "technically &mdash; with right understanding as not "
            "mine, not I, not my self. Where SN 22.48 defined this "
            "scope, this discourse puts it directly to practical use.",
        ]),
        ("Closing on the same chain that opened the whole book's second vagga", [
            "The discourse's final movement is the identical "
            "disillusionment-to-freedom chain that closed SN 22.12 at "
            "the start of Aniccavagga: seeing this, disillusionment; "
            "disillusionment, fading desire; fading desire, freedom; "
            "freedom, knowing one is freed; and the full arahant "
            "declaration. This discourse thus draws together, in a "
            "single teaching to a single householder, threads from "
            "SN 22.7-8's comparing formulas, SN 22.12's liberation "
            "chain, and SN 22.48's elevenfold scope.",
        ]),
    ],
    terms=[
        ("seyyo'ham asmi, sadiso'ham asmi, hīno'ham asmi",
         "&ldquo;I'm better, I'm equal, I'm worse&rdquo; &mdash; the "
         "three comparing conceits this discourse names as based on "
         "the impermanent aggregates."),
        ("na h'idaṁ diṭṭhameva taṁ",
         "&ldquo;what is that but a failure to see truly&rdquo; "
         "&mdash; the discourse's verdict on holding any of the "
         "three comparing conceits, whatever their direction."),
        ("kiṁ maññasi",
         "&ldquo;what do you think&rdquo; &mdash; the opening phrase "
         "of the Socratic dialogue securing Soṇa's own confirmed "
         "agreement step by step."),
        ("atītānāgatapaccuppannaṁ&hellip;yaṁ dūre santike vā",
         "the elevenfold scope formula, identical to SN 22.48's "
         "technical definition, here applied as a direct practical "
         "instruction to Soṇa."),
        ("nibbindati&hellip;vimuccati",
         "&ldquo;grows disillusioned&hellip;is freed&rdquo; &mdash; "
         "the closing chain, identical to SN 22.12's from the start "
         "of Aniccavagga."),
    ],
    text_intro=(
        "The discourse in full. Elided repetitions in each section "
        "(feeling, perception, and choices, each following the same "
        "pattern spelled out in full for form and consciousness) are "
        "given exactly as bilara-data preserves them. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.49:2.1-2.4"),
        ("p", "&sect;2", "sn22.49:2.14-2.17"),
        ("p", "&sect;3", "sn22.49:4.1-4.8"),
        ("p", "&sect;4", "sn22.49:4.13-4.19"),
        ("p", "&sect;5", "sn22.49:5.1-5.1"),
        ("p", "&sect;6", "sn22.49:6.4-6.4"),
        ("p", "&sect;7", "sn22.49:7.1-7.3"),
    ],
    quiz=[
        {"q": "What three comparing conceits does this discourse name as based on the aggregates?",
         "opts": [
             "\"I'm better\", \"I'm equal\", \"I'm worse\"",
             "\"I'm right\", \"I'm wrong\", \"I'm undecided\"",
             "\"I exist\", \"I don't exist\", \"I'm uncertain\"",
             "\"I'm skilled\", \"I'm unskilled\", \"I'm neutral\""],
         "correct": 0,
         "expl": "All three, whatever their direction, are named as a failure to see truly."},
        {"q": "What verdict does the discourse give on holding any of these three comparisons?",
         "opts": [
             "A failure to see truly, regardless of which direction the comparison runs",
             "Only \"I'm worse\" is considered a failure; the others are acceptable",
             "Only \"I'm better\" is considered a failure",
             "All three are considered valid and accurate assessments"],
         "correct": 0,
         "expl": "Held even alongside acknowledged impermanence, all three fail to see truly."},
        {"q": "How does the Buddha secure Soṇa's understanding, rather than simply asserting a conclusion?",
         "opts": [
             "Through a direct Socratic question-and-answer exchange, confirming each step",
             "By reciting a lengthy verse without pause for questions",
             "By refusing to engage with Soṇa's questions at all",
             "By deferring the question to another disciple entirely"],
         "correct": 0,
         "expl": "Giving Soṇa's own confirmed answers equal standing with the teaching's premises."},
        {"q": "What formula does the Buddha instruct Soṇa to apply, identical to SN 22.48's technical definition?",
         "opts": [
             "The elevenfold scope: past, future, or present; internal or external; solid or subtle; inferior or superior; far or near",
             "A formula concerning only physical illness",
             "A formula about monastic robes",
             "A formula unrelated to the five aggregates"],
         "correct": 0,
         "expl": "Where SN 22.48 defined this scope, this discourse puts it to direct practical use."},
        {"q": "What chain closes this discourse, identical to SN 22.12's earlier in the book?",
         "opts": [
             "Disillusionment, fading desire, freedom, knowing one is freed, and the full arahant declaration",
             "An entirely new chain not seen before in the book",
             "A chain concerning only physical health",
             "A denial that liberation is achievable"],
         "correct": 0,
         "expl": "Drawing together threads from several earlier discourses into one teaching."},
        {"q": "Is the Soṇa in this discourse the same individual as the monk Soṇa Koḷivisa associated with the lute-string simile?",
         "opts": [
             "No — this reading guide notes they are different individuals",
             "Yes — they are explicitly identified as the same person",
             "The discourse leaves their identity entirely ambiguous",
             "Soṇa Koḷivisa does not appear anywhere else in the canon"],
         "correct": 0,
         "expl": "This Soṇa is a householder, distinct from the well-known monk associated with that separate teaching."},
        {"q": "How many aggregates does this discourse's teaching apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set, distinct from most of the vagga's other discourses?",
         "opts": [
             "Rājagaha, the Bamboo Grove, the squirrels' feeding ground",
             "Sāvatthī, Jeta's Grove",
             "Devadaha",
             "Kapilavatthu"],
         "correct": 0,
         "expl": "A shift away from the vagga's usual Sāvatthī setting."},
        {"q": "How does this discourse's structure combine material from earlier in the book?",
         "opts": [
             "It draws together threads from SN 22.7-8's comparing formulas, SN 22.12's chain, and SN 22.48's elevenfold scope",
             "It introduces entirely new material unrelated to any earlier discourse",
             "It directly contradicts SN 22.48's definition",
             "It repeats SN 22.12 word for word with no other content"],
         "correct": 0,
         "expl": "A single teaching to a single householder gathering several established threads together."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.50, a second teaching to Soṇa on what makes a \"true\" ascetic or brahmin",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "The same setting and questioner, a related but distinct criterion."},
    ],
    marginalia=[
        ("Comparison itself, not its direction, is the problem", [
            "better, equal, worse — all three &mdash;",
            "each named a failure to see truly",
        ]),
        ("Confirmed step by step, not merely asserted", [
            "kiṁ maññasi, what do you think &mdash;",
            "Soṇa's own answers given equal standing",
        ]),
        ("A defined scope, put to practical use", [
            "SN 22.48's elevenfold formula &mdash;",
            "here applied directly rather than merely defined",
        ]),
        ("Several threads drawn into one teaching", [
            "comparing conceits, the chain, the scope &mdash;",
            "gathered together for a single householder",
        ]),
    ],
    further=[
        '<a href="%s/sn22.49/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.48.html">SN 22.48 &middot; Aggregates</a> '
        "&mdash; the previous discourse, defining the elevenfold "
        "scope this discourse now applies directly.",
        '<a href="sn-22.50.html">SN 22.50 &middot; With Soṇa '
        "(2nd)</a> &mdash; the next discourse, the same setting and "
        "questioner with a criterion for true ascetics and brahmins.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.50 — Dutiyasoṇasutta
# --------------------------------------------------------------------------- #
page(
    22, 50, "Dutiyasoṇa", "With Soṇa (2nd)",
    vagga="Attadīpavagga",
    meta_title="SN 22.50 — With Soṇa (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyasoṇasutta &mdash; a strict criterion for what "
        "counts as a \"true\" ascetic or brahmin, defined by "
        "understanding each aggregate's origin, cessation, and the "
        "path to its cessation. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Rājagaha, the Bamboo Grove, the squirrels' "
                    "feeding ground"),
        ("Speakers", "The Buddha, teaching the householder Soṇa"),
        ("Form", "A strict criterion stated as a matched pair, "
                 "denying and then granting the titles \"ascetic\" "
                 "and \"brahmin\""),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "a pointed redefinition of terms other "
                       "traditions would have applied to themselves"),
    ],
    why=(
        "This discourse returns to the householder Soṇa with a "
        "different, more pointed teaching: a strict definition of "
        "what actually counts as a &ldquo;true ascetic or "
        "brahmin.&rdquo; The criterion is precise and fourfold, "
        "applied to each aggregate: understanding the aggregate "
        "itself, its origin, its cessation, and the practice leading "
        "to its cessation. Ascetics and brahmins &mdash; presumably "
        "including those of other traditions who would apply these "
        "titles to themselves as a matter of course &mdash; who lack "
        "this fourfold understanding are declared, in the Buddha's "
        "own words, not to be deemed true ascetics and brahmins at "
        "all, regardless of whatever other qualifications or "
        "reputation they might hold."
    ),
    guide=[
        ("A fourfold criterion applied to each aggregate", [
            "The discourse's criterion is precise: understanding form "
            "itself, its origin, its cessation, and the practice that "
            "leads to its cessation &mdash; the same four-part "
            "structure (a thing, its arising, its ending, and the "
            "path to that ending) that echoes the four noble truths' "
            "own shape, applied here specifically to each of the five "
            "aggregates in turn rather than to suffering as a whole.",
        ]),
        ("A denial of the titles, stated without qualification", [
            "The discourse's first half is a direct denial: ascetics "
            "and brahmins who don't understand the aggregates this "
            "fourfold way are simply not deemed &ldquo;true ascetics "
            "and brahmins&rdquo; by the Buddha, and are said not to "
            "realize the goal of ascetic or brahmanic life, nor to "
            "live having realized it with their own insight. This is "
            "a pointed reassignment of titles that other traditions "
            "would have claimed for themselves without this "
            "particular qualification.",
        ]),
        ("The identical criterion, granted rather than denied", [
            "The discourse's second half restates the same fourfold "
            "criterion, this time affirmatively: ascetics and "
            "brahmins who do understand each aggregate's origin, "
            "cessation, and the practice leading to its cessation are "
            "deemed true ascetics and brahmins, who do realize and "
            "live having realized the goal of that life with their "
            "own insight. The wording mirrors the first half almost "
            "exactly, simply negating the negation.",
        ]),
        ("A criterion of understanding, not of external practice", [
            "What is notable about this discourse's definition is "
            "what it does not mention: no reference to ascetic "
            "practices, ritual observances, or philosophical school "
            "affiliation. The sole criterion offered for the titles "
            "&ldquo;ascetic&rdquo; and &ldquo;brahmin&rdquo; is a "
            "specific, fourfold understanding of the five aggregates "
            "&mdash; redefining what these socially and religiously "
            "significant titles actually require.",
        ]),
    ],
    terms=[
        ("samaṇā vā brāhmaṇā vā",
         "&ldquo;ascetics or brahmins&rdquo; &mdash; the discourse's "
         "subject, titles this discourse redefines by a specific "
         "criterion rather than by tradition or self-identification."),
        ("samudayaṁ&hellip;atthaṅgamaṁ&hellip;paṭipadaṁ",
         "&ldquo;origin&hellip;cessation&hellip;the practice&rdquo; "
         "&mdash; the fourfold structure (thing, origin, cessation, "
         "path) echoing the four noble truths, applied here per "
         "aggregate."),
        ("na cāhaṁ te samaṇesu vā samaṇasammataṁ",
         "&ldquo;I don't deem them as true ascetics and brahmins&rdquo; "
         "&mdash; the discourse's direct denial, stated as the "
         "Buddha's own personal judgment."),
        ("sāmaññatthaṁ vā brahmaññatthaṁ vā",
         "&ldquo;the goal of life as an ascetic or brahmin&rdquo; "
         "&mdash; the specific attainment this discourse claims is "
         "unrealized without the fourfold understanding."),
        ("sayaṁ abhiññā sacchikatvā",
         "&ldquo;realized with their own insight&rdquo; &mdash; the "
         "discourse's standard for genuine attainment, requiring "
         "direct personal realization rather than secondhand "
         "knowledge."),
    ],
    text_intro=(
        "The discourse in full. Elided repetitions in each half "
        "(feeling, perception, and choices, each following the same "
        "criterion spelled out in full for form and consciousness) "
        "are given exactly as bilara-data preserves them. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.50:2.1-2.1"),
        ("p", "&sect;2", "sn22.50:2.5-2.6"),
        ("p", "&sect;3", "sn22.50:3.1-3.1"),
        ("p", "&sect;4", "sn22.50:3.5-3.6"),
    ],
    quiz=[
        {"q": "What fourfold criterion does this discourse apply to each aggregate?",
         "opts": [
             "Understanding the aggregate itself, its origin, its cessation, and the practice leading to its cessation",
             "Physical strength, ethical conduct, wisdom, and generosity",
             "Age, ordination status, education, and reputation",
             "Meditation skill, teaching ability, debate skill, and memory"],
         "correct": 0,
         "expl": "A structure echoing the four noble truths, applied specifically per aggregate."},
        {"q": "What does the discourse claim about ascetics and brahmins who lack this fourfold understanding?",
         "opts": [
             "They are not deemed \"true ascetics and brahmins\" and have not realized the goal of that life",
             "They are still considered fully accomplished regardless",
             "They are punished directly by the Buddha",
             "They are given a lesser but still valid title"],
         "correct": 0,
         "expl": "A direct denial, stated as the Buddha's own personal judgment."},
        {"q": "How does the discourse's second half relate to its first?",
         "opts": [
             "It restates the identical criterion affirmatively, granting the titles to those who do understand",
             "It contradicts the first half entirely",
             "It introduces an entirely new, unrelated criterion",
             "It denies that anyone can ever meet the criterion"],
         "correct": 0,
         "expl": "The wording mirrors the first half almost exactly, simply negating the negation."},
        {"q": "What does this discourse's criterion notably omit?",
         "opts": [
             "Any reference to ascetic practices, ritual observances, or philosophical school affiliation",
             "Any mention of the aggregates at all",
             "Any reference to understanding whatsoever",
             "Any mention of the Buddha's own judgment"],
         "correct": 0,
         "expl": "The sole criterion offered is a specific, fourfold understanding of the five aggregates."},
        {"q": "What standard does this discourse set for genuine attainment?",
         "opts": [
             "Realization with one's own insight (sayaṁ abhiññā sacchikatvā), not secondhand knowledge",
             "Public recognition from other religious teachers",
             "Formal ordination in a specific lineage",
             "Wealth accumulated through teaching"],
         "correct": 0,
         "expl": "Direct personal realization is the discourse's standard, not merely learned information."},
        {"q": "Who is this discourse addressed to, continuing from SN 22.49?",
         "opts": [
             "The householder Soṇa",
             "Venerable Ānanda",
             "An unnamed mendicant",
             "Venerable Sāriputta"],
         "correct": 0,
         "expl": "The same setting and questioner as SN 22.49 immediately before it."},
        {"q": "How many aggregates does this discourse's criterion apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Rājagaha, the Bamboo Grove, the squirrels' feeding ground",
             "Sāvatthī, Jeta's Grove",
             "Devadaha",
             "Kapilavatthu"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.49."},
        {"q": "How does this discourse's fourfold structure (thing, origin, cessation, path) echo other canonical material?",
         "opts": [
             "It echoes the four noble truths' own shape, applied here per aggregate rather than to suffering as a whole",
             "It has no relationship to any other canonical teaching",
             "It directly contradicts the four noble truths",
             "It echoes only the five precepts, not the four noble truths"],
         "correct": 0,
         "expl": "The same four-part structure applied at a more granular, per-aggregate level."},
        {"q": "What discourse comes immediately after this one?",
         "opts": [
             "SN 22.51, closing the vagga's first pair on the end of relishing",
             "A return to SN 22.33",
             "The vagga's closing uddāna",
             "A discourse from a different saṃyutta"],
         "correct": 0,
         "expl": "Moving toward the vagga's own closing pair."},
    ],
    marginalia=[
        ("A fourfold criterion, echoing the four noble truths", [
            "the aggregate, its origin, cessation, the path &mdash;",
            "applied per aggregate rather than to suffering as a whole",
        ]),
        ("Titles reassigned by a specific standard", [
            "not by tradition or self-identification &mdash;",
            "\"true ascetic and brahmin\" redefined precisely",
        ]),
        ("The same criterion, denial then grant", [
            "wording mirrored almost exactly &mdash;",
            "simply the negation negated",
        ]),
        ("Understanding alone, nothing else mentioned", [
            "no ritual, no school affiliation &mdash;",
            "the sole criterion is this fourfold knowledge",
        ]),
    ],
    further=[
        '<a href="%s/sn22.50/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.49.html">SN 22.49 &middot; With Soṇa</a> '
        "&mdash; the previous discourse, the same questioner taught "
        "on comparing conceits.",
        '<a href="sn-22.51.html">SN 22.51 &middot; The End of '
        "Relishing</a> &mdash; the next discourse, opening the "
        "vagga's closing pair.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.51 — Nandikkhayasutta
# --------------------------------------------------------------------------- #
page(
    22, 51, "Nandikkhaya", "The End of Relishing",
    vagga="Attadīpavagga",
    meta_title="SN 22.51 — The End of Relishing | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Nandikkhayasutta &mdash; relishing and greed presented as "
        "mutually ending each other, rather than one simply causing "
        "the other's end. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "A compact chain naming right view, disillusionment, "
                 "and a distinctive mutual-ending relationship between "
                 "relishing and greed"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; "
                       "its central claim about relishing and greed "
                       "repays careful, slow reading"),
    ],
    why=(
        "This discourse opens the vagga's closing pair with a "
        "distinctive claim about the relationship between two terms "
        "this book has so far treated as closely linked but not "
        "identical: relishing (nandi) and greed (rāga). Rather than "
        "presenting one as simply causing the other's end in a single "
        "direction, the discourse states the relationship as fully "
        "mutual: &ldquo;when relishing ends, greed ends. When greed "
        "ends, relishing ends.&rdquo; This bidirectional phrasing, "
        "distinct from the mostly one-directional chains used "
        "elsewhere in this saṃyutta, suggests the two are being "
        "treated less as cause and effect than as two names for "
        "aspects of a single underlying process that end together."
    ),
    guide=[
        ("Seeing impermanence itself named as right view", [
            "The discourse opens by identifying seeing impermanence "
            "directly with right view (sammādiṭṭhi) itself: "
            "&ldquo;form really is impermanent. A mendicant sees that "
            "it is impermanent: that's their right view.&rdquo; This "
            "is a strong claim &mdash; not merely that seeing "
            "impermanence is compatible with right view, or leads "
            "toward it, but that this seeing simply is what right "
            "view, in this context, consists of.",
        ]),
        ("A single step from right view to disillusionment", [
            "The discourse moves directly from right view to its "
            "consequence: &ldquo;seeing rightly, they grow "
            "disillusioned.&rdquo; No intervening steps are named "
            "&mdash; unlike SN 22.39's fuller chain (disillusionment, "
            "then complete understanding, then freedom), this "
            "discourse's structure is more compressed, moving in a "
            "single step from seeing to disillusionment.",
        ]),
        ("Relishing and greed ending each other, not one ending the other", [
            "The discourse's most distinctive claim follows "
            "immediately: &ldquo;when relishing ends, greed ends. "
            "When greed ends, relishing ends.&rdquo; This mutual "
            "phrasing stands apart from the mostly linear, one-"
            "directional chains used throughout the rest of this book "
            "(disillusionment leading to fading desire leading to "
            "freedom, in strict sequence). Here, relishing and greed "
            "are presented as ending together, each condition for the "
            "other's ending rather than one simply preceding the "
            "other in time.",
        ]),
        ("A closing formula echoing SN 22.4's earlier discourse", [
            "The discourse closes with &ldquo;the mind is freed, and "
            "is said to be well freed&rdquo; (suvimuttaṁ) &mdash; the "
            "same closing verdict SN 22.4 gave, in Nakulapituvagga, "
            "for the ending of desire and craving toward each "
            "aggregate. Reaching back across four vaggas to echo this "
            "exact phrasing gives Attadīpavagga's own closing pair a "
            "quiet structural link to the book's opening material.",
        ]),
    ],
    terms=[
        ("sammādiṭṭhissa hoti",
         "&ldquo;that's their right view&rdquo; &mdash; the "
         "discourse's strong opening identification of seeing "
         "impermanence directly with right view itself."),
        ("nandi",
         "&ldquo;relishing&rdquo; &mdash; the hinge term from SN "
         "22.5 earlier in the book, here presented as mutually "
         "ending together with greed."),
        ("rāga",
         "&ldquo;greed&rdquo; &mdash; paired with relishing in this "
         "discourse's distinctive bidirectional ending formula."),
        ("nandirāgakkhayā",
         "&ldquo;when relishing and greed end&rdquo; &mdash; the "
         "compound term treating the two as a single condition whose "
         "ending frees the mind."),
        ("suvimuttaṁ",
         "&ldquo;well freed&rdquo; &mdash; the discourse's closing "
         "verdict, echoing the identical term used in SN 22.4 in "
         "Nakulapituvagga."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same chain "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.51:1.2-1.5"),
        ("p", "&sect;2", "sn22.51:1.15-1.18"),
    ],
    quiz=[
        {"q": "What does this discourse identify directly with right view?",
         "opts": [
             "Seeing that form (and the other aggregates) is impermanent",
             "Formal ordination as a mendicant",
             "Memorizing every discourse in the collection",
             "Agreement with a specific philosophical school"],
         "correct": 0,
         "expl": "A strong claim — not merely compatible with right view, but what it consists of here."},
        {"q": "What distinctive relationship does this discourse describe between relishing and greed?",
         "opts": [
             "A mutual, bidirectional ending: when one ends, the other ends, and vice versa",
             "Relishing always ends before greed does, in strict sequence",
             "Greed always ends before relishing does, in strict sequence",
             "The two are described as entirely unrelated"],
         "correct": 0,
         "expl": "Distinct from the mostly one-directional chains used elsewhere in this book."},
        {"q": "How does this discourse's structure compare to SN 22.39's fuller chain?",
         "opts": [
             "More compressed, moving in a single step from seeing to disillusionment rather than through several intervening stages",
             "Far longer and more elaborate than SN 22.39",
             "Identical in every structural detail to SN 22.39",
             "Unrelated in structure to SN 22.39"],
         "correct": 0,
         "expl": "SN 22.39 names disillusionment, then complete understanding, then freedom in sequence."},
        {"q": "What closing phrase does this discourse share with SN 22.4, four vaggas earlier?",
         "opts": [
             "\"The mind is freed, and is said to be well freed\" (suvimuttaṁ)",
             "\"Rebirth is ended, the spiritual journey has been completed\"",
             "\"They're freed from suffering, I say\"",
             "\"Nothing further for this place\""],
         "correct": 0,
         "expl": "A quiet structural echo linking Attadīpavagga's close back to Nakulapituvagga's opening material."},
        {"q": "How does the discourse's phrasing of relishing and greed's relationship differ from a simple cause-and-effect chain?",
         "opts": [
             "The two are treated as ending together, each condition for the other's ending, rather than one simply preceding the other",
             "There is no difference; the phrasing is a standard one-directional chain",
             "The discourse denies any relationship exists between them at all",
             "Greed is presented as entirely independent of relishing"],
         "correct": 0,
         "expl": "Two names for aspects of a single underlying process that end together."},
        {"q": "How many aggregates does this discourse's argument apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Rājagaha",
             "Devadaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Returning to the vagga's usual Sāvatthī setting after SN 22.49-50's Rājagaha dialogues."},
        {"q": "What position does this discourse hold in Attadīpavagga?",
         "opts": [
             "The first of the vagga's closing pair",
             "The vagga's opening discourse",
             "The vagga's middle discourse",
             "It does not belong to this vagga"],
         "correct": 0,
         "expl": "Opening the pair SN 22.52 will complete."},
        {"q": "What term does this discourse use for the shared ending of relishing and greed?",
         "opts": [
             "Nandirāgakkhayā, treating the two as a single condition",
             "Sakkāya, \"substantial reality\"",
             "Anusaya, \"underlying tendency\"",
             "Pariññā, \"complete understanding\""],
         "correct": 0,
         "expl": "A compound term whose ending frees the mind."},
        {"q": "What discourse comes immediately after this one, closing the vagga?",
         "opts": [
             "SN 22.52, restating the same claim with a different opening act",
             "A return to SN 22.43",
             "A discourse from a different saṃyutta",
             "SN 22.53, opening the next vagga"],
         "correct": 0,
         "expl": "Completing the vagga's closing pair."},
    ],
    marginalia=[
        ("Seeing impermanence, called right view directly", [
            "not merely compatible with it &mdash;",
            "what right view consists of, here",
        ]),
        ("A single step, not a multi-stage chain", [
            "seeing rightly, then disillusionment &mdash;",
            "more compressed than SN 22.39's fuller sequence",
        ]),
        ("Mutual ending, not one-directional cause", [
            "relishing ends greed, greed ends relishing &mdash;",
            "two aspects of one process, ending together",
        ]),
        ("An echo reaching back across four vaggas", [
            "\"well freed,\" the same words as SN 22.4 &mdash;",
            "a quiet structural link to the book's opening",
        ]),
    ],
    further=[
        '<a href="%s/sn22.51/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.50.html">SN 22.50 &middot; With Soṇa '
        "(2nd)</a> &mdash; the previous discourse, closing the "
        "vagga's Soṇa dialogue pair.",
        '<a href="sn-22.52.html">SN 22.52 &middot; The End of '
        "Relishing (2nd)</a> &mdash; the next discourse, closing the "
        "vagga and the book's first fifty discourses.",
    ],
)
# --------------------------------------------------------------------------- #
# SN 22.52 — Dutiyanandikkhayasutta
# --------------------------------------------------------------------------- #
page(
    22, 52, "Dutiyanandikkhaya", "The End of Relishing (2nd)",
    vagga="Attadīpavagga",
    meta_title="SN 22.52 — The End of Relishing (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for "
        "the Dutiyanandikkhayasutta &mdash; closing Attadīpavagga, "
        "and confirmed by the source's own untranslated colophon as "
        "closing Mūlapaṇṇāsaka, the first fifty discourses of "
        "Khandhasaṃyutta. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī"),
        ("Speakers", "The Buddha alone, addressing the assembled "
                     "mendicants"),
        ("Form", "SN 22.51's claim restated, opening with rational "
                 "application of the mind rather than simply seeing "
                 "impermanence"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "A rough counterpart may exist in the "
                              "Chinese Saṃyukta-āgama (T99), though "
                              "this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; "
                       "closes both the vagga and, confirmed by the "
                       "source's own colophon, the entire first fifty "
                       "discourses of Khandhasaṃyutta"),
    ],
    why=(
        "This discourse closes Attadīpavagga with the same mutual "
        "relishing-and-greed formula SN 22.51 stated immediately "
        "before it, but frames its opening act differently: rather "
        "than simply &ldquo;seeing&rdquo; impermanence, mendicants "
        "are instructed to &ldquo;rationally apply the mind to form&rdquo; "
        "(yoniso manasi karotha) and then truly see its impermanence "
        "&mdash; two distinct acts rather than one. What makes this "
        "discourse especially significant, though, is not translated "
        "into English at all: the source's own untranslated Pali "
        "colophon, closing with &ldquo;Mūlapaṇṇāsako samatto&rdquo; "
        "(&ldquo;the Root Fifty is complete&rdquo;), confirms in the "
        "text itself that this discourse closes not only "
        "Attadīpavagga but the entire first fifty discourses of "
        "Khandhasaṃyutta &mdash; and a further meta-uddāna names all "
        "five vaggas that make up that fifty, matching exactly the "
        "structure this project confirmed independently through "
        "SuttaCentral's own menu API before beginning Book III."
    ),
    guide=[
        ("Two acts instead of one, opening the same chain", [
            "SN 22.51 opened with a single observation &mdash; a "
            "mendicant sees that form is impermanent. This discourse "
            "instead names two distinct steps: rationally apply the "
            "mind (yoniso manasi karotha) to form, and truly see its "
            "impermanence. The rest of the chain that follows "
            "&mdash; disillusionment, the mutual ending of relishing "
            "and greed, and the mind becoming well freed &mdash; is "
            "identical in wording to SN 22.51's.",
        ]),
        ("The identical mutual-ending formula, unchanged from SN 22.51", [
            "As in SN 22.51, this discourse states the relationship "
            "between relishing and greed as fully bidirectional: when "
            "relishing ends, greed ends; when greed ends, relishing "
            "ends. When both end together, the mind is freed and is "
            "said to be well freed &mdash; the same distinctive "
            "phrasing that distinguishes this pair from the mostly "
            "one-directional chains used elsewhere in the book.",
        ]),
        ("An untranslated colophon confirming the vagga's own contents", [
            "The source's Pali (though left untranslated in Sujato's "
            "English) closes with a formal count and summary verse: "
            "&ldquo;Dasamaṁ&rdquo; (&ldquo;tenth&rdquo;), "
            "&ldquo;Attadīpavaggo pañcamo&rdquo; (&ldquo;Attadīpavagga "
            "is the fifth&rdquo;), followed by an uddāna listing all "
            "ten discourse names in verse &mdash; Attadīpa, "
            "Paṭipadā, the two Impermanence discourses, Ways of "
            "Regarding, Aggregates, the two With Soṇa discourses, and "
            "the two End of Relishing discourses &mdash; confirming "
            "precisely the ten titles this project independently "
            "verified from bilara-data before writing a single page.",
        ]),
        ("A second colophon confirming the whole first fifty", [
            "Beyond the vagga's own uddāna, the source adds a further, "
            "larger-scale colophon: &ldquo;Mūlapaṇṇāsako samatto&rdquo; "
            "(&ldquo;the Root Fifty is complete&rdquo;), followed by "
            "a meta-uddāna naming all five vaggas that make up this "
            "first fifty &mdash; Nakulapitā (Nakulapituvagga), anicca "
            "(Aniccavagga), bhāra (Bhāravagga), natumhāka "
            "(Natumhākavagga), and attadīpa (Attadīpavagga) &mdash; "
            "matching exactly the structure this project confirmed "
            "independently through SuttaCentral's own menu API at "
            "Book III's outset. The text's own internal accounting "
            "and this project's external verification agree precisely.",
        ]),
    ],
    terms=[
        ("yoniso manasi karotha",
         "&ldquo;rationally apply the mind&rdquo; &mdash; this "
         "discourse's opening act, distinct from SN 22.51's simpler "
         "\"sees that it is impermanent.\""),
        ("nandikkhayā rāgakkhayo, rāgakkhayā nandikkhayo",
         "&ldquo;when relishing ends, greed ends; when greed ends, "
         "relishing ends&rdquo; &mdash; the mutual-ending formula "
         "shared unchanged with SN 22.51."),
        ("dasamaṁ",
         "&ldquo;tenth&rdquo; &mdash; the untranslated Pali count "
         "confirming this discourse's position as Attadīpavagga's "
         "tenth and final discourse."),
        ("mūlapaṇṇāsako samatto",
         "&ldquo;the Root Fifty is complete&rdquo; &mdash; the "
         "untranslated colophon confirming this discourse closes the "
         "first fifty discourses of Khandhasaṃyutta."),
        ("vagguddāna",
         "&ldquo;vagga-summary&rdquo; &mdash; the meta-level "
         "mnemonic verse naming all five vaggas of the completed "
         "Mūlapaṇṇāsaka, confirming this project's independently "
         "verified structure."),
    ],
    text_intro=(
        "The discourse in full. Three elided repetitions (feeling, "
        "perception, and choices, each following the same chain "
        "spelled out in full for form and consciousness) are given "
        "exactly as bilara-data preserves them. The source's closing "
        "Pali colophon and double uddāna (count, vagga-summary, and "
        "Mūlapaṇṇāsaka-summary verses) are left untranslated in "
        "Sujato's English and are described above rather than quoted "
        "in this section. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "sn22.52:1.2-1.5"),
        ("p", "&sect;2", "sn22.52:1.15-1.18"),
    ],
    quiz=[
        {"q": "What two distinct acts does this discourse's opening name, instead of SN 22.51's single act of \"seeing\"?",
         "opts": [
             "Rationally applying the mind to form, and truly seeing its impermanence",
             "Reciting a formal verse, then meditating in silence",
             "Traveling to a distant monastery, then teaching there",
             "Debating another teacher, then conceding the point"],
         "correct": 0,
         "expl": "Yoniso manasi karotha, followed by samanupassatha — two steps rather than SN 22.51's one."},
        {"q": "What mutual-ending formula does this discourse share unchanged with SN 22.51?",
         "opts": [
             "When relishing ends, greed ends; when greed ends, relishing ends",
             "When form ends, feeling automatically ends too",
             "When greed increases, relishing decreases",
             "When one aggregate ends, all five end simultaneously"],
         "correct": 0,
         "expl": "The identical bidirectional phrasing distinguishing this pair from most of the book's one-directional chains."},
        {"q": "What does the discourse's untranslated Pali colophon confirm about its position?",
         "opts": [
             "That it is the tenth and final discourse of Attadīpavagga, the fifth vagga",
             "That it is the first discourse of an entirely new saṃyutta",
             "That it belongs to a different vagga than the nine discourses before it",
             "The colophon provides no positional information at all"],
         "correct": 0,
         "expl": "\"Dasamaṁ\" (tenth) and \"Attadīpavaggo pañcamo\" (Attadīpavagga is the fifth)."},
        {"q": "What larger structural claim does the source's colophon make, beyond the vagga level?",
         "opts": [
             "\"Mūlapaṇṇāsako samatto\" — the Root Fifty (Mūlapaṇṇāsaka) is complete",
             "That the entire Saṃyutta Nikāya is now complete",
             "That a new saṃyutta begins immediately after this discourse",
             "No claim beyond the vagga level is made"],
         "correct": 0,
         "expl": "Confirming this discourse closes the first fifty discourses of Khandhasaṃyutta."},
        {"q": "What does the source's meta-uddāna (vagga-summary verse) list?",
         "opts": [
             "All five vaggas making up Mūlapaṇṇāsaka: Nakulapitā, Anicca, Bhāra, Natumhāka, Attadīpa",
             "A list of every mendicant mentioned across the fifty discourses",
             "A list of every location where the fifty discourses were taught",
             "The names of the ten discourses within Attadīpavagga alone"],
         "correct": 0,
         "expl": "Matching exactly the structure this project verified independently through SuttaCentral's menu API."},
        {"q": "Is this colophon and its uddāna translated in Sujato's English translation?",
         "opts": [
             "No — it is left untranslated, present only in the Pali",
             "Yes — it is fully translated and quoted in the text section",
             "It is partially translated, with only the vagga name given",
             "The colophon does not exist in the source at all"],
         "correct": 0,
         "expl": "Described in this reading guide's prose rather than quoted in the text-block, since the translation JSON leaves it empty."},
        {"q": "How many aggregates does this discourse's chain apply to?",
         "opts": [
             "All five — form, feeling, perception, choices, and consciousness",
             "Only form",
             "Only form and consciousness",
             "Only feeling"],
         "correct": 0,
         "expl": "Feeling, perception, and choices are elided but follow the same pattern."},
        {"q": "Where is this discourse set?",
         "opts": [
             "Sāvatthī",
             "Rājagaha",
             "Devadaha",
             "Vesālī"],
         "correct": 0,
         "expl": "Continuing the same setting as SN 22.51."},
        {"q": "What agreement does this reading guide highlight between the source's own accounting and this project's prior research?",
         "opts": [
             "The text's internal colophon and this project's independent SuttaCentral API verification agree precisely on the five-vagga structure",
             "The source's colophon contradicts what SuttaCentral's API reported",
             "SuttaCentral's API was found to be entirely unreliable for this book",
             "No comparison between the two sources was made"],
         "correct": 0,
         "expl": "Both confirm the identical five vaggas making up Mūlapaṇṇāsaka."},
        {"q": "What comes immediately after this discourse, moving beyond Mūlapaṇṇāsaka?",
         "opts": [
             "SN 22.53, opening Upayavagga and Majjhimapaṇṇāsaka, the second fifty",
             "A return to SN 22.43",
             "The end of the entire Khandhasaṃyutta",
             "A discourse from an entirely different saṃyutta"],
         "correct": 0,
         "expl": "The book's own systematic coverage continues into SN22's second paṇṇāsaka."},
    ],
    marginalia=[
        ("Two acts, not one, opening the chain", [
            "rationally apply the mind, then truly see &mdash;",
            "SN 22.51 named only the seeing",
        ]),
        ("The same mutual-ending formula, unchanged", [
            "relishing and greed ending together &mdash;",
            "identical phrasing to SN 22.51's",
        ]),
        ("An untranslated colophon confirming the vagga", [
            "tenth, and the fifth vagga &mdash;",
            "matching this project's own ten confirmed titles",
        ]),
        ("A larger colophon: the first fifty complete", [
            "Mūlapaṇṇāsako samatto &mdash;",
            "five vaggas named, matching SuttaCentral's own structure",
        ]),
    ],
    further=[
        '<a href="%s/sn22.52/en/sujato" target="_blank" rel="noopener">Full '
        "Sujato translation on SuttaCentral</a> &mdash; with Pāli "
        "alongside, segment by segment."
        % SC,
        '<a href="sn-22.51.html">SN 22.51 &middot; The End of '
        "Relishing</a> &mdash; the previous discourse, the same "
        "mutual-ending formula with a simpler opening act.",
        '<a href="sn-22.43.html">SN 22.43 &middot; Be Your Own '
        "Island</a> &mdash; the vagga's opening discourse, whose "
        "namesake instruction this closing pair's own colophon now "
        "confirms as Mūlapaṇṇāsaka's final chapter.",
    ],
)
