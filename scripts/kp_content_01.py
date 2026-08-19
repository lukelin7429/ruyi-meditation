# -*- coding: utf-8 -*-
"""Khuddakapatha — Basic Passages. Nine short texts, one per page."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Khuddakapatha — Basic Passages"
# All nine Khuddakapatha texts are covered as a single flat sequence in this
# one module, so HEAD/TAIL both point back to the collection's own index --
# the Khuddakapatha is a standalone Khuddaka Nikāya collection, not chained
# to another module before or after it.
HEAD = ("./", "Khuddakapatha selections")
TAIL = ("./", "Khuddakapatha selections")
INDEX_EXTRA = []

PAGES = []


def page(num, pali, title, **kw):
    """Shared scaffolding for a single text of the Khuddakapatha."""
    d = {
        "slug": "kp-%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "kp%d" % num,
        "crumb": "Kp %d" % num,
        "number_line": "Khuddakapatha &middot; Text %d" % num,
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# Kp 1 — Saraṇattaya
# --------------------------------------------------------------------------- #
page(
    1, "Saraṇattaya", "The Three Refuges",
    meta_title="Kp 1 — The Three Refuges | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saraṇattaya, "
        "opening the Khuddakapatha — the formula of taking refuge in the Buddha, the "
        "teaching, and the Saṅgha, stated three times over. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given; this is a formula, not a discourse "
                    "delivered on a specific occasion"),
        ("Speaker", "Not the Buddha &mdash; the words are spoken by whoever takes refuge, "
                    "in the first person"),
        ("Form", "A short homage line followed by the three-refuges formula, repeated three "
                 "times in full"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The three refuges formula, in close to this exact wording, is "
                              "foundational across every Buddhist tradition; this reading "
                              "guide does not assert a specific matching text"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest and most "
                       "widely recited text in the entire collection"),
    ],
    why=(
        "The Khuddakapatha (&ldquo;Basic Passages&rdquo;) opens with the single most widely "
        "recited formula in the entire Buddhist tradition: taking refuge in the Buddha, the "
        "teaching (<em>dhamma</em>), and the community (<em>saṅgha</em>), stated a first "
        "time, then repeated word for word a second and third time. It is not a discourse "
        "the Buddha delivers; it is a formula anyone can speak, in the first person, to "
        "formally commit to the tradition."),
    guide=[
        ("The shortest text in this collection", [
            "Nine short passages make up the Khuddakapatha, and this is the first and "
            "shortest: a homage line, then the three-refuges formula stated three times over, "
            "with nothing else added."]),
        ("Not a discourse, but a formula", [
            "Unlike almost every other text in this project, this passage names no speaker, "
            "no audience, and no occasion. It is written in the first person "
            "(&ldquo;I take refuge&rdquo;), meant to be spoken by whoever recites it, not "
            "narrated as something the Buddha once said to someone else."]),
        ("Three refuges, three repetitions", [
            "The Buddha, the teaching, and the community &mdash; the three things taken "
            "refuge in &mdash; are stated identically all three times; only the ordinal "
            "marker changes (&lsquo;for the second time&rsquo;, &lsquo;for the third "
            "time&rsquo;). Repeating a formal declaration three times, rather than once, is "
            "itself a widespread convention for making a commitment binding in this "
            "tradition, not unique to this text."]),
        ("A homage line older than the formula itself", [
            "The opening line, &lsquo;Homage to him, the blessed one, the perfected one, the "
            "fully awakened Buddha!&rsquo;, is not part of the refuges formula proper; it is "
            "a separate, extremely widely used homage (<em>namotassa</em>) that traditionally "
            "opens a great deal of recited and chanted material across the canon, not just "
            "this passage."]),
        ("Nine passages, building outward", [
            "The Khuddakapatha's nine texts move from this shortest possible formula toward "
            "progressively longer material: precepts, a list of the body's parts, a "
            "children's catechism, and several full verse suttas closing the collection."]),
    ],
    terms=[
        ("saraṇa",
         "&ldquo;refuge&rdquo; &mdash; the act this text's title names, taken here in the "
         "Buddha, the teaching, and the community."),
        ("Buddha, Dhamma, Saṅgha",
         "the &ldquo;three jewels&rdquo; (<em>tiratana</em>) &mdash; the awakened teacher, "
         "his teaching, and the community that preserves and practices it."),
        ("namotassa",
         "the opening homage line, &lsquo;Homage to him...&rsquo; &mdash; a separate, very "
         "widely used formula distinct from the refuges themselves."),
        ("dutiyampi, tatiyampi",
         "&ldquo;for the second time&rdquo;, &ldquo;for the third time&rdquo; &mdash; the "
         "only words that change across the formula's three repetitions."),
        ("Khuddakapatha",
         "&ldquo;Basic Passages&rdquo; or &ldquo;Short Passages&rdquo; &mdash; this "
         "collection's own title, and the first of the Khuddaka Nikāya's texts covered in "
         "this project."),
    ],
    text_intro=(
        "The text in full: the homage line, then the three refuges, stated three times over. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "kp1:1.1-1.1"),
        ("p", "&sect;2", "kp1:2.1-2.3"),
        ("p", "&sect;3", "kp1:3.1-3.3"),
        ("p", "&sect;4", "kp1:4.1-4.3"),
    ],
    quiz=[
        {"q": "What three things does this text take refuge in?",
         "opts": [
             "The Buddha, the teaching (Dhamma), and the community (Saṅgha)",
             "The four noble truths",
             "The five aggregates",
             "The eightfold path"],
         "correct": 0,
         "expl": "The 'three jewels' (tiratana)."},
        {"q": "How many times is the refuges formula stated in this text?",
         "opts": [
             "Three times, word for word identical except for the ordinal marker",
             "Once only",
             "Five times",
             "The number varies depending on the reciter"],
         "correct": 0,
         "expl": "'For the second time...', 'for the third time...'"},
        {"q": "Who is the speaker of this text?",
         "opts": [
             "Not the Buddha — whoever recites it, speaking in the first person",
             "The Buddha, addressing a specific audience",
             "A deity",
             "An unnamed narrator describing a historical event"],
         "correct": 0,
         "expl": "Unlike most texts in this project, no narrative speaker or setting is given."},
        {"q": "What is the opening homage line, and is it part of the refuges formula itself?",
         "opts": [
             "'Homage to him...' (namotassa) — a separate, widely used formula, not part of the refuges proper",
             "It is the refuges formula's own first line",
             "It is a later scribal addition not found in any edition",
             "It names the specific location where this text was first recited"],
         "correct": 0,
         "expl": "Namotassa traditionally opens a great deal of recited material, not just this text."},
        {"q": "What collection does this text open?",
         "opts": [
             "The Khuddakapatha, 'Basic Passages'",
             "The Dhammapada",
             "The Udāna",
             "The Sutta Nipāta"],
         "correct": 0,
         "expl": "The first and shortest of this collection's nine texts."},
        {"q": "What does 'saraṇa' mean?",
         "opts": [
             "'Refuge'",
             "'Precept'",
             "'Homage'",
             "'Perfection'"],
         "correct": 0,
         "expl": "The act this text's title, Saraṇattaya ('the three refuges'), names."},
        {"q": "What words change across the formula's three repetitions?",
         "opts": [
             "Only the ordinal marker ('for the second/third time'); everything else is identical",
             "The names of the three refuges themselves change each time",
             "The entire formula is rewritten each time",
             "Nothing changes at all between repetitions"],
         "correct": 0,
         "expl": "Dutiyampi, tatiyampi — the only variation."},
        {"q": "What does the Khuddakapatha do after this opening text?",
         "opts": [
             "Moves toward progressively longer material: precepts, a body-parts list, a children's catechism, and full verse suttas",
             "Repeats this same refuges formula for all nine texts",
             "Immediately shifts to narrative prose about the Buddha's life",
             "Ends; this is the collection's only text"],
         "correct": 0,
         "expl": "Nine texts total, building outward from this shortest formula."},
        {"q": "Why might a formal declaration be repeated three times rather than stated once?",
         "opts": [
             "A widespread convention in this tradition for making a commitment binding",
             "A scribal error duplicating the same line",
             "Because three different people are speaking, one repetition each",
             "No reason is given or implied anywhere"],
         "correct": 0,
         "expl": "Not unique to this text; a broader convention across the tradition."},
        {"q": "What is this text's overall form?",
         "opts": [
             "A short homage line followed by the three-refuges formula, repeated three times in full",
             "A long narrative dialogue",
             "A single unrepeated verse",
             "A list with no formulaic repetition"],
         "correct": 0,
         "expl": "The shortest and most widely recited text in this entire collection."},
    ],
    marginalia=[
        ("The three jewels", [
            "Buddha, Dhamma, Saṅgha",
            "&mdash; taken as refuge",
        ]),
        ("Repeated three times", [
            "identical wording,",
            "only the ordinal changes",
        ]),
        ("A formula, not a story", [
            "first person, no narrator,",
            "no setting or audience named",
        ]),
        ("The collection's shortest text", [
            "opening nine passages",
            "that build progressively longer",
        ]),
    ],
    further=[
        '<a href="%s/kp1/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another Khuddaka Nikāya collection '
        "already complete on this site.",
        '<a href="../udana/">Udāna</a> &mdash; another complete Khuddaka Nikāya '
        "collection, also verse-and-prose exclamations rather than dialogues.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 2 — Dasasikkhāpada
# --------------------------------------------------------------------------- #
page(
    2, "Dasasikkhāpada", "The Ten Precepts",
    meta_title="Kp 2 — The Ten Precepts | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dasasikkhāpada, "
        "the Khuddakapatha's ten training precepts traditionally undertaken by novices, "
        "building on the five lay precepts. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given; like Kp 1, this is a formula rather than "
                    "a discourse delivered on a specific occasion"),
        ("Speaker", "Not the Buddha &mdash; whoever undertakes the precepts, in the first "
                    "person"),
        ("Form", "Ten near-identical declarations, one per precept, each following the same "
                 "&lsquo;I undertake the precept to refrain from...&rsquo; pattern"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Comparable ten-item novice precept sets appear across other "
                              "Vinaya traditions; this reading guide does not assert one "
                              "specific matching text"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short formulaic list, "
                       "no narrative or doctrine to unpack"),
    ],
    why=(
        "This text sets out the ten training precepts (<em>dasasikkhāpada</em>) "
        "traditionally undertaken by novices entering the monastic life. It builds directly "
        "on the five precepts kept by lay Buddhists, then adds five more restrictions that "
        "mark the shift from a layperson's ethics to a renunciant's discipline &mdash; in the "
        "same first-person declaration format as the Three Refuges immediately before it."),
    guide=[
        ("Ten declarations, one pattern", [
            "Each of the ten lines follows the identical grammar of Kp 1's refuges formula: "
            "&lsquo;I undertake the precept to refrain from...&rsquo;, with only the object "
            "of restraint changing from line to line."]),
        ("Built on the five lay precepts", [
            "The first four items &mdash; killing, stealing, sexual activity, lying &mdash; "
            "match the first four of the five precepts (<em>pañcasīla</em>) that lay "
            "Buddhists keep. But the third item here is worded as full abstinence from "
            "sexual activity, not the layperson's narrower vow against sexual misconduct "
            "&mdash; the first sign that this is a renunciant's list, not a householder's."]),
        ("Five more restrictions added", [
            "The fifth item, avoiding intoxicants, still matches the fifth lay precept. But "
            "the text does not stop there: it adds restrictions on eating at the wrong time, "
            "on entertainment, on personal adornment, on luxurious beds, and on handling gold "
            "and money &mdash; five further items lay Buddhists do not undertake."]),
        ("Between the five precepts and this list", [
            "On observance days, lay Buddhists sometimes undertake an eight-precept version "
            "drawn from this same set, which merges the entertainment and adornment items "
            "into one and stops there, leaving out the tenth item about money entirely. This "
            "ten-item list is the fuller, novice-level version."]),
        ("What follows in the collection", [
            "After two formulas &mdash; refuges, then precepts &mdash; the Khuddakapatha's "
            "third text turns from ethical undertakings to a meditation subject: a list of "
            "the body's thirty-two parts."]),
    ],
    terms=[
        ("sikkhāpada",
         "&ldquo;training precept&rdquo; &mdash; literally a &ldquo;foot&rdquo; or "
         "&ldquo;step&rdquo; of training; each of the ten items in this formula is one."),
        ("dasasikkhāpada",
         "&ldquo;the ten training precepts&rdquo; &mdash; this text's own title, "
         "traditionally undertaken by novices at ordination."),
        ("pañcasīla",
         "the five precepts kept by lay Buddhists &mdash; the first four items of this "
         "text's ten map directly onto them, with the fifth also shared."),
        ("sāmaṇera, sāmaṇerī",
         "novice monk, novice nun &mdash; those who traditionally undertake this exact "
         "ten-item set upon entering the monastic community."),
        ("uposatha",
         "the observance day on which lay Buddhists may additionally undertake an "
         "eight-precept version drawn from this same list."),
    ],
    text_intro=(
        "The text in full: ten declarations, one per precept. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "kp2:1.1-1.1"),
        ("p", "&sect;2", "kp2:2.1-2.1"),
        ("p", "&sect;3", "kp2:3.1-3.1"),
        ("p", "&sect;4", "kp2:4.1-4.1"),
        ("p", "&sect;5", "kp2:5.1-5.1"),
        ("p", "&sect;6", "kp2:6.1-6.1"),
        ("p", "&sect;7", "kp2:7.1-7.1"),
        ("p", "&sect;8", "kp2:8.1-8.1"),
        ("p", "&sect;9", "kp2:9.1-9.1"),
        ("p", "&sect;10", "kp2:10.1-10.1"),
    ],
    quiz=[
        {"q": "What do all ten declarations in this text have in common?",
         "opts": [
             "They differ in some grammatical way each time",
             "They all follow the identical pattern 'I undertake the precept to refrain from...'",
             "Each is phrased completely differently from the others",
             "Only the first five share a common pattern"],
         "correct": 1,
         "expl": "Only the object of restraint changes from line to line."},
        {"q": "Which of this text's ten items also appear among the five lay precepts (pañcasīla)?",
         "opts": [
             "None of them",
             "Only the first item",
             "The first five, though the third is worded more strictly here",
             "All ten"],
         "correct": 2,
         "expl": "Killing, stealing, sexual activity, lying, and intoxicants — the first five."},
        {"q": "How does this text's third precept differ from the lay precept against sexual misconduct?",
         "opts": [
             "It is identical in wording",
             "It calls for full abstinence from sexual activity, not just avoiding misconduct",
             "It is left out of this text entirely",
             "It applies only to married laypeople"],
         "correct": 1,
         "expl": "A sign that this is a renunciant's list, not a householder's."},
        {"q": "What five items does this text add beyond the five lay precepts?",
         "opts": [
             "Silence, fasting, poverty, solitude, and celibacy",
             "Wrong-time eating, entertainment, adornment, luxurious beds, and handling money",
             "Five additional prohibitions on speech",
             "Nothing is added; the list stops at five"],
         "correct": 1,
         "expl": "These five mark the shift from lay ethics to renunciant discipline."},
        {"q": "Who traditionally undertakes this exact ten-item set?",
         "opts": [
             "Lay Buddhists on any ordinary day",
             "Novices (sāmaṇera/sāmaṇerī) entering the monastic community",
             "Only fully ordained monks, never novices",
             "Deities, according to this text's narrative frame"],
         "correct": 1,
         "expl": "At ordination into novice life."},
        {"q": "What is the eight-precept version taken by lay Buddhists on observance days?",
         "opts": [
             "An entirely different, unrelated list",
             "A version that merges two of this text's items and stops before the tenth",
             "The exact same ten items under a different name",
             "A version with only the first three items"],
         "correct": 1,
         "expl": "Merges the entertainment and adornment items, and omits the money item."},
        {"q": "What does 'sikkhāpada' mean?",
         "opts": [
             "'Meditation object'",
             "'Training precept', literally a 'step' of training",
             "'Refuge'",
             "'Ordination ceremony'"],
         "correct": 1,
         "expl": "Each of the ten items in this formula is one sikkhāpada."},
        {"q": "What text immediately precedes this one in the Khuddakapatha?",
         "opts": [
             "The Boy's Questions",
             "The Three Refuges",
             "Blessings",
             "The Thirty-Two Parts of the Body"],
         "correct": 1,
         "expl": "Kp 1, in the same first-person declaration format."},
        {"q": "What comes right after this text in the Khuddakapatha?",
         "opts": [
             "A list of the body's thirty-two parts, as a meditation subject",
             "A repeat of the same ten precepts",
             "A narrative discourse with a named audience",
             "The collection ends here"],
         "correct": 0,
         "expl": "The third text shifts from ethical undertakings to a meditation subject."},
        {"q": "What is this text's overall form?",
         "opts": [
             "A long narrative dialogue between the Buddha and a deity",
             "Ten near-identical first-person declarations, one per precept",
             "A single unrepeated verse",
             "A dialogue in question-and-answer format"],
         "correct": 1,
         "expl": "Same grammar as Kp 1, extended to ten items instead of one formula repeated three times."},
    ],
    marginalia=[
        ("Ten declarations", [
            "same formula each time,",
            "only the object changes",
        ]),
        ("Builds on the five", [
            "first four match",
            "the lay precepts exactly",
        ]),
        ("Five more added", [
            "food, entertainment,",
            "adornment, beds, money",
        ]),
        ("A novice's undertaking", [
            "traditionally recited",
            "at ordination",
        ]),
    ],
    further=[
        '<a href="%s/kp2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="kp-1.html">Kp 1 &mdash; The Three Refuges</a> &mdash; the formula this '
        "text's declaration format is drawn directly from.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 3 — Dvattiṁsākāra
# --------------------------------------------------------------------------- #
page(
    3, "Dvattiṁsākāra", "The Thirty-Two Parts of the Body",
    meta_title="Kp 3 — The Thirty-Two Parts of the Body | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dvattiṁsākāra, "
        "the Khuddakapatha's list of the body's thirty-two parts — a classic meditation "
        "subject shared with the Satipatthana Sutta. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given; like Kp 1&ndash;2, this is a formula "
                    "rather than a discourse delivered on a specific occasion"),
        ("Speaker", "No speaker is named; the list is presented directly, in quotation marks, "
                    "as material to be recited or contemplated"),
        ("Form", "A single sentence: thirty-two body parts named in one continuous list"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "The same list, in the same or a very similar order, recurs "
                              "widely across early Buddhist meditation material; this "
                              "reading guide does not assert one specific matching text"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a plain list, but the "
                       "meditation practice it supports takes real application to unpack"),
    ],
    why=(
        "This text is a single list: the thirty-two parts traditionally enumerated in "
        "&ldquo;mindfulness of the body&rdquo; meditation, the practice of mentally "
        "reviewing the body part by part to loosen an unreflective attachment to it. The "
        "same list, essentially unchanged, is also embedded inside the much longer "
        "Satipatthana Sutta &mdash; this short text is that shared list on its own, without "
        "the surrounding instructions."),
    guide=[
        ("One list, no frame", [
            "Unlike Kp 1 and Kp 2, this text has no declaration format and no repeated "
            "grammar &mdash; it is a single sentence in quotation marks, naming thirty-two "
            "parts of the body from head hair down to urine, in one continuous list."]),
        ("A meditation subject, not just an anatomy list", [
            "This list is the basis of a specific meditation practice, sometimes called "
            "<em>paṭikūlamanasikāra</em> (&ldquo;attention to repulsiveness&rdquo;) or folded "
            "into the broader <em>kāyagatāsati</em> (&ldquo;mindfulness occupied with the "
            "body&rdquo;). The point is not morbidity for its own sake, but loosening an "
            "unreflective identification with the body by examining it in unglamorous "
            "physical detail."]),
        ("Shared with the Satipatthana Sutta", [
            "This exact list, in close to this exact wording, is embedded within the body "
            "section of the Satipatthana Sutta (the Buddha's major discourse on the four "
            "establishments of mindfulness), where it appears as one contemplation among "
            "several. Here it stands alone, without that surrounding instructional frame."]),
        ("Thirty-one parts, or thirty-two?", [
            "Some versions and discussions of this list count only thirty-one parts, with "
            "the brain absent or folded into an existing item; this text's title and count "
            "both specify thirty-two, brain included as its own item near the end of the "
            "list."]),
        ("From precepts to meditation", [
            "The Khuddakapatha's first three texts move from a refuge formula, to an ethical "
            "undertaking, to a meditation subject &mdash; before the fourth text shifts again, "
            "to a catechism teaching numbered doctrinal lists."]),
    ],
    terms=[
        ("dvattiṁsākāra",
         "&ldquo;thirty-two parts&rdquo; or &ldquo;thirty-two aspects&rdquo; &mdash; this "
         "text's own title, and the name commonly used for the list itself."),
        ("kāyagatāsati",
         "&ldquo;mindfulness occupied with the body&rdquo; &mdash; the broader meditation "
         "category this list of body parts is a central component of."),
        ("paṭikūlamanasikāra",
         "&ldquo;attention to repulsiveness&rdquo; &mdash; a name sometimes used for this "
         "specific practice of reviewing the body part by part."),
        ("Satipatthana Sutta",
         "the Buddha's major discourse on the four establishments of mindfulness, which "
         "embeds this same list of body parts within its body-contemplation section."),
        ("matthaluṅga",
         "&ldquo;brain&rdquo; &mdash; the item some earlier or shorter versions of this list "
         "omit; this text's count of thirty-two includes it."),
    ],
    text_intro=(
        "The text in full: one continuous list of thirty-two body parts. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "kp3:1.1-1.1"),
    ],
    quiz=[
        {"q": "What is this text, in form?",
         "opts": [
             "A dialogue between the Buddha and a questioner",
             "A single sentence listing thirty-two parts of the body",
             "A repeated three-part declaration",
             "A set of ten formulaic undertakings"],
         "correct": 1,
         "expl": "From head hair down to urine, in one continuous list."},
        {"q": "What meditation practice is this list the basis for?",
         "opts": [
             "Loving-kindness meditation directed at all beings",
             "Mindfulness of the body, reviewing it part by part",
             "Concentration on the breath alone",
             "Recollection of past lives"],
         "correct": 1,
         "expl": "Sometimes called paṭikūlamanasikāra or folded into kāyagatāsati."},
        {"q": "What is the purpose of reviewing the body in this much physical detail?",
         "opts": [
             "Purely medical or anatomical instruction",
             "Loosening an unreflective attachment to the body, not morbidity for its own sake",
             "To frighten the listener",
             "No purpose is given anywhere in the tradition"],
         "correct": 1,
         "expl": "The point is a shift in how the body is held in attention, not gruesomeness."},
        {"q": "Where else does this same list of body parts appear?",
         "opts": [
             "Nowhere else in the canon",
             "Embedded within the Satipatthana Sutta's body-contemplation section",
             "Only in later commentarial literature, not in any sutta",
             "In the Three Refuges formula"],
         "correct": 1,
         "expl": "There it appears as one contemplation among several, with a surrounding instructional frame this text lacks."},
        {"q": "How many parts does this text's list name, and what item marks it as the fuller version?",
         "opts": [
             "Thirty-one parts, with the brain omitted",
             "Thirty-two parts, with the brain included as its own item",
             "Twenty parts, organs only",
             "An unspecified number"],
         "correct": 1,
         "expl": "Some shorter versions of the list count only thirty-one, folding out or omitting the brain."},
        {"q": "Is a speaker named for this text?",
         "opts": [
             "Yes, the Buddha addresses a specific named audience",
             "No — the list is presented directly, in quotation marks, without a narrative speaker",
             "Yes, a deity speaks the entire list",
             "Yes, the text names the reciter explicitly"],
         "correct": 1,
         "expl": "Like Kp 1 and Kp 2, no narrative frame is given."},
        {"q": "What does 'kāyagatāsati' mean?",
         "opts": [
             "'Refuge in the body'",
             "'Mindfulness occupied with the body' — the broader category this practice belongs to",
             "'Thirty-two precepts'",
             "'Repulsion toward speech'"],
         "correct": 1,
         "expl": "This list of body parts is a central component of that broader practice."},
        {"q": "What are the first few items named in this text's list?",
         "opts": [
             "Heart, lungs, liver, kidneys",
             "Head hair, body hair, nails, teeth, skin",
             "Blood, sweat, tears, saliva",
             "Bones, bone marrow, brain"],
         "correct": 1,
         "expl": "The list opens from the outside of the body inward."},
        {"q": "What text in the Khuddakapatha comes right before this one?",
         "opts": [
             "The Ten Precepts",
             "Blessings",
             "The Boy's Questions",
             "The Discourse on Love"],
         "correct": 0,
         "expl": "Kp 2, moving here from an ethical undertaking to a meditation subject."},
        {"q": "What does this text's title, 'dvattiṁsākāra', mean?",
         "opts": [
             "'Thirty-two parts' or 'thirty-two aspects'",
             "'Body of refuge'",
             "'Ten precepts'",
             "'Boy's questions'"],
         "correct": 0,
         "expl": "The list itself is commonly known by this name."},
    ],
    marginalia=[
        ("One sentence", [
            "thirty-two parts named",
            "in a single continuous list",
        ]),
        ("A meditation subject", [
            "reviewed part by part",
            "to loosen attachment"
        ]),
        ("Shared with a major sutta", [
            "embedded within",
            "the Satipatthana Sutta"
        ]),
        ("From precepts to practice", [
            "the collection's third text,",
            "its first meditation subject",
        ]),
    ],
    further=[
        '<a href="%s/kp3/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="kp-2.html">Kp 2 &mdash; The Ten Precepts</a> &mdash; the text immediately '
        "before this one in the Khuddakapatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 4 — Kumārapañha
# --------------------------------------------------------------------------- #
page(
    4, "Kumārapañha", "The Boy&rsquo;s Questions",
    meta_title="Kp 4 — The Boy's Questions | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Kumārapañha, "
        "the Khuddakapatha's catechism teaching ten core doctrinal lists through a "
        "question-and-answer numbered pattern. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given in the text itself; commentarial "
                    "tradition associates it with teaching a young novice"),
        ("Speaker", "Neither questioner nor answerer is named within the text"),
        ("Form", "Ten question-and-answer pairs, numbered one through ten, each pairing "
                 "&lsquo;What is the [number]?&rsquo; with a short doctrinal answer"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "Numbered doctrinal catechisms of this kind are widespread "
                              "teaching devices across Buddhist traditions; this reading "
                              "guide does not assert one specific matching text"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the ten answers "
                       "compress a wide span of core doctrine into single phrases"),
    ],
    why=(
        "This text is a catechism: ten questions, &lsquo;What is the one?&rsquo; through "
        "&lsquo;What is the ten?&rsquo;, each answered with a short numbered doctrinal list "
        "&mdash; from &lsquo;all sentient beings are sustained by food&rsquo; at one, up to "
        "the ten factors of a person called &lsquo;perfected&rsquo; at ten. Later "
        "commentarial tradition holds it was taught by the Buddha to his son and novice, "
        "Rāhula, as a way of compressing a wide span of doctrine into a form a beginner "
        "could memorize &mdash; though the text as it stands here names no speaker or "
        "audience."),
    guide=[
        ("A numbered catechism", [
            "Each of the ten items follows the same pattern: a question naming a number, "
            "then a short answer naming that many things. The pattern itself, not any "
            "narrative, is what holds the text together."]),
        ("From food to the noble eightfold path", [
            "The ten answers move through some of the tradition's most central teaching "
            "lists: beings sustained by food (one), name and form (two), the three "
            "feelings (three), the four noble truths (four), the five grasping aggregates "
            "(five), the six interior sense fields (six), the seven awakening factors "
            "(seven), and the noble eightfold path (eight)."]),
        ("Nine and ten close the list", [
            "The ninth answer, the nine abodes of sentient beings, is a less commonly "
            "encountered classification than the items before it. The tenth answer names "
            "not a list of things but a person: one endowed with ten factors is called "
            "&lsquo;perfected&rsquo; &mdash; the ten factors traditionally understood as the "
            "eightfold path completed, plus right knowledge and right liberation."]),
        ("A teaching device, not a doctrinal exposition", [
            "None of the ten answers is explained or expanded within this text; each is "
            "stated as a compressed label, assuming the questioner already knows &mdash; or "
            "is being pointed toward &mdash; the fuller teaching each number stands for."]),
        ("Attributed to Rāhula by later tradition", [
            "The commentarial association of this catechism with Rāhula, the Buddha's son "
            "and one of the tradition's most celebrated novices, fits its form: a numbered "
            "list well suited to memorization by someone new to the teaching, rather than a "
            "discourse addressed to an already advanced audience."]),
    ],
    terms=[
        ("kumārapañha",
         "&ldquo;the boy's questions&rdquo; &mdash; this text's own title."),
        ("āhāra",
         "&ldquo;food&rdquo; or &ldquo;nutriment&rdquo; &mdash; the answer given to "
         "&lsquo;what is the one?&rsquo;, all sentient beings said to be sustained by it."),
        ("nāmarūpa",
         "&ldquo;name and form&rdquo; &mdash; the answer to &lsquo;what is the two?&rsquo;, "
         "also a key link in the chain of dependent origination."),
        ("pañcupādānakkhandhā",
         "&ldquo;the five grasping aggregates&rdquo; &mdash; the answer to &lsquo;what is "
         "the five?&rsquo;, a core analysis of what a person is made of."),
        ("asekha",
         "&ldquo;beyond training&rdquo;, i.e. perfected &mdash; the tenth answer describes "
         "such a person as endowed with ten factors, traditionally the eightfold path plus "
         "right knowledge and right liberation."),
    ],
    text_intro=(
        "The text in full: ten question-and-answer pairs, numbered one through ten. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "kp4:1.1-1.2"),
        ("p", "&sect;2", "kp4:2.1-2.2"),
        ("p", "&sect;3", "kp4:3.1-3.2"),
        ("p", "&sect;4", "kp4:4.1-4.2"),
        ("p", "&sect;5", "kp4:5.1-5.2"),
        ("p", "&sect;6", "kp4:6.1-6.2"),
        ("p", "&sect;7", "kp4:7.1-7.2"),
        ("p", "&sect;8", "kp4:8.1-8.2"),
        ("p", "&sect;9", "kp4:9.1-9.2"),
        ("p", "&sect;10", "kp4:10.1-10.2"),
    ],
    quiz=[
        {"q": "What is this text's overall form?",
         "opts": [
             "A dialogue between the Buddha and a deity",
             "Ten question-and-answer pairs, numbered one through ten",
             "A single repeated three-part formula",
             "A narrative account of a specific event"],
         "correct": 1,
         "expl": "'What is the one?' through 'What is the ten?', each with a short answer."},
        {"q": "What is the answer given to 'What is the one?'",
         "opts": [
             "The four noble truths",
             "All sentient beings are sustained by food",
             "Name and form",
             "The noble eightfold path"],
         "correct": 1,
         "expl": "Āhāra, 'food' or 'nutriment'."},
        {"q": "What is the answer given to 'What is the four?'",
         "opts": [
             "The four noble truths",
             "The five grasping aggregates",
             "Name and form",
             "The seven awakening factors"],
         "correct": 0,
         "expl": "Cattāri ariyasaccāni."},
        {"q": "What is the answer given to 'What is the eight?'",
         "opts": [
             "The nine abodes of sentient beings",
             "The noble eightfold path",
             "The six interior sense fields",
             "Three feelings"],
         "correct": 1,
         "expl": "Ariyo aṭṭhaṅgiko maggo."},
        {"q": "What does the tenth answer describe, unlike the previous nine?",
         "opts": [
             "A list of things, like all the answers before it",
             "A person — one endowed with ten factors, called 'perfected'",
             "A place",
             "A number with no answer given"],
         "correct": 1,
         "expl": "The ten factors traditionally understood as the eightfold path plus right knowledge and right liberation."},
        {"q": "What does later commentarial tradition associate this text with?",
         "opts": [
             "A discourse to a large assembly of monks",
             "Teaching Rāhula, the Buddha's son and a celebrated novice",
             "A dispute between two rival teachers",
             "No association is ever made"],
         "correct": 1,
         "expl": "Though the text as it stands here names no speaker or audience."},
        {"q": "Are the ten answers explained or expanded within this text?",
         "opts": [
             "Yes, each is given a full paragraph of explanation",
             "No — each is stated as a compressed label, not expanded",
             "Only the first and last are explained",
             "The explanations exist but are in verse form"],
         "correct": 1,
         "expl": "The text assumes the fuller teaching behind each number is already known or will be taught separately."},
        {"q": "What is the answer given to 'What is the two?'",
         "opts": [
             "Name and form",
             "Three feelings",
             "Six interior sense fields",
             "Nine abodes of sentient beings"],
         "correct": 0,
         "expl": "Nāmarūpa, also a link in dependent origination."},
        {"q": "What text in the Khuddakapatha comes right before this one?",
         "opts": [
             "Blessings",
             "The Thirty-Two Parts of the Body",
             "The Discourse on Love",
             "Gems"],
         "correct": 1,
         "expl": "Kp 3, the body-parts meditation list."},
        {"q": "What kind of text is this, compared to the narrative discourses common elsewhere in the canon?",
         "opts": [
             "A teaching device built for memorization, not a doctrinal exposition",
             "A biographical account of the Buddha's early life",
             "A legal code for the monastic community",
             "A philosophical debate with a rival school"],
         "correct": 0,
         "expl": "A numbered list well suited to memorization by a beginner."},
    ],
    marginalia=[
        ("Ten questions", [
            "'What is the one?'",
            "through 'What is the ten?'",
        ]),
        ("Core lists compressed", [
            "food, feelings, truths,",
            "aggregates, the path",
        ]),
        ("The tenth names a person", [
            "not a list, but",
            "one called 'perfected'",
        ]),
        ("Associated with Rāhula", [
            "by later commentary,",
            "not by the text itself",
        ]),
    ],
    further=[
        '<a href="%s/kp4/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="kp-3.html">Kp 3 &mdash; The Thirty-Two Parts of the Body</a> &mdash; the '
        "text immediately before this one in the Khuddakapatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 5 — Blessings (Maṅgala Sutta)
# --------------------------------------------------------------------------- #
page(
    5, "Maṅgala Sutta", "Blessings",
    meta_title="Kp 5 — Blessings | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Maṅgala Sutta, "
        "the Khuddakapatha's discourse on the highest blessing — a progression from "
        "ordinary social virtues to full awakening. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Jeta's Grove near Sāvatthī, late at night"),
        ("Speaker", "A glorious deity asks the question; the Buddha answers, in verse"),
        ("Form", "A one-verse question followed by eleven verses of answer, each closing "
                 "with the refrain &lsquo;this is the highest blessing&rsquo;"),
        ("Length", "3&ndash;4 minutes to read"),
        ("Northern parallel", "No specific matching text in the Chinese Āgamas is asserted "
                              "in this reading guide"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple language, but the "
                       "list moves quickly from ordinary virtue to advanced attainment"),
    ],
    why=(
        "A deity asks the Buddha to name the highest blessing, and the Buddha answers with "
        "a list that moves, verse by verse, from ordinary social virtues &mdash; avoiding "
        "bad company, caring for parents, honest work &mdash; up through generosity and "
        "self-restraint, to seeing the noble truths and a mind untouched by the world's "
        "ups and downs. One of the most widely known and recited texts in the entire "
        "tradition, it also appears, in close to this exact wording, as its own text within "
        "the Sutta Nipāta."),
    guide=[
        ("A deity's question, a long answer", [
            "The setting is brief: late one night at Jeta's Grove, a glorious deity "
            "approaches the Buddha and asks, in verse, what the highest blessing is. Eleven "
            "verses of answer follow, each ending with the same refrain: &lsquo;this is the "
            "highest blessing&rsquo;."]),
        ("A progression, not a list of equals", [
            "The blessings named do not sit at the same level. The sequence opens with "
            "avoiding bad company and honoring the wise, moves through education, family "
            "care, generosity, and self-discipline, and only in its final verses reaches "
            "seeing the noble truths and realizing extinguishment &mdash; the sequence "
            "itself tracks a path from ordinary virtue toward full awakening."]),
        ("A mind untouched by the world", [
            "The second-to-last verse describes someone &lsquo;touched by worldly "
            "conditions&rsquo; whose &lsquo;mind does not tremble&rsquo;, "
            "&lsquo;sorrowless, stainless, secure&rsquo; &mdash; a description of "
            "equanimity in the face of gain and loss, praise and blame, rather than a "
            "further item to acquire."]),
        ("Also a text of the Sutta Nipāta", [
            "This same discourse, with only small wording differences between the two "
            "translations, appears again as its own numbered text within the Sutta Nipāta "
            "&mdash; one of a small number of texts included, essentially unchanged, under "
            "two different collection headings in the Pali canon."]),
        ("The Khuddakapatha's longest text so far", [
            "After four short formulas and lists, this is the first full narrative "
            "discourse in the collection &mdash; with a setting, a speaker, an audience, "
            "and an extended verse answer, rather than a formula recited without a frame."]),
    ],
    terms=[
        ("maṅgala",
         "&ldquo;blessing&rdquo; or &ldquo;auspicious sign&rdquo; &mdash; the word this "
         "text's question and refrain both turn on."),
        ("Jeta's Grove",
         "the monastery near Sāvatthī, donated by Anāthapiṇḍika, where a great many "
         "discourses in the canon are set, including this one."),
        ("devatā",
         "&ldquo;deity&rdquo; &mdash; the unnamed &lsquo;glorious deity&rsquo; who asks "
         "the Buddha this text's opening question."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; named directly in the tenth verse as one of "
         "the highest blessings, alongside seeing the noble truths."),
        ("Sutta Nipāta",
         "the other Khuddaka Nikāya collection, already complete on this site, that "
         "includes this same discourse under its own numbering."),
    ],
    text_intro=(
        "The text in full: the setting, the deity's question, and the Buddha's eleven "
        "verses of answer. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting"),
        ("p", "&sect;1", "kp5:1.1-1.4"),
        ("h3", "The deity's question"),
        ("p", "&sect;2", "kp5:2.1-2.4"),
        ("h3", "The Buddha's answer"),
        ("p", "&sect;3", "kp5:3.1-3.4"),
        ("p", "&sect;4", "kp5:4.1-4.4"),
        ("p", "&sect;5", "kp5:5.1-5.4"),
        ("p", "&sect;6", "kp5:6.1-6.4"),
        ("p", "&sect;7", "kp5:7.1-7.4"),
        ("p", "&sect;8", "kp5:8.1-8.4"),
        ("p", "&sect;9", "kp5:9.1-9.4"),
        ("p", "&sect;10", "kp5:10.1-10.4"),
        ("p", "&sect;11", "kp5:11.1-11.4"),
        ("p", "&sect;12", "kp5:12.1-12.4"),
        ("p", "&sect;13", "kp5:13.1-13.4"),
    ],
    quiz=[
        {"q": "Who asks the Buddha the opening question in this text?",
         "opts": [
             "A group of mendicants",
             "A glorious deity, late at night at Jeta's Grove",
             "King Pasenadi",
             "Ānanda"],
         "correct": 1,
         "expl": "The deity lights up the entire grove and asks about the highest blessing."},
        {"q": "What refrain closes each of the Buddha's eleven answer verses?",
         "opts": [
             "'May you be well'",
             "'This is the highest blessing'",
             "'Thus have I heard'",
             "'This is the noble truth'"],
         "correct": 1,
         "expl": "The same closing line across all eleven verses."},
        {"q": "What kind of sequence do the blessings named form?",
         "opts": [
             "A random, unordered list",
             "A progression from ordinary social virtue toward full awakening",
             "A strict ranking with no thematic movement",
             "A repetition of the same blessing eleven times"],
         "correct": 1,
         "expl": "Opening with avoiding bad company, closing with seeing the noble truths and realizing extinguishment."},
        {"q": "What does the second-to-last verse describe?",
         "opts": [
             "A wealthy person's daily routine",
             "A mind untouched by worldly conditions — sorrowless, stainless, secure",
             "The geography of Jeta's Grove",
             "A dispute between two deities"],
         "correct": 1,
         "expl": "Equanimity in the face of gain and loss, praise and blame."},
        {"q": "Where else does this same discourse appear in the Pali canon?",
         "opts": [
             "Nowhere else — this is its only appearance",
             "Again, in close to this exact wording, within the Sutta Nipāta",
             "Only in later commentarial literature",
             "In the Vinaya, as a monastic rule"],
         "correct": 1,
         "expl": "One of a small number of texts included under two different collection headings."},
        {"q": "What does 'maṅgala' mean?",
         "opts": [
             "'Blessing' or 'auspicious sign'",
             "'Refuge'",
             "'Precept'",
             "'Meditation'"],
         "correct": 0,
         "expl": "The word this text's question and refrain both turn on."},
        {"q": "Where is this discourse set?",
         "opts": [
             "The Vulture's Peak near Rājagaha",
             "Jeta's Grove, Anāthapiṇḍika's monastery near Sāvatthī",
             "The Buddha's home town of Kapilavatthu",
             "No location is given"],
         "correct": 1,
         "expl": "Late at night, when a deity's light fills the entire grove."},
        {"q": "How does this text compare to the four texts before it in the Khuddakapatha?",
         "opts": [
             "It is the first full narrative discourse, with a setting, speaker, and audience",
             "It is the shortest text in the collection",
             "It is another formula with no narrative frame, like Kp 1 and Kp 2",
             "It repeats the same content as Kp 4"],
         "correct": 0,
         "expl": "The first four texts are formulas or lists without a narrative setting."},
        {"q": "What does the text name directly as one of the highest blessings, alongside seeing the noble truths?",
         "opts": [
             "Wealth and reputation",
             "Extinguishment (nibbāna)",
             "A long life",
             "Political power"],
         "correct": 1,
         "expl": "Named in the tenth verse."},
        {"q": "How many verses of answer does the Buddha give, after the deity's question verse?",
         "opts": [
             "Three",
             "Eleven",
             "Twenty",
             "One"],
         "correct": 1,
         "expl": "Each closing with the same refrain."},
    ],
    marginalia=[
        ("A deity's question", [
            "at Jeta's Grove,",
            "late at night",
        ]),
        ("Eleven verses answer", [
            "each closing with",
            "'this is the highest blessing'",
        ]),
        ("Virtue toward awakening", [
            "ordinary care, then",
            "the noble truths, extinguishment",
        ]),
        ("Also in the Sutta Nipāta", [
            "the same discourse,",
            "under a different heading",
        ]),
    ],
    further=[
        '<a href="%s/kp5/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../sutta-nipata/snp-2.4.html">Snp 2.4 &mdash; Blessings</a> &mdash; this '
        "same discourse, already complete on this site under the Sutta Nipāta.",
        '<a href="kp-4.html">Kp 4 &mdash; The Boy&rsquo;s Questions</a> &mdash; the text '
        "immediately before this one in the Khuddakapatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 6 — Gems (Ratana Sutta)
# --------------------------------------------------------------------------- #
page(
    6, "Ratana Sutta", "Gems",
    meta_title="Kp 6 — Gems | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ratana Sutta, "
        "the Khuddakapatha's protective chant praising the Buddha, the Dhamma, and the "
        "Saṅgha as three unequalled 'gems'. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given within the text itself; commentarial "
                    "tradition frames it as addressing a calamity in Vesālī"),
        ("Speaker", "Not attributed within the text; traditionally chanted rather than "
                    "read as a reported discourse"),
        ("Form", "Eighteen verses, most closing with the refrain &lsquo;this sublime gem is "
                 "in the [Buddha/Dhamma/Saṅgha]: by this truth, may you be well&rsquo;"),
        ("Length", "3&ndash;4 minutes to read"),
        ("Northern parallel", "No specific matching text in the Chinese Āgamas is asserted "
                              "in this reading guide"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; dense verse imagery and "
                       "technical terms describing stages of awakening"),
    ],
    why=(
        "This text praises the Buddha, the Dhamma, and the Saṅgha in turn as three "
        "unequalled &lsquo;gems&rsquo;, each verse closing with an appeal to truth as a "
        "source of protection: &lsquo;by this truth, may you be well&rsquo;. One of the "
        "most widely chanted protective (<em>paritta</em>) texts in the Theravada "
        "tradition, it also appears, in close to this exact wording, as its own text "
        "within the Sutta Nipāta."),
    guide=[
        ("Three gems, a repeated refrain", [
            "Across its eighteen verses, this text works through the three refuges of Kp 1 "
            "one at a time &mdash; the Buddha, the Dhamma, the Saṅgha &mdash; praising each "
            "as an unequalled &lsquo;gem&rsquo; (<em>ratana</em>), most verses closing with "
            "the same refrain naming which of the three the verse has just praised."]),
        ("Not evenly divided between the three", [
            "The praise is not distributed in strict order or equal measure: Buddha-verses "
            "and Dhamma-verses appear early, then a long run of Saṅgha-verses follows, and "
            "the final Buddha- and Saṅgha-verses close the sequence before three concluding "
            "verses address all three together."]),
        ("Doctrine folded into praise", [
            "The Saṅgha-verses in particular carry compressed doctrinal content &mdash; "
            "references to &lsquo;the four pairs&rsquo; of noble disciples, to giving up "
            "&lsquo;substantialist view, doubt, and attachment to precepts and "
            "observances&rsquo;, and to being freed from &lsquo;the four places of "
            "loss&rsquo; &mdash; describing stages of the path in the same breath as "
            "praising the community that embodies them."]),
        ("A protective chant, by tradition", [
            "Later commentarial tradition frames this text as taught to address a calamity "
            "&mdash; famine, disease, and hostile spirits &mdash; afflicting the city of "
            "Vesālī, with the truth-statements in each refrain understood as the source of "
            "its protective power. The text as it stands here carries no such narrative; "
            "the setting comes from commentary, not from this text itself."]),
        ("Also a text of the Sutta Nipāta", [
            "As with Kp 5, this discourse appears again, with only small wording "
            "differences between the two translations, as its own numbered text within the "
            "Sutta Nipāta."]),
    ],
    terms=[
        ("ratana",
         "&ldquo;gem&rdquo; or &ldquo;jewel&rdquo; &mdash; this text's title, and the word "
         "each refrain applies to the Buddha, Dhamma, or Saṅgha in turn."),
        ("paritta",
         "&ldquo;protection&rdquo; &mdash; the category of chanted text this discourse is "
         "traditionally classed among, recited for protective purposes."),
        ("tiratana",
         "the &ldquo;three jewels&rdquo; &mdash; the same three refuges named in Kp 1, "
         "praised here one at a time across eighteen verses."),
        ("the four pairs",
         "a description of the noble Saṅgha as eight kinds of individual grouped into four "
         "pairs, by stage of awakening attained."),
        ("Vesālī",
         "the city commentarial tradition associates with this text's original occasion "
         "&mdash; a calamity of famine, disease, and hostile spirits &mdash; though this "
         "narrative appears in commentary, not in the text itself."),
    ],
    text_intro=(
        "The text in full: eighteen verses praising the Buddha, the Dhamma, and the "
        "Saṅgha. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "kp6:1.1-1.4"),
        ("p", "&sect;2", "kp6:2.1-2.4"),
        ("p", "&sect;3", "kp6:3.1-3.5"),
        ("p", "&sect;4", "kp6:4.1-4.5"),
        ("p", "&sect;5", "kp6:5.1-5.5"),
        ("p", "&sect;6", "kp6:6.1-6.6"),
        ("p", "&sect;7", "kp6:7.1-7.6"),
        ("p", "&sect;8", "kp6:8.1-8.6"),
        ("p", "&sect;9", "kp6:9.1-9.6"),
        ("p", "&sect;10", "kp6:10.1-10.4"),
        ("p", "&sect;11", "kp6:11.1-11.4"),
        ("p", "&sect;12", "kp6:12.1-12.6"),
        ("p", "&sect;13", "kp6:13.1-13.6"),
        ("p", "&sect;14", "kp6:14.1-14.4"),
        ("p", "&sect;15", "kp6:15.1-15.6"),
        ("p", "&sect;16", "kp6:16.1-16.4"),
        ("p", "&sect;17", "kp6:17.1-17.4"),
        ("p", "&sect;18", "kp6:18.1-18.4"),
    ],
    quiz=[
        {"q": "What three things does this text praise in turn as unequalled 'gems'?",
         "opts": [
             "The Buddha, the Dhamma, and the Saṅgha",
             "The four noble truths",
             "The five precepts",
             "The eightfold path"],
         "correct": 0,
         "expl": "The same three refuges named in Kp 1."},
        {"q": "What refrain closes most of this text's verses?",
         "opts": [
             "'May all beings be happy'",
             "'This sublime gem is in the [Buddha/Dhamma/Saṅgha]: by this truth, may you be well'",
             "'Thus have I heard'",
             "'This is the highest blessing'"],
         "correct": 1,
         "expl": "An appeal to truth as a source of protection."},
        {"q": "Are the Buddha-, Dhamma-, and Saṅgha-verses distributed evenly through the text?",
         "opts": [
             "Yes, in a strict repeating pattern of three",
             "No — Saṅgha-verses in particular form a long run, and the order is uneven",
             "Only the Buddha is praised; the other two never appear",
             "The three are never distinguished from each other"],
         "correct": 1,
         "expl": "Buddha- and Dhamma-verses appear early, then several Saṅgha-verses follow, with Buddha- and Saṅgha-verses again near the close."},
        {"q": "What kind of chant is this text traditionally classed among?",
         "opts": [
             "A funeral chant",
             "A protective (paritta) chant",
             "An ordination formula",
             "A meal-blessing chant"],
         "correct": 1,
         "expl": "Recited for protective purposes in the Theravada tradition."},
        {"q": "What calamity does commentarial tradition associate with this text's original occasion?",
         "opts": [
             "A military invasion",
             "Famine, disease, and hostile spirits afflicting Vesālī",
             "A schism within the monastic community",
             "No occasion is ever associated with it"],
         "correct": 1,
         "expl": "This narrative comes from commentary, not from the text itself, which names no setting."},
        {"q": "What does 'ratana' mean?",
         "opts": [
             "'Gem' or 'jewel'",
             "'Refuge'",
             "'Protection'",
             "'Truth'"],
         "correct": 0,
         "expl": "This text's own title, and the word applied to the Buddha, Dhamma, and Saṅgha in turn."},
        {"q": "What kind of content do the Saṅgha-verses in particular carry?",
         "opts": [
             "Purely narrative description with no doctrine",
             "Compressed doctrinal content, such as stages of the path and freedom from the four places of loss",
             "A list of monastic rules",
             "A biography of individual disciples"],
         "correct": 1,
         "expl": "Doctrine folded into the same verses that praise the community embodying it."},
        {"q": "Where else does this same discourse appear in the Pali canon?",
         "opts": [
             "Nowhere else — this is its only appearance",
             "Again, in close to this exact wording, within the Sutta Nipāta",
             "Only within the Vinaya",
             "It appears seven times across different collections"],
         "correct": 1,
         "expl": "One of a small number of texts shared between the Khuddakapatha and the Sutta Nipāta."},
        {"q": "What term names the Saṅgha described as 'eight kinds of individual grouped into four pairs'?",
         "opts": [
             "The four pairs",
             "The five precepts",
             "The three jewels",
             "The nine abodes"],
         "correct": 0,
         "expl": "A description of the noble Saṅgha by stage of awakening attained."},
        {"q": "What text in the Khuddakapatha comes right before this one?",
         "opts": [
             "The Boy's Questions",
             "Blessings",
             "Outside the Walls",
             "A Treasure Trove"],
         "correct": 1,
         "expl": "Kp 5, another text shared with the Sutta Nipāta."},
    ],
    marginalia=[
        ("Three gems praised", [
            "Buddha, Dhamma, Saṅgha,",
            "each an unequalled jewel",
        ]),
        ("A repeated refrain", [
            "'by this truth,",
            "may you be well'",
        ]),
        ("A protective chant", [
            "recited, by tradition,",
            "to ward off calamity",
        ]),
        ("Also in the Sutta Nipāta", [
            "the same discourse,",
            "under a different heading",
        ]),
    ],
    further=[
        '<a href="%s/kp6/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../sutta-nipata/snp-2.1.html">Snp 2.1 &mdash; Gems</a> &mdash; this same '
        "discourse, already complete on this site under the Sutta Nipāta.",
        '<a href="kp-5.html">Kp 5 &mdash; Blessings</a> &mdash; the text immediately before '
        "this one in the Khuddakapatha, also shared with the Sutta Nipāta.",
        '<a href="kp-1.html">Kp 1 &mdash; The Three Refuges</a> &mdash; the same three '
        "jewels named there, praised here at greater length.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 7 — Tirokuḍḍa Kaṇḍa
# --------------------------------------------------------------------------- #
page(
    7, "Tirokuḍḍa Kaṇḍa", "Outside the Walls",
    meta_title="Kp 7 — Outside the Walls | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Tirokuḍḍa Kaṇḍa, "
        "the Khuddakapatha's verses on departed relatives waiting outside the walls, and "
        "how offerings dedicated to them help. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given within the text itself; commentarial "
                    "tradition frames it as an explanation given to King Bimbisāra"),
        ("Speaker", "Not attributed within the text; presented as direct verse teaching"),
        ("Form", "Thirteen verses moving from a description of waiting departed relatives "
                 "to instructions on how giving benefits them"),
        ("Length", "2&ndash;3 minutes to read"),
        ("Northern parallel", "No specific matching text in the Chinese Āgamas is asserted "
                              "in this reading guide"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain narrative imagery, "
                       "but resting on an unfamiliar cosmology for many readers"),
    ],
    why=(
        "This text describes departed relatives reborn as <em>peta</em> &mdash; often "
        "translated &lsquo;hungry ghosts&rsquo; &mdash; who stand outside the walls of "
        "their former homes, forgotten at feasts, unable to farm or trade to sustain "
        "themselves. It then explains what does help them: offerings given to the Saṅgha "
        "and dedicated in their name, arriving the way rain flowing downhill eventually "
        "reaches the sea. Still recited today at funerals and memorial offerings across "
        "the Theravada world."),
    guide=[
        ("Waiting outside the walls", [
            "The opening verses describe departed relatives standing outside the walls of "
            "their former homes, at junctions and crossroads, forgotten when lavish food "
            "is set out inside &mdash; not through any deliberate cruelty, but simply "
            "because &lsquo;no-one remembers them at all, because of those beings' "
            "deeds&rsquo;."]),
        ("What does not help, and what does", [
            "The text is direct about what fails to reach the departed: neither farming nor "
            "trade sustains them in their new state, and neither tears nor grief nor "
            "lamentation is of any use to them. What helps is a specific act &mdash; giving "
            "an offering, dedicated in their name, placed with the Saṅgha."]),
        ("An image of water flowing downward", [
            "Two consecutive verses compare the offering's effect to water: rain falling on "
            "high ground flows down to the plains, and full rivers swell the ocean seas "
            "&mdash; in the same way, the text says, what is given here reaches and aids "
            "the departed."]),
        ("A duty stated plainly", [
            "The closing verse names this practice directly as &lsquo;the relative's "
            "duty&rsquo;: honoring the departed, supporting the mendicants who receive the "
            "offering, and producing no little merit for the giver, all at once."]),
        ("Still practiced today", [
            "This text remains one of the most commonly recited verses at funerals and "
            "memorial-offering ceremonies across Theravada Buddhist countries, its "
            "instructions followed much as its verses describe them."]),
    ],
    terms=[
        ("peta",
         "often translated &ldquo;hungry ghost&rdquo; &mdash; a being reborn into a "
         "state of want, dependent on offerings dedicated by living relatives."),
        ("dakkhiṇā",
         "a gift or offering, especially one given with a specific dedication &mdash; the "
         "kind of offering this text describes as reaching the departed."),
        ("puñña",
         "&ldquo;merit&rdquo; &mdash; what the giving described in this text is said to "
         "produce, both for the departed and, in the closing verse, for the giver."),
        ("Saṅgha",
         "the monastic community; the text specifies that an offering &ldquo;well placed "
         "in the Saṅgha&rdquo; is what aids the departed, not an offering placed just "
         "anywhere."),
        ("Bimbisāra",
         "the king commentarial tradition names as the original recipient of this "
         "teaching, troubled by relatives reborn as petas; this narrative appears in "
         "commentary, not in the text itself."),
    ],
    text_intro=(
        "The text in full: thirteen verses on departed relatives and the offerings that "
        "aid them. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Waiting outside the walls"),
        ("p", "&sect;1", "kp7:1.1-1.4"),
        ("p", "&sect;2", "kp7:2.1-2.4"),
        ("h3", "Giving, and what it accomplishes"),
        ("p", "&sect;3", "kp7:3.1-3.4"),
        ("p", "&sect;4", "kp7:4.1-4.4"),
        ("p", "&sect;5", "kp7:5.1-5.4"),
        ("p", "&sect;6", "kp7:6.1-6.4"),
        ("p", "&sect;7", "kp7:7.1-7.4"),
        ("p", "&sect;8", "kp7:8.1-8.4"),
        ("p", "&sect;9", "kp7:9.1-9.4"),
        ("h3", "The relative's duty"),
        ("p", "&sect;10", "kp7:10.1-10.4"),
        ("p", "&sect;11", "kp7:11.1-11.4"),
        ("p", "&sect;12", "kp7:12.1-12.4"),
        ("p", "&sect;13", "kp7:13.1-13.4"),
    ],
    quiz=[
        {"q": "Where does this text say departed relatives (petas) stand, waiting?",
         "opts": [
             "Inside their former homes, at the dinner table",
             "Outside the walls, at junctions and crossroads",
             "In a specific named heaven realm",
             "Nowhere — they are said to have no fixed location"],
         "correct": 1,
         "expl": "Returning to their former homes, they wait beside the door posts."},
        {"q": "Why does the text say the departed go unnoticed when food is set out at feasts?",
         "opts": [
             "Because of deliberate cruelty from their living relatives",
             "'No-one remembers them at all, because of those beings' deeds'",
             "Because the food offered is the wrong kind",
             "Because petas are invisible to everyone without exception"],
         "correct": 1,
         "expl": "Simply forgotten, not deliberately excluded."},
        {"q": "What does this text say is NOT of use to the departed?",
         "opts": [
             "Offerings dedicated in their name",
             "Neither tears, grief, nor lamentation from the living",
             "Giving placed with the Saṅgha",
             "Nothing is said to be useless"],
         "correct": 1,
         "expl": "'So long as their relatives stay like this' — grieving instead of giving."},
        {"q": "What image do two consecutive verses use to describe how an offering reaches the departed?",
         "opts": [
             "A lit lamp passed from hand to hand",
             "Water flowing downhill and rivers swelling into the sea",
             "A seed planted and growing into a tree",
             "A messenger carrying a letter"],
         "correct": 1,
         "expl": "Rain on high ground flowing down to the plains; full rivers swelling the ocean."},
        {"q": "Where does the text specify the offering should be placed for it to aid the departed?",
         "opts": [
             "Anywhere at all, the location does not matter",
             "Well placed in the Saṅgha",
             "Buried at the gravesite",
             "Given only to family members"],
         "correct": 1,
         "expl": "An offering 'well placed in the Saṅgha... is for their lasting welfare'."},
        {"q": "What does the closing verse name this entire practice as?",
         "opts": [
             "An optional custom with no particular significance",
             "'The relative's duty'",
             "A punishment for past misdeeds",
             "A purely symbolic gesture with no real effect"],
         "correct": 1,
         "expl": "Honoring the departed, supporting the mendicants, and producing merit, all at once."},
        {"q": "What does 'peta' mean, as this text uses it?",
         "opts": [
             "A fully awakened being",
             "Often translated 'hungry ghost' — a being reborn into a state of want",
             "A deity residing in a heaven realm",
             "A living relative who has not yet died"],
         "correct": 1,
         "expl": "Dependent on offerings dedicated by living relatives."},
        {"q": "What king does commentarial tradition associate with this text's original occasion?",
         "opts": [
             "King Pasenadi",
             "King Bimbisāra, troubled by relatives reborn as petas",
             "King Ajātasattu",
             "No king is ever associated with it"],
         "correct": 1,
         "expl": "This narrative comes from commentary, not from the text itself."},
        {"q": "Is this text still used today?",
         "opts": [
             "No, it fell out of use centuries ago",
             "Yes — commonly recited at funerals and memorial-offering ceremonies",
             "It is used only by novices during training",
             "It is recited only once a year, at a fixed festival"],
         "correct": 1,
         "expl": "Across Theravada Buddhist countries."},
        {"q": "What text in the Khuddakapatha comes right before this one?",
         "opts": [
             "The Ten Precepts",
             "Gems",
             "A Treasure Trove",
             "The Discourse on Love"],
         "correct": 1,
         "expl": "Kp 6, another verse text but praising the three jewels rather than describing an offering's effect."},
    ],
    marginalia=[
        ("Waiting outside", [
            "at junctions, crossroads,",
            "forgotten at the feast",
        ]),
        ("What doesn't help", [
            "farming, trade, tears,",
            "grief, or lamentation",
        ]),
        ("Water flowing downward", [
            "rain to the plains,",
            "rivers to the sea",
        ]),
        ("Named a duty", [
            "for the living relative",
            "toward the departed",
        ]),
    ],
    further=[
        '<a href="%s/kp7/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="kp-6.html">Kp 6 &mdash; Gems</a> &mdash; the text immediately before this '
        "one in the Khuddakapatha.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 8 — Nidhikaṇḍa Sutta
# --------------------------------------------------------------------------- #
page(
    8, "Nidhikaṇḍa Sutta", "A Treasure Trove",
    meta_title="Kp 8 — A Treasure Trove | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nidhikaṇḍa "
        "Sutta, the Khuddakapatha's contrast between buried savings, which can always "
        "fail, and merit, which cannot be lost. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given; this is a teaching in verse, not a "
                    "reported discourse to a named audience"),
        ("Speaker", "Not attributed within the text; presented as direct verse teaching"),
        ("Form", "Sixteen verses: buried savings and how they fail, then merit and the "
                 "long list of what it secures instead"),
        ("Length", "3&ndash;4 minutes to read"),
        ("Northern parallel", "No specific matching text in the Chinese Āgamas is asserted "
                              "in this reading guide"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clear central image, "
                       "but the closing list names several technical attainments by name"),
    ],
    why=(
        "This text opens with an ordinary image: a person buries their savings for "
        "security, only for the text to list five ordinary ways that hoard can still fail "
        "&mdash; shifted, forgotten, stolen by animals or spirits, or dug up by an unloved "
        "heir. Against this, it sets a different kind of saving &mdash; giving, morality, "
        "restraint, self-control &mdash; that no thief can take and that, unlike buried "
        "gold, actually travels with a person when they die."),
    guide=[
        ("A buried hoard, and how it fails", [
            "The opening verses describe someone burying savings by the water's edge, "
            "against future need &mdash; debt, famine, slander, banditry. The text then "
            "lists, quite practically, five ways even a well-hidden hoard can still be "
            "lost: it shifts location, its marker is forgotten, dragons or spirits carry "
            "it off, or an unloved heir digs it up in secret."]),
        ("A different kind of saving", [
            "Against that unreliable hoard, the text sets giving, morality, restraint, and "
            "self-control as a different kind of saving &mdash; one that &lsquo;stays with "
            "you, undecaying&rsquo;, immune to the five failures just listed, and, in the "
            "text's own words, &lsquo;only this you take when you go&rsquo;."]),
        ("A long list of what merit secures", [
            "Roughly half the text is a cumulative list of what this kind of saving "
            "provides &mdash; from ordinary goods like good looks and a good voice, through "
            "worldly power up to the happiness of a Wheel-Turning Monarch, to specifically "
            "spiritual attainments: mastery of knowledge and freedom, the perfections of a "
            "disciple, and the plane of an independent Buddha, each closing on the same "
            "refrain, &lsquo;through this they have it all&rsquo;."]),
        ("From ordinary benefit to full attainment", [
            "Like Kp 5's blessings, this list is not flat: it moves from mundane advantages "
            "any listener would recognize, up through progressively higher forms of "
            "success, ending at &lsquo;attaining extinguishment&rsquo; and the rarest "
            "attainments named in the tradition."]),
        ("A gap in the source text", [
            "One line of the eighth section is missing from the source manuscript this "
            "translation is drawn from (between &lsquo;at a shrine or with the "
            "Saṅgha&rsquo; and &lsquo;with mother or father&rsquo;); this page reproduces "
            "the source exactly as it stands, gap included, rather than supplying a "
            "conjectural line."]),
    ],
    terms=[
        ("nidhi",
         "&ldquo;treasure&rdquo;, &ldquo;hoard&rdquo;, or &ldquo;trove&rdquo; &mdash; this "
         "text's title, applied first to buried savings and then, by contrast, to merit."),
        ("puñña",
         "&ldquo;merit&rdquo; &mdash; the &ldquo;accomplishment&rdquo; the text's closing "
         "verse says is &ldquo;so very beneficial&rdquo;, and the saving that cannot be "
         "lost the way buried gold can."),
        ("cakkavattī",
         "&ldquo;Wheel-Turning Monarch&rdquo; &mdash; a legendary ideal ruler, named among "
         "the worldly attainments this text says merit secures."),
        ("paccekabuddha",
         "an &ldquo;independent Buddha&rdquo;, awakened without a teacher but not teaching "
         "others &mdash; named among the rarest attainments in the text's closing list."),
        ("nibbāna",
         "&ldquo;extinguishment&rdquo; &mdash; named directly among the things merit "
         "secures, alongside human success and heavenly delight."),
    ],
    text_intro=(
        "The text in full: sixteen verses on buried savings and the different saving of "
        "merit. Translation: Bhikkhu Sujato (CC0, SuttaCentral). One line of section 8 is "
        "missing from the source manuscript and is reproduced here as a gap, not filled "
        "in."),
    text=[
        ("h3", "A hoard, and how it fails"),
        ("p", "&sect;1", "kp8:1.1-1.4"),
        ("p", "&sect;2", "kp8:2.1-2.6"),
        ("p", "&sect;3", "kp8:3.1-3.4"),
        ("p", "&sect;4", "kp8:4.1-4.4"),
        ("p", "&sect;5", "kp8:5.1-5.4"),
        ("h3", "A different kind of saving"),
        ("p", "&sect;6", "kp8:6.1-6.4"),
        ("p", "&sect;7", "kp8:7.1-7.4"),
        ("p", "&sect;8", "kp8:8.1-8.4"),
        ("p", "&sect;9", "kp8:9.1-9.4"),
        ("h3", "What merit secures"),
        ("p", "&sect;10", "kp8:10.1-10.4"),
        ("p", "&sect;11", "kp8:11.1-11.4"),
        ("p", "&sect;12", "kp8:12.1-12.4"),
        ("p", "&sect;13", "kp8:13.1-13.4"),
        ("p", "&sect;14", "kp8:14.1-14.4"),
        ("p", "&sect;15", "kp8:15.1-15.4"),
        ("p", "&sect;16", "kp8:16.1-16.4"),
    ],
    quiz=[
        {"q": "What does this text's opening image describe?",
         "opts": [
             "A person meditating in a forest",
             "A person burying their savings by the water's edge, against future need",
             "A king distributing wealth to his subjects",
             "A merchant trading goods at a market"],
         "correct": 1,
         "expl": "Set aside for debt, famine, slander, or banditry."},
        {"q": "How many ways does the text list for a buried hoard to still fail?",
         "opts": [
             "None — buried savings are described as completely reliable",
             "Five: shifting location, forgotten markers, dragons, spirits, or an unloved heir",
             "One single way, repeated for emphasis",
             "Ten separate causes"],
         "correct": 1,
         "expl": "Even a well-hidden hoard can be lost in any of these ways."},
        {"q": "What does the text set up as a different, more reliable kind of saving?",
         "opts": [
             "Investing in land",
             "Giving, morality, restraint, and self-control",
             "Storing wealth with a trusted relative instead of burying it",
             "Converting savings into gems instead of gold"],
         "correct": 1,
         "expl": "'Stays with you, undecaying' — immune to the five failures listed for buried gold."},
        {"q": "What does the text say about this different kind of saving, unlike buried gold?",
         "opts": [
             "It must be shared equally with others",
             "'Only this you take when you go' — it travels with a person after death",
             "It can still be stolen by a thief",
             "It requires constant renewal or it decays"],
         "correct": 1,
         "expl": "No thief makes off with it, and it stays with you when everything else is left behind."},
        {"q": "What refrain closes the list of what merit secures?",
         "opts": [
             "'This is the highest blessing'",
             "'Through this they have it all'",
             "'By this truth, may you be well'",
             "'May all beings be happy'"],
         "correct": 1,
         "expl": "Repeated across the second half of the text's list."},
        {"q": "What kind of progression does the list of merit's benefits follow?",
         "opts": [
             "A random, unordered list with no progression",
             "From ordinary advantages up through worldly power to spiritual attainments",
             "A strictly descending order, from highest to lowest",
             "It repeats the same single benefit throughout"],
         "correct": 1,
         "expl": "From good looks and a good voice up to extinguishment and the rarest attainments."},
        {"q": "What does 'paccekabuddha' mean, as named in the text's closing list?",
         "opts": [
             "A fully ordained monk of ten years' standing",
             "An 'independent Buddha', awakened without a teacher but not teaching others",
             "A lay disciple who has taken the five precepts",
             "A deity residing in the highest heaven"],
         "correct": 1,
         "expl": "Named among the rarest attainments merit is said to secure."},
        {"q": "What is unusual about section 8 of this text, as presented on this page?",
         "opts": [
             "It is written in prose rather than verse",
             "One line is missing from the source manuscript and is left as a gap, not filled in",
             "It repeats an earlier section word for word",
             "It is the only section without a refrain"],
         "correct": 1,
         "expl": "This page reproduces the source translation exactly as it stands."},
        {"q": "What does 'nidhi' mean?",
         "opts": [
             "'Merit'",
             "'Treasure', 'hoard', or 'trove' — this text's own title",
             "'Refuge'",
             "'Precept'"],
         "correct": 1,
         "expl": "Applied first to buried savings, then by contrast to merit."},
        {"q": "What text in the Khuddakapatha comes right before this one?",
         "opts": [
             "Gems",
             "Outside the Walls",
             "The Discourse on Love",
             "Blessings"],
         "correct": 1,
         "expl": "Kp 7, also concerned with what does and doesn't reliably help a person."},
    ],
    marginalia=[
        ("A buried hoard", [
            "five ways it can fail —",
            "lost, forgotten, stolen",
        ]),
        ("A different saving", [
            "giving, morality,",
            "restraint, self-control",
        ]),
        ("Travels with you", [
            "'only this you take",
            "when you go'",
        ]),
        ("A cumulative list", [
            "ordinary goods to",
            "extinguishment itself",
        ]),
    ],
    further=[
        '<a href="%s/kp8/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="kp-7.html">Kp 7 &mdash; Outside the Walls</a> &mdash; the text '
        "immediately before this one in the Khuddakapatha.",
        '<a href="kp-2.html">Kp 2 &mdash; The Ten Precepts</a> &mdash; the ethical '
        "undertakings this text's &lsquo;different kind of saving&rsquo; draws on.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Kp 9 — Metta Sutta
# --------------------------------------------------------------------------- #
page(
    9, "Metta Sutta", "The Discourse on Love",
    meta_title="Kp 9 — The Discourse on Love | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Metta Sutta, "
        "the Khuddakapatha's closing text on unfolding a boundless heart of "
        "loving-kindness toward all beings. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting is given; this is a teaching in verse, not a "
                    "reported discourse to a named audience"),
        ("Speaker", "Not attributed within the text; presented as direct verse teaching"),
        ("Form", "Ten verses: qualities of character first, then an exhaustive wish for "
                 "all beings' happiness, then instructions for sustaining it as a practice"),
        ("Length", "2&ndash;3 minutes to read"),
        ("Northern parallel", "No specific matching text in the Chinese Āgamas is asserted "
                              "in this reading guide"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain language, but the "
                       "closing verse names a specific attainment briefly and without gloss"),
    ],
    why=(
        "This text, among the most widely known in the entire tradition, opens not with "
        "loving-kindness itself but with the character of someone who would practice it: "
        "capable, content, unburdensome, easy to speak to. Only then does it turn to the "
        "practice proper &mdash; wishing happiness for every kind of being that exists, "
        "then sustaining that wish in every posture, as &lsquo;a divine meditation in this "
        "life&rsquo;. It closes the Khuddakapatha, and also appears, in close to this exact "
        "wording, as its own text within the Sutta Nipāta."),
    guide=[
        ("Character before practice", [
            "The text's opening verses describe not loving-kindness itself but the "
            "character of the person who would practice it &mdash; capable, upright, easy "
            "to speak to, gentle, content, unburdensome, alert, courteous, not fawning on "
            "families for support. The practice is introduced only after this groundwork "
            "is laid."]),
        ("An exhaustive taxonomy of beings", [
            "When the wish for happiness finally arrives, it is deliberately exhaustive: "
            "frail or firm, long or large, medium, small, tiny or round, seen or unseen, "
            "living far or near, already born or about to be born &mdash; &lsquo;with not "
            "a one left out&rsquo;, as the text itself says."]),
        ("An ethical floor, not just a feeling", [
            "Before the text moves to its central simile, it states a concrete ethical "
            "limit: let none deceive another, or look down on anyone, or wish pain on "
            "another even when provoked or aggrieved &mdash; loving-kindness here includes "
            "a standard of conduct, not only an inner attitude."]),
        ("A mother's protection, and a boundless heart", [
            "The text's central image compares this attitude to a mother protecting her "
            "only child even at the risk of her own life &mdash; and then asks that the "
            "same intensity of care be unfolded toward all creatures, in every direction, "
            "&lsquo;unconstricted, without enmity or foe&rsquo;."]),
        ("A sustained practice, not a single wish", [
            "The closing verses turn from the wish itself to how it is sustained: kept in "
            "mind while standing, walking, sitting, or lying down, called &lsquo;a divine "
            "meditation in this life&rsquo;, before a final verse links the sustained "
            "practice to a specific fruit &mdash; freedom from further rebirth into "
            "a womb."]),
    ],
    terms=[
        ("mettā",
         "&ldquo;loving-kindness&rdquo; or &ldquo;love&rdquo; &mdash; this text's title and "
         "central practice, a wish for the happiness of all beings."),
        ("brahmavihāra",
         "&ldquo;divine abode&rdquo; or &ldquo;divine meditation&rdquo; &mdash; the "
         "category of practice this text names loving-kindness as one instance of."),
        ("appamāṇa",
         "&ldquo;boundless&rdquo; or &ldquo;immeasurable&rdquo; &mdash; the quality the "
         "text asks the heart of loving-kindness to take on, unconstricted in any "
         "direction."),
        ("anāgāmi",
         "&ldquo;non-returner&rdquo; &mdash; not named directly, but the attainment the "
         "closing verse's phrase &lsquo;never return to a womb again&rsquo; describes."),
        ("Sutta Nipāta",
         "the other Khuddaka Nikāya collection, already complete on this site, that "
         "includes this same discourse under its own numbering."),
    ],
    text_intro=(
        "The text in full: ten verses on the character, the practice, and the sustaining "
        "of loving-kindness. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The character of the practitioner"),
        ("p", "&sect;1", "kp9:1.1-1.4"),
        ("p", "&sect;2", "kp9:2.1-2.4"),
        ("p", "&sect;3", "kp9:3.1-3.4"),
        ("h3", "The wish, exhaustively stated"),
        ("p", "&sect;4", "kp9:4.1-4.4"),
        ("p", "&sect;5", "kp9:5.1-5.4"),
        ("p", "&sect;6", "kp9:6.1-6.4"),
        ("h3", "A boundless heart, sustained"),
        ("p", "&sect;7", "kp9:7.1-7.4"),
        ("p", "&sect;8", "kp9:8.1-8.4"),
        ("p", "&sect;9", "kp9:9.1-9.4"),
        ("p", "&sect;10", "kp9:10.1-10.4"),
    ],
    quiz=[
        {"q": "What does this text describe first, before turning to loving-kindness itself?",
         "opts": [
             "The geography of where the practice should be done",
             "The character of the person who would practice it — capable, content, easy to speak to",
             "A list of historical teachers who taught this practice",
             "The physical posture required for meditation"],
         "correct": 1,
         "expl": "The practice is introduced only after this groundwork is laid."},
        {"q": "How does the text describe the range of beings the wish for happiness covers?",
         "opts": [
             "Only human beings are included",
             "Exhaustively — frail or firm, seen or unseen, born or about to be born, 'with not a one left out'",
             "Only beings the practitioner already knows personally",
             "Only beings currently suffering"],
         "correct": 1,
         "expl": "A deliberately exhaustive taxonomy, not a general gesture."},
        {"q": "What ethical limit does the text state before its central simile?",
         "opts": [
             "No limit is stated; the text is purely about inner feeling",
             "Let none deceive another or wish pain on anyone, even when provoked",
             "Only monastics are bound by any ethical standard here",
             "Violence is permitted in self-defense"],
         "correct": 1,
         "expl": "Loving-kindness here includes a standard of conduct, not only an inner attitude."},
        {"q": "What image does the text use for the intensity of this attitude?",
         "opts": [
             "A soldier defending a fortress",
             "A mother protecting her only child, even at the risk of her own life",
             "A merchant guarding valuable goods",
             "A king protecting his kingdom"],
         "correct": 1,
         "expl": "The same intensity of care is then asked to be unfolded toward all creatures."},
        {"q": "In what postures does the text say this practice should be sustained?",
         "opts": [
             "Only while formally seated in meditation",
             "Standing, walking, sitting, or lying down",
             "Only while walking outdoors",
             "Only immediately before sleep"],
         "correct": 1,
         "expl": "Called 'a divine meditation in this life' when kept up throughout the day."},
        {"q": "What does the text's closing phrase, 'never return to a womb again', describe?",
         "opts": [
             "Literal infertility",
             "The attainment of non-returner (anāgāmi), though not named directly by that term",
             "A curse placed on the practitioner",
             "A metaphor with no connection to rebirth"],
         "correct": 1,
         "expl": "Linking sustained practice to a specific fruit."},
        {"q": "What does 'mettā' mean?",
         "opts": [
             "'Loving-kindness' or 'love' — this text's title and central practice",
             "'Boundless'",
             "'Non-returner'",
             "'Divine abode'"],
         "correct": 0,
         "expl": "A wish for the happiness of all beings."},
        {"q": "What category of practice does this text name loving-kindness as one instance of?",
         "opts": [
             "Ordination formula",
             "Brahmavihāra, 'divine abode' or 'divine meditation'",
             "Precept",
             "Refuge"],
         "correct": 1,
         "expl": "Named directly in the text's closing verses."},
        {"q": "Where else does this same discourse appear in the Pali canon?",
         "opts": [
             "Nowhere else — this is its only appearance",
             "Again, in close to this exact wording, within the Sutta Nipāta",
             "Only in later commentarial literature",
             "In the Vinaya, as a monastic rule"],
         "correct": 1,
         "expl": "One of a small number of texts shared between the Khuddakapatha and the Sutta Nipāta."},
        {"q": "What position does this text hold within the Khuddakapatha?",
         "opts": [
             "It opens the collection",
             "It closes the collection, as its ninth and final text",
             "It is the collection's shortest text",
             "It sits in the middle of the nine texts"],
         "correct": 1,
         "expl": "The last of the Khuddakapatha's nine texts covered in this project."},
    ],
    marginalia=[
        ("Character first", [
            "capable, content,",
            "easy to speak to",
        ]),
        ("Every being included", [
            "'with not a one",
            "left out'",
        ]),
        ("A mother's protection", [
            "unfolded toward",
            "all creatures",
        ]),
        ("Standing, walking, sitting", [
            "a sustained practice,",
            "not a single wish",
        ]),
    ],
    further=[
        '<a href="%s/kp9/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../sutta-nipata/snp-1.8.html">Snp 1.8 &mdash; The Discourse on Love</a> '
        "&mdash; this same discourse, already complete on this site under the Sutta "
        "Nipāta.",
        '<a href="kp-8.html">Kp 8 &mdash; A Treasure Trove</a> &mdash; the text immediately '
        "before this one, closing out the Khuddakapatha.",
        '<a href="./">Khuddakapatha</a> &mdash; back to the collection index, all nine '
        "texts.",
    ],
)
