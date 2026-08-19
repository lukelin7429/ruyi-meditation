# -*- coding: utf-8 -*-
"""Cariyapitaka — The Basket of Conduct. 35 past-life verse stories, one per page."""

SC = "https://suttacentral.net"

INDEX_HEADING = "Cariyapitaka — The Basket of Conduct"
# No pre-existing pages for this collection; HEAD/TAIL both default to "./"
# until a further Khuddaka Nikāya collection module exists to hand off to.
HEAD = ("./", "Cariyapitaka selections")
TAIL = ("./", "Cariyapitaka selections")
INDEX_EXTRA = []

PAGES = []


def page(num, pali, title, **kw):
    """Shared scaffolding for a single past-life story of the Cariyapitaka."""
    d = {
        "slug": "cp-%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "source": "cp%d" % num,
        "crumb": "Cp %d" % num,
        "number_line": "Cariyapitaka &middot; Story %d" % num,
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("vagga") if "vagga" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


# --------------------------------------------------------------------------- #
# Cp 1 — Akitti Cariyā
# --------------------------------------------------------------------------- #
page(
    1, "Akitti Cariyā", "Akitti&rsquo;s Conduct",
    meta_title="Cp 1 — Akitti's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Akitti's Conduct, "
        "the Cariyapitaka's opening story of the perfection of giving — an ascetic who "
        "gives away his only food three times over. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (1st of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about one of his own past lives"),
        ("Speaker", "The Buddha, recounting his life as the ascetic Akitti"),
        ("Form", "A homage line, then ten four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "Many of the Cariyapitaka's underlying past-life stories are "
                              "also known, sometimes with variant names or details, in "
                              "other Buddhist literatures; this reading guide does not "
                              "assert a specific matching text for Akitti's story."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short and direct, "
                       "though it opens a collection built from unfamiliar names"),
    ],
    why=(
        "This is the first of the Cariyapitaka's thirty-five stories &mdash; and unlike "
        "the Jātaka tradition, which narrates the Buddha's past lives in the third person "
        "as &lsquo;the bodhisatta&rsquo;, every story here is spoken by the Buddha himself, "
        "in the first person, recounting what he did in a specific past life and why. This "
        "one is the simplest kind: an ascetic living alone in the jungle gives away his "
        "only food, plain leaves gathered without oil or salt, three times over to a "
        "disguised visitor, without complaint or hesitation."),
    guide=[
        ("Thirty-five stories, only seven perfections", [
            "The Cariyapitaka (&ldquo;Basket of Conduct&rdquo;) collects thirty-five verse "
            "stories across three chapters, each illustrating one of the "
            "<em>pāramī</em> &mdash; the &ldquo;perfections&rdquo; a bodhisatta cultivates "
            "on the way to Buddhahood. Ten stories illustrate giving, ten illustrate "
            "ethics, and the rest are divided across renunciation, resolve, truth, love, "
            "and equanimity &mdash; leaving patience, energy, and wisdom without a "
            "dedicated story of their own in this particular collection."]),
        ("A homage, then a name", [
            "The text opens with the same homage formula that opens Kp 1 of the "
            "Khuddakapatha &mdash; &lsquo;Homage to him, the blessed one...&rsquo; "
            "&mdash; before turning immediately to a specific claim: &lsquo;my name was "
            "Akitti the mortifier&rsquo;. Each of the collection's thirty-five stories "
            "will open this same way, naming who the Buddha says he once was."]),
        ("Tested three times, unmoved each time", [
            "Sakka, king of the gods, disguised as a brahmin, comes to Akitti's hut three "
            "times asking for food. Each time Akitti has nothing but plain gathered "
            "leaves, unseasoned; each time he gives them without reservation, and each "
            "time turns back to his hut having given up on finding more food for himself "
            "that day."]),
        ("A closing formula that names the point", [
            "The story ends by stating its own purpose directly: &lsquo;while giving him "
            "that gift I did not wish for fame or profit. Wishing for omniscience I "
            "performed those deeds.&rsquo; A close variant of this line will close nearly "
            "every story in the collection &mdash; each act of giving is framed "
            "explicitly as a step toward Buddhahood, not virtue for its own sake."]),
    ],
    terms=[
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories."),
        ("pāramī",
         "&ldquo;perfection&rdquo; &mdash; the quality each story illustrates; this one "
         "illustrates the first of ten, giving (<em>dāna</em>)."),
        ("bodhisatta",
         "a being on the path to Buddhahood &mdash; the role every speaker of every "
         "Cariyapitaka story claims to have occupied in that particular past life."),
        ("Sakka",
         "king of the gods, who appears across many of these stories, often in disguise, "
         "testing the bodhisatta's resolve."),
        ("tapasa",
         "&ldquo;ascetic&rdquo; or &ldquo;mortifier&rdquo; &mdash; the description "
         "attached to Akitti's name here, a forest-dwelling renunciant of no fixed "
         "affiliation."),
    ],
    text_intro=(
        "The text in full: a homage line, then ten verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp1:1.1-1.1"),
        ("p", "&sect;2", "cp1:2.1-2.4"),
        ("p", "&sect;3", "cp1:3.1-3.4"),
        ("p", "&sect;4", "cp1:4.1-4.4"),
        ("p", "&sect;5", "cp1:5.1-5.4"),
        ("p", "&sect;6", "cp1:6.1-6.4"),
        ("p", "&sect;7", "cp1:7.1-7.4"),
        ("p", "&sect;8", "cp1:8.1-8.4"),
        ("p", "&sect;9", "cp1:9.1-9.4"),
        ("p", "&sect;10", "cp1:10.1-10.4"),
        ("p", "&sect;11", "cp1:11.1-11.4"),
    ],
    quiz=[
        {"q": "How does the Cariyapitaka's narration differ from the Jātaka tradition's?",
         "opts": [
             "It is written entirely in prose",
             "It is spoken by the Buddha in the first person, not narrated in the third person as 'the bodhisatta'",
             "It names no past-life character at all",
             "It is addressed to a specific named audience"],
         "correct": 1,
         "expl": "Every Cariyapitaka story is the Buddha's own first-person account."},
        {"q": "How many of the ten traditional perfections get a dedicated story in this particular collection?",
         "opts": [
             "All ten, equally represented",
             "Seven — patience, energy, and wisdom have no dedicated story here",
             "Only one, giving",
             "None; the stories are unrelated to the perfections"],
         "correct": 1,
         "expl": "Ten stories on giving, ten on ethics, and the rest spread across five more perfections."},
        {"q": "What formula opens this text, shared with Kp 1 of the Khuddakapatha?",
         "opts": [
             "The three refuges formula",
             "'Homage to him, the blessed one, the perfected one, the fully awakened Buddha!'",
             "A dedication to a specific king",
             "The four noble truths"],
         "correct": 1,
         "expl": "A widely shared formula, not unique to either text."},
        {"q": "Who tests Akitti in this story, and how many times?",
         "opts": [
             "A hungry animal, once",
             "Sakka, disguised as a brahmin, three times",
             "A group of bandits, twice",
             "No one tests him; the story has no visitor"],
         "correct": 1,
         "expl": "Each time asking for food, each time given the same plain leaves without hesitation."},
        {"q": "What does Akitti give each time he is asked?",
         "opts": [
             "Gold and jewels he had hidden away",
             "Plain leaves gathered from the forest, without oil or salt",
             "A portion of rice and ghee",
             "Nothing; he refuses each request"],
         "correct": 1,
         "expl": "His only food, given without reservation each of the three times."},
        {"q": "What does the closing formula say Akitti's giving was NOT motivated by?",
         "opts": [
             "Fame or profit",
             "Compassion",
             "Merit",
             "Renunciation"],
         "correct": 0,
         "expl": "'I did not wish for fame or profit. Wishing for omniscience I performed those deeds.'"},
        {"q": "What does the closing formula say Akitti's giving WAS aimed at?",
         "opts": [
             "A comfortable rebirth",
             "Omniscience — a step toward Buddhahood",
             "Political power",
             "Nothing in particular; no reason is given"],
         "correct": 1,
         "expl": "A variant of this line closes nearly every story in the collection."},
        {"q": "What does 'pāramī' mean?",
         "opts": [
             "'Perfection' — the quality each Cariyapitaka story illustrates",
             "'Homage'",
             "'Renunciation'",
             "'King'"],
         "correct": 0,
         "expl": "This story illustrates the first of ten, giving (dāna)."},
        {"q": "How many stories make up the Cariyapitaka in total, and how are they organized?",
         "opts": [
             "Nine stories in one chapter",
             "Thirty-five stories across three chapters",
             "One hundred stories across ten chapters",
             "Twelve stories, one per perfection"],
         "correct": 1,
         "expl": "This story opens the first chapter, on giving."},
        {"q": "What role does Akitti occupy in this story, according to the text?",
         "opts": [
             "A king ruling a great city",
             "A forest-dwelling ascetic (tapasa)",
             "A merchant traveling by sea",
             "A young prince"],
         "correct": 1,
         "expl": "Living alone in the jungle, without possessions beyond gathered leaves."},
    ],
    marginalia=[
        ("Thirty-five stories", [
            "three chapters,",
            "seven perfections",
        ]),
        ("Spoken in the first person", [
            "the Buddha's own",
            "account of himself",
        ]),
        ("Tested three times", [
            "Sakka in disguise,",
            "the same plain leaves given",
        ]),
        ("A closing formula", [
            "'wishing for omniscience",
            "I performed those deeds'",
        ]),
    ],
    further=[
        '<a href="%s/cp1/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="../khuddakapatha/kp-1.html">Kp 1 &mdash; The Three Refuges</a> &mdash; '
        "the Khuddakapatha text that opens with the same homage formula.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 2 — Saṅkha Cariyā
# --------------------------------------------------------------------------- #
page(
    2, "Saṅkha Cariyā", "Sa&#7749;kha&rsquo;s Conduct",
    meta_title="Cp 2 — Saṅkha's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Saṅkha's Conduct, "
        "the Cariyapitaka's second story on the perfection of giving — a modest gift, "
        "reasoned into rather than simply felt. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (2nd of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as the brahmin Saṅkha, on his way to a port"),
        ("Speaker", "The Buddha, recounting his life as the brahmin Saṅkha"),
        ("Form", "Nine four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for Saṅkha's story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the two similes take "
                       "a moment to unpack"),
    ],
    why=(
        "Where Cp 1 gave away everything its speaker had, this story gives something "
        "modest &mdash; an umbrella and a pair of sandals &mdash; but spends most of its "
        "length on the reasoning behind the gift, not the gift itself. Seeing a figure "
        "described as &lsquo;self-awakened, undefeated&rsquo; walking a scorching desert "
        "road, the brahmin Saṅkha talks himself into giving using two everyday "
        "comparisons: a farmer with unsown fertile ground, and a minister who withholds "
        "gifts from the people he depends on."),
    guide=[
        ("A gift reasoned into, not simply felt", [
            "Unlike Akitti's immediate, unhesitating giving in Cp 1, this story shows its "
            "narrator working out why to give, step by step, before he acts. The verses "
            "spend more space on the reasoning than on the gift itself."]),
        ("Two similes about opportunity", [
            "A farmer who sees fertile ground and does not sow will have no need of "
            "grain &mdash; because there will be none. A minister who does not give money "
            "and grain to secure the people's favor will see his authority dwindle. Both "
            "images make the same point: an opportunity not acted on does not simply "
            "vanish neutrally, it costs something."]),
        ("A field of merit", [
            "Saṅkha applies both similes to himself directly: seeing &lsquo;an "
            "abundantly worthy recipient&rsquo; and not giving would mean he "
            "&lsquo;dwindles in merit&rsquo;, just as the farmer's ungrasped field and "
            "the minister's ungiven grain cost them what they might have gained."]),
        ("A gift out of proportion to comfort", [
            "The text closes by naming the personal cost directly: Saṅkha calls himself "
            "&lsquo;a hundred times more delicate and pampered&rsquo; than the figure he "
            "gives to &mdash; his own sandals and umbrella, given up on a road he is now "
            "left to walk without them."]),
    ],
    terms=[
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its second."),
        ("paccekabuddha",
         "an &ldquo;independently awakened&rdquo; being, awakened without a teacher but "
         "not teaching others &mdash; the standard reading of this text's description, "
         "&lsquo;self-awakened, undefeated&rsquo;."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the second "
         "of ten stories on this theme opening the collection."),
        ("khetta",
         "&ldquo;field&rdquo; &mdash; the image both of the text's similes turn on, and "
         "the word behind the common phrase &lsquo;field of merit&rsquo; for a worthy "
         "recipient of a gift."),
        ("puñña",
         "&ldquo;merit&rdquo; &mdash; what Saṅkha reasons he would &lsquo;dwindle in&rsquo; "
         "by failing to give, the direct stake of both his similes."),
    ],
    text_intro=(
        "The text in full: nine verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp2:1.1-1.4"),
        ("p", "&sect;2", "cp2:2.1-2.4"),
        ("p", "&sect;3", "cp2:3.1-3.4"),
        ("p", "&sect;4", "cp2:4.1-4.4"),
        ("p", "&sect;5", "cp2:5.1-5.4"),
        ("p", "&sect;6", "cp2:6.1-6.4"),
        ("p", "&sect;7", "cp2:7.1-7.4"),
        ("p", "&sect;8", "cp2:8.1-8.4"),
        ("p", "&sect;9", "cp2:9.1-9.4"),
    ],
    quiz=[
        {"q": "How does this story's approach to giving differ from Cp 1's?",
         "opts": [
             "It shows the reasoning behind the gift, not just immediate, unhesitating action",
             "It describes no gift at all",
             "It is narrated in the third person",
             "It involves a much larger gift than Cp 1's"],
         "correct": 0,
         "expl": "The verses spend more space on the two similes than on the gift itself."},
        {"q": "Who does Saṅkha see walking a scorching desert road?",
         "opts": [
             "A group of merchants",
             "A figure described as 'self-awakened, undefeated' — read as a paccekabuddha",
             "A king in exile",
             "His own teacher"],
         "correct": 1,
         "expl": "An independently awakened being, awakened without a teacher."},
        {"q": "What does the farmer simile say about a fertile, unsown field?",
         "opts": [
             "It will still yield grain eventually",
             "Not sowing it means having no need of grain — because there will be none",
             "The field will improve on its own without effort",
             "It is irrelevant to the story's point"],
         "correct": 1,
         "expl": "An opportunity not acted on costs something, rather than vanishing neutrally."},
        {"q": "What does the minister simile compare to withholding a gift?",
         "opts": [
             "A soldier retreating from battle",
             "A minister who withholds money and grain from the people, and so loses authority",
             "A student who refuses to study",
             "A farmer who plants too many seeds"],
         "correct": 1,
         "expl": "The same structure as the farmer simile, applied to political standing instead of a harvest."},
        {"q": "What does Saṅkha conclude he would lose by not giving to a worthy recipient?",
         "opts": [
             "Nothing; the text says giving makes no difference",
             "Merit — he would 'dwindle in merit'",
             "His position as a brahmin",
             "His ability to cross the ocean"],
         "correct": 1,
         "expl": "Applying both similes directly to his own situation."},
        {"q": "What does Saṅkha actually give?",
         "opts": [
             "His entire fortune",
             "An umbrella and a pair of sandals",
             "Food and water",
             "Nothing; he decides against giving in the end"],
         "correct": 1,
         "expl": "A modest gift, unlike Akitti's total self-giving in Cp 1."},
        {"q": "How does the text describe Saṅkha relative to the recipient of his gift?",
         "opts": [
             "Equally accustomed to hardship",
             "'A hundred times more delicate and pampered' than him",
             "Far poorer than the recipient",
             "No comparison is made"],
         "correct": 1,
         "expl": "Naming the personal cost of the gift directly in the closing verse."},
        {"q": "What was Saṅkha's stated purpose for his journey?",
         "opts": [
             "To wage war",
             "To cross the great ocean, on his way to the port",
             "To visit his family",
             "No purpose is given"],
         "correct": 1,
         "expl": "The setting for his encounter with the self-awakened figure."},
        {"q": "What perfection does this story illustrate, and where does it fall in the collection?",
         "opts": [
             "Ethics, the collection's first story",
             "Giving (dāna), the second of ten stories on this theme",
             "Truth, the final story of the collection",
             "Equanimity, the only story on this theme"],
         "correct": 1,
         "expl": "Ten stories on giving open the Cariyapitaka; this is the second."},
        {"q": "What kind of reasoning holds this story together, more than in Cp 1?",
         "opts": [
             "A legal argument about property rights",
             "Two similes about opportunity and cost — a farmer's field and a minister's favor",
             "A mathematical calculation",
             "A retelling of a dream"],
         "correct": 1,
         "expl": "The reasoning, not the gift, takes up most of the text."},
    ],
    marginalia=[
        ("Reasoned, not just felt", [
            "two similes precede",
            "the gift itself",
        ]),
        ("A field left unsown", [
            "opportunity not taken",
            "still costs something",
        ]),
        ("A modest gift", [
            "an umbrella,",
            "a pair of sandals",
        ]),
        ("Given up in comfort", [
            "'a hundred times",
            "more delicate' than the recipient",
        ]),
    ],
    further=[
        '<a href="%s/cp2/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-1.html">Cp 1 &mdash; Akitti&rsquo;s Conduct</a> &mdash; the text '
        "immediately before this one, opening the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 3 — Kururāja Cariyā
# --------------------------------------------------------------------------- #
page(
    3, "Kururāja Cariyā", "Kur&umacr;r&amacr;ja&rsquo;s Conduct",
    meta_title="Cp 3 — Kururāja's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Kururāja's "
        "Conduct, the Cariyapitaka's story of a king who gives away his prized "
        "elephant to a famine-stricken neighbor. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (3rd of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as King Dhanañjaya of Indapatta"),
        ("Speaker", "The Buddha, recounting his life as the king known as Kururāja"),
        ("Form", "Eight four-line verses of first-person narration, including two lines "
                 "of dialogue from brahmin petitioners and the king's ministers"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This narrative element &mdash; a king of the Kurus giving "
                              "away a prized elephant during a neighboring famine &mdash; "
                              "recurs in the broader Jātaka tradition; this reading guide "
                              "does not assert a specific matching text or number."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a short exchange, but "
                       "with real political stakes to follow"),
    ],
    why=(
        "This story raises the stakes beyond a private ascetic's meal or a traveler's "
        "sandals: a king gives away the royal elephant that helped secure his kingdom's "
        "fortune, over his ministers' objection, to brahmins from a country stricken by "
        "drought. Two of its verses reappear almost word for word in Cp 9's story of "
        "Vessantara &mdash; the same elephant-gift scene, replayed on a still larger "
        "stage."),
    guide=[
        ("A king known by two names", [
            "The story's title names him Kururāja, &lsquo;King of the Kurus&rsquo;, but "
            "the text itself gives his personal name as Dhanañjaya, ruling from "
            "Indapatta, and credits him with the &lsquo;ten skillful deeds&rsquo; "
            "&mdash; the traditional ten courses of wholesome conduct expected of a just "
            "ruler."]),
        ("A request driven by famine", [
            "Brahmins arrive from Kaliṅga, a neighboring realm, explaining plainly: "
            "&lsquo;our nation is suffering from drought, food is scarce and famine "
            "abounds&rsquo;, and ask for the royal elephant, auspicious and "
            "&lsquo;deemed lucky&rsquo;, by name Añjana."]),
        ("A vow not to refuse a petitioner", [
            "The king's reasoning turns on a personal standard rather than a calculation "
            "of advantage: &lsquo;when supplicants come to me it is unbefitting to "
            "refuse. Let not my vow be broken.&rsquo; The elephant is handed over with a "
            "formal water-pouring gesture, the traditional way of sealing a solemn gift."]),
        ("The ministers object, the king answers", [
            "His ministers protest that the elephant was &lsquo;supreme victor in "
            "battle&rsquo; and ask how he will now govern the realm. His answer goes "
            "further than the question: he would give away &lsquo;the entire realm and "
            "my physical body as well&rsquo;, because &lsquo;omniscience is precious to "
            "me&rsquo; &mdash; the same closing logic Cp 1's Akitti used for a much "
            "smaller gift."]),
        ("The same verses, reused in Cp 9", [
            "The stanza describing the Kaliṅga brahmins' request and the king's vow not "
            "to refuse a supplicant reappears almost unchanged in Cp 9, where Vessantara "
            "gives away the same kind of elephant under nearly identical circumstances "
            "&mdash; one of the collection's clearest examples of a shared formula "
            "carried across two different stories."]),
    ],
    terms=[
        ("dasakusalakammapatha",
         "the &ldquo;ten skillful deeds&rdquo; &mdash; the traditional standard of "
         "wholesome conduct this text credits the king with upholding."),
        ("Kururāja",
         "&ldquo;King of the Kurus&rdquo; &mdash; this story's title, though the text "
         "gives the king's personal name as Dhanañjaya."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the third "
         "of ten stories on this theme opening the collection."),
        ("udakadāna",
         "a formal gift sealed by pouring water over the recipient's hand &mdash; the "
         "gesture this text describes when the elephant changes hands."),
        ("Kaliṅga",
         "the famine-stricken neighboring realm whose brahmins travel to ask for the "
         "king's elephant."),
    ],
    text_intro=(
        "The text in full: eight verses, including the brahmins' request and the "
        "ministers' objection. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp3:1.1-1.4"),
        ("p", "&sect;2", "cp3:2.1-2.4"),
        ("p", "&sect;3", "cp3:3.1-3.4"),
        ("p", "&sect;4", "cp3:4.1-4.4"),
        ("p", "&sect;5", "cp3:5.1-5.4"),
        ("p", "&sect;6", "cp3:6.1-6.4"),
        ("p", "&sect;7", "cp3:7.1-7.4"),
        ("p", "&sect;8", "cp3:8.1-8.4"),
    ],
    quiz=[
        {"q": "What two names does this story's king go by?",
         "opts": [
             "Only one name is ever given",
             "Kururāja ('King of the Kurus') in the title, and Dhanañjaya in the text",
             "Akitti and Saṅkha",
             "Sivi and Vessantara"],
         "correct": 1,
         "expl": "The title names his kingdom's people; the text names him personally."},
        {"q": "Why do the brahmins from Kaliṅga request the royal elephant?",
         "opts": [
             "As a wedding gift for a prince",
             "Their nation is suffering drought and famine",
             "To use in a religious ceremony unrelated to famine",
             "As payment for a past debt"],
         "correct": 1,
         "expl": "They ask directly and plainly for the auspicious elephant Añjana."},
        {"q": "What personal standard drives the king's decision to give the elephant?",
         "opts": [
             "A calculation of military advantage",
             "A vow not to refuse a supplicant who comes to him",
             "Pressure from his ministers",
             "A prophecy he received in a dream"],
         "correct": 1,
         "expl": "'When supplicants come to me it is unbefitting to refuse. Let not my vow be broken.'"},
        {"q": "What gesture seals the gift of the elephant?",
         "opts": [
             "A written contract",
             "Pouring water over the recipients' hand",
             "A public parade through the city",
             "No formal gesture is described"],
         "correct": 1,
         "expl": "The traditional way of sealing a solemn gift."},
        {"q": "What do the king's ministers object to?",
         "opts": [
             "The gift going to the wrong recipients",
             "Losing an elephant that was 'supreme victor in battle', asking how he will now govern",
             "The cost of the water-pouring ceremony",
             "Nothing; no minister raises an objection"],
         "correct": 1,
         "expl": "A military and political concern about the kingdom's defense."},
        {"q": "How does the king answer his ministers' objection?",
         "opts": [
             "He apologizes and admits it was a mistake",
             "He says he would give away the entire realm and his own body too, for omniscience",
             "He orders the elephant returned",
             "He blames the brahmins for asking"],
         "correct": 1,
         "expl": "The same 'omniscience is precious to me' logic used in Cp 1."},
        {"q": "What connects this story directly to Cp 9's Vessantara?",
         "opts": [
             "Nothing; the two stories share no textual connection",
             "A near-identical stanza about the elephant-gift request and the king's vow reappears in both",
             "They are both narrated in the third person",
             "Both stories end with the elephant being refused"],
         "correct": 1,
         "expl": "One of the collection's clearest examples of a formula shared across stories."},
        {"q": "What does 'dasakusalakammapatha' refer to?",
         "opts": [
             "A specific type of elephant",
             "The traditional ten courses of wholesome conduct expected of a just ruler",
             "A ceremony performed only at a king's coronation",
             "The name of the king's capital city"],
         "correct": 1,
         "expl": "Credited to the king at the story's opening."},
        {"q": "Where is the king's capital, as named in this text?",
         "opts": [
             "Indapatta",
             "Sāvatthī",
             "Rājagaha",
             "Kapilavatthu"],
         "correct": 0,
         "expl": "Named in the opening verse."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Giving (dāna), the third of ten stories on this theme",
             "Truth",
             "Equanimity"],
         "correct": 1,
         "expl": "Continuing the sequence of ten giving-stories opening the collection."},
    ],
    marginalia=[
        ("A king, two names", [
            "Kururāja in title,",
            "Dhanañjaya in the text",
        ]),
        ("A vow not to refuse", [
            "any supplicant",
            "who comes to him",
        ]),
        ("Ministers object", [
            "a war-elephant lost —",
            "how to govern now?",
        ]),
        ("Echoed again in Cp 9", [
            "the same verses,",
            "Vessantara's larger gift",
        ]),
    ],
    further=[
        '<a href="%s/cp3/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-2.html">Cp 2 &mdash; Sa&#7749;kha&rsquo;s Conduct</a> &mdash; the text '
        "immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 4 — Mahāsudassana Cariyā
# --------------------------------------------------------------------------- #
page(
    4, "Mah&amacr;sudassana Cariy&amacr;", "Mah&amacr;sudassana&rsquo;s Conduct",
    meta_title="Cp 4 — Mahāsudassana's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Mahāsudassana's "
        "Conduct, the Cariyapitaka's story of a wheel-turning monarch who proclaims "
        "his generosity aloud, three times a day. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (4th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as King Mahāsudassana of Kusāvatī"),
        ("Speaker", "The Buddha, recounting his life as the wheel-turning monarch "
                    "Mahāsudassana"),
        ("Form", "Nine verses of first-person narration, including a repeated public "
                 "proclamation"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "A King Mahāsudassana is also the subject of a much longer "
                              "canonical discourse, the Mahāsudassana Sutta, not otherwise "
                              "covered on this site; this reading guide does not assert a "
                              "further specific matching text beyond that."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; plain narration, "
                       "built around one repeated proclamation"),
    ],
    why=(
        "Where Cp 1&ndash;3 all show giving in response to someone arriving and asking, "
        "this story shows a king who does not wait to be asked. Three times a day, "
        "Mahāsudassana has it proclaimed throughout his realm &mdash; &lsquo;who needs "
        "what? who wants what?&rsquo; &mdash; and keeps riches prepared in hundreds of "
        "places so that anyone in need can simply come and take what they require."),
    guide=[
        ("Giving sought out, not waited for", [
            "Akitti gave to a visitor at his door; Saṅkha gave to someone he happened to "
            "pass on the road; the king of Cp 3 gave to petitioners who came asking. Here, "
            "the king takes the initiative himself, proclaiming his willingness to give "
            "before anyone has asked for anything."]),
        ("A proclamation repeated daily", [
            "The text quotes the proclamation directly &mdash; &lsquo;who needs an "
            "umbrella? who is thirsty? who a garland? who some makeup?&rsquo; &mdash; a "
            "list of ordinary, unglamorous needs, made public morning and night, &lsquo;not "
            "just in ten places, or even a hundred, but in many hundreds of places&rsquo;."]),
        ("A doctor's fee, reframed", [
            "The king explains his motive with an everyday comparison: someone who is "
            "sick pays a doctor and becomes well again. In the same way, he gives &lsquo;in "
            "order to fulfill without remainder, to fulfill what is lacking&rsquo; &mdash; "
            "giving treated as a remedy applied toward a specific, considered goal rather "
            "than an occasional gesture."]),
        ("A goal named directly at the close", [
            "The story ends without ambiguity about what that goal is: he gave "
            "&lsquo;without clinging or reward, for the attainment of awakening&rsquo; "
            "&mdash; the same destination every story in this chapter has been driving "
            "toward, reached here through sustained, organized generosity rather than a "
            "single dramatic act."]),
    ],
    terms=[
        ("cakkavatti",
         "&ldquo;wheel-turning monarch&rdquo; &mdash; the traditional title for an ideal "
         "ruler of great power and territory, applied to Mahāsudassana in this text."),
        ("Kusāvatī",
         "the capital city from which Mahāsudassana is said to have ruled."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the fourth "
         "of ten stories on this theme opening the collection."),
        ("Mahāsudassana Sutta",
         "a much longer canonical discourse about the same King Mahāsudassana, not "
         "otherwise covered on this site."),
        ("bodhi",
         "&ldquo;awakening&rdquo; &mdash; named directly as the goal of the king's "
         "giving in the story's closing verse."),
    ],
    text_intro=(
        "The text in full: nine verses, including the king's repeated public "
        "proclamation. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp4:1.1-1.4"),
        ("p", "&sect;2", "cp4:2.1-2.4"),
        ("p", "&sect;3", "cp4:3.1-3.4"),
        ("p", "&sect;4", "cp4:4.1-4.4"),
        ("p", "&sect;5", "cp4:5.1-5.4"),
        ("p", "&sect;6", "cp4:6.1-6.4"),
        ("p", "&sect;7", "cp4:7.1-7.4"),
        ("p", "&sect;8", "cp4:8.1-8.4"),
        ("p", "&sect;9", "cp4:9.1-9.6"),
    ],
    quiz=[
        {"q": "How does this story's giving differ from Cp 1–3's?",
         "opts": [
             "It is the same pattern exactly — giving only in response to a visitor",
             "The king proactively proclaims his willingness to give, rather than waiting to be asked",
             "No giving takes place in this story",
             "It describes giving only to family members"],
         "correct": 1,
         "expl": "Three times a day, before anyone has asked for anything."},
        {"q": "How often is the king's proclamation made, and how widely?",
         "opts": [
             "Once a year, in the capital only",
             "Three times a day, in many hundreds of places",
             "Only once, at the start of his reign",
             "Every hour, but only within the palace"],
         "correct": 1,
         "expl": "Morning and night, not just in ten or a hundred places."},
        {"q": "What kinds of needs does the proclamation list?",
         "opts": [
             "Only requests for gold and jewels",
             "Ordinary, unglamorous needs — an umbrella, sandals, a garland, makeup",
             "Only military supplies",
             "No specific needs are listed"],
         "correct": 1,
         "expl": "Everyday items, made available broadly."},
        {"q": "What simile does the king use to explain his motive for giving?",
         "opts": [
             "A farmer sowing a field",
             "A sick person paying a doctor to become well again",
             "A soldier defending a city",
             "A merchant investing in trade goods"],
         "correct": 1,
         "expl": "Giving reframed as a remedy applied toward a specific goal."},
        {"q": "What does the king say his giving was NOT motivated by?",
         "opts": [
             "Disliking riches, or having a store set aside unused",
             "Compassion",
             "A promise to his ministers",
             "Fear of losing his throne"],
         "correct": 0,
         "expl": "He explicitly denies these as his reasons."},
        {"q": "What does the story's closing verse name as the goal of the king's giving?",
         "opts": [
             "A peaceful reign",
             "The attainment of awakening",
             "Popularity among his subjects",
             "Wealth in a future life"],
         "correct": 1,
         "expl": "'Gave gifts to supplicants without clinging or reward, for the attainment of awakening.'"},
        {"q": "What title is given to Mahāsudassana in this text?",
         "opts": [
             "A humble farmer",
             "A wheel-turning monarch (cakkavatti)",
             "A wandering ascetic",
             "A high priest"],
         "correct": 1,
         "expl": "An ideal ruler of great power and territory."},
        {"q": "What is Mahāsudassana's capital city, as named in this text?",
         "opts": [
             "Indapatta",
             "Kusāvatī",
             "Sāvatthī",
             "Jetuttara"],
         "correct": 1,
         "expl": "Where he is said to have ruled."},
        {"q": "What longer canonical discourse also features a King Mahāsudassana?",
         "opts": [
             "No other text mentions this figure",
             "The Mahāsudassana Sutta",
             "The Mangala Sutta",
             "The Metta Sutta"],
         "correct": 1,
         "expl": "Not otherwise covered on this site."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Truth",
             "Giving (dāna), the fourth of ten stories on this theme",
             "Renunciation",
             "Equanimity"],
         "correct": 1,
         "expl": "Continuing the sequence of ten giving-stories opening the collection."},
    ],
    marginalia=[
        ("Giving sought out", [
            "proclaimed aloud,",
            "not waited for",
        ]),
        ("Thrice a day", [
            "'who needs what?",
            "who wants what?'",
        ]),
        ("A doctor's fee", [
            "giving as remedy,",
            "not gesture",
        ]),
        ("A named goal", [
            "'for the attainment",
            "of awakening'",
        ]),
    ],
    further=[
        '<a href="%s/cp4/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-3.html">Cp 3 &mdash; Kur&umacr;r&amacr;ja&rsquo;s Conduct</a> &mdash; '
        "the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 5 — Mahāgovinda Cariyā
# --------------------------------------------------------------------------- #
page(
    5, "Mah&amacr;govinda Cariy&amacr;", "Mah&amacr;govinda&rsquo;s Conduct",
    meta_title="Cp 5 — Mahāgovinda's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Mahāgovinda's "
        "Conduct, the Cariyapitaka's shortest giving-story — a royal chaplain who gives "
        "away tribute from seven kingdoms. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (5th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as the brahmin Mahāgovinda"),
        ("Speaker", "The Buddha, recounting his life as high priest to seven kings"),
        ("Form", "Three four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "A brahmin named Mahāgovinda is also the central figure of "
                              "a much longer canonical discourse, the Mahāgovinda Sutta, "
                              "not otherwise covered on this site; this reading guide "
                              "does not assert a further specific matching text."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; the shortest of the "
                       "collection's giving-stories, direct and uncomplicated"),
    ],
    why=(
        "At three verses, this is the shortest of the Cariyapitaka's ten stories on "
        "giving &mdash; a brahmin who served as high priest to seven kings at once takes "
        "the tribute he collects from all seven kingdoms and gives it away, described as "
        "&lsquo;a great gift unwavering as the ocean&rsquo;. What the story lacks in "
        "incident, it makes up for in directness about motive."),
    guide=[
        ("A position of unusual reach", [
            "Serving as high priest to seven kings at once gave Mahāgovinda access to "
            "tribute from all seven kingdoms combined &mdash; not wealth he earned "
            "directly, but wealth that passed through his hands by virtue of his office, "
            "which he chose to redirect rather than keep."]),
        ("An image of steadiness", [
            "The gift is described as &lsquo;unwavering as the ocean&rsquo; &mdash; not a "
            "single dramatic act but something sustained and continuous, matching the "
            "story's brevity: three verses is enough to state the pattern without needing "
            "to narrate individual instances of it."]),
        ("The same denial, the same reason", [
            "As in Cp 4, the story explicitly rules out one possible motive before naming "
            "the real one: &lsquo;it was not because I disliked riches or grain, or "
            "because I had a store set aside&rsquo;, but &lsquo;because omniscience is "
            "precious to me&rsquo;. This exact denial-then-reason structure recurs across "
            "several of the collection's giving-stories, not just this one."]),
        ("A recognizable name, a different text", [
            "A brahmin named Mahāgovinda is the central figure of a much longer canonical "
            "discourse in its own right, the Mahāgovinda Sutta &mdash; not covered on "
            "this site, but worth knowing this story shares its central figure with a "
            "text well beyond the Cariyapitaka's few verses."]),
    ],
    terms=[
        ("purohita",
         "&ldquo;royal chaplain&rdquo; or &ldquo;high priest&rdquo; &mdash; the office "
         "this text describes Mahāgovinda holding, for seven kings simultaneously."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the fifth "
         "of ten stories on this theme opening the collection."),
        ("Mahāgovinda Sutta",
         "a much longer canonical discourse centered on a brahmin of the same name, not "
         "otherwise covered on this site."),
        ("bali",
         "&ldquo;tribute&rdquo; &mdash; what Mahāgovinda is described as receiving from "
         "all seven kingdoms he served, before giving it away."),
        ("sabbaññutā",
         "&ldquo;omniscience&rdquo; &mdash; named directly as Mahāgovinda's reason for "
         "giving, the same term closing several of this chapter's other stories."),
    ],
    text_intro=(
        "The text in full: three verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp5:1.1-1.4"),
        ("p", "&sect;2", "cp5:2.1-2.4"),
        ("p", "&sect;3", "cp5:3.1-3.4"),
    ],
    quiz=[
        {"q": "What office did Mahāgovinda hold, according to this text?",
         "opts": [
             "King of a single realm",
             "High priest (purohita) to seven kings at once",
             "A wandering ascetic with no fixed position",
             "A merchant trading between kingdoms"],
         "correct": 1,
         "expl": "Giving him access to tribute from all seven kingdoms combined."},
        {"q": "Where did the wealth Mahāgovinda gave away come from?",
         "opts": [
             "His personal inheritance",
             "Tribute collected from the seven kingdoms he served",
             "Gambling winnings",
             "A gift from Sakka"],
         "correct": 1,
         "expl": "Wealth that passed through his hands by virtue of his office."},
        {"q": "How is the gift itself described?",
         "opts": [
             "As a single dramatic, one-time act",
             "As 'a great gift unwavering as the ocean' — sustained and continuous",
             "As reluctant and given only under pressure",
             "As small and infrequent"],
         "correct": 1,
         "expl": "Matching the story's brevity — a pattern stated rather than individual instances narrated."},
        {"q": "What does the story explicitly deny as Mahāgovinda's motive?",
         "opts": [
             "Compassion for the poor",
             "Disliking riches or grain, or having an unused store set aside",
             "A promise made to the kings he served",
             "Nothing is denied; only one motive is ever stated"],
         "correct": 1,
         "expl": "The same denial-then-reason structure recurs across several of the chapter's stories."},
        {"q": "What reason does the text give instead?",
         "opts": [
             "Political ambition",
             "Because omniscience is precious to him",
             "Fear of the kings he served",
             "A desire for fame"],
         "correct": 1,
         "expl": "The same closing logic used throughout this chapter's giving-stories."},
        {"q": "How long is this story compared to others in the same chapter?",
         "opts": [
             "The longest in the chapter",
             "The shortest of the ten giving-stories, at three verses",
             "Exactly the same length as every other story",
             "Twice the length of Cp 1"],
         "correct": 1,
         "expl": "Brief, but direct about motive."},
        {"q": "What longer canonical text features a brahmin named Mahāgovinda?",
         "opts": [
             "No other text mentions this name",
             "The Mahāgovinda Sutta",
             "The Mahāsudassana Sutta",
             "The Ratana Sutta"],
         "correct": 1,
         "expl": "Not otherwise covered on this site, but sharing this story's central figure."},
        {"q": "What does 'purohita' mean?",
         "opts": [
             "'Wheel-turning monarch'",
             "'Royal chaplain' or 'high priest'",
             "'Ascetic'",
             "'Merchant'"],
         "correct": 1,
         "expl": "The office Mahāgovinda held for seven kings at once."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Giving (dāna), the fifth of ten stories on this theme",
             "Truth",
             "Love"],
         "correct": 1,
         "expl": "Continuing the sequence of ten giving-stories opening the collection."},
        {"q": "What kind of narration does this story use?",
         "opts": [
             "Third-person narration about 'the bodhisatta'",
             "First-person narration, spoken by the Buddha about his own past life",
             "A dialogue between two unnamed speakers",
             "A list with no narration at all"],
         "correct": 1,
         "expl": "Consistent with every other story in the Cariyapitaka."},
    ],
    marginalia=[
        ("Priest to seven kings", [
            "tribute from all,",
            "given away entirely",
        ]),
        ("Unwavering as the ocean", [
            "a sustained gift,",
            "not a single act",
        ]),
        ("Denial, then reason", [
            "not dislike of riches —",
            "omniscience is precious",
        ]),
        ("The collection's shortest", [
            "three verses,",
            "direct about motive",
        ]),
    ],
    further=[
        '<a href="%s/cp5/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-4.html">Cp 4 &mdash; Mah&amacr;sudassana&rsquo;s Conduct</a> &mdash; '
        "the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 6 — Nimi Cariyā
# --------------------------------------------------------------------------- #
page(
    6, "Nimi Cariy&amacr;", "King Nimi&rsquo;s Conduct",
    meta_title="Cp 6 — King Nimi's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for King Nimi's "
        "Conduct, the Cariyapitaka's story of a king who builds four public halls to "
        "give to beasts, birds, and people alike. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (6th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as King Nimi of Mithilā"),
        ("Speaker", "The Buddha, recounting his life as the astute King Nimi"),
        ("Form", "Five four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "A King Nemi (Nimi) is the subject of his own jātaka "
                              "traditionally counted among the last ten jātakas widely "
                              "depicted in Southeast Asian Buddhist art and literature; "
                              "this reading guide does not assert further specific "
                              "correspondences beyond that general association."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, but its scope "
                       "of giving is unusually wide"),
    ],
    why=(
        "This story widens who counts as a recipient. King Nimi builds four public "
        "halls, each with four openings, and stocks them with clothing, bedding, food, "
        "and drink &mdash; not for one class of visitor but explicitly &lsquo;for beasts, "
        "birds, men, and so forth&rsquo;, a scope broader than any of the giving-stories "
        "before it in this chapter."),
    guide=[
        ("Four halls, four openings", [
            "Rather than waiting at his own door or proclaiming needs aloud, Nimi builds "
            "dedicated public infrastructure &mdash; four halls, each open on four sides, "
            "so that whoever approaches from any direction can reach the goods kept "
            "there."]),
        ("Beasts, birds, and people together", [
            "The recipients named are not limited to human supplicants: the text "
            "specifies &lsquo;beasts, birds, men, and so forth&rsquo;, extending the "
            "scope of giving beyond any single earlier story in this chapter."]),
        ("A servant's diligence, redirected", [
            "The closing simile compares Nimi's effort to a servant working to earn a "
            "raise from their employer, applying full effort &lsquo;by body, speech, and "
            "mind&rsquo; &mdash; the same diligence, the text suggests, but aimed at "
            "&lsquo;the wisdom born of awakening&rsquo; rather than an employer's favor."]),
        ("A recognizable name from a wider tradition", [
            "A King Nemi (Nimi) is the central figure of his own jātaka, traditionally "
            "counted among a well-known set of the last ten jātakas depicted across "
            "Southeast Asian Buddhist temple art and literature &mdash; a sign that this "
            "brief Cariyapitaka verse draws on a story with a much fuller life outside "
            "this collection."]),
    ],
    terms=[
        ("Mithilā",
         "the capital city from which King Nimi is said to have ruled."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the sixth "
         "of ten stories on this theme opening the collection."),
        ("sāla",
         "&ldquo;hall&rdquo; &mdash; the four public structures this text describes Nimi "
         "having built, each open on four sides."),
        ("bodhi",
         "&ldquo;awakening&rdquo; &mdash; named as the goal of Nimi's giving in the "
         "story's closing simile, comparing his effort to a servant's diligence."),
        ("Nemi Jātaka",
         "the fuller story of King Nemi (Nimi), traditionally counted among a "
         "well-known set of the last ten jātakas."),
    ],
    text_intro=(
        "The text in full: five verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp6:1.1-1.4"),
        ("p", "&sect;2", "cp6:2.1-2.4"),
        ("p", "&sect;3", "cp6:3.1-3.4"),
        ("p", "&sect;4", "cp6:4.1-4.4"),
        ("p", "&sect;5", "cp6:5.1-5.4"),
    ],
    quiz=[
        {"q": "What did King Nimi build to support his giving?",
         "opts": [
             "A single treasury in the palace basement",
             "Four public halls, each with four openings",
             "A network of roads",
             "Nothing; he gave directly from his own hands only"],
         "correct": 1,
         "expl": "Open on all sides, so approach was possible from any direction."},
        {"q": "Who does the text name as recipients of Nimi's giving?",
         "opts": [
             "Only brahmins and ascetics",
             "'Beasts, birds, men, and so forth' — a notably wide scope",
             "Only members of the royal court",
             "Only his own family"],
         "correct": 1,
         "expl": "Broader than any single earlier story in this chapter."},
        {"q": "What kinds of goods were provided at Nimi's four halls?",
         "opts": [
             "Only gold and jewels",
             "Clothing, bedding, food, and drink",
             "Weapons and armor",
             "Nothing physical, only blessings"],
         "correct": 1,
         "expl": "Practical necessities, provided without let."},
        {"q": "What simile closes this story?",
         "opts": [
             "A farmer and an unsown field",
             "A servant working diligently to earn a raise from their employer",
             "A doctor treating a sick patient",
             "A merchant investing in trade"],
         "correct": 1,
         "expl": "Full effort by body, speech, and mind, redirected toward awakening."},
        {"q": "What does the closing simile say Nimi's effort was aimed at, unlike a servant's?",
         "opts": [
             "An employer's favor",
             "The wisdom born of awakening",
             "A larger kingdom",
             "Popularity among his subjects"],
         "correct": 1,
         "expl": "The same diligence, redirected toward a different goal."},
        {"q": "What tradition is King Nemi (Nimi) associated with, beyond this short text?",
         "opts": [
             "No other tradition mentions this figure",
             "A jātaka of his own, among a well-known set of the last ten jātakas",
             "A canonical discourse addressed to King Pasenadi",
             "A Vinaya rule specific to kings"],
         "correct": 1,
         "expl": "Widely depicted in Southeast Asian Buddhist temple art and literature."},
        {"q": "What is King Nimi's capital city, as named in this text?",
         "opts": [
             "Indapatta",
             "Mithilā",
             "Kusāvatī",
             "Jetuttara"],
         "correct": 1,
         "expl": "Where he is said to have ruled."},
        {"q": "How does this story's scope of giving compare to the stories before it?",
         "opts": [
             "Narrower — only for the king's own family",
             "Wider — explicitly including animals, not only human recipients",
             "Identical in every respect",
             "This story describes no giving at all"],
         "correct": 1,
         "expl": "The first story in this chapter to explicitly include beasts and birds."},
        {"q": "What does 'sāla' mean, as used in this text?",
         "opts": [
             "'Hall' — the four structures Nimi built for giving",
             "'King'",
             "'Servant'",
             "'Awakening'"],
         "correct": 0,
         "expl": "Each open on four sides."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Renunciation",
             "Giving (dāna), the sixth of ten stories on this theme",
             "Resolve",
             "Truth"],
         "correct": 1,
         "expl": "Continuing the sequence of ten giving-stories opening the collection."},
    ],
    marginalia=[
        ("Four halls, four sides", [
            "open to all",
            "who approach",
        ]),
        ("Beasts, birds, and people", [
            "a wider scope",
            "than earlier stories",
        ]),
        ("A servant's diligence", [
            "redirected toward",
            "the wisdom of awakening",
        ]),
        ("A figure from a wider tradition", [
            "one of the last",
            "ten jātakas",
        ]),
    ],
    further=[
        '<a href="%s/cp6/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-5.html">Cp 5 &mdash; Mah&amacr;govinda&rsquo;s Conduct</a> &mdash; the '
        "text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 7 — Canda-Kumāra Cariyā
# --------------------------------------------------------------------------- #
page(
    7, "Canda-Kum&amacr;ra Cariy&amacr;", "Prince Candana&rsquo;s Conduct",
    meta_title="Cp 7 — Prince Candana's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Prince Candana's "
        "Conduct, the Cariyapitaka's story of a narrow escape from sacrifice that turns "
        "into a fast and an offering. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (7th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as Prince Candana, son of the One King, in the "
                    "city of Pupphavatī"),
        ("Speaker", "The Buddha, recounting his life as Prince Candana"),
        ("Form", "Six four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; the opening premise, "
                       "a narrow escape from sacrifice, is stated but not elaborated"),
    ],
    why=(
        "This story opens with the sparest possible account of a crisis: &lsquo;released "
        "from being sacrificed, I fled the sacrificial enclosure.&rsquo; The text gives "
        "no further detail about what led to that moment &mdash; only what came after it, "
        "when the prince, moved by a sudden sense of urgency, fasted for five or six "
        "days before offering the first food to a worthy recipient rather than eating it "
        "himself."),
    guide=[
        ("A crisis stated, not explained", [
            "The text names the prince's near-sacrifice and escape in a single line, "
            "without narrating how it came about or was resolved. What matters for this "
            "story is not the crisis itself but what the prince did once he was free of "
            "it."]),
        ("A sense of urgency, acted on immediately", [
            "&lsquo;Giving rise to a sense of urgency&rsquo; &mdash; a specific term, "
            "<em>saṃvega</em>, for the shock that turns a brush with mortality into "
            "spiritual motivation &mdash; the prince responds not with relief alone but "
            "with a fast of five or six days, offering the first food to a worthy "
            "recipient before touching any himself."]),
        ("A merchant's calculation, applied to giving", [
            "The closing simile compares this to a merchant who takes stored goods to "
            "wherever they will fetch the greatest profit: giving away what one would "
            "otherwise use for oneself, the text argues, is exactly this kind of "
            "calculated, understood investment &mdash; &lsquo;what is given to others "
            "multiplies a hundredfold&rsquo;."]),
        ("A single act, repeated as a stated principle", [
            "The story closes by generalizing beyond this one fast: &lsquo;knowing the "
            "reason for this, I gave gifts in life after life&rsquo; &mdash; presenting "
            "this particular act of restraint as evidence for a rule the prince then "
            "applied consistently, not a one-time response to crisis."]),
    ],
    terms=[
        ("saṃvega",
         "a sudden &ldquo;sense of urgency&rdquo; &mdash; the specific reaction named in "
         "this text as what turned the prince's escape into a fast and an offering."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the seventh "
         "of ten stories on this theme opening the collection."),
        ("Pupphavatī",
         "&ldquo;the city of flowers&rdquo; &mdash; the capital named as Prince "
         "Candana's home in this text."),
        ("yañña",
         "&ldquo;sacrifice&rdquo; or &ldquo;offering&rdquo; &mdash; the word behind both "
         "the &lsquo;sacrificial enclosure&rsquo; the prince flees and the &lsquo;great "
         "offering&rsquo; he then performs, a deliberate echo across the story."),
        ("puñña",
         "&ldquo;merit&rdquo; &mdash; what the closing simile says multiplies a "
         "hundredfold when what is given was something the giver would otherwise have "
         "used."),
    ],
    text_intro=(
        "The text in full: six verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp7:1.1-1.4"),
        ("p", "&sect;2", "cp7:2.1-2.4"),
        ("p", "&sect;3", "cp7:3.1-3.4"),
        ("p", "&sect;4", "cp7:4.1-4.4"),
        ("p", "&sect;5", "cp7:5.1-5.4"),
        ("p", "&sect;6", "cp7:6.1-6.4"),
    ],
    quiz=[
        {"q": "How much detail does the text give about the prince's near-sacrifice?",
         "opts": [
             "A long, detailed narrative spanning several verses",
             "A single line, naming it but not explaining how it came about",
             "None at all; the sacrifice is never mentioned",
             "A full dialogue between the prince and his father"],
         "correct": 1,
         "expl": "What matters for the story is what came after, not the crisis itself."},
        {"q": "What does the prince do immediately after fleeing the sacrificial enclosure?",
         "opts": [
             "Returns home and resumes his former life unchanged",
             "Gives rise to a sense of urgency (saṃvega) and performs a great offering",
             "Seeks revenge against those who intended to sacrifice him",
             "Flees the country entirely"],
         "correct": 1,
         "expl": "A specific term for the shock that turns crisis into spiritual motivation."},
        {"q": "How long does the prince fast, and what does he do with the first food afterward?",
         "opts": [
             "He fasts one day and eats immediately after",
             "He fasts five or six days, then offers the first food to a worthy recipient before eating any himself",
             "He never fasts at all",
             "He fasts for a full year"],
         "correct": 1,
         "expl": "Giving before receiving, even after an extended fast."},
        {"q": "What simile does the story use to explain the value of this kind of giving?",
         "opts": [
             "A farmer and an unsown field",
             "A merchant taking stored goods to where they will fetch the greatest profit",
             "A doctor treating a patient",
             "A servant seeking a raise"],
         "correct": 1,
         "expl": "Giving what one would otherwise use is presented as a kind of calculated investment."},
        {"q": "According to the closing simile, what happens to what is given to others?",
         "opts": [
             "It is simply lost to the giver",
             "It multiplies a hundredfold",
             "It returns to the giver unchanged",
             "Nothing is said about its effect"],
         "correct": 1,
         "expl": "The direct payoff of the merchant comparison."},
        {"q": "How does the story generalize beyond this single act of fasting and giving?",
         "opts": [
             "It does not generalize; the story ends with the single act",
             "The prince states he then gave gifts 'in life after life', applying the lesson consistently",
             "It claims this was the only time he ever gave anything",
             "It shifts to describing a completely different character"],
         "correct": 1,
         "expl": "Presenting the fast as evidence for a rule, not a one-time crisis response."},
        {"q": "What does 'saṃvega' name in this text?",
         "opts": [
             "A formal title of nobility",
             "A sudden sense of urgency, prompted by the brush with sacrifice",
             "A type of religious offering",
             "The name of the prince's father"],
         "correct": 1,
         "expl": "What turns the prince's escape into spiritual motivation."},
        {"q": "What is Prince Candana's home city, as named in this text?",
         "opts": [
             "Mithilā",
             "Pupphavatī, 'the city of flowers'",
             "Indapatta",
             "Kusāvatī"],
         "correct": 1,
         "expl": "Where he is named as the true-born son of the One King."},
        {"q": "What word does the text use for both the sacrifice the prince flees and the offering he then performs?",
         "opts": [
             "Two entirely unrelated words are used",
             "The same underlying word, 'yañña' — sacrifice or offering",
             "'Dāna' is used for both",
             "No word is repeated between the two"],
         "correct": 1,
         "expl": "A deliberate echo connecting the crisis to the response."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Truth",
             "Giving (dāna), the seventh of ten stories on this theme",
             "Equanimity",
             "Love"],
         "correct": 1,
         "expl": "Continuing the sequence of ten giving-stories opening the collection."},
    ],
    marginalia=[
        ("A crisis, unexplained", [
            "'released from",
            "being sacrificed'",
        ]),
        ("A sudden urgency", [
            "saṃvega, acted on",
            "immediately",
        ]),
        ("Fasting, then giving first", [
            "five or six days,",
            "offered before eaten",
        ]),
        ("A merchant's calculation", [
            "what is given",
            "multiplies a hundredfold",
        ]),
    ],
    further=[
        '<a href="%s/cp7/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-6.html">Cp 6 &mdash; King Nimi&rsquo;s Conduct</a> &mdash; the text '
        "immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 8 — Sivi Cariyā
# --------------------------------------------------------------------------- #
page(
    8, "Sivi Cariy&amacr;", "King Sivi&rsquo;s Conduct",
    meta_title="Cp 8 — King Sivi's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for King Sivi's "
        "Conduct, the Cariyapitaka's best-known giving-story — a king tested by Sakka, "
        "who gives away both his own eyes. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (8th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as King Sivi of Ariṭṭha"),
        ("Speaker", "The Buddha, recounting his life as King Sivi, with two further "
                    "voices quoted in dialogue: Sakka, and the disguised beggar Sakka "
                    "becomes"),
        ("Form", "Sixteen four-line verses of first-person narration and quoted "
                 "dialogue"),
        ("Length", "2&ndash;3 minutes to read"),
        ("Northern parallel", "King Sivi's story is widely known across Buddhist Asia as "
                              "the Sivi Jātaka, traditionally numbered 499 among the "
                              "full collection of 547; this reading guide does not "
                              "assert further specific textual correspondences beyond "
                              "that widely cited number."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a dialogue-driven "
                       "story with a genuinely difficult subject"),
    ],
    why=(
        "This is probably the best-known story in the whole Cariyapitaka: a king who "
        "declares, seated comfortably in his own longhouse, that he would give away "
        "even his own eye if asked. Sakka, king of the gods, overhears the thought and "
        "decides to test it &mdash; and when the moment comes, Sivi doesn't just meet "
        "the test, he exceeds what was actually asked of him."),
    guide=[
        ("A private thought, overheard", [
            "The story opens with Sivi alone with his own reflection: he can think of no "
            "gift he has not already given, and even names the one thing that might seem "
            "unthinkable &mdash; his own eye &mdash; as something he would give &lsquo;"
            "without wavering&rsquo;. Sakka, seated in the assembly of gods, hears this "
            "and decides to find out if it is true."]),
        ("A test staged carefully", [
            "Sakka does not simply appear and ask; he takes the form of a frail, blind "
            "old man, describes his own blindness in detail, praises the king's "
            "reputation for generosity by name, and asks for only one eye, offering "
            "a concession &mdash; &lsquo;while you too get by with one&rsquo;."]),
        ("A request exceeded, not just met", [
            "Sivi's reaction is not reluctant compliance but open elation: &lsquo;my "
            "wish has come true, my intention is fulfilled&rsquo;. He then orders his "
            "attendant Sivaka to take not the one eye asked for, but both. The gift "
            "given exceeds what was actually requested."]),
        ("A verdict on his own mind", [
            "The story closes not with an outcome but with a report on the king's own "
            "state of mind throughout: &lsquo;while planning to give, while giving, and "
            "after I had given, my mind did not falter&rsquo;, and, in the same denial-"
            "then-reason structure used elsewhere in this chapter, an explicit statement "
            "that this was not from any lack of care for his own eyes or himself, but "
            "&lsquo;because omniscience is precious to me&rsquo;."]),
    ],
    terms=[
        ("Sakka",
         "king of the gods, who overhears Sivi's private reflection and disguises "
         "himself as a blind beggar to test it."),
        ("Sivaka",
         "the attendant Sivi orders to carry out the physical act of removing his eyes "
         "&mdash; the king directs the gift, but does not perform the act himself."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the eighth "
         "of ten stories on this theme opening the collection."),
        ("Ariṭṭha",
         "the city named as King Sivi's seat of rule."),
        ("Sivi Jātaka",
         "the fuller version of this story in the separate Jātaka tradition, "
         "traditionally numbered 499 among the full collection of 547."),
    ],
    text_intro=(
        "The text in full: sixteen verses, including quoted dialogue between Sivi, "
        "Sakka, and the disguised beggar. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("h3", "A private thought, overheard"),
        ("p", "&sect;1", "cp8:1.1-1.4"),
        ("p", "&sect;2", "cp8:2.1-2.4"),
        ("h3", "Sakka decides to test him"),
        ("p", "&sect;3", "cp8:3.1-3.4"),
        ("p", "&sect;4", "cp8:4.1-4.4"),
        ("p", "&sect;5", "cp8:5.1-5.4"),
        ("h3", "A beggar's request"),
        ("p", "&sect;6", "cp8:6.1-6.4"),
        ("p", "&sect;7", "cp8:7.1-7.4"),
        ("p", "&sect;8", "cp8:8.1-8.4"),
        ("p", "&sect;9", "cp8:9.1-9.4"),
        ("h3", "The king's response"),
        ("p", "&sect;10", "cp8:10.1-10.4"),
        ("p", "&sect;11", "cp8:11.1-11.4"),
        ("p", "&sect;12", "cp8:12.1-12.4"),
        ("h3", "The gift given"),
        ("p", "&sect;13", "cp8:13.1-13.4"),
        ("p", "&sect;14", "cp8:14.1-14.4"),
        ("p", "&sect;15", "cp8:15.1-15.4"),
        ("p", "&sect;16", "cp8:16.1-16.4"),
    ],
    quiz=[
        {"q": "What does Sivi think to himself at the start of this story?",
         "opts": [
             "That he regrets his past generosity",
             "That he can think of no gift he has not already given, even his own eye if asked",
             "That he wants to conquer a neighboring kingdom",
             "That he plans to stop giving gifts"],
         "correct": 1,
         "expl": "A private reflection, not spoken aloud to anyone."},
        {"q": "Who overhears Sivi's private thought, and what do they decide to do?",
         "opts": [
             "His ministers, who decide to warn him against it",
             "Sakka, king of the gods, who decides to test whether it is true",
             "A rival king, who plans an invasion",
             "No one overhears it; the thought stays private"],
         "correct": 1,
         "expl": "Sakka is seated in the assembly of gods when he hears it."},
        {"q": "What disguise does Sakka take to approach the king?",
         "opts": [
             "A powerful warrior",
             "A frail, blind old man",
             "A fellow king",
             "A young child"],
         "correct": 1,
         "expl": "Describing his own blindness in detail before making his request."},
        {"q": "How many eyes does the disguised beggar actually ask for?",
         "opts": [
             "Both eyes",
             "Just one, offering that the king would 'get by with one'",
             "No specific number is requested",
             "None; he asks for something else entirely"],
         "correct": 1,
         "expl": "A concession built into the request itself."},
        {"q": "How many eyes does Sivi actually order given?",
         "opts": [
             "Exactly the one asked for, no more",
             "Both — exceeding what was actually requested",
             "None; he changes his mind at the last moment",
             "He asks the beggar to choose which one"],
         "correct": 1,
         "expl": "The gift given exceeds what was actually asked."},
        {"q": "Who physically removes the king's eyes?",
         "opts": [
             "The king does it himself",
             "His attendant, Sivaka, at the king's order",
             "Sakka performs the act directly",
             "The text does not say"],
         "correct": 1,
         "expl": "The king directs the gift but does not perform the physical act himself."},
        {"q": "How does Sivi react when he understands what the beggar is asking?",
         "opts": [
             "With reluctance and hesitation",
             "With open elation — 'my wish has come true, my intention is fulfilled'",
             "With anger at being tested",
             "With confusion about what to do"],
         "correct": 1,
         "expl": "Not reluctant compliance, but genuine joy."},
        {"q": "What does the closing verse report about Sivi's state of mind?",
         "opts": [
             "That he regretted the decision immediately afterward",
             "That his mind did not falter while planning, giving, or after having given",
             "That he felt no emotion at all throughout",
             "That he was forced into it against his will"],
         "correct": 1,
         "expl": "A report on the king's mind throughout the whole episode, not just the outcome."},
        {"q": "What does the text explicitly deny as Sivi's reason for giving away his eyes?",
         "opts": [
             "That he disliked his eyes, or disliked himself",
             "That he wanted to win favor with Sakka",
             "That he was following a royal law",
             "Nothing is denied in this story"],
         "correct": 0,
         "expl": "The same denial-then-reason structure used elsewhere in this chapter."},
        {"q": "What number is King Sivi's story traditionally given in the separate Jātaka collection?",
         "opts": [
             "1",
             "499, among the full collection of 547",
             "35",
             "No number is ever associated with this story"],
         "correct": 1,
         "expl": "A widely cited number for one of Buddhist Asia's best-known stories."},
    ],
    marginalia=[
        ("A private thought", [
            "overheard by Sakka,",
            "put to the test",
        ]),
        ("A beggar in disguise", [
            "blind, frail —",
            "asking for one eye",
        ]),
        ("Exceeding the request", [
            "not one eye,",
            "but both, given freely",
        ]),
        ("An unfaltering mind", [
            "before, during,",
            "and after giving",
        ]),
    ],
    further=[
        '<a href="%s/cp8/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-7.html">Cp 7 &mdash; Prince Candana&rsquo;s Conduct</a> &mdash; the '
        "text immediately before this one in the Cariyapitaka.",
        '<a href="cp-9.html">Cp 9 &mdash; Vessantara&rsquo;s Conduct</a> &mdash; the '
        "collection's other best-known giving-story, also tested by Sakka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 9 — Vessantara Cariyā
# --------------------------------------------------------------------------- #
page(
    9, "Vessantara Cariy&amacr;", "Vessantara&rsquo;s Conduct",
    meta_title="Cp 9 — Vessantara's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Vessantara's "
        "Conduct, the longest and most famous story in the Cariyapitaka — a prince who "
        "gives away his kingdom, his children, and his wife. From Ru-Yi Meditation "
        "Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (9th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as Prince Vessantara, beginning one generation "
                    "earlier with his mother's own story"),
        ("Speaker", "The Buddha, recounting his life as Vessantara, with quoted dialogue "
                    "from his mother Phussatī and Sakka"),
        ("Form", "Fifty-eight verses of first-person narration, by far the longest text "
                 "in the collection"),
        ("Length", "8&ndash;10 minutes to read"),
        ("Northern parallel", "Vessantara's story is traditionally counted as the last "
                              "and longest of the full collection of 547 Jātaka tales, "
                              "widely known and depicted across Buddhist Asia; this "
                              "reading guide does not assert further specific textual "
                              "correspondences beyond that widely cited number."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; long, and its central "
                       "episodes raise real ethical difficulty that this reading guide "
                       "does not smooth over"),
    ],
    why=(
        "This is the longest text in the entire Cariyapitaka, and traditionally the "
        "last and best known of all 547 Jātaka tales: a prince who gives away, in "
        "escalating order, his kingdom's royal elephant, his wealth and possessions, his "
        "own two children, and finally his wife &mdash; each gift raising the stakes "
        "past the one before it, each marked by the earth itself quaking in response."),
    guide=[
        ("A story that starts one generation early", [
            "Unlike every other story in this chapter, this one does not open with the "
            "bodhisatta's own life. It opens with his mother Phussatī, granted ten boons "
            "by Sakka before her death and reborn as an aristocrat who &lsquo;always "
            "delighted in giving&rsquo; while pregnant with Vessantara &mdash; explaining "
            "his character as something present before his own life even began."]),
        ("A resolve made at eight years old", [
            "As a boy, Vessantara already declares he would give his heart, his eyes, "
            "his flesh and blood, if anyone asked &mdash; a resolve the text marks as "
            "cosmically significant: the earth quakes at the steadiness of his "
            "reflection alone, before he has given anything at all."]),
        ("The same elephant-gift verses as Cp 3", [
            "The request from Kaliṅga brahmins for the royal elephant, and Vessantara's "
            "vow not to refuse a supplicant, reuse verses nearly identical to Cp 3's "
            "King Dhanañjaya &mdash; but here the gift has a consequence Cp 3 does not "
            "narrate: angry townsfolk banish Vessantara from his own kingdom for it."]),
        ("Escalating gifts, each marked by the earth", [
            "Exile does not end the giving. Before leaving the city he performs one more "
            "great offering of wealth; on the road he gives up his chariot; in the "
            "forest he gives away his two children to a brahmin named Jūjaka, then his "
            "wife Maddī to a disguised Sakka. The text itself counts the pattern: by its "
            "own final line, the earth has quaked seven times at these gifts."]),
        ("A gap this verse-only text does not fill", [
            "Between giving away his children and the family's eventual reunion, this "
            "text moves directly from the gift itself to &lsquo;later on... we were "
            "reunited by my mother and father&rsquo;, without narrating what happened to "
            "the children in between. The fuller prose Jātaka tradition supplies that "
            "part of the story; this verse-only Cariyapitaka text, like several others "
            "in this collection, does not."]),
        ("The same denial, at the highest stakes yet", [
            "As with earlier stories in this chapter, Vessantara explicitly denies the "
            "obvious reading of his own actions: &lsquo;I had no dislike of my children, "
            "nor for Queen Maddī&rsquo;. The reason given is the same one that has closed "
            "story after story in this chapter &mdash; &lsquo;because omniscience is "
            "precious to me&rsquo; &mdash; now carrying weight it did not carry when the "
            "gift was an umbrella or a plate of leaves."]),
    ],
    terms=[
        ("Phussatī",
         "Vessantara's mother, whose own story of ten boons granted by Sakka opens this "
         "text before Vessantara's life begins."),
        ("Jūjaka",
         "the brahmin who asks Vessantara for his two children, Jāli and Kaṇhājinā."),
        ("Maddī",
         "Vessantara's wife, given in this story's final major gift to a disguised "
         "Sakka."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the ninth "
         "of ten stories on this theme, and by far its longest example."),
        ("Vessantara Jātaka",
         "the fuller prose-and-verse version of this story, traditionally counted as "
         "the last and longest of the full collection of 547 Jātaka tales."),
    ],
    text_intro=(
        "The text in full: fifty-eight verses, the longest text in the Cariyapitaka. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Vessantara's mother, and his birth"),
        ("p", "&sect;1", "cp9:1.1-1.4"),
        ("p", "&sect;2", "cp9:2.1-2.4"),
        ("p", "&sect;3", "cp9:3.1-3.6"),
        ("p", "&sect;4", "cp9:4.1-4.4"),
        ("p", "&sect;5", "cp9:5.1-5.4"),
        ("p", "&sect;6", "cp9:6.1-6.4"),
        ("p", "&sect;7", "cp9:7.1-7.4"),
        ("p", "&sect;8", "cp9:8.1-8.4"),
        ("p", "&sect;9", "cp9:9.1-9.4"),
        ("p", "&sect;10", "cp9:10.1-10.4"),
        ("p", "&sect;11", "cp9:11.1-11.4"),
        ("h3", "A resolve made as a child"),
        ("p", "&sect;12", "cp9:12.1-12.4"),
        ("p", "&sect;13", "cp9:13.1-13.4"),
        ("p", "&sect;14", "cp9:14.1-14.4"),
        ("h3", "The gift of the royal elephant"),
        ("p", "&sect;15", "cp9:15.1-15.4"),
        ("p", "&sect;16", "cp9:16.1-16.4"),
        ("p", "&sect;17", "cp9:17.1-17.4"),
        ("p", "&sect;18", "cp9:18.1-18.4"),
        ("p", "&sect;19", "cp9:19.1-19.4"),
        ("p", "&sect;20", "cp9:20.1-20.4"),
        ("p", "&sect;21", "cp9:21.1-21.4"),
        ("h3", "Banished, giving once more before he goes"),
        ("p", "&sect;22", "cp9:22.1-22.4"),
        ("p", "&sect;23", "cp9:23.1-23.4"),
        ("p", "&sect;24", "cp9:24.1-24.4"),
        ("p", "&sect;25", "cp9:25.1-25.4"),
        ("p", "&sect;26", "cp9:26.1-26.4"),
        ("p", "&sect;27", "cp9:27.1-27.4"),
        ("h3", "Into exile with Maddī and the children"),
        ("p", "&sect;28", "cp9:28.1-28.4"),
        ("p", "&sect;29", "cp9:29.1-29.4"),
        ("p", "&sect;30", "cp9:30.1-30.4"),
        ("p", "&sect;31", "cp9:31.1-31.4"),
        ("p", "&sect;32", "cp9:32.1-32.4"),
        ("p", "&sect;33", "cp9:33.1-33.4"),
        ("p", "&sect;34", "cp9:34.1-34.4"),
        ("p", "&sect;35", "cp9:35.1-35.4"),
        ("p", "&sect;36", "cp9:36.1-36.4"),
        ("p", "&sect;37", "cp9:37.1-37.4"),
        ("p", "&sect;38", "cp9:38.1-38.4"),
        ("h3", "A hermitage in the forest"),
        ("p", "&sect;39", "cp9:39.1-39.4"),
        ("p", "&sect;40", "cp9:40.1-40.4"),
        ("p", "&sect;41", "cp9:41.1-41.4"),
        ("p", "&sect;42", "cp9:42.1-42.4"),
        ("p", "&sect;43", "cp9:43.1-43.4"),
        ("p", "&sect;44", "cp9:44.1-44.4"),
        ("p", "&sect;45", "cp9:45.1-45.4"),
        ("h3", "Giving away the children"),
        ("p", "&sect;46", "cp9:46.1-46.4"),
        ("p", "&sect;47", "cp9:47.1-47.4"),
        ("p", "&sect;48", "cp9:48.1-48.4"),
        ("h3", "Giving away Maddī"),
        ("p", "&sect;49", "cp9:49.1-49.4"),
        ("p", "&sect;50", "cp9:50.1-50.4"),
        ("p", "&sect;51", "cp9:51.1-51.4"),
        ("p", "&sect;52", "cp9:52.1-52.4"),
        ("p", "&sect;53", "cp9:53.1-53.4"),
        ("h3", "Reunion and return"),
        ("p", "&sect;54", "cp9:54.1-54.4"),
        ("p", "&sect;55", "cp9:55.1-55.4"),
        ("p", "&sect;56", "cp9:56.1-56.4"),
        ("p", "&sect;57", "cp9:57.1-57.4"),
        ("p", "&sect;58", "cp9:58.1-58.4"),
    ],
    quiz=[
        {"q": "How does this story's structure differ from every other story in this chapter?",
         "opts": [
             "It is told in the third person",
             "It opens one generation early, with the story of Vessantara's mother Phussatī",
             "It has no ending",
             "It contains no verse at all"],
         "correct": 1,
         "expl": "Explaining his character as present even before his own life began."},
        {"q": "What does Vessantara resolve as an eight-year-old boy?",
         "opts": [
             "To become a great warrior",
             "That he would give his heart, eyes, flesh, and blood if anyone asked",
             "To leave home immediately",
             "Nothing specific is recorded about his childhood"],
         "correct": 1,
         "expl": "The earth quakes at the steadiness of this reflection alone."},
        {"q": "What connects the elephant-gift scene in this story to Cp 3?",
         "opts": [
             "Nothing; the two stories are unrelated",
             "Nearly identical verses describing the Kaliṅga brahmins' request and the vow not to refuse them",
             "Both stories are set in the same city",
             "Both kings refuse to give the elephant"],
         "correct": 1,
         "expl": "Though here the gift has a consequence Cp 3 does not narrate: banishment."},
        {"q": "What happens to Vessantara after he gives away the royal elephant?",
         "opts": [
             "He is celebrated by his people",
             "Angry townsfolk banish him from his own kingdom",
             "He is immediately crowned a greater king",
             "Nothing changes for him"],
         "correct": 1,
         "expl": "Before leaving, he asks one favor: to perform one more great offering."},
        {"q": "In what order does Vessantara give away what he has?",
         "opts": [
             "Randomly, with no particular sequence",
             "Escalating from wealth and possessions, to his children, to his wife",
             "His wife first, then his children, then his wealth",
             "He gives away nothing after the elephant"],
         "correct": 1,
         "expl": "Each gift raising the stakes past the one before it."},
        {"q": "What happens between Vessantara giving away his children and the family's reunion, according to THIS text?",
         "opts": [
             "A detailed account of the children's treatment and eventual ransom",
             "The text does not narrate this part — it moves directly from the gift to 'later on... we were reunited'",
             "The children are given back immediately",
             "Vessantara goes to retrieve them himself"],
         "correct": 1,
         "expl": "A gap this verse-only text leaves for the fuller prose Jātaka tradition to fill."},
        {"q": "Who does Vessantara give his wife Maddī to, and in what disguise?",
         "opts": [
             "Jūjaka, still disguised as a brahmin",
             "Sakka, again disguised as a brahmin",
             "He never gives her away in this story",
             "A rival king"],
         "correct": 1,
         "expl": "The same figure who tested King Sivi in Cp 8."},
        {"q": "What does Vessantara explicitly deny as his reason for giving away his children and wife?",
         "opts": [
             "That he disliked them",
             "That he needed the merit for himself alone",
             "That he was forced by law",
             "Nothing is denied in this part of the story"],
         "correct": 0,
         "expl": "The same denial-then-reason structure used throughout this chapter, now at its highest stakes."},
        {"q": "How many times does the text say the earth quaked over the course of this story?",
         "opts": [
             "Once, at the very end",
             "Seven times, by the story's own count",
             "It never quakes in this version",
             "An unspecified number of times"],
         "correct": 1,
         "expl": "Named directly in the closing verse."},
        {"q": "What is Vessantara's story traditionally counted as, among the Jātaka tales?",
         "opts": [
             "A minor, rarely mentioned story",
             "The last and longest of the full collection of 547 Jātaka tales",
             "The very first Jātaka",
             "It has no traditional number or ranking"],
         "correct": 1,
         "expl": "Widely known and depicted across Buddhist Asia."},
    ],
    marginalia=[
        ("A story begun early", [
            "one generation before",
            "Vessantara's own birth",
        ]),
        ("Escalating gifts", [
            "elephant, wealth,",
            "children, wife",
        ]),
        ("The earth quakes", [
            "seven times,",
            "by the text's own count",
        ]),
        ("A gap left open", [
            "the children's fate,",
            "untold in this version",
        ]),
    ],
    further=[
        '<a href="%s/cp9/en/sujato" target="_blank" rel="noopener">Full Sujato translation '
        "on SuttaCentral</a> &mdash; with Pāli alongside, segment by segment." % SC,
        '<a href="cp-8.html">Cp 8 &mdash; King Sivi&rsquo;s Conduct</a> &mdash; the '
        "collection's other best-known giving-story, also tested by Sakka.",
        '<a href="cp-3.html">Cp 3 &mdash; Kur&umacr;r&amacr;ja&rsquo;s Conduct</a> &mdash; '
        "the story whose elephant-gift verses this text reuses almost word for word.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 10 — Sasa Cariyā
# --------------------------------------------------------------------------- #
page(
    10, "Sasa Cariy&amacr;", "The Wise Hare&rsquo;s Conduct",
    meta_title="Cp 10 — The Wise Hare's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Wise Hare's "
        "Conduct, the Cariyapitaka's closing story on giving — a hare with nothing to "
        "give but his own body. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Akitti &middot; The Perfection of Giving (10th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as a hare living in the forest"),
        ("Speaker", "The Buddha, recounting his life as a hare, with a brief exchange "
                    "with a disguised Sakka"),
        ("Form", "Nineteen four-line verses of first-person narration"),
        ("Length", "2&ndash;3 minutes to read"),
        ("Northern parallel", "This story is traditionally known as the Sasa Jātaka, "
                              "often linked in later tradition to the widespread "
                              "&lsquo;hare in the moon&rsquo; motif found across Asian "
                              "folklore &mdash; though this verse text itself makes no "
                              "mention of the moon beyond marking the day as the "
                              "full-moon sabbath."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a simple, direct "
                       "story closing the chapter on giving"),
    ],
    why=(
        "This closing story of the giving chapter returns to the scale of Cp 1: not a "
        "king or a prince, but an ordinary forest animal, a hare, who has nothing "
        "substantial to give and resolves to give the only thing he does have &mdash; "
        "himself. Where Cp 9 closed the chapter's escalation with a prince giving away "
        "his own family, this final story closes it with the simplest possible giver "
        "and the most complete possible gift."),
    guide=[
        ("Four friends, one teacher", [
            "A hare lives alongside a monkey, a jackal, and a young otter, advising them "
            "on good and bad conduct. Seeing the full-moon sabbath approaching, he tells "
            "them to prepare gifts for a worthy recipient before observing the day."]),
        ("Nothing to give but himself", [
            "Reflecting on what he could offer if a worthy recipient actually appeared, "
            "the hare comes up short: &lsquo;I have no sesame or mung beans, no beans or "
            "rice or ghee. I feed only on grass, but that's not something I can "
            "give.&rsquo; His resolution follows directly from this lack, not around it: "
            "if someone worthy comes, he will give his own self."]),
        ("Sakka arrives to test the resolution", [
            "As in Cp 8's story of King Sivi, Sakka disguises himself, this time as a "
            "brahmin, and approaches specifically &lsquo;to test his giving&rsquo;. The "
            "hare's response is immediate and practical: he asks the visitor to build a "
            "fire, announcing plainly, &lsquo;I shall cook myself, you shall eat me "
            "roasted.&rsquo;"]),
        ("A fire compared to cool water", [
            "The story's most striking image comes at the moment of the gift itself: "
            "entering the blazing fire is described as feeling &lsquo;like diving into "
            "cool water, allaying distress and fever&rsquo; &mdash; not suffering "
            "endured, but relief experienced, closing the giving chapter on a note of "
            "ease rather than ordeal."]),
    ],
    terms=[
        ("Sasa Jātaka",
         "the traditional name of this story in the wider Jātaka literature, sometimes "
         "linked to the &lsquo;hare in the moon&rsquo; motif found across Asian "
         "folklore."),
        ("uposatha",
         "the full-moon observance day the hare points out to his three companions, "
         "prompting them to prepare gifts."),
        ("dāna",
         "&ldquo;giving&rdquo; &mdash; the perfection this story illustrates, the tenth "
         "and final of ten stories on this theme."),
        ("Sakka",
         "king of the gods, who again disguises himself, as in Cp 8, specifically to "
         "test a resolution to give."),
        ("dakkhiṇeyya",
         "a &ldquo;worthy recipient&rdquo; of a gift &mdash; the figure the hare and his "
         "companions are told to seek out before observing the sabbath."),
    ],
    text_intro=(
        "The text in full: nineteen verses, closing the Cariyapitaka's chapter on "
        "giving. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Four friends, one teacher"),
        ("p", "&sect;1", "cp10:1.1-1.4"),
        ("p", "&sect;2", "cp10:2.1-2.4"),
        ("p", "&sect;3", "cp10:3.1-3.4"),
        ("p", "&sect;4", "cp10:4.1-4.4"),
        ("p", "&sect;5", "cp10:5.1-5.4"),
        ("p", "&sect;6", "cp10:6.1-6.4"),
        ("h3", "Nothing to give but himself"),
        ("p", "&sect;7", "cp10:7.1-7.4"),
        ("p", "&sect;8", "cp10:8.1-8.4"),
        ("p", "&sect;9", "cp10:9.1-9.4"),
        ("h3", "Sakka's test"),
        ("p", "&sect;10", "cp10:10.1-10.4"),
        ("p", "&sect;11", "cp10:11.1-11.4"),
        ("p", "&sect;12", "cp10:12.1-12.4"),
        ("p", "&sect;13", "cp10:13.1-13.4"),
        ("p", "&sect;14", "cp10:14.1-14.4"),
        ("h3", "Into the flames"),
        ("p", "&sect;15", "cp10:15.1-15.4"),
        ("p", "&sect;16", "cp10:16.1-16.4"),
        ("p", "&sect;17", "cp10:17.1-17.4"),
        ("p", "&sect;18", "cp10:18.1-18.4"),
        ("p", "&sect;19", "cp10:19.1-19.4"),
    ],
    quiz=[
        {"q": "Who does the hare live alongside in the forest?",
         "opts": [
             "A tiger and a bear",
             "A monkey, a jackal, and a young otter",
             "He lives entirely alone",
             "A group of other hares"],
         "correct": 1,
         "expl": "He advises all three on good and bad conduct."},
        {"q": "What does the hare point out to his companions, prompting them to prepare gifts?",
         "opts": [
             "A stranger approaching the forest",
             "The full-moon sabbath day",
             "A famine affecting the forest",
             "A festival held by nearby villagers"],
         "correct": 1,
         "expl": "Advising them to give to a worthy recipient before observing the day."},
        {"q": "What problem does the hare face when he considers what he could give?",
         "opts": [
             "He has plenty to give but is reluctant",
             "He has nothing but grass, which is not something he can offer as a gift",
             "He has no worthy recipient to give to",
             "He forgets it is the sabbath day"],
         "correct": 1,
         "expl": "Unlike sesame, beans, rice, or ghee, grass cannot be given as an offering."},
        {"q": "What does the hare resolve to give instead?",
         "opts": [
             "Nothing; he decides he cannot give anything",
             "His own self, if a worthy recipient should come",
             "A promise to give something in the future",
             "He asks his companions to give on his behalf"],
         "correct": 1,
         "expl": "His resolution follows directly from having nothing else."},
        {"q": "Who tests the hare's resolution, and in what disguise?",
         "opts": [
             "A rival animal, disguised as a friend",
             "Sakka, disguised as a brahmin",
             "The Buddha himself, undisguised",
             "No one tests him; he is never approached"],
         "correct": 1,
         "expl": "As with King Sivi in Cp 8, Sakka disguises himself specifically to test a giving resolution."},
        {"q": "What does the hare ask the disguised visitor to do?",
         "opts": [
             "Leave the forest immediately",
             "Build a fire, so the hare can be cooked and eaten",
             "Wait until the hare finds other food",
             "Fight him for the right to stay in the forest"],
         "correct": 1,
         "expl": "'I shall cook myself, you shall eat me roasted.'"},
        {"q": "How is the moment of the hare entering the fire described?",
         "opts": [
             "As unbearable agony",
             "Like diving into cool water, allaying distress and fever",
             "The text skips over this moment entirely",
             "As a moment of regret"],
         "correct": 1,
         "expl": "Relief experienced, not suffering endured."},
        {"q": "Does this verse text mention the hare's image being placed on the moon?",
         "opts": [
             "Yes, in detail, as the story's climax",
             "No — that motif belongs to later tradition and folklore, not this verse text",
             "Yes, but only in a single ambiguous line",
             "The text is entirely about the moon"],
         "correct": 1,
         "expl": "This text ends with the gift itself, not any subsequent memorial."},
        {"q": "How does this story's scale compare to Cp 9's, immediately before it?",
         "opts": [
             "Both stories feature the same character",
             "It returns to an ordinary, humble giver after Cp 9's prince and kingdom",
             "It is even larger in scale than Cp 9",
             "There is no meaningful difference in scale"],
         "correct": 1,
         "expl": "Closing the chapter's escalation with the simplest possible giver."},
        {"q": "What perfection does this story illustrate, and what position does it hold in the chapter?",
         "opts": [
             "Ethics, opening the second chapter",
             "Giving (dāna), the tenth and final story of this chapter",
             "Truth, the collection's final story overall",
             "Renunciation, the fifth of five stories on this theme"],
         "correct": 1,
         "expl": "Closing the ten-story sequence on giving that opens the Cariyapitaka."},
    ],
    marginalia=[
        ("Four forest friends", [
            "hare, monkey,",
            "jackal, otter",
        ]),
        ("Nothing but grass to give", [
            "so he resolves",
            "to give himself"
        ]),
        ("Sakka tests again", [
            "disguised as a brahmin,",
            "as with King Sivi"
        ]),
        ("Fire as cool water", [
            "relief, not ordeal,",
            "closing the chapter"
        ]),
    ],
    further=[
        '<a href="%s/cp10/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-9.html">Cp 9 &mdash; Vessantara&rsquo;s Conduct</a> &mdash; the text '
        "immediately before this one, closing the chapter on giving.",
        '<a href="cp-8.html">Cp 8 &mdash; King Sivi&rsquo;s Conduct</a> &mdash; the '
        "collection's other story of Sakka testing a giving resolution.",
        '<a href="./">Cariyapiṭaka</a> &mdash; back to the collection index.',
    ],
)


# --------------------------------------------------------------------------- #
# Cp 11 — Mātuposaka Cariyā
# --------------------------------------------------------------------------- #
page(
    11, "M&amacr;tuposaka Cariy&amacr;", "The Conduct of One Who Provided for His Mother",
    meta_title="Cp 11 — The Elephant Who Provided for His Mother | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Cariyapitaka's "
        "opening story on the perfection of ethics — an elephant of immense strength "
        "who submits to capture rather than fight back. From Ru-Yi Meditation Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (1st of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as an elephant who fed and cared for his "
                    "mother"),
        ("Speaker", "The Buddha, recounting his life as an unnamed elephant of immense "
                    "strength"),
        ("Form", "Ten four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "An elephant who supports his blind mother is the subject "
                              "of its own jātaka in the wider tradition; this reading "
                              "guide does not assert a specific matching text or number."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, but opens a "
                       "chapter whose central idea takes a moment to state clearly"),
    ],
    why=(
        "This story opens the Cariyapitaka's second chapter, on the perfection of "
        "ethics &mdash; and sets the pattern nearly every story in this chapter will "
        "follow. Its central figure is not virtuous because he is weak or has no other "
        "option: an elephant here explicitly states he had the physical power to defeat "
        "an army, and chooses instead to let himself be captured and beaten without "
        "retaliating, purely to keep his ethical conduct intact."),
    guide=[
        ("A different chapter, a different kind of virtue", [
            "Where the first chapter's ten stories were about giving something away, "
            "this second chapter's ten stories are almost all about a different "
            "discipline: not retaliating, not breaking a commitment to non-harm, even "
            "when the character in question has every practical ability to strike back."]),
        ("Enormous strength, deliberately unused", [
            "The elephant states his own power directly: strong enough, in his prime, to "
            "equal a thousand elephants, with the physical capacity to defeat &lsquo;even "
            "a kingdom of men&rsquo; if provoked. None of that capacity is used when "
            "hunters come to capture him."]),
        ("Captured while feeding his mother", [
            "The elephant is found not in a moment of vulnerability but in an act of "
            "care &mdash; pulling lotus roots from a pond to feed his mother &mdash; "
            "and is taken by the trunk without a struggle, on a tamer's word alone, no "
            "moat or restraint required."]),
        ("A vow stated as the reason, not fear", [
            "The story is explicit about motive: &lsquo;for the sake of guarding my "
            "ethics, and fulfilling my perfection of ethics, I did not let my mind "
            "change&rsquo;, even under blows from hatchets and lances. Restraint here is "
            "framed as a discipline actively maintained, not a lack of options."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "entire second chapter illustrates, opening here with its first story."),
        ("Mātuposaka",
         "&ldquo;one who supports his mother&rdquo; &mdash; the descriptive title of "
         "this story, rather than a proper name."),
        ("pāramī",
         "&ldquo;perfection&rdquo; &mdash; the ten stories of this chapter all "
         "illustrate the perfection of ethics, as the ten stories before them "
         "illustrated giving."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its eleventh."),
        ("Hatthinaga-vagga",
         "&ldquo;the Chapter on an Elephant&rdquo; &mdash; the traditional name of this "
         "second chapter, taken from this opening story."),
    ],
    text_intro=(
        "The text in full: ten verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp11:1.1-1.4"),
        ("p", "&sect;2", "cp11:2.1-2.4"),
        ("p", "&sect;3", "cp11:3.1-3.4"),
        ("p", "&sect;4", "cp11:4.1-4.4"),
        ("p", "&sect;5", "cp11:5.1-5.4"),
        ("p", "&sect;6", "cp11:6.1-6.4"),
        ("p", "&sect;7", "cp11:7.1-7.4"),
        ("p", "&sect;8", "cp11:8.1-8.4"),
        ("p", "&sect;9", "cp11:9.1-9.4"),
        ("p", "&sect;10", "cp11:10.1-10.4"),
    ],
    quiz=[
        {"q": "What perfection does this second chapter of the Cariyapitaka illustrate?",
         "opts": [
             "Giving, continuing the first chapter's theme",
             "Ethics (sīla), a new theme for this chapter",
             "Wisdom",
             "Patience, as its own distinct perfection"],
         "correct": 1,
         "expl": "Ten stories on ethics follow the ten stories on giving."},
        {"q": "What discipline does this chapter's opening story establish as a pattern?",
         "opts": [
             "Giving away possessions",
             "Not retaliating, even when the character has the power to",
             "Seeking out teachers for instruction",
             "Performing elaborate rituals"],
         "correct": 1,
         "expl": "Restraint held deliberately, not because of a lack of options."},
        {"q": "What was the elephant doing when he was found by the hunters?",
         "opts": [
             "Fighting off a rival elephant",
             "Pulling lotus roots from a pond to feed his mother",
             "Sleeping in a cave",
             "Fleeing from a forest fire"],
         "correct": 1,
         "expl": "Found in an act of care, not vulnerability."},
        {"q": "How does the elephant describe his own physical power?",
         "opts": [
             "As weak and unremarkable",
             "Strong enough to defeat even a kingdom of men, if provoked",
             "Only slightly stronger than an average elephant",
             "He makes no claim about his strength"],
         "correct": 1,
         "expl": "Equal to a thousand elephants in his prime."},
        {"q": "How was the elephant actually captured?",
         "opts": [
             "With a moat and heavy restraints",
             "Taken by the trunk, on a tamer's word alone, without a struggle",
             "He was tricked with poisoned food",
             "He was never actually captured"],
         "correct": 1,
         "expl": "No force was needed against him."},
        {"q": "What does the elephant say motivated his non-retaliation, even under blows?",
         "opts": [
             "Fear of being killed",
             "Guarding his ethics and fulfilling his perfection of ethics",
             "A promise made to the hunters",
             "Simple exhaustion"],
         "correct": 1,
         "expl": "Framed explicitly as a discipline, not weakness."},
        {"q": "What does 'Mātuposaka' mean?",
         "opts": [
             "'Great elephant'",
             "'One who supports his mother' — a descriptive title, not a proper name",
             "'King of the forest'",
             "'Perfection of ethics'"],
         "correct": 1,
         "expl": "This story's title describes the elephant's role, rather than naming him."},
        {"q": "What is the traditional name of this chapter, taken from this opening story?",
         "opts": [
             "Akitti-vagga",
             "Hatthinaga-vagga, 'the Chapter on an Elephant'",
             "Yudhañjaya-vagga",
             "No traditional name is given"],
         "correct": 1,
         "expl": "Named for its first story, as the first chapter was named for Akitti."},
        {"q": "How does this chapter's approach to virtue differ from the first chapter's?",
         "opts": [
             "There is no meaningful difference",
             "The first chapter is about giving something away; this one is mostly about not retaliating",
             "This chapter is entirely about wealth",
             "This chapter has no stories about animals"],
         "correct": 1,
         "expl": "A different discipline illustrated across ten different stories."},
        {"q": "What perfection did the first chapter of the Cariyapitaka illustrate?",
         "opts": [
             "Ethics",
             "Giving (dāna)",
             "Truth",
             "Equanimity"],
         "correct": 1,
         "expl": "Cp 1 through Cp 10, now followed by this chapter on ethics."},
    ],
    marginalia=[
        ("A new chapter", [
            "ethics (sīla),",
            "not giving"
        ]),
        ("Power held back", [
            "strong enough for an army,",
            "used against no one"
        ]),
        ("Found caring for his mother", [
            "captured without",
            "a struggle"
        ]),
        ("A vow, not weakness", [
            "'I did not let",
            "my mind change'"
        ]),
    ],
    further=[
        '<a href="%s/cp11/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-10.html">Cp 10 &mdash; The Wise Hare&rsquo;s Conduct</a> &mdash; the '
        "text immediately before this one, closing the chapter on giving.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 12 — Bhūridatta Cariyā
# --------------------------------------------------------------------------- #
page(
    12, "Bh&umacr;ridatta Cariy&amacr;", "The Dragon Bh&umacr;ridatta&rsquo;s Conduct",
    meta_title="Cp 12 — The Dragon Bhūridatta's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dragon "
        "Bhūridatta's Conduct, the Cariyapitaka's story of a nāga of immense power who "
        "submits to capture rather than break his precepts. From Ru-Yi Meditation "
        "Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (2nd of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as the nāga Bhūridatta"),
        ("Speaker", "The Buddha, recounting his life as Bhūridatta"),
        ("Form", "Nine four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "Bhūridatta is the subject of his own jātaka, "
                              "traditionally counted among the same well-known set of "
                              "the last ten jātakas as Cp 26's Temiya; this reading "
                              "guide does not assert further specific correspondences "
                              "beyond that general association."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; direct narration "
                       "with a clear central choice"),
    ],
    why=(
        "A nāga &mdash; a serpent being of great psychic power, capable of turning dry "
        "land to water at will &mdash; undertakes ethical observance in hopes of a "
        "heavenly rebirth, and then holds to it even while trapped in a basket, thrown "
        "around, and forced to perform as a street entertainer by the man who caught "
        "him."),
    guide=[
        ("A vow made freely, before any threat", [
            "Bhūridatta's ethical observance does not begin as a response to danger: "
            "seeing gods absorbed in pleasure during a visit to a heavenly realm, he "
            "undertakes ethical practice on his own initiative, resolving on four "
            "factors and lying down on a termite mound, offering his own body to "
            "&lsquo;whoever has use for these&rsquo;."]),
        ("An offer taken advantage of", [
            "A snake-charmer named Ālampāyana takes Bhūridatta at his word in the worst "
            "possible way &mdash; capturing him, throwing him in a basket, and forcing "
            "him to perform in public &mdash; treatment the nāga endures without "
            "retaliating, though he explicitly names the man as an ingrate."]),
        ("A comparison of weights", [
            "The story states its central value directly, through comparison: "
            "&lsquo;to give up my own life was as light as a blade of grass. To "
            "transgress my ethical principles was like overturning the earth.&rsquo; "
            "The two are placed on opposite ends of a scale, not treated as comparable "
            "costs."]),
        ("A stated willingness to repeat the ordeal", [
            "Bhūridatta does not describe this as a one-time sacrifice: he states he "
            "would give up his own life in a hundred successive lives before violating "
            "his ethics &lsquo;for the sake of the four continents&rsquo; &mdash; the "
            "entire world offered as a hypothetical bribe, and refused."]),
    ],
    terms=[
        ("nāga",
         "a serpent being of great psychic power &mdash; the kind of being Bhūridatta "
         "is described as in this text."),
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the second of ten stories on this theme."),
        ("uposatha",
         "the observance day whose ethical undertakings Bhūridatta resolves on before "
         "lying down on the termite mound."),
        ("Ālampāyana",
         "the snake-charmer who captures Bhūridatta and forces him to perform, despite "
         "the nāga's own offer of his body having been made in good faith."),
        ("Bhūridatta Jātaka",
         "the fuller version of this story in the separate Jātaka tradition, "
         "traditionally counted among a well-known set of the last ten jātakas."),
    ],
    text_intro=(
        "The text in full: nine verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp12:1.1-1.4"),
        ("p", "&sect;2", "cp12:2.1-2.4"),
        ("p", "&sect;3", "cp12:3.1-3.4"),
        ("p", "&sect;4", "cp12:4.1-4.4"),
        ("p", "&sect;5", "cp12:5.1-5.4"),
        ("p", "&sect;6", "cp12:6.1-6.4"),
        ("p", "&sect;7", "cp12:7.1-7.4"),
        ("p", "&sect;8", "cp12:8.1-8.4"),
        ("p", "&sect;9", "cp12:9.1-9.4"),
    ],
    quiz=[
        {"q": "What prompts Bhūridatta to undertake ethical observance in the first place?",
         "opts": [
             "A direct threat to his life",
             "Seeing gods absorbed in pleasure during a visit to a heavenly realm, hoping for a heavenly rebirth",
             "A command from a king",
             "No reason is given"],
         "correct": 1,
         "expl": "Undertaken freely, before any danger appears."},
        {"q": "What does Bhūridatta offer while lying on the termite mound?",
         "opts": [
             "His wealth",
             "His own body, to 'whoever has use for these'",
             "A prayer for the world's wellbeing",
             "Nothing; he makes no offer"],
         "correct": 1,
         "expl": "An offer later taken advantage of by the snake-charmer Ālampāyana."},
        {"q": "How does Ālampāyana treat Bhūridatta after capturing him?",
         "opts": [
             "With great respect, honoring his vow",
             "Throwing him in a basket and forcing him to perform in public",
             "Releasing him immediately",
             "Offering him a position at court"],
         "correct": 1,
         "expl": "Treatment Bhūridatta endures without retaliating."},
        {"q": "What comparison does the text use for giving up one's life versus breaking one's ethics?",
         "opts": [
             "Both are treated as equally costly",
             "Giving up life is 'as light as a blade of grass'; breaking ethics is 'like overturning the earth'",
             "Breaking ethics is described as trivial",
             "No comparison is made"],
         "correct": 1,
         "expl": "Placed on opposite ends of a scale, not treated as comparable."},
        {"q": "How many lifetimes does Bhūridatta say he would sacrifice rather than break his ethics?",
         "opts": [
             "None; he would break them to save his life",
             "A hundred successive lives",
             "Exactly one",
             "An unspecified small number"],
         "correct": 1,
         "expl": "Even for the hypothetical bribe of 'the four continents' — the whole world."},
        {"q": "What power does the text say Bhūridatta possessed?",
         "opts": [
             "None; he is described as physically weak",
             "The ability to turn dry land to water and back, among other feats",
             "Only the power of persuasive speech",
             "Control over fire alone"],
         "correct": 1,
         "expl": "Immense psychic power, deliberately unused against his captor."},
        {"q": "What does the text call Ālampāyana, despite Bhūridatta's own good-faith offer?",
         "opts": [
             "A wise teacher",
             "An ingrate",
             "A fellow nāga",
             "A future Buddha"],
         "correct": 1,
         "expl": "Naming the injustice directly, even while enduring it without retaliation."},
        {"q": "What does 'uposatha' refer to in this story?",
         "opts": [
             "A type of basket",
             "The observance day whose undertakings Bhūridatta resolves on",
             "A snake-charmer's trade",
             "A heavenly realm"],
         "correct": 1,
         "expl": "The occasion for his ethical resolve before the termite-mound episode."},
        {"q": "What wider tradition is Bhūridatta's story associated with?",
         "opts": [
             "No other tradition mentions this figure",
             "His own jātaka, counted among a well-known set of the last ten jātakas",
             "A canonical discourse to King Bimbisāra",
             "The Petavatthu"],
         "correct": 1,
         "expl": "The same set that includes Cp 26's Temiya."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the second of ten stories on this theme",
             "Truth",
             "Love"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories opening this chapter."},
    ],
    marginalia=[
        ("A vow made freely", [
            "before any threat",
            "or danger appeared"
        ]),
        ("An offer exploited", [
            "captured, caged,",
            "forced to perform"
        ]),
        ("A blade of grass", [
            "against overturning",
            "the whole earth"
        ]),
        ("A hundred lives offered", [
            "rather than break",
            "his ethics once"
        ]),
    ],
    further=[
        '<a href="%s/cp12/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-11.html">Cp 11 &mdash; The Conduct of One Who Provided for His '
        "Mother</a> &mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 13 — Campeyya Cariyā
# --------------------------------------------------------------------------- #
page(
    13, "Campeyya Cariy&amacr;", "The Dragon Campeyyaka&rsquo;s Conduct",
    meta_title="Cp 13 — The Dragon Campeyyaka's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the Dragon "
        "Campeyyaka's Conduct, the Cariyapitaka's shortest ethics-story — a nāga who "
        "performs on command rather than break his precepts. From Ru-Yi Meditation "
        "Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (3rd of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as the nāga Campeyyaka"),
        ("Speaker", "The Buddha, recounting his life as Campeyyaka"),
        ("Form", "Six four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Campeyyaka is the subject of his own jātaka in the wider "
                              "tradition; this reading guide does not assert a specific "
                              "matching number."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; brief, but its final "
                       "image is a striking one"),
    ],
    why=(
        "A second nāga story follows Cp 12's directly, and shares its basic shape: "
        "immense, world-altering power, held back rather than used against a captor. "
        "Here a snake-charmer forces Campeyyaka to shape-shift and perform tricks on "
        "command &mdash; power the text says could just as easily reduce the man to "
        "ash."),
    guide=[
        ("A performer against his will", [
            "The snake-charmer who captures Campeyyaka makes him perform at the royal "
            "gate, shifting color &mdash; blue, yellow, red &mdash; to match whatever "
            "the charmer merely thinks of, a display of total control exercised over a "
            "being who could end the display at any moment."]),
        ("Named abilities, deliberately unused", [
            "The text states outright what Campeyyaka could do instead: turn dry land "
            "to water and water to dry land, or reduce his captor to ash in an instant, "
            "&lsquo;if I were upset with him&rsquo;. The performance continues because "
            "the nāga chooses restraint, not because he lacks any alternative."]),
        ("A reasoned refusal, not just a feeling", [
            "The text gives a specific argument for holding back: falling under the "
            "sway of anger would mean falling from ethics, and &lsquo;one who has "
            "fallen from their ethics does not succeed at the highest goal&rsquo; "
            "&mdash; framing the restraint as instrumental to a further aim, not simply "
            "an emotional discipline for its own sake."]),
        ("A body offered up, scattered like hay", [
            "The story closes on its most vivid image: Campeyyaka would rather have his "
            "body broken and &lsquo;scattered in this very place... like hay&rsquo; than "
            "break his ethics &mdash; the same willingness to accept bodily destruction "
            "seen in several of this chapter's other stories, stated here in a single "
            "sharp image rather than an extended argument."]),
    ],
    terms=[
        ("nāga",
         "a serpent being of great psychic power &mdash; the kind of being Campeyyaka, "
         "like Bhūridatta in Cp 12, is described as."),
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the third of ten stories on this theme."),
        ("uposatha",
         "the observance day the snake-charmer is described as keeping, even while "
         "forcing Campeyyaka to perform for a living."),
        ("Campeyyaka Jātaka",
         "the fuller version of this story in the separate Jātaka tradition, not "
         "otherwise covered on this site."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its thirteenth."),
    ],
    text_intro=(
        "The text in full: six verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp13:1.1-1.4"),
        ("p", "&sect;2", "cp13:2.1-2.4"),
        ("p", "&sect;3", "cp13:3.1-3.4"),
        ("p", "&sect;4", "cp13:4.1-4.4"),
        ("p", "&sect;5", "cp13:5.1-5.4"),
        ("p", "&sect;6", "cp13:6.1-6.4"),
    ],
    quiz=[
        {"q": "What does the snake-charmer force Campeyyaka to do?",
         "opts": [
             "Guard the royal treasury",
             "Shift color and perform tricks at the royal gate",
             "Fight other captured animals",
             "Teach him magical secrets"],
         "correct": 1,
         "expl": "Matching whatever color the charmer merely thinks of."},
        {"q": "What abilities does the text say Campeyyaka could have used against his captor?",
         "opts": [
             "None; he is described as having no special power",
             "Turning dry land to water, or reducing the man to ash instantly",
             "Only the ability to escape unnoticed",
             "The power of persuasive speech alone"],
         "correct": 1,
         "expl": "Power deliberately unused, not power he lacked."},
        {"q": "What reasoned argument does the text give for Campeyyaka's restraint?",
         "opts": [
             "No reasoning is given, only raw willpower",
             "Falling under anger would mean falling from ethics, and that person cannot succeed at the highest goal",
             "He was physically too weak to retaliate",
             "He feared punishment from a king"],
         "correct": 1,
         "expl": "Restraint framed as instrumental to a further aim."},
        {"q": "What image closes this story?",
         "opts": [
             "Campeyyaka escaping into the river",
             "His body broken and 'scattered... like hay' rather than his ethics broken",
             "A peaceful reconciliation with the charmer",
             "The charmer being punished by the king"],
         "correct": 1,
         "expl": "A willingness to accept bodily destruction, stated in a single sharp image."},
        {"q": "How does this story compare in length to Cp 12, immediately before it?",
         "opts": [
             "Much longer",
             "Shorter — six verses against Cp 12's nine",
             "Exactly the same length",
             "This story has no verses at all"],
         "correct": 1,
         "expl": "One of the shorter stories in this chapter."},
        {"q": "What was the snake-charmer observing, even while exploiting Campeyyaka?",
         "opts": [
             "A vow of silence",
             "The sabbath (uposatha)",
             "A fast from all food",
             "Nothing is said about his own conduct"],
         "correct": 1,
         "expl": "A detail that sits uneasily alongside his treatment of Campeyyaka."},
        {"q": "What kind of being is Campeyyaka, as described in this text?",
         "opts": [
             "A human ascetic",
             "A nāga, a serpent being of great psychic power",
             "A deity residing in a heavenly realm",
             "An ordinary snake with no special abilities"],
         "correct": 1,
         "expl": "The same kind of being as Cp 12's Bhūridatta."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the third of ten stories on this theme",
             "Truth",
             "Renunciation"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories in this chapter."},
        {"q": "How does this story's basic shape compare to Cp 12's?",
         "opts": [
             "Completely unrelated in theme",
             "Shares the same basic shape — great power held back rather than used against a captor",
             "The opposite theme — a being who does retaliate",
             "This story involves no captor at all"],
         "correct": 1,
         "expl": "A second nāga story following directly on the same pattern."},
        {"q": "What does 'sīla' mean?",
         "opts": [
             "'Ethics' or 'precepts' — the perfection this whole chapter illustrates",
             "'Serpent'",
             "'Performance'",
             "'Anger'"],
         "correct": 0,
         "expl": "The theme uniting all ten stories of this chapter."},
    ],
    marginalia=[
        ("Forced to perform", [
            "shape-shifting",
            "on command"
        ]),
        ("Power unused", [
            "could turn land to water,",
            "or the man to ash"
        ]),
        ("A reasoned restraint", [
            "anger breaks ethics,",
            "ethics reaches the goal"
        ]),
        ("Scattered like hay", [
            "the body offered,",
            "not the precepts"
        ]),
    ],
    further=[
        '<a href="%s/cp13/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-12.html">Cp 12 &mdash; The Dragon Bh&umacr;ridatta&rsquo;s '
        "Conduct</a> &mdash; the text immediately before this one, the collection's "
        "other nāga story.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 14 — Cūḷabodhi Cariyā
# --------------------------------------------------------------------------- #
page(
    14, "C&umacr;&#7735;abodhi Cariy&amacr;", "C&umacr;&#7735;abodhi&rsquo;s Conduct",
    meta_title="Cp 14 — Cūḷabodhi's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Cūḷabodhi's "
        "Conduct, the Cariyapitaka's story of an ascetic who masters his own anger "
        "when his companion is seized by a king. From Ru-Yi Meditation Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (4th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as the ascetic Cūḷabodhi, in and around "
                    "Varanasi"),
        ("Speaker", "The Buddha, recounting his life as Cūḷabodhi"),
        ("Form", "Eleven four-line verses of first-person narration, including quoted "
                 "dialogue with a king"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; an emotionally "
                       "charged story about the moment anger actually arises"),
    ],
    why=(
        "Most of this chapter's stories describe restraint held against an external "
        "threat &mdash; capture, violence, provocation from a stranger. This one is "
        "different: it describes restraint at the exact moment personal anger begins "
        "to rise, when a king forcibly seizes the ascetic Cūḷabodhi's close companion, "
        "a woman he shares no marriage with but a shared renunciation and belief."),
    guide=[
        ("A renunciation shared, not a marriage", [
            "Cūḷabodhi and a brahmin lady both give up worldly life out of fear of "
            "rebirth, and travel together to Varanasi &mdash; the text is explicit that "
            "she is not his wife, only someone who shares his teaching and belief, a "
            "distinction the story insists on before the king who assumes otherwise."]),
        ("Seized on the king's assumption", [
            "A king visiting the royal park sees the brahmin lady, asks whether she is "
            "Cūḷabodhi's wife, and on hearing that she is not, has her seized by force "
            "anyway &mdash; the denial of marriage removing whatever restraint the "
            "king might otherwise have felt, rather than protecting her."]),
        ("Anger named, then stopped", [
            "The story does not pretend Cūḷabodhi felt nothing: &lsquo;I felt so "
            "angry.&rsquo; What follows is not suppression before the fact but an "
            "active act performed as the anger arises &mdash; &lsquo;together with the "
            "arising of anger, I remembered my precepts and vows, and right there "
            "controlled my anger, I did not allow it to grow.&rsquo;"]),
        ("The same denial-then-reason as elsewhere", [
            "The closing verses use the structure seen throughout this collection: "
            "Cūḷabodhi explicitly denies that his restraint came from indifference to "
            "the woman or from weakness, naming the real reason directly &mdash; "
            "&lsquo;because omniscience is precious to me, that's why I guarded my "
            "ethics.&rsquo;"]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the fourth of ten stories on this theme."),
        ("Varanasi",
         "the city Cūḷabodhi and his companion travel to and settle near, in the royal "
         "park."),
        ("kodha",
         "&ldquo;anger&rdquo; &mdash; named directly in this story as something felt, "
         "not denied, and then actively restrained rather than suppressed before it "
         "arose."),
        ("bodhi",
         "&ldquo;awakening&rdquo; &mdash; named as the reason for Cūḷabodhi's restraint "
         "in the story's closing verse, the same reason recurring across this "
         "collection."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its fourteenth."),
    ],
    text_intro=(
        "The text in full: eleven verses, including the king's question and "
        "Cūḷabodhi's reply. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp14:1.1-1.4"),
        ("p", "&sect;2", "cp14:2.1-2.4"),
        ("p", "&sect;3", "cp14:3.1-3.4"),
        ("p", "&sect;4", "cp14:4.1-4.4"),
        ("p", "&sect;5", "cp14:5.1-5.4"),
        ("p", "&sect;6", "cp14:6.1-6.4"),
        ("p", "&sect;7", "cp14:7.1-7.4"),
        ("p", "&sect;8", "cp14:8.1-8.4"),
        ("p", "&sect;9", "cp14:9.1-9.4"),
        ("p", "&sect;10", "cp14:10.1-10.4"),
        ("p", "&sect;11", "cp14:11.1-11.4"),
    ],
    quiz=[
        {"q": "How does this story's central test differ from most others in this chapter?",
         "opts": [
             "It involves no other character at all",
             "It focuses on the exact moment personal anger begins to rise, not an external threat alone",
             "It takes place entirely in a courtroom",
             "It is the only story with no ending given"],
         "correct": 1,
         "expl": "A king forcibly seizes Cūḷabodhi's close companion."},
        {"q": "What relationship does the text specify between Cūḷabodhi and the brahmin lady?",
         "opts": [
             "She is his wife",
             "Not his wife — they share the same teaching and belief",
             "She is his sister",
             "No relationship is described"],
         "correct": 1,
         "expl": "A distinction Cūḷabodhi insists on before the king."},
        {"q": "What does the king do after learning she is not Cūḷabodhi's wife?",
         "opts": [
             "He apologizes and leaves them in peace",
             "He has her seized by force anyway",
             "He offers Cūḷabodhi a reward",
             "He asks Cūḷabodhi's permission first"],
         "correct": 1,
         "expl": "The denial of marriage removes restraint rather than granting protection."},
        {"q": "Does the story claim Cūḷabodhi felt no anger at the seizure?",
         "opts": [
             "Yes, he is described as completely unmoved",
             "No — the text states plainly, 'I felt so angry'",
             "The text never addresses his emotional state",
             "He is described as feeling joy instead"],
         "correct": 1,
         "expl": "The anger is named honestly, not denied."},
        {"q": "What does Cūḷabodhi do once the anger arises?",
         "opts": [
             "Acts on it immediately against the king",
             "Remembers his precepts and vows, and controls the anger right there",
             "Flees the scene entirely",
             "Nothing; the anger simply fades on its own"],
         "correct": 1,
         "expl": "An active act performed as the anger arises, not suppression beforehand."},
        {"q": "What reason does Cūḷabodhi give for guarding his ethics in this situation?",
         "opts": [
             "Indifference to the brahmin lady",
             "Because omniscience is precious to him",
             "Fear of the king's soldiers",
             "A promise made to his teacher"],
         "correct": 1,
         "expl": "The same denial-then-reason structure used throughout this collection."},
        {"q": "What does the text explicitly deny as Cūḷabodhi's motive?",
         "opts": [
             "That he disliked the brahmin lady, or lacked the strength to act",
             "That he was afraid of dying",
             "That he wanted to become king",
             "Nothing is denied in this story"],
         "correct": 0,
         "expl": "Ruling out the obvious misreading before giving the real reason."},
        {"q": "Why did Cūḷabodhi and the brahmin lady renounce worldly life?",
         "opts": [
             "They were exiled by a king",
             "Seeing rebirth as fearful",
             "They lost all their possessions",
             "No reason is given"],
         "correct": 1,
         "expl": "A shared motivation, stated at the story's opening."},
        {"q": "Where do Cūḷabodhi and his companion settle after leaving their village?",
         "opts": [
             "Sāvatthī",
             "Varanasi, in the royal park",
             "Rājagaha",
             "Kapilavatthu"],
         "correct": 1,
         "expl": "Living quietly, mixing with no family or group."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the fourth of ten stories on this theme",
             "Wisdom",
             "Renunciation"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories in this chapter."},
    ],
    marginalia=[
        ("Companions, not spouses", [
            "shared renunciation,",
            "not marriage"
        ]),
        ("Seized regardless", [
            "the denial removed",
            "restraint, not granted it"
        ]),
        ("Anger named honestly", [
            "'I felt so angry' —",
            "then controlled at once"
        ]),
        ("The same closing reason", [
            "'omniscience",
            "is precious to me'"
        ]),
    ],
    further=[
        '<a href="%s/cp14/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-13.html">Cp 13 &mdash; The Dragon Campeyyaka&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 15 — Mahisa Cariyā
# --------------------------------------------------------------------------- #
page(
    15, "Mahisa Cariy&amacr;", "The Buffalo King&rsquo;s Conduct",
    meta_title="Cp 15 — The Buffalo King's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Buffalo "
        "King's Conduct, the Cariyapitaka's story of an animal harassed for days who "
        "refuses to kill his tormentor. From Ru-Yi Meditation Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (5th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as a large forest buffalo"),
        ("Speaker", "The Buddha, recounting his life as the buffalo, with a brief "
                    "exchange between him and a spirit"),
        ("Form", "Eleven four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a plain story with a "
                       "notably practical argument at its center"),
    ],
    why=(
        "A monkey repeatedly soils a resting buffalo &mdash; not once, but day after "
        "day &mdash; while a spirit watching from nearby urges the buffalo to simply "
        "kill him. What makes this story distinctive is not the restraint alone but "
        "the buffalo's reasoning: partly principled, and partly a cold calculation "
        "about what will happen to the monkey regardless."),
    guide=[
        ("Provocation repeated, not sudden", [
            "Unlike a single dramatic threat, this story's provocation is prolonged: "
            "the monkey soils the buffalo's shoulder, forehead, and eyebrows &lsquo;not "
            "just that day, but a second, a third, and a fourth&rsquo;, an ongoing "
            "harassment rather than a single insult."]),
        ("A spirit's advice, refused", [
            "A spirit watching the harassment tells the buffalo directly to kill the "
            "monkey with his horns and hooves. The buffalo's reply reframes the "
            "question: acting on the anger would mean &lsquo;degrading himself&rsquo; "
            "and violating his ethics &mdash; the monkey's wrongdoing does not license "
            "the buffalo's own."]),
        ("A striking line about dying clean", [
            "The buffalo states his position plainly: &lsquo;better to die from purity "
            "than live in shame&rsquo;, followed by a direct question &mdash; &lsquo;how "
            "could I, for the sake of life, harm another?&rsquo; &mdash; treating his "
            "own survival as something that does not automatically outweigh causing "
            "harm."]),
        ("A prediction, not just a principle", [
            "The buffalo's reasoning is not purely idealistic: he predicts that the "
            "monkey will go on to treat others the same way, and someone else will "
            "eventually kill him for it &mdash; a practical expectation that the "
            "monkey's own behavior will catch up with him, without the buffalo needing "
            "to be the one to enact it."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the fifth of ten stories on this theme."),
        ("devatā",
         "&ldquo;spirit&rdquo; or &ldquo;deity&rdquo; &mdash; the figure who watches "
         "the monkey's harassment and urges the buffalo to retaliate."),
        ("khanti",
         "&ldquo;patience&rdquo; &mdash; not one of the perfections given its own "
         "dedicated story in this particular collection, though this story's endurance "
         "of repeated provocation closely resembles it."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its fifteenth."),
        ("puñña",
         "&ldquo;merit&rdquo; &mdash; not named directly in this text, but the implicit "
         "stake behind the buffalo's closing claim that &lsquo;the wise one gains their "
         "heart's desire&rsquo; through forgiving disrespect."),
    ],
    text_intro=(
        "The text in full: eleven verses, including the spirit's advice and the "
        "buffalo's reply. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp15:1.1-1.4"),
        ("p", "&sect;2", "cp15:2.1-2.4"),
        ("p", "&sect;3", "cp15:3.1-3.4"),
        ("p", "&sect;4", "cp15:4.1-4.4"),
        ("p", "&sect;5", "cp15:5.1-5.4"),
        ("p", "&sect;6", "cp15:6.1-6.4"),
        ("p", "&sect;7", "cp15:7.1-7.4"),
        ("p", "&sect;8", "cp15:8.1-8.4"),
        ("p", "&sect;9", "cp15:9.1-9.4"),
        ("p", "&sect;10", "cp15:10.1-10.4"),
        ("p", "&sect;11", "cp15:11.1-11.4"),
    ],
    quiz=[
        {"q": "How does the monkey's provocation of the buffalo unfold?",
         "opts": [
             "A single sudden insult",
             "Repeated harassment over several days, not just once",
             "The monkey never actually bothers the buffalo",
             "A single accidental incident"],
         "correct": 1,
         "expl": "'Not just that day, but a second, a third, and a fourth.'"},
        {"q": "What does the spirit urge the buffalo to do?",
         "opts": [
             "Ignore the monkey entirely",
             "Kill the monkey with his horns and hooves",
             "Report the monkey to a nearby village",
             "Move to a different part of the forest"],
         "correct": 1,
         "expl": "Direct advice to retaliate, which the buffalo refuses."},
        {"q": "How does the buffalo reframe the question of retaliation?",
         "opts": [
             "He agrees the monkey deserves to die",
             "Acting on anger would mean degrading himself — the monkey's wrongdoing doesn't license his own",
             "He says it isn't his responsibility either way",
             "He claims he is physically unable to retaliate"],
         "correct": 1,
         "expl": "Separating his own conduct from the monkey's, rather than mirroring it."},
        {"q": "What does the buffalo say about dying versus living in shame?",
         "opts": [
             "That living in shame is always preferable to dying",
             "'Better to die from purity than live in shame'",
             "That death and shame are equally acceptable",
             "He expresses no preference either way"],
         "correct": 1,
         "expl": "Treating his own survival as not automatically outweighing harm to another."},
        {"q": "What practical prediction does the buffalo make about the monkey?",
         "opts": [
             "That the monkey will eventually apologize",
             "That the monkey will treat others the same way, and someone else will kill him for it",
             "That the monkey will become a buffalo in a future life",
             "No prediction is made"],
         "correct": 1,
         "expl": "A practical expectation, not purely an idealistic principle."},
        {"q": "What is the buffalo's closing claim about forgiving disrespect?",
         "opts": [
             "That it achieves nothing",
             "That 'the wise one gains their heart's desire' through it",
             "That it should only be extended to family members",
             "That it applies only to disrespect from equals"],
         "correct": 1,
         "expl": "Extended explicitly to disrespect 'from the low, middle and high'."},
        {"q": "What term names the quality this story closely resembles, though it is not given its own dedicated story in this collection?",
         "opts": [
             "Wisdom (paññā)",
             "Patience (khanti)",
             "Energy (viriya)",
             "Truth (sacca)"],
         "correct": 1,
         "expl": "Enduring repeated provocation without retaliating."},
        {"q": "Where does the buffalo choose to rest, before the monkey begins harassing him?",
         "opts": [
             "A spot he found while wandering the mighty forest",
             "A village on the edge of the forest",
             "The banks of the Ganges",
             "A cave shared with other buffalo"],
         "correct": 0,
         "expl": "A fine spot he found and settled into."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the fifth of ten stories on this theme",
             "Renunciation",
             "Truth"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories in this chapter."},
        {"q": "What figure other than the buffalo and the monkey appears in this story?",
         "opts": [
             "A king",
             "A spirit (devatā), who urges retaliation",
             "A brahmin ascetic",
             "No other figure appears"],
         "correct": 1,
         "expl": "Watching the harassment and offering advice the buffalo refuses."},
    ],
    marginalia=[
        ("Days of harassment", [
            "not a single insult,",
            "but repeated"
        ]),
        ("A spirit's advice refused", [
            "wrongdoing doesn't license",
            "more wrongdoing"
        ]),
        ("Dying from purity", [
            "rather than living",
            "in shame"
        ]),
        ("A practical prediction", [
            "the monkey's conduct",
            "will catch up with him"
        ]),
    ],
    further=[
        '<a href="%s/cp15/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-14.html">Cp 14 &mdash; C&umacr;&#7735;abodhi&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 16 — Ruru Cariyā
# --------------------------------------------------------------------------- #
page(
    16, "Ruru Cariy&amacr;", "Ruru the Deer King&rsquo;s Conduct",
    meta_title="Cp 16 — Ruru the Deer King's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Ruru the Deer "
        "King's Conduct, the Cariyapitaka's story of a rescuer betrayed for money, who "
        "then shields his betrayer from punishment. From Ru-Yi Meditation Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (6th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as Ruru, a golden deer king living on the "
                    "banks of the Ganges"),
        ("Speaker", "The Buddha, recounting his life as Ruru, with quoted dialogue "
                    "between himself and the man he rescues"),
        ("Form", "Twelve verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a story of betrayal "
                       "that goes further than simple restraint"),
    ],
    why=(
        "Where most of this chapter's stories show restraint against a threat, this "
        "one shows something further: Ruru saves a drowning man at real risk to his "
        "own life, is betrayed by that same man for money, and then, when the king "
        "arrives to kill the betrayer, actively steps in to protect him &mdash; not "
        "mere non-retaliation, but forgiveness that intervenes on the wrongdoer's "
        "behalf."),
    guide=[
        ("A rescue at real cost", [
            "Hearing a man's pitiful cries from the Ganges, Ruru enters the river at "
            "night, &lsquo;surrendering his own life&rsquo;, and drags the man out "
            "&mdash; a man who had jumped in fleeing creditors, thinking &lsquo;I live "
            "or I die&rsquo;."]),
        ("One favor asked, and broken", [
            "Ruru's only request afterward is discretion: &lsquo;tell no-one about "
            "me.&rsquo; Once safely back in the city, the man breaks this single "
            "condition for money, leading the king directly to Ruru."]),
        ("The king ready to kill the informer", [
            "When the king learns what the man did, his response is not to hunt Ruru "
            "gently but to prepare an arrow for the informer himself, calling him "
            "&lsquo;this ignoble betrayer of a friend&rsquo; &mdash; the story briefly "
            "puts the betrayer, not Ruru, in mortal danger."]),
        ("Protection extended to the betrayer himself", [
            "Ruru's response goes beyond forgiving an insult already absorbed: he "
            "actively intervenes, &lsquo;substituting himself&rsquo; to stop the king "
            "from killing the man who had just betrayed him, asking only to &lsquo;carry "
            "out your pleasure&rsquo; instead &mdash; ethics maintained not by enduring "
            "harm passively, but by stepping between a wrongdoer and their punishment."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the sixth of ten stories on this theme."),
        ("Ganges",
         "the river along whose bank Ruru lives, and from which he rescues the "
         "drowning man."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its sixteenth."),
        ("bodhi",
         "&ldquo;awakening&rdquo; &mdash; named as the reason Ruru gives for guarding "
         "his ethics rather than his own life, in the story's closing verse."),
        ("mitta-dubbhī",
         "&ldquo;betrayer of a friend&rdquo; &mdash; the king's own description of the "
         "man who broke Ruru's one request, shortly before Ruru intervenes to save him "
         "from the king's arrow."),
    ],
    text_intro=(
        "The text in full: twelve verses, including the rescued man's explanation and "
        "the king's response. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp16:1.1-1.4"),
        ("p", "&sect;2", "cp16:2.1-2.4"),
        ("p", "&sect;3", "cp16:3.1-3.4"),
        ("p", "&sect;4", "cp16:4.1-4.4"),
        ("p", "&sect;5", "cp16:5.1-5.4"),
        ("p", "&sect;6", "cp16:6.1-6.4"),
        ("p", "&sect;7", "cp16:7.1-7.4"),
        ("p", "&sect;8", "cp16:8.1-8.4"),
        ("p", "&sect;9", "cp16:9.1-9.4"),
        ("p", "&sect;10", "cp16:10.1-10.6"),
        ("p", "&sect;11", "cp16:11.1-11.4"),
        ("p", "&sect;12", "cp16:12.1-12.4"),
    ],
    quiz=[
        {"q": "Why had the man Ruru rescues jumped into the Ganges in the first place?",
         "opts": [
             "He was trying to cross to the other side",
             "He was fleeing his creditors, thinking 'I live or I die'",
             "He was bathing and lost his footing",
             "He was fleeing a wild animal"],
         "correct": 1,
         "expl": "Desperate enough to risk drowning rather than face them."},
        {"q": "At what risk does Ruru rescue the man?",
         "opts": [
             "No risk at all; the rescue is described as effortless",
             "'Surrendering his own life' to enter the river at night",
             "Only a minor inconvenience",
             "He sends someone else to do the rescue"],
         "correct": 1,
         "expl": "A real cost, not a casual gesture."},
        {"q": "What single favor does Ruru ask of the man afterward?",
         "opts": [
             "A share of the man's future wealth",
             "That he tell no one about Ruru",
             "That he never return to that stretch of river",
             "Nothing; Ruru asks for no favor"],
         "correct": 1,
         "expl": "A request the man later breaks for money."},
        {"q": "Why does the man reveal Ruru's location to the king?",
         "opts": [
             "He is forced to under torture",
             "For the sake of money",
             "He is tricked into revealing it",
             "He does not reveal it; Ruru is found by other means"],
         "correct": 1,
         "expl": "Breaking his one promise for personal gain."},
        {"q": "How does the king react on learning what the man did?",
         "opts": [
             "He rewards the man for the information",
             "He prepares to kill the man himself, calling him a betrayer of a friend",
             "He ignores the information entirely",
             "He has the man imprisoned only"],
         "correct": 1,
         "expl": "Briefly putting the betrayer, not Ruru, in mortal danger."},
        {"q": "What does Ruru do when the king is about to kill the informer?",
         "opts": [
             "He allows the punishment to proceed",
             "He substitutes himself, actively intervening to save the man who betrayed him",
             "He flees the scene",
             "He asks the king to imprison the man instead"],
         "correct": 1,
         "expl": "Going beyond enduring the betrayal to actively protecting the betrayer."},
        {"q": "How does this story's ending go further than simple non-retaliation?",
         "opts": [
             "It doesn't; Ruru simply lets the events unfold without acting",
             "Ruru actively steps between a wrongdoer and deserved punishment, rather than only refraining from harm himself",
             "Ruru punishes the man himself instead of the king doing so",
             "The story ends before any resolution"],
         "correct": 1,
         "expl": "Forgiveness that intervenes, not merely restraint absorbed."},
        {"q": "What does Ruru say he guarded, rather than his own life?",
         "opts": [
             "His wealth",
             "His ethics",
             "His reputation",
             "His territory"],
         "correct": 1,
         "expl": "'I guarded my ethics, not my life... because it was solely for awakening.'"},
        {"q": "Where does Ruru live, as described at this story's opening?",
         "opts": [
             "A crowded city",
             "A pleasant, human-free region on the bank of the Ganges",
             "A mountain cave",
             "A royal park"],
         "correct": 1,
         "expl": "Chosen deliberately for its distance from people."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the sixth of ten stories on this theme",
             "Truth",
             "Love"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories in this chapter."},
    ],
    marginalia=[
        ("A rescue at night", [
            "risking his own life",
            "to save a stranger"
        ]),
        ("One favor, broken", [
            "for the sake",
            "of money"
        ]),
        ("The king's arrow", [
            "aimed at the betrayer,",
            "not at Ruru"
        ]),
        ("Protection extended", [
            "to the very man",
            "who betrayed him"
        ]),
    ],
    further=[
        '<a href="%s/cp16/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-15.html">Cp 15 &mdash; The Buffalo King&rsquo;s Conduct</a> &mdash; '
        "the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 17 — Mātaṅga Cariyā
# --------------------------------------------------------------------------- #
page(
    17, "M&amacr;ta&#7749;ga Cariy&amacr;", "M&amacr;ta&#7749;ga&rsquo;s Conduct",
    meta_title="Cp 17 — Mātaṅga's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Mātaṅga's "
        "Conduct, the Cariyapitaka's story of a curse that rebounds on the one who "
        "spoke it, and the ascetic who frees him from it. From Ru-Yi Meditation "
        "Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (7th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as the ascetic Mātaṅga, living upstream on "
                    "the Ganges from another brahmin"),
        ("Speaker", "The Buddha, recounting his life as Mātaṅga"),
        ("Form", "Six four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Mātaṅga is the subject of his own jātaka in the wider "
                              "tradition; this reading guide does not assert a specific "
                              "matching number."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, closing on "
                       "nearly the same formula as Cp 16"),
    ],
    why=(
        "A brahmin curses Mātaṅga's head to split in seven, unprovoked, simply for "
        "having seen his hermitage. Mātaṅga could answer with a glance powerful enough "
        "to reduce the man to ashes &mdash; and instead does something closer to Cp "
        "16's Ruru than to open confrontation: he frees his attacker from the very "
        "curse that attacker spoke against him."),
    guide=[
        ("A curse with no provocation given", [
            "The brahmin's abuse is not a response to anything Mātaṅga has done; "
            "wandering the riverbank, he simply sees the hermitage upstream and curses "
            "its occupant &mdash; the story gives no grievance behind the words, only "
            "the words themselves."]),
        ("A power stated, then set aside", [
            "As in several of this chapter's other stories, the text names the power "
            "being withheld directly: &lsquo;if I were not taking care of my ethics, "
            "then just with a glance I could have reduced him to ashes.&rsquo; The "
            "power is real; the restraint is a choice."]),
        ("A curse that turns back on its speaker", [
            "The story does not simply have the curse fail; it describes the curse "
            "recoiling &lsquo;right back on his own head&rsquo; &mdash; and Mātaṅga's "
            "response to that is not satisfaction at the brahmin's comeuppance but "
            "action: &lsquo;I freed him from that yoke.&rsquo;"]),
        ("The same closing couplet as Cp 16", [
            "This story closes with almost the identical formula that closed Ruru's "
            "story immediately before it: &lsquo;I guarded my ethics, not my life. For "
            "then I was ethical, because it was solely for awakening&rsquo; &mdash; a "
            "shared refrain marking both stories as variations on the same underlying "
            "commitment."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the seventh of ten stories on this theme."),
        ("jaṭila",
         "a &ldquo;matted-hair ascetic&rdquo; &mdash; the description given of Mātaṅga "
         "at this story's opening."),
        ("Ganges",
         "the river along whose banks both Mātaṅga and the cursing brahmin live, "
         "upstream and downstream of each other."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its seventeenth."),
        ("bodhi",
         "&ldquo;awakening&rdquo; &mdash; named as the reason for Mātaṅga's restraint "
         "in the story's closing verse, shared word for word with Cp 16."),
    ],
    text_intro=(
        "The text in full: six verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp17:1.1-1.4"),
        ("p", "&sect;2", "cp17:2.1-2.4"),
        ("p", "&sect;3", "cp17:3.1-3.4"),
        ("p", "&sect;4", "cp17:4.1-4.4"),
        ("p", "&sect;5", "cp17:5.1-5.4"),
        ("p", "&sect;6", "cp17:6.1-6.4"),
    ],
    quiz=[
        {"q": "What provokes the brahmin to curse Mātaṅga?",
         "opts": [
             "A long-standing feud between them",
             "Nothing in particular — he simply sees Mātaṅga's hermitage while wandering",
             "Mātaṅga trespassing on his land",
             "A dispute over water rights"],
         "correct": 1,
         "expl": "The story gives no grievance behind the curse, only the words themselves."},
        {"q": "What does the brahmin's curse threaten?",
         "opts": [
             "That Mātaṅga will lose his hermitage",
             "That Mātaṅga's head will split in seven",
             "That Mātaṅga will be exiled",
             "That Mātaṅga will lose his ascetic powers"],
         "correct": 1,
         "expl": "A specific, violent curse, unprovoked."},
        {"q": "What power does Mātaṅga say he could have used against the brahmin?",
         "opts": [
             "None; he claims no special power",
             "Reducing him to ashes with a single glance",
             "Summoning a storm",
             "Turning him into an animal"],
         "correct": 1,
         "expl": "Named directly, then deliberately set aside."},
        {"q": "What happens to the curse the brahmin speaks?",
         "opts": [
             "It has no effect on anyone",
             "It recoils back onto the brahmin's own head",
             "It strikes Mātaṅga as intended",
             "It is never resolved in the story"],
         "correct": 1,
         "expl": "The curse turns back on its speaker."},
        {"q": "How does Mātaṅga respond once the curse recoils on the brahmin?",
         "opts": [
             "With satisfaction at the brahmin's comeuppance",
             "He acts to free the brahmin from it",
             "He ignores the brahmin's fate entirely",
             "He curses the brahmin in return"],
         "correct": 1,
         "expl": "'I freed him from that yoke' — action, not passive satisfaction."},
        {"q": "How does this story's closing formula relate to Cp 16's?",
         "opts": [
             "They are completely different",
             "Nearly identical — 'I guarded my ethics, not my life... because it was solely for awakening'",
             "This story has no closing formula at all",
             "It directly contradicts Cp 16's closing"],
         "correct": 1,
         "expl": "A shared refrain marking both stories as variations on the same commitment."},
        {"q": "What does 'jaṭila' describe?",
         "opts": [
             "A type of curse",
             "A 'matted-hair ascetic' — the description given of Mātaṅga",
             "A river spirit",
             "A royal title"],
         "correct": 1,
         "expl": "Mātaṅga's identity at the story's opening."},
        {"q": "Where do Mātaṅga and the brahmin live relative to each other?",
         "opts": [
             "In the same village",
             "Upstream and downstream of each other on the Ganges",
             "On opposite sides of a mountain",
             "In neighboring kingdoms"],
         "correct": 1,
         "expl": "Mātaṅga upstream, the brahmin downstream."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the seventh of ten stories on this theme",
             "Truth",
             "Renunciation"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories in this chapter."},
        {"q": "How is Mātaṅga's response distinct from merely enduring the curse?",
         "opts": [
             "It isn't distinct; he does nothing at all",
             "He actively frees the brahmin from the curse's consequences, going beyond passive restraint",
             "He reports the brahmin to a king",
             "He leaves the area permanently"],
         "correct": 1,
         "expl": "Similar to Cp 16's Ruru, restraint that extends into active help for the wrongdoer."},
    ],
    marginalia=[
        ("An unprovoked curse", [
            "no grievance given,",
            "only the words"
        ]),
        ("A glance, unused", [
            "power enough",
            "to reduce him to ashes"
        ]),
        ("The curse recoils", [
            "back onto",
            "its own speaker"
        ]),
        ("Freed, not left cursed", [
            "action taken",
            "on his behalf"
        ]),
    ],
    further=[
        '<a href="%s/cp17/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-16.html">Cp 16 &mdash; Ruru the Deer King&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one, closing on nearly the same "
        "formula.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 18 — Dhammadevaputta Cariyā
# --------------------------------------------------------------------------- #
page(
    18, "Dhammadevaputta Cariy&amacr;", "The Deity Dhamma&rsquo;s Conduct",
    meta_title="Cp 18 — The Deity Dhamma's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Deity "
        "Dhamma's Conduct, the Cariyapitaka's allegorical standoff between a spirit "
        "of righteousness and a spirit of wickedness on a narrow road. From Ru-Yi "
        "Meditation Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (8th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as a great spirit named Dhamma"),
        ("Speaker", "The Buddha, recounting his life as the spirit Dhamma"),
        ("Form", "Eight four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a compact allegory "
                       "worth reading slowly for what it is doing structurally"),
    ],
    why=(
        "This story is more openly allegorical than most of this chapter: a spirit "
        "literally named Dhamma, who establishes people in ethical conduct, collides "
        "on a road with a rival spirit who promotes the opposite &mdash; a standoff "
        "resolved not by combat but by Dhamma simply stepping off the road, letting "
        "the wicked spirit pass."),
    guide=[
        ("A name that states the allegory directly", [
            "Unlike this chapter's animals, ascetics, and kings, this story's central "
            "figure is named for the very quality he embodies: Dhamma, a spirit who "
            "travels &lsquo;establishing the populace in the ten ways of skillful "
            "deeds&rsquo;, with sympathy for the whole world."]),
        ("An opposite number, given equal weight", [
            "The story does not present Dhamma alone; it introduces a mirror-image "
            "rival, a &lsquo;wicked, miserly spirit promoting the ten wicked ways&rsquo;, "
            "traveling the same roads with his own retinue &mdash; the two forces "
            "described almost identically in structure, opposite only in content."]),
        ("A collision framed as a looming war", [
            "When their chariots meet, the language escalates quickly: &lsquo;a "
            "dreadful quarrel ensued&rsquo;, and &lsquo;a great war loomed&rsquo; over "
            "who would be pushed off the road &mdash; the everyday problem of two "
            "parties meeting on a narrow path, inflated to cosmic stakes by what each "
            "party represents."]),
        ("Victory ceded, then delivered anyway", [
            "Dhamma has the power to destroy the wicked spirit and his whole retinue, "
            "and instead steps down off the path, yielding the road entirely. The story "
            "does not end there: once Dhamma has quelled his own mind, &lsquo;the earth "
            "opened up for that wicked spirit&rsquo; &mdash; a consequence that arrives "
            "on its own, not one Dhamma inflicts."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the eighth of ten stories on this theme."),
        ("dasakusalakammapatha",
         "the &ldquo;ten skillful deeds&rdquo; &mdash; the same standard of conduct "
         "named in Cp 3, here actively taught by the spirit Dhamma as he travels."),
        ("devaputta",
         "&ldquo;deity&rdquo; or &ldquo;spirit&rdquo; &mdash; the kind of being both "
         "Dhamma and his wicked rival are described as."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its eighteenth."),
        ("adhamma",
         "&ldquo;wickedness&rdquo; or &ldquo;unrighteousness&rdquo; &mdash; not named "
         "directly as the rival spirit's title in this translation, but the opposite "
         "his &lsquo;ten wicked ways&rsquo; represent to Dhamma's ten skillful ones."),
    ],
    text_intro=(
        "The text in full: eight verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp18:1.1-1.4"),
        ("p", "&sect;2", "cp18:2.1-2.4"),
        ("p", "&sect;3", "cp18:3.1-3.4"),
        ("p", "&sect;4", "cp18:4.1-4.4"),
        ("p", "&sect;5", "cp18:5.1-5.4"),
        ("p", "&sect;6", "cp18:6.1-6.4"),
        ("p", "&sect;7", "cp18:7.1-7.4"),
        ("p", "&sect;8", "cp18:8.1-8.4"),
    ],
    quiz=[
        {"q": "What makes this story more openly allegorical than most in this chapter?",
         "opts": [
             "It has no first-person narration",
             "The central figure is a spirit literally named Dhamma, embodying the quality directly",
             "It is written entirely in prose",
             "It features no other characters at all"],
         "correct": 1,
         "expl": "Named for the very quality he embodies."},
        {"q": "What does Dhamma do as he travels from village to town?",
         "opts": [
             "Collects tribute for a king",
             "Establishes the populace in the ten ways of skillful deeds",
             "Searches for a missing relative",
             "Nothing specific is described"],
         "correct": 1,
         "expl": "Teaching ethical conduct as he goes, with sympathy for the whole world."},
        {"q": "Who does Dhamma encounter on the road?",
         "opts": [
             "A group of merchants",
             "A rival spirit promoting the ten wicked ways",
             "A king seeking his counsel",
             "No one; he travels alone throughout"],
         "correct": 1,
         "expl": "Described in terms that mirror Dhamma's own, opposite only in content."},
        {"q": "How does the text describe the confrontation between the two spirits?",
         "opts": [
             "As a minor, easily resolved disagreement",
             "As 'a dreadful quarrel' where 'a great war loomed'",
             "The two spirits never actually meet",
             "As a friendly negotiation"],
         "correct": 1,
         "expl": "An everyday problem — two parties meeting on a narrow road — inflated to cosmic stakes."},
        {"q": "What power does the text say Dhamma had over his rival?",
         "opts": [
             "None; he was powerless against the wicked spirit",
             "The ability to reduce him and his companions to dust",
             "Only the power to summon others for help",
             "Dhamma is never described as powerful"],
         "correct": 1,
         "expl": "Power deliberately unused, as in several other stories in this chapter."},
        {"q": "What does Dhamma actually do at the standoff?",
         "opts": [
             "Fights and defeats the wicked spirit",
             "Steps down off the road, yielding it entirely to the wicked spirit",
             "Calls on the king to intervene",
             "Retreats and never travels that road again"],
         "correct": 1,
         "expl": "Quelling his own heart rather than asserting his right of way."},
        {"q": "What happens to the wicked spirit after Dhamma yields the road?",
         "opts": [
             "Nothing further happens",
             "The earth opens up for him — a consequence that arrives on its own",
             "He is struck by lightning",
             "He becomes a follower of Dhamma"],
         "correct": 1,
         "expl": "Not something Dhamma inflicts directly."},
        {"q": "What does 'dasakusalakammapatha' refer to in this story?",
         "opts": [
             "The name of the rival spirit",
             "The ten skillful deeds Dhamma actively teaches as he travels",
             "A type of chariot",
             "A location on the road"],
         "correct": 1,
         "expl": "The same standard of conduct named earlier in Cp 3."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the eighth of ten stories on this theme",
             "Wisdom",
             "Resolve"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories in this chapter."},
        {"q": "How does this story's structure compare to others in this chapter?",
         "opts": [
             "It follows the same basic pattern — great power held back rather than used — but stages it as an explicit allegory",
             "It is entirely unrelated in theme to the rest of the chapter",
             "It is the only story in the chapter without any form of restraint shown",
             "It is the only story told in the third person"],
         "correct": 0,
         "expl": "The underlying pattern dressed in more overtly symbolic clothing."},
    ],
    marginalia=[
        ("A name that states it plainly", [
            "a spirit called",
            "Dhamma himself"
        ]),
        ("A mirrored rival", [
            "ten wicked ways",
            "against ten skillful ones"
        ]),
        ("A road, a looming war", [
            "an everyday collision,",
            "inflated to cosmic stakes"
        ]),
        ("Yielded, then resolved", [
            "the earth itself",
            "closes the matter"
        ]),
    ],
    further=[
        '<a href="%s/cp18/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-17.html">Cp 17 &mdash; M&amacr;ta&#7749;ga&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 19 — Alīnasattu Cariyā
# --------------------------------------------------------------------------- #
page(
    19, "Al&imacr;nasattu Cariy&amacr;", "Al&imacr;nasattu&rsquo;s Conduct",
    meta_title="Cp 19 — Alīnasattu's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Alīnasattu's "
        "Conduct, the Cariyapitaka's story of a prince who offers himself to a "
        "cannibal in his father's place. From Ru-Yi Meditation Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (9th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as Prince Alīnasattu, son of King Jayaddisa of "
                    "Kapilā"),
        ("Speaker", "The Buddha, recounting his life as Alīnasattu, with quoted speech "
                    "from his father and to the cannibal"),
        ("Form", "Eleven four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This story is connected to a wider jātaka concerning "
                              "King Jayaddisa; this reading guide does not assert a "
                              "specific matching number."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a story with real "
                       "stakes, resolved in an unusual, deliberately calm register"),
    ],
    why=(
        "King Jayaddisa, seized by a cannibal while hunting, buys a temporary release "
        "by promising to return as prey. His son Alīnasattu, on hearing this, "
        "substitutes himself for his father &mdash; not with weapons or defiance, but "
        "by disarming himself deliberately, so as not to frighten the very man who "
        "intends to eat him."),
    guide=[
        ("A king's desperate bargain", [
            "Jayaddisa is seized without warning &mdash; &lsquo;you are my prey, don't "
            "move&rsquo; &mdash; and secures only a delay by promising to return, a "
            "promise he then relays to his son rather than break."]),
        ("A substitution offered without hesitation", [
            "Alīnasattu bows to his parents and takes his father's place immediately, "
            "&lsquo;tossing my bow and sword&rsquo; before approaching the cannibal "
            "&mdash; the disarming stated as deliberate: carrying weapons, he reasons, "
            "might frighten the cannibal, and frightening him would itself be a "
            "violation of his ethics."]),
        ("Kindness addressed to the one who intends to kill him", [
            "Facing a man who plans to eat him, Alīnasattu speaks &lsquo;lovingly and "
            "beneficially&rsquo;, not with hatred or pleading &mdash; going so far as to "
            "instruct the cannibal on how to prepare the fire himself, as though "
            "managing a practical arrangement rather than facing an execution."]),
        ("An outcome stated, not explained", [
            "The story closes on a claim about lasting consequence &mdash; that "
            "Alīnasattu &lsquo;drove out forever his attacks on living creatures&rsquo; "
            "&mdash; without narrating exactly how the encounter resolves or what "
            "became of Alīnasattu himself. As with several other verse-only stories in "
            "this collection, the outcome is asserted rather than shown."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "story illustrates, the ninth of ten stories on this theme."),
        ("Jayaddisa",
         "the king of Kapilā, Alīnasattu's father, seized by a cannibal while hunting."),
        ("Kapilā",
         "the capital city of the kingdom of Pañcāla, named as Alīnasattu's home."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its nineteenth."),
        ("mettā",
         "&ldquo;loving-kindness&rdquo; &mdash; the quality the text says Alīnasattu "
         "spoke with when addressing the cannibal, rather than hatred or fear."),
    ],
    text_intro=(
        "The text in full: eleven verses, including the king's request and "
        "Alīnasattu's words to the cannibal. Translation: Bhikkhu Sujato (CC0, "
        "SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp19:1.1-1.4"),
        ("p", "&sect;2", "cp19:2.1-2.4"),
        ("p", "&sect;3", "cp19:3.1-3.4"),
        ("p", "&sect;4", "cp19:4.1-4.4"),
        ("p", "&sect;5", "cp19:5.1-5.4"),
        ("p", "&sect;6", "cp19:6.1-6.4"),
        ("p", "&sect;7", "cp19:7.1-7.4"),
        ("p", "&sect;8", "cp19:8.1-8.4"),
        ("p", "&sect;9", "cp19:9.1-9.4"),
        ("p", "&sect;10", "cp19:10.1-10.4"),
        ("p", "&sect;11", "cp19:11.1-11.4"),
    ],
    quiz=[
        {"q": "What happens to King Jayaddisa at the start of this story?",
         "opts": [
             "He is overthrown by rebels",
             "He is seized by a cannibal while hunting",
             "He falls ill",
             "He is captured by a rival king"],
         "correct": 1,
         "expl": "Told plainly: 'You are my prey, don't move.'"},
        {"q": "How does Jayaddisa secure a temporary release?",
         "opts": [
             "By paying a ransom",
             "By promising to return as prey himself",
             "By fighting his way free",
             "By offering his kingdom instead"],
         "correct": 1,
         "expl": "A promise he then relays to his son rather than break."},
        {"q": "What does Alīnasattu do on hearing his father's promise?",
         "opts": [
             "Advises his father to break the promise",
             "Substitutes himself for his father immediately",
             "Sends soldiers to kill the cannibal",
             "Does nothing; the story ends with the father's promise"],
         "correct": 1,
         "expl": "Bowing to his parents and taking his father's place."},
        {"q": "Why does Alīnasattu throw away his weapons before approaching the cannibal?",
         "opts": [
             "He forgets to bring them",
             "Carrying them might frighten the cannibal, which he considers a violation of his ethics",
             "The cannibal demands it",
             "He has no weapons to begin with"],
         "correct": 1,
         "expl": "A deliberate choice, reasoned through explicitly."},
        {"q": "How does Alīnasattu speak to the cannibal?",
         "opts": [
             "With hatred and threats",
             "Lovingly and beneficially",
             "He refuses to speak at all",
             "With desperate pleading for mercy"],
         "correct": 1,
         "expl": "Addressing the man who intends to eat him without hostility."},
        {"q": "What does Alīnasattu instruct the cannibal to do?",
         "opts": [
             "Release him immediately",
             "Kindle a fire, so Alīnasattu can prepare himself to be eaten",
             "Fight him in single combat",
             "Bring him before the king"],
         "correct": 1,
         "expl": "Treated as a practical arrangement rather than an execution to resist."},
        {"q": "What does the story claim about the lasting effect of Alīnasattu's actions?",
         "opts": [
             "Nothing changes as a result",
             "He drove out the cannibal's attacks on living creatures forever",
             "The cannibal kills him and continues as before",
             "The kingdom falls into war"],
         "correct": 1,
         "expl": "Stated as an outcome, though not narrated in detail."},
        {"q": "Does this text explain exactly how the encounter with the cannibal resolves?",
         "opts": [
             "Yes, in full narrative detail",
             "No — like several other verse-only stories in this collection, the outcome is asserted rather than shown",
             "The story is left completely open-ended with no claim at all",
             "It explains the resolution through an extended dialogue"],
         "correct": 1,
         "expl": "A gap similar to what appears elsewhere in this collection's verse-only texts."},
        {"q": "What is Alīnasattu's home kingdom and capital, as named in this text?",
         "opts": [
             "Kosala, capital Sāvatthī",
             "Pañcāla, capital Kapilā",
             "Magadha, capital Rājagaha",
             "Videha, capital Mithilā"],
         "correct": 1,
         "expl": "Named at the story's opening, along with his father Jayaddisa."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Giving",
             "Ethics (sīla), the ninth of ten stories on this theme",
             "Wisdom",
             "Equanimity"],
         "correct": 1,
         "expl": "Continuing the sequence of ten ethics-stories in this chapter."},
    ],
    marginalia=[
        ("A king's desperate promise", [
            "to return",
            "as the cannibal's prey"
        ]),
        ("A son substitutes himself", [
            "weapons tossed aside,",
            "deliberately"
        ]),
        ("Kindness to his killer", [
            "spoken lovingly,",
            "not with hatred"
        ]),
        ("An outcome claimed, not shown", [
            "attacks on living creatures",
            "driven out forever"
        ]),
    ],
    further=[
        '<a href="%s/cp19/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-18.html">Cp 18 &mdash; The Deity Dhamma&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 20 — Saṅkhapāla Cariyā
# --------------------------------------------------------------------------- #
page(
    20, "Sa&#7749;khap&amacr;la Cariy&amacr;", "Sa&#7749;khap&amacr;la&rsquo;s Conduct",
    meta_title="Cp 20 — Saṅkhapāla's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Saṅkhapāla's "
        "Conduct, closing the Cariyapitaka's chapter on ethics with a nāga pierced and "
        "carried away, who could have destroyed his captors instantly. From Ru-Yi "
        "Meditation Center."),
    vagga="The Chapter on an Elephant &middot; The Perfection of Ethics (10th of 10)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first person "
                    "about his past life as the nāga Saṅkhapāla, lord of serpents"),
        ("Speaker", "The Buddha, recounting his life as Saṅkhapāla"),
        ("Form", "Seven four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "Saṅkhapāla is the subject of his own jātaka in the wider "
                              "tradition; this reading guide does not assert a specific "
                              "matching number."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; short, closing the "
                       "chapter on its most extreme image of unused power"),
    ],
    why=(
        "This closing story of the ethics chapter returns almost word for word to Cp "
        "12's opening formula &mdash; a nāga resolving on the four factors and "
        "offering his own body to whoever has use for it &mdash; but pushes the "
        "physical ordeal further: pierced through the nose, tail, and spine, and "
        "fastened to a pole, Saṅkhapāla names a destructive power vast enough to burn "
        "the earth from sea to sea, and uses none of it."),
    guide=[
        ("The same vow as Cp 12, almost word for word", [
            "Saṅkhapāla &lsquo;resolved on the four factors&rsquo; and offers his body "
            "with the identical formula Bhūridatta used in Cp 12: &lsquo;whoever has "
            "use for these, they are already given, please take them&rsquo; &mdash; a "
            "deliberate echo bracketing this chapter's nāga stories together, one near "
            "its start and one at its close."]),
        ("Hunters who take the offer at its cruelest", [
            "The hunters, named as the Bhojans, are described as &lsquo;violent and "
            "pitiless&rsquo;: they pierce Saṅkhapāla's nose, tail, and spine, fasten him "
            "to a pole, and carry him away like an object rather than a being who had "
            "just offered himself freely."]),
        ("A destructive power scaled to the whole earth", [
            "This story states the withheld power in the largest terms of any story in "
            "this chapter: Saṅkhapāla claims he could have burned &lsquo;the earth from "
            "sea to sea, with its forests and mountains&rsquo; with a single blast from "
            "his nose, had he wished to."]),
        ("A chapter closed on its central refrain", [
            "The story's final line states the theme this entire chapter has been "
            "building toward directly: &lsquo;though pierced with stakes, and stabbed "
            "with knives, I did not get upset with the Bhojans: this is my perfection of "
            "ethics.&rsquo; Ten stories of restrained, undischarged power close here on "
            "their clearest single statement of what that restraint is for."]),
    ],
    terms=[
        ("sīla",
         "&ldquo;ethics&rdquo; or &ldquo;precepts&rdquo; &mdash; the perfection this "
         "chapter's ten stories illustrate, closing here with its tenth and final "
         "example."),
        ("nāga",
         "a serpent being of great psychic power &mdash; the same kind of being as Cp "
         "12's Bhūridatta and Cp 13's Campeyyaka, opening and closing this chapter's "
         "trio of nāga stories."),
        ("Bhojans",
         "the violent hunters who capture and pierce Saṅkhapāla, described in this "
         "text as pitiless."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twentieth."),
        ("Hatthinaga-vagga",
         "&ldquo;the Chapter on an Elephant&rdquo; &mdash; this second chapter's "
         "traditional name, closing here after ten stories on ethics."),
    ],
    text_intro=(
        "The text in full: seven verses, closing the Cariyapitaka's chapter on ethics. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp20:1.1-1.4"),
        ("p", "&sect;2", "cp20:2.1-2.4"),
        ("p", "&sect;3", "cp20:3.1-3.4"),
        ("p", "&sect;4", "cp20:4.1-4.4"),
        ("p", "&sect;5", "cp20:5.1-5.4"),
        ("p", "&sect;6", "cp20:6.1-6.4"),
        ("p", "&sect;7", "cp20:7.1-7.4"),
    ],
    quiz=[
        {"q": "What formula does Saṅkhapāla open with, echoing Cp 12's Bhūridatta almost word for word?",
         "opts": [
             "A curse against his future captors",
             "'Whoever has use for these, they are already given, please take them'",
             "A request for a heavenly rebirth",
             "A declaration of war against the Bhojans"],
         "correct": 1,
         "expl": "A deliberate echo bracketing this chapter's nāga stories."},
        {"q": "Who captures Saṅkhapāla, and how are they described?",
         "opts": [
             "Peaceful farmers, described as gentle",
             "The Bhojans, described as violent and pitiless hunters",
             "A king's soldiers, acting on royal orders",
             "Fellow nāgas"],
         "correct": 1,
         "expl": "Taking his offer in the cruelest possible way."},
        {"q": "How is Saṅkhapāla physically treated by his captors?",
         "opts": [
             "He is left entirely unharmed",
             "Pierced through the nose, tail, and spine, and fastened to a pole",
             "He is offered food and gentle care",
             "He is released immediately"],
         "correct": 1,
         "expl": "Carried away like an object rather than a being who had offered himself freely."},
        {"q": "What scale of destructive power does Saṅkhapāla claim he could have used?",
         "opts": [
             "None; he claims no special power",
             "Burning the entire earth, from sea to sea, with a blast from his nose",
             "Only enough to injure a single attacker",
             "The power to vanish and escape unnoticed"],
         "correct": 1,
         "expl": "The largest scale of withheld power in this whole chapter."},
        {"q": "What is the story's final statement of its own theme?",
         "opts": [
             "'This is the highest blessing'",
             "'I did not get upset with the Bhojans: this is my perfection of ethics'",
             "'By this truth, may you be well'",
             "'Through this they have it all'"],
         "correct": 1,
         "expl": "The clearest single statement of the whole chapter's theme, at its close."},
        {"q": "What does Saṅkhapāla have in common structurally with Cp 12's Bhūridatta?",
         "opts": [
             "Nothing; the two stories are unrelated",
             "Both resolve on the four factors and offer their bodies with nearly identical wording",
             "Both stories end in the character's death",
             "Both are set in the same city"],
         "correct": 1,
         "expl": "Opening and closing this chapter's trio of nāga stories with matching formulas."},
        {"q": "What perfection does this story close out?",
         "opts": [
             "Giving, the first chapter's theme",
             "Ethics (sīla), the tenth and final story of this chapter",
             "Truth",
             "Renunciation"],
         "correct": 1,
         "expl": "Ten stories on ethics conclude here."},
        {"q": "What is the traditional name of the chapter this story closes?",
         "opts": [
             "Akitti-vagga",
             "Hatthinaga-vagga, 'the Chapter on an Elephant'",
             "Yudhañjaya-vagga",
             "No traditional name is given"],
         "correct": 1,
         "expl": "Named for its opening story, Cp 11's elephant."},
        {"q": "How many nāga stories appear across this chapter, and where do they fall?",
         "opts": [
             "Just this one, at the very end",
             "Three — Cp 12, Cp 13, and this closing story, Cp 20",
             "None; Saṅkhapāla is the only serpent-being in the collection",
             "All ten stories in this chapter feature nāgas"],
         "correct": 1,
         "expl": "Bhūridatta and Campeyyaka near the chapter's start, Saṅkhapāla at its close."},
        {"q": "What kind of being is a 'nāga', as this text uses the term?",
         "opts": [
             "An ordinary snake with no special powers",
             "A serpent being of great psychic power",
             "A human ascetic who has taken a serpent's form permanently",
             "A minor forest spirit"],
         "correct": 1,
         "expl": "The same kind of being as Bhūridatta and Campeyyaka earlier in this chapter."},
    ],
    marginalia=[
        ("The same vow as Cp 12", [
            "'already given,",
            "please take them'"
        ]),
        ("Pierced and carried away", [
            "an offer taken",
            "at its cruelest"
        ]),
        ("Power enough for the earth", [
            "sea to sea,",
            "unused"
        ]),
        ("The chapter's clearest line", [
            "'this is my",
            "perfection of ethics'"
        ]),
    ],
    further=[
        '<a href="%s/cp20/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-12.html">Cp 12 &mdash; The Dragon Bh&umacr;ridatta&rsquo;s '
        "Conduct</a> &mdash; the story this one echoes almost word for word, opening "
        "this chapter's trio of nāga stories.",
        '<a href="cp-19.html">Cp 19 &mdash; Al&imacr;nasattu&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="./">Cariyapiṭaka</a> &mdash; back to the collection index.',
    ],
)


# --------------------------------------------------------------------------- #
# Cp 21 — Yudhañjaya Cariyā
# --------------------------------------------------------------------------- #
page(
    21, "Yudha&ntilde;jaya Cariy&amacr;", "Yudha&ntilde;jaya&rsquo;s Conduct",
    meta_title="Cp 21 — Yudhañjaya's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Yudhañjaya's "
        "Conduct, opening the Cariyapitaka's third and final chapter with a prince who "
        "renounces a kingdom over a single dewdrop. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Renunciation (1st of 5)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as Prince Yudhañjaya"),
        ("Speaker", "The Buddha, recounting his life as Yudhañjaya"),
        ("Form", "Six four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short and direct, "
                       "opening the collection's third and final chapter"),
    ],
    why=(
        "This story opens the Cariyapitaka's third and final chapter, gathering the "
        "remaining perfections &mdash; renunciation, resolve, truth, love, and "
        "equanimity &mdash; across its final fifteen stories. It opens on the smallest "
        "possible trigger: a single dewdrop, evaporating in the heat of the sun, is "
        "enough to move a prince to give up an entire kingdom."),
    guide=[
        ("A third chapter, five more themes", [
            "After ten stories on giving and ten on ethics, this final chapter covers "
            "five different perfections across its fifteen stories: renunciation (five "
            "stories), resolve (one), truth (six), love (two), and equanimity (one) "
            "&mdash; opening here with renunciation."]),
        ("A single dewdrop as the trigger", [
            "Nothing dramatic precipitates Yudhañjaya's decision: seeing a dewdrop fall "
            "and vanish in the sun's heat is enough to stir him with <em>saṃvega</em>, "
            "the same sudden sense of urgency named directly in Kp 5 of the "
            "Khuddakapatha and Cp 7's Prince Candana &mdash; here triggered by nothing "
            "more than ordinary weather."]),
        ("A kingdom offered back, and refused", [
            "As Yudhañjaya prepares to leave, the citizens themselves beg him to stay "
            "and rule &mdash; the kingdom is not lost or threatened, it is actively "
            "being offered, making his refusal a clean renunciation rather than an "
            "escape from difficulty."]),
        ("The same denial-then-reason closing", [
            "As in many stories across this collection, the ending states plainly what "
            "the renunciation was not about: &lsquo;I had no dislike of my parents, nor "
            "did I dislike the great fame. But because omniscience is precious to me, "
            "that is why I forsook kingship.&rsquo;"]),
    ],
    terms=[
        ("nekkhamma",
         "&ldquo;renunciation&rdquo; &mdash; the perfection this story illustrates, "
         "opening this chapter's five stories on the theme."),
        ("saṃvega",
         "a sudden &ldquo;sense of urgency&rdquo; &mdash; the same reaction named in Kp "
         "5 and Cp 7, here triggered by the sight of a single evaporating dewdrop."),
        ("Yudhañjaya-vagga",
         "&ldquo;the Chapter With Yudhañjaya&rdquo; &mdash; the traditional name of "
         "this third and final chapter, taken from this opening story."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-first."),
        ("pabbajjā",
         "&ldquo;going forth&rdquo; &mdash; the formal act of renunciation Yudhañjaya "
         "requests permission for from his parents."),
    ],
    text_intro=(
        "The text in full: six verses, opening the Cariyapitaka's third chapter. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp21:1.1-1.4"),
        ("p", "&sect;2", "cp21:2.1-2.4"),
        ("p", "&sect;3", "cp21:3.1-3.4"),
        ("p", "&sect;4", "cp21:4.1-4.4"),
        ("p", "&sect;5", "cp21:5.1-5.4"),
        ("p", "&sect;6", "cp21:6.1-6.4"),
    ],
    quiz=[
        {"q": "What triggers Yudhañjaya's decision to renounce his kingdom?",
         "opts": [
             "A war that destroys his city",
             "Seeing a single dewdrop evaporate in the sun's heat",
             "The death of his father",
             "A prophecy delivered by a seer"],
         "correct": 1,
         "expl": "Nothing dramatic — an ordinary moment of weather."},
        {"q": "What perfection does this story open, and how many stories does this final chapter cover in total across five themes?",
         "opts": [
             "Ethics; ten stories on one theme",
             "Renunciation; fifteen stories across five perfections",
             "Giving; ten stories on one theme",
             "Truth; six stories on one theme"],
         "correct": 1,
         "expl": "Renunciation (five stories), resolve (one), truth (six), love (two), and equanimity (one)."},
        {"q": "How do the citizens respond to Yudhañjaya's decision to leave?",
         "opts": [
             "They are relieved to be rid of him",
             "They beg him to stay and rule, actively offering him the kingdom",
             "They immediately crown a replacement",
             "No response from the citizens is described"],
         "correct": 1,
         "expl": "Making his refusal a clean renunciation, not an escape from a lost kingdom."},
        {"q": "What term names the sudden reaction that moves Yudhañjaya to act?",
         "opts": [
             "Mettā",
             "Saṃvega, a sense of urgency",
             "Khanti",
             "Upekkhā"],
         "correct": 1,
         "expl": "The same term used in Kp 5 of the Khuddakapatha and Cp 7's Prince Candana."},
        {"q": "What does Yudhañjaya explicitly deny as his reason for leaving?",
         "opts": [
             "That he disliked his parents or the fame of kingship",
             "That he was capable of ruling",
             "That the kingdom was prosperous",
             "Nothing is denied in this story"],
         "correct": 0,
         "expl": "The same denial-then-reason structure used throughout this collection."},
        {"q": "What is the traditional name of this third and final chapter, taken from this story?",
         "opts": [
             "Akitti-vagga",
             "Hatthinaga-vagga",
             "Yudhañjaya-vagga, 'the Chapter With Yudhañjaya'",
             "No traditional name is given"],
         "correct": 2,
         "expl": "Named for its opening story, as the first two chapters were."},
        {"q": "What formal act does Yudhañjaya request permission for from his parents?",
         "opts": [
             "Marriage",
             "Pabbajjā, 'going forth' into renunciation",
             "A military campaign",
             "A pilgrimage"],
         "correct": 1,
         "expl": "Bowing to them before departing."},
        {"q": "What perfection did the second chapter of the Cariyapitaka cover?",
         "opts": [
             "Giving",
             "Ethics (sīla)",
             "Truth",
             "Love"],
         "correct": 1,
         "expl": "Cp 11 through Cp 20, now followed by this final chapter's five themes."},
        {"q": "How does this story's structure compare to Cp 7's Prince Candana?",
         "opts": [
             "Completely unrelated",
             "Both name saṃvega as the trigger for a decisive renunciation",
             "Both stories involve a cannibal",
             "Both are the longest stories in their chapters"],
         "correct": 1,
         "expl": "A sudden sense of urgency, shared across otherwise very different stories."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Renunciation (nekkhamma), the first of five stories on this theme",
             "Resolve",
             "Equanimity",
             "Ethics"],
         "correct": 0,
         "expl": "Opening the third chapter's first theme."},
    ],
    marginalia=[
        ("A single dewdrop", [
            "enough to stir",
            "a sense of urgency"
        ]),
        ("A kingdom offered", [
            "not lost —",
            "actively refused"
        ]),
        ("The third chapter opens", [
            "renunciation, resolve,",
            "truth, love, equanimity"
        ]),
        ("The same closing denial", [
            "not dislike, but",
            "omniscience precious"
        ]),
    ],
    further=[
        '<a href="%s/cp21/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-20.html">Cp 20 &mdash; Sa&#7749;khap&amacr;la&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one, closing the chapter on ethics.",
        '<a href="cp-7.html">Cp 7 &mdash; Prince Candana&rsquo;s Conduct</a> &mdash; '
        "another story triggered by a sudden sense of urgency (saṃvega).",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 22 — Somanassa Cariyā
# --------------------------------------------------------------------------- #
page(
    22, "Somanassa Cariy&amacr;", "Somanassa&rsquo;s Conduct",
    meta_title="Cp 22 — Somanassa's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Somanassa's "
        "Conduct, the Cariyapitaka's story of a prince falsely accused, nearly "
        "executed, who forgives the king and renounces the throne. From Ru-Yi "
        "Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Renunciation (2nd of 5)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as Prince Somanassa of Indapatta"),
        ("Speaker", "The Buddha, recounting his life as Somanassa, with quoted "
                    "dialogue involving a fraudulent ascetic and a king"),
        ("Form", "Seventeen verses of first-person narration"),
        ("Length", "2&ndash;3 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a story of false "
                       "accusation and near-execution, resolved unexpectedly"),
    ],
    why=(
        "This story's renunciation does not come from a quiet moment of reflection "
        "like Cp 21's dewdrop; it comes after Somanassa is falsely accused by a "
        "fraudulent ascetic, sentenced to execution by his own father, and dragged "
        "from his mother's arms &mdash; and only afterward, having survived and "
        "forgiven the king who condemned him, chooses to leave the throne behind "
        "entirely."),
    guide=[
        ("A charlatan recognized for what he is", [
            "Before any accusation is made, Somanassa already sees through the "
            "ascetic his father favors: &lsquo;like a pile of chaff without grain, "
            "like a hollow tree&rsquo;, someone who has &lsquo;left the bright "
            "qualities of conscience for the sake of making a living&rsquo;."]),
        ("A polite visit, met with a death threat", [
            "Sent by his father to attend to the ascetic's needs, Somanassa's simple, "
            "courteous offer of help is met with fury and a threat: &lsquo;I'll have "
            "you killed right now! Or banished from the realm!&rsquo;"]),
        ("A father's order, carried out on a lie", [
            "The charlatan lies to the returning king, and the king &mdash; without "
            "verifying anything &mdash; orders his own son's execution in the most "
            "brutal terms, his body to be quartered and displayed &lsquo;from street "
            "to street&rsquo; as a warning."]),
        ("An unexpected reversal, then a deliberate departure", [
            "Somanassa manages to be brought before the king in time to plead his own "
            "case, and succeeds not only in surviving but in winning the king's "
            "confidence entirely &mdash; the king asks his forgiveness and offers him "
            "the kingdom outright. Somanassa's renunciation, when it comes, is chosen "
            "freely, after both survival and reconciliation, not forced by continued "
            "danger."]),
    ],
    terms=[
        ("nekkhamma",
         "&ldquo;renunciation&rdquo; &mdash; the perfection this story illustrates, "
         "the second of five stories on this theme."),
        ("Indapatta",
         "the capital city named as Somanassa's home, the same city named in Cp 3's "
         "story of King Dhanañjaya."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-second."),
        ("saññatta",
         "not named directly in this translation, but the underlying idea behind "
         "Somanassa &lsquo;persuading&rsquo; and &lsquo;bringing under his "
         "influence&rsquo; the king who had just ordered his execution."),
        ("pabbajjā",
         "&ldquo;going forth&rdquo; &mdash; the renunciation Somanassa chooses only "
         "after being offered, and declining, the kingdom itself."),
    ],
    text_intro=(
        "The text in full: seventeen verses, including the charlatan's threat and "
        "the king's fatal order. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A charlatan recognized"),
        ("p", "&sect;1", "cp22:1.1-1.4"),
        ("p", "&sect;2", "cp22:2.1-2.4"),
        ("p", "&sect;3", "cp22:3.1-3.4"),
        ("p", "&sect;4", "cp22:4.1-4.4"),
        ("p", "&sect;5", "cp22:5.1-5.4"),
        ("h3", "A death sentence on a lie"),
        ("p", "&sect;6", "cp22:6.1-6.4"),
        ("p", "&sect;7", "cp22:7.1-7.4"),
        ("p", "&sect;8", "cp22:8.1-8.4"),
        ("p", "&sect;9", "cp22:9.1-9.4"),
        ("p", "&sect;10", "cp22:10.1-10.4"),
        ("p", "&sect;11", "cp22:11.1-11.4"),
        ("p", "&sect;12", "cp22:12.1-12.4"),
        ("p", "&sect;13", "cp22:13.1-13.4"),
        ("h3", "A reversal, then a chosen departure"),
        ("p", "&sect;14", "cp22:14.1-14.4"),
        ("p", "&sect;15", "cp22:15.1-15.4"),
        ("p", "&sect;16", "cp22:16.1-16.4"),
        ("p", "&sect;17", "cp22:17.1-17.4"),
    ],
    quiz=[
        {"q": "How does Somanassa initially regard the ascetic his father favors?",
         "opts": [
             "With great respect and admiration",
             "As a charlatan — 'like a pile of chaff without grain'",
             "He has never encountered the ascetic before the crisis",
             "As a close personal friend"],
         "correct": 1,
         "expl": "Recognized as fraudulent before any accusation is made."},
        {"q": "What happens when Somanassa politely offers to help the ascetic?",
         "opts": [
             "The ascetic thanks him warmly",
             "The ascetic threatens to have him killed or banished",
             "The ascetic ignores him entirely",
             "The ascetic reports him for good behavior"],
         "correct": 1,
         "expl": "Fury at what should have been an unremarkable courtesy."},
        {"q": "What does the king order after hearing the ascetic's accusation?",
         "opts": [
             "An investigation into the truth of the claim",
             "His own son's execution, without verifying anything",
             "A public trial",
             "Nothing; the king dismisses the accusation"],
         "correct": 1,
         "expl": "A brutal sentence, ordered entirely on a lie."},
        {"q": "How does Somanassa survive the execution order?",
         "opts": [
             "He escapes and flees the kingdom",
             "He manages to be brought before the king in time to plead his own case",
             "His mother intervenes and stops the execution",
             "The executioners refuse to carry out the order"],
         "correct": 1,
         "expl": "Winning the king's confidence entirely, not merely escaping punishment."},
        {"q": "What does the king offer Somanassa after learning the truth?",
         "opts": [
             "Nothing; he simply apologizes",
             "His forgiveness, and the kingdom itself",
             "Exile to a distant province",
             "A public ceremony of apology only"],
         "correct": 1,
         "expl": "A full reversal from execution order to offered throne."},
        {"q": "When does Somanassa's renunciation actually happen?",
         "opts": [
             "While still under threat of execution",
             "Only after surviving and being offered the kingdom outright",
             "Before the false accusation is even made",
             "He never actually renounces the throne"],
         "correct": 1,
         "expl": "A choice made freely, after both survival and reconciliation."},
        {"q": "What does Somanassa explicitly deny as his reason for leaving?",
         "opts": [
             "That he disliked great kingship or sensual enjoyment",
             "That he trusted his father",
             "That the kingdom was safe",
             "Nothing is denied in this story"],
         "correct": 0,
         "expl": "The same denial-then-reason structure used throughout this collection."},
        {"q": "Where is Somanassa's home city, also named in Cp 3's story?",
         "opts": [
             "Mithilā",
             "Indapatta",
             "Varanasi",
             "Kapilā"],
         "correct": 1,
         "expl": "The same capital as King Dhanañjaya's in Cp 3."},
        {"q": "How is Somanassa treated as he is taken away for execution?",
         "opts": [
             "With gentle care throughout",
             "Dragged from his mother's lap by fierce, violent, and pitiless punishers",
             "He is allowed to say a lengthy farewell",
             "He is not physically restrained at all"],
         "correct": 1,
         "expl": "A stark, sudden reversal from his life as a loved and cherished child."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Renunciation (nekkhamma), the second of five stories on this theme",
             "Truth",
             "Resolve"],
         "correct": 1,
         "expl": "Continuing the sequence of five renunciation-stories in this chapter."},
    ],
    marginalia=[
        ("A charlatan exposed", [
            "recognized before",
            "any accusation"
        ]),
        ("A death sentence on a lie", [
            "ordered by his own father,",
            "unverified"
        ]),
        ("Forgiveness, then a throne offered", [
            "survival becomes",
            "reconciliation"
        ]),
        ("Renunciation freely chosen", [
            "only after",
            "the kingdom was his"
        ]),
    ],
    further=[
        '<a href="%s/cp22/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-21.html">Cp 21 &mdash; Yudha&ntilde;jaya&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="cp-3.html">Cp 3 &mdash; Kur&umacr;r&amacr;ja&rsquo;s Conduct</a> '
        "&mdash; another story set in Indapatta.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 23 — Ayoghara Cariyā
# --------------------------------------------------------------------------- #
page(
    23, "Ayoghara Cariy&amacr;", "Ayoghara&rsquo;s Conduct",
    meta_title="Cp 23 — Ayoghara's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Ayoghara's "
        "Conduct, the Cariyapitaka's story of a prince raised in confinement who "
        "refuses the throne offered as compensation. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Renunciation (3rd of 5)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as Prince Ayoghara of Kāsi"),
        ("Speaker", "The Buddha, recounting his life as Ayoghara, addressing a crowd "
                    "that has just offered him the throne"),
        ("Form", "Ten four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a reflective refusal "
                       "built on an unusual, unexplained childhood"),
    ],
    why=(
        "This prince's name states his own origin plainly: Ayoghara, &lsquo;iron "
        "house&rsquo;, raised in confinement for reasons the text never explains. When "
        "the kingdom is offered to him as if it were compensation for that painful "
        "childhood, he refuses it on grounds that go further than personal history "
        "&mdash; a reflection on the vulnerability of every living creature, "
        "regardless of birth or rank."),
    guide=[
        ("A childhood the text does not explain", [
            "Ayoghara's name and history are stated as fact &mdash; raised in an iron "
            "house, &lsquo;scarcely lit by sun or moon&rsquo; &mdash; without the text "
            "offering any reason why. As with several other stories in this collection, "
            "a striking premise is presented without its backstory."]),
        ("A throne offered as if it could compensate", [
            "The king's offer treats kingship as recompense: &lsquo;your life has been "
            "a painful one, as you've been raised in confinement. Today, my son, rule "
            "the entirety of this land.&rsquo; Ayoghara's answer does not accept that "
            "framing."]),
        ("An argument that reaches beyond his own case", [
            "Rather than simply declining, Ayoghara generalizes his refusal into an "
            "observation about everyone: &lsquo;all the creatures of this earth "
            "&mdash; low, middle, or high &mdash; are unprotected in their own home, in "
            "which they grew up with their families.&rsquo; His own confinement becomes "
            "an unusually literal case of a vulnerability he says is universal."]),
        ("A body found repugnant before any suffering caused by others", [
            "Ayoghara's disillusionment does not stop at his own biography: he recalls "
            "entering the world &lsquo;filled with rotting carcass&rsquo; from the "
            "womb itself, before the iron house is even mentioned again &mdash; ordinary "
            "birth described in the same register as his unusual confinement."]),
    ],
    terms=[
        ("nekkhamma",
         "&ldquo;renunciation&rdquo; &mdash; the perfection this story illustrates, "
         "the third of five stories on this theme."),
        ("Ayoghara",
         "&ldquo;iron house&rdquo; &mdash; this prince's own name, describing the "
         "unexplained confinement of his childhood."),
        ("Kāsi",
         "the kingdom Ayoghara is the true-born son of the king of, the same kingdom "
         "named in Cp 26's story of Temiya."),
        ("nibbāna",
         "&ldquo;quenching&rdquo; or &ldquo;extinguishment&rdquo; &mdash; named "
         "directly as what Ayoghara says he will seek, where death will not reach "
         "him."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-third."),
    ],
    text_intro=(
        "The text in full: ten verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp23:1.1-1.4"),
        ("p", "&sect;2", "cp23:2.1-2.4"),
        ("p", "&sect;3", "cp23:3.1-3.4"),
        ("p", "&sect;4", "cp23:4.1-4.4"),
        ("p", "&sect;5", "cp23:5.1-5.4"),
        ("p", "&sect;6", "cp23:6.1-6.4"),
        ("p", "&sect;7", "cp23:7.1-7.4"),
        ("p", "&sect;8", "cp23:8.1-8.4"),
        ("p", "&sect;9", "cp23:9.1-9.4"),
        ("p", "&sect;10", "cp23:10.1-10.4"),
    ],
    quiz=[
        {"q": "What does the name 'Ayoghara' mean, and what does it describe?",
         "opts": [
             "'Golden throne' — a symbol of his eventual kingship",
             "'Iron house' — the unexplained confinement of his childhood",
             "'Wise one' — a title earned through study",
             "'Forest wanderer' — his life after leaving the palace"],
         "correct": 1,
         "expl": "A striking premise the text never explains."},
        {"q": "How does the king frame his offer of the throne to Ayoghara?",
         "opts": [
             "As a test of his abilities",
             "As compensation for his painful, confined childhood",
             "As a punishment",
             "No offer of the throne is made"],
         "correct": 1,
         "expl": "'Your life has been a painful one... today, my son, rule the entirety of this land.'"},
        {"q": "How does Ayoghara's refusal go beyond simply declining the offer?",
         "opts": [
             "He does not explain his refusal at all",
             "He generalizes it into an observation about all creatures being unprotected",
             "He blames his father directly for his confinement",
             "He demands a different kind of compensation"],
         "correct": 1,
         "expl": "His own literal confinement becomes a case of a vulnerability he calls universal."},
        {"q": "What does Ayoghara say about his birth itself?",
         "opts": [
             "That it was a joyous, celebrated occasion",
             "That he escaped his mother's womb 'filled with rotting carcass'",
             "That he does not remember his own birth",
             "Nothing is said about his birth"],
         "correct": 1,
         "expl": "Ordinary birth described in the same register as his unusual confinement."},
        {"q": "What does Ayoghara say he will seek instead of kingship?",
         "opts": [
             "A different kingdom to rule",
             "Quenching (nibbāna), where death will not crush him",
             "Revenge against those who confined him",
             "A simple life as a farmer"],
         "correct": 1,
         "expl": "Named directly as his goal."},
        {"q": "What kingdom is Ayoghara the true-born son of, also named in Cp 26?",
         "opts": [
             "Indapatta",
             "Kāsi",
             "Mithilā",
             "Kapilā"],
         "correct": 1,
         "expl": "The same kingdom as Cp 26's Temiya."},
        {"q": "How does the crowd react as Ayoghara leaves for the forest?",
         "opts": [
             "With indifference",
             "Wailing, as he departs like a bull elephant bursting his ropes",
             "With celebration",
             "No reaction is described"],
         "correct": 1,
         "expl": "A dramatic departure despite the crowd's grief."},
        {"q": "What does Ayoghara explicitly deny as his reason for leaving?",
         "opts": [
             "That he disliked his parents or the great fame",
             "That he wanted to rule elsewhere",
             "That the kingdom was too small",
             "Nothing is denied in this story"],
         "correct": 0,
         "expl": "The same denial-then-reason structure used throughout this collection."},
        {"q": "How does this story compare to Cp 21's Yudhañjaya?",
         "opts": [
             "Both are triggered by an ordinary dewdrop",
             "Both renounce kingship, but this story is built on an unusual, unexplained personal history rather than a small ordinary trigger",
             "There is no meaningful comparison possible",
             "Ayoghara refuses to renounce anything"],
         "correct": 1,
         "expl": "A different route to the same chapter's theme of renunciation."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Renunciation (nekkhamma), the third of five stories on this theme",
             "Truth",
             "Love"],
         "correct": 1,
         "expl": "Continuing the sequence of five renunciation-stories in this chapter."},
    ],
    marginalia=[
        ("An iron house", [
            "confinement never",
            "explained by the text"
        ]),
        ("A throne as compensation", [
            "offered, and",
            "refused"
        ]),
        ("A universal vulnerability", [
            "'low, middle, or high' —",
            "all unprotected"
        ]),
        ("Seeking what death cannot reach", [
            "quenching,",
            "not kingship"
        ]),
    ],
    further=[
        '<a href="%s/cp23/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-22.html">Cp 22 &mdash; Somanassa&rsquo;s Conduct</a> &mdash; the '
        "text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 24 — Bhisa Cariyā
# --------------------------------------------------------------------------- #
page(
    24, "Bhisa Cariy&amacr;", "The Conduct of the Lotus-eaters",
    meta_title="Cp 24 — The Conduct of the Lotus-eaters | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Conduct of "
        "the Lotus-eaters, the Cariyapitaka's story of an entire family choosing "
        "renunciation together. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Renunciation (4th of 5)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as the eldest of eight siblings in "
                    "Kāsi"),
        ("Speaker", "The Buddha, recounting his life as the eldest sibling, with "
                    "quoted dialogue from his family"),
        ("Form", "Eight four-line verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a quiet story about "
                       "an unusually collective decision"),
    ],
    why=(
        "This story's title refers to a detail this particular verse text never "
        "actually mentions &mdash; the lotus roots the fuller tradition has this "
        "family living on afterward. What this text does show is unusual on its own "
        "terms: rather than one figure renouncing alone against family objection, an "
        "entire household &mdash; two parents, eight children &mdash; chooses "
        "renunciation together."),
    guide=[
        ("A title this text doesn't fully explain", [
            "&lsquo;The Conduct of the Lotus-eaters&rsquo; names a detail from the "
            "fuller telling of this story &mdash; presumably how the family sustains "
            "itself once in the forest &mdash; that this particular verse text never "
            "actually states. As elsewhere in this collection, the title points past "
            "what the surviving verses cover."]),
        ("An objection raised, and firmly declined", [
            "When the eldest sibling refuses ordinary family life, the objection is "
            "not hostile: friends and parents simply ask him to &lsquo;maintain the "
            "family lineage&rsquo;. His refusal is nonetheless final, described as "
            "&lsquo;hard for me to hear, like a heated ploughshare&rsquo; &mdash; the "
            "discomfort running in both directions."]),
        ("A family that follows rather than mourns", [
            "Where Cp 21 and Cp 23 both show crowds wailing at a departure, this story "
            "takes a different turn: on hearing of their son's decision, the parents "
            "respond not with grief but with a proposal of their own &mdash; "
            "&lsquo;sirs, let all of us go forth!&rsquo;"]),
        ("Renunciation as a shared decision, not a solitary one", [
            "The story closes with the entire family &mdash; mother, father, sister, "
            "and seven brothers &mdash; discarding their wealth and entering the "
            "forest together, a scale of collective renunciation not seen anywhere "
            "else in this collection's other stories on the theme."]),
    ],
    terms=[
        ("nekkhamma",
         "&ldquo;renunciation&rdquo; &mdash; the perfection this story illustrates, "
         "the fourth of five stories on this theme."),
        ("bhisa",
         "&ldquo;lotus root&rdquo; or &ldquo;lotus fibre&rdquo; &mdash; the detail "
         "behind this story's title, referring to material not covered in this "
         "particular verse text."),
        ("Kāsi",
         "the kingdom named as this family's home, the same kingdom as Cp 23's "
         "Ayoghara and Cp 26's Temiya."),
        ("kula-vaṁsa",
         "&ldquo;family lineage&rdquo; &mdash; what the eldest sibling's friends and "
         "parents initially ask him to maintain, before the family's decision to "
         "renounce together."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-fourth."),
    ],
    text_intro=(
        "The text in full: eight verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp24:1.1-1.4"),
        ("p", "&sect;2", "cp24:2.1-2.4"),
        ("p", "&sect;3", "cp24:3.1-3.4"),
        ("p", "&sect;4", "cp24:4.1-4.4"),
        ("p", "&sect;5", "cp24:5.1-5.4"),
        ("p", "&sect;6", "cp24:6.1-6.4"),
        ("p", "&sect;7", "cp24:7.1-7.4"),
        ("p", "&sect;8", "cp24:8.1-8.4"),
    ],
    quiz=[
        {"q": "What does this story's title, 'The Conduct of the Lotus-eaters', refer to?",
         "opts": [
             "A detail described in full within these verses",
             "A detail from the fuller telling of the story that this particular verse text never actually states",
             "A type of food the family refuses to eat",
             "The name of the family's home village"],
         "correct": 1,
         "expl": "The title points past what the surviving verses actually cover."},
        {"q": "How many siblings are described in this family?",
         "opts": [
             "Just one child, an only child",
             "A sister and seven brothers — eight siblings total",
             "Three siblings",
             "The number is not specified"],
         "correct": 1,
         "expl": "The eldest sibling narrates the story."},
        {"q": "How do the family and friends initially respond to the eldest sibling's refusal of ordinary life?",
         "opts": [
             "With immediate hostility and threats",
             "By simply asking him to maintain the family lineage",
             "By disowning him on the spot",
             "They do not respond at all"],
         "correct": 1,
         "expl": "A gentle objection, though his refusal is firm nonetheless."},
        {"q": "How does the eldest sibling describe hearing about the ordinary pleasures of householder life?",
         "opts": [
             "As pleasant and tempting",
             "As 'hard for me to hear, like a heated ploughshare'",
             "As irrelevant and unremarkable",
             "He expresses no reaction at all"],
         "correct": 1,
         "expl": "Discomfort running in both directions."},
        {"q": "How do the parents respond upon learning of their son's decision?",
         "opts": [
             "With grief and mourning, trying to change his mind",
             "By proposing that the whole family go forth together",
             "By disowning him immediately",
             "They are indifferent to the news"],
         "correct": 1,
         "expl": "A notable departure from the wailing crowds in Cp 21 and Cp 23."},
        {"q": "How does this story's ending differ from Cp 21's and Cp 23's?",
         "opts": [
             "It ends identically, with a solitary departure amid a grieving crowd",
             "The entire family renounces together, rather than one figure departing alone",
             "No one actually leaves in this story",
             "The family is forcibly separated"],
         "correct": 1,
         "expl": "A scale of collective renunciation unique among this chapter's stories."},
        {"q": "What do the family members discard before entering the forest?",
         "opts": [
             "Nothing; they keep all their possessions",
             "Countless riches",
             "Only their clothing",
             "Their family name"],
         "correct": 1,
         "expl": "A complete departure from their former wealth."},
        {"q": "What kingdom is this family's home, shared with Cp 23's Ayoghara and Cp 26's Temiya?",
         "opts": [
             "Indapatta",
             "Kāsi",
             "Mithilā",
             "Videha"],
         "correct": 1,
         "expl": "A kingdom that recurs across several stories in this final chapter."},
        {"q": "What does 'kula-vaṁsa' refer to in this story?",
         "opts": [
             "A type of lotus plant",
             "'Family lineage' — what the eldest sibling is initially asked to maintain",
             "A geographic region",
             "A ritual ceremony"],
         "correct": 1,
         "expl": "The request made before the family's collective decision to renounce."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Renunciation (nekkhamma), the fourth of five stories on this theme",
             "Truth",
             "Equanimity"],
         "correct": 1,
         "expl": "Continuing the sequence of five renunciation-stories in this chapter."},
    ],
    marginalia=[
        ("A title left unexplained", [
            "the lotus-eating itself",
            "not described here"
        ]),
        ("A gentle objection", [
            "'maintain the",
            "family lineage'"
        ]),
        ("No mourning crowd", [
            "the parents propose",
            "joining him instead"
        ]),
        ("A family, not one figure", [
            "eight siblings",
            "and both parents"
        ]),
    ],
    further=[
        '<a href="%s/cp24/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-23.html">Cp 23 &mdash; Ayoghara&rsquo;s Conduct</a> &mdash; the '
        "text immediately before this one, also set in Kāsi.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 25 — Soṇa Cariyā
# --------------------------------------------------------------------------- #
page(
    25, "So&#7751;a Cariy&amacr;", "So&#7751;a the Astute&rsquo;s Conduct",
    meta_title="Cp 25 — Soṇa the Astute's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Soṇa the "
        "Astute's Conduct, closing the Cariyapitaka's chapter on renunciation with a "
        "brother who follows a brother's example. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Renunciation (5th of 5)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as Soṇa, in the city of "
                    "Brahmavaḍḍhana"),
        ("Speaker", "The Buddha, recounting his life as Soṇa"),
        ("Form", "Six four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; short, closing the "
                       "chapter on a quieter note than most of its stories"),
    ],
    why=(
        "This story closes the Cariyapitaka's chapter on renunciation without a crisis "
        "at all &mdash; no near-execution, no unexplained confinement, only a "
        "wealthy family's eldest son who finds the world &lsquo;smothered in "
        "darkness&rsquo;, and a younger brother, Nanda, who simply follows his lead."),
    guide=[
        ("A recoil from the world itself", [
            "Soṇa's motivation is described in general terms rather than a specific "
            "incident: seeing the world's &lsquo;many forms of wickedness&rsquo;, his "
            "mind recoils from rebirth &lsquo;as if harshly pricked by a goad&rsquo; "
            "&mdash; closer to Cp 21's quiet dewdrop than to Cp 22's violent crisis."]),
        ("An invitation declined plainly", [
            "As in Cp 24, relatives invite Soṇa to enjoy sensual pleasures; his reply "
            "is direct rather than argued at length: &lsquo;do not invite me to such "
            "things!&rsquo;"]),
        ("A younger brother who follows, not just a family that joins", [
            "Where Cp 24 showed an entire family departing at once on the parents' own "
            "initiative, here a single sibling, Nanda, chooses independently to follow "
            "Soṇa's example &mdash; a smaller-scale but still notably social version of "
            "renunciation, neither entirely solitary nor a whole household's decision."]),
        ("A chapter of five stories, five different routes to the same theme", [
            "Read together, this chapter's five stories show renunciation reached by "
            "very different roads: a dewdrop, a false accusation survived, an "
            "unexplained confinement, a family's shared decision, and here, a general "
            "disillusionment joined by a brother &mdash; the same destination, arrived "
            "at differently each time."]),
    ],
    terms=[
        ("nekkhamma",
         "&ldquo;renunciation&rdquo; &mdash; the perfection this story illustrates, "
         "closing this chapter's five stories on the theme."),
        ("Brahmavaḍḍhana",
         "the city named as Soṇa's home."),
        ("Nanda",
         "Soṇa's younger brother, who follows his ethical practice and also chooses "
         "to go forth."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-fifth."),
        ("pabbajjā",
         "&ldquo;going forth&rdquo; &mdash; the act Soṇa, Nanda, and both their "
         "parents undertake together at this story's close."),
    ],
    text_intro=(
        "The text in full: six verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp25:1.1-1.4"),
        ("p", "&sect;2", "cp25:2.1-2.4"),
        ("p", "&sect;3", "cp25:3.1-3.4"),
        ("p", "&sect;4", "cp25:4.1-4.4"),
        ("p", "&sect;5", "cp25:5.1-5.4"),
        ("p", "&sect;6", "cp25:6.1-6.4"),
    ],
    quiz=[
        {"q": "What motivates Soṇa's turn toward renunciation?",
         "opts": [
             "A specific violent crisis, like Cp 22's false accusation",
             "A general recoil from the world's 'many forms of wickedness'",
             "An order from his father",
             "No motivation is given"],
         "correct": 1,
         "expl": "Closer to Cp 21's quiet dewdrop than to a dramatic incident."},
        {"q": "How does Soṇa respond when relatives invite him to sensual pleasures?",
         "opts": [
             "He accepts, then changes his mind later",
             "Directly: 'Do not invite me to such things!'",
             "He says nothing and simply leaves",
             "He argues at length about the dangers of pleasure"],
         "correct": 1,
         "expl": "A plain refusal rather than an extended argument."},
        {"q": "Who is Nanda, and what does he do?",
         "opts": [
             "Soṇa's father, who forbids his renunciation",
             "Soṇa's younger brother, who independently chooses to follow his example",
             "A stranger Soṇa meets on the road",
             "A king who offers Soṇa a kingdom"],
         "correct": 1,
         "expl": "Following Soṇa's ethical practice and also going forth."},
        {"q": "How does this story's family departure differ from Cp 24's?",
         "opts": [
             "It is identical — the whole family departs at once, on the parents' initiative",
             "Here a single sibling follows independently, rather than the whole family departing together at once",
             "No one else joins Soṇa in this story",
             "Soṇa is the only character in the text"],
         "correct": 1,
         "expl": "A smaller-scale, still social version of renunciation."},
        {"q": "What is Soṇa's home city, as named in this text?",
         "opts": [
             "Indapatta",
             "Brahmavaḍḍhana",
             "Kāsi",
             "Kapilā"],
         "correct": 1,
         "expl": "Named at the story's opening."},
        {"q": "How does this story characterize the chapter's five stories on renunciation, taken together?",
         "opts": [
             "All five reach renunciation through an identical crisis",
             "Five different routes arriving at the same destination",
             "Only this story actually results in renunciation",
             "The five stories contradict each other"],
         "correct": 1,
         "expl": "A dewdrop, a survived accusation, an unexplained confinement, a family decision, and a general disillusionment."},
        {"q": "What ultimately happens to Soṇa's whole family?",
         "opts": [
             "They remain in the city, unchanged",
             "Soṇa, Nanda, and both parents discard their riches and enter the forest",
             "Only Soṇa leaves; the rest of the family stays behind",
             "The family is separated by force"],
         "correct": 1,
         "expl": "The story's closing verse."},
        {"q": "What perfection does this story illustrate, and what position does it hold in this chapter?",
         "opts": [
             "Ethics, opening the second chapter",
             "Renunciation (nekkhamma), the fifth and final story of this theme",
             "Truth, the first of six stories",
             "Resolve, the chapter's only story on this theme"],
         "correct": 1,
         "expl": "Closing this chapter's five stories on renunciation."},
        {"q": "What perfection does the next chapter section move to, beginning with Cp 26?",
         "opts": [
             "Giving",
             "Resolve (adhiṭṭhāna)",
             "Ethics",
             "Equanimity"],
         "correct": 1,
         "expl": "A single story illustrating this theme, Temiya's Conduct."},
        {"q": "What does 'pabbajjā' mean?",
         "opts": [
             "'Going forth' — the formal act of renunciation",
             "'Kingship'",
             "'False accusation'",
             "'Family lineage'"],
         "correct": 0,
         "expl": "The act Soṇa, Nanda, and their parents undertake together."},
    ],
    marginalia=[
        ("A general disillusionment", [
            "no single crisis,",
            "just a recoil"
        ]),
        ("A plain refusal", [
            "'do not invite me",
            "to such things'"
        ]),
        ("A brother follows", [
            "Nanda joins",
            "independently"
        ]),
        ("Five stories, one theme", [
            "different roads,",
            "the same destination"
        ]),
    ],
    further=[
        '<a href="%s/cp25/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-24.html">Cp 24 &mdash; The Conduct of the Lotus-eaters</a> '
        "&mdash; the text immediately before this one, closing the chapter on "
        "renunciation.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 26 — Temiya Cariyā
# --------------------------------------------------------------------------- #
page(
    26, "Temiya Cariy&amacr;", "Temiya&rsquo;s Conduct",
    meta_title="Cp 26 — Temiya's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Temiya's "
        "Conduct, the Cariyapitaka's sole story on the perfection of resolve — a "
        "prince who feigns disability for sixteen years to escape a throne. From "
        "Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Resolve (1 of 1)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as Prince Temiya, also called "
                    "Mūgapakkha, of Kāsi"),
        ("Speaker", "The Buddha, recounting his life as Temiya, with quoted counsel "
                    "from a goddess"),
        ("Form", "Nineteen verses of first-person narration"),
        ("Length", "3&ndash;4 minutes to read"),
        ("Northern parallel", "Temiya is the subject of his own jātaka, traditionally "
                              "counted among the same well-known set of the last ten "
                              "jātakas as Cp 12's Bhūridatta; this reading guide does "
                              "not assert further specific correspondences beyond that "
                              "general association."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; a long, difficult "
                       "story sustained over sixteen years within the narrative"),
    ],
    why=(
        "This is the Cariyapitaka's only story on the perfection of resolve, and it "
        "earns the distinction: a baby prince, terrified by a vision recalling a past "
        "life in which holding the royal umbrella led him to hell, spends sixteen "
        "years pretending to be deaf, dumb, and crippled &mdash; maintaining the "
        "deception through testing, public humiliation, and finally being taken out "
        "to be buried alive, all to avoid inheriting a throne he fears will damn him "
        "again."),
    guide=[
        ("A vision from a single glimpse", [
            "Waking as an infant and seeing the pale umbrella held over his bed, "
            "Temiya is struck with the memory &lsquo;by which I had gone to hell&rsquo; "
            "in a previous life &mdash; the umbrella representing not comfort but the "
            "kingship that led to his own past ruin."]),
        ("A goddess's counsel, accepted at once", [
            "A goddess who was once his relation advises a specific strategy: appear "
            "as a fool, let everyone scorn him, and this will achieve his goal. Temiya "
            "does not hesitate or negotiate; he resolves immediately on three factors "
            "&mdash; deafness, muteness, and paralysis &mdash; and holds to them for "
            "sixteen years."]),
        ("Tested, and never breaking character", [
            "The court eventually tests him physically, rubbing his limbs and senses "
            "for any sign of feeling or awareness, and finding none, denounces him "
            "with the epithet &lsquo;black-ear&rsquo; &mdash; a term of contempt, not "
            "concern, met by Temiya with private elation rather than distress: his "
            "resolve has succeeded exactly as intended."]),
        ("Discarded, then taken to be buried alive", [
            "Written off as unfit to inherit the throne, Temiya is first paraded "
            "through the city for seven days &mdash; the very ceremony of an heir "
            "apparent, performed over someone about to be discarded &mdash; then taken "
            "by chariot to the forest, where a charioteer begins digging a pit to bury "
            "him in the ground."]),
        ("A resolve held to the story's very edge", [
            "This particular verse text ends without narrating what happens once the "
            "pit is dug: the final verses state only that Temiya, afraid of breaking "
            "any of his many resolves, did not break this one either. As with several "
            "other stories in this collection, the resolution &mdash; what becomes of "
            "him at the graveside &mdash; is left to the fuller Jātaka tradition "
            "outside this text."]),
    ],
    terms=[
        ("adhiṭṭhāna",
         "&ldquo;resolve&rdquo; or &ldquo;determination&rdquo; &mdash; the perfection "
         "this story illustrates, the only one of the ten traditional perfections to "
         "receive just a single dedicated story in this particular collection."),
        ("Mūgapakkha",
         "&ldquo;dumb cripple&rdquo; &mdash; the name given Temiya once his feigned "
         "disability convinces the court, contrasted with &lsquo;Temiya&rsquo; itself."),
        ("Kāsi",
         "the kingdom Temiya is the true-born son of the king of, the same kingdom as "
         "Cp 23's Ayoghara and Cp 24's family of lotus-eaters."),
        ("devatā",
         "&ldquo;goddess&rdquo; or &ldquo;deity&rdquo; &mdash; the former relation of "
         "Temiya's who advises the strategy of feigned disability."),
        ("Temiya Jātaka",
         "the fuller version of this story in the separate Jātaka tradition, "
         "traditionally counted among a well-known set of the last ten jātakas."),
    ],
    text_intro=(
        "The text in full: nineteen verses, the Cariyapitaka's only story on the "
        "perfection of resolve. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "A vision from a single glimpse"),
        ("p", "&sect;1", "cp26:1.1-1.4"),
        ("p", "&sect;2", "cp26:2.1-2.4"),
        ("p", "&sect;3", "cp26:3.1-3.4"),
        ("p", "&sect;4", "cp26:4.1-4.4"),
        ("p", "&sect;5", "cp26:5.1-5.4"),
        ("h3", "A goddess's counsel"),
        ("p", "&sect;6", "cp26:6.1-6.4"),
        ("p", "&sect;7", "cp26:7.1-7.4"),
        ("p", "&sect;8", "cp26:8.1-8.6"),
        ("p", "&sect;9", "cp26:9.1-9.4"),
        ("h3", "Sixteen years, and a test"),
        ("p", "&sect;10", "cp26:10.1-10.4"),
        ("p", "&sect;11", "cp26:11.1-11.4"),
        ("p", "&sect;12", "cp26:12.1-12.4"),
        ("p", "&sect;13", "cp26:13.1-13.4"),
        ("h3", "Paraded, then taken to the forest"),
        ("p", "&sect;14", "cp26:14.1-14.4"),
        ("p", "&sect;15", "cp26:15.1-15.4"),
        ("p", "&sect;16", "cp26:16.1-16.4"),
        ("h3", "A resolve held to the edge of the story"),
        ("p", "&sect;17", "cp26:17.1-17.4"),
        ("p", "&sect;18", "cp26:18.1-18.4"),
        ("p", "&sect;19", "cp26:19.1-19.4"),
    ],
    quiz=[
        {"q": "What triggers Temiya's terror as an infant?",
         "opts": [
             "A nightmare with no clear cause",
             "Seeing the royal umbrella, and recalling a past life in which it led him to hell",
             "A prophecy delivered by a court astrologer",
             "Witnessing a battle"],
         "correct": 1,
         "expl": "The umbrella representing the kingship that led to his own past ruin."},
        {"q": "What strategy does the goddess advise Temiya to adopt?",
         "opts": [
             "Openly refuse the throne and argue his case",
             "Appear as a fool, deaf and dumb, so everyone will scorn and discard him",
             "Flee the kingdom immediately",
             "Challenge his father to a contest"],
         "correct": 1,
         "expl": "A strategy Temiya accepts and resolves on immediately."},
        {"q": "How long does Temiya maintain his feigned disability?",
         "opts": [
             "One year",
             "Sixteen years",
             "A single day",
             "His whole life, without ever being tested"],
         "correct": 1,
         "expl": "Resolved on three factors: deafness, muteness, and paralysis."},
        {"q": "How does the court test whether Temiya's disability is genuine?",
         "opts": [
             "By asking him direct questions",
             "By physically rubbing his limbs and senses for any reaction",
             "By observing him in secret for a single day",
             "No test is ever performed"],
         "correct": 1,
         "expl": "Finding no reaction, they denounce him as 'black-ear'."},
        {"q": "How does Temiya react to being denounced and discarded?",
         "opts": [
             "With visible distress and protest",
             "With private elation — his resolve had succeeded exactly as intended",
             "By finally revealing the truth",
             "With no reaction described at all"],
         "correct": 1,
         "expl": "The scorn is precisely the outcome he had been working toward."},
        {"q": "What happens before Temiya is taken to the forest to be buried?",
         "opts": [
             "He is immediately exiled with no ceremony",
             "He is bathed, oiled, and paraded through the city for seven days as an heir apparent",
             "He is put on trial",
             "He escapes before any further action is taken"],
         "correct": 1,
         "expl": "A ceremony performed over someone about to be discarded."},
        {"q": "What is the charioteer doing when this particular text's narrative ends?",
         "opts": [
             "Driving Temiya back to the palace",
             "Digging a pit in the forest to bury Temiya in the ground",
             "Releasing Temiya and departing",
             "Nothing; the charioteer never appears"],
         "correct": 1,
         "expl": "The story's final narrative image before the closing reflection."},
        {"q": "Does this text narrate what happens once the pit is dug?",
         "opts": [
             "Yes, in full detail",
             "No — the resolution is left to the fuller Jātaka tradition outside this text",
             "Temiya is described as dying at this point",
             "The text explains it through a lengthy epilogue"],
         "correct": 1,
         "expl": "A gap consistent with several other verse-only stories in this collection."},
        {"q": "What is Temiya's other name, given once his disability convinces the court?",
         "opts": [
             "Mūgapakkha, 'dumb cripple'",
             "Kururāja",
             "Somanassa",
             "Ayoghara"],
         "correct": 0,
         "expl": "Contrasted with 'Temiya' itself."},
        {"q": "What wider tradition is Temiya's story associated with?",
         "opts": [
             "No other tradition mentions this figure",
             "His own jātaka, counted among a well-known set of the last ten jātakas",
             "A canonical discourse to King Ajātasattu",
             "The Petavatthu"],
         "correct": 1,
         "expl": "The same set that includes Cp 12's Bhūridatta."},
    ],
    marginalia=[
        ("A vision from an umbrella", [
            "a past life",
            "that led to hell"
        ]),
        ("Sixteen years feigned", [
            "deaf, dumb,",
            "and crippled"
        ]),
        ("Denounced, and elated", [
            "scorn was",
            "the goal itself"
        ]),
        ("A pit being dug", [
            "the story ends",
            "before the resolution"
        ]),
    ],
    further=[
        '<a href="%s/cp26/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-25.html">Cp 25 &mdash; So&#7751;a the Astute&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one, closing the chapter on "
        "renunciation.",
        '<a href="cp-12.html">Cp 12 &mdash; The Dragon Bh&umacr;ridatta&rsquo;s '
        "Conduct</a> &mdash; another story from the same traditional set of the last "
        "ten jātakas.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 27 — Kapi Cariyā
# --------------------------------------------------------------------------- #
page(
    27, "Kapi Cariy&amacr;", "The Monkey King&rsquo;s Conduct",
    meta_title="Cp 27 — The Monkey King's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Monkey "
        "King's Conduct, opening the Cariyapitaka's chapter on truthfulness with a "
        "clever, technically honest escape from a crocodile. From Ru-Yi Meditation "
        "Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Truth (1st of 6)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as a monkey trapped on a riverbank"),
        ("Speaker", "The Buddha, recounting his life as the monkey, with a brief "
                    "exchange with a crocodile"),
        ("Form", "Four four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a short story with "
                       "a genuinely tricky question of interpretation at its center"),
    ],
    why=(
        "This story opens the Cariyapitaka's chapter on truthfulness with its most "
        "ambiguous case: a monkey trapped by a crocodile answers &lsquo;I am "
        "coming&rsquo; to the crocodile's invitation, then crosses the river by "
        "stepping on the crocodile's own head &mdash; technically doing exactly what "
        "he said, while completely defeating what the crocodile intended."),
    guide=[
        ("A trap disguised as an invitation", [
            "The crocodile does not threaten the monkey outright; he waits at the "
            "monkey's usual landing spot and says only &lsquo;come&rsquo;, letting the "
            "ordinary word carry the danger without stating it."]),
        ("A reply that is not a lie", [
            "The monkey's answer, &lsquo;I am coming,&rsquo; is simple and direct "
            "&mdash; and then he does come, by leaping onto the crocodile's head and "
            "using it as a stepping stone to the far bank, arriving exactly as "
            "promised."]),
        ("The text's own claim about what happened", [
            "The story states its own verdict plainly: &lsquo;I spoke no lie to him, "
            "but acted according to my word.&rsquo; The claim to truthfulness rests "
            "entirely on the literal accuracy of &lsquo;I am coming&rsquo;, not on "
            "having honored the crocodile's actual intention."]),
        ("An opening case that raises the chapter's real question", [
            "By placing this story first among six on truthfulness, the collection "
            "poses its sharpest question early: is truthfulness only about the literal "
            "accuracy of what is said, or does it also depend on what a listener is "
            "led to expect? The chapter's later stories, especially Cp 28's ascetic and "
            "Cp 31's uncomfortable confession, approach the theme very differently."]),
    ],
    terms=[
        ("sacca",
         "&ldquo;truth&rdquo; &mdash; the perfection this story illustrates, opening "
         "this chapter's six stories on the theme."),
        ("kumbhīla",
         "&ldquo;crocodile&rdquo; or &ldquo;gharial&rdquo; &mdash; the monkey's foe, "
         "waiting at the usual crossing point."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-seventh."),
        ("musāvāda",
         "&ldquo;false speech&rdquo; &mdash; what the monkey explicitly denies having "
         "engaged in, despite leading the crocodile into a plan that fails him "
         "completely."),
        ("Yudhañjaya-vagga",
         "&ldquo;the Chapter With Yudhañjaya&rdquo; &mdash; this collection's third "
         "chapter, now moving from renunciation and resolve into its six stories on "
         "truth."),
    ],
    text_intro=(
        "The text in full: four verses of first-person narration. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp27:1.1-1.4"),
        ("p", "&sect;2", "cp27:2.1-2.4"),
        ("p", "&sect;3", "cp27:3.1-3.4"),
        ("p", "&sect;4", "cp27:4.1-4.4"),
    ],
    quiz=[
        {"q": "What does the crocodile say to lure the monkey?",
         "opts": [
             "An explicit threat",
             "Simply 'come' — letting the ordinary word carry the danger unstated",
             "An offer of food",
             "Nothing; he attacks without speaking"],
         "correct": 1,
         "expl": "A trap disguised as an ordinary invitation."},
        {"q": "What does the monkey reply?",
         "opts": [
             "A refusal",
             "'I am coming' — and then he does come, by his own route",
             "A counter-threat",
             "He says nothing at all"],
         "correct": 1,
         "expl": "Simple and direct, then literally fulfilled."},
        {"q": "How does the monkey actually cross the river?",
         "opts": [
             "By swimming around the crocodile entirely",
             "By stepping on the crocodile's own head as a stepping stone",
             "By finding another crossing point",
             "He does not cross; the story ends before he does"],
         "correct": 1,
         "expl": "Arriving exactly as promised, just not as the crocodile intended."},
        {"q": "What claim does the story make about the monkey's honesty?",
         "opts": [
             "That he lied to save himself, and this was justified",
             "'I spoke no lie to him, but acted according to my word'",
             "That the crocodile was also being truthful",
             "No claim about honesty is made"],
         "correct": 1,
         "expl": "Resting on the literal accuracy of 'I am coming', not the crocodile's expectations."},
        {"q": "What question does placing this story first in the truth chapter raise?",
         "opts": [
             "Whether animals can speak at all",
             "Whether truthfulness is only about literal accuracy, or also about what a listener is led to expect",
             "Whether crocodiles are inherently untrustworthy",
             "No particular question is raised by the ordering"],
         "correct": 1,
         "expl": "A question the chapter's later stories approach quite differently."},
        {"q": "What does 'musāvāda' mean?",
         "opts": [
             "'False speech' — what the monkey denies having engaged in",
             "'River crossing'",
             "'Crocodile'",
             "'Perfection of truth'"],
         "correct": 0,
         "expl": "Denied despite the crocodile being completely outmaneuvered."},
        {"q": "What perfection does this story open, and how many stories does this chapter give it?",
         "opts": [
             "Ethics; ten stories",
             "Truth (sacca); six stories",
             "Renunciation; five stories",
             "Love; two stories"],
         "correct": 1,
         "expl": "The third of the third chapter's five themes."},
        {"q": "How does this story compare in length to the average story in this collection?",
         "opts": [
             "Among the shortest, at four verses",
             "Among the longest",
             "Exactly average length",
             "It has no verses at all"],
         "correct": 0,
         "expl": "A brief, sharply focused case."},
        {"q": "What perfection did the previous story, Cp 26, illustrate?",
         "opts": [
             "Giving",
             "Resolve (adhiṭṭhāna), the collection's only story on this theme",
             "Ethics",
             "Equanimity"],
         "correct": 1,
         "expl": "Temiya's sixteen years of feigned disability."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Truth (sacca), the first of six stories on this theme",
             "Love",
             "Equanimity",
             "Giving"],
         "correct": 0,
         "expl": "Opening this chapter's largest group of stories after ethics and giving."},
    ],
    marginalia=[
        ("A trap in a single word", [
            "'come' —",
            "danger left unstated"
        ]),
        ("A literal promise kept", [
            "'I am coming',",
            "then he does"
        ]),
        ("A head as a stepping stone", [
            "the crocodile's plan",
            "defeated entirely"
        ]),
        ("A question the chapter raises", [
            "literal truth,",
            "or honored expectation?"
        ]),
    ],
    further=[
        '<a href="%s/cp27/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-26.html">Cp 26 &mdash; Temiya&rsquo;s Conduct</a> &mdash; the text '
        "immediately before this one, closing the chapter on resolve.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 28 — Sacca Cariyā
# --------------------------------------------------------------------------- #
page(
    28, "Sacca Cariy&amacr;", "The Ascetic Truthful&rsquo;s Conduct",
    meta_title="Cp 28 — The Ascetic Truthful's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Ascetic "
        "Truthful's Conduct, the single shortest story in the entire Cariyapitaka — "
        "just four lines, with no incident at all. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Truth (2nd of 6)",
    glance=[
        ("Setting", "No narrative setting whatsoever; the Buddha speaks in the first "
                    "person about his past life as an ascetic named Truthful"),
        ("Speaker", "The Buddha, recounting his life as the ascetic Truthful"),
        ("Form", "A single four-line verse &mdash; the shortest story in the entire "
                 "Cariyapitaka"),
        ("Length", "a few seconds to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; no narrative "
                       "complexity at all, only what four lines can carry"),
    ],
    why=(
        "This is the shortest of all thirty-five Cariyapitaka stories: one verse, no "
        "crisis, no dialogue, no test to pass. Where Cp 27's monkey demonstrates "
        "truthfulness through a clever escape under real pressure, this ascetic's "
        "truthfulness is simply stated as a settled fact about who he was &mdash; a "
        "reputation, not an episode."),
    guide=[
        ("The shortest story in the collection", [
            "At a single four-line verse, this is shorter than every other story in "
            "the Cariyapitaka, including Cp 5's three-verse Mahāgovinda &mdash; there "
            "is simply less text here than anywhere else in the collection's thirty-"
            "five stories."]),
        ("A name that states the whole story", [
            "The ascetic is identified only by his descriptive title, "
            "&lsquo;Truthful&rsquo; &mdash; unlike most of this collection's figures, "
            "who are named and then shown acting, this character's name and his "
            "conduct are presented as the same thing."]),
        ("Truth as a public, stabilizing force", [
            "The verse's claim is social rather than personal: he &lsquo;protected the "
            "world with his truth, uniting the people.&rsquo; Nothing in the text "
            "describes a specific act of protection or unification &mdash; only the "
            "general, sustained reputation for reliability that presumably made it "
            "possible."]),
        ("A deliberate contrast with the story before it", [
            "Read directly after Cp 27's technically honest but strategically evasive "
            "monkey, this story's plain, untested truthfulness reads almost as a "
            "correction &mdash; where the monkey's truth served his own escape, this "
            "ascetic's truth is described as serving everyone around him."]),
    ],
    terms=[
        ("sacca",
         "&ldquo;truth&rdquo; &mdash; the perfection this story illustrates, the "
         "second of six stories on this theme, and the very name this ascetic is "
         "known by."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-eighth and shortest."),
        ("saṅgaha",
         "&ldquo;unification&rdquo; or &ldquo;inclusiveness&rdquo; &mdash; the effect "
         "this text says the ascetic's truthfulness had on the people around him."),
        ("Yudhañjaya-vagga",
         "&ldquo;the Chapter With Yudhañjaya&rdquo; &mdash; this collection's third "
         "chapter, continuing here with its six stories on truth."),
        ("isi",
         "&ldquo;seer&rdquo; or &ldquo;ascetic&rdquo; &mdash; the kind of figure "
         "&lsquo;Truthful&rsquo; is described as."),
    ],
    text_intro=(
        "The text in full: a single verse, the shortest story in the Cariyapitaka. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp28:1.1-1.4"),
    ],
    quiz=[
        {"q": "How does this story compare in length to every other story in the Cariyapitaka?",
         "opts": [
             "It is roughly average length",
             "It is the shortest of all thirty-five stories, at a single verse",
             "It is the longest story in the collection",
             "It is tied for shortest with several others"],
         "correct": 1,
         "expl": "Shorter even than Cp 5's three-verse Mahāgovinda."},
        {"q": "What is this ascetic's name?",
         "opts": [
             "No name is given at all",
             "Truthful — a descriptive title rather than a personal name",
             "Sacca-deva",
             "Isi-vata"],
         "correct": 1,
         "expl": "His name and his conduct are presented as the same thing."},
        {"q": "What specific incident does this story describe?",
         "opts": [
             "A detailed test of his honesty",
             "None — no specific act or event is narrated at all",
             "A conflict with a rival ascetic",
             "A miraculous rescue"],
         "correct": 1,
         "expl": "A settled fact about who he was, not an episode."},
        {"q": "What does the verse claim the ascetic's truthfulness accomplished?",
         "opts": [
             "Nothing in particular",
             "He 'protected the world' with it and 'united the people'",
             "It made him wealthy",
             "It won him a kingdom"],
         "correct": 1,
         "expl": "A social, stabilizing effect rather than a personal outcome."},
        {"q": "How does this story's truthfulness compare to Cp 27's monkey?",
         "opts": [
             "Identical in every way",
             "The monkey's truth served his own escape under pressure; this ascetic's truth is described as serving everyone, with no pressure shown at all",
             "This story shows no truthfulness at all",
             "The monkey lied, while this ascetic did not"],
         "correct": 1,
         "expl": "A deliberate contrast between the collection's two adjacent truth-stories."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Truth (sacca), the second of six stories on this theme",
             "Renunciation",
             "Resolve"],
         "correct": 1,
         "expl": "Continuing the sequence of six truth-stories in this chapter."},
        {"q": "What does 'saṅgaha' refer to in this story?",
         "opts": [
             "A type of ascetic practice",
             "'Unification' or 'inclusiveness' — the effect of the ascetic's truthfulness on the people",
             "A geographic location",
             "A ritual object"],
         "correct": 1,
         "expl": "Named as the outcome of his reputation for truth."},
        {"q": "Does this story include any dialogue?",
         "opts": [
             "Yes, an extended exchange",
             "No — there is no dialogue, crisis, or test of any kind",
             "Only a single line of dialogue",
             "The entire story is dialogue"],
         "correct": 1,
         "expl": "A settled reputation, stated rather than dramatized."},
        {"q": "What perfection did the story immediately before this one illustrate?",
         "opts": [
             "Ethics",
             "Truth (sacca), the first of six stories on this theme",
             "Resolve",
             "Love"],
         "correct": 1,
         "expl": "Cp 27's monkey, opening the same chapter."},
        {"q": "What does 'isi' mean?",
         "opts": [
             "'Seer' or 'ascetic' — the kind of figure this story describes",
             "'King'",
             "'Village'",
             "'Truth'"],
         "correct": 0,
         "expl": "The identity given to 'Truthful' in this text."},
    ],
    marginalia=[
        ("The shortest story", [
            "one verse,",
            "the whole collection's briefest"
        ]),
        ("A name as a summary", [
            "'Truthful' —",
            "name and conduct as one"
        ]),
        ("No incident at all", [
            "a reputation stated,",
            "not dramatized"
        ]),
        ("A contrast with Cp 27", [
            "truth for everyone,",
            "not for one escape"
        ]),
    ],
    further=[
        '<a href="%s/cp28/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-27.html">Cp 27 &mdash; The Monkey King&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one, a study in contrast.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 29 — Vaṭṭaka Cariyā
# --------------------------------------------------------------------------- #
page(
    29, "Va&#7789;&#7789;aka Cariy&amacr;", "The Baby Quail&rsquo;s Conduct",
    meta_title="Cp 29 — The Baby Quail's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Baby "
        "Quail's Conduct, the Cariyapitaka's story of an abandoned, flightless chick "
        "who stops a forest fire with a declaration of truth. From Ru-Yi Meditation "
        "Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Truth (3rd of 6)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as a newly hatched quail in Magadha"),
        ("Speaker", "The Buddha, recounting his life as the baby quail"),
        ("Form", "Eleven verses of first-person narration, including a formal "
                 "declaration of truth"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; introduces a "
                       "specific literary device worth understanding on its own terms"),
    ],
    why=(
        "A newly hatched quail, too young to fly or walk, is abandoned by his fleeing "
        "parents as a forest fire closes in. With no physical means of escape, he "
        "does something this collection has not shown before: he makes a formal, "
        "public &lsquo;declaration of truth&rsquo;, relying on the truth itself, "
        "rather than any action, to turn the fire back."),
    guide=[
        ("A helplessness stated without embellishment", [
            "The quail's situation is described in the plainest physical terms: "
            "&lsquo;wings that do not fly&rsquo;, &lsquo;feet that do not walk&rsquo;, "
            "abandoned in the nest by parents who saved themselves &mdash; no rescue "
            "is coming, and no ordinary action is available to him."]),
        ("A different kind of power invoked", [
            "Facing the fire, the quail does not struggle or pray for aid; he invokes "
            "&lsquo;the quality of virtue in the world, truth, purity, and mercy&rsquo; "
            "directly, framing his own truthful statement as a real force with real "
            "consequences, not merely words."]),
        ("A declaration that states the situation exactly as it is", [
            "The declaration itself is not a request or a wish; it simply restates the "
            "quail's helplessness precisely: &lsquo;I have wings that do not fly! I "
            "have feet that do not walk! Mother and father have fled!&rsquo; &mdash; "
            "followed by a direct command to the fire itself: &lsquo;go back!&rsquo;"]),
        ("An effect stated as immediate and total", [
            "The story reports the result without qualification: the flames withdrew "
            "sixteen leagues, &lsquo;as if they had come to water&rsquo;. This kind of "
            "formal truth-telling with a claimed miraculous effect, sometimes called a "
            "&lsquo;truth-act&rsquo; in scholarship on Indian literature, recurs again "
            "in Cp 30's fish king and Cp 31's Dark Light."]),
    ],
    terms=[
        ("sacca",
         "&ldquo;truth&rdquo; &mdash; the perfection this story illustrates, the "
         "third of six stories on this theme."),
        ("saccakiriyā",
         "an &ldquo;act of truth&rdquo; or &ldquo;truth-act&rdquo; &mdash; a formal "
         "declaration of a true fact, relied upon as a source of real power; this "
         "story is the first of several examples of the device in this chapter."),
        ("Magadha",
         "the region named as the quail's home."),
        ("Jātaveda",
         "an epithet for fire, addressed directly in the quail's declaration "
         "&mdash; &lsquo;Jātaveda the fire: go back!&rsquo;"),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its twenty-ninth."),
    ],
    text_intro=(
        "The text in full: eleven verses, including the quail's formal declaration of "
        "truth. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp29:1.1-1.4"),
        ("p", "&sect;2", "cp29:2.1-2.4"),
        ("p", "&sect;3", "cp29:3.1-3.4"),
        ("p", "&sect;4", "cp29:4.1-4.4"),
        ("p", "&sect;5", "cp29:5.1-5.4"),
        ("p", "&sect;6", "cp29:6.1-6.4"),
        ("p", "&sect;7", "cp29:7.1-7.4"),
        ("p", "&sect;8", "cp29:8.1-8.4"),
        ("p", "&sect;9", "cp29:9.1-9.4"),
        ("p", "&sect;10", "cp29:10.1-10.4"),
        ("p", "&sect;11", "cp29:11.1-11.6"),
    ],
    quiz=[
        {"q": "What is the quail's physical condition when the fire approaches?",
         "opts": [
             "Fully grown and able to fly away",
             "Newly hatched, with wings that don't fly and feet that don't walk",
             "Injured from a previous attack",
             "Asleep and unaware of the danger"],
         "correct": 1,
         "expl": "No ordinary means of escape available to him."},
        {"q": "What do the quail's parents do as the fire approaches?",
         "opts": [
             "They stay and try to protect him",
             "They flee, abandoning him in the nest to save themselves",
             "They carry him to safety",
             "They are killed trying to save him"],
         "correct": 1,
         "expl": "No rescue is coming."},
        {"q": "What does the quail do instead of trying to physically escape?",
         "opts": [
             "He gives up and waits to die",
             "He makes a formal declaration of truth, invoking truth itself as a real force",
             "He calls out for other animals to help",
             "He attempts to fly despite his condition"],
         "correct": 1,
         "expl": "Relying on truth rather than any physical action."},
        {"q": "What does the quail's declaration actually say?",
         "opts": [
             "A request for the gods to intervene",
             "A precise restatement of his own helplessness, followed by a command to the fire",
             "A promise of future good deeds",
             "A curse against the fire"],
         "correct": 1,
         "expl": "'I have wings that do not fly!... Jātaveda the fire: go back!'"},
        {"q": "What is the stated result of the quail's declaration?",
         "opts": [
             "Nothing happens; the fire continues unabated",
             "The flames withdraw sixteen leagues, 'as if they had come to water'",
             "The quail is rescued by a passing traveler",
             "The fire changes direction slightly"],
         "correct": 1,
         "expl": "An immediate, total effect, reported without qualification."},
        {"q": "What is the technical term for this kind of formal truth-declaration with a claimed powerful effect?",
         "opts": [
             "Dhammavinaya",
             "Saccakiriyā, a 'truth-act'",
             "Paritta",
             "Uposatha"],
         "correct": 1,
         "expl": "A device that recurs again in Cp 30 and Cp 31."},
        {"q": "Where else in this chapter does the same kind of declaration reappear?",
         "opts": [
             "Nowhere else in this collection",
             "Cp 30's fish king and Cp 31's Dark Light",
             "Only in Cp 27's monkey story",
             "In every single story in this chapter"],
         "correct": 1,
         "expl": "A recurring literary device across several of this chapter's stories."},
        {"q": "What region is named as the quail's home?",
         "opts": [
             "Kāsi",
             "Magadha",
             "Kosala",
             "Videha"],
         "correct": 1,
         "expl": "Named at the story's opening."},
        {"q": "What does 'Jātaveda' refer to in this story?",
         "opts": [
             "The quail's own name",
             "An epithet for fire, addressed directly in the declaration",
             "A type of forest tree",
             "The name of a deity who intervenes"],
         "correct": 1,
         "expl": "'Jātaveda the fire: go back!'"},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Truth (sacca), the third of six stories on this theme",
             "Renunciation",
             "Love"],
         "correct": 1,
         "expl": "Continuing the sequence of six truth-stories in this chapter."},
    ],
    marginalia=[
        ("Wings that don't fly", [
            "no ordinary escape",
            "available to him"
        ]),
        ("Abandoned by his parents", [
            "fleeing to",
            "save themselves"
        ]),
        ("A declaration, not an action", [
            "truth invoked",
            "as a real force"
        ]),
        ("Flames withdrawn at once", [
            "sixteen leagues,",
            "'as if to water'"
        ]),
    ],
    further=[
        '<a href="%s/cp29/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-28.html">Cp 28 &mdash; The Ascetic Truthful&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one in the Cariyapitaka.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 30 — Maccharāja Cariyā
# --------------------------------------------------------------------------- #
page(
    30, "Macchar&amacr;ja Cariy&amacr;", "The Fish King&rsquo;s Conduct",
    meta_title="Cp 30 — The Fish King's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The Fish "
        "King's Conduct, the Cariyapitaka's second act-of-truth story — a drought, a "
        "declaration of non-harm, and rain summoned to save a lake. From Ru-Yi "
        "Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Truth (4th of 6)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as a fish king in a drying lake"),
        ("Speaker", "The Buddha, recounting his life as the fish king"),
        ("Form", "Nine verses of first-person narration, including a formal "
                 "declaration of truth"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&#9734;&#9734;&#9734; &mdash; a second, "
                       "structurally similar example of the truth-act device"),
    ],
    why=(
        "Following directly on Cp 29's quail, this story shows the same device "
        "&mdash; a formal declaration of truth, relied on for a real effect &mdash; "
        "used at a larger scale: a drought has emptied a lake, scavenging birds are "
        "devouring the trapped fish daily, and their king declares a specific truth "
        "about his own past conduct to summon rain."),
    guide=[
        ("A slow disaster, not a sudden one", [
            "Unlike Cp 29's fire, this crisis unfolds gradually: the lake's water "
            "evaporates in the heat, and crows, vultures, herons, hawks, and falcons "
            "descend to feed on the exposed fish &lsquo;day and night&rsquo;, an "
            "ongoing predation rather than a single moment of danger."]),
        ("A truth chosen deliberately as the tool", [
            "Considering how to help his relatives, the fish king does not attempt a "
            "physical solution; he explicitly &lsquo;saw the truth as a support&rsquo; "
            "and decides in advance to rely on a declaration."]),
        ("A very specific truth, stated as the basis for the claim", [
            "The truth he declares is precise: &lsquo;so long as I can recall myself, "
            "since I became aware, I do not recall deliberately harming even a single "
            "living creature.&rsquo; The power of the declaration rests on the "
            "specificity and accuracy of this claim about his own past, not on a "
            "general appeal."]),
        ("A named deity addressed directly, and an immediate response", [
            "The fish king calls out to Pajjuna, a rain deity, by name, asking that "
            "the crow's hunting ground be disrupted and the fish freed from sorrow. "
            "The response is immediate: thunder, then rain pouring down over "
            "&lsquo;the uplands and valleys&rsquo; without delay."]),
    ],
    terms=[
        ("sacca",
         "&ldquo;truth&rdquo; &mdash; the perfection this story illustrates, the "
         "fourth of six stories on this theme."),
        ("saccakiriyā",
         "an &ldquo;act of truth&rdquo;, the same device used in Cp 29's story of the "
         "baby quail, here applied to save an entire community of fish rather than "
         "one individual."),
        ("Pajjuna",
         "a deity associated with rain and storms, addressed directly in the fish "
         "king's declaration."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its thirtieth."),
        ("ahiṁsā",
         "&ldquo;non-harm&rdquo; &mdash; not named directly in this translation, but "
         "the substance of the specific truth the fish king declares about his own "
         "past conduct."),
    ],
    text_intro=(
        "The text in full: nine verses, including the fish king's declaration of "
        "truth. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp30:1.1-1.4"),
        ("p", "&sect;2", "cp30:2.1-2.4"),
        ("p", "&sect;3", "cp30:3.1-3.4"),
        ("p", "&sect;4", "cp30:4.1-4.4"),
        ("p", "&sect;5", "cp30:5.1-5.4"),
        ("p", "&sect;6", "cp30:6.1-6.4"),
        ("p", "&sect;7", "cp30:7.1-7.6"),
        ("p", "&sect;8", "cp30:8.1-8.4"),
        ("p", "&sect;9", "cp30:9.1-9.6"),
    ],
    quiz=[
        {"q": "How does this story's crisis unfold, compared to Cp 29's forest fire?",
         "opts": [
             "Identically — a sudden, single moment of danger",
             "Gradually — a drought empties the lake, and scavenging birds prey on the fish over time",
             "There is no crisis in this story",
             "The crisis is resolved before it begins"],
         "correct": 1,
         "expl": "Ongoing predation, not a single sudden threat."},
        {"q": "What does the fish king decide to rely on, rather than a physical solution?",
         "opts": [
             "Fleeing with his relatives to another lake",
             "A declaration of truth, seeing 'the truth as a support'",
             "Fighting off the birds directly",
             "Waiting passively for the rain to come naturally"],
         "correct": 1,
         "expl": "A tool chosen deliberately, as in Cp 29."},
        {"q": "What specific truth does the fish king declare?",
         "opts": [
             "That he is the strongest fish in the lake",
             "That he does not recall ever deliberately harming a single living creature",
             "That the birds deserve punishment",
             "That the drought will end naturally"],
         "correct": 1,
         "expl": "The power of the declaration rests on this claim's specificity and accuracy."},
        {"q": "Who does the fish king address directly in his declaration?",
         "opts": [
             "The king of the birds",
             "Pajjuna, a deity associated with rain",
             "Sakka",
             "No one is addressed directly"],
         "correct": 1,
         "expl": "Naming the deity whose response he seeks."},
        {"q": "What is the result of the fish king's declaration?",
         "opts": [
             "Nothing happens",
             "Thunder, then immediate rain pouring down over the uplands and valleys",
             "The birds simply lose interest and leave",
             "The lake refills gradually over many months"],
         "correct": 1,
         "expl": "An immediate response, without delay."},
        {"q": "How does this story relate to Cp 29's baby quail?",
         "opts": [
             "They are unrelated in theme and structure",
             "Both use the same 'act of truth' device, applied at different scales",
             "This story contradicts Cp 29's approach",
             "Only this story actually succeeds"],
         "correct": 1,
         "expl": "The same device, here saving a whole community rather than one individual."},
        {"q": "What does 'saccakiriyā' mean?",
         "opts": [
             "'Act of truth' — a formal declaration relied on for a real effect",
             "'Rain deity'",
             "'Fish king'",
             "'Drought'"],
         "correct": 0,
         "expl": "The device shared between this story and Cp 29's."},
        {"q": "What creatures does the text name as preying on the trapped fish?",
         "opts": [
             "Only crows",
             "Crows, vultures, herons, hawks, and falcons",
             "Only a single vulture",
             "No predators are named"],
         "correct": 1,
         "expl": "A range of scavenging and hunting birds."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Truth (sacca), the fourth of six stories on this theme",
             "Renunciation",
             "Equanimity"],
         "correct": 1,
         "expl": "Continuing the sequence of six truth-stories in this chapter."},
        {"q": "What relationship do the fish being preyed upon have to the fish king?",
         "opts": [
             "They are strangers to him",
             "They are described as his relatives",
             "They are his rivals",
             "No relationship is specified"],
         "correct": 1,
         "expl": "Making the crisis a personal one, not just a general disaster."},
    ],
    marginalia=[
        ("A slow disaster", [
            "birds preying",
            "day and night"
        ]),
        ("Truth chosen deliberately", [
            "as the tool,",
            "not a last resort"
        ]),
        ("A precise claim", [
            "never deliberately",
            "harmed a living creature"
        ]),
        ("Rain, without delay", [
            "thunder, then",
            "an immediate downpour"
        ]),
    ],
    further=[
        '<a href="%s/cp30/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-29.html">Cp 29 &mdash; The Baby Quail&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one, the collection's other "
        "act-of-truth story so far.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 31 — Kaṇhadīpāyana Cariyā
# --------------------------------------------------------------------------- #
page(
    31, "Ka&#7751;had&imacr;p&amacr;yana Cariy&amacr;", "Dark Light&rsquo;s Conduct",
    meta_title="Cp 31 — Dark Light's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Dark Light's "
        "Conduct, the Cariyapitaka's most unusual act-of-truth story — a seer cures "
        "snake poison by confessing fifty years of private dissatisfaction. From "
        "Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Truth (5th of 6)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as the seer Dark Light"),
        ("Speaker", "The Buddha, recounting his life as the seer, addressing the "
                    "parents of a poisoned boy"),
        ("Form", "Thirteen verses of first-person narration, including a formal "
                 "declaration of truth"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the collection's "
                       "most conceptually unusual story, worth reading closely"),
    ],
    why=(
        "This story shares its basic device with Cp 29 and Cp 30 &mdash; a formal "
        "declaration of truth, producing a real effect &mdash; but breaks sharply "
        "with them in content. Where the quail and the fish king declared truths that "
        "reflected well on themselves, the seer Dark Light cures a poisoned boy by "
        "confessing something almost no one would willingly admit: that for fifty "
        "years, his own spiritual life has left him unsatisfied."),
    guide=[
        ("A private dissatisfaction, kept secret for decades", [
            "For more than fifty years the seer lived, in his own words, "
            "&lsquo;dissatisfied&rsquo; &mdash; and told no one. The text is explicit "
            "that this was a private, ongoing state, not a passing mood: &lsquo;it "
            "only went on in my mind.&rsquo;"]),
        ("A crisis that has nothing to do with his own struggle", [
            "The emergency that draws out his confession is external: a boy, son of "
            "visiting friends, is bitten by a viper after touching it by accident, and "
            "collapses &mdash; the seer's own decades of quiet dissatisfaction have no "
            "obvious connection to this at all."]),
        ("An unflattering truth, declared as the cure", [
            "Rather than declaring a truth about virtue or non-harm, as in Cp 29 and Cp "
            "30, the seer declares the opposite kind of fact: &lsquo;for just seven "
            "days with a mind of faith I led the spiritual life seeking merit. My life "
            "since then, for fifty years or more, I have lived unwillingly.&rsquo; This "
            "is a confession, not a claim to virtue."]),
        ("The truth's power independent of what it reveals", [
            "The declaration works exactly as the other truth-acts in this chapter do "
            "&mdash; the boy recovers immediately. The story implies that the power of "
            "a saccakiriyā rests on the accuracy of what is declared, not on whether "
            "the content reflects well on the one declaring it."]),
    ],
    terms=[
        ("sacca",
         "&ldquo;truth&rdquo; &mdash; the perfection this story illustrates, the "
         "fifth of six stories on this theme."),
        ("saccakiriyā",
         "an &ldquo;act of truth&rdquo;, here declaring an unflattering private fact "
         "rather than a claim to virtue, unlike Cp 29's and Cp 30's examples."),
        ("Maṇḍabya",
         "a fellow seer and spiritual companion of Dark Light's, whom he nurses back "
         "to health after Maṇḍabya is impaled on a stake, earlier in this story."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its thirty-first."),
        ("Yaññadatta",
         "the name given to the poisoned boy in the seer's own declaration of truth."),
    ],
    text_intro=(
        "The text in full: thirteen verses, including the seer's unusual declaration "
        "of truth. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "Fifty years of private dissatisfaction"),
        ("p", "&sect;1", "cp31:1.1-1.4"),
        ("p", "&sect;2", "cp31:2.1-2.4"),
        ("h3", "A friend nursed, then a crisis with strangers"),
        ("p", "&sect;3", "cp31:3.1-3.4"),
        ("p", "&sect;4", "cp31:4.1-4.4"),
        ("p", "&sect;5", "cp31:5.1-5.4"),
        ("p", "&sect;6", "cp31:6.1-6.4"),
        ("p", "&sect;7", "cp31:7.1-7.4"),
        ("p", "&sect;8", "cp31:8.1-8.4"),
        ("p", "&sect;9", "cp31:9.1-9.4"),
        ("h3", "A confession as the cure"),
        ("p", "&sect;10", "cp31:10.1-10.4"),
        ("p", "&sect;11", "cp31:11.1-11.4"),
        ("p", "&sect;12", "cp31:12.1-12.3"),
        ("p", "&sect;13", "cp31:13.1-13.6"),
    ],
    quiz=[
        {"q": "What does Dark Light keep secret for more than fifty years?",
         "opts": [
             "A great treasure",
             "His own ongoing dissatisfaction with his spiritual life",
             "A crime he committed",
             "His true identity"],
         "correct": 1,
         "expl": "'It only went on in my mind' — private, not a passing mood."},
        {"q": "What crisis prompts the seer's declaration of truth?",
         "opts": [
             "His own illness",
             "A visiting friend's son is bitten by a viper and collapses",
             "A drought threatens his hermitage",
             "An attack by bandits"],
         "correct": 1,
         "expl": "An emergency with no obvious connection to his own private struggle."},
        {"q": "How does this story's declaration of truth differ from Cp 29's and Cp 30's?",
         "opts": [
             "It is identical in content and structure",
             "It confesses an unflattering private fact rather than claiming virtue",
             "It involves no declaration of truth at all",
             "It is spoken by someone else, not the seer himself"],
         "correct": 1,
         "expl": "A sharp break in content while sharing the same underlying device."},
        {"q": "What exactly does the seer declare?",
         "opts": [
             "That he has never harmed a living creature",
             "That only his first seven days of spiritual life were willing; the other fifty-plus years were lived unwillingly",
             "That he possesses great magical power",
             "That the boy deserves to recover"],
         "correct": 1,
         "expl": "A confession, not a claim to virtue."},
        {"q": "What happens after the seer makes this declaration?",
         "opts": [
             "Nothing changes",
             "The boy recovers immediately, just as in Cp 29's and Cp 30's declarations",
             "The boy's condition worsens",
             "The declaration is rejected as insufficient"],
         "correct": 1,
         "expl": "The same immediate effect as the other truth-acts in this chapter."},
        {"q": "What does this story suggest about the source of a truth-act's power?",
         "opts": [
             "It only works when the declared truth is flattering to the speaker",
             "It rests on the accuracy of what is declared, not on whether it reflects well on the speaker",
             "It requires the declaration to be about someone else",
             "It has no connection to the truth of the statement at all"],
         "correct": 1,
         "expl": "An unflattering truth works exactly as well as a flattering one."},
        {"q": "Who is Maṇḍabya, and what happens to him earlier in this story?",
         "opts": [
             "A stranger the seer has never met",
             "A fellow seer and friend, whom Dark Light nurses back to health after he is impaled on a stake",
             "The name of the poisoned boy",
             "A king who visits the hermitage"],
         "correct": 1,
         "expl": "An earlier episode of care, before the main crisis of the story."},
        {"q": "What name does the seer give the poisoned boy in his declaration?",
         "opts": [
             "Maṇḍabya",
             "Yaññadatta",
             "Somanassa",
             "Jāli"],
         "correct": 1,
         "expl": "Named directly: 'May the poison die! May Yaññadatta live!'"},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Ethics",
             "Truth (sacca), the fifth of six stories on this theme",
             "Renunciation",
             "Resolve"],
         "correct": 1,
         "expl": "Continuing the sequence of six truth-stories in this chapter, its most unusual example."},
        {"q": "How is this story's difficulty rating best justified?",
         "opts": [
             "The vocabulary is unusually obscure",
             "It is the collection's most conceptually unusual story, complicating what a 'truth-act' can be about",
             "It is written in an unfamiliar verse meter",
             "It requires knowledge of a separate untranslated text"],
         "correct": 1,
         "expl": "Worth reading closely for what it implies about truthfulness itself."},
    ],
    marginalia=[
        ("Fifty years, unspoken", [
            "a private",
            "dissatisfaction"
        ]),
        ("A stranger's crisis", [
            "unconnected to",
            "his own struggle"
        ]),
        ("An unflattering confession", [
            "not virtue claimed,",
            "but honesty"
        ]),
        ("The same cure, regardless", [
            "truth works,",
            "whatever it reveals"
        ]),
    ],
    further=[
        '<a href="%s/cp31/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-30.html">Cp 30 &mdash; The Fish King&rsquo;s Conduct</a> &mdash; '
        "the text immediately before this one, another act-of-truth story.",
        '<a href="cp-29.html">Cp 29 &mdash; The Baby Quail&rsquo;s Conduct</a> '
        "&mdash; the first of this chapter's three act-of-truth stories.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 32 — Sutasoma Cariyā
# --------------------------------------------------------------------------- #
page(
    32, "Sutasoma Cariy&amacr;", "Sutasoma&rsquo;s Conduct",
    meta_title="Cp 32 — Sutasoma's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Sutasoma's "
        "Conduct, closing the Cariyapitaka's chapter on truth with a king who keeps "
        "a promise to a cannibal, expecting certain death. From Ru-Yi Meditation "
        "Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Truth (6th of 6)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as King Sutasoma"),
        ("Speaker", "The Buddha, recounting his life as Sutasoma, with a brief "
                    "exchange with a cannibal"),
        ("Form", "Six verses of first-person narration"),
        ("Length", "1&ndash;2 minutes to read"),
        ("Northern parallel", "Sutasoma is the subject of his own jātaka in the wider "
                              "tradition; this reading guide does not assert a specific "
                              "matching number."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; a plain, direct "
                       "story closing the chapter on its starkest note"),
    ],
    why=(
        "This story closes the truth chapter with no clever escape and no miraculous "
        "declaration &mdash; only a king, captured by a cannibal who has already "
        "strung up and drained a hundred warriors, granted temporary release on a "
        "promise to return, who then keeps that promise fully expecting to die."),
    guide=[
        ("A captor already shown to be lethal", [
            "Before Sutasoma is even introduced to the reader's attention, the text "
            "establishes exactly what kind of danger he faces: a hundred aristocrat "
            "warriors already strung up by their hands, drained of blood, brought for "
            "sacrifice &mdash; there is no ambiguity about what awaits a broken "
            "promise here."]),
        ("A release granted on trust alone", [
            "The cannibal's offer is oddly formal for someone so violent: "
            "&lsquo;what do you wish for &mdash; release? I shall act as you think, so "
            "long as you will return.&rsquo; Sutasoma's word is treated, even by his "
            "captor, as sufficient security."]),
        ("A debt settled before the return", [
            "Given his freedom, Sutasoma does not flee or fortify his city; he uses "
            "the time to give money to a brahmin, settling an obligation, before "
            "renouncing kingship and going back to the cannibal exactly as promised."]),
        ("No escape, no miracle, only a kept word", [
            "The story closes without any of the reversals seen elsewhere in this "
            "chapter: no clever technicality like Cp 27's monkey, no declaration that "
            "changes the outcome like Cp 29 through Cp 31. Sutasoma states plainly, "
            "&lsquo;I had no doubt that he was going to kill me&rsquo;, and returns "
            "anyway, closing the chapter on its most unadorned example of what keeping "
            "one's word can cost."]),
    ],
    terms=[
        ("sacca",
         "&ldquo;truth&rdquo; &mdash; the perfection this story illustrates, closing "
         "this chapter's six stories on the theme."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its thirty-second."),
        ("Yudhañjaya-vagga",
         "&ldquo;the Chapter With Yudhañjaya&rdquo; &mdash; this collection's third "
         "chapter, now moving from truth into its final two themes, love and "
         "equanimity."),
        ("Sutasoma Jātaka",
         "the fuller version of this story in the separate Jātaka tradition, not "
         "otherwise covered on this site."),
        ("pabbajjā",
         "&ldquo;going forth&rdquo; &mdash; the renunciation of kingship Sutasoma "
         "undertakes in the brief window between his release and his return to the "
         "cannibal."),
    ],
    text_intro=(
        "The text in full: six verses, closing the Cariyapitaka's chapter on truth. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp32:1.1-1.4"),
        ("p", "&sect;2", "cp32:2.1-2.4"),
        ("p", "&sect;3", "cp32:3.1-3.4"),
        ("p", "&sect;4", "cp32:4.1-4.4"),
        ("p", "&sect;5", "cp32:5.1-5.4"),
        ("p", "&sect;6", "cp32:6.1-6.6"),
    ],
    quiz=[
        {"q": "What has the cannibal already done to a hundred warriors before this story's main events?",
         "opts": [
             "Released them all unharmed",
             "Strung them up by their hands and drained their blood",
             "Made them his servants",
             "Nothing is said about other warriors"],
         "correct": 1,
         "expl": "Establishing exactly what kind of danger Sutasoma faces."},
        {"q": "What does the cannibal offer Sutasoma?",
         "opts": [
             "Immediate death with no discussion",
             "Temporary release, on the condition that he will return",
             "A trade of places with another prisoner",
             "Nothing; Sutasoma is never released"],
         "correct": 1,
         "expl": "The king's word treated as sufficient security by his own captor."},
        {"q": "What does Sutasoma do with his temporary freedom?",
         "opts": [
             "He flees to a distant kingdom",
             "He fortifies his city against attack",
             "He settles a debt with a brahmin and renounces kingship",
             "He raises an army to fight the cannibal"],
         "correct": 2,
         "expl": "Using the time to settle an obligation, not to escape his promise."},
        {"q": "Does Sutasoma attempt to avoid returning to the cannibal?",
         "opts": [
             "Yes, he breaks his promise",
             "No — he returns exactly as promised",
             "He sends someone else in his place",
             "The story does not say whether he returns"],
         "correct": 1,
         "expl": "Keeping his word despite having every opportunity to flee."},
        {"q": "Does Sutasoma expect to survive his return?",
         "opts": [
             "Yes, he is certain of a clever escape",
             "No — 'I had no doubt that he was going to kill me'",
             "The text leaves this unclear",
             "He expects to be rescued at the last moment"],
         "correct": 1,
         "expl": "Returning with full awareness of the likely outcome."},
        {"q": "How does this story's resolution differ from Cp 27's, Cp 29's, Cp 30's, and Cp 31's?",
         "opts": [
             "It uses the same clever technicality as Cp 27",
             "It uses the same declaration-of-truth device as Cp 29 through Cp 31",
             "It has no reversal or miracle at all — just a kept promise",
             "It is the only story where the character breaks their word"],
         "correct": 2,
         "expl": "The chapter's most unadorned example of what truthfulness can cost."},
        {"q": "What perfection does this story close out?",
         "opts": [
             "Ethics",
             "Truth (sacca), the sixth and final story of this theme",
             "Renunciation",
             "Resolve"],
         "correct": 1,
         "expl": "Six stories on truth conclude here."},
        {"q": "What two themes does this collection's chapter move to next, after truth?",
         "opts": [
             "Giving and ethics",
             "Love and equanimity",
             "Renunciation and resolve",
             "The collection ends here"],
         "correct": 1,
         "expl": "Two stories on love, then one on equanimity, closing the whole collection."},
        {"q": "What does Sutasoma's story share with Cp 19's Alīnasattu?",
         "opts": [
             "Nothing; the two stories are unrelated",
             "Both involve a cannibal captor and a character facing likely death calmly",
             "Both stories involve a viper bite",
             "Both are the shortest stories in their chapters"],
         "correct": 1,
         "expl": "A recurring cannibal motif across this collection's final chapter."},
        {"q": "What does 'pabbajjā' mean, as used in this story?",
         "opts": [
             "'Going forth' — the renunciation Sutasoma undertakes before returning to the cannibal",
             "'Blood debt'",
             "'Broken promise'",
             "'Royal decree'"],
         "correct": 0,
         "expl": "Undertaken in the brief window of his freedom."},
    ],
    marginalia=[
        ("A captor already lethal", [
            "a hundred warriors,",
            "drained already"
        ]),
        ("Released on his word alone", [
            "no guarantee",
            "but a promise"
        ]),
        ("A debt settled first", [
            "before returning,",
            "not fleeing"
        ]),
        ("No escape, no miracle", [
            "just a promise",
            "kept anyway"
        ]),
    ],
    further=[
        '<a href="%s/cp32/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-31.html">Cp 31 &mdash; Dark Light&rsquo;s Conduct</a> &mdash; '
        "the text immediately before this one, closing the chapter on truth.",
        '<a href="cp-19.html">Cp 19 &mdash; Al&imacr;nasattu&rsquo;s Conduct</a> '
        "&mdash; another story of a captive cannibal encounter.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 33 — Suvaṇṇasāma Cariyā
# --------------------------------------------------------------------------- #
page(
    33, "Suva&#7751;&#7751;as&amacr;ma Cariy&amacr;", "Goldblack&rsquo;s Conduct",
    meta_title="Cp 33 — Goldblack's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for Goldblack's "
        "Conduct, opening the Cariyapitaka's chapter on loving-kindness with a figure "
        "who lives fearlessly among lions and tigers. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Love (1st of 2)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as Sāma, a figure created by Sakka, "
                    "living in a forest full of predators"),
        ("Speaker", "The Buddha, recounting his life as Sāma"),
        ("Form", "Three four-line verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "A figure named Suvaṇṇasāma is the subject of his own "
                              "jātaka in the wider tradition; this reading guide does "
                              "not assert a specific matching number."),
        ("Difficulty", "&starf;&#9734;&#9734;&#9734;&#9734; &mdash; a short, peaceful "
                       "story opening the collection's penultimate theme"),
    ],
    why=(
        "This story opens the Cariyapitaka's chapter on loving-kindness with an image "
        "rather than a crisis: a figure created by Sakka lives surrounded by lions, "
        "tigers, leopards, bears, and the animals those predators would ordinarily "
        "hunt, all coexisting without fear &mdash; sustained, the text says, purely by "
        "the power of love."),
    guide=[
        ("An unusual origin, stated without elaboration", [
            "Sāma is described as &lsquo;created by Sakka&rsquo;, a detail the text "
            "does not explain further &mdash; a different kind of beginning than the "
            "births, ordinary or unusual, that open most of this collection's other "
            "stories."]),
        ("Predator and prey together, without incident", [
            "The forest Sāma inhabits holds lions and tigers alongside leopards, "
            "bears, buffaloes, spotted deer, and wild boar &mdash; species that would "
            "ordinarily prey on one another, gathered in a single list with no "
            "predation described taking place."]),
        ("Fearlessness stated as mutual, not one-directional", [
            "The text is specific about the relationship: &lsquo;none were scared of "
            "me, nor I of them&rsquo; &mdash; loving-kindness here is not simply Sāma's "
            "own emotional state but a shared condition affecting how every creature "
            "in the forest related to every other."]),
        ("A different kind of perfection story", [
            "Unlike nearly every other story in this collection, this one describes no "
            "test, no threat, and no decision under pressure &mdash; only a sustained "
            "condition, described directly as delightful rather than as an achievement "
            "won through struggle."]),
    ],
    terms=[
        ("mettā",
         "&ldquo;loving-kindness&rdquo; &mdash; the perfection this story illustrates, "
         "the first of two stories on this theme, and the same central practice "
         "taught in Kp 9 and Snp 1.8, the Metta Sutta."),
        ("Sakka",
         "king of the gods, described here as Sāma's creator, a detail unique to this "
         "story among this collection's many appearances of Sakka."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its thirty-third."),
        ("Suvaṇṇasāma Jātaka",
         "the fuller version of this story in the separate Jātaka tradition, not "
         "otherwise covered on this site."),
        ("Yudhañjaya-vagga",
         "&ldquo;the Chapter With Yudhañjaya&rdquo; &mdash; this collection's third "
         "chapter, now in its penultimate theme."),
    ],
    text_intro=(
        "The text in full: three verses, opening the Cariyapitaka's chapter on "
        "loving-kindness. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp33:1.1-1.4"),
        ("p", "&sect;2", "cp33:2.1-2.4"),
        ("p", "&sect;3", "cp33:3.1-3.4"),
    ],
    quiz=[
        {"q": "How is Sāma's origin described in this text?",
         "opts": [
             "Born to human parents, like most figures in this collection",
             "Created by Sakka, a detail left unexplained",
             "Hatched from an egg",
             "No origin is given at all"],
         "correct": 1,
         "expl": "A different kind of beginning than most other stories in this collection."},
        {"q": "What kinds of animals does Sāma live among?",
         "opts": [
             "Only gentle herbivores",
             "Lions, tigers, leopards, bears, buffaloes, spotted deer, and wild boar together",
             "Only predators, with no prey species present",
             "Domesticated farm animals"],
         "correct": 1,
         "expl": "Predators and prey gathered in the same list, without incident."},
        {"q": "How does the text describe the fear between Sāma and the animals?",
         "opts": [
             "Only the animals fear Sāma",
             "Only Sāma fears the animals",
             "'None were scared of me, nor I of them' — a mutual condition",
             "Fear is not addressed in the text"],
         "correct": 2,
         "expl": "A shared condition, not one-directional."},
        {"q": "What does the text say sustains this peaceful coexistence?",
         "opts": [
             "Sāma's physical strength",
             "The power of love (mettā)",
             "A magical barrier",
             "Fear of Sakka's punishment"],
         "correct": 1,
         "expl": "Named directly as the sustaining force."},
        {"q": "How does this story differ structurally from most others in this collection?",
         "opts": [
             "It describes no test, threat, or decision under pressure — only a sustained peaceful condition",
             "It is the longest story in the collection",
             "It is the only story with no animals present",
             "It follows an identical structure to every other story"],
         "correct": 0,
         "expl": "Described as delightful rather than as an achievement won through struggle."},
        {"q": "What perfection does this story open, and how many stories does this chapter give it?",
         "opts": [
             "Truth; six stories",
             "Love (mettā); two stories",
             "Equanimity; one story",
             "Resolve; one story"],
         "correct": 1,
         "expl": "The fourth of the third chapter's five themes."},
        {"q": "What other texts on this site teach the same central practice named here?",
         "opts": [
             "No other texts on this site cover this theme",
             "Kp 9 and Snp 1.8, both called the Metta Sutta",
             "Only the Dhammapada",
             "Only the Ratana Sutta"],
         "correct": 1,
         "expl": "The same practice of loving-kindness, in a very different form here."},
        {"q": "What role does Sakka play in this particular story, unique among this collection's other Sakka appearances?",
         "opts": [
             "He tests the protagonist's resolve",
             "He is described as Sāma's creator",
             "He disguises himself as a beggar",
             "Sakka does not appear in this story"],
         "correct": 1,
         "expl": "Different from Sakka's usual role elsewhere in the Cariyapitaka."},
        {"q": "What perfection did the previous chapter section (Cp 27–32) cover?",
         "opts": [
             "Ethics",
             "Truth (sacca), across six stories",
             "Giving",
             "Resolve"],
         "correct": 1,
         "expl": "Now followed by two stories on love."},
        {"q": "What perfection does this story illustrate?",
         "opts": [
             "Truth",
             "Love (mettā), the first of two stories on this theme",
             "Renunciation",
             "Ethics"],
         "correct": 1,
         "expl": "Opening this chapter's final pair of stories before equanimity closes the collection."},
    ],
    marginalia=[
        ("Created by Sakka", [
            "a detail left",
            "unexplained"
        ]),
        ("Predator and prey together", [
            "lions, tigers, deer,",
            "boar, unharmed"
        ]),
        ("A mutual fearlessness", [
            "'none were scared",
            "of me, nor I of them'"
        ]),
        ("No test, only a condition", [
            "sustained,",
            "not struggled for"
        ]),
    ],
    further=[
        '<a href="%s/cp33/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-32.html">Cp 32 &mdash; Sutasoma&rsquo;s Conduct</a> &mdash; the '
        "text immediately before this one, closing the chapter on truth.",
        '<a href="../khuddakapatha/kp-9.html">Kp 9 &mdash; The Discourse on Love</a> '
        "&mdash; the Khuddakapatha's own text on this same practice of loving-"
        "kindness.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 34 — Ekarāja Cariyā
# --------------------------------------------------------------------------- #
page(
    34, "Ekar&amacr;ja Cariy&amacr;", "The One King&rsquo;s Conduct",
    meta_title="Cp 34 — The One King's Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for The One King's "
        "Conduct, closing the Cariyapitaka's chapter on loving-kindness with a "
        "calamity described in full but its resolution left entirely untold. From "
        "Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Love (2nd of 2)",
    glance=[
        ("Setting", "No external narrative frame; the Buddha speaks in the first "
                    "person about his past life as a just king, ruling the whole "
                    "earth"),
        ("Speaker", "The Buddha, recounting his life as the One King"),
        ("Form", "Five verses of first-person narration"),
        ("Length", "under 1 minute to read"),
        ("Northern parallel", "This reading guide does not assert a specific matching "
                              "text for this story in other Buddhist literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; short, but ends on "
                       "its claim before showing the conduct that earns it"),
    ],
    why=(
        "This is the most abrupt story in the whole collection: a diligent, "
        "ethical king is overthrown, his city sacked, his court and family captured, "
        "and he himself buried in a pit &mdash; and then, without narrating any act "
        "of forgiveness, mercy, or restraint toward the man who did this to him, the "
        "text simply declares, &lsquo;there is no-one to equal my love: this is my "
        "perfection of love.&rsquo;"),
    guide=[
        ("A model ruler, established briefly", [
            "The opening verses establish the king's character economically: "
            "&lsquo;resolved on highest ethics&rsquo;, following the ten skillful "
            "deeds without exception, using the four ways of being inclusive to unite "
            "his population &mdash; a ruler doing everything right."]),
        ("A sudden, total reversal", [
            "Dabbasena's attack is described with no warning and no buildup: the city "
            "is sacked, the king's dependents, military, and citizens are all "
            "captured, and the king himself is buried in a pit &mdash; a complete "
            "collapse compressed into a single verse."]),
        ("A claim made without its evidence shown", [
            "Unlike Cp 33's Sāma, whose peaceful coexistence with the forest's animals "
            "is at least described directly, this story never shows what loving-"
            "kindness toward Dabbasena, or toward anyone else in this crisis, actually "
            "looked like. The text moves from calamity straight to the claim of "
            "perfected love, with the demonstrating action itself left out entirely."]),
        ("The most extreme gap in a collection full of them", [
            "Several stories in this collection leave a resolution untold &mdash; Cp "
            "9's Vessantara, Cp 19's Alīnasattu, Cp 26's Temiya. This story goes "
            "further: it is not the outcome that goes unnarrated here, but the entire "
            "action the title perfection is named for. What the fuller Ekarāja "
            "tradition presumably shows &mdash; forgiveness, or restraint toward a "
            "captor &mdash; this particular verse selection does not include at all."]),
    ],
    terms=[
        ("mettā",
         "&ldquo;loving-kindness&rdquo; &mdash; the perfection this story illustrates, "
         "closing this chapter's two stories on the theme."),
        ("dasakusalakammapatha",
         "the &ldquo;ten skillful deeds&rdquo;, the same standard named in Cp 3 and Cp "
         "18, followed here &lsquo;without exception&rsquo; by the king before his "
         "downfall."),
        ("saṅgahavatthu",
         "the &ldquo;four ways of being inclusive&rdquo; &mdash; the methods the king "
         "uses to unite his population, named directly in this text."),
        ("Dabbasena",
         "the attacker who sacks the king's city and buries him in a pit; the text "
         "gives no further detail about him or what became of the conflict."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its thirty-fourth."),
    ],
    text_intro=(
        "The text in full: five verses, closing the Cariyapitaka's chapter on "
        "loving-kindness. Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("p", "&sect;1", "cp34:1.1-1.4"),
        ("p", "&sect;2", "cp34:2.1-2.4"),
        ("p", "&sect;3", "cp34:3.1-3.4"),
        ("p", "&sect;4", "cp34:4.1-4.4"),
        ("p", "&sect;5", "cp34:5.1-5.6"),
    ],
    quiz=[
        {"q": "How is the king's character established at this story's opening?",
         "opts": [
             "As cruel and self-serving",
             "As a model ruler, resolved on highest ethics and uniting his people",
             "As weak and indecisive",
             "No character description is given"],
         "correct": 1,
         "expl": "Following the ten skillful deeds without exception."},
        {"q": "What happens to the king's city and family?",
         "opts": [
             "Nothing; the kingdom remains at peace throughout",
             "The city is sacked, his family and court captured, and he is buried in a pit",
             "The king successfully repels the attack",
             "He voluntarily abdicates"],
         "correct": 1,
         "expl": "A complete, sudden reversal compressed into a single verse."},
        {"q": "Who attacks the king, and what further detail does the text give about him?",
         "opts": [
             "Dabbasena; the text gives extensive backstory",
             "Dabbasena; the text gives no further detail about him at all",
             "No attacker is named",
             "The king attacks himself in a moment of madness"],
         "correct": 1,
         "expl": "Named, but otherwise left unexplained."},
        {"q": "Does this text show any specific act of loving-kindness the king performs?",
         "opts": [
             "Yes, in great detail",
             "No — the text moves from the calamity directly to the claim of perfected love, without showing the demonstrating action",
             "Yes, but only briefly summarized",
             "The king explicitly refuses to show love in this story"],
         "correct": 1,
         "expl": "The most extreme gap of its kind in this collection."},
        {"q": "How does this story's gap compare to Cp 9's Vessantara or Cp 26's Temiya?",
         "opts": [
             "It is identical — only the final outcome is left untold",
             "It goes further — here the entire action demonstrating the perfection is left out, not just the outcome",
             "There is no gap in this story at all",
             "This story has no connection to those other gaps"],
         "correct": 1,
         "expl": "The most extreme example of this pattern in the whole collection."},
        {"q": "What does 'saṅgahavatthu' refer to in this story?",
         "opts": [
             "A type of weapon",
             "The 'four ways of being inclusive' the king uses to unite his population",
             "The name of the attacking army",
             "A ritual performed before battle"],
         "correct": 1,
         "expl": "Named directly as part of the king's good governance."},
        {"q": "What standard of conduct, also named in Cp 3 and Cp 18, does this king follow?",
         "opts": [
             "The eightfold path",
             "The ten skillful deeds (dasakusalakammapatha)",
             "The five precepts",
             "The four noble truths"],
         "correct": 1,
         "expl": "A recurring standard across several stories in this collection."},
        {"q": "What perfection does this story close, and what position does it hold?",
         "opts": [
             "Truth, the fifth of six stories",
             "Love (mettā), the second and final story of this theme",
             "Equanimity, the collection's only story on this theme",
             "Renunciation, the third of five stories"],
         "correct": 1,
         "expl": "Closing this chapter's pair of stories before equanimity closes the whole collection."},
        {"q": "What does the king see during the calamity, mentioned in the story's final lines?",
         "opts": [
             "His enemy's defeat",
             "His beloved son, captured along with the rest of his court",
             "A vision of his own future",
             "Nothing further is described"],
         "correct": 1,
         "expl": "One of the last details given before the closing claim."},
        {"q": "What is the very last perfection covered by the Cariyapitaka's thirty-five stories, immediately after this one?",
         "opts": [
             "Wisdom",
             "Equanimity, in a single closing story",
             "Patience",
             "Energy"],
         "correct": 1,
         "expl": "Cp 35, the collection's final text."},
    ],
    marginalia=[
        ("A model ruler", [
            "ethics upheld",
            "without exception"
        ]),
        ("A sudden collapse", [
            "city sacked,",
            "family captured"
        ]),
        ("A claim, unshown", [
            "no act of love",
            "actually narrated"
        ]),
        ("The collection's deepest gap", [
            "not just the outcome —",
            "the whole demonstration"
        ]),
    ],
    further=[
        '<a href="%s/cp34/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-33.html">Cp 33 &mdash; Goldblack&rsquo;s Conduct</a> &mdash; the '
        "text immediately before this one, this chapter's other story on love.",
        '<a href="../dhammapada/">Dhammapada</a> &mdash; another complete Khuddaka Nikāya '
        "collection on this site.",
        '<a href="../sutta-nipata/">Sutta Nipāta</a> &mdash; another complete Khuddaka '
        "Nikāya collection, entirely in verse.",
    ],
)


# --------------------------------------------------------------------------- #
# Cp 35 — Lomahaṁsa Cariyā
# --------------------------------------------------------------------------- #
page(
    35, "Lomaha&#7745;sa Cariy&amacr;", "The Great Hair-raising Conduct",
    meta_title="Cp 35 — The Great Hair-raising Conduct | Ru-Yi Meditation Center",
    meta_desc=(
        "A reading guide, full English text, and self-check quiz for the "
        "Cariyapitaka's final story and closing verses — sleeping in a charnel "
        "ground, equanimity toward mockery and honor alike, and a summary of the "
        "whole collection. From Ru-Yi Meditation Center."),
    vagga="The Chapter With Yudhañjaya &middot; The Perfection of Equanimity (1 of 1)",
    glance=[
        ("Setting", "No external narrative frame for the story itself; the second "
                    "half of this page is a closing summary addressed to no "
                    "particular audience, closing the whole Cariyapitaka"),
        ("Speaker", "The Buddha, recounting his life sleeping in a charnel ground, "
                    "then speaking in his own voice as the summary closes the work"),
        ("Form", "Four verses telling the final individual story, followed by a "
                 "separate closing sequence of verses summarizing the whole "
                 "collection"),
        ("Length", "2&ndash;3 minutes to read"),
        ("Northern parallel", "This reading guide does not assert a specific "
                              "matching text for this story in other Buddhist "
                              "literatures."),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; the final story "
                       "is simple; the closing summary rewards a careful second "
                       "read"),
    ],
    why=(
        "This page closes the entire Cariyapitaka. Its own thirty-fifth story is "
        "brief: a figure who sleeps in a charnel ground, resting on a skeleton, "
        "treated with total equanimity whether mocked by louts or honored with "
        "incense and food. What follows it is not part of that story at all "
        "&mdash; it is the collection's own closing summary, naming several "
        "perfections in review before a final colophon names the whole work."),
    guide=[
        ("A bed among the dead", [
            "The setting is stark and unadorned: a charnel ground, a skeleton for a "
            "bed. Village louts mock the sleeper &lsquo;in all sorts of ways&rsquo;; "
            "others bring incense, flowers, and fine food, thrilled and reverent. Both "
            "receive the identical response."]),
        ("Equanimity defined by what it does not distinguish", [
            "The story states its perfection plainly: &lsquo;those who brought me "
            "pain, and those who gave me happiness, were all the same to me. I felt no "
            "favor or anger.&rsquo; Unlike the restraint shown in the ethics chapter, "
            "which withholds a specific retaliation, this is a flatness applied "
            "equally to opposite treatment, not a response to any one threat."]),
        ("A numbering gap in the source itself", [
            "This page's sections jump directly from &sect;4, the end of the story "
            "proper, to &sect;10 &mdash; sections 5 through 9 do not exist in the "
            "source text at all. This reading guide reproduces the source exactly as "
            "numbered, rather than renumbering to hide the gap."]),
        ("A closing summary, not another story", [
            "Section 10 onward is a different kind of writing: a review naming "
            "several perfections in quick succession &mdash; giving, ethics, "
            "renunciation, and, notably, a &lsquo;perfection of acceptance&rsquo; "
            "alongside effort and inquiry, resolve and truthful speech, and finally "
            "equanimity again &mdash; each said to lead to &lsquo;supreme "
            "awakening&rsquo;. This summary mentions qualities, like acceptance, that "
            "did not receive their own dedicated story anywhere in the preceding "
            "thirty-five &mdash; the individual stories dramatize seven perfections in "
            "depth, while this closing review gestures more broadly across the "
            "tradition's fuller list of ten."]),
        ("Three short exhortations, then a colophon", [
            "Before the work closes, three brief verses repeat a single pattern "
            "&mdash; laziness feared, energy as sanctuary; dispute feared, harmony as "
            "sanctuary; negligence feared, the eightfold path as sanctuary &mdash; each "
            "closing with the same refrain, &lsquo;this is the Buddha's "
            "instruction!&rsquo; A final sentence then names the whole work: "
            "&lsquo;the exposition of the teaching named the &lsquo;Legends of the "
            "Buddha&rsquo;.&rsquo;"]),
    ],
    terms=[
        ("upekkhā",
         "&ldquo;equanimity&rdquo; &mdash; the perfection this final story "
         "illustrates, the last of the seven perfections given a dedicated story in "
         "this particular collection."),
        ("Lomahaṁsa",
         "&ldquo;hair-raising&rdquo; &mdash; part of this story's title, referring to "
         "the unsettling austerity of sleeping in a charnel ground."),
        ("saccakiriyā-vagga",
         "not a formal term in this translation, but a useful label for the pattern "
         "closing several of this chapter's stories: &lsquo;seeing X as fearful, and Y "
         "as sanctuary... this is the Buddha's instruction!&rsquo;"),
        ("Buddhāpadāniya",
         "&ldquo;Legends of the Buddha&rdquo; &mdash; the name this text's own closing "
         "colophon gives to the whole exposition, referring to the Cariyapitaka "
         "itself."),
        ("cariyā",
         "&ldquo;conduct&rdquo; &mdash; this collection's title, and the word used for "
         "each of its thirty-five stories, this one its thirty-fifth and last."),
    ],
    text_intro=(
        "The text in full: four verses telling the final story, then the "
        "Cariyapitaka's own closing summary and colophon. The source's own section "
        "numbering skips from 4 to 10, reproduced here as it stands. "
        "Translation: Bhikkhu Sujato (CC0, SuttaCentral)."),
    text=[
        ("h3", "The Great Hair-raising Conduct"),
        ("p", "&sect;1", "cp35:1.1-1.4"),
        ("p", "&sect;2", "cp35:2.1-2.4"),
        ("p", "&sect;3", "cp35:3.1-3.4"),
        ("p", "&sect;4", "cp35:4.1-4.4"),
        ("h3", "Closing verses of the whole Cariyapitaka"),
        ("p", "&sect;10", "cp35:10.1-10.4"),
        ("p", "&sect;11", "cp35:11.1-11.4"),
        ("p", "&sect;12", "cp35:12.1-12.4"),
        ("p", "&sect;13", "cp35:13.1-13.4"),
        ("p", "&sect;14", "cp35:14.1-14.4"),
        ("p", "&sect;15", "cp35:15.1-15.4"),
        ("p", "&sect;16", "cp35:16.1-16.4"),
        ("p", "&sect;17", "cp35:17.1-17.4"),
        ("p", "&sect;18", "cp35:18.1-18.1"),
    ],
    quiz=[
        {"q": "Where does the final story's protagonist sleep?",
         "opts": [
             "In a royal palace",
             "In a charnel ground, resting on a skeleton",
             "In a forest hermitage",
             "On a riverbank"],
         "correct": 1,
         "expl": "An unsettling, unadorned setting."},
        {"q": "How does the protagonist respond to being mocked versus being honored with incense and food?",
         "opts": [
             "With anger at the mockers, gratitude toward the honorers",
             "With the identical response — no favor, no anger, in either case",
             "By fleeing from both groups",
             "By punishing the mockers"],
         "correct": 1,
         "expl": "'Those who brought me pain, and those who gave me happiness, were all the same to me.'"},
        {"q": "What is unusual about the section numbering on this particular page?",
         "opts": [
             "Nothing; the numbering is entirely continuous",
             "It jumps directly from section 4 to section 10, with no sections 5 through 9 in the source",
             "It restarts from 1 partway through",
             "It uses letters instead of numbers"],
         "correct": 1,
         "expl": "Reproduced here exactly as the source has it, not smoothed over."},
        {"q": "What is the second half of this page, starting at section 10?",
         "opts": [
             "A continuation of the charnel-ground story",
             "A separate closing summary reviewing several perfections, not part of the individual story",
             "An unrelated discourse copied in by mistake",
             "A repeat of the first half"],
         "correct": 1,
         "expl": "Closing the entire Cariyapitaka, not just this final story."},
        {"q": "What perfection does the closing summary mention that received no dedicated story among the collection's thirty-five?",
         "opts": [
             "Giving",
             "A 'perfection of acceptance', alongside effort and inquiry",
             "Ethics",
             "Truth"],
         "correct": 1,
         "expl": "The summary gestures more broadly across the tradition's full list of ten than the individual stories do."},
        {"q": "What refrain closes each of the summary's three brief exhortations?",
         "opts": [
             "'This is the highest blessing'",
             "'This is the Buddha's instruction!'",
             "'By this truth, may you be well'",
             "'There is no-one to equal me'"],
         "correct": 1,
         "expl": "Repeated after each fear-and-sanctuary pairing: laziness, dispute, negligence."},
        {"q": "What name does the text's own closing colophon give to the whole work?",
         "opts": [
             "'The Basket of Conduct' only",
             "'The exposition of the teaching named the Legends of the Buddha'",
             "No name is given at all",
             "'The Thirty-Five Perfections'"],
         "correct": 1,
         "expl": "A traditional close-of-text formula naming the exposition."},
        {"q": "What does 'Lomahaṁsa' mean, as part of this story's title?",
         "opts": [
             "'Hair-raising' — referring to the unsettling austerity of the setting",
             "'Equanimity'",
             "'Charnel ground'",
             "'Skeleton'"],
         "correct": 0,
         "expl": "Describing the effect of the practice, not a proper name."},
        {"q": "How does this story's equanimity differ from the ethics chapter's restraint (Cp 11–20)?",
         "opts": [
             "There is no meaningful difference",
             "The ethics chapter withholds a specific retaliation against one threat; equanimity applies a flatness equally to opposite treatment",
             "Equanimity only applies to positive experiences",
             "The ethics chapter is about kindness, not restraint"],
         "correct": 1,
         "expl": "A response to a whole range of treatment, not a single provocation."},
        {"q": "What perfection does this final story illustrate?",
         "opts": [
             "Truth",
             "Equanimity (upekkhā), the last of seven perfections given a dedicated story in this collection",
             "Love",
             "Resolve"],
         "correct": 1,
         "expl": "Closing the Cariyapitaka's thirty-five stories."},
    ],
    marginalia=[
        ("A bed among the dead", [
            "a charnel ground,",
            "a skeleton for rest"
        ]),
        ("No favor, no anger", [
            "mockery and honor",
            "treated the same"
        ]),
        ("A gap in the numbering", [
            "sections 5 to 9",
            "absent from the source"
        ]),
        ("A summary, then a name", [
            "'Legends of the Buddha' —",
            "the whole work closed"
        ]),
    ],
    further=[
        '<a href="%s/cp35/en/sujato" target="_blank" rel="noopener">Full Sujato '
        "translation on SuttaCentral</a> &mdash; with Pāli alongside, segment by "
        "segment." % SC,
        '<a href="cp-34.html">Cp 34 &mdash; The One King&rsquo;s Conduct</a> '
        "&mdash; the text immediately before this one, closing the chapter on love.",
        '<a href="cp-1.html">Cp 1 &mdash; Akitti&rsquo;s Conduct</a> &mdash; the '
        "collection's opening story, on the perfection of giving.",
        '<a href="./">Cariyapiṭaka</a> &mdash; back to the collection index, all '
        "thirty-five stories.",
    ],
)
