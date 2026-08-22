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
