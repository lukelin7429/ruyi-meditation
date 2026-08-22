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
