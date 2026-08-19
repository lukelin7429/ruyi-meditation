# -*- coding: utf-8 -*-
"""Khuddakapatha — Basic Passages. Nine short texts, one per page."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Khuddakapatha — Basic Passages"
# This is the first module of the whole Khuddakapatha, and the Khuddakapatha
# itself has no pre-existing pages on this site, so HEAD/TAIL both default to
# "./" until a further Khuddaka Nikāya collection module exists to hand off
# to (or from).
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
