# -*- coding: utf-8 -*-
"""Tika Nipāta — The Threes. One discourse per page, from AN 3.1."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Tika Nipāta — The Threes"
# The Threes follow the completed Twos. AN 3.61, 3.65 and 3.100 were published
# before this series began working in order; they are listed in the index by
# INDEX_EXTRA and are not generated here.
HEAD = ("an-2.310-479.html", "AN 2.310&ndash;479 &middot; Greed, Abbreviated")
TAIL = ("an-3.61.html", "AN 3.61 &middot; Sectarian Tenets")
INDEX_EXTRA = [
    ("an-3.61", "Titthāyatana", "Sectarian Tenets"),
    ("an-3.65", "Kesamutti (Kālāma)", "With the Kālāmas of Kesamutta"),
    ("an-3.100", "Loṇaphala", "A Lump of Salt"),
]

PAGES = []

VAGGA_1 = "<em>Bālavagga</em> &mdash; the first chapter of the Threes"
SETTING_1 = ("Sāvatthī, in Jeta&rsquo;s Grove, Anāthapiṇḍika&rsquo;s monastery; stated at "
             "the head of AN 3.1 and understood to hold across the chapter")
SPEAKER = "The Buddha alone, addressing the mendicants"


def page(num, pali, title, **kw):
    """Shared scaffolding for a single discourse of the Threes."""
    d = {
        "slug": "an-3.%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "an3/an3.%d" % num,
        "crumb": "AN 3.%d" % num,
        "number_line": "Aṅguttara Nikāya &middot; Discourse 3.%d" % num,
        "title": title,
        "subtitle": "<em>%ssutta</em> &mdash; %s" % (pali, kw.pop("vagga", VAGGA_1)),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# AN 3.1 — Bhayasutta
# --------------------------------------------------------------------------- #
page(
    1, "Bhaya", "Perils",
    meta_title="AN 3.1 — Perils | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Bhayasutta, the "
        "discourse that opens the Threes — every danger in the world traced to the foolish "
        "rather than the astute, with the simile of a fire that starts in a grass hut and "
        "burns down the mansion. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", SETTING_1),
        ("Speakers", SPEAKER),
        ("Form", "A threefold assertion, a simile, the assertion restated, and a closing "
                 "training instruction"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The fool-and-astute material that opens this chapter is well "
                              "represented in the Chinese Madhyama-āgama (T26); this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a short and forceful discourse "
                       "whose claim is broader than it first appears"),
    ],
    why=(
        "The Threes open on a claim large enough to be startling: whatever dangers, perils, and "
        "hazards there are in the world, all of them come from the foolish and none from the "
        "astute. Not most. All. The simile that follows &mdash; a fire starting in a grass hut and "
        "burning down a sealed and plastered mansion &mdash; is about how little the initial scale "
        "of a foolish act predicts its eventual damage. And the discourse ends by naming what the "
        "next nine will spend themselves defining: the three things by which a fool is known."),
    guide=[
        ("The teaching in one sentence", [
            "Every danger in the world originates in foolishness, and the small scale at which it "
            "starts tells you nothing about how far it will reach."]),
        ("Three words for danger", [
            "The discourse uses three: <em>bhaya</em>, danger or fear; <em>upaddava</em>, peril or "
            "affliction; and <em>upasagga</em>, hazard or calamity. English translators divide them "
            "differently and the boundaries are not sharp in Pāli either.",
            "The Threes routinely open a discourse by enumerating near-synonyms in this way, and the "
            "function is the same as the ten terms for dependence in AN 2.77&ndash;86: to state that "
            "the claim holds under every available description. Whatever you would call a bad thing "
            "that happens, it belongs on this list."]),
        ("The claim, and how strong it is", [
            "Read carefully the assertion is unrestricted. It does not say that fools cause more "
            "danger than the astute, or that most dangers can be traced to folly. It says all "
            "dangers come from the foolish and that no danger, peril, or hazard comes from the "
            "astute at all.",
            "That is worth pressing on, because the obvious objection arrives immediately: what "
            "about earthquakes, illness, and the ordinary hazards of being alive? The discourse does "
            "not address it, and it would be dishonest to pretend it does. What can be said is that "
            "the Pāli terms carry a strong sense of harm arising within human affairs &mdash; the "
            "perils a community faces, the calamities that overtake a household &mdash; and that the "
            "surrounding discourses are all about conduct. Read in context, the subject is the "
            "damage people do, not the weather.",
            "Read that way the claim is still strong and considerably more defensible. It says that "
            "when something goes wrong between people, the cause is always somebody acting "
            "foolishly, and that no amount of astuteness anywhere in the system generates harm. "
            "Wisdom, on this account, is not merely less harmful than folly. It is not harmful."]),
        ("The fire in the grass hut", [
            "The simile is precise and worth unpacking. A fire spreads from a hut made of reeds or "
            "grass and burns down a bungalow that is plastered inside and out, draft-free, with "
            "doors fastened and windows shuttered.",
            "Every detail of the second building is a defense. It is sealed, weatherproofed, and "
            "shut up; nothing about its own construction is at fault. And none of it helps, because "
            "the fire did not start there. The image is about the asymmetry between the effort that "
            "goes into protecting something and the effort required to destroy it &mdash; and about "
            "the fact that a well-built structure is not protected by its own soundness from what "
            "happens next door.",
            "Applied to a community, which is how the surrounding chapters use this kind of image, it "
            "says that the careful and the well-ordered are not insulated from the one person acting "
            "foolishly among them. That is a plain observation about institutions and it does not "
            "need any Buddhist commitment to recognize."]),
        ("The instruction at the end", [
            "The discourse closes by telling the listener to shun the three things by which a fool is "
            "known and to undertake the three things by which an astute person is known &mdash; "
            "without saying what those things are.",
            "That is not an oversight. AN 3.2, the next discourse, supplies them: bad and good "
            "conduct by way of body, speech, and mind. The opening discourse states the stakes and "
            "the closing formula, and the chapter then spends nine discourses filling in the "
            "content, each time from a slightly different angle &mdash; deeds, thinking, mistakes, "
            "questions, blame, harm. Reading AN 3.1 alone leaves a gap that the chapter is designed "
            "to close."]),
    ],
    terms=[
        ("bhaya",
         "&ldquo;danger, fear, peril&rdquo; &mdash; the first of the three words the discourse uses "
         "and the one it is named after."),
        ("upaddava",
         "&ldquo;peril, affliction&rdquo; &mdash; the second, carrying a sense of something that "
         "befalls a person or a household."),
        ("upasagga",
         "&ldquo;hazard, calamity&rdquo; &mdash; the third, and the most sudden of the three."),
        ("bāla / paṇḍita",
         "&ldquo;fool&rdquo; and &ldquo;astute person&rdquo; &mdash; the pair the whole chapter turns "
         "on, defined by conduct rather than by intelligence."),
        ("naḷāgārā vā tiṇāgārā vā",
         "&ldquo;from a hut of reeds or grass&rdquo; &mdash; where the fire starts. The contrast is "
         "with a <em>kūṭāgāra</em>, a peaked-roof house, plastered and shuttered."),
    ],
    text_intro=(
        "The discourse in full: the threefold assertion, the simile of the fire, the restatement, "
        "and the training instruction. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The setting"),
        ("p", "&sect;1", "an3.1:1.1-1.6"),
        ("h3", "All danger comes from the foolish"),
        ("p", "&sect;2", "an3.1:2.1-2.7"),
        ("p", "&sect;3", "an3.1:3.1-3.4"),
        ("h3", "So you should train"),
        ("p", "&sect;4", "an3.1:4.1-4.3"),
    ],
    quiz=[
        {"q": "How strong is the claim AN 3.1 makes about danger?",
         "opts": [
             "That fools cause somewhat more danger than the astute",
             "That most dangers can be traced to folly",
             "That all dangers, perils, and hazards come from the foolish, and none at all from the astute",
             "That danger is unavoidable"],
         "correct": 2,
         "expl": "Unrestricted in both directions: everything from one source, nothing from the other."},
        {"q": "Why does the discourse use three words for danger?",
         "opts": [
             "Because they name three different times of life",
             "To state that the claim holds under every available description &mdash; the same function as the ten terms for dependence in AN 2.77&ndash;86",
             "Because the Pāli has no general word for danger",
             "To distinguish monastic from lay hazards"],
         "correct": 1,
         "expl": "Whatever you would call a bad thing that happens, it belongs on the list."},
        {"q": "What objection does the guide raise, and how does it answer it?",
         "opts": [
             "That earthquakes and illness are not caused by fools &mdash; and the answer is that the Pāli terms carry a strong sense of harm arising within human affairs, and the surrounding discourses are all about conduct",
             "That the discourse is inauthentic",
             "That fools cannot be identified",
             "That the claim is trivially true"],
         "correct": 0,
         "expl": "Read in context, the subject is the damage people do, not the weather."},
        {"q": "What does the claim amount to on that reading?",
         "opts": [
             "That wisdom is merely less harmful than folly",
             "That when something goes wrong between people the cause is always somebody acting foolishly, and no amount of astuteness anywhere in the system generates harm",
             "That the astute are exempt from suffering",
             "That folly is incurable"],
         "correct": 1,
         "expl": "Wisdom is not less harmful than folly; it is not harmful."},
        {"q": "What is significant about the building that burns down in the simile?",
         "opts": [
             "That it is poorly built",
             "That every detail of it is a defense &mdash; plastered, draft-free, doors fastened, windows shuttered &mdash; and none of it helps, because the fire did not start there",
             "That it is unoccupied",
             "That it belongs to a fool"],
         "correct": 1,
         "expl": "A well-built structure is not protected by its own soundness from what happens next door."},
        {"q": "What does the simile say about scale?",
         "opts": [
             "That large fires start large",
             "That the initial scale of a foolish act tells you nothing about how far the damage will reach &mdash; a grass hut can take down a mansion",
             "That small fires are harmless",
             "That fires spread only in dry seasons"],
         "correct": 1,
         "expl": "The asymmetry between the effort of protecting something and the effort of destroying it."},
        {"q": "Applied to a community, what does the image observe?",
         "opts": [
             "That communities should be smaller",
             "That the careful and the well-ordered are not insulated from the one person acting foolishly among them",
             "That fools should be expelled immediately",
             "That buildings should be separated"],
         "correct": 1,
         "expl": "A plain observation about institutions, needing no Buddhist commitment to recognize."},
        {"q": "What does the closing instruction tell the listener to do?",
         "opts": [
             "To avoid fools entirely",
             "To shun the three things by which a fool is known and undertake the three by which an astute person is known &mdash; without saying what they are",
             "To extinguish fires promptly",
             "To build with stone rather than reeds"],
         "correct": 1,
         "expl": "The gap is deliberate."},
        {"q": "Where are those three things supplied?",
         "opts": [
             "Nowhere in the canon",
             "In AN 3.2, the next discourse: bad and good conduct by way of body, speech, and mind",
             "In the Vinaya",
             "In a later commentary only"],
         "correct": 1,
         "expl": "The opening discourse states the stakes; the chapter then fills in the content nine times over."},
        {"q": "How does the rest of the chapter proceed?",
         "opts": [
             "By repeating AN 3.1 verbatim",
             "By turning to an unrelated subject",
             "By defining the fool and the astute person from a slightly different angle each time &mdash; deeds, thinking, mistakes, questions, blame, harm",
             "By naming individual disciples"],
         "correct": 2,
         "expl": "Reading AN 3.1 alone leaves a gap the chapter is designed to close."},
    ],
    marginalia=[
        ("Three words", [
            "<span class=\"pali\">bhaya</span>danger",
            "<span class=\"pali\">upaddava</span>peril",
            "<span class=\"pali\">upasagga</span>hazard",
        ]),
        ("The simile", [
            "a hut of reeds or grass",
            "a mansion, plastered and shuttered",
            "&mdash; every defense, and none of it helps",
        ]),
        ("The gap", [
            "&ldquo;the three things by which&hellip;&rdquo;",
            "not named here",
            "supplied by AN 3.2",
        ]),
        ("Cross-references", [
            "AN 3.2 &middot; next: what the three are",
            "AN 2.21 &middot; the two fools",
            "AN 2.77&ndash;86 &middot; enumerating synonyms",
        ]),
    ],
    further=[
        '<a href="%s/an3.1/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.2.html">AN 3.2 &middot; Characteristics</a> &mdash; next in this series, and '
        "the discourse that supplies the three things this one names without stating.",
        '<a href="an-2.21-31.html">AN 2.21&ndash;31 &middot; Fools</a> &mdash; the Twos&rsquo; version '
        "of the same pair, defined by what happens around a fault.",
        '<a href="an-2.310-479.html">AN 2.310&ndash;479 &middot; Greed, Abbreviated</a> &mdash; the '
        "last chapter of the Twos, where this series has just come from.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.2 — Lakkhaṇasutta
# --------------------------------------------------------------------------- #
page(
    2, "Lakkhaṇa", "Characteristics",
    meta_title="AN 3.2 — Characteristics | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Lakkhaṇasutta — "
        "a fool and an astute person are characterized by their deeds, for wisdom shines in "
        "its traces. The discourse that supplies what AN 3.1 named without stating. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "A statement of principle, the three things for each of the pair, and the "
                 "chapter&rsquo;s standing training instruction"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Comparable material appears in the Chinese Madhyama-āgama (T26); this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; brief and unambiguous, with one "
                       "sentence worth memorizing"),
    ],
    why=(
        "AN 3.1 told the listener to shun the three things by which a fool is known and did not say "
        "what they are. This discourse says: bad conduct by way of body, speech, and mind &mdash; and "
        "good conduct, for the astute. But its first line is the reason the discourse has its own "
        "name and its own page. <em>A fool is characterized by their deeds, and an astute person is "
        "characterized by their deeds, for wisdom shines in its traces.</em> That is a claim about "
        "how anyone can be known at all, and it settles a question the chapter would otherwise "
        "leave open."),
    guide=[
        ("The teaching in one sentence", [
            "You cannot see wisdom directly; you can see what it leaves behind, and that is what "
            "deeds are."]),
        ("Wisdom shines in its traces", [
            "The Pāli behind Sujato&rsquo;s rendering is <em>kammalakkhaṇo bālo, kammalakkhaṇo "
            "paṇḍito, apadānasobhinī paññā</em>. <em>Lakkhaṇa</em> is a mark or characteristic &mdash; "
            "the same word used of the marks of a great man, and of the three characteristics of "
            "existence. <em>Apadāna</em> is a track or a trace, what is left behind by something that "
            "has passed.",
            "So the claim is that wisdom is not itself visible and does not need to be. It is legible "
            "in its footprints. That is a genuinely useful epistemological point for a tradition "
            "which insists that people be evaluated: it says the evaluation is done on conduct, not "
            "on report, self-description, atmosphere, or the impression a person makes.",
            "It also cuts both ways, which is the part worth teaching. If wisdom shines in its traces "
            "then so does its absence, and a person cannot be foolish privately. The chapter has "
            "already said that all danger comes from the foolish; this discourse says that "
            "foolishness is always visible in what someone does, which is what makes the previous "
            "claim actionable rather than merely alarming."]),
        ("Body, speech, and mind", [
            "The three things turn out to be the standard threefold division of action: conduct by "
            "way of body, of speech, and of mind. Bad conduct in all three marks the fool; good "
            "conduct in all three marks the astute person.",
            "That the list includes mind is what keeps the discourse from being a simple behaviorism. "
            "Mental conduct is conduct: what a person cultivates in thought is on the list of deeds "
            "alongside what they do and say. The Threes will return to this division constantly, and "
            "it is the reason the collection can make claims about the inner life without abandoning "
            "the principle that people are known by their deeds. A thought is a deed.",
            "AN 3.3, the next discourse, makes exactly this explicit: a fool thinks poorly, speaks "
            "poorly, and acts poorly, and it is because they do so that the astute can recognize "
            "them."]),
        ("Reading it as a standard for judgment", [
            "Practically, this discourse is a rule for how to assess anyone, and it is a restrictive "
            "one. Not by what they say about themselves. Not by what others say about them. Not by "
            "the quality of their presence or the fluency of their teaching. By their deeds, of "
            "which speech is one kind.",
            "That is worth setting against AN 1.378&ndash;393 in the Ones, which listed sixteen things "
            "that inspire confidence in a monastic &mdash; including being handsome, well-presented, "
            "and from a good family. The two are not in conflict, but they answer different "
            "questions: what makes people trust someone, and what actually shows what someone is. "
            "Anyone teaching the first list should teach this discourse alongside it."]),
    ],
    terms=[
        ("lakkhaṇa",
         "&ldquo;characteristic, mark&rdquo; &mdash; the same word used of the marks of a great man "
         "and of the three characteristics of existence. Here, what a person is known by."),
        ("kamma",
         "&ldquo;deed, action&rdquo; &mdash; the thing a fool and an astute person are alike "
         "characterized by."),
        ("apadānasobhinī paññā",
         "&ldquo;wisdom shines in its traces&rdquo; &mdash; <em>apadāna</em> is a track left behind. "
         "Wisdom is not itself visible and is legible in its footprints."),
        ("kāya-, vacī-, manoduccarita",
         "bad conduct by way of body, speech, and mind &mdash; the three things by which a fool is "
         "known, with their positives for the astute."),
        ("manokamma",
         "&ldquo;mental action&rdquo; &mdash; the inclusion that keeps the discourse from being a "
         "simple behaviorism. A thought is a deed."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "How a person is known"),
        ("p", "&sect;1", "an3.2:1.1-1.5"),
        ("p", "&sect;2", "an3.2:2.1-2.4"),
        ("h3", "So you should train"),
        ("p", "&sect;3", "an3.2:3.1-3.3"),
    ],
    quiz=[
        {"q": "What are the three things by which a fool is known?",
         "opts": [
             "Poverty, illness, and low birth",
             "Bad conduct by way of body, speech, and mind",
             "Ignorance, doubt, and restlessness",
             "Greed, hate, and delusion"],
         "correct": 1,
         "expl": "The standard threefold division of action, supplying what AN 3.1 named without stating."},
        {"q": "What does <em>apadānasobhinī paññā</em> claim?",
         "opts": [
             "That wisdom is visible directly",
             "That wisdom shines in its traces &mdash; <em>apadāna</em> is a track left behind, so wisdom is legible in its footprints rather than in itself",
             "That wisdom is invisible and unknowable",
             "That wisdom is inherited"],
         "correct": 1,
         "expl": "A genuinely useful epistemological point for a tradition that insists people be evaluated."},
        {"q": "What does that principle rule out as a basis for evaluation?",
         "opts": [
             "Deeds",
             "Report, self-description, atmosphere, and the impression a person makes",
             "Speech",
             "Nothing"],
         "correct": 1,
         "expl": "The evaluation is done on conduct, of which speech is one kind."},
        {"q": "How does the principle cut both ways?",
         "opts": [
             "It does not",
             "If wisdom shines in its traces then so does its absence &mdash; a person cannot be foolish privately",
             "It applies only to the astute",
             "It applies only to monastics"],
         "correct": 1,
         "expl": "Which is what makes AN 3.1's claim actionable rather than merely alarming."},
        {"q": "Why does the inclusion of mind matter?",
         "opts": [
             "It makes the discourse a simple behaviorism",
             "It keeps the discourse from being a simple behaviorism &mdash; what a person cultivates in thought is on the list of deeds alongside what they do and say",
             "It restricts the teaching to meditators",
             "It contradicts the first line"],
         "correct": 1,
         "expl": "A thought is a deed, which is how the collection makes claims about the inner life without abandoning the principle that people are known by their deeds."},
        {"q": "How does AN 3.3 develop this?",
         "opts": [
             "By dropping the mental component",
             "By making it explicit &mdash; a fool thinks poorly, speaks poorly, and acts poorly, and it is because they do so that the astute can recognize them",
             "By turning to a different subject",
             "By adding a fourth thing"],
         "correct": 1,
         "expl": "The recognizability is the point of the next discourse."},
        {"q": "What is <em>lakkhaṇa</em> elsewhere used of?",
         "opts": [
             "Only of physical appearance",
             "The marks of a great man, and the three characteristics of existence",
             "Only of monastic offenses",
             "Only of meditation objects"],
         "correct": 1,
         "expl": "A mark or characteristic &mdash; here, what a person is known by."},
        {"q": "Which chapter of the Ones does the guide set this discourse against?",
         "opts": [
             "AN 1.378&ndash;393, the sixteen things that inspire confidence &mdash; including being handsome, well-presented, and from a good family",
             "AN 1.1&ndash;10 on the senses",
             "AN 1.170&ndash;187 on the one individual",
             "AN 1.296&ndash;305 on the recollections"],
         "correct": 0,
         "expl": "The two answer different questions: what makes people trust someone, and what actually shows what someone is."},
        {"q": "Are the two in conflict?",
         "opts": [
             "Yes, directly",
             "No &mdash; but anyone teaching the sixteen inspiring qualities should teach this discourse alongside them",
             "The guide does not say",
             "Only for monastics"],
         "correct": 1,
         "expl": "Different questions, both worth asking."},
        {"q": "What does the discourse&rsquo;s closing formula tell the listener?",
         "opts": [
             "To avoid fools",
             "To shun the three things by which a fool is known and undertake the three by which an astute person is known &mdash; the chapter&rsquo;s standing instruction",
             "To examine their own conduct daily",
             "To report fools to the Saṅgha"],
         "correct": 1,
         "expl": "Repeated across the chapter, and now with content attached."},
    ],
    marginalia=[
        ("The three", [
            "conduct by body",
            "conduct by speech",
            "conduct by mind",
            "&mdash; a thought is a deed",
        ]),
        ("The first line", [
            "<span class=\"pali\">lakkhaṇa</span>a mark",
            "<span class=\"pali\">apadāna</span>a track left behind",
            "&ldquo;wisdom shines in its traces&rdquo;",
        ]),
        ("What it rules out", [
            "self-description",
            "reputation",
            "presence and fluency",
        ]),
        ("Cross-references", [
            "AN 3.1 &middot; the gap this fills",
            "AN 3.3 &middot; next: recognizability",
            "AN 1.378&ndash;393 &middot; what inspires confidence",
        ]),
    ],
    further=[
        '<a href="%s/an3.2/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.3.html">AN 3.3 &middot; Thinking</a> &mdash; next in this series, where the '
        "recognizability of a fool is made the explicit subject.",
        '<a href="an-1.378-393.html">AN 1.378&ndash;393 &middot; Inspiring Qualities</a> &mdash; the '
        "sixteen things that make people trust a monastic, which this discourse is the necessary "
        "companion to.",
        '<a href="an-3.1.html">AN 3.1 &middot; Perils</a> &mdash; previous in this series, which names '
        "these three things without stating them.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.3 — Cintīsutta
# --------------------------------------------------------------------------- #
page(
    3, "Cintī", "Thinking",
    meta_title="AN 3.3 — Thinking | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Cintīsutta — the "
        "three characteristics, signs, and manifestations of a fool, and the argument that "
        "makes recognition possible at all. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "Two parallel passages, each running a small argument from the visible signs to "
                 "the possibility of recognition"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Comparable material appears in the Chinese Madhyama-āgama (T26); this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, with an argument in the "
                       "middle that is easy to read past"),
    ],
    why=(
        "AN 3.2 said wisdom shines in its traces. This discourse asks what follows if that were not "
        "so, and answers with a small counterfactual argument: <em>if a fool didn&rsquo;t think "
        "poorly, speak poorly, and act poorly, then how would the astute know of them?</em> It is one "
        "of the few places in the Threes where the reasoning is shown rather than the conclusion "
        "asserted, and what it establishes is the condition under which any of this chapter&rsquo;s "
        "advice can be followed at all."),
    guide=[
        ("The teaching in one sentence", [
            "A fool is recognizable because folly shows in thinking, speech, and action &mdash; and "
            "if it did not, nobody could be recognized as anything."]),
        ("Three words again", [
            "<em>Bālalakkhaṇāni, bālanimittāni, bālāpadānāni</em>: characteristics, signs, and "
            "manifestations of a fool. As at AN 3.1, three near-synonyms are stacked. "
            "<em>Nimitta</em> is the sign or feature by which something is picked out &mdash; the same "
            "word as the feature of beauty in the hindrances material. <em>Apadāna</em> is the trace "
            "or track from the previous discourse.",
            "The effect is to say that folly is visible under every description of visibility: as a "
            "characteristic, as a distinguishing sign, and as something left behind."]),
        ("The counterfactual", [
            "The middle of each passage does something the Threes rarely bother with. Having said "
            "that a fool thinks, speaks, and acts poorly, the discourse asks what would follow "
            "otherwise: <em>if a fool didn&rsquo;t do these things, then how would the astute know of "
            "them, &lsquo;this worthy one is a fool, an untrue person&rsquo;?</em> And then the "
            "positive: since a fool does do them, the astute do know.",
            "The argument is small but it is doing real work. It establishes that recognition is "
            "possible, and it establishes why &mdash; not because the astute have some special "
            "faculty for detecting folly, but because folly is the kind of thing that necessarily "
            "produces evidence. Nothing hidden is being read. The signs are simply there.",
            "That matters because the surrounding chapter is full of instructions that presuppose it. "
            "Shun what a fool does; keep good company; avoid bad friends; do not be taken in. Every "
            "one of those requires that a fool can in fact be identified, and this discourse is where "
            "the collection says so and gives its reason."]),
        ("The symmetry, and its limit", [
            "The second passage is the first with every term reversed: an astute person thinks well, "
            "speaks well, and acts well, and is recognizable for the same reason. The Threes state "
            "both directions as a matter of course.",
            "But the symmetry has a limit worth naming, because it affects how this discourse gets "
            "used. In both passages it is <em>the astute</em> who do the recognizing. The discourse "
            "does not claim that anyone can identify a fool, or that folly is obvious to everybody. "
            "It claims that folly produces signs and that those with judgment read them.",
            "That is a more modest and more accurate claim than it is usually taken for. A reader who "
            "comes away confident of their own ability to spot a fool has read the discourse as "
            "flattery. What it actually offers is a criterion &mdash; thinking, speech, action &mdash; "
            "and the observation that the criterion is applied by people who are themselves "
            "reliable."]),
        ("Thinking as the first item", [
            "The order is worth noticing: thinks poorly, speaks poorly, acts poorly. Thought comes "
            "first, and the discourse is named after it &mdash; <em>Cintī</em>, from "
            "<em>cinteti</em>, to think or ponder.",
            "That ordering runs through the collection. AN 1.56&ndash;57 said that mind precedes all "
            "things and the rest follows behind. AN 1.306&ndash;315 said that view shapes every deed "
            "undertaken in line with it. Here the same sequence appears as a description of how folly "
            "becomes visible: it begins where nobody can see it and arrives, in speech and action, "
            "where everybody can."]),
    ],
    terms=[
        ("cintī",
         "&ldquo;thinking, pondering&rdquo; &mdash; the discourse&rsquo;s name, and the first of the "
         "three places folly shows."),
        ("nimitta",
         "&ldquo;sign, feature&rdquo; &mdash; the mark by which something is picked out. The same "
         "word as the feature of beauty in the hindrances material."),
        ("apadāna",
         "&ldquo;trace, manifestation&rdquo; &mdash; carried over from AN 3.2, where wisdom was said "
         "to shine in its traces."),
        ("asappurisa / sappurisa",
         "&ldquo;untrue person&rdquo; and &ldquo;true person&rdquo; &mdash; what the astute conclude "
         "on seeing the signs. A recurring pair in the Threes."),
        ("paṇḍitā jānanti",
         "&ldquo;the astute know&rdquo; &mdash; the recognizing is done by those with judgment, not "
         "by everyone, which is the discourse&rsquo;s modest and easily overstated claim."),
    ],
    text_intro=(
        "The discourse in full, in two parallel passages. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "The signs of a fool"),
        ("p", "&sect;1", "an3.3:1.1-1.8"),
        ("h3", "The signs of an astute person"),
        ("p", "&sect;2", "an3.3:2.1-2.9"),
    ],
    quiz=[
        {"q": "In which three places does folly show, according to this discourse?",
         "opts": [
             "Wealth, health, and reputation",
             "Thinking, speech, and action",
             "Body, feeling, and perception",
             "Past, present, and future"],
         "correct": 1,
         "expl": "Thought comes first, and the discourse is named after it."},
        {"q": "What counterfactual does the discourse argue from?",
         "opts": [
             "If there were no fools at all",
             "If a fool didn&rsquo;t think, speak, and act poorly, then how would the astute know of them?",
             "If nobody spoke",
             "If the astute did not exist"],
         "correct": 1,
         "expl": "One of the few places in the Threes where the reasoning is shown rather than the conclusion asserted."},
        {"q": "What does that argument establish?",
         "opts": [
             "That the astute have a special faculty for detecting folly",
             "That recognition is possible, and why &mdash; because folly is the kind of thing that necessarily produces evidence",
             "That fools cannot be identified",
             "That recognition requires a teacher"],
         "correct": 1,
         "expl": "Nothing hidden is being read; the signs are simply there."},
        {"q": "Why does that matter for the rest of the chapter?",
         "opts": [
             "It does not",
             "Because the surrounding instructions &mdash; shun what a fool does, keep good company, avoid bad friends &mdash; all presuppose that a fool can in fact be identified",
             "Because it settles a doctrinal dispute",
             "Because it names the fools"],
         "correct": 1,
         "expl": "This is where the collection says so and gives its reason."},
        {"q": "Who does the recognizing, in both passages?",
         "opts": [
             "Anyone at all",
             "The astute &mdash; the discourse does not claim folly is obvious to everybody",
             "Only the Buddha",
             "Only senior monastics"],
         "correct": 1,
         "expl": "A more modest and more accurate claim than it is usually taken for."},
        {"q": "How has a reader misread the discourse if they come away confident of their own ability to spot a fool?",
         "opts": [
             "They have read it correctly",
             "They have read it as flattery &mdash; what it offers is a criterion, and the observation that the criterion is applied by people who are themselves reliable",
             "They have misread the Pāli",
             "They have skipped the second passage"],
         "correct": 1,
         "expl": "The claim is about signs and about who reads them."},
        {"q": "What are the three near-synonyms stacked at the head of each passage?",
         "opts": [
             "Characteristics, signs, and manifestations",
             "Body, speech, and mind",
             "Danger, peril, and hazard",
             "Greed, hate, and delusion"],
         "correct": 0,
         "expl": "Folly is visible under every description of visibility."},
        {"q": "What is <em>nimitta</em> elsewhere used of?",
         "opts": [
             "The feature of beauty, in the hindrances material",
             "The monastic code",
             "The four absorptions",
             "The stages of the path"],
         "correct": 0,
         "expl": "The mark by which something is picked out."},
        {"q": "Which earlier discourses share this ordering of thought before speech and action?",
         "opts": [
             "AN 1.56&ndash;57, that mind precedes all things, and AN 1.306&ndash;315, that view shapes every deed undertaken in line with it",
             "AN 1.1&ndash;10 on the senses",
             "AN 2.42&ndash;51 on assemblies",
             "AN 2.141&ndash;150 on giving"],
         "correct": 0,
         "expl": "The sequence runs through the collection."},
        {"q": "How does the guide describe folly&rsquo;s journey in that ordering?",
         "opts": [
             "It stays hidden",
             "It begins where nobody can see it and arrives, in speech and action, where everybody can",
             "It appears first in action",
             "It is visible only to the person themselves"],
         "correct": 1,
         "expl": "Which is what makes the criterion usable."},
    ],
    marginalia=[
        ("Three signs", [
            "thinks poorly",
            "speaks poorly",
            "acts poorly",
            "&mdash; in that order",
        ]),
        ("The argument", [
            "if a fool didn&rsquo;t &hellip;",
            "how would the astute know?",
            "but since they do, the astute do",
        ]),
        ("The limit", [
            "<span class=\"pali\">paṇḍitā jānanti</span>the astute know",
            "not: anyone can tell",
        ]),
        ("Cross-references", [
            "AN 3.2 &middot; wisdom shines in its traces",
            "AN 1.56&ndash;57 &middot; mind goes first",
            "AN 3.4 &middot; next: mistakes",
        ]),
    ],
    further=[
        '<a href="%s/an3.3/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.4.html">AN 3.4 &middot; Mistakes</a> &mdash; next in this series, which narrows '
        "the criterion to what a person does about a fault.",
        '<a href="an-1.51-60.html">AN 1.51&ndash;60 &middot; A Finger-Snap</a> &mdash; AN '
        "1.56&ndash;57, that mind precedes all things and the rest follows behind.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.4 — Accayasutta
# --------------------------------------------------------------------------- #
page(
    4, "Accaya", "Mistakes",
    meta_title="AN 3.4 — Mistakes | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Accayasutta — a fool "
        "is known by three things around a mistake: not recognizing it, not dealing with it, "
        "and not accepting someone else's confession. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "Three things for the fool, the same three inverted for the astute, and the "
                 "chapter&rsquo;s standing instruction"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The material on acknowledging and accepting a fault is well "
                              "represented in the Chinese Āgamas and underlies the confession "
                              "procedure of every Vinaya tradition; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; four sentences, and among the most "
                       "practically useful in the collection"),
    ],
    why=(
        "The chapter has said that folly shows in deeds and that deeds are what a person is known by. "
        "This discourse narrows the criterion to a single situation, and it is the one where "
        "character is least concealable: what a person does when something has gone wrong. Three "
        "things, and the third is the one that catches most people &mdash; not what you do about your "
        "own mistake, but what you do when somebody brings theirs to you."),
    guide=[
        ("The teaching in one sentence", [
            "A fool cannot see their own mistake, cannot handle it once seen, and cannot receive "
            "someone else&rsquo;s acknowledgment properly."]),
        ("Three separate failures", [
            "The three are sequential and independent, and separating them is the discourse&rsquo;s "
            "whole contribution. First: recognizing that one has made a mistake at all. Second: "
            "having recognized it, dealing with it properly &mdash; <em>yathādhammaṁ paṭikaroti</em>, "
            "making amends in accordance with the teaching. Third: when someone else confesses a "
            "mistake to them, accepting it properly.",
            "A person can pass the first and fail the second: they know perfectly well what they did "
            "and do nothing about it. A person can pass the first two and fail the third, and this is "
            "the common case &mdash; scrupulous about their own faults and impossible to apologize "
            "to. The discourse counts all three as marks of the same condition."]),
        ("The third one", [
            "Accepting a confession properly is a skill, and it is almost never taught as one. The "
            "failures are recognizable: receiving an apology with a lecture, receiving it with visible "
            "reluctance, receiving it while making clear that the matter is not closed, or refusing to "
            "receive it at all on the grounds that the offense was too serious for words.",
            "The Vinaya treats this as a formal matter, which is a good indication of how seriously "
            "the tradition took it. Confession between monastics is a procedure with two parties, and "
            "the receiving party has obligations. A community in which faults are confessed and not "
            "accepted is not a community that has solved the problem of faults; it has moved the "
            "problem.",
            "AN 2.21 in the Twos gave the same pair as the two fools and the two astute &mdash; not "
            "recognizing one&rsquo;s own mistake, and not accepting another&rsquo;s confession. This "
            "discourse adds the middle term, which is the one that turns recognition into something "
            "that has actually happened."]),
        ("Why this is the sharpest test in the chapter", [
            "The other discourses of this chapter name conduct in general: bad by body, speech, and "
            "mind; unskillful, blameworthy, hurtful. Those are true and hard to use, because almost "
            "nobody believes their own conduct falls under them.",
            "This one is usable because it names a specific and dateable event. Everyone has made a "
            "mistake recently, and everyone has recently had someone bring a mistake to them. The "
            "discourse can be checked against a particular week rather than against a self-image, and "
            "that is the difference between a criterion and a compliment."]),
    ],
    terms=[
        ("accaya",
         "&ldquo;mistake, transgression, fault&rdquo; &mdash; literally an overstepping. The word "
         "used across the canon for what is confessed."),
        ("accayaṁ accayato passati",
         "&ldquo;recognizes a mistake as a mistake&rdquo; &mdash; the first of the three, and the one "
         "the others depend on."),
        ("yathādhammaṁ paṭikaroti",
         "&ldquo;deals with it properly&rdquo; &mdash; makes amends in accordance with the teaching. "
         "The middle term this discourse adds to the pair given at AN 2.21."),
        ("paṭiggaṇhāti",
         "&ldquo;accepts&rdquo; &mdash; what the astute person does with someone else&rsquo;s "
         "confession, and what the Vinaya treats as a formal obligation of the receiving party."),
        ("desanā",
         "&ldquo;confession, declaration&rdquo; &mdash; the monastic procedure this discourse "
         "underlies, which has two parties and not one."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three things by which a fool is known"),
        ("p", "&sect;1", "an3.4:1.1-1.4"),
        ("h3", "And an astute person"),
        ("p", "&sect;2", "an3.4:2.1-2.5"),
    ],
    quiz=[
        {"q": "What are the three things by which a fool is known here?",
         "opts": [
             "Bad conduct of body, speech, and mind",
             "Not recognizing their own mistake; not dealing with it properly once recognized; and not accepting someone else&rsquo;s confession properly",
             "Greed, hate, and delusion",
             "Poor thinking, speech, and action"],
         "correct": 1,
         "expl": "Three sequential and independent failures around a single situation."},
        {"q": "Why does the guide say separating the three is the discourse&rsquo;s whole contribution?",
         "opts": [
             "Because they occur at different ages",
             "Because a person can pass one and fail another &mdash; knowing perfectly well what they did and doing nothing, or being scrupulous about their own faults and impossible to apologize to",
             "Because only the first matters",
             "Because they apply to different people"],
         "correct": 1,
         "expl": "The discourse counts all three as marks of the same condition."},
        {"q": "Which of the three does the guide call the common case?",
         "opts": [
             "The first",
             "The second",
             "The third &mdash; scrupulous about one&rsquo;s own faults and impossible to apologize to",
             "None is more common"],
         "correct": 2,
         "expl": "Not what you do about your own mistake, but what you do when somebody brings theirs to you."},
        {"q": "What does accepting a confession badly look like?",
         "opts": [
             "Receiving it with a lecture, with visible reluctance, while making clear the matter is not closed, or refusing on the grounds that the offense was too serious for words",
             "Receiving it silently",
             "Receiving it in private",
             "Receiving it immediately"],
         "correct": 0,
         "expl": "A skill, and almost never taught as one."},
        {"q": "How does the Vinaya treat this?",
         "opts": [
             "As a private matter",
             "As a formal matter &mdash; confession between monastics is a procedure with two parties, and the receiving party has obligations",
             "As optional",
             "It does not address it"],
         "correct": 1,
         "expl": "A good indication of how seriously the tradition took it."},
        {"q": "What does the guide say about a community where faults are confessed and not accepted?",
         "opts": [
             "It has solved the problem of faults",
             "It has not solved the problem; it has moved it",
             "It is functioning normally",
             "It should confess less"],
         "correct": 1,
         "expl": "Which is why the receiving party's conduct is named as a mark of folly."},
        {"q": "What did AN 2.21 in the Twos give?",
         "opts": [
             "All three of these",
             "The first and third as the two fools and the two astute &mdash; this discourse adds the middle term",
             "None of these",
             "A different list entirely"],
         "correct": 1,
         "expl": "The middle term is the one that turns recognition into something that has actually happened."},
        {"q": "Why does the guide call the other discourses of this chapter hard to use?",
         "opts": [
             "They are too long",
             "They name conduct in general &mdash; bad, unskillful, blameworthy, hurtful &mdash; and almost nobody believes their own conduct falls under them",
             "They are in Pāli",
             "They concern only monastics"],
         "correct": 1,
         "expl": "True, and hard to check oneself against."},
        {"q": "What makes this discourse usable by comparison?",
         "opts": [
             "It is shorter",
             "It names a specific and dateable event &mdash; everyone has recently made a mistake and recently had someone bring one to them",
             "It gives a simile",
             "It names a disciple"],
         "correct": 1,
         "expl": "It can be checked against a particular week rather than against a self-image."},
        {"q": "What does the guide call that difference?",
         "opts": [
             "The difference between a criterion and a compliment",
             "The difference between theory and practice",
             "The difference between lay and monastic",
             "The difference between Pāli and English"],
         "correct": 0,
         "expl": "A criterion is something a claim can fail."},
    ],
    marginalia=[
        ("Three failures", [
            "not seeing the mistake",
            "seeing and not dealing with it",
            "not accepting another&rsquo;s confession",
        ]),
        ("The third one", [
            "receiving with a lecture",
            "receiving reluctantly",
            "refusing on grounds of gravity",
        ]),
        ("Why it is usable", [
            "a dateable event",
            "checkable against a week",
            "not against a self-image",
        ]),
        ("Cross-references", [
            "AN 2.21 &middot; the same, minus the middle",
            "AN 2.11&ndash;20 &middot; both sides of a dispute",
            "AN 3.5 &middot; next: questions",
        ]),
    ],
    further=[
        '<a href="%s/an3.4/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.11-20.html">AN 2.11&ndash;20 &middot; Disciplinary Issues</a> &mdash; AN 2.15, '
        "where both parties to a dispute reach &ldquo;the mistake is mine alone,&rdquo; which is what "
        "this discourse&rsquo;s three abilities make possible.",
        '<a href="an-2.21-31.html">AN 2.21&ndash;31 &middot; Fools</a> &mdash; the Twos&rsquo; version, '
        "with the first and third of these three and without the middle.",
        '<a href="an-3.5.html">AN 3.5 &middot; Irrational</a> &mdash; next in this series, applying '
        "the same test to how a person asks and answers a question.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.5 — Ayonisosutta
# --------------------------------------------------------------------------- #
page(
    5, "Ayoniso", "Irrational",
    meta_title="AN 3.5 — Irrational | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ayonisosutta — a "
        "fool is known by how they ask a question, how they answer one, and whether they can "
        "agree with a good answer given by someone else. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "Three things for the fool, inverted for the astute, and the standing instruction"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Material on questioning and answering well is found across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, and the most directly "
                       "pedagogical discourse in the chapter"),
    ],
    why=(
        "AN 3.4 tested a person by what they do about a mistake. This one tests them by what they do "
        "in a conversation, and the three things it names are the three moves available in any "
        "discussion: asking, answering, and responding to somebody else&rsquo;s answer. The third is "
        "again the one that catches people, and it is described with unusual precision &mdash; the "
        "fool disagrees with a rational answer <em>given with well-rounded, coherent, and relevant "
        "words and phrases</em>. The quality of the answer is stipulated. The disagreement is not "
        "about the answer."),
    guide=[
        ("The teaching in one sentence", [
            "A fool asks badly, answers badly, and cannot assent to a good answer from someone else."]),
        ("Three moves in a conversation", [
            "The Pāli hinge is <em>yoniso</em> and <em>ayoniso</em> &mdash; rationally and "
            "irrationally, the same pair that runs through the whole collection as the quality of "
            "attention. Here it is applied to speech: a question can be put rationally or not, and an "
            "answer can be given rationally or not.",
            "That connection is worth drawing. The collection has consistently treated "
            "<em>yoniso manasikāra</em> as the hinge on which everything turns &mdash; it feeds the "
            "hindrances or starves them, it produces right view or wrong view. This discourse says the "
            "same quality is visible in how a person conducts a discussion. Asking a question badly is "
            "not a social failing; it is attention going wrong, in public."]),
        ("What a bad question is", [
            "The discourse does not define it, and the omission is worth thinking about rather than "
            "filling in confidently. But the surrounding material suggests the shape. A question asked "
            "<em>ayoniso</em> is one that does not go to the source of the matter &mdash; that takes "
            "the appearance of a thing at face value, or that is not really asking.",
            "Anyone who teaches will recognize the second category. A question can be a challenge in "
            "the grammar of a question, or a demonstration of what the asker already knows, or a "
            "request for reassurance. None of these are asking, and none of them can be answered, "
            "which is why the discourse pairs the failure with the inability to accept an answer."]),
        ("The stipulated answer", [
            "The third item is the precise one. When someone else answers a question rationally "
            "&mdash; and the discourse specifies the quality: with <em>well-rounded, coherent, and "
            "relevant words and phrases</em> &mdash; the fool disagrees with it.",
            "By stipulating that the answer is good, the discourse removes the obvious defense. The "
            "disagreement is not a judgment about the answer&rsquo;s merit, because the merit has been "
            "settled by the terms of the case. What is being described is a person who cannot assent "
            "&mdash; for whom agreement with another&rsquo;s answer is not an available move.",
            "The astute person is defined by the inversion: they agree with it. That is a low bar "
            "stated as a mark of wisdom, and it is worth letting the lowness of it register. The "
            "capacity to say <em>yes, that is right</em> about somebody else&rsquo;s answer is named "
            "here, in a chapter about what distinguishes the wise from the foolish, as one of the "
            "three marks."]),
        ("For a classroom", [
            "This is the discourse of the chapter most directly usable by anyone who teaches. Its "
            "three items map onto three observable behaviors, and a teacher who watches for them will "
            "learn more about a room than from any amount of assessment: how people ask, how they "
            "answer, and what happens in the room when somebody else says something correct.",
            "It pairs naturally with AN 2.47 in the Twos, on the assembly educated in questioning "
            "rather than in fancy talk, where the mark of a good assembly was that its members "
            "questioned and examined each other afterward &mdash; <em>why does it say this? what does "
            "that mean?</em> This discourse is the individual-level version of the same test."]),
    ],
    terms=[
        ("yoniso / ayoniso",
         "&ldquo;rationally&rdquo; and &ldquo;irrationally&rdquo; &mdash; <em>yoni</em> is a womb or "
         "source, so: going to the origin of a thing, or not. The collection&rsquo;s standing term for "
         "the quality of attention, applied here to speech."),
        ("pañhaṁ pucchati",
         "&ldquo;asks a question&rdquo; &mdash; the first of the three moves, and one that can be done "
         "rationally or not."),
        ("pañhaṁ vissajjeti",
         "&ldquo;answers a question&rdquo; &mdash; the second move."),
        ("pariyāgatehi padabyañjanehi",
         "&ldquo;with well-rounded, coherent, and relevant words and phrases&rdquo; &mdash; the "
         "stipulated quality of the answer the fool disagrees with, which removes the obvious defense."),
        ("nābbhanumodati",
         "&ldquo;does not agree, does not approve&rdquo; &mdash; the fool&rsquo;s response to a good "
         "answer. The astute person&rsquo;s assent is named as one of the three marks of wisdom."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three things by which a fool is known"),
        ("p", "&sect;1", "an3.5:1.1-1.4"),
        ("h3", "And an astute person"),
        ("p", "&sect;2", "an3.5:2.1-2.5"),
    ],
    quiz=[
        {"q": "Which three moves does this discourse test a person by?",
         "opts": [
             "Reading, writing, and reciting",
             "Asking a question, answering a question, and responding to somebody else&rsquo;s answer",
             "Body, speech, and mind",
             "Giving, receiving, and sharing"],
         "correct": 1,
         "expl": "The three moves available in any discussion."},
        {"q": "What Pāli pair is the hinge of the discourse?",
         "opts": [
             "<em>Kusala</em> and <em>akusala</em>",
             "<em>Yoniso</em> and <em>ayoniso</em> &mdash; rationally and irrationally, the collection&rsquo;s standing term for the quality of attention",
             "<em>Sati</em> and <em>sampajañña</em>",
             "<em>Samatha</em> and <em>vipassanā</em>"],
         "correct": 1,
         "expl": "Applied here to speech rather than to attention alone."},
        {"q": "What does that connection imply about asking a question badly?",
         "opts": [
             "That it is a social failing",
             "That it is attention going wrong, in public",
             "That it is unimportant",
             "That it can be corrected by etiquette"],
         "correct": 1,
         "expl": "The same quality that feeds or starves the hindrances is visible in how a person conducts a discussion."},
        {"q": "What shape does the guide suggest for a question asked <em>ayoniso</em>?",
         "opts": [
             "One that is too long",
             "One that does not go to the source of the matter &mdash; taking a thing at face value, or not really asking at all",
             "One asked by a layperson",
             "One asked in public"],
         "correct": 1,
         "expl": "The discourse does not define it, and the omission is worth thinking about rather than filling in confidently."},
        {"q": "Which forms of not-really-asking does the guide name?",
         "opts": [
             "A challenge in the grammar of a question, a demonstration of what the asker already knows, or a request for reassurance",
             "A question asked twice",
             "A question asked in writing",
             "A question about the Vinaya"],
         "correct": 0,
         "expl": "None of these can be answered, which is why the failure pairs with the inability to accept an answer."},
        {"q": "What does the discourse stipulate about the answer the fool disagrees with?",
         "opts": [
             "That it is brief",
             "That it is given rationally, with well-rounded, coherent, and relevant words and phrases",
             "That it is given by a monastic",
             "That it is written down"],
         "correct": 1,
         "expl": "The quality of the answer is settled by the terms of the case."},
        {"q": "What does that stipulation remove?",
         "opts": [
             "The need for the astute person",
             "The obvious defense &mdash; the disagreement cannot be a judgment about the answer&rsquo;s merit",
             "The relevance of the question",
             "The role of attention"],
         "correct": 1,
         "expl": "What is described is a person for whom agreement with another's answer is not an available move."},
        {"q": "How is the astute person defined in the third item?",
         "opts": [
             "By answering better",
             "By agreeing with the good answer &mdash; a low bar stated as a mark of wisdom",
             "By remaining silent",
             "By asking a further question"],
         "correct": 1,
         "expl": "Worth letting the lowness of the bar register."},
        {"q": "Why is this the chapter&rsquo;s most usable discourse for a teacher?",
         "opts": [
             "Because it is shortest",
             "Because its three items map onto three observable behaviors &mdash; how people ask, how they answer, and what happens when somebody else says something correct",
             "Because it names a disciple",
             "Because it gives a simile"],
         "correct": 1,
         "expl": "More informative about a room than any amount of assessment."},
        {"q": "Which discourse of the Twos does it pair with?",
         "opts": [
             "AN 2.47, on the assembly educated in questioning rather than in fancy talk",
             "AN 2.1, on judicial punishment",
             "AN 2.33, on repaying parents",
             "AN 2.141, on giving"],
         "correct": 0,
         "expl": "This discourse is the individual-level version of the same test."},
    ],
    marginalia=[
        ("Three moves", [
            "how you ask",
            "how you answer",
            "what you do with a good answer",
        ]),
        ("The stipulation", [
            "&ldquo;well-rounded, coherent,",
            "and relevant words and phrases&rdquo;",
            "&mdash; the merit is settled",
        ]),
        ("The low bar", [
            "the astute person agrees",
            "&mdash; named as a mark of wisdom",
        ]),
        ("Cross-references", [
            "AN 2.42&ndash;51 &middot; the same test, for a room",
            "AN 1.11&ndash;20 &middot; where <em>yoniso</em> first turns",
            "AN 3.6 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.5/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.42-51.html">AN 2.42&ndash;51 &middot; Assemblies</a> &mdash; AN 2.47, where the '
        "same test is applied to a whole room and the two questions worth putting on a wall are named.",
        '<a href="an-1.11-20.html">AN 1.11&ndash;20 &middot; Giving Up the Hindrances</a> &mdash; '
        "where rational and irrational application of mind first appears as the hinge everything "
        "turns on.",
        '<a href="an-3.6.html">AN 3.6 &middot; Unskillful</a> &mdash; next in this series.',
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.6–3.8 — Akusala, Sāvajja, Sabyābajjha
# --------------------------------------------------------------------------- #
_ABBREV_NOTE = (
    "The Pāli abbreviates this discourse against the ones before it, writing out only the "
    "term that changes and marking the rest with an ellipsis, which Sujato preserves. Every "
    "word is present; what is compressed is the repetition. Translation: Bhikkhu Sujato "
    "(CC0, SuttaCentral).")

page(
    6, "Akusala", "Unskillful",
    meta_title="AN 3.6 — Unskillful | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Akusalasutta — the "
        "same three things by which a fool is known, now under the term unskillful, and what "
        "changes when the predicate changes. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "The chapter&rsquo;s standing template with one term substituted"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "Comparable material appears in the Chinese Madhyama-āgama (T26); this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a substitution, and worth one "
                       "observation"),
    ],
    why=(
        "Three discourses in a row now run the same template with one word changed: unskillful deeds, "
        "then blameworthy deeds, then hurtful deeds, each by way of body, speech, and mind. Nothing "
        "new is asserted. What the sequence does is show that the chapter&rsquo;s criterion survives "
        "translation into every register in which conduct can be judged, and this first substitution "
        "is where that becomes visible."),
    guide=[
        ("The teaching in one sentence", [
            "A fool is known by unskillful deeds of body, speech, and mind; an astute person by "
            "skillful ones."]),
        ("What <em>akusala</em> means, and does not", [
            "<em>Kusala</em> and <em>akusala</em> are usually Englished skillful and unskillful, and "
            "the choice is deliberate on the part of most modern translators. The word&rsquo;s range "
            "covers wholesome, healthy, proficient, and clever; it is not primarily a moral term in "
            "the sense of permitted and forbidden.",
            "That matters here. AN 3.2 gave the same three things as <em>bad conduct</em>, which is a "
            "moral description. This discourse gives them as <em>unskillful deeds</em>, which is a "
            "description of competence. The conduct has not changed. What has changed is the frame in "
            "which it is being judged, and the collection is showing that both frames pick out the "
            "same acts.",
            "Anyone teaching this material to students who bristle at moral language has a use for "
            "this discourse. The chapter is not less demanding under the skill description &mdash; it "
            "is the same three items &mdash; but a person who will not accept &ldquo;bad&rdquo; will "
            "often accept &ldquo;this does not work.&rdquo;"]),
        ("Three discourses, one move", [
            "AN 3.6, 3.7, and 3.8 substitute <em>unskillful</em>, <em>blameworthy</em>, and "
            "<em>hurtful</em> into the same sentence. Read as a set, they cover three distinct kinds "
            "of judgment: whether an act works, whether it can be criticized, and whether it does "
            "damage.",
            "These are separable, and the collection knows it. An act can be blameless and still "
            "unskillful; an act can be skillful in the narrow sense and still hurtful. By running the "
            "same three items through all three predicates, the chapter claims that in the case of "
            "bad conduct by body, speech, and mind, the three judgments coincide. That is a claim, not "
            "a tautology, and it is the reason three discourses exist where one would have "
            "served."]),
    ],
    terms=[
        ("kusala / akusala",
         "&ldquo;skillful&rdquo; and &ldquo;unskillful&rdquo; &mdash; a range covering wholesome, "
         "healthy, proficient, and clever. Not primarily a term of permission and prohibition."),
        ("duccarita",
         "&ldquo;bad conduct&rdquo; &mdash; the moral description AN 3.2 used for the same three "
         "items."),
        ("sāvajja",
         "&ldquo;blameworthy&rdquo; &mdash; the predicate of AN 3.7: whether an act can be criticized."),
        ("sabyābajjha",
         "&ldquo;hurtful&rdquo; &mdash; the predicate of AN 3.8: whether an act does damage."),
        ("kāya-, vacī-, manokamma",
         "deeds by way of body, speech, and mind &mdash; the three items that stay fixed while the "
         "predicates change around them."),
    ],
    text_intro=_ABBREV_NOTE,
    text=[
        ("h3", "Unskillful deeds"),
        ("p", "&sect;1", "an3.6:1.1-1.4"),
        ("p", "&sect;2", "an3.6:2.1-2.5"),
    ],
    quiz=[
        {"q": "What changes between AN 3.2 and AN 3.6?",
         "opts": [
             "The three items",
             "The predicate &mdash; the same three items are given as <em>bad conduct</em> there and as <em>unskillful deeds</em> here",
             "The speaker",
             "The setting"],
         "correct": 1,
         "expl": "The conduct has not changed; the frame in which it is judged has."},
        {"q": "What range does <em>kusala</em> cover?",
         "opts": [
             "Only what is permitted",
             "Wholesome, healthy, proficient, and clever &mdash; not primarily a term of permission and prohibition",
             "Only ritual purity",
             "Only meditative skill"],
         "correct": 1,
         "expl": "Which is why most modern translators choose &ldquo;skillful.&rdquo;"},
        {"q": "How does the guide say this is useful in teaching?",
         "opts": [
             "It is not useful",
             "For students who bristle at moral language &mdash; a person who will not accept &ldquo;bad&rdquo; will often accept &ldquo;this does not work&rdquo;",
             "For memorization",
             "For monastic discipline only"],
         "correct": 1,
         "expl": "The chapter is not less demanding under the skill description; it is the same three items."},
        {"q": "Which three predicates do AN 3.6&ndash;3.8 substitute?",
         "opts": [
             "Unskillful, blameworthy, and hurtful",
             "Good, bad, and neutral",
             "Past, present, and future",
             "Bodily, verbal, and mental"],
         "correct": 0,
         "expl": "Whether an act works, whether it can be criticized, and whether it does damage."},
        {"q": "Are those three judgments separable in general?",
         "opts": [
             "No, they always coincide",
             "Yes &mdash; an act can be blameless and still unskillful, or skillful in the narrow sense and still hurtful",
             "Only for monastics",
             "The collection does not distinguish them"],
         "correct": 1,
         "expl": "Which is what makes the chapter's claim a claim."},
        {"q": "What do the three discourses together claim?",
         "opts": [
             "That the three judgments are meaningless",
             "That in the case of bad conduct by body, speech, and mind, the three judgments coincide",
             "That only one of the three matters",
             "That the judgments contradict each other"],
         "correct": 1,
         "expl": "A claim, not a tautology &mdash; and the reason three discourses exist where one would have served."},
        {"q": "How is this discourse written in Pāli?",
         "opts": [
             "In full",
             "Abbreviated against the ones before it, writing out only the term that changes",
             "In verse",
             "As a dialogue"],
         "correct": 1,
         "expl": "Every word is present; what is compressed is the repetition."},
        {"q": "What stays fixed across AN 3.6&ndash;3.8?",
         "opts": [
             "The predicate",
             "The three items &mdash; deeds by way of body, speech, and mind",
             "The setting",
             "Nothing"],
         "correct": 1,
         "expl": "The predicates change around them."},
        {"q": "What is <em>sāvajja</em>?",
         "opts": [
             "&ldquo;Blameworthy&rdquo; &mdash; whether an act can be criticized",
             "&ldquo;Hurtful&rdquo;",
             "&ldquo;Unskillful&rdquo;",
             "&ldquo;Unwholesome&rdquo;"],
         "correct": 0,
         "expl": "The predicate of AN 3.7."},
        {"q": "What is <em>sabyābajjha</em>?",
         "opts": [
             "&ldquo;Hurtful&rdquo; &mdash; whether an act does damage",
             "&ldquo;Blameworthy&rdquo;",
             "&ldquo;Skillful&rdquo;",
             "&ldquo;Bad&rdquo;"],
         "correct": 0,
         "expl": "The predicate of AN 3.8."},
    ],
    marginalia=[
        ("One template", [
            "deeds by body",
            "deeds by speech",
            "deeds by mind",
            "&mdash; fixed across three discourses",
        ]),
        ("Three predicates", [
            "<span class=\"pali\">akusala</span>does it work",
            "<span class=\"pali\">sāvajja</span>can it be criticized",
            "<span class=\"pali\">sabyābajjha</span>does it damage",
        ]),
        ("The claim", [
            "the three judgments are separable",
            "here they coincide",
            "&mdash; not a tautology",
        ]),
        ("Cross-references", [
            "AN 3.2 &middot; the same three, as bad conduct",
            "AN 3.7 &middot; next: blameworthy",
            "AN 2.230&ndash;279 &middot; predicates stacked",
        ]),
    ],
    further=[
        '<a href="%s/an3.6/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.7.html">AN 3.7 &middot; Blameworthy</a> &mdash; next in this series, the second '
        "of the three substitutions.",
        '<a href="an-2.230-279.html">AN 2.230&ndash;279 &middot; The Unskillful, Abbreviated</a> '
        "&mdash; the same predicates stacked in the Twos, where the guide separates what each of them "
        "actually judges.",
    ],
)


page(
    7, "Sāvajja", "Blameworthy",
    meta_title="AN 3.7 — Blameworthy | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sāvajjasutta — the "
        "shortest discourse in the first chapter of the Threes, and a good place to look at "
        "what canonical abbreviation actually does. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "The standing template, abbreviated to a single sentence with both halves folded "
                 "into it"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "Comparable material appears in the Chinese Madhyama-āgama (T26); this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; thirty-five words, and one point "
                       "about how the canon is written"),
    ],
    why=(
        "This is the shortest discourse in the chapter and one of the shortest in the Threes: a single "
        "sentence, with the astute person&rsquo;s half folded into the same line as the fool&rsquo;s "
        "and two ellipses doing the rest of the work. There is nothing in it that AN 3.6 has not "
        "already established. It is worth a page because it shows, more clearly than a long discourse "
        "can, what the canon looks like at the point where abbreviation takes over completely."),
    guide=[
        ("The teaching in one sentence", [
            "A fool is known by blameworthy deeds of body, speech, and mind; an astute person by "
            "blameless ones."]),
        ("<em>Sāvajja</em>: with fault", [
            "The word is <em>sa-</em> plus <em>vajja</em>, with-fault; its opposite <em>anavajja</em> "
            "is without-fault. <em>Vajja</em> is the same word that opened this nipāta&rsquo;s "
            "neighbor at AN 2.1, where two kinds of fault were distinguished by whether their "
            "consequences fall in this life or the next.",
            "What the predicate adds to <em>akusala</em> is the dimension of judgment. An unskillful "
            "act fails on its own terms; a blameworthy act is one that can be held against you. Those "
            "are different, and the canon elsewhere is careful about the difference &mdash; AN 3.65 "
            "lists <em>blameworthy</em> and <em>criticized by sensible people</em> as separate marks "
            "in the test it gives the Kālāmas, alongside <em>unskillful</em> and <em>leads to "
            "harm</em>. Four marks, four distinct questions.",
            "Reading this one-line discourse against that four-part test is the most useful thing to "
            "do with it. The Kālāma test asks all four at once. This chapter asks them one at a time, "
            "in three consecutive discourses, and gets the same answer each time."]),
        ("What the abbreviation looks like", [
            "The Pāli writes: <em>a fool is known by three things &mdash; what three? &mdash; "
            "blameworthy deeds by way of body, speech, and mind &hellip; an astute person is known by "
            "blameless deeds by way of body, speech, and mind &hellip;</em>. Two ellipses, and the "
            "discourse is over.",
            "What has been elided is the closing formula of each half (<em>these are the three things "
            "by which&hellip;</em>) and the training instruction. A reciter restores them from the "
            "pattern; a reader without the pattern is looking at a fragment.",
            "This series prints the abbreviation as the canon transmits it rather than silently "
            "unrolling it, which is the same decision made throughout the Ones and Twos. The cost is "
            "that a discourse like this reads as incomplete. The benefit is that the reader can see "
            "how much of this literature is stored rather than written, and can count the discourses "
            "the way the tradition did."]),
    ],
    terms=[
        ("sāvajja / anavajja",
         "&ldquo;blameworthy&rdquo; and &ldquo;blameless&rdquo; &mdash; literally with-fault and "
         "without-fault, from <em>vajja</em>."),
        ("vajja",
         "&ldquo;fault&rdquo; &mdash; the same word AN 2.1 divided into the fault apparent in this "
         "life and the fault to do with lives to come."),
        ("viññugarahita",
         "&ldquo;criticized by sensible people&rdquo; &mdash; a separate mark from <em>sāvajja</em> in "
         "the four-part test AN 3.65 gives the Kālāmas."),
        ("peyyāla",
         "the abbreviation convention. Here it removes the closing formula of each half and the "
         "training instruction, leaving a single sentence."),
        ("kāya-, vacī-, manokamma",
         "deeds by way of body, speech, and mind &mdash; unchanged from the discourses on either side."),
    ],
    text_intro=_ABBREV_NOTE,
    text=[
        ("h3", "Blameworthy deeds"),
        ("p", "&sect;1", "an3.7:1.1-1.3"),
    ],
    quiz=[
        {"q": "What does <em>sāvajja</em> literally mean?",
         "opts": [
             "&ldquo;With-fault&rdquo; &mdash; <em>sa-</em> plus <em>vajja</em>, against <em>anavajja</em>, without-fault",
             "&ldquo;Unskillful&rdquo;",
             "&ldquo;Hurtful&rdquo;",
             "&ldquo;Forbidden&rdquo;"],
         "correct": 0,
         "expl": "The same <em>vajja</em> that AN 2.1 divided into two kinds of fault."},
        {"q": "What does the predicate add to <em>akusala</em>?",
         "opts": [
             "Nothing",
             "The dimension of judgment &mdash; an unskillful act fails on its own terms; a blameworthy act is one that can be held against you",
             "A rebirth destination",
             "A monastic penalty"],
         "correct": 1,
         "expl": "Different questions, and the canon is careful about the difference."},
        {"q": "Which four marks does AN 3.65 give the Kālāmas?",
         "opts": [
             "Unskillful, blameworthy, criticized by sensible people, and leading to harm when undertaken",
             "Bodily, verbal, mental, and habitual",
             "Past, present, future, and timeless",
             "Greed, hate, delusion, and conceit"],
         "correct": 0,
         "expl": "Four marks, four distinct questions &mdash; asked all at once there, one at a time here."},
        {"q": "How does this chapter differ from the Kālāma test in method?",
         "opts": [
             "It asks the same questions one at a time, in three consecutive discourses, and gets the same answer each time",
             "It asks different questions",
             "It refuses to ask any",
             "It asks only about monastics"],
         "correct": 0,
         "expl": "Reading the one-line discourse against the four-part test is the most useful thing to do with it."},
        {"q": "What has been elided in this discourse?",
         "opts": [
             "The three items",
             "The closing formula of each half and the training instruction",
             "The setting",
             "The speaker"],
         "correct": 1,
         "expl": "A reciter restores them from the pattern; a reader without the pattern is looking at a fragment."},
        {"q": "How many ellipses does the Pāli use here?",
         "opts": ["None", "One", "Two &mdash; and the discourse is over", "Ten"],
         "correct": 2,
         "expl": "The shortest discourse in the chapter."},
        {"q": "Why does this series print the abbreviation rather than unrolling it?",
         "opts": [
             "To save space",
             "The same decision made throughout the Ones and Twos &mdash; so the reader can see how much of this literature is stored rather than written, and can count discourses the way the tradition did",
             "Because the full text is lost",
             "Because Sujato requires it"],
         "correct": 1,
         "expl": "The cost is that a discourse like this reads as incomplete."},
        {"q": "What is <em>viññugarahita</em>?",
         "opts": [
             "&ldquo;Criticized by sensible people&rdquo; &mdash; a separate mark from <em>sāvajja</em> in the Kālāma test",
             "&ldquo;Blameworthy&rdquo;",
             "&ldquo;Unskillful&rdquo;",
             "&ldquo;Hurtful&rdquo;"],
         "correct": 0,
         "expl": "Being at fault and being criticized are two different questions."},
        {"q": "What stays unchanged from the discourses on either side?",
         "opts": [
             "The predicate",
             "The three items &mdash; deeds by way of body, speech, and mind",
             "The length",
             "The abbreviation"],
         "correct": 1,
         "expl": "Only the predicate moves across AN 3.6&ndash;3.8."},
        {"q": "Is there anything in AN 3.7 that AN 3.6 has not established?",
         "opts": [
             "Yes, an entirely new teaching",
             "No &mdash; it is worth a page for what it shows about how the canon is written, not for new content",
             "Yes, a new list of three",
             "Yes, a simile"],
         "correct": 1,
         "expl": "It shows what the canon looks like where abbreviation takes over completely."},
    ],
    marginalia=[
        ("Thirty-five words", [
            "one sentence",
            "two ellipses",
            "both halves folded in",
        ]),
        ("Four marks", [
            "<span class=\"pali\">akusala</span>unskillful",
            "<span class=\"pali\">sāvajja</span>blameworthy",
            "<span class=\"pali\">viññugarahita</span>criticized by the wise",
            "leads to harm undertaken",
        ]),
        ("What was elided", [
            "&ldquo;these are the three&hellip;&rdquo;",
            "the training instruction",
        ]),
        ("Cross-references", [
            "AN 3.65 &middot; all four marks at once",
            "AN 2.1 &middot; two kinds of <em>vajja</em>",
            "AN 3.8 &middot; next: hurtful",
        ]),
    ],
    further=[
        '<a href="%s/an3.7/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.65.html">AN 3.65 &middot; With the Kālāmas of Kesamutta</a> &mdash; the '
        "four-part test that asks at once what this chapter asks one discourse at a time.",
        '<a href="an-3.8.html">AN 3.8 &middot; Hurtful</a> &mdash; next in this series, the last of '
        "the three substitutions.",
    ],
)


page(
    8, "Sabyābajjha", "Hurtful",
    meta_title="AN 3.8 — Hurtful | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sabyābajjhasutta — "
        "the last of the three substitutions, where the predicate is damage done and the "
        "positive term is kindness. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "The standing template with the last of the three predicates, and the training "
                 "instruction restored in full"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Comparable material appears in the Chinese Madhyama-āgama (T26); this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short, and the term on the "
                       "positive side is worth a moment"),
    ],
    why=(
        "The third and last of the substitutions, and the one where the two halves stop being exact "
        "mirrors. The fool is known by <em>hurtful</em> deeds of body, speech, and mind. The astute "
        "person is not known by unhurtful deeds &mdash; the discourse says <em>kind</em> deeds. That "
        "is a small asymmetry, and the only one in the whole run of three."),
    guide=[
        ("The teaching in one sentence", [
            "A fool is known by deeds that do damage; an astute person by deeds that are kind."]),
        ("Hurtful, and its opposite", [
            "<em>Sabyābajjha</em> is with-affliction, from <em>byābajjha</em>, harm or vexation. Its "
            "grammatical opposite is <em>abyābajjha</em>, without-affliction, and that is the word one "
            "would expect on the positive side. It is a standard canonical term &mdash; the "
            "unafflicted is one of the epithets of the goal.",
            "What the discourse gives instead, in Sujato&rsquo;s rendering, is <em>kind</em>. The "
            "positive half is not the mere absence of the negative but something with content of its "
            "own. Whether that difference is in the Pāli or in the English is a question worth "
            "checking against the parallel text, and readers can do so on SuttaCentral; what is not in "
            "doubt is that the collection routinely does state its positives as absences, and here it "
            "is worth noticing when a translator judges otherwise.",
            "The point is small and the habit it illustrates is not. This series has flagged several "
            "renderings that would have been made differently &mdash; <em>situational awareness</em> "
            "for <em>sampajañña</em>, <em>aborigines</em> for <em>kiṁpurisā</em> &mdash; on the "
            "principle set out in AN 1.140&ndash;149 that representing a text accurately is itself a "
            "practice. The principle applies to small choices as much as to large ones."]),
        ("The full instruction restored", [
            "Unlike AN 3.7, this discourse writes out the closing formula and the training instruction "
            "in full: <em>we will shun the three qualities by which a fool is known, and we will "
            "undertake and follow the three qualities by which an astute person is known</em>.",
            "That is how the canon usually handles a run of abbreviations: it compresses the middle and "
            "restores the frame at the end, so that a reciter working through the sequence gets the "
            "full pattern back before moving on. AN 3.6 was partly abbreviated, AN 3.7 almost entirely "
            "so, and AN 3.8 restores. Reading the three in order shows the mechanism.",
            "It also means AN 3.8 is the natural place to stop and take stock of the run. Three "
            "predicates &mdash; unskillful, blameworthy, hurtful &mdash; and one unchanging set of "
            "three items. The chapter has now said that bad conduct of body, speech, and mind fails "
            "the competence test, the judgment test, and the harm test alike."]),
        ("Where the chapter goes next", [
            "AN 3.9 and 3.10 close the chapter by changing the frame rather than the predicate. AN 3.9 "
            "returns to the broken-and-damaged formula met at AN 2.134 in the Twos: the fool "
            "<em>keeps themselves broken and damaged</em>, which relocates the injury from those "
            "around them to themselves. And AN 3.10 leaves the fool-and-astute pair entirely for three "
            "specific stains &mdash; immorality, jealousy, and stinginess &mdash; and a rebirth "
            "destination.",
            "So the chapter&rsquo;s shape is: a large claim about danger, a criterion, the criterion "
            "argued for, the criterion narrowed to two testable situations, the criterion run through "
            "three predicates, and then two discourses on what it costs the person themselves. Ten "
            "discourses that are much more tightly composed than their individual brevity "
            "suggests."]),
    ],
    terms=[
        ("sabyābajjha",
         "&ldquo;hurtful&rdquo; &mdash; literally with-affliction, from <em>byābajjha</em>, harm or "
         "vexation."),
        ("abyābajjha",
         "&ldquo;without affliction&rdquo; &mdash; the expected grammatical opposite, and one of the "
         "canonical epithets of the goal; not the word used on the positive side here."),
        ("byābajjha",
         "&ldquo;harm, vexation&rdquo; &mdash; the root of the pair, and the third of the three "
         "predicates run across AN 3.6&ndash;3.8."),
        ("sikkhitabbaṁ",
         "&ldquo;you should train&rdquo; &mdash; the closing instruction, restored in full here after "
         "being elided in the two discourses before."),
        ("dhamma",
         "&ldquo;quality&rdquo; in the closing formula of this discourse, where the earlier ones said "
         "&ldquo;thing&rdquo; &mdash; the word&rsquo;s range is wide enough to carry both."),
    ],
    text_intro=(
        "The discourse in full, with the closing instruction restored after two abbreviated "
        "discourses. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Hurtful deeds, and kind ones"),
        ("p", "&sect;1", "an3.8:1.1-1.4"),
        ("h3", "So you should train"),
        ("p", "&sect;2", "an3.8:2.1-2.3"),
    ],
    quiz=[
        {"q": "What does <em>sabyābajjha</em> literally mean?",
         "opts": [
             "&ldquo;With-affliction&rdquo; &mdash; from <em>byābajjha</em>, harm or vexation",
             "&ldquo;Blameworthy&rdquo;",
             "&ldquo;Unskillful&rdquo;",
             "&ldquo;Forbidden&rdquo;"],
         "correct": 0,
         "expl": "The third and last of the three predicates."},
        {"q": "What word would one grammatically expect on the positive side?",
         "opts": [
             "<em>Kusala</em>",
             "<em>Abyābajjha</em>, without-affliction &mdash; a standard canonical term and one of the epithets of the goal",
             "<em>Anavajja</em>",
             "<em>Sukha</em>"],
         "correct": 1,
         "expl": "What the discourse gives instead is <em>kind</em>."},
        {"q": "What is notable about that substitution?",
         "opts": [
             "Nothing",
             "The positive half is not the mere absence of the negative but something with content of its own &mdash; and the collection routinely does state its positives as absences",
             "It changes the meaning entirely",
             "It removes the training instruction"],
         "correct": 1,
         "expl": "The only asymmetry in the whole run of three."},
        {"q": "How does the guide handle the question of whether the difference is in the Pāli or the English?",
         "opts": [
             "By asserting one answer",
             "By naming it as a question worth checking against the parallel text, which readers can do on SuttaCentral",
             "By ignoring it",
             "By changing the translation"],
         "correct": 1,
         "expl": "The English printed is Sujato's throughout, as it is on every page of this series."},
        {"q": "Which other renderings has this series flagged on the same principle?",
         "opts": [
             "<em>Situational awareness</em> for <em>sampajañña</em>, and <em>aborigines</em> for <em>kiṁpurisā</em>",
             "None",
             "Only Pāli terms with no English equivalent",
             "Only terms in the Vinaya"],
         "correct": 0,
         "expl": "On the principle of AN 1.140&ndash;149 that representing a text accurately is itself a practice."},
        {"q": "How does AN 3.8 differ from AN 3.7 in form?",
         "opts": [
             "It is shorter",
             "It writes out the closing formula and the training instruction in full, where AN 3.7 elided them",
             "It has no predicate",
             "It names a disciple"],
         "correct": 1,
         "expl": "AN 3.6 partly abbreviated, AN 3.7 almost entirely, AN 3.8 restores."},
        {"q": "What does that pattern show about how the canon handles a run of abbreviations?",
         "opts": [
             "That abbreviation is random",
             "That it compresses the middle and restores the frame at the end, so a reciter gets the full pattern back before moving on",
             "That the abbreviations are errors",
             "That later editors filled them in"],
         "correct": 1,
         "expl": "Reading the three in order shows the mechanism."},
        {"q": "What has the chapter established by the end of AN 3.8?",
         "opts": [
             "That bad conduct of body, speech, and mind fails the competence test, the judgment test, and the harm test alike",
             "That only monastics can be astute",
             "That folly is incurable",
             "That the three items differ by predicate"],
         "correct": 0,
         "expl": "Three predicates, one unchanging set of three items."},
        {"q": "What do AN 3.9 and 3.10 change?",
         "opts": [
             "The predicate",
             "The frame &mdash; 3.9 relocates the injury to the fool themselves with the broken-and-damaged formula, and 3.10 leaves the pair entirely for three stains and a rebirth destination",
             "The setting",
             "The speaker"],
         "correct": 1,
         "expl": "The chapter closes by turning from what folly does to others to what it costs the person."},
        {"q": "How does the guide characterize the chapter&rsquo;s composition?",
         "opts": [
             "As a loose collection",
             "As much more tightly composed than the individual brevity of its discourses suggests &mdash; a large claim, a criterion, an argument for it, two testable situations, three predicates, and two discourses on the cost",
             "As disordered",
             "As a later compilation"],
         "correct": 1,
         "expl": "Ten short discourses with a shape."},
    ],
    marginalia=[
        ("The asymmetry", [
            "<span class=\"pali\">sabyābajjha</span>hurtful",
            "expected: without affliction",
            "given: kind",
        ]),
        ("The run of three", [
            "3.6 partly abbreviated",
            "3.7 almost entirely",
            "3.8 restores the frame",
        ]),
        ("The chapter&rsquo;s shape", [
            "3.1 &middot; the claim",
            "3.2&ndash;3 &middot; the criterion",
            "3.4&ndash;5 &middot; two tests",
            "3.6&ndash;8 &middot; three predicates",
            "3.9&ndash;10 &middot; what it costs",
        ]),
        ("Cross-references", [
            "AN 1.140&ndash;149 &middot; representing accurately",
            "AN 2.130&ndash;140 &middot; broken and damaged",
            "AN 3.9 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.8/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, so that the rendering discussed above can be "
        "checked against the parallel text." % SC,
        '<a href="an-1.140-149.html">AN 1.140&ndash;149 &middot; Not the Teaching</a> &mdash; the '
        "principle behind this guide&rsquo;s notes on translation: representing a text accurately is "
        "itself named as meritorious work.",
        '<a href="an-3.9.html">AN 3.9 &middot; Broken</a> &mdash; next in this series, where the '
        "injury is relocated from those around the fool to the fool.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.9 — Khatasutta
# --------------------------------------------------------------------------- #
page(
    9, "Khata", "Broken",
    meta_title="AN 3.9 — Broken | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Khatasutta — the "
        "fool keeps themselves broken and damaged, which relocates the harm of folly from "
        "those around it to the person who has it. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "Two parallel passages on the broken-and-damaged formula, with no training "
                 "instruction attached"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Comparable material appears in the Chinese Madhyama-āgama (T26); this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, and turning the "
                       "chapter&rsquo;s argument around"),
    ],
    why=(
        "The chapter opened by saying that all danger comes from the foolish &mdash; a claim about "
        "what folly does to everyone else. This discourse turns it around. The fool "
        "<em>keeps themselves broken and damaged</em>, deserves criticism from sensible people, and "
        "brims with much wickedness. The harm has not been withdrawn from the world; a second account "
        "of it has been added, and the second account is about the person who has it."),
    guide=[
        ("The teaching in one sentence", [
            "Bad conduct of body, speech, and mind does its first damage to the person doing it."]),
        ("The image in the formula", [
            "<em>Khataṁ upahataṁ attānaṁ pariharati</em>: they carry about a self that is dug out and "
            "injured. <em>Khata</em> is excavated or dug up; <em>upahata</em> is struck or damaged. "
            "The verb <em>pariharati</em> means to carry around, to keep with one.",
            "So the image is not of an injury received but of one maintained. The fool is not damaged "
            "by something; they carry the damage about with them, continuously, as a condition. "
            "Sujato&rsquo;s &ldquo;keeps themselves broken and damaged&rdquo; holds that sense of "
            "ongoing self-maintenance, which a phrase like &ldquo;is broken&rdquo; would lose.",
            "The formula appeared twice in the Twos, at AN 2.134&ndash;137, applied to praising and "
            "blaming without examination and to acting wrongly toward parents and toward the Realized "
            "One. In each case the same point: the injury named falls on the one who did it."]),
        ("Three consequences, in order", [
            "The discourse names three things that follow, and they are worth separating. The person "
            "keeps themselves broken and damaged &mdash; the internal consequence. They deserve to be "
            "blamed and criticized by sensible people &mdash; the social one. And they brim with much "
            "wickedness &mdash; the kammic one.",
            "The order is not arbitrary. It runs from what has already happened, through what others "
            "will do, to what will follow later. And the first is stated first, which is the "
            "chapter&rsquo;s point: before anyone else has noticed and before anything has ripened, "
            "the damage is done and is being carried.",
            "For the astute person all three are inverted: intact and unscathed, undeserving of "
            "criticism, brimming with much merit. Note that the second is stated as "
            "<em>don&rsquo;t deserve to be criticized</em>, not <em>are not criticized</em>. The canon "
            "is not promising that the wise escape blame; AN 2.39 has already described a community in "
            "which the good-hearted fall silent. What is promised is that the blame would be "
            "undeserved."]),
        ("No training instruction", [
            "Alone among the discourses of this chapter, AN 3.9 does not end with <em>so you should "
            "train like this</em>. It states the consequence and stops.",
            "Whether that is a compositional decision or an accident of transmission cannot be settled "
            "from the text. What can be said is that the effect is different. The eight discourses "
            "before it end by handing the listener something to do. This one ends by describing a "
            "condition, and leaves the reader in it. The next discourse, AN 3.10, does the same and "
            "goes further, ending on a rebirth destination with no instruction attached either."]),
    ],
    terms=[
        ("khata",
         "&ldquo;excavated, dug out&rdquo; &mdash; the first half of the formula, and a physical image "
         "of ground removed from under something."),
        ("upahata",
         "&ldquo;struck, damaged&rdquo; &mdash; the second half."),
        ("pariharati",
         "&ldquo;carries about, keeps with one&rdquo; &mdash; the verb that makes the formula describe "
         "a maintained condition rather than an injury received."),
        ("sānuvajja",
         "&ldquo;deserving of criticism&rdquo; &mdash; note that the astute person is said not to "
         "<em>deserve</em> criticism, which is not the same as not receiving it."),
        ("bahuñca apuññaṁ pasavati",
         "&ldquo;brims with much wickedness&rdquo; &mdash; the third and last consequence, and the "
         "only one that lies in the future."),
    ],
    text_intro=(
        "The discourse in full, in two parallel passages. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "The foolish, incompetent, untrue person"),
        ("p", "&sect;1", "an3.9:1.1-1.4"),
        ("h3", "The astute, competent, true person"),
        ("p", "&sect;2", "an3.9:2.1-2.4"),
    ],
    quiz=[
        {"q": "How does this discourse turn the chapter&rsquo;s opening claim around?",
         "opts": [
             "By denying that folly causes danger",
             "AN 3.1 said all danger comes from the foolish &mdash; a claim about others; this one says the fool keeps <em>themselves</em> broken and damaged",
             "By restricting the claim to monastics",
             "By adding a fourth item"],
         "correct": 1,
         "expl": "A second account of the harm is added, and it is about the person who has it."},
        {"q": "What does <em>pariharati</em> add to the formula?",
         "opts": [
             "Nothing",
             "&ldquo;Carries about, keeps with one&rdquo; &mdash; making the image one of a maintained condition rather than an injury received",
             "A time limit",
             "A rebirth destination"],
         "correct": 1,
         "expl": "Sujato's &ldquo;keeps themselves broken and damaged&rdquo; holds that sense; &ldquo;is broken&rdquo; would lose it."},
        {"q": "What are <em>khata</em> and <em>upahata</em>?",
         "opts": [
             "&ldquo;Excavated, dug out&rdquo; and &ldquo;struck, damaged&rdquo;",
             "&ldquo;Blameworthy&rdquo; and &ldquo;hurtful&rdquo;",
             "&ldquo;Foolish&rdquo; and &ldquo;astute&rdquo;",
             "&ldquo;Skillful&rdquo; and &ldquo;unskillful&rdquo;"],
         "correct": 0,
         "expl": "A physical image of ground removed from under something, and of a blow."},
        {"q": "Where else in this series has the formula appeared?",
         "opts": [
             "Nowhere",
             "AN 2.134&ndash;137, applied to praising and blaming without examination and to acting wrongly toward parents and toward the Realized One",
             "Only in the Ones",
             "Only in the Vinaya"],
         "correct": 1,
         "expl": "In each case the injury named falls on the one who did it."},
        {"q": "What are the three consequences, in order?",
         "opts": [
             "Internal (keeping oneself damaged), social (deserving criticism), and kammic (brimming with wickedness)",
             "Kammic, social, internal",
             "Social, internal, kammic",
             "Three kammic consequences"],
         "correct": 0,
         "expl": "Running from what has already happened, through what others will do, to what follows later."},
        {"q": "Why does the guide say the order is not arbitrary?",
         "opts": [
             "Because the Pāli requires it",
             "Because the internal consequence is stated first &mdash; before anyone else has noticed and before anything has ripened, the damage is done and is being carried",
             "Because the social one is most important",
             "Because it matches the Vinaya"],
         "correct": 1,
         "expl": "Which is the chapter's point in this discourse."},
        {"q": "How is the astute person&rsquo;s social consequence phrased?",
         "opts": [
             "That they are not criticized",
             "That they do not <em>deserve</em> to be criticized &mdash; which is not the same thing",
             "That they are praised by all",
             "That they are ignored"],
         "correct": 1,
         "expl": "The canon is not promising that the wise escape blame; AN 2.39 describes a community where the good-hearted fall silent."},
        {"q": "What is unique about this discourse within the chapter?",
         "opts": [
             "It is the longest",
             "Alone among the chapter&rsquo;s discourses it does not end with &ldquo;so you should train like this&rdquo;",
             "It names a disciple",
             "It has a simile"],
         "correct": 1,
         "expl": "It states the consequence and stops."},
        {"q": "What effect does the guide say that has?",
         "opts": [
             "None",
             "The eight discourses before it end by handing the listener something to do; this one ends by describing a condition and leaves the reader in it",
             "It makes the discourse incomplete",
             "It makes the discourse optional"],
         "correct": 1,
         "expl": "AN 3.10 does the same and goes further."},
        {"q": "Can the guide settle whether the missing instruction is compositional or accidental?",
         "opts": [
             "Yes, it is certainly compositional",
             "Yes, it is certainly a transmission error",
             "No &mdash; it says the question cannot be settled from the text, and describes the effect instead",
             "The question is not raised"],
         "correct": 2,
         "expl": "What can be said is what the effect is."},
    ],
    marginalia=[
        ("The formula", [
            "<span class=\"pali\">khata</span>dug out",
            "<span class=\"pali\">upahata</span>struck",
            "<span class=\"pali\">pariharati</span>carries about",
        ]),
        ("Three consequences", [
            "keeps themselves damaged",
            "deserves criticism",
            "brims with wickedness",
            "&mdash; now, soon, later",
        ]),
        ("A careful phrase", [
            "not: the wise are not criticized",
            "but: they do not deserve it",
        ]),
        ("Cross-references", [
            "AN 3.1 &middot; danger to others",
            "AN 2.130&ndash;140 &middot; the same formula",
            "AN 2.39 &middot; when the good fall silent",
        ]),
    ],
    further=[
        '<a href="%s/an3.9/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.130-140.html">AN 2.130&ndash;140 &middot; Aspiration</a> &mdash; where the same '
        "broken-and-damaged formula is applied to praising and blaming without examination.",
        '<a href="an-3.10.html">AN 3.10 &middot; Stains</a> &mdash; next in this series, and the '
        "chapter&rsquo;s close.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.10 — Malasutta
# --------------------------------------------------------------------------- #
page(
    10, "Mala", "Stains",
    meta_title="AN 3.10 — Stains | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Malasutta, which "
        "closes the first chapter of the Threes — three stains named specifically, and a "
        "destination stated without an instruction attached. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
                    "is understood to hold"),
        ("Speakers", SPEAKER),
        ("Form", "Two parallel passages naming three qualities and three stains, each closing on a "
                 "destination"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "The triad of immorality, jealousy, and stinginess appears across the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, and specific where the rest "
                       "of the chapter was general"),
    ],
    why=(
        "The chapter closes by dropping the fool-and-astute vocabulary entirely and naming three "
        "things: immorality, jealousy, and stinginess. After nine discourses that defined a fool by "
        "conduct in general &mdash; bad, unskillful, blameworthy, hurtful, all by way of body, speech, "
        "and mind &mdash; the last one names three particular faults and says where they lead. It is "
        "the only discourse in the chapter with content this specific, and the specificity is the "
        "point of putting it last."),
    guide=[
        ("The teaching in one sentence", [
            "Being unethical, jealous, and stingy &mdash; and not having given up the stains of "
            "these &mdash; places a person in hell as if delivered there."]),
        ("Why three <em>stains</em>", [
            "<em>Mala</em> is a stain, dirt, or impurity &mdash; the word for what discolors a cloth "
            "or tarnishes metal. It is not the collection&rsquo;s usual word for a fault, and its "
            "appearance here is deliberate.",
            "The discourse also does something grammatically odd that is easy to read past. It names "
            "each item twice: the person is unethical <em>and has not given up the stain of "
            "immorality</em>; jealous <em>and has not given up the stain of jealousy</em>; stingy "
            "<em>and has not given up the stain of stinginess</em>. The quality and its stain are "
            "listed as two things.",
            "The distinction is worth taking seriously rather than treating as verbal doubling. Being "
            "stingy is a present condition; the stain of stinginess is what it leaves. A person may "
            "stop acting stingily and still carry the discoloration &mdash; the disposition remains, "
            "the residue has not been removed. That reading fits the image exactly: a cloth is not "
            "clean because nothing is currently being spilled on it."]),
        ("The three, and why these three", [
            "Immorality (<em>dussīlya</em>), jealousy (<em>issā</em>), and stinginess "
            "(<em>macchariya</em>). The last two are a fixed pair across the canon, met in the Twos at "
            "AN 2.180&ndash;229, where jealousy resents what another has and stinginess refuses to "
            "release what one has oneself &mdash; the same reflex pointed outward and inward.",
            "Putting general unethical conduct alongside them makes an interesting group: one item "
            "covering everything the chapter has been discussing, and two very specific social faults "
            "about the flow of goods and standing between people. Nothing here is about meditation, "
            "doctrine, or belief. A person who wanted to know what this chapter would actually have "
            "them stop doing would be answered by these three names."]),
        ("A destination, with no instruction", [
            "Like AN 3.9, this discourse ends without <em>so you should train</em>. What it ends with "
            "instead is a destination: such a person is placed in hell <em>as if delivered there</em>, "
            "and the person who has given the three up is placed in heaven the same way.",
            "The phrase is the one met at AN 1.43&ndash;44 in the Ones and again in the Twos: "
            "<em>yathābhataṁ nikkhitto</em>, carried and set down. There is no judgment, no interval, "
            "and no agent doing the placing. The image is of something being put where it belongs by "
            "the simple fact of what it is.",
            "Ending the chapter this way is a considered choice. Nine discourses have argued that folly "
            "is recognizable, that it is recognizable by conduct, and that it damages both others and "
            "the person themselves. The tenth stops arguing, names three faults, states where they "
            "lead, and does not tell anyone what to do about it. After nine training instructions, "
            "the absence of a tenth is the most emphatic thing the chapter could have done."]),
    ],
    terms=[
        ("mala",
         "&ldquo;stain, impurity&rdquo; &mdash; the word for what discolors cloth or tarnishes metal, "
         "and not the collection&rsquo;s usual term for a fault."),
        ("dussīlya",
         "&ldquo;immorality, bad conduct&rdquo; &mdash; the first of the three, covering in one word "
         "everything the chapter has spent nine discourses on."),
        ("issā / macchariya",
         "&ldquo;jealousy&rdquo; and &ldquo;stinginess&rdquo; &mdash; a fixed pair across the canon: "
         "resenting what another has, and refusing to release what one has."),
        ("appahīna",
         "&ldquo;not given up&rdquo; &mdash; the word that makes the discourse list each quality and "
         "its stain as two things: the condition, and the residue it leaves."),
        ("yathābhataṁ nikkhitto",
         "&ldquo;placed as if delivered there&rdquo; &mdash; carried and set down. No judgment, no "
         "interval, no agent doing the placing."),
    ],
    text_intro=(
        "The discourse in full, in two parallel passages. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Three qualities, three stains, and hell"),
        ("p", "&sect;1", "an3.10:1.1-1.6"),
        ("h3", "And their opposites"),
        ("p", "&sect;2", "an3.10:2.1-2.6"),
    ],
    quiz=[
        {"q": "Which three stains does the discourse name?",
         "opts": [
             "Greed, hate, and delusion",
             "Immorality, jealousy, and stinginess",
             "Anger, acrimony, and contempt",
             "Ignorance, doubt, and restlessness"],
         "correct": 1,
         "expl": "The only discourse in the chapter with content this specific."},
        {"q": "What does <em>mala</em> mean, and why is the word notable?",
         "opts": [
             "&ldquo;Stain, impurity&rdquo; &mdash; the word for what discolors cloth or tarnishes metal, and not the collection&rsquo;s usual term for a fault",
             "&ldquo;Offense&rdquo; &mdash; the standard Vinaya term",
             "&ldquo;Hindrance&rdquo;",
             "&ldquo;Fetter&rdquo;"],
         "correct": 0,
         "expl": "Its appearance here is deliberate."},
        {"q": "What grammatical oddity does the discourse contain?",
         "opts": [
             "It names each item twice &mdash; the person is jealous <em>and has not given up the stain of jealousy</em>, listing the quality and its stain as two things",
             "It omits the verb",
             "It uses no pronouns",
             "It repeats the setting"],
         "correct": 0,
         "expl": "Worth taking seriously rather than treating as verbal doubling."},
        {"q": "What distinction does the guide draw from that doubling?",
         "opts": [
             "None; it is mere repetition",
             "Being stingy is a present condition; the stain of stinginess is what it leaves &mdash; a person may stop acting stingily and still carry the discoloration",
             "One applies to monastics and one to laypeople",
             "One is bodily and one is mental"],
         "correct": 1,
         "expl": "A cloth is not clean because nothing is currently being spilled on it."},
        {"q": "How do jealousy and stinginess relate?",
         "opts": [
             "They are unrelated",
             "Jealousy resents what another has; stinginess refuses to release what one has &mdash; the same reflex pointed outward and inward",
             "Stinginess causes jealousy",
             "Both concern only monastics"],
         "correct": 1,
         "expl": "A fixed pair across the canon, met in the Twos at AN 2.180&ndash;229."},
        {"q": "What is notable about the composition of the three?",
         "opts": [
             "All three concern meditation",
             "One item covers everything the chapter has been discussing, and two are very specific social faults about the flow of goods and standing between people &mdash; nothing about meditation, doctrine, or belief",
             "All three concern doctrine",
             "All three concern monastic rules"],
         "correct": 1,
         "expl": "A person asking what this chapter would have them stop doing is answered by these three names."},
        {"q": "How does the discourse end?",
         "opts": [
             "With a training instruction",
             "With a destination &mdash; placed in hell <em>as if delivered there</em>, and its opposite &mdash; and no instruction attached",
             "With a simile",
             "With a question"],
         "correct": 1,
         "expl": "Like AN 3.9, and going further."},
        {"q": "What does <em>yathābhataṁ nikkhitto</em> convey?",
         "opts": [
             "A judgment passed after death",
             "Carried and set down &mdash; no judgment, no interval, and no agent doing the placing",
             "A punishment proportional to the offense",
             "A temporary condition"],
         "correct": 1,
         "expl": "Something put where it belongs by the simple fact of what it is."},
        {"q": "Why does the guide call the missing instruction a considered choice?",
         "opts": [
             "Because the Pāli requires it",
             "Because after nine training instructions, the absence of a tenth is the most emphatic thing the chapter could have done",
             "Because the text is damaged",
             "Because instructions are optional"],
         "correct": 1,
         "expl": "The tenth discourse stops arguing, names three faults, and states where they lead."},
        {"q": "What has the chapter argued across its ten discourses?",
         "opts": [
             "That folly is recognizable, that it is recognizable by conduct, and that it damages both others and the person themselves",
             "That folly is incurable",
             "That only monastics can be astute",
             "That danger is unavoidable"],
         "correct": 0,
         "expl": "And then it names three things and stops."},
    ],
    marginalia=[
        ("Three stains", [
            "<span class=\"pali\">dussīlya</span>immorality",
            "<span class=\"pali\">issā</span>jealousy",
            "<span class=\"pali\">macchariya</span>stinginess",
        ]),
        ("Named twice", [
            "the quality: being stingy",
            "the stain: what it leaves",
            "&mdash; a cloth is not clean by default",
        ]),
        ("The ending", [
            "<span class=\"pali\">yathābhataṁ nikkhitto</span>carried and set down",
            "no judgment, no agent",
            "and no instruction",
        ]),
        ("Cross-references", [
            "AN 1.41&ndash;50 &middot; the same phrase",
            "AN 2.180&ndash;229 &middot; jealousy and stinginess",
            "AN 3.61 &middot; where this series goes next",
        ]),
    ],
    further=[
        '<a href="%s/an3.10/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-1.41-50.html">AN 1.41&ndash;50 &middot; A Spike</a> &mdash; AN 1.43&ndash;44, '
        "where &ldquo;placed as if delivered there&rdquo; is first used and the mechanism discussed.",
        '<a href="an-2.180-229.html">AN 2.180&ndash;229 &middot; Anger, Abbreviated</a> &mdash; where '
        "jealousy and stinginess are separated as the same reflex pointed outward and inward.",
        '<a href="an-3.61.html">AN 3.61 &middot; Sectarian Tenets</a> &mdash; where this series '
        "continues, until the intervening discourses of the Threes are added.",
    ],
)
