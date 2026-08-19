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
