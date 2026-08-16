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


# --------------------------------------------------------------------------- #
# AN 3.11–20 — Rathakāravagga
# --------------------------------------------------------------------------- #
VAGGA_2 = "<em>Rathakāravagga</em> &mdash; the second chapter of the Threes"
NO_SETTING = ("None stated; the discourse continues from AN 3.1, whose setting at Sāvatthī "
              "is understood to hold")

page(
    11, "Ñāta", "Well-known",
    vagga=VAGGA_2,
    meta_title="AN 3.11 — Well-known | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ñātasutta — what a "
        "well-known mendicant does with the three things they encourage, and why the "
        "discourse specifies fame before it specifies conduct. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Two parallel passages, negative then positive, on one qualified subject"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Comparable material on the influence of prominent monastics appears "
                              "in the Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, with one qualifying word "
                       "doing all the work"),
    ],
    why=(
        "The second chapter of the Threes opens on a subject the first never touched: not what a "
        "person is, but what a person with an audience is. The discourse is about a "
        "<em>well-known</em> mendicant &mdash; and everything it says would be unremarkable without "
        "that word. What it names is the multiplier: the same three things, encouraged by someone "
        "nobody listens to, do not act for the harm of gods and humans."),
    guide=[
        ("The teaching in one sentence", [
            "A mendicant with a reputation encourages deeds and principles, and whether those are in "
            "line with good qualities decides whether their fame does harm or good on a very large "
            "scale."]),
        ("The word that changes everything", [
            "<em>Ñāta</em> means known, famous, recognized. Strip it out and the discourse reads like "
            "any of the ten before it: someone who promotes bad conduct acts for the harm of the "
            "many. With it, the subject is different. The discourse is not about a fault; it is about "
            "a fault with reach.",
            "The Aṅguttara is unusually attentive to this. AN 2.39 described what happens when bad "
            "mendicants are strong and the good-hearted fall silent. AN 2.44 described the assembly "
            "whose seniors are leaders in backsliding and whose juniors follow. Both are about "
            "influence rather than about individual conduct, and this discourse states the principle "
            "underlying them: a person whose words carry has a different relationship to their own "
            "faults than a person whose words do not."]),
        ("Three things, and the third is odd", [
            "The three are deeds of body, deeds of speech, and <em>principles</em> &mdash; "
            "<em>dhamma</em>. The first two are the familiar list minus its third member; mental "
            "action has been replaced by something else.",
            "That substitution is the discourse&rsquo;s real content. What a well-known person "
            "encourages is not only how people behave but what they take to be true, and the "
            "discourse counts the second as a third kind of encouragement alongside the two kinds of "
            "conduct. A prominent teacher propagates a view whether or not they mean to.",
            "It is worth setting this beside AN 3.2, where the three things were body, speech, and "
            "mind. For an ordinary person the third term is private &mdash; what they cultivate in "
            "thought. For a well-known person it has become public: the principles they encourage in "
            "others. Fame converts the inner term into an outer one."]),
        ("Reading it now", [
            "The discourse assumes a world in which a well-known monastic&rsquo;s reach was a "
            "district and a generation. That assumption no longer holds, and the arithmetic of the "
            "claim has changed accordingly rather than the claim itself.",
            "It is also worth naming what the discourse does not offer, which is any advice about "
            "how to become or stay well-known, or any suggestion that a person should avoid "
            "prominence. It treats being known as a circumstance, like the shopkeeper&rsquo;s "
            "capital two discourses later. What it asks is what is being multiplied."]),
    ],
    terms=[
        ("ñāta",
         "&ldquo;known, famous, recognized&rdquo; &mdash; the qualifying word without which the "
         "discourse would say nothing new."),
        ("samādapeti",
         "&ldquo;encourages, incites, takes up together with&rdquo; &mdash; what the well-known "
         "mendicant does with deeds and principles. Not commanding but bringing others along."),
        ("dhamma",
         "&ldquo;principle, teaching&rdquo; &mdash; the third of the three things encouraged, "
         "replacing the mental action of the standard triad."),
        ("ananulomika",
         "&ldquo;not in line with&rdquo; &mdash; said of what is encouraged when it does not accord "
         "with good qualities."),
        ("bahujanaahitāya",
         "&ldquo;for the detriment of the people&rdquo; &mdash; the standard formula for large-scale "
         "harm, used in the Ones of those who make the true teaching disappear."),
    ],
    text_intro=(
        "The discourse in full, in two parallel passages. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "A well-known mendicant, acting for harm"),
        ("p", "&sect;1", "an3.11:1.1-1.4"),
        ("h3", "And for welfare"),
        ("p", "&sect;2", "an3.11:2.1-2.4"),
    ],
    quiz=[
        {"q": "What single word makes this discourse different from the ten before it?",
         "opts": [
             "<em>Mendicant</em>",
             "<em>Ñāta</em> &mdash; well-known; the subject is a fault with reach rather than a fault",
             "<em>Deeds</em>",
             "<em>Principles</em>"],
         "correct": 1,
         "expl": "Strip it out and the discourse reads like any of the ten before it."},
        {"q": "Which three things does a well-known mendicant encourage?",
         "opts": [
             "Deeds of body, deeds of speech, and principles",
             "Deeds of body, speech, and mind",
             "Giving, ethics, and meditation",
             "Faith, energy, and wisdom"],
         "correct": 0,
         "expl": "Mental action has been replaced by something else."},
        {"q": "What does that substitution amount to?",
         "opts": [
             "Nothing; the terms are synonyms",
             "What a well-known person encourages is not only how people behave but what they take to be true &mdash; a prominent teacher propagates a view whether or not they mean to",
             "That mental action does not matter",
             "That principles are easier to teach"],
         "correct": 1,
         "expl": "The discourse counts it as a third kind of encouragement alongside the two kinds of conduct."},
        {"q": "How does the guide relate this to AN 3.2?",
         "opts": [
             "They are unrelated",
             "For an ordinary person the third term is private &mdash; what they cultivate in thought; for a well-known person it has become public. Fame converts the inner term into an outer one",
             "AN 3.2 contradicts this discourse",
             "AN 3.2 uses the same three terms"],
         "correct": 1,
         "expl": "A small change in a list carrying a real observation."},
        {"q": "Which earlier discourses does the guide say share this concern with influence?",
         "opts": [
             "AN 2.39 on bad mendicants being strong, and AN 2.44 on the assembly whose seniors are leaders in backsliding",
             "AN 2.141&ndash;150 on giving",
             "AN 1.1&ndash;10 on the senses",
             "AN 2.77&ndash;86 on causation"],
         "correct": 0,
         "expl": "Both are about influence rather than individual conduct."},
        {"q": "What principle does this discourse state that underlies them?",
         "opts": [
             "That fame should be avoided",
             "That a person whose words carry has a different relationship to their own faults than a person whose words do not",
             "That reputation is always deserved",
             "That influence cannot be measured"],
         "correct": 1,
         "expl": "The multiplier is the subject."},
        {"q": "What does <em>samādapeti</em> mean?",
         "opts": [
             "&ldquo;Commands&rdquo;",
             "&ldquo;Encourages, incites, takes up together with&rdquo; &mdash; bringing others along rather than commanding",
             "&ldquo;Forbids&rdquo;",
             "&ldquo;Records&rdquo;"],
         "correct": 1,
         "expl": "Which is how influence actually works in the discourse's picture."},
        {"q": "What does the discourse <em>not</em> offer?",
         "opts": [
             "Any advice about becoming or staying well-known, or any suggestion that a person should avoid prominence",
             "Any account of harm",
             "Any positive case",
             "Any mention of principles"],
         "correct": 0,
         "expl": "It treats being known as a circumstance and asks what is being multiplied."},
        {"q": "What assumption of the discourse no longer holds?",
         "opts": [
             "That monastics exist",
             "That a well-known monastic&rsquo;s reach was a district and a generation",
             "That conduct matters",
             "That teachings can be encouraged"],
         "correct": 1,
         "expl": "The arithmetic of the claim has changed; the claim has not."},
        {"q": "What is the formula <em>bahujanaahitāya</em> used of elsewhere in this series?",
         "opts": [
             "Those who make the true teaching disappear, in the Ones",
             "The foremost disciples",
             "The four assemblies",
             "The ten recollections"],
         "correct": 0,
         "expl": "The standard formula for large-scale harm."},
    ],
    marginalia=[
        ("One word", [
            "<span class=\"pali\">ñāta</span>well-known",
            "&mdash; a fault with reach",
        ]),
        ("Three things", [
            "deeds of body",
            "deeds of speech",
            "<span class=\"pali\">dhamma</span>principles",
            "&mdash; mind, gone public",
        ]),
        ("What it does not say", [
            "not: avoid prominence",
            "not: how to become known",
            "but: what is being multiplied",
        ]),
        ("Cross-references", [
            "AN 2.39 &middot; when bad monastics are strong",
            "AN 2.44 &middot; seniors set the pace",
            "AN 3.2 &middot; the private third term",
        ]),
    ],
    further=[
        '<a href="%s/an3.11/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.32-41.html">AN 2.32&ndash;41 &middot; The Peaceful Mind</a> &mdash; AN 2.39, '
        "on what happens to a community when the influence runs the wrong way and the decent fall "
        "silent.",
        '<a href="an-3.12.html">AN 3.12 &middot; Commemoration</a> &mdash; next in this series.',
    ],
)


page(
    12, "Sāraṇīya", "Commemoration",
    vagga=VAGGA_2,
    meta_title="AN 3.12 — Commemoration | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sāraṇīyasutta — the "
        "three places a king remembers all his life, and the three a mendicant should, with "
        "the parallel drawn exactly. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three places for a king, then three for a mendicant, on a strict parallel"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Comparable material appears in the Chinese Āgamas, where places "
                              "associated with the Buddha&rsquo;s life became objects of pilgrimage; "
                              "this reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple, and quietly making a "
                       "large claim about what a life is measured by"),
    ],
    why=(
        "An anointed king remembers three places as long as he lives: where he was born, where he was "
        "crowned, and where he won his decisive battle. The discourse gives the list, and then gives "
        "a mendicant&rsquo;s three: where they went forth, where they understood the four truths, and "
        "where they realized freedom. The parallel is exact and the substitution is the point. A "
        "life is measured by three moments, and the question is which three."),
    guide=[
        ("The teaching in one sentence", [
            "Both a king and a mendicant have three places worth remembering for life, and the two "
            "lists are structurally identical and share nothing."]),
        ("The king&rsquo;s three", [
            "Birth, coronation, and the battle that established him as foremost. Read as a life they "
            "are: what you were given, what you were granted, and what you took. Two of the three "
            "depend entirely on other people &mdash; a king does not choose to be born royal or "
            "anoint himself &mdash; and the third is a victory over someone else.",
            "The discourse does not criticize any of this. It is stated as a plain fact about what a "
            "king commemorates, and the tone is neutral. The critique, if there is one, is entirely "
            "in the parallel."]),
        ("The mendicant&rsquo;s three", [
            "Where they shaved off hair and beard, put on ocher robes, and went forth. Where they "
            "truly understood <em>this is suffering, this is its origin, this is its cessation, this "
            "is the practice leading to its cessation</em>. And where they realized the undefiled "
            "freedom of heart and freedom by wisdom in this very life.",
            "Line the two lists up. Birth answers to going forth &mdash; both are the beginning of a "
            "life, one received and one undertaken. Coronation answers to understanding the four "
            "truths &mdash; both the moment of becoming what one is going to be. And the decisive "
            "battle answers to the ending of the defilements &mdash; both a victory, except that the "
            "second has no opponent outside the person who wins it.",
            "That third correspondence is the discourse&rsquo;s sharpest move and it is made without "
            "comment. A king&rsquo;s greatest day is the day he defeated somebody. A "
            "mendicant&rsquo;s is the day nothing was left to defeat."]),
        ("Why places", [
            "The Pāli is specific: these are <em>places</em>, not moments. <em>Sāraṇīya</em> is worth "
            "remembering, worth calling to mind; and what is to be remembered is where the thing "
            "happened.",
            "That the canon locates spiritual events geographically is not incidental. The four places "
            "the Buddha is elsewhere said to name as worth seeing &mdash; where he was born, awakened, "
            "first taught, and passed away &mdash; are the origin of Buddhist pilgrimage, and the "
            "logic here is the same. A realization has an address.",
            "For a modern reader who has met Buddhism mostly as an interior practice, this is worth "
            "sitting with. The discourse does not tell a mendicant to remember three states of mind. "
            "It tells them to remember three locations, which means their practice is a thing that "
            "happened somewhere, on a particular day, in a body that was standing in a particular "
            "field."]),
        ("Teaching it", [
            "The exercise this discourse suggests almost writes itself, and it works with any group. "
            "The king&rsquo;s list is easy to construct for oneself &mdash; where you were born, where "
            "you were given what you have, where you won. The mendicant&rsquo;s list is harder and the "
            "difficulty is instructive: most people can name the first, few can name the second, and "
            "the third is not available.",
            "Read that way the discourse is not a criticism of kings but a description of an "
            "incomplete list, and the incompleteness is the ordinary condition. AN 3.13, the next "
            "discourse, is about exactly that: what it is like to be partway through such a list, and "
            "what it is like not to be on it at all."]),
    ],
    terms=[
        ("sāraṇīya",
         "&ldquo;worth remembering, to be called to mind&rdquo; &mdash; from the root for memory. The "
         "discourse&rsquo;s name, and said of places rather than of events."),
        ("muddhāvasitta",
         "&ldquo;anointed on the head&rdquo; &mdash; the coronation rite that makes a king, and the "
         "second of his three places."),
        ("agārasmā anagāriyaṁ pabbajati",
         "&ldquo;goes forth from the lay life to homelessness&rdquo; &mdash; the standard formula for "
         "ordination, and the mendicant&rsquo;s first place."),
        ("cetovimutti / paññāvimutti",
         "&ldquo;freedom of heart&rdquo; and &ldquo;freedom by wisdom&rdquo; &mdash; realized "
         "together at the mendicant&rsquo;s third place, answering to the king&rsquo;s battle."),
        ("āsavānaṁ khayā",
         "&ldquo;due to the ending of defilements&rdquo; &mdash; the phrase that marks the third "
         "place as an ending rather than an achievement over anyone."),
    ],
    text_intro=(
        "The discourse in full: the king&rsquo;s three places, then the mendicant&rsquo;s. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The three places a king commemorates"),
        ("p", "&sect;1", "an3.12:1.1-1.4"),
        ("p", "&sect;2&ndash;3", "an3.12:2.1-3.3"),
        ("h3", "And the three a mendicant should"),
        ("p", "&sect;4", "an3.12:4.1-4.4"),
        ("p", "&sect;5&ndash;6", "an3.12:5.1-6.3"),
    ],
    quiz=[
        {"q": "Which three places does an anointed king commemorate?",
         "opts": [
             "Where he was born, where he was anointed, and where he won victory in battle",
             "His palace, his temple, and his treasury",
             "Where he was married, where his heir was born, and where he died",
             "Three cities of his realm"],
         "correct": 0,
         "expl": "What you were given, what you were granted, and what you took."},
        {"q": "How many of the king&rsquo;s three depend entirely on other people?",
         "opts": ["None", "Two &mdash; a king does not choose to be born royal or anoint himself",
                  "All three", "One"],
         "correct": 1,
         "expl": "And the third is a victory over someone else."},
        {"q": "Which three places should a mendicant commemorate?",
         "opts": [
             "Where they were born, ordained, and will die",
             "Where they went forth; where they truly understood the four truths; and where they realized freedom of heart and freedom by wisdom",
             "Three monasteries",
             "Where they first heard the Dhamma, first gave alms, and first meditated"],
         "correct": 1,
         "expl": "The parallel with the king's list is exact."},
        {"q": "What does the discourse&rsquo;s sharpest correspondence pair?",
         "opts": [
             "Birth with going forth",
             "Coronation with understanding the truths",
             "The decisive battle with the ending of the defilements &mdash; both a victory, except that the second has no opponent outside the person who wins it",
             "Nothing; the lists are unrelated"],
         "correct": 2,
         "expl": "A king's greatest day is the day he defeated somebody; a mendicant's is the day nothing was left to defeat."},
        {"q": "Does the discourse criticize the king&rsquo;s list?",
         "opts": [
             "Yes, explicitly",
             "No &mdash; it is stated as a plain fact and the tone is neutral; the critique, if there is one, is entirely in the parallel",
             "Yes, by calling it worldly",
             "The discourse does not mention a king"],
         "correct": 1,
         "expl": "The substitution does the work without comment."},
        {"q": "What is notable about the Pāli specifying <em>places</em>?",
         "opts": [
             "Nothing; places and moments are the same",
             "The canon locates spiritual events geographically &mdash; a realization has an address, which is the same logic behind the four places of Buddhist pilgrimage",
             "It means the events are legendary",
             "It restricts the teaching to India"],
         "correct": 1,
         "expl": "The discourse does not tell a mendicant to remember three states of mind."},
        {"q": "Why does the guide say that is worth sitting with?",
         "opts": [
             "Because pilgrimage is required",
             "Because for a reader who has met Buddhism mostly as an interior practice, it means the practice is a thing that happened somewhere, on a particular day, in a body standing in a particular field",
             "Because places can be visited",
             "Because geography is doctrinally important"],
         "correct": 1,
         "expl": "Three locations, not three states."},
        {"q": "What exercise does the guide propose?",
         "opts": [
             "Memorizing the Pāli names",
             "Constructing both lists for oneself &mdash; most people can name the first of the mendicant&rsquo;s three, few can name the second, and the third is not available",
             "Visiting the four pilgrimage places",
             "Reciting the four truths daily"],
         "correct": 1,
         "expl": "The difficulty of the second list is the instructive part."},
        {"q": "How does that reading change the discourse?",
         "opts": [
             "It becomes a criticism of kings",
             "It becomes a description of an incomplete list, and the incompleteness is the ordinary condition",
             "It becomes irrelevant to laypeople",
             "It becomes a rule"],
         "correct": 1,
         "expl": "Which is exactly what AN 3.13 takes up next."},
        {"q": "What does <em>sāraṇīya</em> mean?",
         "opts": [
             "&ldquo;Worth remembering, to be called to mind&rdquo; &mdash; from the root for memory",
             "&ldquo;Sacred&rdquo;",
             "&ldquo;Hidden&rdquo;",
             "&ldquo;Distant&rdquo;"],
         "correct": 0,
         "expl": "The discourse's name, and said of places rather than of events."},
    ],
    marginalia=[
        ("A king&rsquo;s three", [
            "where he was born",
            "where he was anointed",
            "where he won the battle",
        ]),
        ("A mendicant&rsquo;s three", [
            "where they went forth",
            "where they understood the truths",
            "where the defilements ended",
        ]),
        ("The third pairing", [
            "a victory over someone",
            "a victory with no opponent",
        ]),
        ("Cross-references", [
            "AN 2.52&ndash;63 &middot; Buddha and monarch paired",
            "AN 3.13 &middot; next: partway through the list",
            "AN 3.14 &middot; the monarch&rsquo;s own king",
        ]),
    ],
    further=[
        '<a href="%s/an3.12/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.52-63.html">AN 2.52&ndash;63 &middot; Individuals</a> &mdash; where the Buddha '
        "and the wheel-turning monarch are paired four times in public standing but never in "
        "attainment, which is the same move this discourse makes with three places.",
        '<a href="an-3.13.html">AN 3.13 &middot; Hopes</a> &mdash; next in this series, on what it is '
        "like to be partway through such a list, and what it is like not to be on it.",
    ],
)


page(
    13, "Āsaṁsa", "Hopes",
    vagga=VAGGA_2,
    meta_title="AN 3.13 — Hopes | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Āsaṁsasutta — the "
        "hopeless, the hopeful, and the one who has done away with hope, illustrated first "
        "with a royal succession and then with the Saṅgha. The chapter's caste and disability "
        "language read honestly. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals defined and illustrated among laypeople, then the same three "
                 "among mendicants, on a strict parallel"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "Comparable three-person typologies appear in the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the structure is clear; the "
                       "illustration in the first half needs handling"),
    ],
    why=(
        "Three individuals: the hopeless, the hopeful, and the one who has done away with hope. The "
        "first and third look alike from outside &mdash; neither of them thinks <em>when will it be "
        "my turn?</em> &mdash; and the discourse&rsquo;s whole point is that they are opposites. But "
        "the illustration it uses for the first is a passage about caste and disability that reads "
        "badly today and should not be passed over, and the illustration it uses for the third has an "
        "internal tension with the discourse two pages later. Both are worth facing."),
    guide=[
        ("The teaching in one sentence", [
            "Hopelessness and the end of hope produce the same silence and are opposite conditions."]),
        ("The structure", [
            "Three individuals, each defined by what does or does not occur to them on hearing a "
            "particular piece of news. The hopeless person hears that someone has been made king and "
            "it never occurs to them to wonder when their own turn will come. The hopeful person "
            "hears it and does wonder. The person who has done away with hope hears it and does not "
            "wonder &mdash; because they have already been crowned.",
            "So the first and third are behaviorally identical and causally opposite. One does not "
            "hope because it is unimaginable; the other does not hope because it is finished. That is "
            "a genuinely acute observation and it survives entirely intact into the second half, "
            "where the news is that a certain mendicant has realized freedom.",
            "The three among mendicants are: the unethical person, of bad qualities, &ldquo;rotten "
            "inside, festering, and depraved,&rdquo; to whom it never occurs that they might be freed; "
            "the ethical person, to whom it does occur; and the perfected one, to whom it does not, "
            "because <em>the former hope they had to be freed has now died down</em>."]),
        ("The caste and disability passage", [
            "The illustration of the hopeless layperson is the difficult part, and it should be read "
            "rather than summarized. The person is born into a low family &mdash; corpse-workers, "
            "bamboo-workers, hunters, chariot-makers, scavengers &mdash; poor, with little food, where "
            "life is tough. And then: ugly, deformed, sickly, one-eyed, crippled, lame, or "
            "half-paralyzed, without food, clothing, or shelter.",
            "There is no version of this that a modern reader will find comfortable, and the honest "
            "things to say about it are limited but real. First, what the passage is doing "
            "structurally: it is constructing the most extreme case of social impossibility available "
            "to its audience, in order to make vivid a state of mind &mdash; the state in which a "
            "certain future does not present itself as a possibility at all. The disability terms are "
            "there for the same reason as the poverty terms, as intensifiers.",
            "Second, what that does not excuse: the passage treats birth and bodily condition as "
            "self-evidently marking a person as beyond hope, and it does so without comment. That is a "
            "view about caste and about disabled people, and it is in the text. A reader who finds it "
            "objectionable is not misreading it.",
            "Third, what the same canon does elsewhere, which is not a defense but is part of an "
            "accurate picture. The Buddha is repeatedly shown rejecting birth as a determinant of "
            "worth, ordaining people from exactly these occupations, and telling brahmins that one is "
            "not noble by birth but by conduct. Upāli, on whom the entire monastic law depends, is "
            "remembered as a barber. The second half of this very discourse relocates hopelessness "
            "from birth to conduct: among mendicants, the hopeless person is hopeless because they are "
            "corrupt, not because of how they were born.",
            "That last point is the most useful thing to teach here. The discourse&rsquo;s two halves "
            "do not use the same criterion, and the shift from the first to the second is a shift "
            "from a social fact to a moral one."]),
        ("The chariot-maker", [
            "One detail in the list of low families is worth pointing out because of what happens two "
            "discourses later. <em>Rathakāra</em>, chariot-maker, is named here among the occupations "
            "that mark a hopeless birth. AN 3.15 &mdash; which gives this whole chapter its name "
            "&mdash; is the story of a chariot-maker, and it ends with the Buddha saying "
            "<em>I myself was the chariot-maker at that time</em>.",
            "The two passages sit four pages apart in the same chapter. Nothing in the text "
            "acknowledges the tension and it may well be accidental, since the Aṅguttara assembles "
            "material by number rather than by theme. But a reader who notices it has noticed "
            "something real, and pointing it out is a better use of a class than smoothing it over: "
            "the collection lists chariot-making among the marks of a hopeless birth, and then has "
            "the Buddha claim the trade as his own."]),
        ("What &ldquo;done away with hope&rdquo; means", [
            "The third individual is <em>vigatāsa</em>, hope-departed, and the phrase for why is "
            "precise: <em>the former hope they had to be freed has now died down</em>. Not abandoned, "
            "not renounced &mdash; <em>paṭippassaddhā</em>, stilled, settled, calmed. The hope has not "
            "been given up as a fault. It has stopped because it has been satisfied.",
            "That matters because Buddhism is often presented as recommending the abandonment of hope "
            "on the grounds that hope is a form of craving. This discourse does not do that. The "
            "hopeful mendicant is the ethical one, and hoping to be freed is what an ethical "
            "practitioner does. Hope ends when it is met, and its ending is not something to aim at "
            "separately from the thing hoped for."]),
    ],
    terms=[
        ("āsaṁsa",
         "&ldquo;hope, expectation&rdquo; &mdash; the discourse&rsquo;s name and the axis of its "
         "three-person typology."),
        ("nirāsa / āsaṁsa / vigatāsa",
         "&ldquo;hopeless,&rdquo; &ldquo;hopeful,&rdquo; and &ldquo;hope-departed&rdquo; &mdash; the "
         "first and third behaviorally identical and causally opposite."),
        ("paṭippassaddhā",
         "&ldquo;died down, stilled, calmed&rdquo; &mdash; what happens to the hope of the perfected "
         "one. Not abandoned or renounced; satisfied."),
        ("nīce kule",
         "&ldquo;in a low family&rdquo; &mdash; the phrase introducing the caste passage, followed by "
         "a list of occupations including <em>rathakāra</em>, chariot-maker."),
        ("dussīla pāpadhamma",
         "&ldquo;unethical, of bad qualities&rdquo; &mdash; the criterion for hopelessness in the "
         "second half, where conduct replaces birth."),
    ],
    text_intro=(
        "The discourse in full: the three individuals among people at large, then the same three "
        "among mendicants. The first illustration includes a passage on caste and bodily condition "
        "that the reading guide addresses directly. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The hopeless, the hopeful, and the one who has done away with hope"),
        ("p", "&sect;1", "an3.13:1.1-1.11"),
        ("p", "&sect;2", "an3.13:2.1-2.7"),
        ("p", "&sect;3", "an3.13:3.1-3.10"),
        ("h3", "The same three among mendicants"),
        ("p", "&sect;4", "an3.13:4.1-4.10"),
        ("p", "&sect;5", "an3.13:5.1-5.7"),
        ("p", "&sect;6", "an3.13:6.1-6.10"),
    ],
    quiz=[
        {"q": "What do the hopeless person and the one who has done away with hope have in common?",
         "opts": [
             "Both are unethical",
             "Neither thinks &ldquo;when will it be my turn?&rdquo; &mdash; they are behaviorally identical and causally opposite",
             "Both have been crowned",
             "Both are mendicants"],
         "correct": 1,
         "expl": "One does not hope because it is unimaginable; the other because it is finished."},
        {"q": "Who are the three among mendicants?",
         "opts": [
             "The unethical person, the ethical person, and the perfected one",
             "The novice, the trainee, and the elder",
             "The forest dweller, the village dweller, and the wanderer",
             "The teacher, the student, and the donor"],
         "correct": 0,
         "expl": "The news they hear is that a certain mendicant has realized freedom."},
        {"q": "What does the guide say the caste and disability passage is doing structurally?",
         "opts": [
             "Making a doctrinal claim about rebirth",
             "Constructing the most extreme case of social impossibility available to its audience, to make vivid a state of mind in which a certain future does not present itself as a possibility at all",
             "Describing a specific historical person",
             "Listing occupations open to monastics"],
         "correct": 1,
         "expl": "The disability terms are there for the same reason as the poverty terms, as intensifiers."},
        {"q": "What does the guide say that does <em>not</em> excuse?",
         "opts": [
             "Nothing needs excusing",
             "That the passage treats birth and bodily condition as self-evidently marking a person as beyond hope, without comment &mdash; a view about caste and about disabled people that is in the text",
             "The length of the discourse",
             "The use of a royal illustration"],
         "correct": 1,
         "expl": "A reader who finds it objectionable is not misreading it."},
        {"q": "What does the same canon do elsewhere, as part of an accurate picture?",
         "opts": [
             "Repeats the same view without variation",
             "Shows the Buddha rejecting birth as a determinant of worth, ordaining people from these occupations, and telling brahmins one is noble by conduct rather than birth &mdash; and Upāli, on whom the monastic law depends, is remembered as a barber",
             "Never mentions caste",
             "Endorses the caste system explicitly"],
         "correct": 1,
         "expl": "Not a defense, but part of an accurate picture."},
        {"q": "What is the most useful thing to teach about the discourse&rsquo;s two halves?",
         "opts": [
             "That they are identical",
             "That they do not use the same criterion &mdash; the shift from the first to the second is a shift from a social fact to a moral one",
             "That the second half is later",
             "That only the second half is authentic"],
         "correct": 1,
         "expl": "Among mendicants, the hopeless person is hopeless because they are corrupt, not because of how they were born."},
        {"q": "What tension does the guide point out with AN 3.15?",
         "opts": [
             "None",
             "<em>Rathakāra</em>, chariot-maker, is listed here among the occupations marking a hopeless birth &mdash; and AN 3.15 ends with the Buddha saying &ldquo;I myself was the chariot-maker at that time&rdquo;",
             "AN 3.15 repeats the caste list",
             "AN 3.15 corrects this discourse"],
         "correct": 1,
         "expl": "Four pages apart in the same chapter, and nothing in the text acknowledges it."},
        {"q": "How does the guide suggest handling that tension?",
         "opts": [
             "Smoothing it over",
             "Pointing it out &mdash; it may well be accidental, since the Aṅguttara assembles by number rather than theme, but a reader who notices it has noticed something real",
             "Treating it as proof of forgery",
             "Ignoring AN 3.15"],
         "correct": 1,
         "expl": "A better use of a class than smoothing it over."},
        {"q": "What does <em>paṭippassaddhā</em> say about the perfected one&rsquo;s hope?",
         "opts": [
             "That it was abandoned as a fault",
             "That it has died down, stilled, calmed &mdash; it stopped because it was satisfied",
             "That it was never present",
             "That it was replaced by a greater hope"],
         "correct": 1,
         "expl": "Not abandoned or renounced."},
        {"q": "What common presentation of Buddhism does this discourse cut against?",
         "opts": [
             "That Buddhism recommends abandoning hope on the grounds that hope is a form of craving &mdash; here the hopeful mendicant is the ethical one, and hope ends when it is met",
             "That Buddhism values ethics",
             "That Buddhism has stages of attainment",
             "That Buddhism uses similes"],
         "correct": 0,
         "expl": "The ending of hope is not something to aim at separately from the thing hoped for."},
    ],
    marginalia=[
        ("Three individuals", [
            "<span class=\"pali\">nirāsa</span>hopeless",
            "<span class=\"pali\">āsaṁsa</span>hopeful",
            "<span class=\"pali\">vigatāsa</span>hope departed",
            "&mdash; first and third look alike",
        ]),
        ("Two criteria", [
            "first half &middot; birth and body",
            "second half &middot; conduct",
            "&mdash; not the same test",
        ]),
        ("A tension", [
            "3.13 &middot; chariot-maker, a low birth",
            "3.15 &middot; &ldquo;I was the chariot-maker&rdquo;",
        ]),
        ("Cross-references", [
            "AN 3.15 &middot; the chariot-maker",
            "AN 3.12 &middot; an incomplete list",
            "Dhammapada 26 &middot; noble by conduct",
        ]),
    ],
    further=[
        '<a href="%s/an3.13/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../dhammapada/dhp-26.html">Dhammapada 26 &middot; Brahmins</a> &mdash; the '
        "collection&rsquo;s sustained argument that one is not noble by birth but by conduct, which "
        "is the other half of the canon&rsquo;s position on what this discourse illustrates with.",
        '<a href="an-3.15.html">AN 3.15 &middot; About Pacetana</a> &mdash; where the Buddha names '
        "himself a chariot-maker, four pages after chariot-making appears in a list of hopeless "
        "births.",
        '<a href="an-1.219-234.html">AN 1.219&ndash;234 &middot; Foremost Monks (IV)</a> &mdash; '
        "Upāli, remembered as a barber, foremost in the monastic law and reciting it at the first "
        "council.",
    ],
)


page(
    14, "Cakkavatti", "The Wheel-Turning Monarch",
    vagga=VAGGA_2,
    meta_title="AN 3.14 — The Wheel-Turning Monarch | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Cakkavattisutta — "
        "even a universal monarch has a king above him, and it is principle; and the Buddha "
        "rules the same way, over actions of body, speech, and mind. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", "The Buddha, answering a question from one of the mendicants"),
        ("Form", "A cryptic statement, a question from the assembly, and the answer worked out on "
                 "both sides of a parallel"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The wheel-turning monarch ruling by Dharma is a standard theme across "
                              "the Chinese Āgamas and shaped Buddhist political thought in East Asia; "
                              "this reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short, and one of the most "
                       "consequential political passages in the canon"),
    ],
    why=(
        "&ldquo;Even a wheel-turning monarch does not wield power without having their own king.&rdquo; "
        "A monk asks the obvious question &mdash; who is the king of a universal monarch? &mdash; and "
        "the answer is one word: <em>dhamma</em>. Principle. What follows is the working out of that "
        "on two sides: how a king rules under principle, and how a Buddha does. It is the passage "
        "every Buddhist polity from Aśoka onward reached for, and its logic is worth having exactly "
        "right."),
    guide=[
        ("The teaching in one sentence", [
            "The highest human authority is itself under an authority, and so is the Buddha; the name "
            "of that authority is principle."]),
        ("The claim, and the question it provokes", [
            "The opening sentence is deliberately incomplete: even a wheel-turning monarch, a just and "
            "principled king, does not wield power <em>arājaka</em> &mdash; kingless. The word is "
            "arresting because a <em>cakkavatti</em> is by definition the one who has no superior; "
            "there is nobody above him in the political order.",
            "A monk asks. That in itself is worth noticing: the discourse is structured so that the "
            "answer is requested rather than volunteered, and the request comes from the assembly. It "
            "is a small piece of pedagogy embedded in a political teaching.",
            "The answer is <em>dhammo</em>. Sujato renders it &ldquo;principle,&rdquo; a choice worth "
            "flagging: the word could equally be &ldquo;the Dhamma,&rdquo; &ldquo;the law,&rdquo; or "
            "&ldquo;the teaching,&rdquo; and translators differ. The rendering matters, because "
            "&ldquo;principle&rdquo; keeps the claim general &mdash; the king is under a standard, not "
            "under a religion &mdash; while &ldquo;the Dhamma&rdquo; would make it the Buddha&rsquo;s "
            "teaching specifically. The Pāli does not settle it, and both readings had long careers."]),
        ("What ruling under principle looks like", [
            "The king honors, respects, and venerates principle, and has it as his flag, banner, and "
            "authority. Then the substance: he provides just protection and security for his court, "
            "his aristocrats and vassals, his troops, brahmins and householders, town and country "
            "people, ascetics and brahmins &mdash; and <em>beasts and birds</em>.",
            "That last item is not decorative. The list runs from the innermost circle of power "
            "outward through every human class to animals, and the same obligation covers all of them. "
            "A monarch whose legitimacy rests on providing protection to birds is a considerable "
            "distance from a monarch whose legitimacy rests on conquest, and the canon says this "
            "twice: this discourse and AN 3.12 together describe a king who commemorates his battle "
            "and a king who is obligated to wildlife.",
            "The consequence stated is worth quoting precisely: when he has done this, he wields power "
            "only in a principled manner, <em>and this power cannot be undermined by any human "
            "enemy</em>. The claim is not that principled rule is morally preferable. It is that it is "
            "structurally secure, which is a different and more interesting argument."]),
        ("And how a Buddha rules", [
            "The parallel is exact and the domain is different. The Realized One, also called here a "
            "just and principled king, provides protection and security not over subjects but over "
            "<em>actions</em>: this kind of bodily action should be cultivated, this kind should not; "
            "and the same for speech and for mind.",
            "So the Buddha&rsquo;s realm is conduct, and his governing is the drawing of that line. He "
            "too rules under principle rather than by personal authority &mdash; which is the "
            "discourse&rsquo;s most important claim and the one most easily missed. The Buddha is not "
            "the source of what should and should not be cultivated. He is, on this account, the one "
            "who sees it and says so, standing under the same authority he points to.",
            "That reading is consistent with the rest of the canon. It is why AN 3.65 can tell the "
            "Kālāmas to test claims against observed consequences rather than against a "
            "teacher&rsquo;s authority, and why AN 1.276 says someone accomplished in view cannot "
            "dedicate themselves to another teacher &mdash; there is nothing to transfer, because the "
            "authority was never personal.",
            "The discourse closes on the wheel: having done this, he rolls forth the supreme Wheel of "
            "Dhamma, and it <em>cannot be rolled back</em> by any ascetic, brahmin, god, Māra, "
            "divinity, or anyone in the world. The same structural security claimed for the "
            "principled king is claimed for the teaching."]),
        ("What was made of it", [
            "This passage, and the wheel-turning monarch material generally, is the foundation of "
            "Buddhist political theory. Aśoka&rsquo;s edicts read as an attempt to govern by it; "
            "every later Buddhist kingdom in South and Southeast Asia and in East Asia invoked the "
            "<em>cakkavatti</em> ideal; and the claim that a ruler is subject to Dhamma rather than "
            "the source of it is the closest thing early Buddhism has to a constitutional principle.",
            "It should be said that the ideal was invoked at least as often to legitimate power as to "
            "constrain it. A king who declares himself a wheel-turning monarch has claimed the highest "
            "available title, and the obligations attached to it are enforced by nobody. That is a "
            "real limitation of the doctrine and it is visible in the history. But the text itself is "
            "unambiguous about the direction of authority, and a ruler who invoked it was at least "
            "invoking something that could be quoted back at them."]),
    ],
    terms=[
        ("cakkavatti",
         "&ldquo;wheel-turning monarch&rdquo; &mdash; the universal righteous king, who by definition "
         "has no political superior, which is what makes the discourse&rsquo;s opening arresting."),
        ("arājaka",
         "&ldquo;kingless, without a king&rdquo; &mdash; the word the Buddha denies of even a "
         "universal monarch."),
        ("dhamma",
         "the answer to the monk&rsquo;s question. Sujato renders it &ldquo;principle&rdquo;; the word "
         "could equally be &ldquo;the Dhamma,&rdquo; &ldquo;the law,&rdquo; or &ldquo;the teaching,&rdquo; "
         "and the choice affects whether the king is under a standard or under a religion."),
        ("dhammiraṁ rakkhāvaraṇaguttiṁ",
         "&ldquo;just protection and security&rdquo; &mdash; what the king provides to every class of "
         "subject, ending with beasts and birds, and what the Buddha provides regarding actions."),
        ("dhammacakka",
         "&ldquo;the Wheel of Dhamma&rdquo; &mdash; rolled forth once the protection is established, "
         "and said to be unrollable-back by anyone in the world."),
    ],
    text_intro=(
        "The discourse in full: the opening claim, the monk&rsquo;s question, and the answer worked "
        "out for a king and for a Buddha. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Who is the king of a universal monarch?"),
        ("p", "&sect;1", "an3.14:1.1-1.5"),
        ("h3", "How a king rules under principle"),
        ("p", "&sect;2", "an3.14:2.1-2.3"),
        ("h3", "And how a Realized One does"),
        ("p", "&sect;3&ndash;4", "an3.14:3.1-4.3"),
        ("p", "&sect;5", "an3.14:5.1-5.2"),
    ],
    quiz=[
        {"q": "Why is the discourse&rsquo;s opening sentence arresting?",
         "opts": [
             "Because it names a specific king",
             "Because a <em>cakkavatti</em> is by definition the one who has no political superior, and the Buddha says even he is not kingless",
             "Because it is spoken by a monk",
             "Because it contradicts AN 3.12"],
         "correct": 1,
         "expl": "There is nobody above him in the political order."},
        {"q": "How does the answer come?",
         "opts": [
             "The Buddha volunteers it",
             "A monk asks, so the answer is requested rather than volunteered &mdash; a small piece of pedagogy embedded in a political teaching",
             "It is not given",
             "A king asks"],
         "correct": 1,
         "expl": "And the request comes from the assembly."},
        {"q": "What is the answer, and why does the rendering matter?",
         "opts": [
             "<em>Dhamma</em> &mdash; and &ldquo;principle&rdquo; keeps the claim general, while &ldquo;the Dhamma&rdquo; would make it the Buddha&rsquo;s teaching specifically",
             "<em>Kamma</em> &mdash; and the rendering is settled",
             "<em>Saṅgha</em>",
             "<em>Nibbāna</em>"],
         "correct": 0,
         "expl": "The Pāli does not settle it, and both readings had long careers."},
        {"q": "Who is on the list of those the king must protect?",
         "opts": [
             "Only his court and army",
             "His court, aristocrats, vassals, troops, brahmins and householders, town and country people, ascetics and brahmins &mdash; and beasts and birds",
             "Only monastics",
             "Only his own people"],
         "correct": 1,
         "expl": "The list runs from the innermost circle of power outward to animals, with the same obligation covering all."},
        {"q": "Why does the guide say the last item is not decorative?",
         "opts": [
             "Because birds were sacred",
             "Because a monarch whose legitimacy rests on providing protection to birds is a considerable distance from one whose legitimacy rests on conquest",
             "Because animals could not be taxed",
             "Because the Vinaya requires it"],
         "correct": 1,
         "expl": "And AN 3.12 has just described a king who commemorates his battle."},
        {"q": "What consequence does the discourse claim for principled rule?",
         "opts": [
             "That it is morally preferable",
             "That the power cannot be undermined by any human enemy &mdash; a claim about structural security rather than about moral preference",
             "That it produces wealth",
             "That it guarantees a long reign"],
         "correct": 1,
         "expl": "A different and more interesting argument."},
        {"q": "What is the Buddha&rsquo;s realm, on the parallel?",
         "opts": [
             "Subjects and territory",
             "Actions &mdash; this kind of bodily, verbal, and mental action should be cultivated, and this kind should not",
             "The Saṅgha only",
             "The heavens"],
         "correct": 1,
         "expl": "His governing is the drawing of that line."},
        {"q": "What is the discourse&rsquo;s most important and most easily missed claim?",
         "opts": [
             "That the Buddha rules under principle rather than by personal authority &mdash; he is not the source of what should be cultivated but the one who sees it and says so",
             "That kings should be Buddhists",
             "That monarchs are superior to monastics",
             "That the wheel can be rolled back"],
         "correct": 0,
         "expl": "Standing under the same authority he points to."},
        {"q": "Which other passages does the guide say that reading is consistent with?",
         "opts": [
             "AN 3.65, telling the Kālāmas to test claims against consequences rather than a teacher&rsquo;s authority, and AN 1.276, where someone accomplished in view cannot dedicate themselves to another teacher",
             "AN 1.1&ndash;10 and AN 2.1",
             "AN 2.141&ndash;150",
             "AN 3.13 alone"],
         "correct": 0,
         "expl": "There is nothing to transfer, because the authority was never personal."},
        {"q": "What limitation of the doctrine does the guide name?",
         "opts": [
             "That it is unclear",
             "That the ideal was invoked at least as often to legitimate power as to constrain it, and the obligations attached to the title are enforced by nobody",
             "That kings never used it",
             "That it applies only to India"],
         "correct": 1,
         "expl": "A real limitation, visible in the history &mdash; though a ruler who invoked it was invoking something that could be quoted back at them."},
    ],
    marginalia=[
        ("The question", [
            "even a <span class=\"pali\">cakkavatti</span>",
            "is not <span class=\"pali\">arājaka</span>",
            "&mdash; who is his king?",
        ]),
        ("The answer", [
            "<span class=\"pali\">dhammo</span>principle",
            "his flag, banner, and authority",
        ]),
        ("Two realms", [
            "the king &middot; subjects, down to birds",
            "the Buddha &middot; actions of body, speech, mind",
            "&mdash; both under principle",
        ]),
        ("Cross-references", [
            "AN 3.12 &middot; the king who commemorates a battle",
            "AN 3.65 &middot; authority is not personal",
            "AN 2.52&ndash;63 &middot; the pair, elsewhere",
        ]),
    ],
    further=[
        '<a href="%s/an3.14/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.65.html">AN 3.65 &middot; With the Kālāmas of Kesamutta</a> &mdash; the '
        "discourse that makes the same point from the listener&rsquo;s side: what settles a claim is "
        "not who said it.",
        '<a href="an-2.52-63.html">AN 2.52&ndash;63 &middot; Individuals</a> &mdash; where the Buddha '
        "and the wheel-turning monarch are paired in public standing but never in attainment.",
        '<a href="an-3.15.html">AN 3.15 &middot; About Pacetana</a> &mdash; next in this series, '
        "and the chapter&rsquo;s namesake.",
    ],
)


page(
    15, "Sacetana", "About Pacetana",
    vagga=VAGGA_2,
    meta_title="AN 3.15 — About Pacetana | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sacetanasutta — the "
        "chariot-maker who took six months over one wheel and six days over the other, and "
        "the Buddha's statement that he was the chariot-maker. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Varanasi, in the deer park at Isipatana &mdash; the site of the first teaching, "
                    "named here rather than the chapter&rsquo;s usual Sāvatthī"),
        ("Speakers", "The Buddha, narrating a story of his own past life"),
        ("Form", "A narrative with dialogue, a demonstration, an explanation, and the "
                 "speaker&rsquo;s identification of himself with its main character"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The story appears in the Chinese Āgamas and in the wider Jātaka "
                              "literature; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a story, told plainly, with its "
                       "point stated at the end"),
    ],
    why=(
        "The best-told story in the first two chapters of the Threes, and the one that gives the "
        "chapter its name. A king orders a pair of chariot wheels six months before a battle. His "
        "chariot-maker finishes the first with six days to spare, then makes the second in those six "
        "days. The king cannot tell them apart. The wheels are then rolled, and the difference is "
        "immediate and total. It is a discourse about the invisibility of workmanship until the thing "
        "is used &mdash; and it ends with the Buddha saying he was the chariot-maker."),
    guide=[
        ("The teaching in one sentence", [
            "Crookedness that cannot be seen in a finished thing shows the moment the thing is put in "
            "motion."]),
        ("The arithmetic of the story", [
            "The timings are exact and worth following. Six months are allowed. At six days less than "
            "six months, one wheel is finished &mdash; so the first wheel took almost the whole "
            "period. The second is then made in the remaining six days.",
            "The story is careful to make the second wheel a real achievement rather than a botch. "
            "The chariot-maker says he can do it and does; the wheels are delivered on time; and the "
            "king, examining them, can see no difference at all. Nothing was skipped that shows. "
            "Whatever is wrong with the fast wheel is invisible to an interested and competent "
            "observer holding it in his hands.",
            "Then it is rolled. Both wheels roll as far as the initial push carries them. The fast one "
            "wobbles and falls. The slow one <em>stood still as if fixed to an axle</em> &mdash; it "
            "comes to rest upright, balanced, as though still mounted. The defect was in rim, spoke, "
            "and hub: crooked, flawed, and defective. Every part."]),
        ("What the simile is not about", [
            "It is easy to read this as a discourse about haste, and it is worth being precise, "
            "because it is not quite that. The chariot-maker was not rushed by his own impatience; he "
            "was given a deadline and met it. Nor is the point that the fast wheel is useless &mdash; "
            "it rolls exactly as far as the slow one.",
            "What separates them is what happens when the momentum runs out. Under the initial push "
            "the two are indistinguishable. The difference appears only when the wheel has to stand on "
            "its own accumulated trueness, and at that moment the fast wheel has nothing to draw on.",
            "Applied to a practitioner, which is what the discourse does, that is a specific and "
            "uncomfortable claim. Someone whose practice has crooks and flaws is not thereby "
            "incapable; they will go exactly as far as their initial impetus takes them &mdash; the "
            "enthusiasm of a new commitment, the momentum of a retreat, the push of a crisis. What "
            "they will not do is stand when it is spent."]),
        ("Rim, spoke, and hub", [
            "The three defective parts are given as three, which is what puts the story in the Threes, "
            "and the Buddha maps them onto three: the crooks, flaws, and defects of body, speech, and "
            "mind.",
            "The vocabulary is worth keeping. <em>Vaṅka</em> is crooked or bent; <em>dosa</em> is a "
            "flaw or blemish &mdash; the same word as the hatred in greed-hate-delusion, and here "
            "meaning something closer to a fault in material; <em>kasāva</em> is a stain or "
            "astringency, a defect running through the grain. Three different kinds of wrongness in a "
            "piece of wood: bent, blemished, impure.",
            "That is a more useful taxonomy of a person&rsquo;s faults than good and bad. Something "
            "bent has been forced out of true by pressure. Something blemished has a local fault. "
            "Something with <em>kasāva</em> is wrong all the way through and cannot be repaired by "
            "working on the surface."]),
        ("&ldquo;I myself was the chariot-maker&rdquo;", [
            "The turn at the end is the discourse&rsquo;s real content. The Buddha heads off the "
            "expected assumption &mdash; <em>you might think that chariot-maker must have been someone "
            "else; you should not see it like that</em> &mdash; and identifies himself with the "
            "craftsman. Then he draws the parallel exactly: <em>then I was skilled in the crooks, "
            "flaws, and defects of wood; now I am skilled in the crooks, flaws, and defects of actions "
            "by body, speech, and mind</em>.",
            "So the claim is about a transferred competence. What the Buddha has is not a different "
            "kind of faculty from a craftsman&rsquo;s but the same kind applied to a different "
            "material: the trained eye that sees a defect in something that looks finished. That is a "
            "remarkably deflationary self-description for a collection that elsewhere calls him "
            "unequaled and without peer, and the two pictures sit in the same nipāta.",
            "It is also worth putting beside AN 3.13, two discourses earlier, where chariot-makers "
            "appear in a list of low families whose members have no hope. Nothing in the text connects "
            "them and the juxtaposition may be accidental. But the Buddha of AN 3.15 claims a trade "
            "that AN 3.13 uses as an example of hopelessness, and a reader is entitled to notice."]),
    ],
    terms=[
        ("rathakāra",
         "&ldquo;chariot-maker&rdquo; &mdash; the trade the Buddha claims as his own in a past life, "
         "and one of the occupations listed at AN 3.13 as marking a hopeless birth."),
        ("vaṅka",
         "&ldquo;crooked, bent&rdquo; &mdash; the first of the three defects; something forced out of "
         "true."),
        ("dosa",
         "&ldquo;flaw, blemish&rdquo; &mdash; the second. The same word as the hatred of "
         "greed-hate-delusion, here meaning a fault in the material."),
        ("kasāva",
         "&ldquo;defect, stain, astringency&rdquo; &mdash; the third, running through the grain, and "
         "not repairable by working the surface."),
        ("nemi, ara, nābhi",
         "rim, spoke, and hub &mdash; the three parts of a wheel found defective, mapped onto actions "
         "of body, speech, and mind."),
    ],
    text_intro=(
        "The discourse in full: the story of King Pacetana&rsquo;s chariot-maker, the demonstration "
        "with the two wheels, and the Buddha&rsquo;s identification of himself with the craftsman. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "At Isipatana"),
        ("p", "&sect;1", "an3.15:1.1-1.5"),
        ("h3", "The two wheels"),
        ("p", "&sect;2", "an3.15:2.1-2.16"),
        ("p", "&sect;3", "an3.15:3.1-3.4"),
        ("p", "&sect;4", "an3.15:4.1-4.6"),
        ("h3", "&ldquo;I myself was the chariot-maker&rdquo;"),
        ("p", "&sect;5&ndash;6", "an3.15:5.1-6.1"),
        ("p", "&sect;7", "an3.15:7.1-7.3"),
    ],
    quiz=[
        {"q": "How long did each wheel take?",
         "opts": [
             "Both took six months",
             "The first took six days less than six months; the second was made in those remaining six days",
             "Both took six days",
             "The first took six days and the second six months"],
         "correct": 1,
         "expl": "The timings are exact and worth following."},
        {"q": "Could the king tell the wheels apart?",
         "opts": [
             "Yes, immediately",
             "No &mdash; examining them he could see no difference at all",
             "Only by weighing them",
             "The story does not say"],
         "correct": 1,
         "expl": "Whatever is wrong with the fast wheel is invisible to an interested and competent observer holding it."},
        {"q": "What happened when the wheels were rolled?",
         "opts": [
             "The fast one did not roll at all",
             "Both rolled as far as the initial push carried them; then the fast one wobbled and fell, and the slow one stood still as if fixed to an axle",
             "Both fell",
             "Both stood"],
         "correct": 1,
         "expl": "The difference appears only when the momentum runs out."},
        {"q": "Why does the guide say this is not quite a discourse about haste?",
         "opts": [
             "Because the chariot-maker was given a deadline and met it, and the fast wheel rolls exactly as far as the slow one",
             "Because no time is mentioned",
             "Because the king was at fault",
             "Because the wheels were identical"],
         "correct": 0,
         "expl": "What separates them is what happens when the momentum runs out."},
        {"q": "Applied to a practitioner, what is the claim?",
         "opts": [
             "That flawed practice is useless",
             "That they will go exactly as far as their initial impetus takes them &mdash; the enthusiasm of a new commitment, the momentum of a retreat, the push of a crisis &mdash; and will not stand when it is spent",
             "That practice takes six months",
             "That defects can be seen from outside"],
         "correct": 1,
         "expl": "Specific, and uncomfortable."},
        {"q": "Which three parts of the wheel were defective?",
         "opts": [
             "Rim, spoke, and hub &mdash; mapped onto actions of body, speech, and mind",
             "Axle, yoke, and pole",
             "Wood, iron, and leather",
             "Only the rim"],
         "correct": 0,
         "expl": "Three, which is what puts the story in the Threes."},
        {"q": "What do <em>vaṅka</em>, <em>dosa</em>, and <em>kasāva</em> distinguish?",
         "opts": [
             "Three degrees of severity",
             "Bent, blemished, and impure &mdash; something forced out of true, a local fault, and something wrong all the way through the grain",
             "Three kinds of wood",
             "Three stages of manufacture"],
         "correct": 1,
         "expl": "A more useful taxonomy of a person's faults than good and bad."},
        {"q": "Which of the three cannot be repaired by working the surface?",
         "opts": [
             "<em>Vaṅka</em>", "<em>Dosa</em>",
             "<em>Kasāva</em> &mdash; it runs through the grain", "All three can"],
         "correct": 2,
         "expl": "A stain or astringency running through the material."},
        {"q": "What does the Buddha say about the chariot-maker?",
         "opts": [
             "That he was a previous Buddha",
             "That he was someone else",
             "That he himself was the chariot-maker at that time &mdash; heading off the expected assumption first",
             "That the story is a parable with no historical claim"],
         "correct": 2,
         "expl": "&ldquo;You might think that chariot-maker must have been someone else; you should not see it like that.&rdquo;"},
        {"q": "What kind of claim does the guide say the identification makes?",
         "opts": [
             "A claim about miraculous powers",
             "A claim about transferred competence &mdash; the same trained eye that sees a defect in something that looks finished, applied to a different material",
             "A claim about caste",
             "A claim about the length of the path"],
         "correct": 1,
         "expl": "A remarkably deflationary self-description for a collection that elsewhere calls him unequaled."},
    ],
    marginalia=[
        ("The two wheels", [
            "six months less six days",
            "six days",
            "&mdash; indistinguishable in the hand",
        ]),
        ("Rolled", [
            "both go as far as the push",
            "one wobbles and falls",
            "one stands as if on an axle",
        ]),
        ("Three defects", [
            "<span class=\"pali\">vaṅka</span>bent",
            "<span class=\"pali\">dosa</span>blemished",
            "<span class=\"pali\">kasāva</span>wrong through the grain",
        ]),
        ("Cross-references", [
            "AN 3.13 &middot; chariot-makers, two pages earlier",
            "AN 3.12 &middot; the deer park at Isipatana",
            "AN 3.16 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.15/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.13.html">AN 3.13 &middot; Hopes</a> &mdash; two discourses earlier, where '
        "chariot-making appears in a list of occupations marking a hopeless birth.",
        '<a href="../samyutta-nikaya/sn-56.11.html">SN 56.11 &middot; Rolling Forth the Wheel of '
        "Dhamma</a> &mdash; spoken at Isipatana, the setting named here, and the reason a wheel is the "
        "canon&rsquo;s image for a teaching set in motion.",
    ],
)


page(
    16, "Apaṇṇaka", "Sure Bet",
    vagga=VAGGA_2,
    meta_title="AN 3.16 — Sure Bet | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Apaṇṇakasutta — "
        "guarding the sense doors, eating in moderation, and dedication to wakefulness, each "
        "defined in full. The three preliminaries that make a practice a sure bet. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three things named, then each defined at length in its own passage"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "This triad opens the gradual training in the Chinese Madhyama-āgama "
                              "(T26) as it does in the Pāli; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; entirely practical, and the most "
                       "immediately usable discourse in the chapter"),
    ],
    why=(
        "Three things, each given a full definition rather than a name: guarding the sense doors, "
        "eating in moderation, and dedication to wakefulness. A mendicant who has them is said to have "
        "a practice that is <em>apaṇṇaka</em> &mdash; a sure bet, a certainty, something that cannot "
        "come out wrong &mdash; and to have laid the groundwork for ending the defilements. The three "
        "are unglamorous to the point of being domestic: what you do with your attention, what you do "
        "with your food, and what you do with your night. That is the whole list."),
    guide=[
        ("The teaching in one sentence", [
            "Attention at the senses, moderation at meals, and a disciplined night are the groundwork "
            "on which the ending of defilements is possible."]),
        ("What <em>apaṇṇaka</em> claims", [
            "The word is a gambling term. <em>Apaṇṇaka</em> is the throw that cannot lose, the bet "
            "that is not a gamble &mdash; a sure thing. Applied to a practice it says something quite "
            "strong: that a practice built on these three is not a wager on an uncertain outcome.",
            "The second half of the sentence is more careful, though, and the two halves should be "
            "read together. Such a mendicant <em>has laid the groundwork for ending the "
            "defilements</em> &mdash; <em>āraddho</em>, begun, undertaken. Not completed. The claim is "
            "not that these three produce awakening; it is that with them in place the enterprise is "
            "no longer a gamble, and without them, whatever else is done, it is."]),
        ("Guarding the sense doors", [
            "The definition is the standard one and it is worth reading closely, because it is far "
            "more specific than &ldquo;be careful what you look at.&rdquo; On seeing a sight, the "
            "mendicant does not <em>get caught up in the features and details</em> &mdash; "
            "<em>nimittaggāhī</em> and <em>anubyañjanaggāhī</em>, seizing on the general mark and "
            "seizing on the particulars.",
            "Nothing here says not to see. The restraint operates after contact, on the elaboration: "
            "the move from <em>there is a face</em> to <em>there is a face, and here is what it means "
            "to me, and here is what I want from it</em>. The reason given is precise and "
            "consequential rather than moral: if the faculty were left unrestrained, covetousness and "
            "displeasure would become overwhelming.",
            "The list runs through all six &mdash; eye, ear, nose, tongue, body, mind &mdash; and the "
            "inclusion of mind is what makes the practice complete. Thoughts arrive at a sense door "
            "like anything else, and are seized on in exactly the same way. A practitioner who guards "
            "five and elaborates freely on the sixth has not understood the instruction."]),
        ("Eating in moderation", [
            "The definition is a reflection, given as a formula to be actually recited: not for fun, "
            "indulgence, adornment, or decoration, but to sustain the body, avoid harm, and support "
            "spiritual practice &mdash; to end old discomfort without producing new discomfort, and to "
            "have the means to keep going, blamelessness, and a comfortable abiding.",
            "Two features are worth pointing out. First, the four rejected motives are all about the "
            "body as display or entertainment; nothing rejects nourishment or even pleasure as such. "
            "Second, the positive formula is unusually accommodating: <em>a comfortable abiding</em> "
            "is named as one of the aims. This is not an austerity instruction. A person eating to "
            "this standard would eat enough, regularly, and without fuss.",
            "For lay students this reflection transfers directly, and is one of the few canonical "
            "formulas that can be used unmodified outside a monastic setting."]),
        ("Dedication to wakefulness", [
            "The definition is a timetable. Walking and sitting meditation by day; walking and sitting "
            "in the first watch of the night; in the middle watch, lying down in the lion&rsquo;s "
            "posture &mdash; on the right side, one foot on the other, mindful and aware, and "
            "<em>focused on the time of getting up</em>; and in the last watch, up again.",
            "That is roughly four hours of sleep, and it is worth being honest that this is a monastic "
            "regime and a demanding one. What transfers is not the schedule but two details inside it. "
            "The posture is specified, which makes lying down a described practice rather than the "
            "cessation of practice. And the mendicant goes to sleep <em>focused on the time of getting "
            "up</em> &mdash; the intention to rise is formed before sleep, not on waking.",
            "<em>Jāgariya</em>, wakefulness, is not primarily about hours. It is about the night not "
            "being a gap in which nothing is happening."]),
        ("Why these three", [
            "The selection is worth a comment because it is not obvious. Nothing here concerns "
            "doctrine, view, generosity, or ethics in the ordinary sense; there is no mention of the "
            "precepts. What the three have in common is that each governs a continuous, unavoidable, "
            "daily process &mdash; perceiving, eating, sleeping &mdash; that a person will engage in "
            "whether or not they practice.",
            "That is the logic of calling them groundwork. They are not additional activities to be "
            "fitted into a life; they are the three activities a life already consists of, done "
            "differently. Which is also why the discourse can call a practice built on them a sure "
            "bet: nothing about them depends on finding time."]),
    ],
    terms=[
        ("apaṇṇaka",
         "&ldquo;a sure bet, a certainty&rdquo; &mdash; a gambling term for the throw that cannot "
         "lose. Applied here to a practice, not to its outcome."),
        ("nimittaggāhī / anubyañjanaggāhī",
         "&ldquo;seizing on the features&rdquo; and &ldquo;on the details&rdquo; &mdash; what a "
         "guarded practitioner does not do. The restraint operates after contact, on the elaboration."),
        ("bhojane mattaññutā",
         "&ldquo;moderation in eating&rdquo; &mdash; literally knowing the measure in food, and "
         "defined by a reflection rather than by a quantity."),
        ("jāgariya",
         "&ldquo;wakefulness&rdquo; &mdash; defined by a timetable in three watches. Not primarily "
         "about hours but about the night not being a gap."),
        ("uṭṭhānasaññaṁ manasi karitvā",
         "&ldquo;focused on the time of getting up&rdquo; &mdash; the intention to rise is formed "
         "before sleep, not on waking."),
    ],
    text_intro=(
        "The discourse in full: the three named, then each defined. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Three things"),
        ("p", "&sect;1", "an3.16:1.1-1.3"),
        ("h3", "Guarding the sense doors"),
        ("p", "&sect;2", "an3.16:2.1-2.10"),
        ("h3", "Eating in moderation"),
        ("p", "&sect;3", "an3.16:3.1-3.4"),
        ("h3", "Dedication to wakefulness"),
        ("p", "&sect;4", "an3.16:4.1-4.4"),
    ],
    quiz=[
        {"q": "What are the three things?",
         "opts": [
             "Ethics, immersion, and wisdom",
             "Guarding the sense doors, eating in moderation, and dedication to wakefulness",
             "Faith, energy, and mindfulness",
             "Giving, ethics, and meditation"],
         "correct": 1,
         "expl": "What you do with your attention, your food, and your night."},
        {"q": "What does <em>apaṇṇaka</em> mean?",
         "opts": [
             "&ldquo;A sure bet&rdquo; &mdash; a gambling term for the throw that cannot lose",
             "&ldquo;Difficult&rdquo;",
             "&ldquo;Preliminary&rdquo;",
             "&ldquo;Complete&rdquo;"],
         "correct": 0,
         "expl": "Applied to a practice, not to its outcome."},
        {"q": "What is the second half of the claim?",
         "opts": [
             "That awakening follows automatically",
             "That such a mendicant has <em>laid the groundwork</em> for ending the defilements &mdash; begun, not completed",
             "That no further practice is needed",
             "That the defilements are already ended"],
         "correct": 1,
         "expl": "With these in place the enterprise is no longer a gamble; without them, whatever else is done, it is."},
        {"q": "What does guarding the sense doors actually restrain?",
         "opts": [
             "Seeing and hearing themselves",
             "The elaboration after contact &mdash; not seizing on the features and details",
             "Contact with laypeople",
             "Speech"],
         "correct": 1,
         "expl": "The move from &ldquo;there is a face&rdquo; to &ldquo;here is what I want from it.&rdquo;"},
        {"q": "What reason is given for the restraint?",
         "opts": [
             "That the senses are impure",
             "That it is required by the Vinaya",
             "That if the faculty were left unrestrained, covetousness and displeasure would become overwhelming &mdash; a consequential reason, not a moral one",
             "That teachers expect it"],
         "correct": 2,
         "expl": "Precise, and about what happens rather than about what is permitted."},
        {"q": "Why does the guide say the inclusion of mind completes the practice?",
         "opts": [
             "Because mind is the most important sense",
             "Because thoughts arrive at a sense door like anything else and are seized on in the same way &mdash; a practitioner who guards five and elaborates freely on the sixth has not understood the instruction",
             "Because the mind cannot be guarded",
             "Because the Vinaya requires six"],
         "correct": 1,
         "expl": "The list runs through all six."},
        {"q": "What do the four rejected motives in the eating reflection have in common?",
         "opts": [
             "They all concern the body as display or entertainment &mdash; nothing rejects nourishment or even pleasure as such",
             "They all concern cost",
             "They all concern monastic rules",
             "They all concern taste"],
         "correct": 0,
         "expl": "Not for fun, indulgence, adornment, or decoration."},
        {"q": "What does the guide say is unusually accommodating in the positive formula?",
         "opts": [
             "That fasting is permitted",
             "That <em>a comfortable abiding</em> is named as one of the aims &mdash; this is not an austerity instruction",
             "That any quantity is allowed",
             "That meals may be skipped"],
         "correct": 1,
         "expl": "A person eating to this standard would eat enough, regularly, and without fuss."},
        {"q": "What two details of the wakefulness timetable does the guide say transfer, as against the schedule itself?",
         "opts": [
             "The posture is specified, making lying down a described practice rather than the cessation of practice; and the intention to rise is formed before sleep, not on waking",
             "The number of hours and the direction faced",
             "The time of the last meal and the time of rising",
             "Nothing transfers"],
         "correct": 0,
         "expl": "Roughly four hours of sleep is a monastic regime, and a demanding one."},
        {"q": "What do the three things have in common, according to the guide?",
         "opts": [
             "Each requires a teacher",
             "Each governs a continuous, unavoidable daily process &mdash; perceiving, eating, sleeping &mdash; that a person engages in whether or not they practice",
             "Each takes an hour a day",
             "Each concerns the body only"],
         "correct": 1,
         "expl": "Not additional activities fitted into a life but the activities a life already consists of, done differently."},
    ],
    marginalia=[
        ("Three things", [
            "the sense doors",
            "the meal",
            "the night",
        ]),
        ("The bet", [
            "<span class=\"pali\">apaṇṇaka</span>the throw that cannot lose",
            "&ldquo;laid the groundwork&rdquo;",
            "&mdash; begun, not finished",
        ]),
        ("What is restrained", [
            "not seeing",
            "<span class=\"pali\">nimittaggāhī</span>seizing the feature",
            "&mdash; the elaboration after contact",
        ]),
        ("Cross-references", [
            "AN 1.1&ndash;10 &middot; where sense restraint is aimed",
            "AN 1.11&ndash;20 &middot; covetousness and displeasure",
            "MN 39 &middot; the same three, in the gradual training",
        ]),
    ],
    further=[
        '<a href="%s/an3.16/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../majjhima-nikaya/mn-039.html">MN 39 &middot; The Longer Discourse at '
        "Assapura</a> &mdash; these same three set inside the full gradual training, so their place "
        "in a sequence can be seen.",
        '<a href="an-1.1-10.html">AN 1.1&ndash;10 &middot; What Occupies the Mind</a> &mdash; the '
        "chapter that opens the collection by naming what the sense doors are being guarded against.",
        '<a href="/sutras/mohe-zhiguan/fascicle-004/">Mohe Zhiguan, Fascicle 4</a> &mdash; Zhiyi '
        "arranging the same preliminaries as conditions to be settled before formal practice begins.",
    ],
)


page(
    17, "Attabyābādha", "Hurting Yourself",
    vagga=VAGGA_2,
    meta_title="AN 3.17 — Hurting Yourself | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Attabyābādhasutta — "
        "bad conduct hurts yourself, hurts others, and hurts both, and the three are named "
        "separately. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Two parallel passages on the standard threefold division of action"),
        ("Length", "under a minute to read"),
        ("Northern parallel", "The threefold analysis of harm is standard across the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; four sentences, with one "
                       "distinction worth keeping"),
    ],
    why=(
        "Bad conduct of body, speech, and mind leads to hurting yourself, hurting others, and hurting "
        "both. Three destinations for one cause, and the discourse names them as three rather than "
        "collapsing them into &ldquo;harm.&rdquo; That separation is the whole of what the discourse "
        "adds, and it is enough."),
    guide=[
        ("The teaching in one sentence", [
            "The same bad conduct produces three distinguishable kinds of damage, and the first of "
            "them is to yourself."]),
        ("Why three and not one", [
            "<em>Attabyābādhāya</em>, <em>parabyābādhāya</em>, <em>ubhayabyābādhāya</em>: for the "
            "hurting of self, of another, of both. The Pāli gives three separate compounds where one "
            "would have done.",
            "Read as a list they are not three degrees of the same thing. Some conduct damages the "
            "person doing it and nobody else &mdash; a private resentment, a habit of thought. Some "
            "damages another and leaves the doer apparently untouched. And some does both, which is "
            "the ordinary case and the one people notice.",
            "By naming all three the discourse forecloses two familiar defenses at once. "
            "<em>It only hurts me</em> is answered by the first item being on a list of harms. "
            "<em>It doesn&rsquo;t hurt me</em> is answered by the first item being on the list at "
            "all."]),
        ("Reading it beside AN 3.9", [
            "AN 3.9, eight discourses earlier, said the fool <em>keeps themselves broken and "
            "damaged</em>. This one gives the same claim without the image and adds the other two "
            "terms. The pair is worth reading together: AN 3.9 established that the harm falls on the "
            "doer, and AN 3.17 establishes that it does not fall only there.",
            "The Aṅguttara does this constantly &mdash; states a claim in one discourse with an image "
            "and in another as a bare list &mdash; and the two versions are useful for different "
            "purposes. The image is what a person remembers. The list is what they can check "
            "themselves against."]),
        ("The positive half", [
            "Good conduct of body, speech, and mind does <em>not</em> lead to hurting yourself, "
            "others, or both. Note the form: the positive is stated as a negation. It is not said that "
            "good conduct helps yourself, others, and both &mdash; only that it does not hurt.",
            "That is characteristic and worth noticing rather than reading past. The collection is "
            "quite capable of stating positive benefits when it wants to, and here it does not. What "
            "is being claimed for good conduct is precisely and only that it is not one of the three "
            "kinds of damage. Whether it produces anything further is a different question, answered "
            "elsewhere."]),
    ],
    terms=[
        ("attabyābādha",
         "&ldquo;hurting oneself&rdquo; &mdash; the first of the three, and the one the collection "
         "puts first."),
        ("parabyābādha",
         "&ldquo;hurting another&rdquo; &mdash; the second."),
        ("ubhayabyābādha",
         "&ldquo;hurting both&rdquo; &mdash; the third, and the ordinary case that people notice."),
        ("duccarita / sucarita",
         "&ldquo;bad conduct&rdquo; and &ldquo;good conduct&rdquo; &mdash; by way of body, speech, "
         "and mind, as throughout this chapter."),
        ("byābādha",
         "&ldquo;hurting, affliction&rdquo; &mdash; the same root as <em>sabyābajjha</em>, hurtful, "
         "at AN 3.8."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three things that lead to hurting"),
        ("p", "&sect;1", "an3.17:1.1-1.4"),
        ("h3", "And three that do not"),
        ("p", "&sect;2", "an3.17:2.1-2.4"),
    ],
    quiz=[
        {"q": "What three kinds of hurting does bad conduct lead to?",
         "opts": [
             "Hurting yourself, hurting others, and hurting both",
             "Hurting the body, speech, and mind",
             "Hurting now, later, and always",
             "Hurting monastics, laypeople, and gods"],
         "correct": 0,
         "expl": "Three separate Pāli compounds where one would have done."},
        {"q": "Are the three degrees of the same thing?",
         "opts": [
             "Yes, increasing in severity",
             "No &mdash; some conduct damages the doer and nobody else, some damages another and leaves the doer apparently untouched, and some does both",
             "Yes, decreasing in severity",
             "The discourse does not distinguish them"],
         "correct": 1,
         "expl": "The third is the ordinary case and the one people notice."},
        {"q": "Which two familiar defenses does naming all three foreclose?",
         "opts": [
             "&ldquo;It only hurts me,&rdquo; answered by the first item being on a list of harms; and &ldquo;it doesn&rsquo;t hurt me,&rdquo; answered by the first item being on the list at all",
             "&ldquo;I did not mean it&rdquo; and &ldquo;nobody saw&rdquo;",
             "&ldquo;It was necessary&rdquo; and &ldquo;it was small&rdquo;",
             "Neither; the discourse offers no defense"],
         "correct": 0,
         "expl": "Both are closed by the same item."},
        {"q": "How does this discourse relate to AN 3.9?",
         "opts": [
             "It contradicts it",
             "AN 3.9 established that the harm falls on the doer; this one establishes that it does not fall only there",
             "It repeats it exactly",
             "They concern different subjects"],
         "correct": 1,
         "expl": "The same claim, once with an image and once as a bare list."},
        {"q": "What does the guide say the two versions are useful for?",
         "opts": [
             "The image is what a person remembers; the list is what they can check themselves against",
             "The image is for monastics and the list for laypeople",
             "Only the image is useful",
             "Only the list is useful"],
         "correct": 0,
         "expl": "The Aṅguttara does this constantly."},
        {"q": "How is the positive half stated?",
         "opts": [
             "As a benefit &mdash; good conduct helps yourself, others, and both",
             "As a negation &mdash; good conduct does <em>not</em> lead to hurting yourself, others, or both",
             "As a training instruction",
             "As a rebirth destination"],
         "correct": 1,
         "expl": "Characteristic, and worth noticing rather than reading past."},
        {"q": "What does the guide say is being claimed for good conduct here?",
         "opts": [
             "That it produces happiness",
             "Precisely and only that it is not one of the three kinds of damage &mdash; whether it produces anything further is a different question, answered elsewhere",
             "That it guarantees a good rebirth",
             "That it ends the defilements"],
         "correct": 1,
         "expl": "The collection is quite capable of stating positive benefits when it wants to, and here it does not."},
        {"q": "What is the root of <em>byābādha</em> shared with?",
         "opts": [
             "<em>Sabyābajjha</em>, hurtful, at AN 3.8",
             "<em>Sāvajja</em>, blameworthy",
             "<em>Akusala</em>, unskillful",
             "<em>Bhaya</em>, danger"],
         "correct": 0,
         "expl": "Which is why AN 3.8 and AN 3.17 read as a pair."},
        {"q": "Which of the three does the collection put first?",
         "opts": [
             "Hurting others",
             "Hurting both",
             "Hurting oneself",
             "The order varies"],
         "correct": 2,
         "expl": "Consistent with AN 3.9, where the internal consequence is also stated first."},
        {"q": "How long is this discourse?",
         "opts": ["Four sentences", "Two pages", "Ten paragraphs", "A single word"],
         "correct": 0,
         "expl": "With one distinction worth keeping."},
    ],
    marginalia=[
        ("Three harms", [
            "<span class=\"pali\">atta-</span>yourself",
            "<span class=\"pali\">para-</span>another",
            "<span class=\"pali\">ubhaya-</span>both",
        ]),
        ("Two defenses closed", [
            "&ldquo;it only hurts me&rdquo;",
            "&ldquo;it doesn&rsquo;t hurt me&rdquo;",
            "&mdash; by the same item",
        ]),
        ("The positive half", [
            "not: good conduct helps",
            "but: it does not hurt",
        ]),
        ("Cross-references", [
            "AN 3.9 &middot; the same claim, with an image",
            "AN 3.8 &middot; the same root",
            "AN 3.18 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.17/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.9.html">AN 3.9 &middot; Broken</a> &mdash; the same claim about self-harm given '
        "as an image rather than as a list.",
        '<a href="an-3.18.html">AN 3.18 &middot; The Realm of the Gods</a> &mdash; next in this '
        "series.",
    ],
)


page(
    18, "Devaloka", "The Realm of the Gods",
    vagga=VAGGA_2,
    meta_title="AN 3.18 — The Realm of the Gods | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Devalokasutta — the "
        "Buddha asks whether his monastics would be disgusted to be told they practice for "
        "rebirth in heaven, and builds an argument out of their answer. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", "The Buddha and the assembled mendicants, who answer him"),
        ("Form", "A hypothetical question put to the assembly, their answer, and an argument built "
                 "from it"),
        ("Length", "~1 minute to read"),
        ("Northern parallel", "Comparable material distinguishing the goal from heavenly rebirth "
                              "appears in the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short, and its argument is a "
                       "genuine piece of reasoning rather than an assertion"),
    ],
    why=(
        "The Buddha asks his monastics a hypothetical: if wanderers of another religion asked whether "
        "you practice with me in order to be reborn among the gods, wouldn&rsquo;t you be horrified, "
        "repelled, and disgusted? They say yes. And then he uses their answer as a premise: so you are "
        "disgusted by heavenly lifespan, beauty, happiness, glory, and sovereignty &mdash; how much "
        "more should you be disgusted by bad conduct of body, speech, and mind. It is a short discourse "
        "that argues rather than asserts, and its premise is supplied by the audience."),
    guide=[
        ("The teaching in one sentence", [
            "If the best thing the world can offer already disgusts you, the worst thing should "
            "disgust you more."]),
        ("The shape of the argument", [
            "The reasoning is an <em>a fortiori</em> &mdash; an argument from the stronger case. If X "
            "disgusts you, and Y is worse than X in the relevant respect, then Y should disgust you "
            "more. The Buddha supplies X (heavenly rebirth), the monastics supply the fact that it "
            "disgusts them, and he supplies Y (bad conduct).",
            "What makes it work is that X is not a bad thing. Heavenly lifespan, beauty, happiness, "
            "glory, and sovereignty are named without irony and the canon treats them as genuinely "
            "desirable &mdash; a heavenly rebirth is what the collection repeatedly says good conduct "
            "leads to. The argument runs from the best available outcome, not from a straw man.",
            "That is what gives the conclusion its force. If the summit of what can be attained by "
            "ordinary merit is already beneath contempt for someone practicing for the end of "
            "suffering, then conduct that leads in the opposite direction is not merely inadvisable."]),
        ("Why they would be horrified", [
            "The reaction is stronger than disagreement: <em>aṭṭiyeyyātha harāyeyyātha jiguccheyyātha</em> "
            "&mdash; horrified, repelled, disgusted. The same triad is used elsewhere of the reaction "
            "to a corpse.",
            "The reason is not that heaven is bad but that being thought to want it would misdescribe "
            "the enterprise entirely. A person practicing for a better rebirth is doing something the "
            "canon recognizes and does not condemn &mdash; the discourses to laypeople recommend "
            "exactly this. But it is a different project, and to have it attributed to you by an "
            "outsider is to have your whole undertaking misidentified.",
            "There is a small piece of social observation embedded here too. The question comes from "
            "<em>wanderers who follow another religion</em>, and the discourse assumes such "
            "encounters happen and that one has to be able to answer. The Aṅguttara is full of these "
            "conversations; this one is about how it would feel to be asked the wrong question."]),
        ("The awkward part, stated plainly", [
            "It should be said that this discourse sits uneasily beside a great deal of the "
            "collection, and the tension is worth naming rather than resolving. The Aṅguttara "
            "repeatedly commends conduct that leads to a heavenly rebirth, promises it to the "
            "generous and the ethical, and uses <em>placed in heaven as if delivered there</em> as a "
            "standard formula of praise. AN 3.10, eight discourses earlier, ends on exactly that.",
            "So the collection recommends to some listeners what it expects other listeners to find "
            "disgusting. That is not a contradiction if one notices who is being addressed: this "
            "discourse is spoken to full-time practitioners about their own aim, and the "
            "heavenly-rebirth material is largely addressed to householders about theirs. But the two "
            "are in one book, and a reader who moves between them without noticing the shift will "
            "find the collection incoherent.",
            "The honest formulation is that the canon holds two things at once: that a good rebirth is "
            "a real and worthy outcome of good conduct, and that it is not what the path is for. "
            "AN 3.12 made the same point structurally, with a king&rsquo;s three places and a "
            "mendicant&rsquo;s."]),
    ],
    terms=[
        ("devaloka",
         "&ldquo;the realm of the gods&rdquo; &mdash; a heavenly rebirth, which the canon treats as "
         "genuinely desirable and as the standard result of good conduct."),
        ("aṭṭiyati, harāyati, jigucchati",
         "&ldquo;horrified, repelled, disgusted&rdquo; &mdash; a fixed triad used elsewhere of the "
         "reaction to a corpse."),
        ("aññatitthiyā paribbājakā",
         "&ldquo;wanderers who follow another religion&rdquo; &mdash; the hypothetical questioners, "
         "and a standing feature of the Aṅguttara&rsquo;s social world."),
        ("dibbaṁ āyu, vaṇṇa, sukha, yasa, ādhipateyya",
         "heavenly lifespan, beauty, happiness, glory, and sovereignty &mdash; the five goods named "
         "without irony, which is what gives the argument its force."),
        ("pageva",
         "&ldquo;how much more&rdquo; &mdash; the particle that carries the argument from the "
         "stronger case."),
    ],
    text_intro=(
        "The discourse in full, including the mendicants&rsquo; answer. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "A question, and what follows from the answer"),
        ("p", "&sect;1", "an3.18:1.1-1.6"),
    ],
    quiz=[
        {"q": "What hypothetical does the Buddha put to the mendicants?",
         "opts": [
             "Whether they would leave if he died",
             "Whether they would be horrified, repelled, and disgusted to be asked by wanderers of another religion if they practice in order to be reborn among the gods",
             "Whether they can name the four truths",
             "Whether they would accept a donation"],
         "correct": 1,
         "expl": "And they say yes, which becomes the premise of the argument."},
        {"q": "What kind of argument is it?",
         "opts": [
             "An argument from authority",
             "An <em>a fortiori</em> &mdash; from the stronger case: if X disgusts you and Y is worse in the relevant respect, Y should disgust you more",
             "An argument from consequences",
             "A simile"],
         "correct": 1,
         "expl": "The premise is supplied by the audience."},
        {"q": "What makes the argument work?",
         "opts": [
             "That heavenly rebirth is a bad thing",
             "That X is <em>not</em> a bad thing &mdash; heavenly lifespan, beauty, happiness, glory, and sovereignty are named without irony and the canon treats them as genuinely desirable",
             "That the wanderers are hostile",
             "That the monastics are senior"],
         "correct": 1,
         "expl": "The argument runs from the best available outcome, not from a straw man."},
        {"q": "Why would being asked the question be horrifying?",
         "opts": [
             "Because heaven is bad",
             "Because being thought to want it would misdescribe the enterprise entirely &mdash; a different project attributed to you by an outsider",
             "Because the wanderers are enemies",
             "Because the answer is unknown"],
         "correct": 1,
         "expl": "The canon recognizes and does not condemn practicing for a better rebirth; it is simply a different undertaking."},
        {"q": "Where else is the triad &ldquo;horrified, repelled, disgusted&rdquo; used?",
         "opts": [
             "Of the reaction to a corpse",
             "Of the reaction to a teaching",
             "Of the reaction to poverty",
             "Nowhere else"],
         "correct": 0,
         "expl": "The reaction is stronger than disagreement."},
        {"q": "What tension does the guide name?",
         "opts": [
             "That the discourse contradicts the Vinaya",
             "That the Aṅguttara repeatedly commends conduct leading to a heavenly rebirth and uses &ldquo;placed in heaven as if delivered there&rdquo; as praise &mdash; AN 3.10, eight discourses earlier, ends on exactly that",
             "That the mendicants disagree with the Buddha",
             "That the wanderers are never identified"],
         "correct": 1,
         "expl": "The collection recommends to some listeners what it expects others to find disgusting."},
        {"q": "How does the guide resolve it?",
         "opts": [
             "By declaring one passage inauthentic",
             "By noticing who is addressed &mdash; this discourse speaks to full-time practitioners about their aim, and the heavenly-rebirth material largely to householders about theirs",
             "By ignoring the heavenly-rebirth material",
             "It is not resolved at all"],
         "correct": 1,
         "expl": "But a reader who moves between them without noticing the shift will find the collection incoherent."},
        {"q": "What is the honest formulation the guide offers?",
         "opts": [
             "That heaven does not exist",
             "That the canon holds two things at once: a good rebirth is a real and worthy outcome of good conduct, and it is not what the path is for",
             "That only monastics may aim higher",
             "That the question is undecidable"],
         "correct": 1,
         "expl": "AN 3.12 made the same point structurally, with a king's three places and a mendicant's."},
        {"q": "Who are the hypothetical questioners?",
         "opts": [
             "Wanderers who follow another religion &mdash; a standing feature of the Aṅguttara&rsquo;s social world",
             "Kings",
             "Householders",
             "Other Buddhist monastics"],
         "correct": 0,
         "expl": "The discourse assumes such encounters happen and that one has to be able to answer."},
        {"q": "What carries the argument from the stronger case?",
         "opts": [
             "The particle <em>pageva</em> &mdash; &ldquo;how much more&rdquo;",
             "A simile",
             "A training instruction",
             "A list of three"],
         "correct": 0,
         "expl": "The hinge of the whole discourse."},
    ],
    marginalia=[
        ("The argument", [
            "if heaven disgusts you",
            "&mdash; lifespan, beauty, happiness,",
            "glory, sovereignty &mdash;",
            "<span class=\"pali\">pageva</span>how much more, bad conduct",
        ]),
        ("The reaction", [
            "horrified, repelled, disgusted",
            "&mdash; the triad used of a corpse",
        ]),
        ("The tension", [
            "AN 3.10 &middot; placed in heaven, as praise",
            "AN 3.18 &middot; heaven, as disgusting",
            "&mdash; different listeners, one book",
        ]),
        ("Cross-references", [
            "AN 3.10 &middot; eight discourses earlier",
            "AN 3.12 &middot; two lists of three places",
            "AN 4.62 &middot; a householder&rsquo;s aim",
        ]),
    ],
    further=[
        '<a href="%s/an3.18/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.10.html">AN 3.10 &middot; Stains</a> &mdash; eight discourses earlier, ending '
        "on the heavenly destination this one treats as beneath the listener&rsquo;s aim.",
        '<a href="an-4.62.html">AN 4.62 &middot; Debtlessness</a> &mdash; the householder&rsquo;s side '
        "of the same distinction, where worldly goods are named and ranked without apology.",
        '<a href="an-3.12.html">AN 3.12 &middot; Commemoration</a> &mdash; the same point made '
        "structurally, with a king&rsquo;s three places against a mendicant&rsquo;s.",
    ],
)


page(
    19, "Paṭhamapāpaṇika", "A Shopkeeper (1st)",
    vagga=VAGGA_2,
    meta_title="AN 3.19 — A Shopkeeper (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the first "
        "Pāpaṇikasutta — a shopkeeper who does not attend to the shop morning, midday, and "
        "afternoon cannot grow the business, and neither can a mendicant. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "A simile from trade in two directions, each applied to a mendicant"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Similes drawn from trade are common in the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a single clear simile, with one "
                       "detail that changes how it reads"),
    ],
    why=(
        "A shopkeeper who does not attend carefully to the business in the morning, at midday, and in "
        "the afternoon cannot acquire wealth or grow what they have. So too a mendicant who does not "
        "attend carefully to a meditation subject at those three times. It is the plainest of the "
        "chapter&rsquo;s similes and its interest is entirely in the schedule: not more effort, not "
        "better effort &mdash; three times a day."),
    guide=[
        ("The teaching in one sentence", [
            "A practice grows the way a business does: by being attended to three times a day."]),
        ("The simile is about frequency, not intensity", [
            "Nothing in the discourse says the shopkeeper is lazy, unskilled, or badly capitalized. "
            "The failure named is entirely one of scheduling: they do not carefully focus on the work "
            "<em>in the morning, at midday, and in the afternoon</em>. That is all.",
            "The parallel is exact. The mendicant who fails does not lack diligence in general; they "
            "do not carefully focus on <em>a meditation subject as a basis of immersion</em> at those "
            "three times. And the consequence is stated in the same commercial terms: unable to "
            "acquire more skillful qualities or to increase those already acquired.",
            "That commercial framing is worth sitting with rather than apologizing for. Skillful "
            "qualities are treated here as a stock that can be built up and can fail to grow, and "
            "attention to them is treated as minding a shop. The canon is entirely comfortable with "
            "this register &mdash; AN 7.6 lists seven treasures, AN 2.145 speaks of riches in the "
            "teaching &mdash; and it produces a more workmanlike picture of practice than most modern "
            "presentations offer."]),
        ("Three times, and what they are not", [
            "Morning, midday, afternoon. Notice that the night is absent: this discourse does not "
            "reach for the three watches that AN 3.16 used for wakefulness. These are the three "
            "divisions of a working day, which is what makes the shopkeeper the right figure for it.",
            "Notice also what the instruction is not. It is not to meditate all day, and it is not to "
            "meditate for a long time. It is to attend carefully, three times, to a specific object "
            "&mdash; a meditation subject taken as a basis of immersion. A shopkeeper who checks the "
            "shop three times has not spent the day in it either.",
            "For anyone building a practice around a working life, this is the most directly usable "
            "discourse in the chapter, and its usability comes from being unambitious. The failing it "
            "diagnoses is not doing too little at a sitting; it is going a whole day without turning "
            "toward the object at all."]),
        ("The pair of shopkeeper discourses", [
            "AN 3.19 and AN 3.20 both use a shopkeeper and they do different jobs. This one is about "
            "regularity; the next is about three capacities &mdash; seeing clearly, being "
            "indefatigable, and having supporters. Read together they say that a practice needs both "
            "a schedule and a set of competences, and that neither substitutes for the other.",
            "The Aṅguttara often runs a figure twice like this, with the number staying at three and "
            "the content changing entirely. It is worth reading the pair in one sitting for that "
            "reason: the second discourse is not an expansion of the first but a different question "
            "asked of the same shop."]),
    ],
    terms=[
        ("pāpaṇika",
         "&ldquo;shopkeeper, trader&rdquo; &mdash; the figure of both this discourse and the next."),
        ("sakkaccaṁ",
         "&ldquo;carefully, attentively&rdquo; &mdash; the manner of the attending, and the word the "
         "whole discourse turns on."),
        ("samādhinimitta",
         "&ldquo;a meditation subject as a basis of immersion&rdquo; &mdash; literally the sign or "
         "feature of immersion; the specific object the mendicant is to attend to."),
        ("kusalā dhammā",
         "&ldquo;skillful qualities&rdquo; &mdash; treated here as a stock that can be acquired and "
         "increased, in the same terms as a shopkeeper&rsquo;s wealth."),
        ("pubbaṇhasamayaṁ, majjhanhikasamayaṁ, sāyanhasamayaṁ",
         "morning, midday, and afternoon &mdash; the three divisions of a working day, as against the "
         "three watches of the night used at AN 3.16."),
    ],
    text_intro=(
        "The discourse in full, in two directions. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The shopkeeper who cannot grow the business"),
        ("p", "&sect;1", "an3.19:1.1-1.4"),
        ("p", "&sect;2", "an3.19:2.1-2.4"),
        ("h3", "And the one who can"),
        ("p", "&sect;3", "an3.19:3.1-3.4"),
        ("p", "&sect;4", "an3.19:4.1-4.4"),
    ],
    quiz=[
        {"q": "What is the shopkeeper&rsquo;s failing?",
         "opts": [
             "Laziness",
             "Lack of capital",
             "Not carefully focusing on the work in the morning, at midday, and in the afternoon &mdash; a failure of scheduling",
             "Poor judgment of prices"],
         "correct": 2,
         "expl": "Nothing in the discourse says the shopkeeper is lazy, unskilled, or badly capitalized."},
        {"q": "What is the mendicant&rsquo;s corresponding failing?",
         "opts": [
             "Not carefully focusing on a meditation subject as a basis of immersion at those three times",
             "Not keeping the precepts",
             "Not studying the discourses",
             "Not having good friends"],
         "correct": 0,
         "expl": "The parallel is exact, including the consequence stated in commercial terms."},
        {"q": "How does the discourse describe the consequence?",
         "opts": [
             "As rebirth in a bad destination",
             "As being unable to acquire more skillful qualities or increase those already acquired &mdash; the same terms as a shopkeeper&rsquo;s wealth",
             "As criticism from the wise",
             "As losing one&rsquo;s teacher"],
         "correct": 1,
         "expl": "Skillful qualities are treated as a stock that can be built up and can fail to grow."},
        {"q": "What does the guide say about that commercial framing?",
         "opts": [
             "That it should be apologized for",
             "That the canon is entirely comfortable with the register &mdash; AN 7.6 lists seven treasures, AN 2.145 speaks of riches in the teaching &mdash; and it produces a more workmanlike picture of practice than most modern presentations",
             "That it is a later addition",
             "That it applies only to laypeople"],
         "correct": 1,
         "expl": "Worth sitting with rather than apologizing for."},
        {"q": "Which three times are named?",
         "opts": [
             "Morning, midday, and afternoon",
             "The three watches of the night",
             "Dawn, dusk, and midnight",
             "Before, during, and after meals"],
         "correct": 0,
         "expl": "The three divisions of a working day, which is what makes the shopkeeper the right figure."},
        {"q": "What is notably absent from those three times?",
         "opts": [
             "The night &mdash; this discourse does not reach for the three watches AN 3.16 used for wakefulness",
             "The morning",
             "Mealtimes",
             "Nothing is absent"],
         "correct": 0,
         "expl": "A working day, not a monastic night."},
        {"q": "What is the instruction <em>not</em>?",
         "opts": [
             "It is not to meditate all day, and not to meditate for a long time &mdash; it is to attend carefully, three times, to a specific object",
             "It is not for monastics",
             "It is not about attention",
             "It is not about frequency"],
         "correct": 0,
         "expl": "A shopkeeper who checks the shop three times has not spent the day in it either."},
        {"q": "What failing does the discourse actually diagnose?",
         "opts": [
             "Doing too little at a sitting",
             "Going a whole day without turning toward the object at all",
             "Meditating on the wrong object",
             "Meditating in the wrong posture"],
         "correct": 1,
         "expl": "Which is why the guide calls it the most usable discourse in the chapter for a working life."},
        {"q": "How do AN 3.19 and AN 3.20 differ?",
         "opts": [
             "They are identical",
             "This one is about regularity; the next is about three capacities &mdash; seeing clearly, being indefatigable, and having supporters",
             "The second corrects the first",
             "The second concerns laypeople"],
         "correct": 1,
         "expl": "A practice needs both a schedule and a set of competences, and neither substitutes for the other."},
        {"q": "What does the guide say about the Aṅguttara running a figure twice?",
         "opts": [
             "That it indicates a compilation error",
             "That the number stays at three and the content changes entirely &mdash; the second discourse is not an expansion of the first but a different question asked of the same shop",
             "That the second is always longer",
             "That only the first is authentic"],
         "correct": 1,
         "expl": "Worth reading the pair in one sitting for that reason."},
    ],
    marginalia=[
        ("Three times", [
            "morning",
            "midday",
            "afternoon",
            "&mdash; a working day, not a night",
        ]),
        ("The failing", [
            "not: too little at a sitting",
            "but: a whole day without turning",
        ]),
        ("The register", [
            "<span class=\"pali\">kusalā dhammā</span>a stock",
            "acquired &middot; increased",
            "&mdash; the canon is at ease with this",
        ]),
        ("Cross-references", [
            "AN 3.20 &middot; the same shop, another question",
            "AN 7.6 &middot; seven treasures",
            "AN 3.16 &middot; the three watches instead",
        ]),
    ],
    further=[
        '<a href="%s/an3.19/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.20.html">AN 3.20 &middot; A Shopkeeper (2nd)</a> &mdash; next in this series, '
        "and the other question asked of the same shop.",
        '<a href="an-7.6.html">AN 7.6 &middot; Wealth in Detail</a> &mdash; the seven treasures, '
        "and the clearest case of the canon using a commercial vocabulary without embarrassment.",
    ],
)


page(
    20, "Dutiyapāpaṇika", "A Shopkeeper (2nd)",
    vagga=VAGGA_2,
    meta_title="AN 3.20 — A Shopkeeper (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second "
        "Pāpaṇikasutta, which closes the Rathakāravagga — seeing clearly, being "
        "indefatigable, and having supporters, with the third defined as asking senior "
        "monastics what a passage means. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three qualities defined for a shopkeeper, then the same three for a mendicant"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Similes drawn from trade are common in the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; clear throughout, and the third "
                       "quality is the reason to read it"),
    ],
    why=(
        "Three qualities let a shopkeeper acquire great wealth quickly: seeing clearly, being "
        "indefatigable, and having supporters. The same three, redefined, do the same for a mendicant. "
        "The third is the one worth the page. A mendicant &ldquo;has supporters&rdquo; when they go "
        "from time to time to the very learned and ask them <em>why does it say this? what does that "
        "mean?</em> &mdash; the same two questions AN 2.47 made the mark of a good assembly. Support, "
        "for a practitioner, turns out to mean people you can ask."),
    guide=[
        ("The teaching in one sentence", [
            "A practice grows fast when a person sees the situation clearly, keeps working, and has "
            "somebody to ask."]),
        ("The shopkeeper&rsquo;s three", [
            "Seeing clearly is knowing the numbers: this product is bought at this price and sells at "
            "this; with this much investment it will bring this much profit. Being indefatigable is "
            "skill in buying and selling. Having supporters is credit &mdash; wealthy householders who "
            "know the shopkeeper is capable and deposit money with him to trade on.",
            "The third is the most concrete and the most social. The reason given for the deposit is "
            "specific: <em>they are capable of providing for their wives and children, and paying us "
            "back from time to time</em>. Support is extended on the basis of demonstrated competence "
            "and demonstrated reliability, not goodwill. That detail matters when the simile turns."]),
        ("The mendicant&rsquo;s three", [
            "Seeing clearly is understanding the four truths. Being indefatigable is living with "
            "energy roused for giving up the unskillful and embracing the skillful &mdash; strong, "
            "staunchly vigorous, not slacking off.",
            "And having supporters is this: from time to time going up to those mendicants who are "
            "very learned &mdash; <em>inheritors of the heritage, who have memorized the teachings, "
            "the monastic law, and the outlines</em> &mdash; and asking them questions. <em>Why, sir, "
            "does it say this? What does that mean?</em> And those venerables reveal what is hidden, "
            "clarify what is unclear, and dispel doubt regarding the many doubtful matters."]),
        ("The two questions again", [
            "Those are the same two questions, in the same words, that AN 2.47 in the Twos made the "
            "mark of an assembly educated in questioning rather than in fancy talk. There the test was "
            "whether the members of a community interrogate each other after hearing a teaching. Here "
            "it is an individual competence, and it is named as one of three things that make a "
            "practice grow quickly.",
            "The correspondence is exact enough to be worth teaching as a pair. A community that asks "
            "is AN 2.47; a person who asks is AN 3.20; and the questions are the same two. For a "
            "teacher, that is a usable standard on both scales, and it has the advantage of being "
            "observable &mdash; you can hear whether anyone in a room is asking what a passage means.",
            "It is also worth noticing what the definition rules out. Having supporters is not "
            "described as being encouraged, funded, admired, or looked after. It is described as "
            "having access to people who know more and going to them with a specific kind of "
            "question. That is a narrow and rather demanding account of what support consists of."]),
        ("Who the supporters are", [
            "The description of the senior monastics is worth reading closely: very learned, "
            "<em>inheritors of the heritage</em>, who have memorized the teachings, the monastic law, "
            "and the outlines. Three bodies of material &mdash; discourse, discipline, and summaries "
            "&mdash; and the emphasis is on retention rather than on attainment.",
            "That is characteristic of an oral tradition and it names a specific role: the person "
            "worth asking is the one who has the material. Nothing here says they must be awakened, "
            "senior in years, or personally impressive. What they have is what has been handed down, "
            "and what they do with it is <em>reveal what is hidden, clarify what is unclear, and "
            "dispel doubt</em> &mdash; three verbs, and none of them is <em>teach</em>.",
            "The whole exchange, on both sides, is transactional in the way the shopkeeper simile "
            "prepared for. The learner brings a question; the learned bring the material; the doubt is "
            "dispelled. Nobody is being inspired."]),
        ("Closing the chapter", [
            "AN 3.20 ends the Rathakāravagga, and the chapter it closes is unusually varied: a "
            "well-known monastic&rsquo;s influence, three places to commemorate, three kinds of hope, "
            "the king who has a king, a chariot-maker&rsquo;s two wheels, three preliminaries, three "
            "kinds of harm, a question about heaven, and two shopkeepers.",
            "What holds it together, if anything does, is that almost every discourse in it is about "
            "how something is <em>built</em> &mdash; a reputation, a life measured in three places, a "
            "wheel, a body of skillful qualities, a business. The first chapter of the Threes was "
            "about recognizing what a person is. The second is about what a person accumulates, and "
            "how fast, and whether it will stand when the initial push runs out."]),
    ],
    terms=[
        ("cakkhumā",
         "&ldquo;seeing clearly&rdquo; &mdash; literally possessed of eyes. For a shopkeeper, knowing "
         "the numbers; for a mendicant, understanding the four truths."),
        ("vidhuro",
         "&ldquo;indefatigable, capable&rdquo; &mdash; skill in buying and selling for one, roused "
         "energy for the other."),
        ("nissayasampanno",
         "&ldquo;having supporters&rdquo; &mdash; literally furnished with a support or basis. Defined "
         "for a mendicant as having people to ask."),
        ("bahussutā āgatāgamā",
         "&ldquo;very learned, inheritors of the heritage&rdquo; &mdash; those who have memorized the "
         "teachings, the monastic law, and the outlines. The emphasis is on retention, not attainment."),
        ("kathaṁ imassa bhāsitassa attho",
         "&ldquo;what does that mean?&rdquo; &mdash; with &ldquo;why does it say this?&rdquo;, the two "
         "questions AN 2.47 makes the mark of a good assembly and this discourse makes an individual "
         "competence."),
    ],
    text_intro=(
        "The discourse in full: three qualities for a shopkeeper, then the same three for a mendicant. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A shopkeeper who acquires great wealth"),
        ("p", "&sect;1", "an3.20:1.1-1.7"),
        ("p", "&sect;2", "an3.20:2.1-2.3"),
        ("p", "&sect;3", "an3.20:3.1-3.7"),
        ("h3", "And a mendicant"),
        ("p", "&sect;4", "an3.20:4.1-4.6"),
        ("p", "&sect;5", "an3.20:5.1-5.3"),
        ("p", "&sect;6", "an3.20:6.1-6.6"),
    ],
    quiz=[
        {"q": "What three qualities let a shopkeeper acquire great wealth quickly?",
         "opts": [
             "Seeing clearly, being indefatigable, and having supporters",
             "Capital, location, and luck",
             "Honesty, thrift, and industry",
             "Buying low, selling high, and saving"],
         "correct": 0,
         "expl": "The same three, redefined, do the same for a mendicant."},
        {"q": "What does &ldquo;having supporters&rdquo; mean for the shopkeeper?",
         "opts": [
             "Loyal customers",
             "Credit &mdash; wealthy householders who know he is capable and deposit money with him to trade on",
             "A large family",
             "Political protection"],
         "correct": 1,
         "expl": "Extended on the basis of demonstrated competence and reliability, not goodwill."},
        {"q": "What does &ldquo;having supporters&rdquo; mean for the mendicant?",
         "opts": [
             "Lay donors who provide requisites",
             "Going from time to time to the very learned and asking them questions",
             "A large following",
             "A monastery to live in"],
         "correct": 1,
         "expl": "Support turns out to mean people you can ask."},
        {"q": "Which two questions does the mendicant ask?",
         "opts": [
             "&ldquo;Why, sir, does it say this? What does that mean?&rdquo;",
             "&ldquo;Is this permitted? Is this forbidden?&rdquo;",
             "&ldquo;Who said this? When?&rdquo;",
             "&ldquo;What should I do? When should I do it?&rdquo;"],
         "correct": 0,
         "expl": "The same two words for word as AN 2.47 in the Twos."},
        {"q": "How does AN 2.47 use those same questions?",
         "opts": [
             "As a mark of an assembly educated in questioning rather than in fancy talk &mdash; whether members interrogate each other after hearing a teaching",
             "As a monastic offense",
             "As a form of doubt",
             "It does not use them"],
         "correct": 0,
         "expl": "A community that asks is AN 2.47; a person who asks is AN 3.20."},
        {"q": "What does the definition of having supporters rule out?",
         "opts": [
             "Being encouraged, funded, admired, or looked after &mdash; it is access to people who know more, and going to them with a specific kind of question",
             "Having any support at all",
             "Asking questions",
             "Living in community"],
         "correct": 0,
         "expl": "A narrow and rather demanding account of what support consists of."},
        {"q": "How are the senior monastics described?",
         "opts": [
             "As awakened and senior in years",
             "As very learned, inheritors of the heritage, who have memorized the teachings, the monastic law, and the outlines &mdash; the emphasis on retention rather than attainment",
             "As personally impressive",
             "As appointed by the Saṅgha"],
         "correct": 1,
         "expl": "The person worth asking is the one who has the material."},
        {"q": "What three things do those venerables do?",
         "opts": [
             "Reveal what is hidden, clarify what is unclear, and dispel doubt &mdash; and none of the three verbs is <em>teach</em>",
             "Preach, exhort, and inspire",
             "Ordain, admonish, and expel",
             "Recite, memorize, and transmit"],
         "correct": 0,
         "expl": "The whole exchange is transactional in the way the shopkeeper simile prepared for."},
        {"q": "What holds the Rathakāravagga together, according to the guide?",
         "opts": [
             "Nothing; it is a random assortment",
             "Almost every discourse in it is about how something is <em>built</em> &mdash; a reputation, a life, a wheel, a body of skillful qualities, a business",
             "All its discourses concern kings",
             "All its discourses use similes"],
         "correct": 1,
         "expl": "The first chapter was about recognizing what a person is; the second about what a person accumulates."},
        {"q": "What question does the chapter&rsquo;s central story leave hanging over it?",
         "opts": [
             "Whether the shopkeeper is honest",
             "Whether what is built will stand when the initial push runs out &mdash; the chariot-maker&rsquo;s two wheels",
             "Whether kings can be trusted",
             "Whether heaven exists"],
         "correct": 1,
         "expl": "Which is why AN 3.15 gives the chapter its name."},
    ],
    marginalia=[
        ("Three qualities", [
            "<span class=\"pali\">cakkhumā</span>sees clearly",
            "<span class=\"pali\">vidhuro</span>indefatigable",
            "<span class=\"pali\">nissayasampanno</span>has supporters",
        ]),
        ("What support means", [
            "not funding",
            "not encouragement",
            "&mdash; people you can ask",
        ]),
        ("The two questions", [
            "&ldquo;Why does it say this?&rdquo;",
            "&ldquo;What does that mean?&rdquo;",
            "&mdash; AN 2.47, for a room",
        ]),
        ("The chapter", [
            "a reputation &middot; a life",
            "a wheel &middot; a business",
            "&mdash; all of them, built",
        ]),
    ],
    further=[
        '<a href="%s/an3.20/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.42-51.html">AN 2.42&ndash;51 &middot; Assemblies</a> &mdash; AN 2.47, where the '
        "same two questions are the mark of a whole community rather than of one practitioner.",
        '<a href="an-3.19.html">AN 3.19 &middot; A Shopkeeper (1st)</a> &mdash; the other question '
        "asked of the same shop: not what capacities a practice needs, but how often it is attended to.",
        '<a href="an-3.15.html">AN 3.15 &middot; About Pacetana</a> &mdash; the chariot-maker '
        "whose two wheels give this chapter its name and its standing question.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.21–30 — Puggalavagga
# --------------------------------------------------------------------------- #
VAGGA_3 = "<em>Puggalavagga</em> &mdash; the third chapter of the Threes"

page(
    21, "Samiddha", "With Saviṭṭha",
    vagga=VAGGA_3,
    meta_title="AN 3.21 — With Saviṭṭha | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Samiddhasutta — "
        "three senior monks each name a different kind of person as the finest, take the "
        "question to the Buddha, and are told it cannot be settled. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Sāvatthī, in Jeta&rsquo;s Grove; a conversation among three senior monks, then "
                    "taken to the Buddha"),
        ("Speakers", "Venerable Sāriputta, Venerable Saviṭṭha, Venerable Mahākoṭṭhita, and the "
                     "Buddha"),
        ("Form", "A question asked three times with three different answers, then referred upward "
                 "and declined"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "Comparable material on the three kinds of noble person appears in the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the three technical terms need "
                       "holding, and the ending is the point"),
    ],
    why=(
        "Three senior monks are asked which of three kinds of accomplished person is finest. Each "
        "gives a different answer, and each gives a good reason for it. They agree that they have "
        "each spoken from the heart, take the question to the Buddha, and he declines to settle it "
        "&mdash; four times over, in nearly identical words. It is one of the few places in the canon "
        "where a question is put to the highest available authority and comes back unresolved, and "
        "the reason he gives is worth more than an answer would have been."),
    guide=[
        ("The teaching in one sentence", [
            "Three kinds of accomplished person cannot be ranked against each other, because the "
            "ranking depends on where each of them has actually got to."]),
        ("The three individuals", [
            "<em>Kāyasakkhī</em>, the direct witness &mdash; one whose realization has come through "
            "the meditative attainments, experienced with the body. <em>Diṭṭhippatta</em>, the one "
            "attained to view &mdash; one who has arrived by seeing, through understanding. "
            "<em>Saddhāvimutta</em>, the one freed by faith &mdash; one whose confidence carried "
            "them.",
            "These are technical categories in the canon&rsquo;s typology of noble persons, and all "
            "three are genuinely accomplished; nobody in this discourse is discussing a beginner. "
            "What distinguishes them is which faculty predominated on the way in."]),
        ("Three answers, each defensible", [
            "Saviṭṭha says the one freed by faith is finest, because that person&rsquo;s faculty of "
            "faith is extraordinary. Mahākoṭṭhita says the direct witness, because their faculty of "
            "immersion is extraordinary. Sāriputta says the one attained to view, because their "
            "faculty of wisdom is extraordinary.",
            "Each answer has the same form: the person is finest because the faculty that carried "
            "them is outstanding. So all three are arguing correctly from a shared premise, and "
            "reaching incompatible conclusions. The disagreement is not a failure of reasoning by any "
            "of them.",
            "It is worth noticing who says what. Sāriputta &mdash; named foremost in great wisdom "
            "&mdash; picks the one who came by wisdom. Mahākoṭṭhita, foremost in the analytical "
            "knowledges, picks immersion. The canon does not comment, but each man has answered from "
            "where he stands, and the discourse is quietly aware of it."]),
        ("What Sāriputta does next", [
            "&ldquo;Each of us has spoken from the heart. Come, reverends, let&rsquo;s go to the "
            "Buddha and tell him about this. As he answers, so we&rsquo;ll remember it.&rdquo;",
            "That sentence is a small model of how to handle a disagreement among people who all have "
            "standing. Nobody concedes; nobody is out-argued; the positions are recorded as sincerely "
            "held and the matter is referred. And Sāriputta &mdash; the most senior of the three, and "
            "the one whose answer the tradition would most likely have deferred to &mdash; is the one "
            "who proposes referring it."]),
        ("And what the Buddha does", [
            "He says four times that it is not easy to categorically declare which of the three is "
            "finest, and gives the reason three times over: in some cases the one freed by faith is "
            "practicing for perfection while the other two are once-returners or non-returners &mdash; "
            "and then the same with the direct witness in that position, and then with the one "
            "attained to view.",
            "So the reason is not that the question is improper or that ranking is unspiritual. It is "
            "that the categories cut across the stages. Knowing which faculty carried someone in tells "
            "you nothing about how far they have come, and any of the three types can be found at any "
            "of the levels. Comparing a type against a type is comparing the wrong thing.",
            "That is an unusually precise refusal. The Buddha does not say the monks are wrong to "
            "rank, or that all paths are equal, or that the question does not matter. He says the "
            "question as put cannot be answered because it holds the wrong variable fixed. Anyone who "
            "has watched an argument about which kind of practice is best has watched this discourse."]),
        ("Using it", [
            "For a teacher this is one of the most useful discourses in the Threes, because the "
            "argument it defuses is perennial: whether devotion, concentration, or study is the real "
            "path. All three answers in this discourse are held by named senior disciples, argued "
            "well, and left standing.",
            "The practical form of the Buddha&rsquo;s point is simple enough to hand to a class. Ask "
            "not which kind of practitioner someone is, but how far they have got &mdash; and notice "
            "that the first question is easy to answer about a stranger and the second is not."]),
    ],
    terms=[
        ("kāyasakkhī",
         "&ldquo;direct witness&rdquo; &mdash; one whose realization came through the meditative "
         "attainments, experienced with the body. Mahākoṭṭhita&rsquo;s choice, for the faculty of "
         "immersion."),
        ("diṭṭhippatta",
         "&ldquo;attained to view&rdquo; &mdash; one who arrived by understanding. "
         "Sāriputta&rsquo;s choice, for the faculty of wisdom."),
        ("saddhāvimutta",
         "&ldquo;freed by faith&rdquo; &mdash; one whose confidence carried them. Saviṭṭha&rsquo;s "
         "choice, for the faculty of faith."),
        ("ekaṁsena byākātuṁ",
         "&ldquo;to declare categorically&rdquo; &mdash; what the Buddha says is not easy here. The "
         "canon elsewhere distinguishes questions answerable categorically from those needing "
         "analysis or a counter-question."),
        ("adhimatta",
         "&ldquo;extraordinary, predominant&rdquo; &mdash; said of the faculty in each monk&rsquo;s "
         "answer, and the shared premise from which all three argue correctly to different "
         "conclusions."),
    ],
    text_intro=(
        "The discourse in full, including all three monks&rsquo; answers and the Buddha&rsquo;s "
        "fourfold refusal. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The question, put to Saviṭṭha"),
        ("p", "&sect;1", "an3.21:1.1-1.4"),
        ("p", "&sect;2&ndash;3", "an3.21:2.1-3.7"),
        ("h3", "And to Mahākoṭṭhita, and to Sāriputta"),
        ("p", "&sect;4&ndash;5", "an3.21:4.1-5.7"),
        ("p", "&sect;6&ndash;7", "an3.21:6.1-7.7"),
        ("h3", "Taken to the Buddha"),
        ("p", "&sect;8", "an3.21:8.1-8.7"),
        ("p", "&sect;9&ndash;12", "an3.21:9.1-12.2"),
    ],
    quiz=[
        {"q": "Which three individuals are being compared?",
         "opts": [
             "The direct witness, the one attained to view, and the one freed by faith",
             "The stream-enterer, once-returner, and non-returner",
             "The monk, the nun, and the layperson",
             "The teacher, the student, and the donor"],
         "correct": 0,
         "expl": "All three genuinely accomplished; what distinguishes them is which faculty predominated on the way in."},
        {"q": "What form does each of the three answers take?",
         "opts": [
             "An appeal to seniority",
             "The person is finest because the faculty that carried them &mdash; faith, immersion, or wisdom &mdash; is extraordinary",
             "An appeal to the Buddha&rsquo;s authority",
             "A refusal to answer"],
         "correct": 1,
         "expl": "All three argue correctly from a shared premise to incompatible conclusions."},
        {"q": "What does the guide notice about who picks what?",
         "opts": [
             "Nothing",
             "Sāriputta, foremost in great wisdom, picks the one who came by wisdom; Mahākoṭṭhita, foremost in the analytical knowledges, picks immersion &mdash; each has answered from where he stands",
             "They all pick the same",
             "The choices are randomly assigned"],
         "correct": 1,
         "expl": "The canon does not comment, but the discourse is quietly aware of it."},
        {"q": "What does Sāriputta propose?",
         "opts": [
             "That his answer be accepted, as the most senior",
             "That each has spoken from the heart, and they take the question to the Buddha &mdash; &ldquo;as he answers, so we&rsquo;ll remember it&rdquo;",
             "That they drop the question",
             "That they vote"],
         "correct": 1,
         "expl": "The most senior of the three, and the one whose answer would most likely have been deferred to, is the one who proposes referring it."},
        {"q": "What does the Buddha say?",
         "opts": [
             "That Sāriputta is right",
             "That it is not easy to declare categorically which of the three is finest &mdash; four times over",
             "That the question is improper",
             "That all three are equal"],
         "correct": 1,
         "expl": "One of the few places where a question put to the highest authority comes back unresolved."},
        {"q": "What reason does he give?",
         "opts": [
             "That ranking is unspiritual",
             "That the categories cut across the stages &mdash; any of the three types can be at any level, so in some cases one is practicing for perfection while the others are once-returners or non-returners",
             "That the monks lack the standing to ask",
             "That the answer is secret"],
         "correct": 1,
         "expl": "Knowing which faculty carried someone in tells you nothing about how far they have come."},
        {"q": "How does the guide characterize the refusal?",
         "opts": [
             "As evasive",
             "As unusually precise &mdash; the question as put cannot be answered because it holds the wrong variable fixed",
             "As a concession to all sides",
             "As a rebuke"],
         "correct": 1,
         "expl": "He does not say the monks are wrong to rank, or that all paths are equal, or that the question does not matter."},
        {"q": "Which perennial argument does the guide say this defuses?",
         "opts": [
             "Whether devotion, concentration, or study is the real path",
             "Whether laypeople can awaken",
             "Whether the Vinaya may be amended",
             "Whether rebirth is literal"],
         "correct": 0,
         "expl": "All three answers are held by named senior disciples, argued well, and left standing."},
        {"q": "What practical form does the guide give the Buddha&rsquo;s point?",
         "opts": [
             "Ask not which kind of practitioner someone is, but how far they have got &mdash; and notice that the first question is easy to answer about a stranger and the second is not",
             "Ask which faculty is strongest",
             "Ask the most senior person present",
             "Do not ask at all"],
         "correct": 0,
         "expl": "Simple enough to hand to a class."},
        {"q": "What does <em>ekaṁsena byākātuṁ</em> mean?",
         "opts": [
             "&ldquo;To declare categorically&rdquo; &mdash; and the canon elsewhere distinguishes questions answerable this way from those needing analysis or a counter-question",
             "&ldquo;To refuse to answer&rdquo;",
             "&ldquo;To answer briefly&rdquo;",
             "&ldquo;To answer in verse&rdquo;"],
         "correct": 0,
         "expl": "The kind of answer being declined is specific."},
    ],
    marginalia=[
        ("Three individuals", [
            "<span class=\"pali\">kāyasakkhī</span>direct witness",
            "<span class=\"pali\">diṭṭhippatta</span>attained to view",
            "<span class=\"pali\">saddhāvimutta</span>freed by faith",
        ]),
        ("Three answers", [
            "Saviṭṭha &middot; faith",
            "Mahākoṭṭhita &middot; immersion",
            "Sāriputta &middot; wisdom",
            "&mdash; each from where he stands",
        ]),
        ("The refusal", [
            "not: the question is improper",
            "not: all paths are equal",
            "but: it holds the wrong variable fixed",
        ]),
        ("Cross-references", [
            "AN 1.188&ndash;197 &middot; Sāriputta, Mahākoṭṭhita",
            "AN 3.22 &middot; next: three patients",
            "AN 2.51 &middot; being persuadable",
        ]),
    ],
    further=[
        '<a href="%s/an3.21/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-1.209-218.html">AN 1.209&ndash;218 &middot; Foremost Monks (III)</a> &mdash; '
        "where Mahākoṭṭhita is named foremost in the four analytical knowledges, which is worth "
        "knowing before reading his answer here.",
        '<a href="an-2.42-51.html">AN 2.42&ndash;51 &middot; Assemblies</a> &mdash; AN 2.51, on the '
        "assembly whose members can convince and be convinced, which is what these three monks are "
        "doing.",
        '<a href="an-3.22.html">AN 3.22 &middot; Patients</a> &mdash; next in this series.',
    ],
)


page(
    22, "Gilāna", "Patients",
    vagga=VAGGA_3,
    meta_title="AN 3.22 — Patients | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Gilānasutta — three "
        "kinds of patient, only one of whom treatment decides, and the sentence that keeps "
        "the discourse from being a triage argument. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three patients described, a conclusion drawn, and the same structure applied to "
                 "three kinds of listener"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The medical simile for the reach of teaching appears across the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; clear, and containing one "
                       "sentence that reverses the obvious reading"),
    ],
    why=(
        "Three patients: one who will not recover whatever is done, one who will recover whatever is "
        "done, and one who will recover only if treated. Care is prescribed, the discourse says, for "
        "the sake of the third. Read that far, it is a triage argument, and an uncomfortable one. "
        "Then comes the next sentence: <em>but also, for the sake of this patient, the other patients "
        "should be looked after.</em> Everything the discourse is worth turns on that line."),
    guide=[
        ("The teaching in one sentence", [
            "Treatment is justified by the patient it decides, and therefore everyone is treated."]),
        ("The three patients", [
            "The distinction is by outcome under intervention, not by severity. The first will not "
            "recover regardless of suitable food, medicines, and a capable carer. The second will "
            "recover regardless. The third recovers if treated and does not if not.",
            "Stated coldly, only the third patient&rsquo;s outcome depends on anything anyone does. "
            "The first is beyond help; the second does not need it. This is the logic of triage, and "
            "the discourse states it without flinching: it is for the sake of the third that food, "
            "medicines, and a carer are <em>prescribed</em>.",
            "It is worth being clear that the argument is about justification, not about worth. The "
            "discourse is answering the question <em>why is treatment provided at all?</em>, and the "
            "answer is that there exists a class of case that it decides."]),
        ("The sentence that turns it", [
            "<em>But also, for the sake of this patient, the other patients should be looked after.</em>",
            "That reverses the practical conclusion without touching the logic. Care is justified by "
            "the third patient &mdash; and because care must reach the third patient, it is extended "
            "to all three. The reason is not compassion, or fairness, or the equal worth of the "
            "sick, though the canon says all of those elsewhere. The reason given here is structural: "
            "you cannot reliably identify in advance which patient in front of you is the third one, "
            "so a practice of care that reaches the third must be a practice that treats everybody.",
            "That is a stronger foundation than sentiment, because it does not depend on the carer "
            "feeling anything in particular. A triage argument that concludes in universal care is an "
            "unusual thing to find in any literature."]),
        ("The three listeners", [
            "The parallel is exact. Some people do not step into the sure path with regard to skillful "
            "qualities whether or not they meet a Buddha and hear the teaching. Some do so regardless. "
            "And some do so only if they meet a Buddha and hear the teaching, and not otherwise.",
            "Teaching the Dhamma is prescribed for the sake of the third. And then the same reversal: "
            "<em>but also, for the sake of this individual, the other people should be taught "
            "Dhamma.</em>",
            "For anyone who teaches, that is the discourse&rsquo;s practical payload. It says plainly "
            "that some of your audience will not be reached by anything you do, and that some would "
            "have got there without you, and it does not pretend otherwise. And it concludes that you "
            "teach all of them anyway &mdash; not because the claim about the three types is false, "
            "but because the third type is the reason for the whole enterprise and cannot be picked "
            "out in advance."]),
        ("A note on the first type", [
            "The discourse asserts that some people will not step onto the path whatever happens, and "
            "it is worth not softening that, because it is stated flatly and the canon means it. AN "
            "3.13 said the same thing in the language of hope; AN 1.333&ndash;377 said it in the "
            "language of proportion.",
            "What is worth adding is what the discourse does with the claim, which is nothing. No "
            "advice follows about identifying such people, avoiding them, or spending less effort on "
            "them. The category exists in the analysis and disappears in the instruction. That gap "
            "between what the canon is willing to assert and what it is willing to act on is itself "
            "worth teaching."]),
    ],
    terms=[
        ("gilāna",
         "&ldquo;sick person, patient&rdquo; &mdash; the figure of the simile, and a subject the "
         "canon treats with unusual practical attention elsewhere."),
        ("sappāyāni bhojanāni bhesajjāni",
         "&ldquo;suitable food and medicines&rdquo; &mdash; with a capable carer, the three "
         "components of treatment held constant across all three patients."),
        ("okkamati niyāmaṁ kusalesu dhammesu",
         "&ldquo;steps into the sure path with regard to skillful qualities&rdquo; &mdash; the "
         "outcome that distinguishes the three listeners."),
        ("paññatta",
         "&ldquo;prescribed, laid down&rdquo; &mdash; used of both the treatment and the teaching, "
         "and the word that makes this a discourse about justification."),
        ("upaṭṭhātabbā",
         "&ldquo;should be looked after&rdquo; &mdash; the verb in the sentence that extends care "
         "from the third patient to all three."),
    ],
    text_intro=(
        "The discourse in full: the three patients, then the three listeners. Translation: Bhikkhu "
        "Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three patients"),
        ("p", "&sect;1", "an3.22:1.1-1.3"),
        ("p", "&sect;2", "an3.22:2.1"),
        ("p", "&sect;3", "an3.22:3.1"),
        ("p", "&sect;4", "an3.22:4.1-4.3"),
        ("h3", "Three individuals similar to patients"),
        ("p", "&sect;5", "an3.22:5.1-5.3"),
        ("p", "&sect;6", "an3.22:6.1"),
        ("p", "&sect;7", "an3.22:7.1"),
        ("p", "&sect;8", "an3.22:8.1-8.3"),
    ],
    quiz=[
        {"q": "How are the three patients distinguished?",
         "opts": [
             "By severity of illness",
             "By outcome under intervention &mdash; one will not recover regardless, one will recover regardless, and one recovers only if treated",
             "By wealth",
             "By age"],
         "correct": 1,
         "expl": "Only the third patient's outcome depends on anything anyone does."},
        {"q": "For whose sake is treatment said to be prescribed?",
         "opts": [
             "The first patient&rsquo;s", "The second patient&rsquo;s",
             "The third patient&rsquo;s &mdash; the one who recovers only if treated", "All equally"],
         "correct": 2,
         "expl": "The discourse states the triage logic without flinching."},
        {"q": "What sentence reverses the practical conclusion?",
         "opts": [
             "&ldquo;These are the three kinds of patients found in the world&rdquo;",
             "&ldquo;But also, for the sake of this patient, the other patients should be looked after&rdquo;",
             "&ldquo;Some patients will not recover&rdquo;",
             "&ldquo;A capable carer is needed&rdquo;"],
         "correct": 1,
         "expl": "Everything the discourse is worth turns on that line."},
        {"q": "What reason does the guide give for the reversal?",
         "opts": [
             "Compassion",
             "Fairness",
             "A structural one &mdash; you cannot reliably identify in advance which patient is the third, so a practice of care that reaches them must treat everybody",
             "The equal worth of the sick"],
         "correct": 2,
         "expl": "The canon says the others elsewhere; the reason given here is structural."},
        {"q": "Why does the guide call that a stronger foundation than sentiment?",
         "opts": [
             "Because it is older",
             "Because it does not depend on the carer feeling anything in particular",
             "Because it is easier to teach",
             "Because it excludes the first patient"],
         "correct": 1,
         "expl": "A triage argument that concludes in universal care is an unusual thing to find in any literature."},
        {"q": "What distinguishes the three listeners?",
         "opts": [
             "Whether they step into the sure path with regard to skillful qualities &mdash; regardless of meeting a Buddha, regardless, or only if they do",
             "Their ordination status",
             "Their caste",
             "Their intelligence"],
         "correct": 0,
         "expl": "The parallel with the patients is exact."},
        {"q": "What is the discourse&rsquo;s practical payload for anyone who teaches?",
         "opts": [
             "That teaching is unnecessary",
             "That some of your audience will not be reached by anything you do and some would have got there without you &mdash; and that you teach all of them anyway, because the third type is the reason for the enterprise and cannot be picked out in advance",
             "That only the receptive should be taught",
             "That teaching should be restricted to monastics"],
         "correct": 1,
         "expl": "It does not pretend otherwise about the first two types."},
        {"q": "What does the discourse do with its claim that some people cannot be reached?",
         "opts": [
             "Advises avoiding them",
             "Advises spending less effort on them",
             "Nothing &mdash; the category exists in the analysis and disappears in the instruction",
             "Advises identifying them early"],
         "correct": 2,
         "expl": "That gap between what the canon asserts and what it acts on is itself worth teaching."},
        {"q": "Which earlier discourses make the same claim in other language?",
         "opts": [
             "AN 3.13 in the language of hope, and AN 1.333&ndash;377 in the language of proportion",
             "AN 2.1 and AN 2.2",
             "AN 1.1&ndash;10",
             "AN 3.14 and AN 3.15"],
         "correct": 0,
         "expl": "Stated flatly, and the canon means it."},
        {"q": "What question is the triage argument actually answering?",
         "opts": [
             "Which patients deserve care",
             "<em>Why is treatment provided at all?</em> &mdash; the argument is about justification, not about worth",
             "How much care to give",
             "Who should provide care"],
         "correct": 1,
         "expl": "The answer is that there exists a class of case that treatment decides."},
    ],
    marginalia=[
        ("Three patients", [
            "will not recover, treated or not",
            "will recover, treated or not",
            "recovers only if treated",
        ]),
        ("The turn", [
            "care is <em>for</em> the third",
            "&ldquo;but also, for the sake of this patient,",
            "the other patients should be looked after&rdquo;",
        ]),
        ("Why", [
            "not compassion, not fairness",
            "&mdash; you cannot tell which is which",
        ]),
        ("Cross-references", [
            "AN 3.13 &middot; the same claim, as hope",
            "AN 1.333&ndash;377 &middot; as proportion",
            "AN 3.23 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.22/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-1.258-267.html">AN 1.258&ndash;267 &middot; Foremost Laywomen</a> &mdash; '
        "Suppiyā, foremost among those who care for the sick, and the only nursing entry anywhere on "
        "the foremost list.",
        '<a href="an-3.13.html">AN 3.13 &middot; Hopes</a> &mdash; the same three-way division made '
        "in the language of hope rather than of treatment.",
        '<a href="an-3.23.html">AN 3.23 &middot; Choices</a> &mdash; next in this series.',
    ],
)


page(
    23, "Saṅkhāra", "Choices",
    vagga=VAGGA_3,
    meta_title="AN 3.23 — Choices | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Saṅkhārasutta — "
        "hurtful choices, pleasing choices, and both, each producing a world, a contact, and "
        "a feeling of the same character. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals, each traced through the same four-step chain"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The analysis of choices producing a corresponding world and feeling is "
                              "standard across the Chinese Āgamas; this reading guide does not assert "
                              "a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short, and its chain is worth "
                       "following link by link"),
    ],
    why=(
        "Three individuals, and each is traced through the same four steps: choices, a world, a "
        "contact, a feeling. Hurtful choices produce a hurtful world where hurtful contacts strike "
        "and hurtful feelings are experienced. Pleasing choices produce the reverse. Mixed choices "
        "produce a mixed world, which the discourse names as the human one. What makes the discourse "
        "worth reading is the chain, not the conclusion &mdash; the character of the choice is carried "
        "through four distinct stages without ever changing."),
    guide=[
        ("The teaching in one sentence", [
            "The character of what you choose becomes the character of the world you are in, of what "
            "meets you there, and of what you feel."]),
        ("The four-step chain", [
            "It is stated identically three times. First, an individual makes choices &mdash; "
            "<em>saṅkhāra</em> &mdash; by way of body, speech, and mind, of a certain character. "
            "Second, they are reborn in a world of that character. Third, contacts of that character "
            "strike them there. Fourth, touched by those contacts, they feel feelings of that "
            "character.",
            "The steps are not redundant. A world of a certain character is not the same as contacts "
            "of that character; one could in principle be in a pleasant place and be met by something "
            "unpleasant. And contact is not the same as feeling; the canon elsewhere spends a great "
            "deal of effort on exactly that gap. What this discourse asserts is that in these three "
            "cases the character propagates through all four without loss.",
            "That is worth noticing precisely because the canon usually insists on the gap. AN 3.100 "
            "argues at length that the same deed produces very different results depending on the "
            "person; the whole framework of dependent origination is about where the chain can be "
            "broken. This discourse describes what happens when nothing intervenes."]),
        ("The third case is ours", [
            "The first two illustrations are extreme: the beings in hell, whose feelings are "
            "exclusively painful, and the gods of universal beauty, whose feelings are of perfect "
            "happiness. Both are stated as limit cases &mdash; unmixed.",
            "The third is <em>like humans, some gods, and some beings in the underworld</em>: hurtful "
            "and pleasing choices together, a world that is both, contacts that are both, feelings "
            "that are a mixture of pleasure and pain. That is the discourse&rsquo;s description of "
            "ordinary human experience, and it locates the mixture in the choices rather than in the "
            "circumstances.",
            "It is a plain claim and worth stating plainly: on this account the mixed quality of "
            "ordinary life is not bad luck. It is the shape of what has been chosen, arriving back."]),
        ("What <em>saṅkhāra</em> is doing here", [
            "The word is one of the hardest in the canon and it carries a wide range &mdash; "
            "formations, conditions, volitional activities, constructions. Sujato&rsquo;s "
            "&ldquo;choices&rdquo; is a strong and defensible narrowing for this context, where the "
            "term is being used of something a person does by way of body, speech, and mind and which "
            "then bears fruit.",
            "It is worth flagging the range anyway, because <em>saṅkhāra</em> in other contexts means "
            "something quite different &mdash; the conditioned in general, as in <em>all conditions "
            "are impermanent</em>, where nothing is being chosen by anyone. A reader who meets the "
            "word in both places and assumes one meaning will be confused by at least one of them.",
            "Here the choosing sense is clearly right: the discourse is about what a person does and "
            "what follows from it."]),
    ],
    terms=[
        ("saṅkhāra",
         "&ldquo;choices&rdquo; here; elsewhere formations, conditions, or the conditioned in general. "
         "One of the widest-ranging words in the canon, and Sujato&rsquo;s narrowing is contextual."),
        ("sabyābajjha / abyābajjha",
         "&ldquo;hurtful&rdquo; and &ldquo;pleasing&rdquo; &mdash; the same root met at AN 3.8 and AN "
         "3.17, carried here through four stages."),
        ("phassa",
         "&ldquo;contact&rdquo; &mdash; the third step, between the world one is in and the feeling "
         "one has. Distinguished from both."),
        ("Subhakiṇha",
         "&ldquo;the gods of universal beauty&rdquo; &mdash; the limit case of unmixed pleasant "
         "feeling, as the beings in hell are of unmixed painful feeling."),
        ("vokiṇṇasukhadukkha",
         "&ldquo;a mixture of pleasure and pain&rdquo; &mdash; the third case, illustrated by humans, "
         "some gods, and some beings in the underworld."),
    ],
    text_intro=(
        "The discourse in full: three individuals, each traced through the same chain. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Hurtful choices"),
        ("p", "&sect;1", "an3.23:1.1-1.6"),
        ("h3", "Pleasing choices"),
        ("p", "&sect;2", "an3.23:2.1-2.4"),
        ("h3", "Both"),
        ("p", "&sect;3", "an3.23:3.1-3.5"),
    ],
    quiz=[
        {"q": "What are the four steps of the chain?",
         "opts": [
             "Choices, a world, a contact, a feeling",
             "Ignorance, formations, consciousness, name-and-form",
             "Body, speech, mind, and result",
             "Cause, condition, effect, and end"],
         "correct": 0,
         "expl": "Stated identically three times, with the character carried through unchanged."},
        {"q": "Why does the guide say the steps are not redundant?",
         "opts": [
             "Because they occur at different times",
             "Because a world of a certain character is not the same as contacts of that character, and contact is not the same as feeling &mdash; one could be in a pleasant place and be met by something unpleasant",
             "Because each has a different cause",
             "Because they concern different people"],
         "correct": 1,
         "expl": "The discourse asserts that in these three cases the character propagates through all four without loss."},
        {"q": "Why is that worth noticing?",
         "opts": [
             "Because the canon usually insists on the gap &mdash; AN 3.100 argues the same deed produces different results depending on the person, and dependent origination is about where the chain can be broken",
             "Because the steps are unusual",
             "Because it contradicts the Vinaya",
             "Because it is a late addition"],
         "correct": 0,
         "expl": "This discourse describes what happens when nothing intervenes."},
        {"q": "Which two limit cases illustrate the first two individuals?",
         "opts": [
             "The beings in hell, whose feelings are exclusively painful, and the gods of universal beauty, whose feelings are of perfect happiness",
             "Kings and beggars",
             "Monastics and laypeople",
             "The young and the old"],
         "correct": 0,
         "expl": "Both stated as unmixed."},
        {"q": "What illustrates the third?",
         "opts": [
             "Only animals",
             "Humans, some gods, and some beings in the underworld &mdash; a mixture of pleasure and pain",
             "Only the gods",
             "No illustration is given"],
         "correct": 1,
         "expl": "The discourse's description of ordinary human experience."},
        {"q": "Where does the discourse locate the mixture?",
         "opts": [
             "In circumstances",
             "In the choices &mdash; on this account the mixed quality of ordinary life is not bad luck but the shape of what has been chosen, arriving back",
             "In the actions of others",
             "In chance"],
         "correct": 1,
         "expl": "A plain claim, and worth stating plainly."},
        {"q": "What range does <em>saṅkhāra</em> cover elsewhere?",
         "opts": [
             "Only volitional choices",
             "Formations, conditions, and the conditioned in general &mdash; as in &ldquo;all conditions are impermanent,&rdquo; where nothing is being chosen by anyone",
             "Only mental states",
             "Only bodily actions"],
         "correct": 1,
         "expl": "A reader who meets the word in both places and assumes one meaning will be confused by at least one."},
        {"q": "Is Sujato&rsquo;s &ldquo;choices&rdquo; defensible here?",
         "opts": [
             "No, it is a mistranslation",
             "Yes &mdash; a strong and defensible contextual narrowing, since the term is used of something a person does by way of body, speech, and mind that then bears fruit",
             "The guide does not say",
             "Only for the third individual"],
         "correct": 1,
         "expl": "The choosing sense is clearly right here; the range is worth flagging anyway."},
        {"q": "What is <em>phassa</em>?",
         "opts": [
             "&ldquo;Contact&rdquo; &mdash; the third step, between the world one is in and the feeling one has, and distinguished from both",
             "&ldquo;Feeling&rdquo;",
             "&ldquo;Choice&rdquo;",
             "&ldquo;World&rdquo;"],
         "correct": 0,
         "expl": "The canon spends a great deal of effort elsewhere on the gap between contact and feeling."},
        {"q": "Which root do <em>sabyābajjha</em> and <em>abyābajjha</em> share with earlier discourses in this chapter?",
         "opts": [
             "The root met at AN 3.8, hurtful deeds, and AN 3.17, hurting yourself and others",
             "The root of <em>bhaya</em>, danger",
             "The root of <em>kusala</em>, skillful",
             "None"],
         "correct": 0,
         "expl": "Carried here through four stages instead of named as a predicate."},
    ],
    marginalia=[
        ("The chain", [
            "choices",
            "a world",
            "contacts",
            "feelings",
            "&mdash; one character throughout",
        ]),
        ("Three cases", [
            "hurtful &middot; the beings in hell",
            "pleasing &middot; the gods of universal beauty",
            "both &middot; humans",
        ]),
        ("A hard word", [
            "<span class=\"pali\">saṅkhāra</span>here: choices",
            "elsewhere: the conditioned",
            "&mdash; and nothing is chosen there",
        ]),
        ("Cross-references", [
            "AN 3.100 &middot; where the chain does not propagate",
            "AN 3.17 &middot; the same root",
            "AN 3.24 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.23/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.100.html">AN 3.100 &middot; A Lump of Salt</a> &mdash; the discourse that '
        "complicates this one, arguing that the same deed produces very different results depending "
        "on the character of the person who does it.",
        '<a href="../samyutta-nikaya/sn-12.1.html">SN 12.1 &middot; Dependent Origination</a> &mdash; '
        "the full chain this discourse gives a four-step version of, and where the links can be broken.",
    ],
)


page(
    24, "Bahukāra", "Very Helpful",
    vagga=VAGGA_3,
    meta_title="AN 3.24 — Very Helpful | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Bahukārasutta — the "
        "three people who have done most for you, and the statement that they cannot easily "
        "be repaid. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals named by what they enabled, and a closing statement about "
                 "repayment"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The theme of the irrepayable debt to those who bring one to the "
                              "teaching is widespread in the Chinese Āgamas; this reading guide does "
                              "not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, and the closing sentence "
                       "connects it to one of the most consequential passages in the Twos"),
    ],
    why=(
        "Three people are very helpful to another: the one who enabled you to go for refuge, the one "
        "who enabled you to understand the four truths, and the one who enabled you to realize "
        "freedom. Nobody, the Buddha says, is more helpful than these three. And then the sentence "
        "that gives the discourse its weight: they cannot easily be repaid by any amount of respect "
        "or by any amount of material support. It is the same structure as AN 2.33 on parents, and "
        "reading the two together is how both are best understood."),
    guide=[
        ("The teaching in one sentence", [
            "The three people who brought you to refuge, to understanding, and to freedom cannot be "
            "repaid by respect or by goods."]),
        ("Three, in sequence", [
            "The three are stages of one journey, and each is defined by what they enabled rather than "
            "by who they are. Going for refuge to the Buddha, the teaching, and the Saṅgha. Truly "
            "understanding <em>this is suffering</em> and the other three truths. Realizing the "
            "undefiled freedom of heart and freedom by wisdom in this very life.",
            "Notice that no role is specified. The discourse does not say <em>your teacher</em>, or "
            "<em>a monastic</em>, or <em>the person who ordained you</em>. It says the individual who "
            "enabled it &mdash; whoever that turns out to have been. For many people the first of the "
            "three is not a teacher at all but a friend, a parent, or someone who lent them a book.",
            "It is also worth noticing that they may be three different people, or one person, or in "
            "principle nobody at all for the later stages. The discourse does not require the list to "
            "be filled."]),
        ("Why they cannot be repaid", [
            "The closing sentence names two currencies and rules out both. Not by bowing down, rising "
            "up, greeting with cupped palms, and observing proper etiquette &mdash; the full "
            "vocabulary of respect. And not by providing robes, almsfood, lodgings, and medicines "
            "&mdash; the full vocabulary of material support, and precisely the four requisites that "
            "AN 2.2 called the lay endeavor.",
            "So the two things a person actually has to offer, honor and goods, are both declared "
            "insufficient. The discourse does not then say what would be sufficient, and the silence "
            "is the interesting part.",
            "AN 2.33 asked the same question about parents and did answer it: what discharges the debt "
            "is establishing them in faith, ethics, generosity, and wisdom. Read the two discourses "
            "together and the answer here suggests itself without being stated &mdash; the only "
            "repayment available for having been brought to the teaching is bringing someone else. "
            "The canon does not say so in this discourse, and a guide should not pretend it does. But "
            "the parallel is exact and the two passages are plainly of a piece."]),
        ("The debt structure of the tradition", [
            "Put beside AN 2.33 and AN 2.136 &mdash; where acting rightly toward parents and toward "
            "the Realized One are given in identical language &mdash; this discourse completes a "
            "pattern. The canon recognizes a small number of irrepayable debts: to those who gave you "
            "your life, and to those who gave you the teaching.",
            "Both are handled the same way. The debt is affirmed as real and as beyond discharge by "
            "ordinary means; and the only currency that touches it is spiritual rather than material. "
            "That is the structure the Chinese tradition would later formalize as 四恩 &mdash; the four "
            "debts of gratitude, to parents, to beings, to rulers, and to the Three Jewels &mdash; and "
            "the two Pāli discourses behind it are AN 2.33 and this one.",
            "It is worth pointing out to students that this is not a system of obligation in the "
            "ordinary sense, because no one is owed anything by anyone. The three helpful individuals "
            "are not described as expecting repayment, and no duty toward them is prescribed. What is "
            "described is a fact about the size of what was received."]),
    ],
    terms=[
        ("bahukāra",
         "&ldquo;very helpful, of great service&rdquo; &mdash; said of the three individuals, and the "
         "discourse&rsquo;s name."),
        ("upanissāya",
         "&ldquo;relying on, by the support of&rdquo; &mdash; the sense in which each of the three "
         "enabled what followed. Each is defined by what they made possible, not by their role."),
        ("saraṇaṁ gato",
         "&ldquo;gone for refuge&rdquo; &mdash; the first of the three enablings, and the one most "
         "often owed to someone who is not a teacher at all."),
        ("na suppaṭikāraṁ",
         "&ldquo;not easily repaid&rdquo; &mdash; the same phrase used of mother and father at AN "
         "2.33, which is what links the two discourses."),
        ("cattāro paccayā",
         "robes, almsfood, lodgings, and medicines &mdash; the four requisites, named here as "
         "insufficient repayment and named at AN 2.2 as the whole of the lay endeavor."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three individuals very helpful to another"),
        ("p", "&sect;1", "an3.24:1.1-1.4"),
        ("p", "&sect;2", "an3.24:2.1-2.2"),
        ("p", "&sect;3", "an3.24:3.1-3.3"),
        ("h3", "And they cannot easily be repaid"),
        ("p", "&sect;4", "an3.24:4.1-4.2"),
    ],
    quiz=[
        {"q": "Which three individuals are named?",
         "opts": [
             "One&rsquo;s parents, teacher, and preceptor",
             "The one who enabled you to go for refuge, the one who enabled you to understand the four truths, and the one who enabled you to realize freedom",
             "The Buddha, the teaching, and the Saṅgha",
             "A donor, a teacher, and a companion"],
         "correct": 1,
         "expl": "Each defined by what they enabled rather than by who they are."},
        {"q": "What role does the discourse specify for them?",
         "opts": [
             "Teacher",
             "Monastic",
             "None &mdash; it says the individual who enabled it, whoever that turns out to have been",
             "Preceptor"],
         "correct": 2,
         "expl": "For many people the first is not a teacher at all but a friend, a parent, or someone who lent them a book."},
        {"q": "Which two currencies does the closing sentence rule out?",
         "opts": [
             "Respect &mdash; bowing, rising, cupped palms, proper etiquette &mdash; and material support: robes, almsfood, lodgings, and medicines",
             "Money and land",
             "Praise and obedience",
             "Time and effort"],
         "correct": 0,
         "expl": "The two things a person actually has to offer, both declared insufficient."},
        {"q": "What does the discourse say <em>would</em> be sufficient?",
         "opts": [
             "Nothing &mdash; it does not say, and the silence is the interesting part",
             "Ordination",
             "Building a monastery",
             "Lifelong service"],
         "correct": 0,
         "expl": "AN 2.33 asked the same question about parents and did answer it."},
        {"q": "What answer does AN 2.33 give for parents?",
         "opts": [
             "Lifelong material care",
             "Establishing them in faith, ethical conduct, generosity, and wisdom",
             "Performing their funeral rites",
             "Ordaining in their name"],
         "correct": 1,
         "expl": "Read together, the answer here suggests itself &mdash; though the canon does not say so in this discourse."},
        {"q": "How does the guide handle that suggestion?",
         "opts": [
             "By asserting it as the discourse&rsquo;s teaching",
             "By naming it as suggested by the parallel while saying plainly that the canon does not say so here and a guide should not pretend it does",
             "By ignoring it",
             "By rejecting it"],
         "correct": 1,
         "expl": "The parallel is exact and the two passages are plainly of a piece."},
        {"q": "What pattern does this discourse complete, beside AN 2.33 and AN 2.136?",
         "opts": [
             "A system of monastic seniority",
             "A small number of irrepayable debts &mdash; to those who gave you your life, and to those who gave you the teaching",
             "A ranking of the four assemblies",
             "A list of meditation objects"],
         "correct": 1,
         "expl": "Both handled the same way: the debt is real, beyond ordinary discharge, and touched only by spiritual currency."},
        {"q": "What did the Chinese tradition later formalize from this?",
         "opts": [
             "四恩 &mdash; the four debts of gratitude, to parents, to beings, to rulers, and to the Three Jewels",
             "四諦 &mdash; the four truths",
             "四攝 &mdash; the four ways of being inclusive",
             "四依 &mdash; the four reliances"],
         "correct": 0,
         "expl": "The two Pāli discourses behind it are AN 2.33 and this one."},
        {"q": "Why does the guide say this is not a system of obligation in the ordinary sense?",
         "opts": [
             "Because the debts are small",
             "Because no one is owed anything by anyone &mdash; the three are not described as expecting repayment, and no duty toward them is prescribed",
             "Because it applies only to monastics",
             "Because repayment is impossible"],
         "correct": 1,
         "expl": "What is described is a fact about the size of what was received."},
        {"q": "What phrase links this discourse to AN 2.33?",
         "opts": [
             "<em>Na suppaṭikāraṁ</em> &mdash; &ldquo;not easily repaid,&rdquo; used there of mother and father",
             "<em>Bahukāra</em>",
             "<em>Saraṇaṁ gato</em>",
             "<em>Cattāro paccayā</em>"],
         "correct": 0,
         "expl": "The same phrase, the same structure."},
    ],
    marginalia=[
        ("Three enablings", [
            "going for refuge",
            "understanding the four truths",
            "realizing freedom",
        ]),
        ("Two currencies ruled out", [
            "bowing, rising, cupped palms",
            "robes, almsfood, lodgings, medicines",
        ]),
        ("The parallel", [
            "AN 2.33 &middot; mother and father",
            "same phrase: not easily repaid",
            "&mdash; there, an answer is given",
        ]),
        ("Cross-references", [
            "AN 2.33 &middot; repaying parents",
            "AN 2.136 &middot; parents and the Realized One",
            "四恩 &middot; the later formalization",
        ]),
    ],
    further=[
        '<a href="%s/an3.24/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.32-41.html">AN 2.32&ndash;41 &middot; The Peaceful Mind</a> &mdash; AN 2.33 on '
        "repaying parents, which uses the same phrase and does supply an answer.",
        '<a href="/sutras/brahma-net-sutra/chapter-07/">The Brahmā Net Sūtra &middot; The Precept '
        "Preface</a> &mdash; where the debts to parents, teachers, and the Three Jewels are named in "
        "one breath and made the first content of the bodhisattva precepts.",
        '<a href="an-2.130-140.html">AN 2.130&ndash;140 &middot; Aspiration</a> &mdash; AN 2.136, '
        "where acting rightly toward parents and toward the Realized One are given in identical "
        "language.",
    ],
)


page(
    25, "Vajirūpama", "Like Diamond",
    vagga=VAGGA_3,
    meta_title="AN 3.25 — Like Diamond | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Vajirūpamasutta — "
        "three minds: one like an open sore, one like lightning, one like diamond. Three "
        "similes for irritability, insight, and the end of the defilements. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals, each named by a simile and then defined"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The diamond simile for the unbreakable mind is widespread in the "
                              "Chinese canon and gives the Diamond Sūtra its name; this reading guide "
                              "does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; three vivid images, and one gap "
                       "in the sequence worth noticing"),
    ],
    why=(
        "Three minds and three similes. A mind like an open sore, which discharges more when struck. "
        "A mind like lightning, which sees the whole landscape in a flash. A mind like diamond, which "
        "nothing can cut. The images are among the most memorable in the Threes, and the sequence has "
        "a gap in it that is worth noticing: the first is a description of ordinary bad temper, and "
        "the second is already the four truths understood. There is nothing in between."),
    guide=[
        ("The teaching in one sentence", [
            "A mind is either raw and discharging, or lit by a flash of understanding, or beyond "
            "damage."]),
        ("The open sore", [
            "The definition comes before the image and is unusually behavioral: irritable and "
            "bad-tempered; even when <em>lightly</em> criticized they lose their temper, becoming "
            "annoyed, hostile, and hard-hearted, and they display annoyance, hate, and bitterness.",
            "Two details carry the description. The provocation is small &mdash; the Pāli specifies "
            "that the criticism is slight. And the response is not merely felt but <em>displayed</em>: "
            "the discourse lists both the internal states and their exhibition.",
            "Then the image: a festering sore which, struck with a stick or a stone, discharges even "
            "more. What makes it precise is that a sore does not respond to being struck by hurting "
            "more; it responds by producing more of what it was already producing. The bad temper was "
            "there before the criticism. The criticism did not cause it &mdash; it released it.",
            "That is a more useful account of irritability than one which treats the provocation as "
            "the cause. It also explains why the size of the provocation does not predict the size of "
            "the response, which is the detail the definition led with."]),
        ("The lightning", [
            "The definition is the four truths truly understood. The image is a person with keen eyes "
            "in the dark of the night who sees by a flash of lightning.",
            "Every element does work. The eyes are keen &mdash; the capacity is already there. The "
            "night is dark &mdash; the ordinary condition is not seeing. And the flash is brief; what "
            "it gives is not illumination that lasts but a moment in which what is there becomes "
            "visible. A person who has seen a landscape by lightning knows the landscape afterward, in "
            "the dark.",
            "The simile is often read as describing the suddenness of insight, and it does. But its "
            "more interesting claim is about what the flash reveals: not something new arriving, but "
            "what was there all along, unlit."]),
        ("The diamond", [
            "The definition is the highest: realizing the undefiled freedom of heart and freedom by "
            "wisdom in this very life, having realized it with one&rsquo;s own insight due to the "
            "ending of defilements. The image is a diamond, which cannot be cut by anything at all, "
            "not even a gem or a stone.",
            "<em>Vajira</em> means both diamond and thunderbolt, and the word&rsquo;s later career in "
            "Buddhism is enormous &mdash; the Diamond Sūtra, whose full title names the "
            "<em>vajracchedikā</em>, the diamond-cutter, and the whole of Vajrayāna. What the image "
            "asserts here is narrow and physical: hardness, in the sense of not being alterable by "
            "anything brought against it.",
            "Read against the first simile, the contrast is exact. The open sore is defined by what "
            "happens when it is struck; the diamond is defined by what does not. Both are descriptions "
            "of a response to contact, and the middle term &mdash; the lightning &mdash; is the one "
            "that is not about contact at all."]),
        ("The gap in the sequence", [
            "It is worth stating plainly that these three are not a ladder with equal rungs. The first "
            "describes a person with a temper &mdash; a condition anyone can recognize in themselves "
            "or a colleague. The second describes someone who has understood the four truths, which in "
            "the canon&rsquo;s technical vocabulary means at least stream-entry. The third is full "
            "awakening.",
            "So the sequence runs: ordinary bad temper, then a stage of the noble path, then the end "
            "of the path. Nothing occupies the space between the first and the second, and the "
            "discourse does not remark on it.",
            "That shape is characteristic of the Aṅguttara&rsquo;s three-person lists and worth "
            "flagging for students, who reasonably expect a middle term to be a middle. What these "
            "lists usually give instead is one recognizable case and two attainments &mdash; the "
            "recognizable case doing the work of making the set memorable, and the other two doing the "
            "work of naming what is possible."]),
    ],
    terms=[
        ("arukūpama",
         "&ldquo;like an open sore&rdquo; &mdash; a festering wound which, struck, discharges more of "
         "what it was already producing."),
        ("vijjūpama",
         "&ldquo;like lightning&rdquo; &mdash; the flash by which keen eyes see in the dark. Brief, "
         "and revealing what was already there."),
        ("vajirūpama",
         "&ldquo;like diamond&rdquo; &mdash; <em>vajira</em> means both diamond and thunderbolt, and "
         "gives its name to the Diamond Sūtra and to Vajrayāna. Here the claim is narrow: not "
         "alterable by anything brought against it."),
        ("appamattakena",
         "&ldquo;lightly, by a little&rdquo; &mdash; the size of the criticism that provokes the first "
         "individual, and the detail the definition leads with."),
        ("āsavānaṁ khayā",
         "&ldquo;due to the ending of defilements&rdquo; &mdash; the definition of the third, and the "
         "canon&rsquo;s standard formula for full awakening."),
    ],
    text_intro=(
        "The discourse in full: three individuals, each defined and then given a simile. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A mind like an open sore"),
        ("p", "&sect;1", "an3.25:1.1-1.10"),
        ("h3", "A mind like lightning"),
        ("p", "&sect;2", "an3.25:2.1-2.5"),
        ("h3", "A mind like diamond"),
        ("p", "&sect;3", "an3.25:3.1-3.6"),
    ],
    quiz=[
        {"q": "What are the three minds?",
         "opts": [
             "Like an open sore, like lightning, and like diamond",
             "Like water, like fire, and like earth",
             "Like a child, an adult, and an elder",
             "Like a seed, a shoot, and a tree"],
         "correct": 0,
         "expl": "Among the most memorable images in the Threes."},
        {"q": "How large is the provocation that sets off the first individual?",
         "opts": [
             "A serious accusation",
             "Slight &mdash; the Pāli specifies that the criticism is light",
             "A physical attack",
             "The discourse does not say"],
         "correct": 1,
         "expl": "The detail the definition leads with."},
        {"q": "What is precise about the sore simile?",
         "opts": [
             "That a sore is painful",
             "That a sore struck does not hurt more but produces more of what it was already producing &mdash; the bad temper was there before the criticism, which released rather than caused it",
             "That sores heal slowly",
             "That sores are visible"],
         "correct": 1,
         "expl": "A more useful account of irritability than one treating the provocation as the cause."},
        {"q": "What does that explain?",
         "opts": [
             "Why criticism should be avoided",
             "Why the size of the provocation does not predict the size of the response",
             "Why sores fester",
             "Why the person displays their anger"],
         "correct": 1,
         "expl": "Which is exactly what the definition led with."},
        {"q": "What is the definition behind the lightning simile?",
         "opts": [
             "Quick thinking",
             "The four truths truly understood",
             "Psychic power",
             "A sudden temper"],
         "correct": 1,
         "expl": "Which in the canon's technical vocabulary means at least stream-entry."},
        {"q": "What does the guide say is the more interesting claim of the lightning image?",
         "opts": [
             "That insight is sudden",
             "That the flash reveals not something new arriving but what was there all along, unlit",
             "That the night is dangerous",
             "That eyesight must be trained"],
         "correct": 1,
         "expl": "A person who has seen a landscape by lightning knows the landscape afterward, in the dark."},
        {"q": "What does <em>vajira</em> mean, and where does the word go later?",
         "opts": [
             "Both diamond and thunderbolt &mdash; and it names the Diamond Sūtra and the whole of Vajrayāna",
             "Only diamond &mdash; and it has no later career",
             "Only thunderbolt",
             "Stone"],
         "correct": 0,
         "expl": "What the image asserts here is narrow and physical: hardness."},
        {"q": "How do the first and third similes contrast exactly?",
         "opts": [
             "One is soft and one is hard",
             "The open sore is defined by what happens when it is struck; the diamond by what does not &mdash; both are descriptions of a response to contact",
             "One is alive and one is not",
             "One is small and one is large"],
         "correct": 1,
         "expl": "And the middle term, the lightning, is the one not about contact at all."},
        {"q": "What gap does the guide point out in the sequence?",
         "opts": [
             "None",
             "The first describes ordinary bad temper, the second a stage of the noble path, the third full awakening &mdash; nothing occupies the space between the first and second, and the discourse does not remark on it",
             "The third is missing a definition",
             "The similes do not match the definitions"],
         "correct": 1,
         "expl": "These three are not a ladder with equal rungs."},
        {"q": "What does the guide say is characteristic of the Aṅguttara&rsquo;s three-person lists?",
         "opts": [
             "That they always progress evenly",
             "That they usually give one recognizable case and two attainments &mdash; the recognizable case making the set memorable, the other two naming what is possible",
             "That they concern only monastics",
             "That the middle term is always the most important"],
         "correct": 1,
         "expl": "Worth flagging for students, who reasonably expect a middle term to be a middle."},
    ],
    marginalia=[
        ("Three minds", [
            "<span class=\"pali\">arukūpama</span>an open sore",
            "<span class=\"pali\">vijjūpama</span>lightning",
            "<span class=\"pali\">vajirūpama</span>diamond",
        ]),
        ("The sore", [
            "struck lightly",
            "discharges more of what was there",
            "&mdash; released, not caused",
        ]),
        ("The gap", [
            "1 &middot; a bad temper",
            "2 &middot; the four truths understood",
            "3 &middot; the defilements ended",
            "&mdash; nothing between 1 and 2",
        ]),
        ("Cross-references", [
            "Diamond Sūtra &middot; where <em>vajira</em> goes",
            "AN 3.21 &middot; three individuals, ranked",
            "AN 3.26 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.25/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="/sutras/diamond-sutra/opening-and-non-abiding-giving.html">The Diamond Sūtra '
        "&middot; Opening</a> &mdash; where <em>vajira</em> ends up: a text named for the "
        "diamond-cutter, and the most familiar use of this image in East Asia.",
        '<a href="an-3.21.html">AN 3.21 &middot; With Saviṭṭha</a> &mdash; another three-person list '
        "in this chapter, and the discourse that shows what happens when someone tries to rank one.",
    ],
)


page(
    26, "Sevitabba", "Associates",
    vagga=VAGGA_3,
    meta_title="AN 3.26 — Associates | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sevitabbasutta — "
        "whom to keep away from, whom to keep company with, and whom to attend with honor, "
        "sorted by ethics, immersion, and wisdom. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals defined by comparison with oneself, each with a stated reason, "
                 "closing in verse"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Advice on choosing company by ethical and meditative standing is "
                              "widespread in the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain advice, with one clause "
                       "that stops it being merely self-interested"),
    ],
    why=(
        "Sort the people around you by ethics, immersion, and wisdom, relative to yourself. Those "
        "below you: do not associate with them. Those level with you: do. Those above you: do, and "
        "with honor and respect. Stated baldly that is social climbing with a spiritual vocabulary, "
        "and the discourse would deserve the objection if it stopped there. It does not: the first "
        "case carries an exception, and the exception is the reason the discourse is worth reading."),
    guide=[
        ("The teaching in one sentence", [
            "Keep company with your equals and your betters in ethics, immersion, and wisdom &mdash; "
            "and go to your inferiors only out of kindness."]),
        ("The exception in the first case", [
            "The instruction about the person inferior in ethics, immersion, and wisdom is: do not "
            "associate with, accompany, or attend them &mdash; <em>except out of kindness and "
            "sympathy</em>.",
            "That clause changes the character of the whole discourse. Without it, the advice is about "
            "protecting one&rsquo;s own development, and the person below you is simply a hazard. With "
            "it, there remains exactly one reason to seek them out, and it is the only reason the "
            "discourse allows: their benefit rather than yours.",
            "So the rule is not <em>avoid the worse</em>. It is: do not go to them for what you would "
            "go to an equal or a better for. Company for your own sake goes upward or sideways; going "
            "downward is not company but help, and the discourse marks the difference by naming the "
            "motive."]),
        ("Why equals", [
            "The reason given for keeping company with equals is unexpectedly concrete and has nothing "
            "to do with attainment. <em>Since our ethical conduct is similar, we can discuss ethics, "
            "the conversation will flow, and we&rsquo;ll both be at ease.</em> And the same for "
            "immersion and for wisdom.",
            "What is being valued is a conversation that works. Two people at the same level can "
            "actually talk about the thing &mdash; neither is explaining and neither is struggling to "
            "follow &mdash; and the discourse names the ease of it as the point. That is an unusually "
            "sociable reason to find in a list about spiritual company, and it is worth pointing out "
            "to students who expect the canon to recommend only vertical relationships.",
            "It also implies something about peers that the tradition does not otherwise say much "
            "about. A teacher gives you what you lack; an equal gives you a conversation. Both are on "
            "the list."]),
        ("Why betters, and what &ldquo;with honor&rdquo; adds", [
            "The person superior in the three is to be attended <em>with honor and respect</em> "
            "&mdash; the extra clause that distinguishes this case from the second. And the reason is "
            "stated as a first-person resolve: I will fulfill the ethics, immersion, and wisdom I have "
            "not yet fulfilled, or support with wisdom what I have.",
            "Note that both halves are named. Association upward is not only for acquiring what one "
            "lacks but for consolidating what one has. That second half is easy to skip and it is the "
            "more realistic of the two: most of what a practitioner gets from someone further along is "
            "not new material but confirmation that what they already do is sound."]),
        ("The closing verse", [
            "<em>A man who associates with an inferior goes downhill, but associating with an equal, "
            "you&rsquo;ll never decline; following the best, you&rsquo;ll quickly rise up, so you "
            "should keep company with people better than you.</em>",
            "The verse compresses the prose and, in compressing it, drops the exception. Read alone it "
            "is the bare social advice; read after the prose it is a summary that assumes the "
            "qualification has already been made. That is a common relationship between a "
            "discourse&rsquo;s prose and its closing verse, and it is worth knowing about, because "
            "these verses travel independently and get quoted without what preceded them.",
            "The same verse closes AN 3.27, the next discourse. Both times it follows a fuller "
            "treatment that is more careful than the verse is."]),
    ],
    terms=[
        ("sevitabba",
         "&ldquo;to be associated with&rdquo; &mdash; the gerundive that gives the discourse its name; "
         "the question throughout is who <em>should</em> be kept company with."),
        ("bhajitabba / payirupāsitabba",
         "&ldquo;to be accompanied&rdquo; and &ldquo;to be attended&rdquo; &mdash; the two further "
         "verbs, running from casual association to sitting at someone&rsquo;s feet."),
        ("anukampaṁ upādāya",
         "&ldquo;out of kindness and sympathy&rdquo; &mdash; the exception that permits going to "
         "someone below one in the three, and the clause that changes the discourse&rsquo;s character."),
        ("sīla, samādhi, paññā",
         "ethics, immersion, and wisdom &mdash; the three axes of comparison, and the canon&rsquo;s "
         "standard division of the training."),
        ("sakkatvā garuṁ katvā",
         "&ldquo;with honor and respect&rdquo; &mdash; the addition that distinguishes attending a "
         "superior from keeping company with an equal."),
    ],
    text_intro=(
        "The discourse in full, closing in verse. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three individuals"),
        ("p", "&sect;1", "an3.26:1.1-1.8"),
        ("h3", "The equal"),
        ("p", "&sect;2", "an3.26:2.1-2.8"),
        ("h3", "The superior"),
        ("p", "&sect;3", "an3.26:3.1-3.9"),
        ("h3", "In verse"),
        ("p", "&sect;4", "an3.26:4.1-4.4"),
    ],
    quiz=[
        {"q": "By what are the three individuals sorted?",
         "opts": [
             "Seniority, learning, and reputation",
             "Ethics, immersion, and wisdom, relative to oneself",
             "Wealth, birth, and health",
             "Age, ordination, and office"],
         "correct": 1,
         "expl": "The canon's standard division of the training, used here as a social sorting."},
        {"q": "What exception attaches to the first case?",
         "opts": [
             "None",
             "&ldquo;Except out of kindness and sympathy&rdquo;",
             "Except when they ask",
             "Except in a monastery"],
         "correct": 1,
         "expl": "The clause that changes the character of the whole discourse."},
        {"q": "How does that exception change the rule?",
         "opts": [
             "It does not",
             "The rule is not &ldquo;avoid the worse&rdquo; but &ldquo;do not go to them for what you would go to an equal or a better for&rdquo; &mdash; going downward is not company but help",
             "It permits all association",
             "It restricts the rule to monastics"],
         "correct": 1,
         "expl": "The discourse marks the difference by naming the motive."},
        {"q": "What reason is given for keeping company with equals?",
         "opts": [
             "That they will not lead one astray",
             "That the conversation works &mdash; both can discuss the thing, it will flow, and both will be at ease",
             "That they are easier to find",
             "That they need help"],
         "correct": 1,
         "expl": "An unusually sociable reason to find in a list about spiritual company."},
        {"q": "What does the guide say that implies about peers?",
         "opts": [
             "That they are unnecessary",
             "That a teacher gives you what you lack and an equal gives you a conversation &mdash; and both are on the list",
             "That peers should be avoided",
             "That peers are the same as teachers"],
         "correct": 1,
         "expl": "Worth pointing out to students who expect the canon to recommend only vertical relationships."},
        {"q": "What extra clause distinguishes the third case?",
         "opts": [
             "&ldquo;With honor and respect&rdquo;",
             "&ldquo;Out of kindness&rdquo;",
             "&ldquo;From time to time&rdquo;",
             "&ldquo;In private&rdquo;"],
         "correct": 0,
         "expl": "<em>Sakkatvā garuṁ katvā</em>."},
        {"q": "What two halves does the resolve behind attending a superior contain?",
         "opts": [
             "Fulfilling what one has not yet fulfilled, and supporting with wisdom what one already has",
             "Learning and teaching",
             "Giving and receiving",
             "Asking and answering"],
         "correct": 0,
         "expl": "Association upward is not only for acquiring what one lacks."},
        {"q": "Which half does the guide call more realistic?",
         "opts": [
             "The first",
             "The second &mdash; most of what a practitioner gets from someone further along is not new material but confirmation that what they already do is sound",
             "Neither",
             "The guide does not say"],
         "correct": 1,
         "expl": "Easy to skip in the reading."},
        {"q": "What does the closing verse drop?",
         "opts": [
             "The three axes",
             "The exception &mdash; read alone it is the bare social advice",
             "The superior individual",
             "Nothing"],
         "correct": 1,
         "expl": "A summary that assumes the qualification has already been made."},
        {"q": "Why does the guide say that matters?",
         "opts": [
             "Because the verse is inauthentic",
             "Because these verses travel independently and get quoted without what preceded them &mdash; and the same verse closes AN 3.27 as well",
             "Because verses are harder to translate",
             "Because the prose is optional"],
         "correct": 1,
         "expl": "Both times it follows a fuller treatment that is more careful than the verse is."},
    ],
    marginalia=[
        ("Three, by comparison", [
            "below you &middot; do not associate",
            "level with you &middot; do",
            "above you &middot; do, with honor",
        ]),
        ("The exception", [
            "<span class=\"pali\">anukampaṁ upādāya</span>out of kindness",
            "&mdash; not company, but help",
        ]),
        ("Why equals", [
            "the conversation flows",
            "both are at ease",
            "&mdash; a sociable reason",
        ]),
        ("Cross-references", [
            "AN 3.27 &middot; next, same closing verse",
            "AN 1.71&ndash;81 &middot; good friendship",
            "AN 2.118&ndash;129 &middot; the voice of another",
        ]),
    ],
    further=[
        '<a href="%s/an3.26/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-1.71-81.html">AN 1.71&ndash;81 &middot; Good Friends</a> &mdash; where good '
        "friendship is called not half but the whole of the spiritual life, which this discourse turns "
        "into a sorting rule.",
        '<a href="an-2.118-129.html">AN 2.118&ndash;129 &middot; Hopes Hard to Give Up</a> &mdash; the '
        "discourse that explains why company matters this much: the voice of another is the sole "
        "external source of view, right or wrong.",
        '<a href="an-3.27.html">AN 3.27 &middot; You Should be Disgusted</a> &mdash; next in this '
        "series, which sorts the same field by a different criterion.",
    ],
)


page(
    27, "Jigucchitabba", "You Should be Disgusted",
    vagga=VAGGA_3,
    meta_title="AN 3.27 — You Should be Disgusted | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Jigucchitabbasutta — "
        "three people to be disgusted by, regarded with equanimity, or kept company with, "
        "with the snake in the dunghill and the firebrand of ebony. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals, each with a prescribed attitude, a reason, and one or more "
                 "similes; closing on the same verse as AN 3.26"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "Comparable material on bad association appears in the Chinese Āgamas; "
                              "this reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; vivid and direct, and worth "
                       "reading for the difference between its first two prescriptions"),
    ],
    why=(
        "The previous discourse sorted people by ethics, immersion, and wisdom. This one sorts them by "
        "what attitude to take: be disgusted by the corrupt, regard the bad-tempered with equanimity, "
        "keep company with the ethical. The two negative prescriptions are different, and the "
        "difference is the discourse&rsquo;s content &mdash; disgust and equanimity are not two "
        "strengths of the same reaction but two reactions to two different problems."),
    guide=[
        ("The teaching in one sentence", [
            "Corruption calls for disgust and distance; bad temper calls for equanimity and distance; "
            "and only good character calls for company."]),
        ("Disgust, and the snake in the dunghill", [
            "The first individual is described in the canon&rsquo;s harshest register: unethical, of "
            "bad qualities, filthy, of suspicious behavior, underhand, no true ascetic though claiming "
            "to be one, <em>rotten inside, festering, and depraved</em>. The prescription is disgust "
            "and complete avoidance.",
            "The reason is not what one might expect. It is not that you will be corrupted by them "
            "&mdash; the discourse explicitly says <em>even if you don&rsquo;t follow the example of "
            "such an individual</em>. It is that you will get a bad reputation: <em>that individual "
            "has bad friends, companions, and associates.</em>",
            "And the simile is exact about the mechanism. A snake that has been living in a dunghill: "
            "even if it does not bite, it will still rub off on you. The danger named is not venom but "
            "residue. Association transfers something whether or not anything happens.",
            "That is a claim about reputation, and it is worth being honest that it is a prudential "
            "argument rather than a moral one. The discourse does not say the corrupt person will make "
            "you corrupt. It says being seen with them will cost you, and treats that cost as "
            "sufficient reason."]),
        ("Equanimity, and three similes for one temper", [
            "The second individual is the irritable and bad-tempered person of AN 3.25 &mdash; the "
            "same definition word for word, down to being lightly criticized. But where AN 3.25 gave "
            "one simile, this discourse gives three.",
            "The festering sore, struck, discharges more. A firebrand of pale-moon ebony, struck, "
            "sizzles and crackles more. A sewer, stirred, stinks more. Three different sensory "
            "registers &mdash; sight, sound, smell &mdash; for the same mechanism: contact produces "
            "an increase of what was already there.",
            "The prescribed attitude is equanimity, not disgust, and the reason given is purely "
            "practical: <em>they might abuse or insult me, or do me harm.</em> No moral judgment is "
            "passed on the bad-tempered person at all. They are a hazard to be given room, not a "
            "corruption to be recoiled from.",
            "That distinction is the most useful thing in the discourse. Corruption gets disgust "
            "because it is a moral condition that contaminates by association. Bad temper gets "
            "equanimity because it is a hazard that injures on contact. Two problems, two attitudes, "
            "and the same practical conclusion &mdash; distance &mdash; reached by different routes."]),
        ("And the third", [
            "The person to keep company with is simply <em>ethical, of good character</em> &mdash; no "
            "further qualification, and a much lower bar than AN 3.26&rsquo;s superior in ethics, "
            "immersion, and wisdom.",
            "The reason is the mirror of the first: even if you do not follow their example, you get a "
            "good reputation. The whole discourse runs on the same prudential logic in both "
            "directions, which is consistent if unedifying, and honest about what it is doing."]),
        ("The verse it shares with AN 3.26", [
            "The closing verse is identical to the previous discourse&rsquo;s: associate with an "
            "inferior and go downhill, with an equal and never decline, with the best and quickly rise.",
            "Reading the two discourses in sequence shows what a shared verse does in this literature. "
            "The prose of AN 3.26 sorts by attainment and adds an exception for kindness; the prose of "
            "AN 3.27 sorts by character and adds a distinction between disgust and equanimity. The "
            "verse fits both and captures neither qualification. It is a mnemonic, not a summary, and "
            "the two discourses it closes are more careful than it is."]),
    ],
    terms=[
        ("jigucchitabba",
         "&ldquo;to be disgusted by&rdquo; &mdash; the attitude prescribed toward the first "
         "individual, and the discourse&rsquo;s name."),
        ("ajjhupekkhitabba",
         "&ldquo;to be regarded with equanimity&rdquo; &mdash; the attitude prescribed toward the "
         "second. Not a weaker disgust but a different response to a different problem."),
        ("antopūti avassuta kasambujāta",
         "&ldquo;rotten inside, festering, and depraved&rdquo; &mdash; the canon&rsquo;s harshest "
         "register, reserved for one claiming to be an ascetic and not being one."),
        ("gūthagata ahi",
         "&ldquo;a snake living in a dunghill&rdquo; &mdash; the simile for the first individual. The "
         "danger named is residue rather than venom."),
        ("pāpamitta",
         "&ldquo;bad friend&rdquo; &mdash; what one is reputed to have, which is the actual reason the "
         "discourse gives for avoidance."),
    ],
    text_intro=(
        "The discourse in full, closing on the same verse as AN 3.26. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "The one to be disgusted by"),
        ("p", "&sect;1", "an3.27:1.1-1.15"),
        ("h3", "The one to regard with equanimity"),
        ("p", "&sect;2", "an3.27:2.1-2.14"),
        ("h3", "The one to keep company with"),
        ("p", "&sect;3", "an3.27:3.1-3.8"),
        ("h3", "In verse"),
        ("p", "&sect;4", "an3.27:4.1-4.4"),
    ],
    quiz=[
        {"q": "What three attitudes does the discourse prescribe?",
         "opts": [
             "Disgust, equanimity, and company",
             "Pity, patience, and praise",
             "Avoidance, tolerance, and imitation",
             "Fear, respect, and love"],
         "correct": 0,
         "expl": "Two of the three end in distance, reached by different routes."},
        {"q": "What reason does the discourse give for avoiding the corrupt person?",
         "opts": [
             "That you will be corrupted by them",
             "That you will get a bad reputation &mdash; explicitly &ldquo;even if you don&rsquo;t follow the example of such an individual&rdquo;",
             "That they will harm you physically",
             "That they will waste your time"],
         "correct": 1,
         "expl": "A prudential argument rather than a moral one, and the guide says so."},
        {"q": "What does the snake simile say about the mechanism?",
         "opts": [
             "That the snake will bite",
             "That even if it does not bite, it will still rub off on you &mdash; the danger is residue, not venom",
             "That snakes are inherently evil",
             "That dunghills should be avoided"],
         "correct": 1,
         "expl": "Association transfers something whether or not anything happens."},
        {"q": "How is the second individual defined?",
         "opts": [
             "As unethical and corrupt",
             "As irritable and bad-tempered, losing their temper even when lightly criticized &mdash; the same definition as AN 3.25, word for word",
             "As lazy",
             "As ignorant"],
         "correct": 1,
         "expl": "Where AN 3.25 gave one simile, this discourse gives three."},
        {"q": "What three similes are used for the bad-tempered person?",
         "opts": [
             "A festering sore, a firebrand of pale-moon ebony, and a sewer",
             "A snake, a fire, and a flood",
             "A wheel, a pot, and a lamp",
             "A dog, a jackal, and a crow"],
         "correct": 0,
         "expl": "Sight, sound, and smell &mdash; three registers for one mechanism."},
        {"q": "What is that mechanism?",
         "opts": [
             "That contact causes new damage",
             "That contact produces an increase of what was already there",
             "That contact spreads corruption",
             "That contact provokes retaliation"],
         "correct": 1,
         "expl": "The same point AN 3.25 made with the sore alone."},
        {"q": "What reason is given for equanimity rather than disgust?",
         "opts": [
             "That the person may improve",
             "A purely practical one &mdash; &ldquo;they might abuse or insult me, or do me harm&rdquo;; no moral judgment is passed at all",
             "That anger is not a fault",
             "That equanimity is always preferable"],
         "correct": 1,
         "expl": "A hazard to be given room, not a corruption to be recoiled from."},
        {"q": "What is the distinction the guide calls the most useful thing in the discourse?",
         "opts": [
             "That corruption contaminates by association and gets disgust, while bad temper injures on contact and gets equanimity &mdash; two problems, two attitudes, one practical conclusion",
             "That both are equally bad",
             "That neither should be avoided",
             "That only monastics need apply it"],
         "correct": 0,
         "expl": "Disgust and equanimity are not two strengths of one reaction."},
        {"q": "How is the third individual described?",
         "opts": [
             "As superior in ethics, immersion, and wisdom",
             "Simply as ethical, of good character &mdash; a much lower bar than AN 3.26&rsquo;s",
             "As a teacher",
             "As a monastic"],
         "correct": 1,
         "expl": "And the reason is the mirror of the first: you get a good reputation."},
        {"q": "What does the guide say about the verse shared with AN 3.26?",
         "opts": [
             "That it summarizes both discourses accurately",
             "That it fits both and captures neither qualification &mdash; it is a mnemonic, not a summary, and the two discourses it closes are more careful than it is",
             "That it belongs only to AN 3.26",
             "That it contradicts the prose"],
         "correct": 1,
         "expl": "AN 3.26 adds an exception for kindness; AN 3.27 distinguishes disgust from equanimity; the verse has neither."},
    ],
    marginalia=[
        ("Three attitudes", [
            "<span class=\"pali\">jigucchitabba</span>be disgusted by",
            "<span class=\"pali\">ajjhupekkhitabba</span>regard with equanimity",
            "<span class=\"pali\">sevitabba</span>keep company with",
        ]),
        ("Two problems", [
            "corruption &middot; contaminates by association",
            "bad temper &middot; injures on contact",
            "&mdash; same distance, different route",
        ]),
        ("Three similes, one temper", [
            "a sore, struck",
            "ebony in the fire, struck",
            "a sewer, stirred",
        ]),
        ("Cross-references", [
            "AN 3.25 &middot; the same temper, one simile",
            "AN 3.26 &middot; the same closing verse",
            "AN 3.28 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.27/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.25.html">AN 3.25 &middot; Like Diamond</a> &mdash; the same definition of the '
        "bad-tempered person with a single simile, where it serves a different argument.",
        '<a href="an-3.26.html">AN 3.26 &middot; Associates</a> &mdash; the previous discourse, '
        "which sorts the same field by attainment rather than by character and adds the exception for "
        "kindness that this one does not repeat.",
    ],
)


page(
    28, "Gūthabhāṇī", "Speech like Dung",
    vagga=VAGGA_3,
    meta_title="AN 3.28 — Speech like Dung | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Gūthabhāṇīsutta — "
        "speech like dung, like flowers, and like honey, with the first two defined by "
        "testimony under oath. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals named by simile, the first two defined by an identical scene "
                 "with the answers reversed"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The threefold classification of speech is found across the Chinese "
                              "Āgamas; this reading guide does not assert a specific matching sutra "
                              "number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; simple, and its middle term is "
                       "set lower than most readers expect"),
    ],
    why=(
        "Three kinds of speech, named by what they are like: dung, flowers, honey. The scene that "
        "defines the first two is the same for both &mdash; being summoned to give evidence before a "
        "council, an assembly, a family meeting, a guild, or the royal court &mdash; and the "
        "difference is only whether the answers are true. What makes the discourse worth reading is "
        "where it puts the middle term: speech like flowers is not eloquence. It is not lying under "
        "oath."),
    guide=[
        ("The teaching in one sentence", [
            "Lying under oath is like dung, telling the truth under oath is like flowers, and kind "
            "speech is like honey."]),
        ("The scene, and why it is specified", [
            "The setting is a formal one and the list of venues is worth reading: a council, an "
            "assembly, a family meeting, a guild, or the royal court. Those are the places where "
            "disputes were actually settled &mdash; public, domestic, commercial, and judicial &mdash; "
            "and a person is called to say what they know.",
            "The formula for the lie is precise and fourfold: not knowing, they say <em>I know</em>; "
            "knowing, they say <em>I don&rsquo;t know</em>; not seeing, <em>I see</em>; seeing, "
            "<em>I don&rsquo;t see</em>. Both directions of both faculties, so that withholding is "
            "counted alongside asserting. Someone who conceals what they saw has lied by this "
            "definition exactly as much as someone who invents.",
            "And the motives are named: for the sake of themselves or another, <em>or for some trivial "
            "worldly reason</em>. That last clause is the sharp one. The definition does not require "
            "the lie to be self-serving or even to matter; a trivial reason qualifies. Most lying is "
            "not dramatic, and the discourse knows it."]),
        ("Where the middle term is set", [
            "Speech like flowers is the same scene with the four answers reversed: not knowing, they "
            "say <em>I don&rsquo;t know</em>; and so on. That is the whole definition.",
            "It is worth stopping on how low that bar is. Flowers, in this taxonomy, is not beautiful "
            "speech, or wise speech, or helpful speech. It is answering a question accurately when "
            "under obligation to answer. A person who has never lied in a formal setting has speech "
            "like flowers, and nothing further is required of them.",
            "That is a useful correction to a common assumption about the canon&rsquo;s standards. The "
            "middle term of a three-term list is often read as a decent intermediate achievement. Here "
            "it is the absence of a specific fault, and the discourse is content to praise it in those "
            "terms."]),
        ("Honey, and what it adds", [
            "The third is defined differently: not by a scene but by a practice. Such a person "
            "<em>gives up harsh speech</em> and speaks in a way that is mellow, pleasing to the ear, "
            "endearing, going to the heart, polite, likable and agreeable to people.",
            "So the third term is not a further degree of truthfulness. It is a different axis "
            "entirely: the first two concern accuracy, the third concerns manner. Honey is not "
            "truer than flowers; it is kinder, and the discourse does not say whether it is also true.",
            "That gap is worth noticing rather than filling in. The canon elsewhere treats these as "
            "separate factors of right speech &mdash; abstaining from lying, from divisive speech, "
            "from harsh speech, from idle chatter &mdash; and a person can satisfy one and fail "
            "another. Reading the three terms of this discourse as a single ladder produces a "
            "confusion the fourfold analysis of right speech avoids."]),
        ("The images", [
            "The three similes are not explained and do not need to be. What is worth noting is their "
            "ordering by what one does with them: dung is what you get away from, flowers are what you "
            "are pleased to receive, honey is what you actually want. The scale runs from repulsion "
            "through acceptability to desire.",
            "It also runs from what speech is like to what speech does to the hearer, which is the "
            "same progression the definitions make: the first two are about the speaker&rsquo;s "
            "relation to the facts, and the third is about the listener&rsquo;s experience."]),
    ],
    terms=[
        ("gūthabhāṇī",
         "&ldquo;one whose speech is like dung&rdquo; &mdash; the discourse&rsquo;s name, defined by "
         "lying under formal obligation to answer."),
        ("pupphabhāṇī",
         "&ldquo;one whose speech is like flowers&rdquo; &mdash; and the bar is not eloquence but "
         "accuracy: answering truthfully when called to bear witness."),
        ("madhubhāṇī",
         "&ldquo;one whose speech is like honey&rdquo; &mdash; defined not by a scene but by giving "
         "up harsh speech; a different axis from the first two."),
        ("sampajānamusā bhāsati",
         "&ldquo;deliberately lies&rdquo; &mdash; the fourfold formula covering both asserting what is "
         "not so and withholding what is."),
        ("appamattakassa lokāmisassa hetu",
         "&ldquo;for some trivial worldly reason&rdquo; &mdash; the clause that removes any "
         "requirement for the lie to be significant."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Speech like dung"),
        ("p", "&sect;1", "an3.28:1.1-1.6"),
        ("h3", "Speech like flowers"),
        ("p", "&sect;2", "an3.28:2.1-2.3"),
        ("h3", "Speech like honey"),
        ("p", "&sect;3", "an3.28:3.1-3.5"),
    ],
    quiz=[
        {"q": "What scene defines the first two individuals?",
         "opts": [
             "A monastic recitation",
             "Being summoned to bear witness before a council, an assembly, a family meeting, a guild, or the royal court",
             "A conversation with the Buddha",
             "An alms round"],
         "correct": 1,
         "expl": "The places where disputes were actually settled &mdash; public, domestic, commercial, and judicial."},
        {"q": "What is fourfold about the formula for lying?",
         "opts": [
             "Four kinds of lie by subject matter",
             "Both directions of both faculties &mdash; not knowing, saying &ldquo;I know&rdquo;; knowing, saying &ldquo;I don&rsquo;t know&rdquo;; and the same for seeing",
             "Four venues",
             "Four motives"],
         "correct": 1,
         "expl": "So withholding is counted alongside asserting."},
        {"q": "What follows from that?",
         "opts": [
             "That only assertions count as lies",
             "That someone who conceals what they saw has lied by this definition exactly as much as someone who invents",
             "That silence is always safe",
             "That intent does not matter"],
         "correct": 1,
         "expl": "Both directions of both faculties."},
        {"q": "Which motive clause does the guide call the sharp one?",
         "opts": [
             "&ldquo;For the sake of themselves&rdquo;",
             "&ldquo;For the sake of another&rdquo;",
             "&ldquo;Or for some trivial worldly reason&rdquo; &mdash; the definition does not require the lie to be self-serving or even to matter",
             "There is no motive clause"],
         "correct": 2,
         "expl": "Most lying is not dramatic, and the discourse knows it."},
        {"q": "What is speech like flowers?",
         "opts": [
             "Beautiful or eloquent speech",
             "Answering the same four questions accurately &mdash; that is the whole definition",
             "Speech that pleases the hearer",
             "Speech about the Dhamma"],
         "correct": 1,
         "expl": "Not beautiful speech, or wise speech, or helpful speech."},
        {"q": "What does the guide say about how low that bar is?",
         "opts": [
             "That it is too low to be praised",
             "That a person who has never lied in a formal setting has speech like flowers, and nothing further is required &mdash; the middle term is the absence of a specific fault, and the discourse is content to praise it in those terms",
             "That the bar is actually very high",
             "That the term is mistranslated"],
         "correct": 1,
         "expl": "A useful correction to a common assumption about the canon's standards."},
        {"q": "How is speech like honey defined?",
         "opts": [
             "By a scene, like the first two",
             "By a practice &mdash; giving up harsh speech, and speaking in a way that is mellow, pleasing, endearing, going to the heart, polite, likable and agreeable",
             "By truthfulness alone",
             "By silence"],
         "correct": 1,
         "expl": "A different axis entirely from the first two."},
        {"q": "Is honey truer than flowers?",
         "opts": [
             "Yes, it is a further degree of truthfulness",
             "No &mdash; the first two concern accuracy and the third concerns manner; honey is kinder, and the discourse does not say whether it is also true",
             "The discourse says honey is often false",
             "The two cannot be compared"],
         "correct": 1,
         "expl": "A gap worth noticing rather than filling in."},
        {"q": "How does the canon elsewhere handle this?",
         "opts": [
             "As a single ladder",
             "As separate factors of right speech &mdash; abstaining from lying, divisive speech, harsh speech, and idle chatter &mdash; any of which a person can satisfy while failing another",
             "It does not address speech",
             "As two factors only"],
         "correct": 1,
         "expl": "Reading these three terms as one ladder produces a confusion the fourfold analysis avoids."},
        {"q": "How does the guide describe the ordering of the three images?",
         "opts": [
             "By colour",
             "By what one does with them &mdash; dung is what you get away from, flowers what you are pleased to receive, honey what you actually want: repulsion, acceptability, desire",
             "By value",
             "By rarity"],
         "correct": 1,
         "expl": "And it runs from the speaker's relation to the facts to the listener's experience."},
    ],
    marginalia=[
        ("Three kinds", [
            "<span class=\"pali\">gūthabhāṇī</span>dung",
            "<span class=\"pali\">pupphabhāṇī</span>flowers",
            "<span class=\"pali\">madhubhāṇī</span>honey",
        ]),
        ("The fourfold lie", [
            "not knowing &rarr; &ldquo;I know&rdquo;",
            "knowing &rarr; &ldquo;I don&rsquo;t know&rdquo;",
            "and the same for seeing",
            "&mdash; withholding counts",
        ]),
        ("Two axes", [
            "dung / flowers &middot; accuracy",
            "honey &middot; manner",
            "&mdash; not one ladder",
        ]),
        ("Cross-references", [
            "AN 1.140&ndash;149 &middot; reporting accurately",
            "AN 3.29 &middot; next",
            "MN 117 &middot; right speech, fourfold",
        ]),
    ],
    further=[
        '<a href="%s/an3.28/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../majjhima-nikaya/mn-117.html">MN 117 &middot; The Great Forty</a> &mdash; right '
        "speech set out as four separate abstentions, which is the analysis that keeps this "
        "discourse&rsquo;s three terms from being read as one ladder.",
        '<a href="an-1.140-149.html">AN 1.140&ndash;149 &middot; Not the Teaching</a> &mdash; the same '
        "concern with saying accurately what is and is not so, applied to the tradition rather than to "
        "a courtroom.",
    ],
)


page(
    29, "Andha", "Blind",
    vagga=VAGGA_3,
    meta_title="AN 3.29 — Blind | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Andhasutta — the "
        "blind, the one-eyed, and the two-eyed, sorted by two kinds of vision: the kind that "
        "makes money and the kind that tells right from wrong. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three individuals defined by which of two capacities they have, followed by six "
                 "verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The blind and one-eyed simile appears in the Chinese Āgamas; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a clean two-by-two, with the "
                       "fourth cell conspicuously absent"),
    ],
    why=(
        "Two kinds of vision: the kind needed to acquire and increase wealth, and the kind needed to "
        "tell skillful from unskillful, blameworthy from blameless, inferior from superior. Someone "
        "with neither is blind. Someone with the first only is one-eyed. Someone with both is "
        "two-eyed, and the discourse calls them the best individual. It is a two-by-two with one cell "
        "missing, and the missing cell is worth asking about."),
    guide=[
        ("The teaching in one sentence", [
            "Worldly competence and moral discernment are two separate eyes, and most people have at "
            "most one."]),
        ("The two visions", [
            "The first is stated in commercial terms and taken entirely seriously: the vision needed "
            "to acquire more wealth or to increase the wealth one has. That is not a grudging "
            "concession. The verses that follow praise the two-eyed person specifically for wealth "
            "<em>earned legitimately, money acquired by their own hard work</em>.",
            "The second is moral discernment: knowing the difference between qualities that are "
            "skillful and unskillful, blameworthy and blameless, inferior and superior, and those with "
            "a portion of dark or bright. Four pairs, and the last is the least familiar &mdash; the "
            "canon&rsquo;s way of naming qualities that are mixed rather than one thing or the other.",
            "So the discourse is not contrasting the worldly with the spiritual. It is naming two "
            "competences and observing that they come apart."]),
        ("The missing cell", [
            "A two-by-two of two capacities has four cells: neither, first only, second only, both. "
            "The discourse gives three. There is no name here for the person who has moral discernment "
            "and no ability to make a living.",
            "It would be reading too much in to say the discourse denies such a person exists. What can "
            "be said is that it does not name them, and that the numbering is by threes, which "
            "constrains what fits. But the absence is worth putting to a class, because the person in "
            "the missing cell is one most modern readers can picture immediately, and the discourse&rsquo;s "
            "silence about them is more interesting than any answer would have been.",
            "It is also worth noticing what the ordering assumes. The eye that is present in the "
            "one-eyed person is the commercial one, not the moral one. On the discourse&rsquo;s own "
            "arrangement, the more commonly held of the two capacities is the ability to get on in the "
            "world."]),
        ("What the one-eyed person does", [
            "The verses are much harsher than the prose, and they are worth reading for the "
            "specificity. The one-eyed person seeks wealth <em>by methods good and bad</em>; the "
            "verses name fraudulent and thieving deeds, and lies; and they add that this person is "
            "<em>skilled at piling up money, and enjoying sensual pleasures</em>. And then: from here "
            "they go to hell.",
            "The prose said only that the one-eyed person lacks moral discernment. The verses assume "
            "that lacking it, they will use their one eye badly, and describe the result. That gap "
            "between prose and verse is common in the canon and worth flagging: the prose classifies, "
            "the verse moralizes, and they are not saying quite the same thing."]),
        ("The closing advice", [
            "<em>The blind and the one-eyed, you should avoid from afar. But you should keep the "
            "two-eyed close, the best individual.</em>",
            "Read after AN 3.26 and AN 3.27, this is the third consecutive discourse ending in advice "
            "about company, and the third to sort people for that purpose on a different axis: "
            "attainment, character, and now capacity. The Puggalavagga is a chapter about types of "
            "person, and it keeps arriving at the same practical question.",
            "It is worth noting that this one, unlike AN 3.26, offers no exception for kindness. The "
            "verse says avoid from afar, and nothing qualifies it. A reader working through the "
            "chapter in order has been given the exception once and should probably carry it forward; "
            "the discourse itself does not."]),
    ],
    terms=[
        ("andha",
         "&ldquo;blind&rdquo; &mdash; here lacking both kinds of vision, worldly and moral."),
        ("ekacakkhu",
         "&ldquo;one-eyed&rdquo; &mdash; having the vision that acquires wealth and not the vision "
         "that tells skillful from unskillful."),
        ("dvicakkhu",
         "&ldquo;two-eyed&rdquo; &mdash; having both, and called by the verses the best individual."),
        ("kaṇhasukkasappaṭibhāga",
         "&ldquo;having a portion of dark or bright&rdquo; &mdash; the fourth and least familiar of "
         "the pairs the moral eye distinguishes: qualities that are mixed rather than one thing or "
         "the other."),
        ("dhammena bhogā",
         "&ldquo;wealth earned legitimately&rdquo; &mdash; what the verses praise in the two-eyed "
         "person, which is why the discourse is not contrasting the worldly with the spiritual."),
    ],
    text_intro=(
        "The discourse in full, with its six closing verses. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "The blind"),
        ("p", "&sect;1", "an3.29:1.1-1.7"),
        ("h3", "The one-eyed"),
        ("p", "&sect;2", "an3.29:2.1-2.4"),
        ("h3", "The two-eyed"),
        ("p", "&sect;3", "an3.29:3.1-3.6"),
        ("h3", "In verse"),
        ("p", "&sect;4&ndash;6", "an3.29:4.1-6.6"),
        ("p", "&sect;7&ndash;9", "an3.29:7.1-9.4"),
    ],
    quiz=[
        {"q": "What are the two kinds of vision?",
         "opts": [
             "The vision needed to acquire and increase wealth, and the vision needed to tell skillful from unskillful, blameworthy from blameless, inferior from superior",
             "Physical sight and the divine eye",
             "Insight and serenity",
             "Foresight and hindsight"],
         "correct": 0,
         "expl": "Two competences that come apart."},
        {"q": "Is the discourse contrasting the worldly with the spiritual?",
         "opts": [
             "Yes, and it condemns wealth",
             "No &mdash; the verses praise the two-eyed person specifically for wealth earned legitimately by their own hard work",
             "Yes, and it condemns discernment",
             "The discourse does not mention wealth"],
         "correct": 1,
         "expl": "The first vision is taken entirely seriously."},
        {"q": "What is <em>kaṇhasukkasappaṭibhāga</em>?",
         "opts": [
             "&ldquo;Having a portion of dark or bright&rdquo; &mdash; qualities that are mixed rather than one thing or the other",
             "&ldquo;Wholly dark&rdquo;",
             "&ldquo;Wholly bright&rdquo;",
             "&ldquo;Neither dark nor bright&rdquo;"],
         "correct": 0,
         "expl": "The least familiar of the four pairs the moral eye distinguishes."},
        {"q": "Which cell of the two-by-two is missing?",
         "opts": [
             "The person with neither capacity",
             "The person with moral discernment and no ability to make a living",
             "The person with both",
             "None is missing"],
         "correct": 1,
         "expl": "The discourse gives three of four, and the numbering by threes constrains what fits."},
        {"q": "How does the guide handle that absence?",
         "opts": [
             "By claiming the discourse denies such a person exists",
             "By saying it would be reading too much in to claim that, while noting the silence is worth putting to a class since the missing person is one modern readers picture immediately",
             "By ignoring it",
             "By supplying a fourth type"],
         "correct": 1,
         "expl": "The silence is more interesting than any answer would have been."},
        {"q": "Which eye does the one-eyed person have?",
         "opts": [
             "The moral one",
             "The commercial one &mdash; so on the discourse&rsquo;s own arrangement, the more commonly held capacity is the ability to get on in the world",
             "Neither",
             "It varies"],
         "correct": 1,
         "expl": "Worth noticing what the ordering assumes."},
        {"q": "How do the verses go beyond the prose about the one-eyed person?",
         "opts": [
             "They do not",
             "The prose says only that they lack moral discernment; the verses assume they will use their one eye badly and name fraudulent and thieving deeds and lies, ending in hell",
             "They praise them",
             "They add a fourth type"],
         "correct": 1,
         "expl": "The prose classifies, the verse moralizes, and they are not saying quite the same thing."},
        {"q": "What does the guide say about that gap generally?",
         "opts": [
             "That it indicates two authors",
             "That it is common in the canon and worth flagging",
             "That the verses are always later",
             "That the prose should be ignored"],
         "correct": 1,
         "expl": "A structural feature rather than a defect."},
        {"q": "What advice do the closing verses give?",
         "opts": [
             "Avoid the blind and the one-eyed from afar, and keep the two-eyed close",
             "Help the blind and the one-eyed",
             "Avoid everyone",
             "Keep all three close"],
         "correct": 0,
         "expl": "The third consecutive discourse in this chapter to end in advice about company."},
        {"q": "How does that advice differ from AN 3.26&rsquo;s?",
         "opts": [
             "It is identical",
             "It offers no exception for kindness &mdash; a reader working through the chapter has been given the exception once and should probably carry it forward, but this discourse does not",
             "It is gentler",
             "It concerns monastics only"],
         "correct": 1,
         "expl": "The verse says avoid from afar, and nothing qualifies it."},
    ],
    marginalia=[
        ("Two eyes", [
            "one &middot; acquiring wealth",
            "two &middot; skillful from unskillful",
        ]),
        ("Three of four", [
            "neither &middot; blind",
            "wealth only &middot; one-eyed",
            "both &middot; two-eyed",
            "&mdash; discernment only: unnamed",
        ]),
        ("Prose and verse", [
            "prose &middot; lacks the second eye",
            "verse &middot; fraud, theft, lies, hell",
        ]),
        ("Cross-references", [
            "AN 3.26 &middot; the exception this one drops",
            "AN 4.62 &middot; wealth taken seriously",
            "AN 3.30 &middot; next",
        ]),
    ],
    further=[
        '<a href="%s/an3.29/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-4.62.html">AN 4.62 &middot; Debtlessness</a> &mdash; the fullest treatment of the '
        "first eye: a householder&rsquo;s happiness in wealth legitimately earned, named without "
        "apology.",
        '<a href="an-3.26.html">AN 3.26 &middot; Associates</a> &mdash; the discourse in this chapter '
        "that adds the exception for kindness which this one&rsquo;s closing verse omits.",
    ],
)


page(
    30, "Avakujja", "Upside-down",
    vagga=VAGGA_3,
    meta_title="AN 3.30 — Upside-down | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Avakujjasutta, which "
        "closes the Puggalavagga — the upturned pot, the food spilled from a lap, and the pot "
        "set straight. Three kinds of listener, and the best discourse in the Threes for "
        "anyone who teaches. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three listeners, each defined by what they do during and after a teaching, each "
                 "with a simile; closing in verse"),
        ("Length", "~5 minutes to read"),
        ("Northern parallel", "The three-pot simile for kinds of listener is well known across the "
                              "Chinese Āgamas and became standard in later teaching literature; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; long by the standards of this "
                       "chapter, and entirely practical"),
    ],
    why=(
        "Three people go regularly to hear the teaching. The first attends to none of it, during or "
        "after &mdash; a pot turned upside down, which water runs off. The second attends while "
        "sitting there and to none of it afterward &mdash; food heaped on a lap, which scatters when "
        "the person stands. The third attends during and after &mdash; a pot set upright, which holds "
        "what is poured in. Of everything in the Threes, this is the discourse most directly about "
        "what happens in a room where something is being taught, and it is unsparing about the middle "
        "case."),
    guide=[
        ("The teaching in one sentence", [
            "What separates listeners is not what they hear but whether they are still attending to it "
            "after they stand up."]),
        ("One variable, tested twice", [
            "The three are defined by exactly one thing, asked at two moments: does this person apply "
            "the mind to the beginning, middle, and end of the discussion &mdash; while sitting there, "
            "and after getting up from their seat?",
            "No, no. Yes, no. Yes, yes. That is the whole taxonomy, and it produces three of the four "
            "possible cases; the fourth, not attending during but attending afterward, is not "
            "available in practice.",
            "Everything else in the discourse is held constant, deliberately and at length. All three "
            "<em>often go to the monastery</em>. All three hear teaching that is <em>good in the "
            "beginning, good in the middle, and good in the end, meaningful and well-phrased</em>. The "
            "repetition of that formula three times over is doing real work: no listener here is being "
            "short-changed. The teaching is identical and excellent in all three cases, so nothing "
            "about the outcome can be laid at the teacher&rsquo;s door."]),
        ("The middle case is the point", [
            "The upside-down pot and the upright pot are obvious. The lap is the discourse&rsquo;s "
            "real contribution, and it is the most uncomfortable of the three because it describes "
            "somebody who is doing everything visible correctly.",
            "The image is exact: a person with different kinds of food crammed on their lap &mdash; "
            "sesame, rice, sweets, jujube &mdash; who stands up without mindfulness, and everything "
            "scatters. The food was really there. It was collected, it was varied, and it was held "
            "while sitting. The failure is entirely in the transition.",
            "The verses press it further, and this is the sentence to take away: <em>they&rsquo;ve "
            "only grasped the phrasing, for when they get up their understanding fails, and what "
            "they&rsquo;ve learned is lost.</em> Grasping the phrasing while sitting is not nothing "
            "&mdash; the verses say this person is better than the first &mdash; but what is retained "
            "is the wording rather than the sense, and the wording does not survive standing up.",
            "For anyone who teaches, that is a description of most of an audience most of the time, "
            "and the discourse offers no technique for changing it. What it offers is the diagnosis."]),
        ("What the third person actually does", [
            "The definition of the widespread-wisdom listener is the second one plus five words: "
            "<em>and when they get up from their seat, they continue to apply the mind</em>.",
            "The verses add what that produces: they grasp the phrasing, <em>they remember it with the "
            "best of intentions</em>, and &mdash; the last line of the discourse &mdash; practicing in "
            "line with the teaching, they would make an end of suffering.",
            "So the chain runs: attend while sitting, attend after standing, grasp the phrasing, "
            "remember it, practice in line with it, end suffering. Six steps, and the first two are "
            "the only ones this discourse asks about. That is a defensible pedagogical judgment: the "
            "step that can be observed and worked on is attention, and everything downstream follows "
            "from it."]),
        ("Using it", [
            "This discourse is the most directly usable thing in the Threes for a teacher, and its use "
            "is not what one might expect. It does not suggest teaching differently, and it explicitly "
            "rules out blaming the material.",
            "What it suggests is that the question worth asking about a session is not whether people "
            "followed it but whether anything is still being turned over an hour later. AN 2.47 in the "
            "Twos gave the communal version of the same test &mdash; whether the assembly questions "
            "and examines afterward, <em>why does it say this? what does that mean?</em> Both "
            "discourses locate the decisive moment after the teaching has finished, and both are "
            "about what the listener does rather than what the teacher does.",
            "It also gives a listener something to do, which is more than most discourses about "
            "listening manage. The instruction implicit in the third case is small and precise: when "
            "you stand up, keep going."]),
        ("Closing the chapter", [
            "AN 3.30 ends the Puggalavagga, ten discourses all built on <em>these three individuals "
            "are found in the world</em>. Read in order they sort people by attainment, by treatment "
            "response, by the character of their choices, by what they enabled in you, by the "
            "hardness of their mind, by their standing relative to yours, by their character, by their "
            "speech, by their two kinds of vision, and finally by their attention.",
            "The chapter never says which sorting is the right one, and the accumulation is the point. "
            "A person is not one type; they are a position on ten different scales, and the "
            "chapter&rsquo;s repeated formula &mdash; found in the world &mdash; keeps insisting that "
            "these are observations rather than categories to be assigned."]),
    ],
    terms=[
        ("avakujjapañña",
         "&ldquo;upside-down wisdom&rdquo; &mdash; the first listener, whose simile is a pot turned "
         "over so the water runs off."),
        ("ucchaṅgapañña",
         "&ldquo;wisdom on the lap&rdquo; &mdash; the second, who holds what is given while seated "
         "and scatters it on standing."),
        ("puthupañña",
         "&ldquo;widespread wisdom&rdquo; &mdash; the third, whose simile is a pot set upright, which "
         "holds what is poured in."),
        ("ādikalyāṇa majjhekalyāṇa pariyosānakalyāṇa",
         "&ldquo;good in the beginning, middle, and end&rdquo; &mdash; the formula for the teaching, "
         "repeated identically for all three listeners so that nothing can be laid at the "
         "teacher&rsquo;s door."),
        ("byañjanam eva gaṇhāti",
         "&ldquo;they&rsquo;ve only grasped the phrasing&rdquo; &mdash; the verses&rsquo; verdict on "
         "the middle listener: the wording is retained and the sense is not."),
    ],
    text_intro=(
        "The discourse in full, with its closing verses. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Upside-down wisdom"),
        ("p", "&sect;1", "an3.30:1.1-1.14"),
        ("h3", "Wisdom on the lap"),
        ("p", "&sect;2", "an3.30:2.1-2.13"),
        ("h3", "Widespread wisdom"),
        ("p", "&sect;3", "an3.30:3.1-3.12"),
        ("h3", "In verse"),
        ("p", "&sect;4&ndash;7", "an3.30:4.1-7.6"),
        ("p", "&sect;8&ndash;10", "an3.30:8.1-10.4"),
    ],
    quiz=[
        {"q": "By what single variable are the three listeners distinguished?",
         "opts": [
             "How much they understand",
             "Whether they apply the mind to the discussion &mdash; asked twice: while sitting there, and after getting up",
             "How often they attend",
             "Which teacher they hear"],
         "correct": 1,
         "expl": "No/no, yes/no, yes/yes &mdash; three of the four possible cases."},
        {"q": "Which possible case is not available in practice?",
         "opts": [
             "Attending during and after",
             "Attending during but not after",
             "Not attending during but attending afterward",
             "Attending neither"],
         "correct": 2,
         "expl": "Which is why the taxonomy has three terms and not four."},
        {"q": "What is held constant across all three, and why does it matter?",
         "opts": [
             "That all three go often to the monastery and hear teaching good in the beginning, middle, and end &mdash; so nothing about the outcome can be laid at the teacher&rsquo;s door",
             "Their age",
             "Their ordination",
             "Nothing is held constant"],
         "correct": 0,
         "expl": "The repetition of that formula three times over is doing real work."},
        {"q": "What does the lap simile describe?",
         "opts": [
             "Someone who does not attend at all",
             "Someone doing everything visible correctly &mdash; food really collected, varied, and held while sitting &mdash; whose failure is entirely in the transition of standing up",
             "Someone who eats during a teaching",
             "Someone who forgets to attend"],
         "correct": 1,
         "expl": "The most uncomfortable of the three, and the discourse's real contribution."},
        {"q": "What do the verses say the middle listener retains?",
         "opts": [
             "Nothing",
             "Only the phrasing &mdash; when they get up their understanding fails, and what they have learned is lost",
             "The full meaning",
             "The teacher&rsquo;s name"],
         "correct": 1,
         "expl": "The wording is retained and the sense is not."},
        {"q": "How much longer is the third definition than the second?",
         "opts": [
             "Twice as long",
             "Five words &mdash; &ldquo;and when they get up from their seat, they continue to apply the mind&rdquo;",
             "A full paragraph",
             "They are the same length"],
         "correct": 1,
         "expl": "The whole difference between the second and third listener."},
        {"q": "What six-step chain do the verses give for the third listener?",
         "opts": [
             "Attend while sitting, attend after standing, grasp the phrasing, remember it, practice in line with it, end suffering",
             "Hear, memorize, recite, teach, ordain, awaken",
             "Faith, energy, mindfulness, immersion, wisdom, freedom",
             "Give, keep precepts, meditate, study, teach, retire"],
         "correct": 0,
         "expl": "And the first two are the only ones this discourse asks about."},
        {"q": "Why does the guide call that a defensible pedagogical judgment?",
         "opts": [
             "Because the later steps do not matter",
             "Because the step that can be observed and worked on is attention, and everything downstream follows from it",
             "Because the verses are optional",
             "Because listeners cannot be taught"],
         "correct": 1,
         "expl": "The discourse offers a diagnosis rather than a technique."},
        {"q": "What question does the guide say this discourse suggests asking about a session?",
         "opts": [
             "Whether people enjoyed it",
             "Whether people followed it",
             "Whether anything is still being turned over an hour later",
             "Whether the material was correct"],
         "correct": 2,
         "expl": "AN 2.47 gives the communal version of the same test."},
        {"q": "What does the Puggalavagga&rsquo;s repeated formula &ldquo;found in the world&rdquo; keep insisting?",
         "opts": [
             "That the types are fixed",
             "That these are observations rather than categories to be assigned &mdash; a person is a position on ten different scales, not one type",
             "That the types are rare",
             "That only monastics are meant"],
         "correct": 1,
         "expl": "The chapter never says which sorting is the right one, and the accumulation is the point."},
    ],
    marginalia=[
        ("Three pots", [
            "<span class=\"pali\">avakujja</span>turned over",
            "<span class=\"pali\">ucchaṅga</span>on the lap",
            "<span class=\"pali\">puthu</span>set upright",
        ]),
        ("One variable, twice", [
            "while sitting &middot; after standing",
            "no / no",
            "yes / no",
            "yes / yes",
        ]),
        ("The middle case", [
            "sesame, rice, sweets, jujube",
            "&ldquo;only grasped the phrasing&rdquo;",
            "&mdash; the failure is the transition",
        ]),
        ("Cross-references", [
            "AN 2.47 &middot; the same test, for a room",
            "AN 3.20 &middot; asking afterward",
            "AN 1.333&ndash;377 &middot; understanding without practicing",
        ]),
    ],
    further=[
        '<a href="%s/an3.30/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.42-51.html">AN 2.42&ndash;51 &middot; Assemblies</a> &mdash; AN 2.47, the '
        "communal version of this test: whether an assembly questions and examines afterward.",
        '<a href="an-3.20.html">AN 3.20 &middot; A Shopkeeper (2nd)</a> &mdash; where going to ask '
        "the learned what a passage means is named as one of three things that make a practice grow "
        "quickly.",
        '<a href="an-1.333-377.html">AN 1.333&ndash;377 &middot; Few and Many</a> &mdash; where those '
        "who understand the teaching but do not practice in line with it are counted among the many.",
    ],
)


# --------------------------------------------------------------------------- #
# AN 3.31–3.40 — Devadūtavagga
# --------------------------------------------------------------------------- #
VAGGA_4 = "<em>Devadūtavagga</em> &mdash; the fourth chapter of the Threes"

page(
    31, "Sabrahmaka", "With Divinity",
    vagga=VAGGA_4,
    meta_title="AN 3.31 — With Divinity | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sabrahmakasutta — the "
        "discourse that gives parents the three highest titles the surrounding religion had to "
        "offer, and says why. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three parallel statements about a household, three one-line glosses, a reason, "
                 "and three verses"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "The same discourse stands in the Pāli canon at Iti 106; the equation "
                              "of parents with Brahmā and with the first teachers is preserved in the "
                              "Chinese Āgamas and became a standing theme of East Asian Buddhist "
                              "writing on filial duty; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short and plain, and its central "
                       "move is easy to walk straight past"),
    ],
    why=(
        "A household where the children look after their parents is called a household living with "
        "divinity, with the first tutors, and with those worthy of offerings dedicated to the gods. "
        "Then the discourse tells you what all three phrases refer to: your parents. Each of the "
        "three was a high word in the religion the Buddha was speaking into &mdash; the highest god, "
        "the teacher who initiates you, and the recipient of sacrifice &mdash; and the discourse "
        "hands all three to two ordinary people at home. It is one of the shortest discourses in the "
        "Threes and one of the boldest."),
    guide=[
        ("The teaching in one sentence", [
            "The words the surrounding religion reserved for its god, its teachers, and its "
            "sacrifices belong to your parents, because of what they actually did for you."]),
        ("Three borrowed titles", [
            "<em>Brahmā</em> is not a general word for holiness. He is the highest god of the "
            "brahmanical world, the creator, the being whose company a brahmin&rsquo;s whole "
            "discipline aimed at reaching. Sujato renders him &ldquo;divinity&rdquo; here, which "
            "keeps the sentence readable in English; the Pāli says the god&rsquo;s name.",
            "<em>Pubbācariya</em>, &ldquo;first tutors,&rdquo; borrows the other pillar of brahmin "
            "life. The <em>ācariya</em> is the teacher who takes a boy through his sacred education; "
            "the relation was formal, lifelong, and carried real authority. The discourse says the "
            "first holder of that office in anybody&rsquo;s life was already at home.",
            "<em>Āhuneyya</em> is a sacrificial term &mdash; it describes what is fit to receive an "
            "offering, and behind it stands the fire ritual into which offerings for the gods were "
            "poured. Sujato&rsquo;s &ldquo;worthy of offerings dedicated to the gods&rdquo; keeps "
            "that background visible. The same word is used of the Saṅgha in the standard verse of "
            "recollection, which shows how high it reaches."]),
        ("What the move accomplishes", [
            "Taken one at a time these read as compliments. Taken together they are a redirection of "
            "an entire religious economy. Everything a brahmin household spent on reaching Brahmā, "
            "honoring its teachers, and feeding the sacrificial fire is pointed at two people who are "
            "already in the house.",
            "The Buddha uses this maneuver often, and the Threes will show more of it: the "
            "Brāhmaṇavagga at AN 3.51&ndash;60 takes brahmin vocabulary apart term by term. What "
            "makes AN 3.31 unusual is that the replacement is not a monastic practice or a meditative "
            "attainment. It is looking after your mother and father.",
            "It is worth noticing what the discourse does <em>not</em> do. It does not abolish the "
            "words, mock the sacrifice, or argue with anyone. It simply states where the referent "
            "actually is, three times, and moves on."]),
        ("The reason given, and how narrow it is", [
            "&ldquo;Why is that? Parents are very helpful to their children, they raise them, nurture "
            "them, and show them the world.&rdquo;",
            "The ground is not that parents are wise, or good, or owed obedience. It is historical: "
            "somebody fed you before you could feed yourself and showed you a world you had no other "
            "way of seeing. The claim is about a debt already incurred, not about the character of "
            "the person who holds it.",
            "That narrowness matters, and a teacher should say it out loud rather than let a class "
            "supply the missing sentence themselves. Readers whose parents did not raise or nurture "
            "them are not being addressed by the stated reason, because the stated reason does not "
            "apply to their case. The discourse describes what a household with living parents and a "
            "real debt owes; it does not legislate for every family, and it never says that a parent "
            "cannot be wrong.",
            "Nor does the honoring it asks for consist of agreement. The list is entirely material "
            "and entirely concrete: food and drink, clothes and bedding, anointing and bathing, "
            "washing their feet. Not one item is about obeying an instruction or holding an opinion. "
            "The canon has other places for the question of a parent who asks for something wrong; "
            "this discourse is about maintenance."]),
        ("The verses, and the one word they add", [
            "The verse restates the three titles and then supplies a reason the prose left out: "
            "parents are worthy of offerings from their children <em>for they love their "
            "offspring</em> &mdash; <em>anukampakā pajāya</em>, the word for sympathy or "
            "solicitude, the same quality the canon attributes to the Buddha&rsquo;s own teaching "
            "activity.",
            "So the prose grounds the duty in what parents did and the verse grounds it in what "
            "parents feel. The pairing is not decorative: it is the difference between a debt and a "
            "relationship, and the discourse ends up asserting both.",
            "The closing couplet gives the reward in the usual two registers &mdash; praised by the "
            "astute in this life, rejoicing in heaven after. Read alongside AN 3.10, where being "
            "praised and going to heaven are simply the two ways good conduct shows up, this is the "
            "standard formula rather than a bribe."]),
        ("Using it", [
            "In a Chinese-speaking classroom this discourse does specific work. Buddhism was attacked "
            "in China for over a millennium on the ground that it was unfilial: monastics leave home, "
            "shave their heads, and produce no descendants to maintain the ancestral offerings. The "
            "Chinese tradition answered at length &mdash; the Brahma Net Sutra states flatly that "
            "filial devotion is what is called precept &mdash; and the answer is sometimes described "
            "as a Chinese addition made under Confucian pressure.",
            "AN 3.31 is a short Pāli text saying that your parents are Brahmā, and it was there "
            "before the argument started. It does not settle the historical question of how much "
            "Chinese Buddhism accommodated, but it does show that the raw material was in the "
            "earliest layer.",
            "For a lesson, the useful exercise is the substitution itself. Ask a class what the three "
            "highest words in their own vocabulary are &mdash; the ones reserved for what is beyond "
            "ordinary life &mdash; and then read them the four glosses. The discourse works by "
            "putting a word where nobody expects to find it, and that effect survives translation."]),
    ],
    terms=[
        ("sabrahmaka",
         "&ldquo;with divinity&rdquo; &mdash; the title of the discourse, said of a household where "
         "the children honor their parents; not a household that worships Brahmā but one that has "
         "him living in it."),
        ("brahmā",
         "the highest god of the brahmanical world and the goal of brahmin practice. Rendered "
         "&ldquo;divinity&rdquo; here; the force of the discourse depends on it being a proper name."),
        ("pubbācariya",
         "&ldquo;first tutors&rdquo; &mdash; the <em>ācariya</em> was the teacher who conducted a "
         "boy&rsquo;s sacred education, a formal and lifelong relation. The discourse says the office "
         "was filled at home first."),
        ("āhuneyya",
         "&ldquo;worthy of offerings dedicated to the gods&rdquo; &mdash; a sacrificial term for what "
         "may properly receive an offering, used elsewhere of the Saṅgha in the standard recollection."),
        ("anukampaka",
         "&ldquo;sympathetic, solicitous&rdquo; &mdash; the verse&rsquo;s word for how parents stand "
         "toward their children, and the canon&rsquo;s word for why a Buddha teaches at all."),
    ],
    text_intro=(
        "The discourse in full, with its closing verses. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "Three names for two people"),
        ("p", "&sect;1", "an3.31:1.1-1.8"),
        ("h3", "In verse"),
        ("p", "&sect;2", "an3.31:2.1-2.4"),
        ("p", "&sect;3", "an3.31:3.1-3.6"),
        ("p", "&sect;4", "an3.31:4.1-4.4"),
    ],
    quiz=[
        {"q": "What is a family where the children honor their parents said to live with?",
         "opts": [
             "Divinity, the first tutors, and those worthy of offerings dedicated to the gods",
             "Wealth, health, and long life",
             "The Buddha, the Dhamma, and the Saṅgha",
             "Good friends, good neighbors, and good rulers"],
         "correct": 0,
         "expl": "Three statements, each then glossed as referring to the parents."},
        {"q": "Why does the guide insist that <em>brahmā</em> is a proper name here?",
         "opts": [
             "Because it is a general word for anything holy",
             "Because Brahmā is the highest god of the brahmanical world and the goal of brahmin practice &mdash; the force of the discourse depends on the title being his",
             "Because the Buddha claimed the name for himself",
             "Because the verse uses it in the plural"],
         "correct": 1,
         "expl": "&ldquo;Divinity&rdquo; keeps the English readable; the Pāli says the god&rsquo;s name."},
        {"q": "What kind of relationship does <em>pubbācariya</em>, &ldquo;first tutors,&rdquo; borrow from?",
         "opts": [
             "The relation between king and subject",
             "The relation between a merchant and an apprentice",
             "The <em>ācariya</em>, the teacher who conducted a boy&rsquo;s sacred education &mdash; a formal, lifelong, authoritative office",
             "The relation between a monastic preceptor and a novice only"],
         "correct": 2,
         "expl": "The discourse says the office was filled at home before anyone else held it."},
        {"q": "What is the background of the term <em>āhuneyya</em>?",
         "opts": [
             "Legal inheritance",
             "Sacrifice &mdash; it describes what may properly receive an offering, and behind it stands the fire ritual",
             "Royal tribute",
             "Almsround etiquette"],
         "correct": 1,
         "expl": "The same word is used of the Saṅgha in the standard verse of recollection, which shows how high it reaches."},
        {"q": "How does the guide describe the combined effect of the three titles?",
         "opts": [
             "As three unrelated compliments",
             "As a redirection of an entire religious economy &mdash; what a brahmin household spent on Brahmā, its teachers, and the sacrificial fire is pointed at two people already in the house",
             "As a criticism of brahmins",
             "As a promise of rebirth in the Brahmā realm"],
         "correct": 1,
         "expl": "And it is done without abolishing the words, mocking the sacrifice, or arguing with anyone."},
        {"q": "What reason does the discourse itself give?",
         "opts": [
             "That parents are wise",
             "That parents are owed obedience",
             "That parents are very helpful to their children &mdash; they raise them, nurture them, and show them the world",
             "That honoring parents produces wealth"],
         "correct": 2,
         "expl": "The ground is a debt already incurred, not the character of the person who holds it."},
        {"q": "Why does the guide call that reason narrow, and say so out loud?",
         "opts": [
             "Because it applies only to monastics",
             "Because a reader whose parents did not raise or nurture them is not addressed by the stated reason &mdash; the discourse describes a household with a real debt rather than legislating for every family",
             "Because it applies only in India",
             "Because the verse contradicts it"],
         "correct": 1,
         "expl": "And the discourse never says that a parent cannot be wrong."},
        {"q": "What does the honoring actually consist of, in the discourse&rsquo;s own list?",
         "opts": [
             "Obedience and agreement",
             "Ritual offerings at a shrine",
             "Food and drink, clothes and bedding, anointing and bathing, and washing their feet",
             "Financial inheritance"],
         "correct": 2,
         "expl": "Entirely material and entirely concrete; not one item is about holding an opinion."},
        {"q": "What does the verse add that the prose left out?",
         "opts": [
             "That parents love their offspring &mdash; <em>anukampakā pajāya</em>, the canon&rsquo;s word for why a Buddha teaches at all",
             "That parents must be obeyed",
             "That parents are reborn as gods",
             "That children inherit their parents&rsquo; deeds"],
         "correct": 0,
         "expl": "The prose grounds the duty in what parents did; the verse grounds it in what parents feel."},
        {"q": "Why is this discourse useful in a Chinese-speaking classroom?",
         "opts": [
             "Because it names a Chinese festival",
             "Because Buddhism was attacked in China for a millennium as unfilial, and this short Pāli text &mdash; saying your parents are Brahmā &mdash; was there before the argument started",
             "Because it was translated by Xuanzang",
             "Because it forbids monastic ordination"],
         "correct": 1,
         "expl": "It does not settle how much Chinese Buddhism accommodated, but it shows the raw material was in the earliest layer."},
    ],
    marginalia=[
        ("Three titles", [
            "<span class=\"pali\">brahmā</span>the highest god",
            "<span class=\"pali\">pubbācariya</span>the first teacher",
            "<span class=\"pali\">āhuneyya</span>fit for offerings",
        ]),
        ("The stated ground", [
            "they raise them",
            "they nurture them",
            "they show them the world",
            "&mdash; a debt, not a character reference",
        ]),
        ("What honoring is", [
            "food and drink",
            "clothes and bedding",
            "anointing and bathing",
            "washing their feet",
        ]),
        ("Cross-references", [
            "Iti 106 &middot; the same discourse",
            "DN 31 &middot; the duties in five pairs",
            "AN 3.10 &middot; praise here, heaven after",
        ]),
    ],
    further=[
        '<a href="%s/an3.31/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../itivuttaka/iti-106.html">Iti 106 &middot; With Divinity</a> &mdash; the same '
        "discourse, preserved a second time in a different collection. Worth reading beside this one "
        "for what an early text looks like when the tradition thought it important enough to keep "
        "twice.",
        '<a href="../digha-nikaya/dn-31.html">DN 31 &middot; Advice to Sigālaka</a> &mdash; the '
        "long lay-life discourse, where the same duty is set out in working detail: five things "
        "children do for parents and five things parents do for children, inside a scheme covering "
        "every relationship a householder has.",
        '<a href="/sutras/brahma-net-sutra/chapter-07/">Brahma Net Sutra &middot; the precept '
        "preface</a> &mdash; where the Chinese tradition states its position in one line, 孝名為戒, "
        "filial devotion is what is called precept. Read after AN 3.31 it shows a later tradition "
        "pushing a claim that the Pāli text had already made.",
        '<a href="an-3.10.html">AN 3.10 &middot; Stains</a> &mdash; for the closing couplet&rsquo;s '
        "two registers of reward, praise in this life and heaven after, in their usual setting.",
    ],
)


page(
    32, "Ānanda", "With Ānanda",
    vagga=VAGGA_4,
    meta_title="AN 3.32 — With Ānanda | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ānandasutta — whether "
        "there is a state of immersion with no I-making, mine-making, or conceit, and the "
        "one-sentence answer, sealed with a verse from the Pārāyana. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; Ānanda approaches the Buddha, bows, and asks"),
        ("Speakers", "Venerable Ānanda and the Buddha"),
        ("Form", "A question, a yes, a second question, a one-sentence method, and a quoted verse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Material on immersion free of I-making and mine-making is preserved in "
                              "the Chinese Saṃyukta-āgama (T99); this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; three technical terms, one long "
                       "sentence repeated four times, and an answer far shorter than the question"),
    ],
    why=(
        "Ānanda asks whether a mendicant can reach a state of immersion in which there is no "
        "I-making, no mine-making, and no underlying tendency to conceit &mdash; not toward this "
        "body, and not toward anything outside it. The Buddha says yes, in the same words. Ānanda "
        "asks how. And the answer is one sentence long: they think, <em>this is peaceful, this is "
        "sublime</em>. The gap between the size of the question and the size of the answer is the "
        "whole interest of the discourse."),
    guide=[
        ("The teaching in one sentence", [
            "The immersion in which self-reference has stopped is reached by giving the mind the one "
            "object that has nothing in it to make a self out of."]),
        ("The three things being asked about", [
            "<em>Ahaṅkāra</em>, I-making, and <em>mamiṅkāra</em>, mine-making, are not nouns for "
            "beliefs. They are verbs made into nouns: the mind&rsquo;s ongoing activity of producing "
            "an <em>I</em> and producing a <em>mine</em>. A person can hold no philosophical view of "
            "a self and go on doing both all day.",
            "<em>Mānānusaya</em> is the underlying tendency to conceit &mdash; not conceit as an "
            "episode of arrogance but conceit as a disposition, the reflex of measuring: better than, "
            "equal to, worse than. The canon treats it as the last fetter to go, which is why it "
            "appears here in a question about the highest attainment rather than in a discourse about "
            "manners.",
            "The three are asked about in two directions. <em>For this conscious body</em> covers "
            "everything on the inside; <em>externally for all signs</em> covers everything else, "
            "<em>nimitta</em> being the aspect of a thing the mind takes hold of. Between them "
            "nothing is left over. That is why the sentence is so long, and why it is repeated "
            "without abbreviation each time."]),
        ("Why Ānanda asks in that form", [
            "The question is not &ldquo;is there such a thing?&rdquo; but &ldquo;could it be that a "
            "mendicant might gain a state of immersion such that&hellip;?&rdquo; He is asking whether "
            "a describable, attainable state has this property.",
            "That is characteristic of him. Ānanda&rsquo;s questions in the canon tend to be about "
            "the reachable middle of the path rather than its terminus, and they are usually framed "
            "so that a yes commits the Buddha to something specific. Here a yes commits him to saying "
            "that the end of self-making is not merely a description of an arahant after the fact but "
            "a state that can be entered."]),
        ("The answer, and why it is so short", [
            "&ldquo;It&rsquo;s when a mendicant thinks: <em>this is peaceful; this is sublime &mdash; "
            "that is, the stilling of all activities, the letting go of all attachments, the ending "
            "of craving, fading away, cessation, extinguishment.</em>&rdquo;",
            "The formula is a stock one and it names extinguishment, <em>nibbāna</em>, by six "
            "descriptions in a row. What the discourse asks the practitioner to do with it is simply "
            "to hold it as what the mind is attending to.",
            "The logic is worth spelling out, because a class will otherwise hear a non-answer. "
            "I-making needs material: some experience with enough content in it to be claimed. Every "
            "object inside the conscious body and every external sign supplies that material. The one "
            "object that does not is the stilling of the whole business. Attending to it, there is "
            "nothing there to make an <em>I</em> out of, nothing to make a <em>mine</em> out of, and "
            "nothing to measure against.",
            "So the answer is not a technique of suppression. It is a change of object, and the "
            "absence of self-making follows from what the object is. AN 3.33, the next discourse, "
            "gives the identical formula to Sāriputta as something to train in, which is how a state "
            "described here becomes an instruction there."]),
        ("The quoted verse", [
            "The Buddha closes by identifying his own earlier words: this is what he meant in the "
            "Pārāyana, in the Questions of Puṇṇaka. The verse is on this site at Snp 5.4, and it "
            "answers a brahmin who had asked about sacrifice.",
            "<em>Having appraised the world high and low, there is nothing in the world that disturbs "
            "them. Peaceful, unclouded, untroubled, with no need for hope &mdash; they&rsquo;ve "
            "crossed over rebirth and old age, I declare.</em>",
            "Two things are happening. The first is a claim about continuity: the prose analysis and "
            "the old verse are the same teaching, and the Buddha says so himself. The second is a "
            "shift of register. Everything the prose states in technical negatives &mdash; no "
            "I-making, no mine-making, no conceit &mdash; the verse states as a condition: nothing "
            "disturbs them, they have no need for hope. <em>Nirāsa</em>, hopeless in that sense, is a "
            "compliment here, which is the kind of reversal worth flagging to a class before they "
            "meet it."]),
        ("Using it", [
            "This is a short text with a high ceiling, and it is easy to teach badly by pretending "
            "the answer is simpler than it is. The honest presentation gives the class both halves: "
            "an enormous question and a one-line reply, and then the work of seeing why the reply is "
            "not evasive.",
            "The transferable part is the general principle that what the mind does depends on what "
            "it is holding. That is not a claim anyone needs to be Buddhist to test, and it is the "
            "load-bearing move of the discourse."]),
    ],
    terms=[
        ("ahaṅkāra",
         "&ldquo;I-making&rdquo; &mdash; not the belief in a self but the activity of producing an "
         "<em>I</em>, which continues in people who hold no such belief."),
        ("mamiṅkāra",
         "&ldquo;mine-making&rdquo; &mdash; its partner, the activity of producing a <em>mine</em>. "
         "The pair is standard in the canon and always occurs together."),
        ("mānānusaya",
         "&ldquo;the underlying tendency to conceit&rdquo; &mdash; conceit as a disposition rather "
         "than an episode: the reflex of measuring oneself as better, equal, or worse. Held to be the "
         "last fetter abandoned."),
        ("nimitta",
         "&ldquo;sign&rdquo; &mdash; the aspect of a thing that the mind takes hold of. "
         "&ldquo;Externally for all signs&rdquo; is how the discourse covers everything outside the "
         "body without listing it."),
        ("cetovimutti paññāvimutti",
         "&ldquo;freedom of heart and freedom by wisdom&rdquo; &mdash; the two-sided formula for "
         "liberation, one term for the mind released and one for the release being a matter of "
         "understanding."),
    ],
    text_intro=(
        "The discourse in full, with the verse from the Pārāyana that closes it. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Ānanda&rsquo;s question"),
        ("p", "&sect;1", "an3.32:1.1"),
        ("p", "&sect;2", "an3.32:2.1-2.4"),
        ("h3", "But how?"),
        ("p", "&sect;3", "an3.32:3.1-3.2"),
        ("p", "&sect;4", "an3.32:4.1-4.4"),
        ("h3", "The verse he is quoting"),
        ("p", "&sect;5", "an3.32:5.1"),
        ("p", "&sect;6", "an3.32:6.1-6.4"),
    ],
    quiz=[
        {"q": "What does Ānanda ask?",
         "opts": [
             "Whether an arahant still has a body",
             "Whether a mendicant might gain a state of immersion with no I-making, mine-making, or underlying tendency to conceit &mdash; internally or externally",
             "How many jhānas there are",
             "Whether laypeople can be liberated"],
         "correct": 1,
         "expl": "He asks whether a describable, attainable state has this property."},
        {"q": "What are I-making and mine-making, according to the guide?",
         "opts": [
             "Philosophical beliefs about a self",
             "Two names for craving",
             "Activities of the mind &mdash; the ongoing production of an <em>I</em> and a <em>mine</em>, which continue in people who hold no view of a self",
             "Types of speech"],
         "correct": 2,
         "expl": "Verbs made into nouns, not nouns for beliefs."},
        {"q": "How does the guide distinguish <em>mānānusaya</em> from ordinary arrogance?",
         "opts": [
             "It is conceit as a disposition &mdash; the reflex of measuring better, equal, or worse &mdash; and it is held to be the last fetter abandoned",
             "It is arrogance in speech only",
             "It applies only to monastics",
             "There is no difference"],
         "correct": 0,
         "expl": "Which is why it appears in a question about the highest attainment rather than one about manners."},
        {"q": "What is covered by &ldquo;externally for all signs&rdquo;?",
         "opts": [
             "Other people only",
             "Visible objects only",
             "Everything outside the conscious body &mdash; <em>nimitta</em> being the aspect of a thing the mind takes hold of",
             "Meditation objects only"],
         "correct": 2,
         "expl": "Between inside and outside, nothing is left over &mdash; which is why the sentence is so long."},
        {"q": "What is the Buddha&rsquo;s answer to &ldquo;how?&rdquo;",
         "opts": [
             "A course of four jhānas",
             "A single contemplation: <em>this is peaceful; this is sublime</em> &mdash; the stilling of all activities, the ending of craving, extinguishment",
             "Study of the discourses",
             "Observance of the precepts"],
         "correct": 1,
         "expl": "One sentence, in answer to a question four lines long."},
        {"q": "Why does the guide say the answer is not evasive?",
         "opts": [
             "Because it is repeated three times",
             "Because I-making needs material, and the one object that supplies none is the stilling of the whole business &mdash; so the absence of self-making follows from what the object is",
             "Because Ānanda accepts it",
             "Because it is in verse"],
         "correct": 1,
         "expl": "It is a change of object rather than a technique of suppression."},
        {"q": "How does AN 3.33 relate to this discourse?",
         "opts": [
             "It contradicts it",
             "It gives the identical formula to Sāriputta as something to train in &mdash; a state described here becomes an instruction there",
             "It is about a different subject entirely",
             "It repeats it word for word with no change"],
         "correct": 1,
         "expl": "The two discourses are a matched pair and are best read together."},
        {"q": "Which text does the Buddha quote at the end?",
         "opts": [
             "The Dhammapada",
             "The Pārāyana, in the Questions of Puṇṇaka &mdash; on this site at Snp 5.4",
             "The Vinaya",
             "The Questions of Udaya"],
         "correct": 1,
         "expl": "The Questions of Udaya is quoted in the next discourse, AN 3.33."},
        {"q": "What does the guide say is happening in the quotation?",
         "opts": [
             "Only a change of style",
             "A claim about continuity &mdash; that the prose analysis and the old verse are the same teaching &mdash; and a shift of register from technical negatives to a description of a condition",
             "A correction of the earlier verse",
             "An appeal to another teacher&rsquo;s authority"],
         "correct": 1,
         "expl": "And the Buddha makes the continuity claim himself."},
        {"q": "Why does the guide flag the phrase &ldquo;with no need for hope&rdquo;?",
         "opts": [
             "Because it is a mistranslation",
             "Because being without hope is a compliment here &mdash; a reversal worth warning a class about before they meet it",
             "Because it refers to despair",
             "Because it is addressed to laypeople"],
         "correct": 1,
         "expl": "<em>Nirāsa</em> names the state of someone with nothing outstanding, not someone defeated."},
    ],
    marginalia=[
        ("Three things absent", [
            "<span class=\"pali\">ahaṅkāra</span>I-making",
            "<span class=\"pali\">mamiṅkāra</span>mine-making",
            "<span class=\"pali\">mānānusaya</span>conceit, underlying",
        ]),
        ("Two directions", [
            "this conscious body",
            "externally, all signs",
            "&mdash; nothing left over",
        ]),
        ("The whole method", [
            "&ldquo;this is peaceful&rdquo;",
            "&ldquo;this is sublime&rdquo;",
            "&mdash; a change of object",
        ]),
        ("Cross-references", [
            "Snp 5.4 &middot; the verse quoted",
            "AN 3.33 &middot; the same, as training",
            "MN 109 &middot; the formula at length",
        ]),
    ],
    further=[
        '<a href="%s/an3.32/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../sutta-nipata/snp-5.4.html">Snp 5.4 &middot; The Questions of Puṇṇaka</a> '
        "&mdash; the verse the Buddha quotes, in its own setting: an answer to a brahmin who came "
        "asking about sacrifice. Reading the two together shows what the Buddha meant by saying the "
        "prose and the verse are the same teaching.",
        '<a href="an-3.33.html">AN 3.33 &middot; With Sāriputta</a> &mdash; the matched discourse, '
        "where the same sentence is handed over as a training rather than described as a state.",
        '<a href="../majjhima-nikaya/mn-109.html">MN 109 &middot; The Longer Discourse on the '
        "Full-Moon Night</a> &mdash; where the I-making and mine-making formula is worked through at "
        "length against the five aggregates, which is the analysis AN 3.32 compresses into a phrase.",
        '<a href="../majjhima-nikaya/mn-064.html">MN 64 &middot; The Longer Discourse with '
        "Māluṅkya</a> &mdash; for the same &ldquo;this is peaceful, this is sublime&rdquo; formula "
        "used as the turning point out of the meditative attainments.",
    ],
)


page(
    33, "Sāriputta", "With Sāriputta",
    vagga=VAGGA_4,
    meta_title="AN 3.33 — With Sāriputta | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sāriputtasutta — the "
        "Buddha says it is hard to find anyone who understands, Sāriputta says now is the time, "
        "and the training that follows is the same sentence given to Ānanda. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "None stated; Sāriputta approaches the Buddha, bows, and is spoken to first"),
        ("Speakers", "The Buddha and Venerable Sāriputta"),
        ("Form", "An opening remark, a request, a training instruction, a title conferred, and a "
                 "quoted verse"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Comparable material on training free of I-making and mine-making is "
                              "preserved in the Chinese Āgamas; this reading guide does not assert a "
                              "specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the same technical sentence as AN "
                       "3.32, plus a dense verse on the hindrances"),
    ],
    why=(
        "The Buddha opens by saying he might teach in brief, or in detail, or both &mdash; but that "
        "it is hard to find anyone who understands. Sāriputta answers, <em>now is the time,</em> and "
        "guarantees an audience. What follows is the sentence AN 3.32 gave to Ānanda as a description "
        "of a state, handed over here as something to train in. The pair are best read one after the "
        "other, and the difference between them is the difference between knowing that something is "
        "possible and being told to do it."),
    guide=[
        ("The teaching in one sentence", [
            "Train so that there is no I-making, mine-making, or conceit toward anything inside or "
            "outside &mdash; and that training is what the canon calls having made an end of "
            "suffering."]),
        ("The opening complaint", [
            "&ldquo;Maybe I&rsquo;ll teach Dhamma in brief, maybe in detail, maybe both in brief and "
            "in detail. But it&rsquo;s hard to find anyone who understands.&rdquo;",
            "This is not a rebuke of Sāriputta, who is standing right there and is about to be given "
            "the teaching. It is a statement about the general case, and it puts a condition on "
            "teaching: the form a teaching takes depends on who can receive it. The canon returns to "
            "this repeatedly, most famously in the hesitation after the awakening.",
            "Sāriputta&rsquo;s reply is the second half of the exchange and the reason it was "
            "preserved: <em>now is the time, Blessed One! There will be those who understand the "
            "teaching!</em> Somebody has to make that claim before a teaching happens, and here it is "
            "not the teacher who makes it."]),
        ("The same sentence, in a new mood", [
            "What the Buddha then says is word for word the formula of AN 3.32, with one change: it "
            "is put in the first person plural and prefaced by <em>you should train like this</em>. "
            "Ānanda asked whether such a state exists and was told how it is reached; Sāriputta is "
            "told to train for it.",
            "That difference is not trivial and it is worth making a class notice it, because the two "
            "discourses stand next to each other in the collection deliberately. A description "
            "answers a question. A training is an instruction with a second person in it. The "
            "compilers put the answer first and the instruction second.",
            "The content is unchanged: no I-making, mine-making, or underlying tendency to conceit "
            "for this conscious body, none externally for all signs, and living in the freedom of "
            "heart and freedom by wisdom where those three are no more. See the key terms on AN 3.32 "
            "for the vocabulary."]),
        ("The title conferred", [
            "Then comes something AN 3.32 does not have: a name for the person who has done it. Such "
            "a mendicant <em>has cut off craving, cast off the fetters, and by rightly comprehending "
            "conceit has made an end of suffering</em>.",
            "The three clauses are a compressed description of arahantship, and the third is the one "
            "to slow down on. It does not say that conceit is suppressed or that the person no longer "
            "feels superior to anyone. It says conceit is <em>rightly comprehended</em>, "
            "<em>sammā mānābhisamayā</em> &mdash; understood in a way that ends it. The canon "
            "consistently treats conceit as something that dissolves under accurate seeing rather "
            "than something defeated by effort, and this phrase is where the Threes say so."]),
        ("The verse from the Questions of Udaya", [
            "The closing quotation is from the Pārāyana again, this time the Questions of Udaya, on "
            "this site at Snp 5.14. It is denser than the Puṇṇaka verse and repays a slow read.",
            "<em>The giving up of both sensual desires and displeasures, the casting aside of "
            "dullness, and the prevention of remorse; pure equanimity and mindfulness, preceded by "
            "investigation of principles &mdash; this, I declare, is liberation by enlightenment, the "
            "smashing of ignorance.</em>",
            "The first half is the five hindrances, in order and by name: sensual desire, ill will "
            "(&ldquo;displeasures&rdquo;), dullness and drowsiness, restlessness and remorse, and "
            "&mdash; by way of the investigation of principles &mdash; doubt. The second half is the "
            "fourth jhāna, whose standard formula is exactly <em>purity of mindfulness and "
            "equanimity</em>. So the verse walks from the hindrances abandoned to the fourth jhāna "
            "and calls the result liberation by enlightenment.",
            "That is a strong claim about meditation, and it is the reason this verse gets quoted. It "
            "does not say that the fourth jhāna is liberation. It says that this sequence &mdash; "
            "hindrances gone, investigation leading, equanimity and mindfulness pure &mdash; is what "
            "<em>aññāvimokkha</em>, liberation by enlightenment, names. The Chinese meditation "
            "manuals build their whole preliminary section on the same order of operations."]),
        ("Using it", [
            "Read AN 3.32 and AN 3.33 in one sitting. They are short, they share a sentence, and the "
            "pair demonstrates something a single discourse cannot: that the canon distinguishes "
            "carefully between telling you a state exists, telling you how it is entered, and telling "
            "you to train for it.",
            "For a class the usable handle is Sāriputta&rsquo;s line. Somebody in the room has to say "
            "<em>there will be those who understand</em>, and the discourse records a teaching that "
            "happened because a student said it rather than because the teacher assumed it."]),
    ],
    terms=[
        ("saṅkhittena vitthārena",
         "&ldquo;in brief, in detail&rdquo; &mdash; the two modes of teaching the Buddha offers, plus "
         "both together. The canon treats the choice between them as depending on the listener."),
        ("kālo bhagavā",
         "&ldquo;now is the time, Blessed One&rdquo; &mdash; the formula by which a request for "
         "teaching is made. In this discourse the student supplies both the request and the "
         "assurance that there is an audience."),
        ("sammā mānābhisamayā",
         "&ldquo;by rightly comprehending conceit&rdquo; &mdash; the phrase for how conceit ends: "
         "understood accurately rather than suppressed."),
        ("upekkhāsatipārisuddhi",
         "&ldquo;purity of equanimity and mindfulness&rdquo; &mdash; the standing formula for the "
         "fourth jhāna, which is what the quoted verse arrives at."),
        ("aññāvimokkha",
         "&ldquo;liberation by enlightenment&rdquo; &mdash; what the verse calls the result of that "
         "sequence, glossed in the same line as the smashing of ignorance."),
    ],
    text_intro=(
        "The discourse in full, with the verse from the Questions of Udaya. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Hard to find anyone who understands"),
        ("p", "&sect;1", "an3.33:1.1-1.8"),
        ("h3", "The training"),
        ("p", "&sect;2", "an3.33:2.1-2.3"),
        ("p", "&sect;3", "an3.33:3.1-3.4"),
        ("h3", "The verse he is quoting"),
        ("p", "&sect;4", "an3.33:4.1-4.4"),
        ("p", "&sect;5", "an3.33:5.1-5.4"),
    ],
    quiz=[
        {"q": "How does the discourse open?",
         "opts": [
             "Sāriputta asks a question",
             "The Buddha says he might teach in brief, in detail, or both &mdash; but that it is hard to find anyone who understands",
             "The Buddha rebukes Sāriputta",
             "A layperson asks for teaching"],
         "correct": 1,
         "expl": "A statement about the general case, not about the monk standing in front of him."},
        {"q": "What does Sāriputta contribute?",
         "opts": [
             "An answer of his own",
             "A summary of the teaching",
             "The request and the assurance &mdash; &ldquo;now is the time&hellip; there will be those who understand the teaching!&rdquo;",
             "A question about rebirth"],
         "correct": 2,
         "expl": "Somebody has to say it, and here it is not the teacher."},
        {"q": "What is the relationship between this discourse and AN 3.32?",
         "opts": [
             "They share the same formula, given there as a description of a state and here as a training",
             "They contradict each other",
             "This one is longer and more detailed",
             "They share only a speaker"],
         "correct": 0,
         "expl": "The compilers put the answer first and the instruction second."},
        {"q": "What does the guide say distinguishes a description from a training?",
         "opts": [
             "Length",
             "A description answers a question; a training is an instruction with a second person in it",
             "Whether it is in verse",
             "Whether it names an audience"],
         "correct": 1,
         "expl": "The two discourses stand next to each other in the collection deliberately."},
        {"q": "What is the mendicant who has done this called?",
         "opts": [
             "A stream-enterer",
             "A teacher of the Dhamma",
             "One who has cut off craving, cast off the fetters, and by rightly comprehending conceit has made an end of suffering",
             "One who has entered the fourth jhāna"],
         "correct": 2,
         "expl": "A compressed description of arahantship, and something AN 3.32 does not contain."},
        {"q": "Why does the guide slow down on <em>sammā mānābhisamayā</em>?",
         "opts": [
             "Because it is a rare word",
             "Because it says conceit is rightly comprehended &mdash; understood in a way that ends it, rather than suppressed or defeated by effort",
             "Because it refers to a monastic rule",
             "Because Sāriputta questions it"],
         "correct": 1,
         "expl": "The canon consistently treats conceit as dissolving under accurate seeing."},
        {"q": "Which verse does the Buddha quote here?",
         "opts": [
             "The Questions of Puṇṇaka",
             "The Questions of Udaya, from the Pārāyana &mdash; on this site at Snp 5.14",
             "A verse of the Dhammapada",
             "His own first sermon"],
         "correct": 1,
         "expl": "The Questions of Puṇṇaka is quoted in the previous discourse, AN 3.32."},
        {"q": "What does the first half of that verse enumerate?",
         "opts": [
             "The three characteristics",
             "The four noble truths",
             "The five hindrances &mdash; sensual desire, ill will, dullness, restlessness and remorse, and doubt by way of the investigation of principles",
             "The five aggregates"],
         "correct": 2,
         "expl": "In order and by name, though not under the collective label."},
        {"q": "What does its second half describe?",
         "opts": [
             "The first jhāna",
             "The fourth jhāna, whose standard formula is exactly purity of mindfulness and equanimity",
             "The formless attainments",
             "Stream-entry"],
         "correct": 1,
         "expl": "The verse walks from the hindrances abandoned to the fourth jhāna."},
        {"q": "What does the verse claim about that sequence?",
         "opts": [
             "That the fourth jhāna simply is liberation",
             "That it is preliminary and unimportant",
             "That this sequence is what <em>aññāvimokkha</em>, liberation by enlightenment, names &mdash; glossed in the same line as the smashing of ignorance",
             "That it applies only to Sāriputta"],
         "correct": 2,
         "expl": "A strong claim about meditation, and the reason this verse gets quoted."},
    ],
    marginalia=[
        ("The pair", [
            "AN 3.32 &middot; a state described",
            "AN 3.33 &middot; a training given",
            "&mdash; one sentence, two moods",
        ]),
        ("Three clauses", [
            "cut off craving",
            "cast off the fetters",
            "rightly comprehended conceit",
        ]),
        ("The Udaya verse", [
            "hindrances abandoned",
            "investigation leading",
            "equanimity and mindfulness pure",
            "&mdash; liberation by enlightenment",
        ]),
        ("Cross-references", [
            "Snp 5.14 &middot; the verse quoted",
            "AN 3.32 &middot; the matched discourse",
            "AN 3.63 &middot; the jhāna formula in full",
        ]),
    ],
    further=[
        '<a href="%s/an3.33/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../sutta-nipata/snp-5.14.html">Snp 5.14 &middot; The Questions of Udaya</a> '
        "&mdash; the verse quoted here, in the exchange it belongs to. Udaya asks about the "
        "breaking of ignorance and gets this in reply, which is why the Buddha can cite it as a "
        "summary of the training just given.",
        '<a href="an-3.32.html">AN 3.32 &middot; With Ānanda</a> &mdash; the other half of the pair, '
        "with the key terms for the shared formula set out in full.",
        '<a href="/sutras/shi-chan-boluomi/fascicle-002/">Shi Chan Boluomi &middot; Fascicle 2</a> '
        "&mdash; Zhiyi&rsquo;s preliminary expedients, built on the same order of operations the "
        "Udaya verse assumes: the five hindrances abandoned before the mind is gathered. Useful for "
        "seeing a Chinese manual work out in detail what a Pāli verse states in four lines.",
    ],
)


page(
    34, "Nidāna", "Sources",
    vagga=VAGGA_4,
    meta_title="AN 3.34 — Sources | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Nidānasutta — greed, "
        "hate, and delusion as the sources of deeds, the seed sown in a good field and the seed "
        "burned to ash, and a closing verse that drops the prose's timings. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "A triad and its simile, a second triad and its simile, and two closing verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The three unwholesome roots are preserved throughout the Chinese "
                              "Āgamas and the triad became standard Abhidharma vocabulary as 貪瞋癡; "
                              "this reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; heavily repetitive by design, "
                       "with one sentence that has puzzled readers for a long time"),
    ],
    why=(
        "Three things give rise to deeds: greed, hate, and delusion. A deed born of them ripens "
        "wherever the doer is reborn, and its result is experienced in this life, the next, or some "
        "later one &mdash; like sound seed sown in a prepared field with rain falling. Then the "
        "discourse names a second three, contentment, love, and understanding, and the simile "
        "changes completely: the seeds are burned, the ashes scattered in the wind or floated down a "
        "river. The second half is not about good deeds being rewarded. It is about deeds coming to "
        "an end."),
    guide=[
        ("The teaching in one sentence", [
            "Deeds rooted in greed, hate, and delusion keep producing results wherever you go next; "
            "deeds rooted in their opposites are what brings the whole production to a stop."]),
        ("The word <em>nidāna</em>, and why the title matters", [
            "<em>Nidāna</em> is source, origin, or ground &mdash; the same word that titles the "
            "great chapter on dependent origination in the Saṁyutta. The discourse is not asking "
            "which deeds are bad. It is asking what deeds come out of.",
            "The answer is a triad that will be doing structural work for the rest of the "
            "collection: <em>lobha</em>, greed; <em>dosa</em>, hate; <em>moha</em>, delusion. East "
            "Asian Buddhism inherited it as 貪瞋癡, the three poisons, and built a whole moral "
            "psychology on top of it. This is one of the plainest early statements of what the triad "
            "is for.",
            "Notice that the roots are not deeds. Greed is not stealing and hate is not violence; "
            "they are what stealing and violence come out of. That distinction is the entire content "
            "of the word <em>nidāna</em>, and it is why the discourse can then say something about "
            "all deeds at once."]),
        ("Two clauses about where and when", [
            "Each root gets the same sentence: a deed born, sourced, and originated from it "
            "<em>ripens where that new incarnation is born</em>, and wherever it ripens, its result "
            "is experienced <em>either in the present life, or in the next life, or in some "
            "subsequent period</em>.",
            "Two separate claims are packed in there. The first is about place: the deed matures "
            "wherever the doer turns up, not in some ledger held elsewhere. The second is about time, "
            "and it gives three options rather than one.",
            "This is where a Western class usually stops, and the honest thing is to stop with them. "
            "The discourse assumes rebirth. It is not using &ldquo;next life&rdquo; as a metaphor for "
            "tomorrow, and reading it that way makes the sentence say nothing at all. Anyone who does "
            "not accept rebirth is entitled to say so, and should be told that the text is not on "
            "their side of the question.",
            "What survives that disagreement is still substantial: that acts have sources, that the "
            "source determines what the act produces, and that results are not on a schedule the doer "
            "controls. The three timings are stated precisely so that no one can read a delay as an "
            "acquittal &mdash; which is the same point AN 3.100 makes with its lump of salt."]),
        ("The two similes, and how differently they behave", [
            "The first simile is agricultural and entirely positive in mechanism: seeds intact, "
            "unspoiled, undamaged by weather, fertile, well kept; sown in a well-prepared productive "
            "field; the heavens providing plenty of rain. Then they grow, increase, and mature. "
            "Everything is working. That is the point &mdash; deeds rooted in the three roots are not "
            "defective machinery. They function.",
            "The second simile takes the identical seeds and destroys them: burned with fire, reduced "
            "to ashes, and the ashes whisked away in a strong wind or floated down a swift stream. "
            "Not stored, not neutralized, not offset. Ended, and then the remains dispersed so "
            "thoroughly that the image forecloses recovery.",
            "The asymmetry is the discourse&rsquo;s real argument. A reader coming in expects a "
            "symmetrical ledger: bad deeds produce bad fruit, good deeds produce good fruit. The "
            "second half does not say that. It says that deeds rooted in non-greed, non-hate, and "
            "non-delusion are <em>cut off at the root, made like a palm stump, obliterated, and "
            "unable to arise in the future.</em> The subject has changed from what kamma produces to "
            "how kamma stops."]),
        ("The sentence that has puzzled readers", [
            "In the second half each root gets this form: a deed that emerges from contentment "
            "&ldquo;is given up when greed is done away with,&rdquo; a deed from love is abandoned "
            "when hate is done away with, a deed from understanding when delusion is done away with.",
            "Read plainly that is odd. It seems to say that wholesome-rooted deeds are abandoned when "
            "the corresponding <em>unwholesome</em> root goes &mdash; and it is the wholesome deed, "
            "not the unwholesome one, that is described as cut off like a palm stump. Translators and "
            "commentators have not read this uniformly, and this guide is not going to pretend the "
            "question is settled.",
            "Two readings are worth having in mind. On one, the sentence is about the person in whom "
            "greed is gone: their good deeds no longer function as kamma-producing deeds at all, "
            "because there is nothing left to carry them forward &mdash; which is what the canon "
            "elsewhere says of an arahant&rsquo;s actions. On the other, the passage is describing "
            "the whole apparatus of deed-and-result winding down, wholesome deeds included, since "
            "the goal is not an improved balance but no balance.",
            "Both readings land in the same place, which is why the disagreement is tolerable: the "
            "second half of this discourse is not about accumulating merit. If a class comes away "
            "thinking that non-greed, non-hate, and non-delusion are how you earn a better rebirth, "
            "they have read the first half twice and the second half not at all."]),
        ("The verses, and what they leave out", [
            "The closing verses say that when an ignorant person acts out of greed, hate, or "
            "delusion, any deeds they have done, a little or a lot, <em>are to be experienced right "
            "here, not in any other place</em>.",
            "That is not what the prose said. The prose was careful to give three timings &mdash; "
            "this life, the next, or some subsequent period &mdash; and the verse compresses them "
            "into one. It is the same thing the verses do at AN 3.26 and AN 3.27, where a "
            "qualification stated carefully in prose disappears when the material is put into meter.",
            "The right response is not to accuse the verse of error. Verse in this collection works "
            "by force rather than precision, and <em>right here, not in any other place</em> is doing "
            "rhetorical work: there is no elsewhere to send the consequences to. But a reader who "
            "takes the verse as the discourse&rsquo;s doctrine of kamma will have a narrower position "
            "than the prose eight paragraphs earlier, and a teacher should point at the seam rather "
            "than smooth it over.",
            "The final verse gives the practical upshot, and it is not a warning: a wise mendicant "
            "who <em>arouses knowledge of the outcome</em> of greed, hate, and delusion abandons all "
            "bad destinies. What ends the trouble is understanding where deeds come from &mdash; "
            "which is the discourse&rsquo;s title."]),
    ],
    terms=[
        ("nidāna",
         "&ldquo;source, ground, origin&rdquo; &mdash; the title word, and the same term that names "
         "the great chapter on dependent origination. The question is not which deeds are bad but "
         "what deeds come out of."),
        ("lobha dosa moha",
         "&ldquo;greed, hate, delusion&rdquo; &mdash; the three unwholesome roots, inherited by East "
         "Asian Buddhism as 貪瞋癡, the three poisons. They are not deeds but what deeds arise from."),
        ("alobha adosa amoha",
         "&ldquo;contentment, love, understanding&rdquo; &mdash; the three wholesome roots, each "
         "formed in Pāli as the simple negation of its opposite, which is why the English renderings "
         "vary so much."),
        ("ucchinnamūla tālāvatthukata",
         "&ldquo;cut off at the root, made like a palm stump&rdquo; &mdash; the canon&rsquo;s "
         "standard formula for something permanently ended. A palm cut through the crown cannot "
         "regrow."),
        ("diṭṭheva dhamme upapajje vā apare vā pariyāye",
         "&ldquo;in the present life, in the next life, or in some subsequent period&rdquo; &mdash; "
         "the three timings for a result, stated so that a delay cannot be read as an acquittal."),
    ],
    text_intro=(
        "The discourse in full, both triads with their similes and the closing verses. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Three sources"),
        ("p", "&sect;1", "an3.34:1.1-1.3"),
        ("p", "&sect;2&ndash;4", "an3.34:2.1-4.2"),
        ("h3", "Seeds sown in a good field"),
        ("p", "&sect;5&ndash;6", "an3.34:5.1-6.4"),
        ("h3", "And three more"),
        ("p", "&sect;7", "an3.34:7.1-7.3"),
        ("p", "&sect;8&ndash;10", "an3.34:8.1-10.1"),
        ("h3", "Seeds burned to ash"),
        ("p", "&sect;11&ndash;12", "an3.34:11.1-12.4"),
        ("h3", "In verse"),
        ("p", "&sect;13&ndash;14", "an3.34:13.1-14.4"),
    ],
    quiz=[
        {"q": "What does <em>nidāna</em> mean, and what question does it set?",
         "opts": [
             "&ldquo;Result&rdquo; &mdash; what deeds produce",
             "&ldquo;Source&rdquo; &mdash; not which deeds are bad, but what deeds come out of",
             "&ldquo;Story&rdquo; &mdash; the setting of a discourse",
             "&ldquo;Intention&rdquo; &mdash; the will behind an act"],
         "correct": 1,
         "expl": "The same word titles the great chapter on dependent origination."},
        {"q": "Why does the guide stress that the roots are not deeds?",
         "opts": [
             "Because greed is not stealing and hate is not violence &mdash; they are what such acts come out of, which is what lets the discourse speak about all deeds at once",
             "Because the roots are only mental and therefore harmless",
             "Because deeds are unimportant",
             "Because the roots apply only to monastics"],
         "correct": 0,
         "expl": "That distinction is the entire content of the word <em>nidāna</em>."},
        {"q": "What two separate claims are packed into the repeated sentence?",
         "opts": [
             "One about intention and one about speech",
             "One about place &mdash; the deed ripens wherever the doer is reborn &mdash; and one about time, with three options rather than one",
             "One about monastics and one about laypeople",
             "One about this life only"],
         "correct": 1,
         "expl": "The result is not held in a ledger elsewhere, and it is not on a schedule the doer controls."},
        {"q": "How does the guide handle a reader who does not accept rebirth?",
         "opts": [
             "By treating &ldquo;next life&rdquo; as a metaphor for tomorrow",
             "By saying the objection is not allowed",
             "By stating plainly that the discourse assumes rebirth and that the text is not on that reader&rsquo;s side of the question",
             "By omitting the passage"],
         "correct": 2,
         "expl": "Reading it as metaphor makes the sentence say nothing at all."},
        {"q": "What is the first simile, and what does it establish?",
         "opts": [
             "Seeds sown in poor soil &mdash; deeds are wasted",
             "Sound seeds in a prepared field with plenty of rain &mdash; deeds rooted in the three roots are not defective machinery; they function",
             "A fire in a grass hut",
             "A pot turned upside down"],
         "correct": 1,
         "expl": "Everything in the image is working, and that is the point."},
        {"q": "What happens to the seeds in the second simile?",
         "opts": [
             "They are stored for later",
             "They are planted in a better field",
             "They are burned to ash and the ashes whisked away in a strong wind or floated down a swift stream",
             "They are eaten by birds"],
         "correct": 2,
         "expl": "Not stored, not neutralized, not offset &mdash; ended, and the remains dispersed beyond recovery."},
        {"q": "What asymmetry does the guide call the discourse&rsquo;s real argument?",
         "opts": [
             "That good deeds ripen faster",
             "That the second half is not a symmetrical ledger of good fruit for good deeds &mdash; the subject changes from what kamma produces to how kamma stops",
             "That hate is worse than greed",
             "That the similes are the same"],
         "correct": 1,
         "expl": "The reader arrives expecting a ledger, and does not get one."},
        {"q": "How does the guide treat the puzzling sentence about wholesome-rooted deeds?",
         "opts": [
             "As a translation error to be ignored",
             "As settled by the commentary",
             "As a genuine crux &mdash; two readings are set out, and the guide declines to pretend the question is settled",
             "As proof that good deeds have no result"],
         "correct": 2,
         "expl": "Both readings land in the same place, which is why the disagreement is tolerable."},
        {"q": "What do the closing verses say about when deeds are experienced?",
         "opts": [
             "In the present life, the next, or some subsequent period",
             "Right here, not in any other place &mdash; compressing the prose&rsquo;s three timings into one",
             "Only after death",
             "They say nothing about timing"],
         "correct": 1,
         "expl": "The same thing the verses do at AN 3.26 and AN 3.27."},
        {"q": "What does the guide recommend doing about that gap?",
         "opts": [
             "Accusing the verse of error",
             "Treating the verse as the discourse&rsquo;s real doctrine",
             "Pointing at the seam rather than smoothing it over &mdash; verse works by force rather than precision, and the prose eight paragraphs earlier is wider",
             "Removing the verse"],
         "correct": 2,
         "expl": "&ldquo;Right here, not in any other place&rdquo; is doing rhetorical work: there is no elsewhere to send consequences to."},
    ],
    marginalia=[
        ("Three roots", [
            "<span class=\"pali\">lobha</span>greed &middot; 貪",
            "<span class=\"pali\">dosa</span>hate &middot; 瞋",
            "<span class=\"pali\">moha</span>delusion &middot; 癡",
        ]),
        ("Two similes", [
            "sound seed, good field, rain",
            "burned, ashed, scattered",
            "&mdash; function vs. ending",
        ]),
        ("Three timings", [
            "in the present life",
            "in the next life",
            "in some subsequent period",
            "&mdash; dropped by the verse",
        ]),
        ("Cross-references", [
            "AN 3.100 &middot; the lump of salt",
            "AN 3.26 &middot; verse dropping prose",
            "AN 3.35 &middot; the palm-stump formula",
        ]),
    ],
    further=[
        '<a href="%s/an3.34/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.100.html">AN 3.100 &middot; A Lump of Salt</a> &mdash; the other great kamma '
        "discourse of the Threes, and the necessary companion: where this one says a result comes at "
        "one of three times, that one says the same deed lands differently depending on who did it.",
        '<a href="an-3.26.html">AN 3.26 &middot; Associates</a> &mdash; for the same seam between '
        "prose and closing verse, where a qualification carefully stated in prose is dropped when "
        "the material goes into meter.",
        '<a href="/abhidharma/abhidharmakosa/fascicle-013/">Abhidharmakośa &middot; Fascicle 13</a> '
        "&mdash; the opening of the karma chapter, where the same question this discourse asks in "
        "five paragraphs becomes a systematic treatment: what kamma is, whether it leaves a physical "
        "residue, and why no creator god is needed to explain the world&rsquo;s differences.",
        '<a href="an-3.35.html">AN 3.35 &middot; With Hatthaka</a> &mdash; the next discourse, which '
        "applies the same palm-stump formula to a person rather than to a deed.",
    ],
)


page(
    35, "Hatthaka", "With Hatthaka",
    vagga=VAGGA_4,
    meta_title="AN 3.35 — With Hatthaka | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Hatthakasutta — the "
        "Buddha, asked whether he slept well on a mat of leaves in midwinter, says yes, and "
        "answers with the most comfortable bed in the discourses. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "Near Āḷavī, on a mat of leaves by a cow-path in a rosewood grove, in the week "
                    "of mid-winter"),
        ("Speakers", "Hatthaka of Āḷavī and the Buddha"),
        ("Form", "A polite question taken literally, a counter-question with a long simile, three "
                 "rounds of the same argument, and closing verses"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The exchange with Hatthaka on sleeping at ease has counterparts in the "
                              "Chinese Āgamas; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; one of the most immediately "
                       "readable discourses in the Threes"),
    ],
    why=(
        "Hatthaka finds the Buddha sitting on leaves by a cow-path in the coldest week of the year "
        "and asks the polite question &mdash; did you sleep well? The Buddha says yes, and adds that "
        "he is one of those who sleep at ease in the world. Hatthaka lists everything wrong with the "
        "situation: frozen ground, thin leaves, bare trees, cold robes, a north wind. And the reply "
        "is not an argument about hardship. It is a description of the most comfortable bedroom in "
        "the discourses, and a question about who is really asleep in it."),
    guide=[
        ("The teaching in one sentence", [
            "Sleeping well is not a fact about the bed."]),
        ("The scene, and why it is drawn so carefully", [
            "The details are unusually specific for this collection: Āḷavī, a mat of leaves, a "
            "cow-path in a rosewood grove, the week of mid-winter when the snow falls, ground "
            "trampled hard by hooves, sparse leaves on the trees, thin ocher robes, a north wind. "
            "Hatthaka supplies most of them himself, in one breath, as an objection.",
            "This matters because the discourse could easily have been an assertion that discomfort "
            "does not matter to a spiritually advanced person. It is not. Hatthaka&rsquo;s catalogue "
            "is allowed to stand in full and is never contradicted. The Buddha does not say the "
            "ground was soft or the wind was mild.",
            "Hatthaka is a lay disciple of Āḷavī, addressed here as <em>kumāra</em>, prince. He "
            "appears elsewhere in this same chapter at AN 3.127 and is one of the more attractive "
            "laypeople in the collection: rich, well connected, and consistently drawn as someone who "
            "asks direct questions and takes the answers."]),
        ("The bungalow", [
            "Rather than defend the leaves, the Buddha describes their opposite in loving detail. A "
            "householder or his son in a bungalow plastered inside and out, draft-free, with door "
            "fastened and window shuttered. A couch spread with woolen covers &mdash; shag-piled, "
            "pure white, or embroidered with flowers &mdash; and a fine deer hide, a canopy above, "
            "red pillows at both ends. A lamp burning. Four wives attending to him in all manner of "
            "agreeable ways.",
            "The building is word for word the mansion of AN 3.1, where the same sealed and shuttered "
            "bungalow burns down because a fire started in a grass hut next door. Whoever assembled "
            "the Threes liked this image, and both discourses use it the same way: as the best "
            "protection money can build, and as insufficient.",
            "The wives belong to that inventory, and it is worth naming plainly what a modern reader "
            "is looking at. They appear in the list the way the deer hide and the red pillows appear "
            "&mdash; as items in an ancient rich man&rsquo;s catalogue of comfort. The discourse is "
            "not recommending the arrangement; it is not discussing the arrangement at all. It is "
            "describing the most enviable situation its first audience could imagine in order to say "
            "that the man in it may still be lying awake. A class can be told exactly that, and told "
            "that the text&rsquo;s indifference to the wives as people is a feature of its world "
            "rather than a teaching of the discourse."]),
        ("The question that turns it", [
            "Hatthaka agrees at once that such a man sleeps at ease &mdash; of those who sleep at "
            "ease in the world, he would be one. Which is the whole trap, because he has just used "
            "the Buddha&rsquo;s own phrase.",
            "Then: <em>is it not possible that a fever born of greed &mdash; physical or mental "
            "&mdash; might arise in that householder, burning him so he sleeps badly?</em> Hatthaka "
            "says yes. The same for hate, and for delusion.",
            "<em>Pariḷāha</em> is fever, burning, torment; and the discourse insists it can be "
            "<em>kāyika</em> or <em>cetasika</em>, of the body or of the mind. Nothing in the "
            "bungalow addresses either. Shutters keep out wind, not the thing that is actually "
            "keeping the man awake.",
            "So the argument is not that austerity is superior to comfort. It is that comfort and "
            "torment are answers to different questions, and the fully equipped bedroom is aimed at "
            "the wrong one."]),
        ("What the Buddha claims for himself", [
            "&ldquo;The greed that burns that householder, making them sleep badly, has been cut off "
            "at the root by the Realized One, made like a palm stump, obliterated, and unable to "
            "arise in the future. That&rsquo;s why I sleep at ease.&rdquo;",
            "The formula is the one AN 3.34 has just used for deeds. Here it is used of a person, and "
            "the claim is stated in the third person &mdash; <em>by the Realized One</em> &mdash; "
            "which is the canon&rsquo;s usual register when the Buddha describes his own condition "
            "as a matter of fact rather than of feeling.",
            "Note what is <em>not</em> claimed. He does not say he feels no cold. He says the cause "
            "of the fever is gone. The mat of leaves is still thin; the north wind is still blowing; "
            "the man in the bungalow is still better provided for in every respect the two of them "
            "have discussed. What has changed is the one variable neither the leaves nor the shutters "
            "could touch."]),
        ("Using it", [
            "This is the discourse to teach when a class has begun to suspect that Buddhism is "
            "against comfort. It is not: the bungalow is described with evident relish, and the "
            "Buddha never suggests the householder should give it up. The claim is narrower and "
            "harder to argue with &mdash; that the equipment does not reach the problem.",
            "It also models something useful about answering questions. Hatthaka asks a formality and "
            "gets a literal answer; he raises an objection and gets a counter-question rather than a "
            "rebuttal; and he arrives at the conclusion himself, having agreed to every step. "
            "Nowhere is he told he is wrong.",
            "The closing verses generalize it: the one who is fully quenched always sleeps at ease, "
            "sensual pleasures slip off them, they are cooled and free of attachments. <em>Cooled</em> "
            "&mdash; <em>sītibhūta</em>, become cool &mdash; is the exact opposite of the fever, and "
            "it is worth pointing out that in a country where the problem is heat, the word for "
            "liberation reaches for coolness while a Northern European vocabulary would have reached "
            "for warmth."]),
    ],
    terms=[
        ("sukhaṁ seti",
         "&ldquo;sleeps at ease&rdquo; &mdash; the phrase the whole discourse turns on. Hatthaka "
         "uses it of the man in the bungalow, having just heard the Buddha use it of himself on a mat "
         "of leaves."),
        ("pariḷāha",
         "&ldquo;fever, burning, torment&rdquo; &mdash; and the discourse specifies that it may be "
         "<em>kāyika</em> or <em>cetasika</em>, bodily or mental. Nothing in the bungalow addresses "
         "either."),
        ("ucchinnamūla tālāvatthukata",
         "&ldquo;cut off at the root, made like a palm stump&rdquo; &mdash; the same formula AN 3.34 "
         "applies to deeds, here applied to the three roots in a person."),
        ("sītibhūta",
         "&ldquo;become cool&rdquo; &mdash; the closing verses&rsquo; word for the quenched person, "
         "the exact opposite of the fever, and a reminder that the vocabulary of liberation was "
         "formed in a hot country."),
        ("kumāra",
         "&ldquo;prince&rdquo; &mdash; how the Buddha addresses Hatthaka of Āḷavī, a wealthy lay "
         "disciple who appears again in this collection at AN 3.127."),
    ],
    text_intro=(
        "The discourse in full, with its closing verses. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "On a mat of leaves in midwinter"),
        ("p", "&sect;1", "an3.35:1.1-1.7"),
        ("p", "&sect;2", "an3.35:2.1-2.4"),
        ("h3", "The bungalow"),
        ("p", "&sect;3", "an3.35:3.1-3.9"),
        ("h3", "The fever"),
        ("p", "&sect;4", "an3.35:4.1-4.3"),
        ("p", "&sect;5", "an3.35:5.1-5.2"),
        ("p", "&sect;6", "an3.35:6.1-6.4"),
        ("p", "&sect;7", "an3.35:7.1-7.2"),
        ("h3", "In verse"),
        ("p", "&sect;8&ndash;9", "an3.35:8.1-9.4"),
    ],
    quiz=[
        {"q": "What does Hatthaka ask, and what does he get?",
         "opts": [
             "A question about rebirth, answered with a simile",
             "The polite question &mdash; did the Buddha sleep well? &mdash; answered literally, and with the claim to be one of those who sleep at ease in the world",
             "A request for ordination",
             "A question about the cold, answered with a rebuke"],
         "correct": 1,
         "expl": "A formality taken literally is what starts the discourse."},
        {"q": "What does the Buddha do with Hatthaka&rsquo;s catalogue of hardships?",
         "opts": [
             "Denies them &mdash; the ground was soft and the wind mild",
             "Lets them stand in full and never contradicts them",
             "Says they do not matter to an advanced practitioner",
             "Says Hatthaka is exaggerating"],
         "correct": 1,
         "expl": "The discourse is not an assertion that discomfort does not matter."},
        {"q": "What does the Buddha describe in reply?",
         "opts": [
             "A monastery",
             "A forest hut",
             "A bungalow plastered inside and out, with a shag-piled couch, a canopy, red pillows, a burning lamp, and four wives in attendance",
             "A king&rsquo;s palace at war"],
         "correct": 2,
         "expl": "Rather than defend the leaves, he describes their opposite in loving detail."},
        {"q": "Where else in the Threes does that same bungalow appear?",
         "opts": [
             "AN 3.1, where it burns down because a fire started in a grass hut next door",
             "AN 3.30, as a pot set upright",
             "AN 3.21, as an example of seniority",
             "It appears only here"],
         "correct": 0,
         "expl": "Both discourses use it the same way: the best protection money can build, and insufficient."},
        {"q": "How does the guide handle the four wives?",
         "opts": [
             "By omitting the passage",
             "By treating it as a teaching about marriage",
             "By naming plainly that they appear as items in an ancient rich man&rsquo;s inventory of comfort, and that the text&rsquo;s indifference to them as people belongs to its world rather than to the discourse&rsquo;s teaching",
             "By arguing that the passage is a later addition"],
         "correct": 2,
         "expl": "The discourse is not recommending the arrangement; it is not discussing it at all."},
        {"q": "What does Hatthaka concede, and why does it matter?",
         "opts": [
             "That such a man sleeps at ease &mdash; using the Buddha&rsquo;s own phrase, which is the whole trap",
             "That the Buddha is right about the cold",
             "That wealth is worthless",
             "That he cannot answer"],
         "correct": 0,
         "expl": "He has agreed to every step before the conclusion arrives."},
        {"q": "What is <em>pariḷāha</em>, and what does the discourse specify about it?",
         "opts": [
             "Cold; and that it affects only the body",
             "Fever or burning; and that it may be bodily or mental",
             "Fear; and that it affects only the mind",
             "Hunger; and that it is easily relieved"],
         "correct": 1,
         "expl": "Shutters keep out wind, not the thing that is actually keeping the man awake."},
        {"q": "What is the argument, according to the guide?",
         "opts": [
             "That austerity is superior to comfort",
             "That the householder should give up his bungalow",
             "That comfort and torment are answers to different questions, and the fully equipped bedroom is aimed at the wrong one",
             "That sleep is unimportant"],
         "correct": 2,
         "expl": "Which is why the discourse works on a class that suspects Buddhism is against comfort."},
        {"q": "What does the Buddha claim for himself, and what does he not claim?",
         "opts": [
             "That he feels no cold",
             "That the cause of the fever is gone &mdash; cut off at the root like a palm stump &mdash; not that he feels no cold",
             "That the leaves are comfortable",
             "That he does not sleep at all"],
         "correct": 1,
         "expl": "The mat is still thin and the north wind is still blowing."},
        {"q": "What does the guide notice about the word <em>sītibhūta</em>, &ldquo;become cool&rdquo;?",
         "opts": [
             "That it means indifference",
             "That it is a late addition",
             "That in a hot country the vocabulary of liberation reaches for coolness, where a Northern European vocabulary would have reached for warmth",
             "That it refers to the weather in the discourse"],
         "correct": 2,
         "expl": "And it is the exact opposite of the fever the discourse has been describing."},
    ],
    marginalia=[
        ("The mat", [
            "mid-winter, snow falling",
            "ground hard with hooves",
            "thin leaves, cold robes",
            "&mdash; never denied",
        ]),
        ("The bungalow", [
            "plastered, shuttered, draft-free",
            "shag-piled covers, deer hide",
            "canopy, red pillows, a lamp",
        ]),
        ("What it cannot reach", [
            "<span class=\"pali\">pariḷāha</span>fever",
            "bodily or mental",
            "&mdash; born of greed, hate, delusion",
        ]),
        ("Cross-references", [
            "AN 3.1 &middot; the same bungalow, burning",
            "AN 3.34 &middot; the palm-stump formula",
            "Dhp 15 &middot; happiness, in verse",
        ]),
    ],
    further=[
        '<a href="%s/an3.35/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.1.html">AN 3.1 &middot; Perils</a> &mdash; where the identical bungalow, '
        "plastered inside and out with door fastened and window shuttered, burns down because of a "
        "fire next door. Read together, the two discourses say that the best-built shelter fails "
        "against both what comes from outside and what comes from inside.",
        '<a href="an-3.34.html">AN 3.34 &middot; Sources</a> &mdash; the previous discourse, which '
        "applies the palm-stump formula to deeds; this one applies it to the roots in a person.",
        '<a href="../dhammapada/dhp-15.html">Dhammapada &middot; Chapter 15, Happiness</a> &mdash; '
        "the verse collection on the same claim, including the line about living happily among those "
        "who are afflicted. Useful beside AN 3.35 for how the same idea sounds without a narrative "
        "around it.",
        '<a href="../majjhima-nikaya/mn-004.html">MN 4 &middot; Fear and Dread</a> &mdash; the '
        "Buddha&rsquo;s own account of what it took to sit out the nights in the wilderness, and the "
        "long list of things that make a mind unable to settle. It supplies the interior of the "
        "situation Hatthaka is looking at from the outside.",
    ],
)


page(
    36, "Devadūta", "Messengers of the Gods",
    vagga=VAGGA_4,
    meta_title="AN 3.36 — Messengers of the Gods | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Devadūtasutta, which "
        "gives the chapter its name — King Yama's three questions, the hells, and the one wish "
        "the lord of the underworld makes for himself. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "A narrated interrogation in three identical rounds, a passage of punishments, a "
                 "verse describing the Great Hell, a reported wish, and four closing verses"),
        ("Length", "~7 minutes to read"),
        ("Northern parallel", "The discourse of the divine messengers is well represented in the "
                              "Chinese Madhyama-āgama (T26) and its imagery passed into East Asian "
                              "art and liturgy through the Ten Kings tradition; the longer Pāli "
                              "version with five messengers is at MN 130; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; plainly told, and the most "
                       "graphic discourse in the Threes"),
    ],
    why=(
        "Three messengers are sent among human beings and everybody sees them: an old person, a sick "
        "person, and a corpse. The discourse imagines the interview that follows for someone who saw "
        "all three and did nothing. King Yama asks the same question three times, gets the same "
        "answer three times &mdash; <em>I couldn&rsquo;t, sir. I was negligent</em> &mdash; and then "
        "falls silent. What comes next is the harshest passage in the Threes. But the discourse ends "
        "somewhere unexpected: with Yama himself hoping to be reborn as a human being so that he can "
        "meet a Buddha."),
    guide=[
        ("The teaching in one sentence", [
            "The warnings were not hidden and not rare; they were an old person, a sick person, and a "
            "corpse, and the only question afterward is what you did about seeing them."]),
        ("Who the messengers are", [
            "<em>Devadūta</em> is a messenger or envoy of the gods, and the joke &mdash; if that is "
            "the word &mdash; is that they are not supernatural at all. The first is an old man or "
            "woman of eighty, ninety, or a hundred, bent double, leaning on a staff, teeth broken and "
            "skin blotchy. The second is somebody gravely ill, fallen in their own waste, lifted by "
            "one person and set down by another. The third is a body two or three days dead, bloated "
            "and festering.",
            "Nothing has been sent. These are simply the three things everybody sees, renamed as "
            "dispatches. The renaming is the entire argument: what looks like the ordinary background "
            "of human life is treated as a message that has already been delivered, and the recipient "
            "signed for it.",
            "MN 130 tells the same story at greater length with five messengers, adding a newborn "
            "infant at the start and a criminal being punished. The Threes keep the three that "
            "correspond exactly to the three reflections of AN 3.39, which is the next-but-three "
            "discourse in this same chapter and the reason the pair should be read together."]),
        ("What Yama actually does", [
            "It is worth being precise, because a reader raised on a different underworld will supply "
            "the wrong picture. Yama does not sentence anybody. He asks a question &mdash; did you "
            "not see the messenger? &mdash; and when the answer is <em>I saw nothing</em>, he "
            "describes what was there until the person admits having seen it. Then he asks whether "
            "the obvious thought followed: <em>I too am liable to grow old; I am not exempt; I had "
            "better do good.</em>",
            "The reply each time is <em>I couldn&rsquo;t, sir. I was negligent</em>. <em>Pamāda</em>, "
            "negligence or heedlessness, is the canon&rsquo;s great single-word diagnosis, and the "
            "discourse puts it in the person&rsquo;s own mouth rather than in the mouth of the judge.",
            "Then the crucial sentence, repeated three times: <em>that bad deed wasn&rsquo;t done by "
            "your mother, father, brother, or sister; it wasn&rsquo;t done by friends and colleagues, "
            "by relatives and kin, by the deities, or by ascetics and brahmins. That bad deed was "
            "done by you alone, and you alone will experience the result.</em>",
            "That list is doing careful work. It rules out inherited guilt, it rules out family "
            "liability, and by naming deities and ascetics it rules out the transfer of responsibility "
            "to any religious specialist. Nobody stands between the person and the consequence in "
            "either direction &mdash; which is also why nobody can intercede.",
            "And after the third round Yama <em>falls silent</em>. He does not pronounce. The wardens "
            "act; the king says nothing more."]),
        ("The hells, and how to read them honestly", [
            "The punishments are described in detail: the five-fold crucifixion with red-hot stakes "
            "through hands, feet, and chest; hacking with axes; being harnessed to a chariot and "
            "driven across burning ground; a mountain of coals; a copper pot in which the person is "
            "swept up and down and round and round in boiling scum. Then the Great Hell, four-cornered "
            "and iron-roofed, radiating heat a hundred leagues.",
            "A modern class will have three objections and they should be met in order rather than "
            "hurried past.",
            "First, the sheer cruelty. It is cruel, and the text does not soften it. What can be said "
            "is what the text itself keeps repeating: <em>they don&rsquo;t die until that bad deed is "
            "eliminated</em>. The suffering is bounded by the deed rather than by a sentence, and "
            "when the deed is exhausted the situation ends. Buddhist hells are long and they are not "
            "eternal, and that is a real structural difference from the doctrine most Western readers "
            "grew up arguing with.",
            "Second, proportionality &mdash; can any finite act deserve this? The discourse does not "
            "argue the point, and pretending otherwise would be dishonest. What it says is that the "
            "punishment fits the negligence, and the framework it assumes is one of natural "
            "consequence rather than judicial retribution: nobody chose the sentence, which is "
            "precisely why Yama has nothing to say after the third question.",
            "Third, whether any of it is literal. Here the tradition itself argues, and it is worth "
            "telling a class that the argument is internal rather than a modern embarrassment. "
            "Vasubandhu, in the Viṃśatikā, uses the wardens of hell as a test case and concludes that "
            "they are not independent beings at all but appearances thrown up by the kamma of those "
            "who see them &mdash; a position developed within Buddhist scholasticism, in Sanskrit, "
            "long before anyone in Europe had an opinion about it."]),
        ("Yama&rsquo;s wish", [
            "Then the discourse does something no summary of it ever mentions. King Yama, having "
            "watched this happen for a very long time, thinks: <em>oh, I hope I may be reborn as a "
            "human being! And that a Realized One arises in the world! And that I may pay homage to "
            "the Buddha, so that he can teach me Dhamma, and I may understand his teaching.</em>",
            "The lord of the underworld wants to be a person, and specifically he wants the one thing "
            "the people in front of him had and wasted: a human life during which a Buddha is "
            "available. In one paragraph the discourse converts its own most terrifying figure into "
            "evidence for its central claim &mdash; that a human birth in which the teaching can be "
            "heard is the rarest and most valuable position in the cosmos, and that being a king in "
            "any other realm is worse.",
            "The Buddha then adds a line that is easy to skip: <em>I don&rsquo;t say this because "
            "I&rsquo;ve heard it from some other ascetic or brahmin. I only say it because I&rsquo;ve "
            "known, seen, and realized it for myself.</em> He is aware that he is reporting the inner "
            "monologue of a mythological king, and he marks the claim as first-hand rather than "
            "traditional. Whatever one makes of the claim, the discourse is not passing on folklore "
            "unexamined."]),
        ("Using it", [
            "This is a hard text to teach and an easy one to teach badly, in either direction: as "
            "horror, or as embarrassed allegory. The honest middle is to let the hells be as bad as "
            "they are, name the three objections, and then point at what the discourse is actually "
            "built to do, which is not to frighten anybody into belief but to make an ordinary "
            "observation unavoidable.",
            "The observation is in Yama&rsquo;s question, and it survives every disagreement about "
            "cosmology: you have seen an old person, a sick person, and a dead body, and you are not "
            "exempt from any of the three. The interrogation format simply asks the question that "
            "nobody asks themselves at the time.",
            "The closing verses supply the constructive half, and they are the reason the discourse "
            "is not merely a threat: those warned by the messengers who do not neglect the teaching "
            "see the peril in grasping, are freed with the ending of birth and death, and are "
            "<em>quenched in this very life</em>. The point of arrival is not a better rebirth. It is "
            "safety now."]),
    ],
    terms=[
        ("devadūta",
         "&ldquo;messenger of the gods&rdquo; &mdash; and the three are an old person, a sick person, "
         "and a corpse. Nothing is sent; what everyone already sees is renamed as a dispatch."),
        ("yama",
         "the king of the underworld, inherited from earlier Indian religion. In this discourse he "
         "interrogates rather than sentences, and after the third question he falls silent."),
        ("pamāda",
         "&ldquo;negligence, heedlessness&rdquo; &mdash; the canon&rsquo;s single-word diagnosis, and "
         "in this discourse the answer the person gives about themselves rather than the charge laid "
         "against them."),
        ("niraya",
         "&ldquo;hell&rdquo; &mdash; long but not everlasting: the text repeats that the being does "
         "not die until the bad deed is eliminated, which bounds the suffering by the deed rather "
         "than by a sentence."),
        ("mahāniraya",
         "&ldquo;the Great Hell&rdquo; &mdash; four-cornered, four-doored, walled and roofed in iron, "
         "radiating heat a hundred leagues, described in a verse the canon quotes in several places."),
    ],
    text_intro=(
        "The discourse in full, including the punishments and the closing verses. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Brought before King Yama"),
        ("p", "&sect;1", "an3.36:1.1-1.7"),
        ("h3", "The first messenger"),
        ("p", "&sect;2&ndash;5", "an3.36:2.1-5.5"),
        ("h3", "The second"),
        ("p", "&sect;6&ndash;8", "an3.36:6.1-8.5"),
        ("h3", "The third"),
        ("p", "&sect;9&ndash;12", "an3.36:9.1-12.5"),
        ("h3", "The king falls silent"),
        ("p", "&sect;13", "an3.36:13.1-13.4"),
        ("p", "&sect;14&ndash;15", "an3.36:14.1-15.8"),
        ("p", "&sect;16&ndash;17", "an3.36:16.1-17.4"),
        ("h3", "What King Yama wants"),
        ("p", "&sect;18", "an3.36:18.1-18.5"),
        ("h3", "In verse"),
        ("p", "&sect;19&ndash;20", "an3.36:19.1-20.4"),
        ("p", "&sect;21&ndash;22", "an3.36:21.1-22.4"),
    ],
    quiz=[
        {"q": "Who are the three messengers of the gods?",
         "opts": [
             "Three deities sent to warn humanity",
             "An old person, a sick person, and a corpse &mdash; things everybody already sees, renamed as dispatches",
             "Three past Buddhas",
             "Yama&rsquo;s three ministers"],
         "correct": 1,
         "expl": "Nothing has been sent; the renaming is the entire argument."},
        {"q": "How does the longer version at MN 130 differ?",
         "opts": [
             "It has five messengers, adding a newborn infant and a criminal being punished",
             "It has only two",
             "It omits the hells",
             "It is spoken by Sāriputta"],
         "correct": 0,
         "expl": "The Threes keep the three that match the three reflections of AN 3.39."},
        {"q": "What does King Yama actually do in this discourse?",
         "opts": [
             "Pronounces a sentence",
             "Weighs the person&rsquo;s deeds on a scale",
             "Asks whether the person saw the messenger, then whether the obvious thought followed &mdash; and after the third round falls silent",
             "Argues the person&rsquo;s case for them"],
         "correct": 2,
         "expl": "The wardens act; the king says nothing more."},
        {"q": "What answer does the person give each time?",
         "opts": [
             "&ldquo;It was not my fault.&rdquo;",
             "&ldquo;I couldn&rsquo;t, sir. I was negligent.&rdquo;",
             "&ldquo;I did not know.&rdquo;",
             "&ldquo;I was following orders.&rdquo;"],
         "correct": 1,
         "expl": "<em>Pamāda</em> is put in the person&rsquo;s own mouth rather than in the judge&rsquo;s."},
        {"q": "What is the long list of people who did not do the deed accomplishing?",
         "opts": [
             "Nothing; it is a stock formula",
             "Ruling out inherited guilt, family liability, and &mdash; by naming deities and ascetics &mdash; the transfer of responsibility to any religious specialist",
             "Blaming the family after all",
             "Establishing who should be punished instead"],
         "correct": 1,
         "expl": "Nobody stands between the person and the consequence in either direction, which is also why nobody can intercede."},
        {"q": "What does the text keep repeating about the punishments?",
         "opts": [
             "That they last forever",
             "That they are deserved",
             "That the being does not die until that bad deed is eliminated &mdash; the suffering is bounded by the deed rather than by a sentence",
             "That they are symbolic"],
         "correct": 2,
         "expl": "Buddhist hells are long and not eternal, which is a real structural difference."},
        {"q": "How does the guide handle the objection about proportionality?",
         "opts": [
             "By claiming the discourse answers it",
             "By saying the discourse does not argue the point, and that the framework it assumes is natural consequence rather than judicial retribution",
             "By saying the objection is modern and therefore invalid",
             "By omitting the passage"],
         "correct": 1,
         "expl": "Which is precisely why Yama has nothing to say after the third question."},
        {"q": "Which Buddhist thinker used the wardens of hell as a test case, and what did he conclude?",
         "opts": [
             "Nāgārjuna &mdash; that hells are empty",
             "Buddhaghosa &mdash; that they are literal",
             "Vasubandhu, in the Viṃśatikā &mdash; that they are not independent beings but appearances thrown up by the kamma of those who see them",
             "Zhiyi &mdash; that they are states of mind only"],
         "correct": 2,
         "expl": "The argument about literalness is internal to the tradition, not a modern embarrassment."},
        {"q": "What does King Yama wish for himself?",
         "opts": [
             "A larger realm",
             "To be reborn as a human being, in a world where a Buddha has arisen, so that he can hear and understand the teaching",
             "To be released from his office",
             "To become a god of the thirty-three"],
         "correct": 1,
         "expl": "The discourse converts its most terrifying figure into evidence that a human birth with a Buddha available is the rarest position in the cosmos."},
        {"q": "What do the closing verses give as the point of arrival?",
         "opts": [
             "A better rebirth",
             "A shorter time in hell",
             "Safety now &mdash; the unattached are freed with the ending of birth and death, quenched in this very life",
             "The favor of the gods"],
         "correct": 2,
         "expl": "Which is why the discourse is not merely a threat."},
    ],
    marginalia=[
        ("Three messengers", [
            "an old person",
            "a sick person",
            "a corpse",
            "&mdash; already delivered",
        ]),
        ("The one question", [
            "&ldquo;did you not see?&rdquo;",
            "&ldquo;did it not occur to you?&rdquo;",
            "&ldquo;I was negligent.&rdquo;",
        ]),
        ("Nobody else did it", [
            "not mother or father",
            "not friends or kin",
            "not deities",
            "not ascetics or brahmins",
        ]),
        ("Cross-references", [
            "MN 130 &middot; five messengers",
            "AN 3.39 &middot; the same three, voluntary",
            "Viṃśatikā &middot; are the wardens real?",
        ]),
    ],
    further=[
        '<a href="%s/an3.36/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../majjhima-nikaya/mn-130.html">MN 130 &middot; Messengers of the Gods</a> '
        "&mdash; the long version, with five messengers instead of three and the hells at greater "
        "length. Read after this one it shows what the Threes cut and why the number three was worth "
        "cutting to.",
        '<a href="an-3.39.html">AN 3.39 &middot; A Delicate Lifestyle</a> &mdash; the necessary '
        "companion, three discourses later in this same chapter: the young Bodhisatta asking himself "
        "exactly the question Yama asks, and answering it in time.",
        '<a href="/sutras/vimsatika/part-01/">Viṃśatikā &middot; Part 1</a> &mdash; where Vasubandhu '
        "takes the hells as his hardest case: if there is no external world, how do the condemned "
        "share a fixed place and time and see the same wardens? His answer, that the wardens are "
        "appearances produced by kamma, is the tradition arguing with itself about how literally to "
        "read a passage like this one.",
        '<a href="an-3.34.html">AN 3.34 &middot; Sources</a> &mdash; for the mechanism this discourse '
        "dramatizes: where deeds come from, and the three times at which a result may be experienced.",
    ],
)


page(
    37, "Catumahārāja", "The Four Great Kings (1st)",
    vagga=VAGGA_4,
    meta_title="AN 3.37 — The Four Great Kings (1st) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Catumahārājasutta — the "
        "sabbath inspection of the world by the four great kings, and why Sakka's verse about "
        "himself was poorly sung. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "A three-stage narrative of inspection, two reports with opposite outcomes, a quoted "
                 "verse, its rejection, and the same verse reassigned"),
        ("Length", "~3 minutes to read"),
        ("Northern parallel", "The sabbath inspection by the four great kings is preserved in the "
                              "Chinese Āgamas, and the observance days became the 六齋日 of East "
                              "Asian practice; this reading guide does not assert a specific matching "
                              "sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; easy to follow, with a sharp turn "
                       "in the last third"),
    ],
    why=(
        "On the eighth day of the fortnight the ministers of the four great kings walk the world "
        "counting; on the fourteenth their sons; on the fifteenth the kings themselves. They report "
        "to the assembled gods, who are pleased or disappointed depending on the numbers. Then Sakka, "
        "lord of gods, is quoted saying <em>whoever wants to be like me would observe the sabbath</em> "
        "&mdash; and the Buddha says the verse was poorly sung. The same words are then given to "
        "somebody entitled to say them. The discourse spends two-thirds of its length building a "
        "heavenly bureaucracy and the last third pointing out that its chief executive is not worth "
        "imitating."),
    guide=[
        ("The teaching in one sentence", [
            "Whether &ldquo;be like me&rdquo; is a good thing to say depends entirely on who is "
            "saying it."]),
        ("The inspection", [
            "The four great kings are the guardian deities of the four directions &mdash; familiar to "
            "anyone who has walked into a Chinese temple past the 四大天王 at the gate. Here they run "
            "a three-tier survey on the three sabbath days of the fortnight: ministers on the eighth, "
            "the kings&rsquo; sons on the fourteenth, the kings in person on the fifteenth.",
            "What they count is precise, and it is the same list AN 3.31 was about: whether people "
            "are paying due respect to parents, ascetics and brahmins, honoring the elders of their "
            "families, observing the sabbath, and making merit.",
            "The reporting scene is worth reading slowly. If the numbers are low the gods of the "
            "thirty-three are disappointed &mdash; <em>the heavenly hosts will dwindle, while the "
            "titan hosts will swell</em>. If high, the reverse. The gods are not concerned for human "
            "welfare here. They are watching their own demographics, since human conduct determines "
            "who is born into which realm next, and the gods have an ongoing conflict with the titans "
            "to staff."]),
        ("Whether to be uneasy about the surveillance", [
            "A modern reader may find the whole apparatus unattractive: invisible officials walking "
            "the world on fixed days, checking whether you were good, and filing a report. It reads "
            "like the celestial bureaucracy of a later Chinese imagination, and in fact it is one of "
            "the places that imagination came from.",
            "Two things are worth saying plainly. The first is that the Buddha is using a picture his "
            "audience already held rather than announcing a discovery; the four great kings and the "
            "gods of the thirty-three were part of the furniture, and the discourse assumes them "
            "without arguing for them.",
            "The second is what he then does with the picture, which is to demolish the standing of "
            "the being at the top of it. That is the actual content, and it is unfriendly to "
            "surveillance rather than reliant on it. The related discourse AN 3.40 makes the point "
            "without any gods at all: what watches you most reliably is you."]),
        ("Sakka&rsquo;s verse, and its rejection", [
            "Sakka, lord of the gods of the thirty-three, is quoted encouraging the sabbath complete "
            "in all eight factors, on the fourteenth, fifteenth, and eighth days of the fortnight, "
            "and on the special displays. The content is unobjectionable; the Buddha recommends the "
            "same observance elsewhere.",
            "&ldquo;But that verse was poorly sung by Sakka, lord of gods, not well sung; poorly "
            "spoken, not well spoken. Why is that? Sakka, lord of gods, is not free of greed, hate, "
            "and delusion.&rdquo;",
            "The defect is not in the recommendation. It is in the first two words. <em>Whoever wants "
            "to be like me</em> converts a piece of good advice into an offer of a model, and Sakka "
            "is not one. A being who still has the three roots intact may say true things, and this "
            "is a true thing, but he may not hold himself up as the destination.",
            "Then the identical verse is given to a mendicant who is perfected &mdash; defilements "
            "ended, burden laid down, rightly freed through enlightenment &mdash; and it becomes "
            "appropriate, for the reason stated with the same flatness: <em>because that mendicant is "
            "free of greed, hate, and delusion</em>. Not because the monastic outranks the god, but "
            "because in the one respect the sentence depends on, the monastic has finished and the "
            "god has not."]),
        ("The eight-factored sabbath", [
            "The observance in question is the <em>uposatha</em> kept with eight factors: the five "
            "precepts, with the third tightened from misconduct to celibacy, plus abstention from "
            "eating at the wrong time, from entertainment and adornment, and from high and luxurious "
            "beds. Laypeople take it for a day and a night, on the days named here.",
            "East Asian Buddhism inherited the practice as the 八關齋戒 and the days as the 六齋日, "
            "still marked in temple calendars. A class in Taiwan is likely to have relatives who keep "
            "them, and this discourse is where the schedule is set out in Pāli.",
            "It is worth noticing that the sabbath is one of the five items the kings are counting, "
            "and that all five are things a layperson does. The heavenly census is not measuring "
            "meditation or insight. It is measuring whether ordinary households look after their "
            "parents and keep a day."]),
        ("Using it", [
            "Teach it for the reversal at the end, which is unusually clean. The class hears an "
            "unimpeachable piece of religious advice, agrees with it, and then watches the Buddha "
            "reject it on grounds that have nothing to do with its content.",
            "The transferable question is a good one for teachers in particular: what makes someone "
            "entitled to say <em>do as I do</em>? This discourse gives an answer with no wiggle room "
            "&mdash; that the speaker has actually finished the thing they are recommending &mdash; "
            "and it applies the test to a god rather than to a person, which makes it easier to "
            "discuss without anyone in the room feeling accused.",
            "AN 3.38, the next discourse, repeats the whole exchange and changes the reason. Read "
            "them together and the pair says something neither says alone."]),
    ],
    terms=[
        ("cattāro mahārājāno",
         "&ldquo;the four great kings&rdquo; &mdash; guardian deities of the four directions, the "
         "四大天王 who stand inside the gate of a Chinese temple. Here they run a three-tier survey of "
         "human conduct."),
        ("uposatha",
         "the sabbath, observed on the eighth, fourteenth, and fifteenth days of the fortnight. Kept "
         "by laypeople with eight factors, it became the 八關齋戒 of East Asian practice."),
        ("aṭṭhaṅgasamannāgata",
         "&ldquo;complete in all eight factors&rdquo; &mdash; the five precepts with celibacy in "
         "place of the third, plus abstention from untimely eating, from entertainment and adornment, "
         "and from luxurious beds."),
        ("sakka devānaminda",
         "&ldquo;Sakka, lord of gods&rdquo; &mdash; ruler of the thirty-three, a devout figure "
         "throughout the canon, and here the one whose verse is judged poorly sung."),
        ("dubbhāsita",
         "&ldquo;poorly spoken&rdquo; &mdash; the verdict on the verse. The judgment falls on the "
         "speaker&rsquo;s standing to say it, not on what was said."),
    ],
    text_intro=(
        "The discourse in full, with Sakka&rsquo;s verse given twice. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "The inspection"),
        ("p", "&sect;1", "an3.37:1.1-1.6"),
        ("p", "&sect;2", "an3.37:2.1-2.5"),
        ("p", "&sect;3", "an3.37:3.1-3.5"),
        ("h3", "Sakka&rsquo;s verse"),
        ("p", "&sect;4&ndash;5", "an3.37:4.1-5.6"),
        ("p", "&sect;6", "an3.37:6.1-6.3"),
        ("h3", "The same verse, reassigned"),
        ("p", "&sect;7&ndash;9", "an3.37:7.1-9.2"),
    ],
    quiz=[
        {"q": "Who inspects the world, and on which days?",
         "opts": [
             "The four great kings only, on the full moon",
             "Their ministers on the eighth, their sons on the fourteenth, and the kings themselves on the fifteenth",
             "Sakka, every day",
             "The gods of the thirty-three, once a year"],
         "correct": 1,
         "expl": "A three-tier survey on the three sabbath days of the fortnight."},
        {"q": "What are they counting?",
         "opts": [
             "How many people meditate",
             "How many monastics have been ordained",
             "Whether people respect parents, ascetics and brahmins, honor family elders, observe the sabbath, and make merit",
             "How many temples have been built"],
         "correct": 2,
         "expl": "All five are things a layperson does; the census is not measuring insight."},
        {"q": "Why are the gods pleased or disappointed by the report?",
         "opts": [
             "Out of concern for human welfare",
             "Because human conduct determines who is born where next &mdash; the heavenly hosts swell or dwindle while the titan hosts do the opposite",
             "Because they are judged on the numbers",
             "Because they wager on the outcome"],
         "correct": 1,
         "expl": "The gods are watching their own demographics."},
        {"q": "Where does a reader in Taiwan already meet the four great kings?",
         "opts": [
             "In the 四大天王 standing inside a Chinese temple gate",
             "In the Vinaya",
             "Only in Pāli texts",
             "In the Heart Sutra"],
         "correct": 0,
         "expl": "The discourse assumes a picture its audience already held."},
        {"q": "What does Sakka&rsquo;s verse recommend?",
         "opts": [
             "Meditation retreats",
             "Observing the sabbath complete in all eight factors, on the fourteenth, fifteenth, and eighth days",
             "Giving to the gods",
             "Ordination"],
         "correct": 1,
         "expl": "The content is unobjectionable; the Buddha recommends the same observance elsewhere."},
        {"q": "What is the Buddha&rsquo;s verdict on that verse, and why?",
         "opts": [
             "Well sung, because the advice is correct",
             "Poorly sung, because the advice is wrong",
             "Poorly sung, because Sakka is not free of greed, hate, and delusion",
             "Poorly sung, because a god should not address humans"],
         "correct": 2,
         "expl": "The judgment falls on the speaker&rsquo;s standing, not on what was said."},
        {"q": "Which part of the verse is the defect actually in?",
         "opts": [
             "The list of days",
             "The eight factors",
             "The first two words &mdash; &ldquo;whoever wants to be like me&rdquo; converts good advice into an offer of a model",
             "The meter"],
         "correct": 2,
         "expl": "A being with the three roots intact may say true things but may not hold himself up as the destination."},
        {"q": "Who is then given the same words?",
         "opts": [
             "The Buddha himself",
             "A perfected mendicant &mdash; defilements ended, burden laid down, rightly freed through enlightenment",
             "The four great kings",
             "A lay disciple"],
         "correct": 1,
         "expl": "Not because the monastic outranks the god, but because in the one respect the sentence depends on, the monastic has finished."},
        {"q": "What does the eight-factored sabbath consist of?",
         "opts": [
             "Eight hours of meditation",
             "The five precepts with celibacy in place of the third, plus no untimely eating, no entertainment or adornment, and no luxurious beds",
             "Eight days of fasting",
             "The eightfold path recited"],
         "correct": 1,
         "expl": "Kept by laypeople for a day and a night, and inherited in East Asia as the 八關齋戒."},
        {"q": "What question does the guide draw out for teachers?",
         "opts": [
             "How often to hold retreats",
             "Which days are auspicious",
             "What makes someone entitled to say &ldquo;do as I do&rdquo; &mdash; answered here as: that the speaker has actually finished the thing they are recommending",
             "Whether gods exist"],
         "correct": 2,
         "expl": "And the test is applied to a god, which makes it easier to discuss without anyone feeling accused."},
    ],
    marginalia=[
        ("Three days, three ranks", [
            "8th &middot; the ministers",
            "14th &middot; the kings&rsquo; sons",
            "15th &middot; the kings themselves",
        ]),
        ("What is counted", [
            "respect for parents",
            "respect for ascetics and brahmins",
            "honoring family elders",
            "keeping the sabbath &middot; making merit",
        ]),
        ("The verdict", [
            "<span class=\"pali\">dubbhāsita</span>poorly spoken",
            "not: the advice is wrong",
            "but: he is not free of the three roots",
        ]),
        ("Cross-references", [
            "AN 3.38 &middot; same verse, new reason",
            "AN 3.31 &middot; the list being counted",
            "AN 3.40 &middot; what watches you instead",
        ]),
    ],
    further=[
        '<a href="%s/an3.37/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.38.html">AN 3.38 &middot; The Four Great Kings (2nd)</a> &mdash; the same '
        "exchange with the reason changed, and the discourse this one has to be read with.",
        '<a href="/sutras/upasaka-precepts-sutra/chapter-21/">Sutra on Upasaka Precepts &middot; '
        "Chapter 21</a> &mdash; a Chinese Mahāyāna treatment of the same observance, where Shansheng "
        "asks what reward the three refuges and the eight-precept fast actually bring and gets an "
        "answer measured against four kingdoms&rsquo; worth of treasure.",
        '<a href="an-3.31.html">AN 3.31 &middot; With Divinity</a> &mdash; for the first item on the '
        "kings&rsquo; checklist, treated at length six discourses earlier in this chapter.",
    ],
)


page(
    38, "Dutiyacatumahārāja", "The Four Great Kings (2nd)",
    vagga=VAGGA_4,
    meta_title="AN 3.38 — The Four Great Kings (2nd) | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the second "
        "Catumahārājasutta — the same verse of Sakka's rejected again, this time for a different "
        "reason. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "A quoted verse, its rejection, the same verse reassigned, with one clause changed "
                 "throughout"),
        ("Length", "~2 minutes to read"),
        ("Northern parallel", "Comparable material on the limits of Sakka&rsquo;s standing appears in "
                              "the Chinese Āgamas; this reading guide does not assert a specific "
                              "matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; almost identical to AN 3.37, and "
                       "the difference is the whole discourse"),
    ],
    why=(
        "The same verse, the same verdict, the same reassignment &mdash; and a different reason. In "
        "AN 3.37 Sakka may not say <em>be like me</em> because he still has greed, hate, and delusion. "
        "Here it is because he is not exempt from rebirth, old age, and death, from sorrow, "
        "lamentation, pain, sadness, and distress. The Threes rarely repeat a discourse this closely, "
        "and when they do the variable is the point."),
    guide=[
        ("The teaching in one sentence", [
            "The lord of the gods cannot be a model, and there are two separate reasons why, either "
            "of which is enough."]),
        ("What has changed", [
            "The narrative frame is gone: no inspection, no ministers, no census. The discourse opens "
            "directly with Sakka&rsquo;s verse and moves straight to the verdict, which means the "
            "reader is meant to arrive already knowing AN 3.37 and to notice one clause.",
            "In AN 3.37 the disqualifier was <em>not free of greed, hate, and delusion</em> &mdash; a "
            "statement about what is still present in Sakka. Here it is <em>not exempt from rebirth, "
            "old age, and death, from sorrow, lamentation, pain, sadness, and distress; he is not "
            "exempt from suffering</em> &mdash; a statement about what is still going to happen to "
            "him.",
            "The two are related but not the same. The first names a defilement; the second names a "
            "predicament. A being could in principle be told that his mind is impure, which is a "
            "reproach, or that his situation is unresolved, which is not. The second discourse chooses "
            "the second and it is noticeably gentler in tone while being no less final."]),
        ("Why it matters that it is Sakka", [
            "Sakka is not a foil. Throughout the canon he is the most devout of the gods: he asks the "
            "Buddha questions, he is a stream-enterer by some accounts, and he is generally on the "
            "right side of every story he appears in. The verse quoted here is him doing his job "
            "well, encouraging observance among the gods.",
            "Choosing him is what makes the point general. If the discourse had disqualified a wicked "
            "deity it would have said nothing. Disqualifying the best available god says that the "
            "issue is structural: as long as birth, aging, and death are still ahead of you, you are "
            "not a destination, however admirable you are and however good your advice is.",
            "It also quietly settles the question of where the gods sit in this religion. They are "
            "real, they are powerful, they are worth being polite to, and they are fellow travelers "
            "with unfinished business. The distance from that to worship is not a short one."]),
        ("The one who may say it", [
            "The perfected mendicant gets the verse, with the qualification stated in the same terms: "
            "<em>because that mendicant is exempt from rebirth, old age, and death, from sorrow, "
            "lamentation, pain, sadness, and distress. He is exempt from suffering, I say.</em>",
            "The phrase <em>I say</em>, <em>vadāmi</em>, is doing something. This is a claim the "
            "Buddha is making on his own authority about somebody else&rsquo;s condition, and the "
            "canon marks such claims rather than leaving them impersonal.",
            "The list of what the mendicant is exempt from is the standard formula for suffering in "
            "the first noble truth, given in full. So the credential being asserted is not seniority, "
            "learning, or virtue. It is having finished with the thing the whole teaching is about."]),
        ("Reading the pair", [
            "Together the two discourses give a complete answer to a question people ask constantly "
            "in religious life: who is worth following? The answer comes in two parts, and either is "
            "sufficient to disqualify.",
            "Is there still greed, hate, or delusion in this person? Then their advice may be sound "
            "and their example is not. Is this person still subject to aging, sickness, sorrow, and "
            "death in the way everybody is? Then whatever they have, it is not the thing that solves "
            "that.",
            "The test is severe enough that almost nobody passes it, which is the intended effect. "
            "The canon&rsquo;s standing recommendation to laypeople is not to find a perfected teacher "
            "but to rely on the teaching, examine it, and keep good company &mdash; see AN 3.65, "
            "later in this chapter of the collection, for the fullest statement of that."]),
        ("Using it", [
            "Teach the two discourses as one lesson. Read AN 3.37 in full, then read AN 3.38 aloud "
            "and ask a class to find the change; it takes about thirty seconds and they will remember "
            "the point far longer than if they were told it.",
            "Then the harder question, which is the reason the pair exists: why would the compilers "
            "keep two versions differing by one clause? Because the disqualification is not a single "
            "fact about Sakka but a class of facts, and the discourse is showing the class by giving "
            "two of its members."]),
    ],
    terms=[
        ("aparimutta",
         "&ldquo;not exempt, not freed from&rdquo; &mdash; the word that replaces AN 3.37&rsquo;s "
         "&ldquo;not free of greed, hate, and delusion.&rdquo; It names a predicament rather than a "
         "defilement."),
        ("jātijarāmaraṇa",
         "&ldquo;rebirth, old age, and death&rdquo; &mdash; the opening of the standard formula for "
         "suffering, given here in full as the thing Sakka has not got past."),
        ("sokaparidevadukkhadomanassupāyāsa",
         "&ldquo;sorrow, lamentation, pain, sadness, and distress&rdquo; &mdash; the rest of that "
         "formula, familiar from the first noble truth."),
        ("khīṇāsava",
         "&ldquo;with defilements ended&rdquo; &mdash; the first item in the standard description of "
         "a perfected one, the being who may say &ldquo;be like me.&rdquo;"),
        ("vadāmi",
         "&ldquo;I say&rdquo; &mdash; the Buddha marking a claim as made on his own authority. The "
         "canon uses it where a statement about another being&rsquo;s condition is being asserted "
         "rather than reported."),
    ],
    text_intro=(
        "The discourse in full. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Sakka&rsquo;s verse"),
        ("p", "&sect;1&ndash;2", "an3.38:1.1-2.6"),
        ("p", "&sect;3", "an3.38:3.1-3.3"),
        ("h3", "The same verse, reassigned"),
        ("p", "&sect;4&ndash;5", "an3.38:4.1-5.6"),
        ("p", "&sect;6", "an3.38:6.1-6.2"),
    ],
    quiz=[
        {"q": "How does this discourse differ from AN 3.37?",
         "opts": [
             "The verse is different",
             "The narrative frame is gone and the reason for the verdict has changed",
             "Sakka is praised instead",
             "It is spoken by Ānanda"],
         "correct": 1,
         "expl": "The reader is meant to arrive already knowing AN 3.37 and to notice one clause."},
        {"q": "What is the disqualifying reason here?",
         "opts": [
             "That Sakka is not free of greed, hate, and delusion",
             "That Sakka is not exempt from rebirth, old age, and death, from sorrow, lamentation, pain, sadness, and distress",
             "That Sakka is a god rather than a human",
             "That the verse is badly composed"],
         "correct": 1,
         "expl": "A statement about what is still going to happen to him, rather than about what is still present in him."},
        {"q": "How does the guide distinguish the two reasons?",
         "opts": [
             "The first names a defilement; the second names a predicament",
             "The first is about speech; the second about action",
             "The first applies to gods; the second to humans",
             "They are identical"],
         "correct": 0,
         "expl": "The second is noticeably gentler in tone while being no less final."},
        {"q": "Why does it matter that the figure disqualified is Sakka?",
         "opts": [
             "Because he is a wicked deity",
             "Because he is the most devout of the gods, generally on the right side of every story &mdash; so disqualifying him makes the point structural rather than personal",
             "Because he is unknown to the audience",
             "Because he opposes the Buddha"],
         "correct": 1,
         "expl": "If the discourse had disqualified a wicked deity it would have said nothing."},
        {"q": "What does the pair settle about the status of gods in this religion?",
         "opts": [
             "That they do not exist",
             "That they are to be worshiped",
             "That they are real, powerful, worth being polite to, and fellow travelers with unfinished business",
             "That they are metaphors for mental states"],
         "correct": 2,
         "expl": "The distance from that to worship is not a short one."},
        {"q": "What credential does the perfected mendicant have?",
         "opts": [
             "Seniority",
             "Learning",
             "Being exempt from rebirth, old age, and death and from the rest of the standard formula for suffering",
             "Ordination in the right lineage"],
         "correct": 2,
         "expl": "Having finished with the thing the whole teaching is about."},
        {"q": "What is the guide&rsquo;s point about the word <em>vadāmi</em>, &ldquo;I say&rdquo;?",
         "opts": [
             "It is filler",
             "It marks the claim as made on the Buddha&rsquo;s own authority rather than left impersonal",
             "It indicates verse",
             "It signals doubt"],
         "correct": 1,
         "expl": "The canon marks claims about another being&rsquo;s condition."},
        {"q": "What complete answer do the two discourses give together?",
         "opts": [
             "Which days to observe",
             "Who is worth following &mdash; in two parts, either of which is enough to disqualify",
             "How to address a god",
             "How many gods there are"],
         "correct": 1,
         "expl": "Still defiled: sound advice, bad example. Still subject to aging and death: whatever they have does not solve that."},
        {"q": "What does the guide say about how severe that test is?",
         "opts": [
             "That it is easily met",
             "That almost nobody passes it, which is the intended effect &mdash; the canon&rsquo;s standing advice is to rely on the teaching, examine it, and keep good company",
             "That it applies only to gods",
             "That it should be relaxed for teachers"],
         "correct": 1,
         "expl": "AN 3.65 later in this collection gives the fullest statement of that advice."},
        {"q": "Why would the compilers keep two versions differing by one clause?",
         "opts": [
             "Scribal accident",
             "To pad the chapter",
             "Because the disqualification is a class of facts rather than a single fact, and two members of the class show the class",
             "Because the first version was lost"],
         "correct": 2,
         "expl": "Which is why the pair says something neither says alone."},
    ],
    marginalia=[
        ("One clause, changed", [
            "AN 3.37 &middot; not free of the three roots",
            "AN 3.38 &middot; not exempt from birth, aging, death",
            "&mdash; defilement vs. predicament",
        ]),
        ("Who Sakka is", [
            "lord of the thirty-three",
            "the most devout of the gods",
            "&mdash; and still not a destination",
        ]),
        ("The credential", [
            "<span class=\"pali\">khīṇāsava</span>defilements ended",
            "burden laid down",
            "exempt from suffering, &ldquo;I say&rdquo;",
        ]),
        ("Cross-references", [
            "AN 3.37 &middot; the first version",
            "AN 3.65 &middot; how to judge a teaching",
            "AN 3.35 &middot; what a perfected one claims",
        ]),
    ],
    further=[
        '<a href="%s/an3.38/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.37.html">AN 3.37 &middot; The Four Great Kings (1st)</a> &mdash; the first '
        "version, with the heavenly inspection that this one drops. The pair is a single lesson.",
        '<a href="an-3.65.html">AN 3.65 &middot; With the Kālāmas of Kesamutta</a> &mdash; the '
        "famous discourse later in this collection on how to judge a teaching when you cannot judge "
        "the teacher, which is the practical problem this discourse leaves you with.",
        '<a href="an-3.35.html">AN 3.35 &middot; With Hatthaka</a> &mdash; for what a perfected one '
        "does claim about their own condition, stated in the same flat third person.",
    ],
)


page(
    39, "Sukhumāla", "A Delicate Lifestyle",
    vagga=VAGGA_4,
    meta_title="AN 3.39 — A Delicate Lifestyle | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Sukhumālasutta — the "
        "Buddha's own account of the three palaces, the white parasol, and the three vanities he "
        "gave up before he left. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", "The Buddha, speaking about his own life before awakening"),
        ("Form", "An autobiographical description, three parallel reflections, a definition of three "
                 "vanities, and five closing verses"),
        ("Length", "~4 minutes to read"),
        ("Northern parallel", "The account of the Bodhisatta&rsquo;s three palaces and the three "
                              "intoxications is preserved in the Chinese Āgamas and became the basis "
                              "of the later legend of the four sights; this reading guide does not "
                              "assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the most personal discourse in "
                       "the Threes, and the plainest"),
    ],
    why=(
        "&ldquo;My lifestyle was delicate, mendicants, most delicate, extremely delicate.&rdquo; What "
        "follows is the Buddha&rsquo;s own inventory of his father&rsquo;s house: lotus ponds stocked "
        "in three colors for his benefit, sandalwood and cloth from Kāsi, a white parasol held over "
        "him night and day, three houses for three seasons. And then the reflection that ended it "
        "&mdash; not a vision, not an encounter arranged by gods, but a young man noticing that when "
        "he saw an old person he was disgusted, and that he had no standing to be."),
    guide=[
        ("The teaching in one sentence", [
            "The disgust an ordinary person feels at age, sickness, and death is a claim to be exempt "
            "from them, and nobody has that standing."]),
        ("The inventory, and why it is given", [
            "The details are specific and slightly odd, which is a mark in their favor: lotus ponds "
            "with blue water lilies in one, pink and white lotuses in another, all for one person. "
            "Sandalwood from Kāsi, and turbans, jackets, sarongs, and upper robes from Kāsi too. A "
            "white parasol held over him night and day so that <em>cold, heat, grass, dust, or "
            "damp</em> should not bother him. Three stilt longhouses for winter, summer, and the "
            "rains, and four months in one of them without coming downstairs.",
            "The purpose of the inventory is comparative. It establishes that the person about to "
            "renounce everything had a maximal amount to renounce, and it establishes that nothing "
            "in the list worked. The parasol keeps off dust; the discourse is about what it does not "
            "keep off.",
            "Two details deserve to be named rather than skated over. The musicians who entertained "
            "him were <em>none of them men</em>, and the passage about servants compares his "
            "father&rsquo;s household &mdash; where staff got fine rice with meat &mdash; against "
            "other houses where they got rough gruel with false black pepper. The first is a rich "
            "man&rsquo;s pleasure quarter described without comment; the second is a boast about "
            "generous provisioning that simultaneously records that bondservants elsewhere ate badly.",
            "Both belong to a world with slavery in it and with women as furnishing in it, and the "
            "discourse is not examining either. It is worth telling a class that plainly. What the "
            "discourse does with the household is not to defend it but to establish it as the best "
            "case, and then report that the best case failed &mdash; which is a use of the material "
            "that does not depend on approving of any of it."]),
        ("The three reflections", [
            "Each has an identical structure, and the structure is the argument. An unlearned "
            "ordinary person, <em>who is liable to grow old, not being exempt from old age</em>, sees "
            "someone else who is old and is horrified, repelled, and disgusted &mdash; "
            "<em>overlooking the fact that they themselves are in the same situation</em>. Then: "
            "since I too am liable to grow old, <em>it would not be appropriate for me</em> to be "
            "disgusted.",
            "Notice that the objection is not that disgust is unkind. The objection is that it is "
            "false. Disgust at an old person is a performance of not being one, and the performance "
            "is a lie about the performer. The word Sujato renders as &ldquo;it would not be "
            "appropriate&rdquo; is doing the work of a logical <em>therefore</em>.",
            "That matters for how the discourse reads today. A modern reader will hear the description "
            "of the old, the sick, and the dead as unkind &mdash; horrified, repelled, disgusted &mdash; "
            "and it is worth pointing out that these are the ordinary person&rsquo;s reactions being "
            "diagnosed, not the discourse&rsquo;s attitude. The whole passage exists in order to say "
            "that the reaction is unwarranted, and the reason given is not that the old deserve "
            "respect but that the person recoiling is looking at their own future."]),
        ("Three vanities", [
            "<em>Mada</em> is intoxication, and it gets rendered as vanity, pride, or conceit "
            "depending on the translator. The three are the vanity of youth, of health, and of life.",
            "They are not the same as vanity about appearance. Each is an assumed exemption: the "
            "background sense that aging happens to other people, that illness is something one "
            "recovers from as a matter of course, that death is a fact about the world rather than an "
            "appointment. The discourse is precise that these are intoxications, meaning that they "
            "distort judgment without being noticed.",
            "The consequences given are two, and the second is unexpected. Intoxicated with any of "
            "the three, an ordinary person does bad things by body, speech, and mind and is reborn "
            "badly. And then: intoxicated with youth, health, or life, <em>a mendicant disavows the "
            "training and returns to a lesser life</em>. Same intoxication, two different failures, "
            "and the monastic one is disrobing. It is the discourse&rsquo;s quiet acknowledgment that "
            "the three vanities do not stop at the monastery gate."]),
        ("What this discourse is not", [
            "This is the canonical version of the story everybody knows, and it is worth showing a "
            "class exactly how much of the familiar version is not here.",
            "There are no gods arranging encounters. There is no chariot ride outside the palace, no "
            "charioteer explaining what an old man is, no father conspiring to hide reality, no "
            "fourth sight of a serene renunciant. The Bodhisatta is not shielded from knowledge of "
            "aging: he has clearly seen old, sick, and dead people, and the discourse&rsquo;s "
            "complaint is about his reaction to them, not his ignorance of them.",
            "What is here is smaller and much more usable: a young man with everything notices that "
            "his response to other people&rsquo;s aging is disgust, works out that the response is "
            "incoherent, and loses his intoxication. The elaborate legend grew later, and it is a "
            "good legend; but it makes the turning point an accident of exposure, and the discourse "
            "makes it an act of thinking.",
            "The verses close in the first person and end the story where the legend does: <em>zeal "
            "sprang up in me as I looked to extinguishment. Now I&rsquo;m unable to indulge in "
            "sensual pleasures; there&rsquo;s no turning back.</em>"]),
        ("Using it", [
            "Read this immediately after AN 3.36. Yama&rsquo;s question to the person in hell is "
            "<em>did it not occur to you &mdash; I too am liable to grow old &mdash; I had better do "
            "good?</em> and the answer is <em>I was negligent.</em> AN 3.39 is the same question, "
            "asked in time, by somebody who answered it. Three discourses apart, in the same chapter, "
            "and almost certainly on purpose.",
            "For a class of teachers the useful frame is the diagnosis of disgust. Everyone has felt "
            "the recoil the discourse describes, in a hospital corridor or on a bus, and most people "
            "have filed it under compassion fatigue or squeamishness. This text files it under a "
            "false claim about oneself, and the reframing does more work in a lesson than any amount "
            "of exhortation to be kind."]),
    ],
    terms=[
        ("sukhumāla",
         "&ldquo;delicate, refined, softly raised&rdquo; &mdash; the word the Buddha applies to his "
         "own upbringing three times over in the opening line."),
        ("mada",
         "&ldquo;intoxication&rdquo; &mdash; rendered vanity or pride. The three are of youth, of "
         "health, and of life, and each is an assumed exemption that distorts judgment without being "
         "noticed."),
        ("assutavā puthujjana",
         "&ldquo;unlearned ordinary person&rdquo; &mdash; the canon&rsquo;s standard term for the "
         "untrained majority, used here for the one who is disgusted by age and sickness."),
        ("na kallaṁ",
         "&ldquo;it would not be appropriate&rdquo; &mdash; the pivot of all three reflections. The "
         "objection to disgust is that it is unwarranted, not that it is unkind."),
        ("sikkhaṁ paccakkhāya hīnāyāvattati",
         "&ldquo;disavows the training and returns to a lesser life&rdquo; &mdash; the formula for "
         "disrobing, named here as what the three vanities do to a monastic."),
    ],
    text_intro=(
        "The discourse in full, with its closing verses. Translation: Bhikkhu Sujato "
        "(CC0, SuttaCentral)."),
    text=[
        ("h3", "My father&rsquo;s house"),
        ("p", "&sect;1", "an3.39:1.1-1.6"),
        ("p", "&sect;2", "an3.39:2.1-2.3"),
        ("h3", "Three reflections"),
        ("p", "&sect;3", "an3.39:3.1-3.4"),
        ("p", "&sect;4", "an3.39:4.1-4.3"),
        ("p", "&sect;5", "an3.39:5.1-5.3"),
        ("h3", "Three vanities"),
        ("p", "&sect;6", "an3.39:6.1-6.8"),
        ("p", "&sect;7", "an3.39:7.1"),
        ("h3", "In verse"),
        ("p", "&sect;8&ndash;9", "an3.39:8.1-9.4"),
        ("p", "&sect;10&ndash;12", "an3.39:10.1-12.4"),
    ],
    quiz=[
        {"q": "How does the discourse open?",
         "opts": [
             "With a question from a monk",
             "With the Buddha&rsquo;s own words: &ldquo;My lifestyle was delicate, mendicants, most delicate, extremely delicate.&rdquo;",
             "With a description of hell",
             "With Sakka&rsquo;s verse"],
         "correct": 1,
         "expl": "The most personal discourse in the Threes."},
        {"q": "What is the purpose of the inventory of his father&rsquo;s house?",
         "opts": [
             "To praise his family",
             "To establish that the person about to renounce everything had a maximal amount to renounce &mdash; and that nothing in the list worked",
             "To explain his later poverty",
             "To describe royal customs"],
         "correct": 1,
         "expl": "The parasol keeps off dust; the discourse is about what it does not keep off."},
        {"q": "How does the guide treat the musicians and the passage about servants?",
         "opts": [
             "By omitting them",
             "By defending them as cultural",
             "By naming plainly that both belong to a world with slavery and with women as furnishing in it, which the discourse does not examine &mdash; while noting that its use of the household does not depend on approving of any of it",
             "By claiming they are later additions"],
         "correct": 2,
         "expl": "The household is established as the best case, and the best case failed."},
        {"q": "What is the objection to being disgusted at an old person?",
         "opts": [
             "That it is unkind",
             "That it is impolite",
             "That it is false &mdash; disgust is a performance of not being one, and the performance is a lie about the performer",
             "That the old cannot help it"],
         "correct": 2,
         "expl": "&ldquo;It would not be appropriate&rdquo; is doing the work of a logical <em>therefore</em>."},
        {"q": "Whose reactions are being described as horrified, repelled, and disgusted?",
         "opts": [
             "The discourse&rsquo;s own attitude to the old and sick",
             "The unlearned ordinary person&rsquo;s &mdash; being diagnosed, not endorsed",
             "The Buddha&rsquo;s, before awakening",
             "The gods&rsquo;"],
         "correct": 1,
         "expl": "The whole passage exists to say the reaction is unwarranted."},
        {"q": "What are the three vanities?",
         "opts": [
             "Wealth, beauty, and fame",
             "Youth, health, and life",
             "Birth, caste, and learning",
             "Strength, skill, and knowledge"],
         "correct": 1,
         "expl": "<em>Mada</em> is intoxication: each is an assumed exemption that distorts judgment without being noticed."},
        {"q": "What second consequence does the discourse name, beyond bad rebirth?",
         "opts": [
             "Illness",
             "Poverty",
             "That an intoxicated mendicant disavows the training and returns to a lesser life",
             "Loss of memory"],
         "correct": 2,
         "expl": "The discourse&rsquo;s quiet acknowledgment that the three vanities do not stop at the monastery gate."},
        {"q": "What familiar elements of the legend are absent here?",
         "opts": [
             "The three palaces",
             "The white parasol",
             "Gods arranging encounters, the chariot ride, the charioteer&rsquo;s explanations, the conspiring father, and the fourth sight of a renunciant",
             "The three vanities"],
         "correct": 2,
         "expl": "The Bodhisatta has clearly seen old, sick, and dead people; the complaint is about his reaction, not his ignorance."},
        {"q": "How does the guide contrast the legend with the discourse?",
         "opts": [
             "The legend is false and the discourse true",
             "The legend makes the turning point an accident of exposure; the discourse makes it an act of thinking",
             "They are the same story",
             "The discourse is later"],
         "correct": 1,
         "expl": "Smaller, and much more usable."},
        {"q": "Which discourse does the guide say this should be read against?",
         "opts": [
             "AN 3.36, where Yama asks the same question of someone who answered &ldquo;I was negligent&rdquo;",
             "AN 3.30, on three kinds of listener",
             "AN 3.1, on perils",
             "AN 3.21, on three individuals"],
         "correct": 0,
         "expl": "Three discourses apart, in the same chapter, and almost certainly on purpose."},
    ],
    marginalia=[
        ("The house", [
            "lotus ponds in three colors",
            "sandalwood and cloth from Kāsi",
            "a white parasol, night and day",
            "three houses, three seasons",
        ]),
        ("Three vanities", [
            "<span class=\"pali\">mada</span>intoxication",
            "of youth",
            "of health",
            "of life",
        ]),
        ("The reflection", [
            "they are disgusted",
            "overlooking that they are the same",
            "&mdash; &ldquo;it would not be appropriate for me&rdquo;",
        ]),
        ("Cross-references", [
            "AN 3.36 &middot; the question, asked too late",
            "MN 26 &middot; the going forth",
            "AN 3.35 &middot; comfort that does not reach",
        ]),
    ],
    further=[
        '<a href="%s/an3.39/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-3.36.html">AN 3.36 &middot; Messengers of the Gods</a> &mdash; the same three '
        "facts, put as an interrogation after death. Yama&rsquo;s question and the Bodhisatta&rsquo;s "
        "reflection are word for word the same thought; only the timing differs.",
        '<a href="../majjhima-nikaya/mn-026.html">MN 26 &middot; The Noble Search</a> &mdash; the '
        "Buddha&rsquo;s other first-person account of leaving home, told as a search rather than as a "
        "loss of intoxication. The two together are the canon&rsquo;s own biography, without the "
        "later legend.",
        '<a href="an-3.35.html">AN 3.35 &middot; With Hatthaka</a> &mdash; for the same argument run '
        "the other way: a fully equipped house described in loving detail, and what it fails to "
        "reach.",
    ],
)


page(
    40, "Ādhipateyya", "In Charge",
    vagga=VAGGA_4,
    meta_title="AN 3.40 — In Charge | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Ādhipateyyasutta — three "
        "things to put in charge of a life: yourself, the world, and the teaching. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", NO_SETTING),
        ("Speakers", SPEAKER),
        ("Form", "Three parallel expositions, each a reflection made in solitude, closing with four "
                 "verses"),
        ("Length", "~6 minutes to read"),
        ("Northern parallel", "The three authorities are preserved in the Chinese Āgamas and the "
                              "triad passed into East Asian usage as 自增上、世增上、法增上; this "
                              "reading guide does not assert a specific matching sutra number"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; long, highly repetitive, and the "
                       "middle section is the interesting one"),
    ],
    why=(
        "Three things can be put in charge of a life: yourself, the world, or the teaching. Each is "
        "described as a reflection made alone in a wilderness, at the root of a tree, or in an empty "
        "hut, and each ends in the same sentence about rousing energy and settling the mind. What "
        "differs is the reason that gets you there &mdash; your own purpose, the fact that others can "
        "see you, or the quality of the teaching itself. The middle one is the strangest and the most "
        "honest."),
    guide=[
        ("The teaching in one sentence", [
            "There are three things you can appeal to when nobody is making you practice, and all "
            "three end in the same place."]),
        ("What <em>ādhipateyya</em> means", [
            "The word is built from <em>adhipati</em>, an overlord or ruler. To make something "
            "<em>ādhipateyya</em> is to give it the deciding vote &mdash; to let it be the authority "
            "a decision is referred to. Sujato&rsquo;s &ldquo;putting in charge&rdquo; keeps the "
            "political flavor, which is right: the question is what governs you.",
            "East Asian Buddhism took the triad over as 自增上、世增上、法增上, and it is one of the "
            "places where the Pāli and the Chinese vocabularies line up cleanly enough that a "
            "bilingual class can hold both.",
            "All three descriptions share an opening and a closing. The opening is the practitioner "
            "alone &mdash; in a wilderness, at the root of a tree, or in an empty hut &mdash; "
            "recalling why they left home: not for a robe, almsfood, lodgings, or a better rebirth, "
            "but because they were <em>swamped by suffering, mired in suffering</em>. The closing is "
            "the resolution: energy roused and unflagging, mindfulness established and lucid, body "
            "tranquil, mind immersed in samādhi. Everything between the two is the variable."]),
        ("Self in charge", [
            "The reflection is short: I did not go forth for this; it would not be appropriate for me "
            "to seek the same sensual pleasures I abandoned, or worse.",
            "It is an appeal to consistency with one&rsquo;s own stated purpose, and it needs no "
            "witness and no doctrine. This is what the canon elsewhere calls <em>hiri</em>, the sense "
            "of shame that faces inward &mdash; the first of the two qualities AN 2.9 names as what "
            "keeps the world from dissolving.",
            "It is also the version most immediately transferable to lay life, and to work that "
            "nobody is checking. The whole of it is: remember what you said you were doing."]),
        ("The world in charge", [
            "Here the discourse becomes surprising. The reflection is that the world is large, and it "
            "contains ascetics and brahmins with psychic powers who are clairvoyant and can read "
            "minds; <em>they see far without being seen, even by those close</em>. And there are "
            "deities of the same kind. Any of them might look and think: <em>look at this gentleman; "
            "he&rsquo;s gone forth out of faith, but he&rsquo;s living mixed up with bad, unskillful "
            "qualities.</em>",
            "This is <em>ottappa</em>, prudence, the outward-facing counterpart of shame &mdash; and "
            "the discourse gives it a cosmology to work with. A reader who does not believe in "
            "mind-reading ascetics or in deities will find this section inert, and it is better to "
            "say so than to translate it into something more comfortable.",
            "But notice what the argument actually needs, which is less than it says. It needs the "
            "practitioner to abandon the assumption of privacy. The closing verse states it without "
            "any supernatural machinery at all: <em>there&rsquo;s no privacy in the world for someone "
            "who does bad deeds. You&rsquo;ll know for yourself, whether you&rsquo;ve lied or told the "
            "truth.</em> The first witness the verse names is the person themselves.",
            "There is also a sharp psychological observation buried in the verses, and it is easy to "
            "read past: <em>when you witness your good self, you despise it; while you disguise your "
            "bad self inside yourself.</em> The line describes somebody who is contemptuous of the "
            "part of them that is doing well and protective of the part that is not. Anyone who has "
            "worked with their own motivation will recognize it, and the canon states it in one "
            "sentence and moves on."]),
        ("The teaching in charge", [
            "The third reflection appeals to the quality of what is on offer: the teaching is "
            "<em>well explained by the Buddha &mdash; apparent in the present life, immediately "
            "effective, inviting inspection, relevant, so that sensible people can know it for "
            "themselves</em>. That is the standard recollection of the Dhamma, used here as a motive "
            "rather than as a devotion.",
            "And a second clause that does not usually get quoted with it: <em>I have spiritual "
            "companions who live knowing and seeing</em>. The evidence is not only the doctrine&rsquo;s "
            "elegance but the existence of people in the same community who have got somewhere with "
            "it. Given that, it would not be appropriate to live lazy and heedless.",
            "This is the version that scales best, because it does not depend on your resolve holding "
            "or on anyone watching. It depends on the material being good and on somebody nearby "
            "having demonstrated it."]),
        ("Using it", [
            "The triad is genuinely useful outside monastic life, and a class will find its own "
            "examples fast. Why does a teacher prepare a lesson properly when nobody will check? "
            "Because of what they said they were for; because someone might see; because the subject "
            "deserves it. The discourse says all three are legitimate and that they land in the same "
            "place.",
            "It is worth resisting the temptation to rank them. The text does not, and the closing "
            "verse recommends all three in one line: <em>with yourself in charge, live mindfully; "
            "with the world in charge, be alert and practice absorption; with the teaching in charge, "
            "live in line with that teaching.</em>",
            "The last verses end where the chapter began, with the messengers: <em>Māra&rsquo;s "
            "conquered; the terminator&rsquo;s overcome: one who strives reaches the end of "
            "rebirth.</em> The Devadūtavagga opened with three warnings that go unheeded and closes "
            "with three ways of getting oneself to act without being warned at all."]),
    ],
    terms=[
        ("ādhipateyya",
         "&ldquo;overlordship, being in charge&rdquo; &mdash; from <em>adhipati</em>, a ruler. To "
         "make something <em>ādhipateyya</em> is to give it the deciding vote. Taken into Chinese as "
         "增上."),
        ("attādhipateyya",
         "&ldquo;self in charge&rdquo; &mdash; the appeal to consistency with one&rsquo;s own stated "
         "purpose. Close to <em>hiri</em>, the sense of shame that faces inward."),
        ("lokādhipateyya",
         "&ldquo;the world in charge&rdquo; &mdash; the appeal to being visible to others, including "
         "those who see far without being seen. Close to <em>ottappa</em>, prudence."),
        ("dhammādhipateyya",
         "&ldquo;the teaching in charge&rdquo; &mdash; the appeal to the quality of the teaching and "
         "to companions who live knowing and seeing."),
        ("sandiṭṭhiko akāliko ehipassiko",
         "&ldquo;apparent in the present life, immediately effective, inviting inspection&rdquo; "
         "&mdash; the standard recollection of the Dhamma, used here as a motive for effort rather "
         "than as a devotional formula."),
    ],
    text_intro=(
        "The discourse in full, all three expositions and the closing verses. Translation: "
        "Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Putting oneself in charge"),
        ("p", "&sect;1", "an3.40:1.1-1.14"),
        ("h3", "Putting the world in charge"),
        ("p", "&sect;2", "an3.40:2.1-2.19"),
        ("h3", "Putting the teaching in charge"),
        ("p", "&sect;3", "an3.40:3.1-3.14"),
        ("h3", "In verse"),
        ("p", "&sect;4&ndash;5", "an3.40:4.1-5.4"),
        ("p", "&sect;6", "an3.40:6.1-6.6"),
        ("p", "&sect;7", "an3.40:7.1-7.4"),
    ],
    quiz=[
        {"q": "What does <em>ādhipateyya</em> mean?",
         "opts": [
             "&ldquo;Effort&rdquo;",
             "&ldquo;Overlordship&rdquo; &mdash; from <em>adhipati</em>, a ruler; to give something the deciding vote",
             "&ldquo;Reflection&rdquo;",
             "&ldquo;Solitude&rdquo;"],
         "correct": 1,
         "expl": "The question is what governs you. Taken into Chinese as 增上."},
        {"q": "What do all three descriptions share?",
         "opts": [
             "Nothing but the title",
             "The same opening &mdash; alone, recalling why one left home, swamped by suffering &mdash; and the same closing resolution about energy, mindfulness, tranquility, and samādhi",
             "The same speaker",
             "The same length"],
         "correct": 1,
         "expl": "Everything between the two is the variable."},
        {"q": "What is the reflection when self is in charge?",
         "opts": [
             "That others are watching",
             "That the teaching is well explained",
             "That one did not go forth for robes, almsfood, lodgings, or rebirth &mdash; so it would not be appropriate to seek the pleasures one abandoned",
             "That death is near"],
         "correct": 2,
         "expl": "An appeal to consistency with one&rsquo;s own stated purpose, needing no witness and no doctrine."},
        {"q": "Which canonical pair does the guide line the first two up with?",
         "opts": [
             "Calm and insight",
             "<em>Hiri</em> and <em>ottappa</em> &mdash; shame facing inward and prudence facing outward",
             "Faith and wisdom",
             "Giving and ethics"],
         "correct": 1,
         "expl": "AN 2.9 names them as what keeps the world from dissolving."},
        {"q": "What does the second reflection actually appeal to?",
         "opts": [
             "Public reputation only",
             "Ascetics and brahmins with psychic powers, and deities of the same kind, who see far without being seen and can read minds",
             "The monastic rule",
             "One&rsquo;s family"],
         "correct": 1,
         "expl": "This is <em>ottappa</em> given a cosmology to work with."},
        {"q": "How does the guide handle a reader who does not believe in mind-reading ascetics?",
         "opts": [
             "By translating the passage into something more comfortable",
             "By saying the section will be inert for them, and that saying so is better than softening it &mdash; while noting the argument needs less than it says",
             "By claiming the passage is a later addition",
             "By dropping the section"],
         "correct": 1,
         "expl": "What it needs is that the practitioner abandon the assumption of privacy."},
        {"q": "How does the closing verse state the same point without supernatural machinery?",
         "opts": [
             "&ldquo;The gods see everything.&rdquo;",
             "&ldquo;There&rsquo;s no privacy in the world for someone who does bad deeds. You&rsquo;ll know for yourself, whether you&rsquo;ve lied or told the truth.&rdquo;",
             "&ldquo;Nothing is hidden from the Buddha.&rdquo;",
             "&ldquo;Deeds ripen where they are done.&rdquo;"],
         "correct": 1,
         "expl": "The first witness the verse names is the person themselves."},
        {"q": "What psychological observation is buried in the verses?",
         "opts": [
             "That people forget their resolutions",
             "That people fear death",
             "That one despises one&rsquo;s good self while disguising one&rsquo;s bad self inside oneself",
             "That solitude is difficult"],
         "correct": 2,
         "expl": "Contemptuous of the part doing well, protective of the part that is not &mdash; stated in one sentence and left there."},
        {"q": "What second clause supports the third reflection, beyond the quality of the teaching?",
         "opts": [
             "That the Buddha is still alive",
             "That the monastery is well provisioned",
             "That one has spiritual companions who live knowing and seeing",
             "That the rains retreat has begun"],
         "correct": 2,
         "expl": "The evidence is not only the doctrine&rsquo;s elegance but people nearby who have got somewhere with it."},
        {"q": "Does the discourse rank the three?",
         "opts": [
             "Yes &mdash; the teaching first",
             "Yes &mdash; the self first",
             "No &mdash; and the closing verse recommends all three in a single line",
             "No &mdash; it says only one is valid"],
         "correct": 2,
         "expl": "With yourself in charge live mindfully; with the world in charge be alert; with the teaching in charge live in line with it."},
    ],
    marginalia=[
        ("Three in charge", [
            "<span class=\"pali\">atta</span>oneself &middot; 自增上",
            "<span class=\"pali\">loka</span>the world &middot; 世增上",
            "<span class=\"pali\">dhamma</span>the teaching &middot; 法增上",
        ]),
        ("Same frame each time", [
            "wilderness, tree root, empty hut",
            "&ldquo;not for a robe or almsfood&rdquo;",
            "energy, mindfulness, tranquility, samādhi",
        ]),
        ("From the verses", [
            "&ldquo;no privacy in the world&rdquo;",
            "&ldquo;you&rsquo;ll know for yourself&rdquo;",
            "&mdash; the first witness is you",
        ]),
        ("Cross-references", [
            "AN 2.1&ndash;10 &middot; conscience and prudence",
            "AN 3.36 &middot; warnings unheeded",
            "AN 3.31 &middot; the chapter&rsquo;s other duty",
        ]),
    ],
    further=[
        '<a href="%s/an3.40/en/sujato" target="_blank" rel="noopener">Full Sujato translation on '
        "SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="an-2.1-10.html">AN 2.1&ndash;10 &middot; Punishments</a> &mdash; for AN 2.9, where '
        "conscience and prudence, the inward and outward forms of shame, are named as the two bright "
        "things that keep the world from dissolving. The first two authorities here are those two "
        "qualities put to work.",
        '<a href="an-3.36.html">AN 3.36 &middot; Messengers of the Gods</a> &mdash; the discourse '
        "that opens this chapter with three warnings unheeded; this one closes it with three ways of "
        "getting oneself to act without being warned.",
        '<a href="/sutras/mohe-zhiguan/fascicle-001/">Mohe Zhiguan &middot; Fascicle 1</a> &mdash; '
        "Zhiyi on why a practitioner starts at all, which is the same question this discourse answers "
        "three ways. Useful for seeing how a Chinese master frames motivation when there is no one "
        "to compel it.",
    ],
)
