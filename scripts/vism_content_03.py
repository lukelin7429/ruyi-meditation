# -*- coding: utf-8 -*-
"""Visuddhimagga -- Part III: Paññā (Understanding), Chapters 14-23.

Same no-verbatim-text policy as vism_content_01.py/02.py -- see
vism_build.py's docstring. This module opens with Chapter 14; HEAD points
back at the last page of Part II (vism-13.html), TAIL stays at the
collection page since this is the work's final part.
"""

PDF_LINK = ('<a href="https://www.accesstoinsight.org/lib/authors/nanamoli/'
            'PathofPurification2011.pdf" target="_blank" rel="noopener">Bhikkhu '
            'Ñāṇamoli&rsquo;s full translation (PDF, Access to Insight)</a> '
            '&mdash; the complete English text, distributed free by the Buddhist '
            'Publication Society; not reproduced here as it remains under '
            'copyright.')
SC_LINK = ('<a href="https://suttacentral.net/vism/pli/ms" target="_blank" '
           'rel="noopener">The Pali root text on SuttaCentral</a> &mdash; '
           'Buddhaghosa&rsquo;s original composition, public domain.')

INDEX_HEADING = "Part III: Paññā — Understanding (Chapters 14&ndash;23)"
HEAD = ("vism-13.html", "The Other Direct-Knowledges")
TAIL = ("./", "Visuddhimagga guide")
INDEX_EXTRA = []

PAGES = []


def page(num, pali, title, **kw):
    """Shared scaffolding for a single Visuddhimagga chapter guide."""
    d = {
        "slug": "vism-%d" % num,
        "index_pali": pali,
        "nav_title": title,
        "crumb": "Chapter %d" % num,
        "number_line": "Visuddhimagga &middot; Chapter %d" % num,
        "title": title,
        "subtitle": "<em>%s</em>%s" % (
            pali, " &mdash; %s" % kw.pop("part") if "part" in kw else ""),
    }
    d.update(kw)
    PAGES.append(d)
    return d


PART_3 = "Part III: Paññā (Understanding)"

# --------------------------------------------------------------------------- #
# Chapter 14 -- Khandhaniddesa
# --------------------------------------------------------------------------- #
page(
    14, "Khandhaniddesa", "The Aggregates",
    part=PART_3,
    meta_title="Visuddhimagga Ch. 14 — The Aggregates | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 14 of the Visuddhimagga (The Path of "
        "Purification) — the five aggregates, why each is called an "
        "&lsquo;aggregate&rsquo;, an elevenfold cross-section applied to each, and "
        "why this analysis marks the real beginning of insight. No translated text "
        "reproduced; links to the full free translation and the Pali original. "
        "From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter opens Part III with the same "
                    "systematic method Part I used for virtue, now turned toward "
                    "analysis rather than practical training"),
        ("Speaker", "Buddhaghosa, opening the ten-chapter section on understanding"),
        ("Form", "Five categories analyzed in turn, each run through a defining "
                 "framework and then a recurring elevenfold classification"),
        ("Length", "substantial, given the systematic detail applied to each of the "
                   "five categories in turn"),
        ("Northern parallel", "Analysis of a person into five aggregates is one of "
                              "the most widely shared frameworks across Buddhist "
                              "traditions; this guide does not assert a specific "
                              "matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the most "
                       "abstract material the series has covered so far, opening "
                       "the doctrinally dense final third of the work"),
    ],
    why=(
        "Parts I and II built the practical foundation (virtue) and the meditative "
        "skill (concentration) the whole path depends on. Part III turns to what "
        "all of that has been in service of: seeing clearly. Chapter 14 opens this "
        "work with the most basic analytical move the rest of the section builds "
        "on &mdash; breaking down what is ordinarily experienced as a single, "
        "unified person into five aggregates, none of which, examined "
        "individually, amounts to anything fixed."),
    guide=[
        ("A different kind of chapter", [
            "Where Parts I and II were organized around practical training "
            "&mdash; conduct to take up, subjects to develop &mdash; Part III works "
            "by taking apart what ordinarily looks unified. Chapter 14 is where "
            "that analytical project begins."]),
        ("Five aggregates", [
            "The chapter treats five categories in turn: form, covering material "
            "and physical phenomena; feeling, the pleasant, unpleasant, or neutral "
            "quality of experience; perception, the factor that recognizes and "
            "labels; formations, a broad and notably heterogeneous category "
            "covering the mind's remaining volitional and constructing activity; "
            "and consciousness, bare cognizing awareness, itself further divided "
            "by which of the six sense doors it arises through."]),
        ("Why &lsquo;aggregate&rsquo;", [
            "The chapter explains the term khandha as reflecting that each of the "
            "five is itself a grouping rather than a single thing &mdash; form "
            "alone covers many distinct material phenomena bundled under one "
            "heading, and the same holds for each of the other four."]),
        ("An elevenfold cross-section", [
            "Rather than offering one flat definition, the chapter applies a "
            "recurring elevenfold classification to each of the five aggregates in "
            "turn: past, future, and present; internal and external; gross and "
            "subtle; inferior and superior; far and near &mdash; producing a "
            "systematic cross-section of each category rather than a single "
            "summary statement."]),
        ("Five aggregates, no fixed self", [
            "The chapter's underlying point is made explicit through this "
            "analysis: what is conventionally experienced and spoken of as a "
            "single &lsquo;person&rsquo; or &lsquo;self&rsquo; resolves, on "
            "examination, into five distinct, constantly varying categories, none "
            "of which by itself constitutes anything fixed or unified."]),
        ("The actual start of insight", [
            "This kind of analytical seeing, rather than concentration itself, is "
            "what the tradition calls insight (<em>vipassanā</em>), and this "
            "chapter marks its real beginning within the Visuddhimagga's own "
            "structure, distinct from everything Part II covered."]),
        ("What follows", [
            "Chapter 15 continues the same analytical project with two further "
            "classification schemes: the sense bases and the elements."]),
    ],
    terms=[
        ("khandha",
         "&ldquo;aggregate&rdquo; &mdash; this chapter's general term and "
         "organizing concept, reflecting that each category is a grouping of many "
         "instances."),
        ("rūpa",
         "form &mdash; the first aggregate, covering material and physical "
         "phenomena."),
        ("vedanā, saññā",
         "feeling and perception &mdash; the second and third aggregates."),
        ("saṅkhāra",
         "(mental) formations &mdash; the fourth and most heterogeneous "
         "aggregate, covering the mind's remaining volitional activity."),
        ("viññāṇa",
         "consciousness &mdash; the fifth aggregate, itself divided by the six "
         "sense doors it arises through."),
    ],
    quiz=[
        {"q": "What shift does Chapter 14 mark within the Visuddhimagga's overall structure?",
         "opts": [
             "From Parts I and II's practical training to Part III's analytical project",
             "A return to the practical training already covered in Part I",
             "The end of the entire work",
             "A repeat of Chapter 3's preview of meditation subjects"],
         "correct": 0,
         "expl": "Part III works by taking apart what ordinarily looks unified."},
        {"q": "What five categories does this chapter analyze?",
         "opts": [
             "Form, feeling, perception, formations, and consciousness",
             "Virtue, concentration, understanding, liberation, and knowledge",
             "The four elements and space",
             "The ten kasinas"],
         "correct": 0,
         "expl": "The traditional five aggregates, each treated in turn."},
        {"q": "What does the aggregate of form cover?",
         "opts": [
             "Material and physical phenomena",
             "Only thoughts and ideas",
             "Only pleasant sensations",
             "Only sounds and smells"],
         "correct": 0,
         "expl": "The first of the five aggregates the chapter treats."},
        {"q": "What does the aggregate of feeling cover?",
         "opts": [
             "The pleasant, unpleasant, or neutral quality of experience",
             "Physical strength and endurance",
             "Memory of past events specifically",
             "Visual perception exclusively"],
         "correct": 0,
         "expl": "Distinct from perception, which is treated as a separate, third aggregate."},
        {"q": "Why is the aggregate of formations (saṅkhāra) described as especially heterogeneous?",
         "opts": [
             "It is a broad category covering the mind's remaining volitional and constructing activity beyond feeling and perception",
             "It contains only a single, simple mental factor",
             "It refers only to physical formations like rock and clay",
             "It is identical in content to the aggregate of consciousness"],
         "correct": 0,
         "expl": "Everything mental not already classed as feeling or perception falls here."},
        {"q": "How is the aggregate of consciousness further subdivided?",
         "opts": [
             "By which of the six sense doors it arises through",
             "By the practitioner's age at the time it arises",
             "By whether it occurs during the day or at night",
             "It cannot be subdivided at all"],
         "correct": 0,
         "expl": "Eye-, ear-, nose-, tongue-, body-, and mind-consciousness."},
        {"q": "Why does the chapter use the term &lsquo;aggregate&rsquo; (khandha) for each of the five categories?",
         "opts": [
             "Because each is itself a grouping of many instances, not a single thing",
             "Because the term simply means &lsquo;important&rsquo; in Pali",
             "Because there are exactly five physical objects each aggregate refers to",
             "Because the term was invented specifically for this chapter and used nowhere else"],
         "correct": 0,
         "expl": "Form alone, for instance, covers many distinct material phenomena bundled under one heading."},
        {"q": "What elevenfold classification does the chapter apply to each of the five aggregates?",
         "opts": [
             "Past/future/present, internal/external, gross/subtle, inferior/superior, far/near",
             "A ranking from most to least important",
             "A count of how many times each aggregate is mentioned in the canon",
             "A geographic classification by region"],
         "correct": 0,
         "expl": "Producing a systematic cross-section of each aggregate rather than one flat definition."},
        {"q": "What is the chapter's underlying point about the conventional sense of a unified &lsquo;self&rsquo;?",
         "opts": [
             "It resolves into five distinct, constantly varying categories, none fixed or unified on its own",
             "It is confirmed and reinforced by this analysis",
             "It exists independently of all five aggregates",
             "The chapter reaches no conclusion on this question"],
         "correct": 0,
         "expl": "The analytical move this chapter opens Part III with."},
        {"q": "Where can a reader go for Chapter 14's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("A different kind of chapter", [
            "Part III begins &mdash;",
            "understanding, not concentration",
        ]),
        ("Five aggregates", [
            "form, feeling, perception,",
            "formations, consciousness",
        ]),
        ("An elevenfold cross-section", [
            "past/future/present, internal/external,",
            "gross/subtle, inferior/superior, far/near",
        ]),
        ("No fixed self", [
            "five varying categories,",
            "none of them unified",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/samyutta-nikaya/sn-22.59.html">SN 22.59 &mdash; The '
        "Characteristic of Not-Self</a> &mdash; the foundational discourse "
        "analyzing the five aggregates this chapter treats in systematic detail.",
        '<a href="../discourses/samyutta-nikaya/sn-22.1.html">SN 22.1 &mdash; '
        "Nakula's Father</a> &mdash; a further discourse from the same collection "
        "devoted to the five aggregates.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 15 -- Āyatanadhātuniddesa
# --------------------------------------------------------------------------- #
page(
    15, "Āyatanadhātuniddesa", "The Bases and Elements",
    part=PART_3,
    meta_title="Visuddhimagga Ch. 15 — The Bases and Elements | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 15 of the Visuddhimagga (The Path of "
        "Purification) — the twelve sense bases, the eighteen elements, why the "
        "text offers more than one analytical scheme, and how each dissolves the "
        "sense of a unified self differently. No translated text reproduced; links "
        "to the full free translation and the Pali original. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter continues Chapter 14's "
                    "analytical project with two further classification schemes"),
        ("Speaker", "Buddhaghosa, continuing the systematic survey that opened "
                    "Part III"),
        ("Form", "Two schemes treated in one chapter, each analyzed with the same "
                 "systematic detail Chapter 14 gave the five aggregates"),
        ("Length", "substantial, covering two distinct twelve- and eighteen-part "
                   "schemes in turn"),
        ("Northern parallel", "Alternate analytical grids alongside the aggregates "
                              "are widely used across Buddhist abhidharma "
                              "literature; this guide does not assert a specific "
                              "matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; conceptually "
                       "continuous with Chapter 14, though the eighteen-element "
                       "scheme in particular takes some care to hold in mind"),
    ],
    why=(
        "Chapter 14 analyzed a person into five aggregates. Chapter 15 is not a "
        "correction or an expansion of that analysis but a deliberate change of "
        "angle: the twelve sense bases and the eighteen elements describe the same "
        "conditioned reality the aggregates already covered, sorted differently. "
        "The text's own justification for offering more than one scheme is "
        "practical &mdash; different practitioners' particular flavor of self-view "
        "is said to loosen more readily under one classification than another."),
    guide=[
        ("Why more than one scheme", [
            "Rather than treating the aggregates, bases, and elements as competing "
            "theories, the chapter presents them as complementary tools: a given "
            "person's habitual sense of self may respond better to being examined "
            "through one classification than through the others, so the "
            "Visuddhimagga offers all three rather than settling on a single "
            "preferred version."]),
        ("Twelve sense bases", [
            "The first scheme divides into six internal bases &mdash; the sense "
            "faculties of eye, ear, nose, tongue, body, and mind &mdash; and six "
            "external bases, their corresponding objects: visible form, sound, "
            "odor, flavor, tangible object, and mental object. Together these "
            "twelve account for how experience arises at all, faculty meeting "
            "object."]),
        ("Eighteen elements", [
            "The second scheme is more granular still: the same twelve bases, plus "
            "the six kinds of consciousness that arise from each faculty-object "
            "pairing &mdash; eye-consciousness through mind-consciousness &mdash; "
            "bringing the total to eighteen distinct components."]),
        ("A shared purpose", [
            "Like Chapter 14's aggregates, both of these schemes are aimed at "
            "dissolving an unexamined sense of a single, compact self into a set "
            "of impersonal, conditioned components. The eighteen-element scheme "
            "makes this especially explicit: a single moment of experience, on "
            "this analysis, depends on three things meeting &mdash; a sense "
            "faculty, its object, and the corresponding consciousness &mdash; "
            "rather than resting on any one unified experiencer."]),
        ("How the schemes overlap", [
            "None of this introduces genuinely new territory beyond what Chapter "
            "14 already covered; the same underlying phenomena simply reappear "
            "sorted along different lines. The value of adding these two schemes "
            "lies in the different angle each offers on the same conditioned "
            "reality, not in any new content."]),
        ("What follows", [
            "Chapter 16 continues with two more classification schemes: the "
            "twenty-two faculties, and the four noble truths."]),
    ],
    terms=[
        ("āyatana",
         "&ldquo;sense base&rdquo; &mdash; this chapter's first scheme, twelve in "
         "total."),
        ("ajjhattikāyatana, bāhirāyatana",
         "internal bases and external bases &mdash; the six sense faculties and "
         "their six corresponding objects, the two halves of the twelvefold "
         "scheme."),
        ("dhātu",
         "&ldquo;element&rdquo; &mdash; this chapter's second scheme, eighteen in "
         "total: the twelve bases plus six kinds of consciousness."),
        ("cakkhuviññāṇa",
         "eye-consciousness &mdash; a representative example of the six "
         "consciousness-elements the eighteenfold scheme adds to the twelve "
         "bases."),
        ("dhammāyatana",
         "the mental-object base &mdash; the sixth external base, covering mental "
         "objects generally."),
    ],
    quiz=[
        {"q": "What two classification schemes does Chapter 15 cover?",
         "opts": [
             "The twelve sense bases and the eighteen elements",
             "The five aggregates and the four noble truths",
             "The ten kasinas and the ten kinds of foulness",
             "The four divine abidings and the four immaterial states"],
         "correct": 0,
         "expl": "Two further ways of analyzing the same conditioned reality Chapter 14 covered through the aggregates."},
        {"q": "Why does the text offer more than one scheme for analyzing a person?",
         "opts": [
             "Different practitioners' particular flavor of self-view is said to loosen more readily under one scheme than another",
             "Because the aggregates scheme from Chapter 14 was later found to be incorrect",
             "Because each scheme applies to a different physical location",
             "Because the number of schemes must always match the number of jhānas"],
         "correct": 0,
         "expl": "Presented as complementary tools rather than competing theories."},
        {"q": "What are the six internal sense bases?",
         "opts": [
             "The sense faculties: eye, ear, nose, tongue, body, and mind",
             "The four elements plus space and consciousness",
             "The five aggregates plus consciousness",
             "The six recollections from Chapter 7"],
         "correct": 0,
         "expl": "Paired with six external bases, their corresponding objects."},
        {"q": "What are the six external sense bases?",
         "opts": [
             "Visible form, sound, odor, flavor, tangible object, and mental object",
             "The six directions: north, south, east, west, up, and down",
             "Six named meditation teachers",
             "Six types of monastic robes"],
         "correct": 0,
         "expl": "Each corresponding to one of the six internal, faculty-side bases."},
        {"q": "How many elements does the eighteenfold scheme total, and what does it add to the twelve bases?",
         "opts": [
             "Eighteen; it adds the six kinds of consciousness arising from each faculty-object pairing",
             "Twenty-four; it adds six new sense faculties not covered by the bases",
             "Twelve; it is identical to the bases scheme with a different name",
             "Forty; it merges the bases scheme with the forty meditation subjects"],
         "correct": 0,
         "expl": "Eye-consciousness through mind-consciousness, added to the twelve bases already covered."},
        {"q": "What does the eighteen-element scheme highlight about a single moment of experience?",
         "opts": [
             "It depends on three things meeting: a sense faculty, its object, and the corresponding consciousness",
             "It depends entirely on a single, unified experiencer",
             "It cannot be analyzed or broken down in any way",
             "It occurs identically regardless of which sense faculty is involved"],
         "correct": 0,
         "expl": "Rather than resting on any one unified experiencer."},
        {"q": "What shared purpose do the bases and elements schemes serve, alongside Chapter 14's aggregates?",
         "opts": [
             "Dissolving an unexamined sense of a single, compact self into impersonal, conditioned components",
             "Establishing a fixed, permanent identity for each practitioner",
             "Ranking practitioners by their level of spiritual attainment",
             "Providing a calendar for monastic ceremonies"],
         "correct": 0,
         "expl": "The same underlying aim carried through three different classification schemes."},
        {"q": "How do the bases and elements schemes relate to the aggregates scheme in terms of content?",
         "opts": [
             "They cut across the same underlying phenomena from different angles, rather than adding genuinely new content",
             "They describe an entirely separate set of phenomena with no overlap at all",
             "They replace and supersede the aggregates scheme entirely",
             "They apply only to advanced practitioners who have already reached full awakening"],
         "correct": 0,
         "expl": "The value lies in the different angle each offers, not in new material."},
        {"q": "What does Chapter 16 turn to next?",
         "opts": [
             "The twenty-two faculties and the four noble truths",
             "The ten kasinas, revisited in more detail",
             "The thirteen ascetic practices",
             "The supernormal powers"],
         "correct": 0,
         "expl": "Two more classification schemes continuing Part III's analytical project."},
        {"q": "Where can a reader go for Chapter 15's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Same territory, different cuts", [
            "aggregates, bases, elements &mdash;",
            "three complementary schemes",
        ]),
        ("Twelve sense bases", [
            "six faculties,",
            "six objects",
        ]),
        ("Eighteen elements", [
            "bases plus six kinds",
            "of consciousness",
        ]),
        ("No single experiencer", [
            "a moment of experience needs",
            "three things meeting",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/samyutta-nikaya/sn-35.28.html">SN 35.28 &mdash; '
        "Burning</a> &mdash; popularly known as &ldquo;The Fire Sermon,&rdquo; on "
        "the six sense faculties and their objects, the core of this chapter's "
        "twelve bases.",
        '<a href="../discourses/majjhima-nikaya/mn-018.html">MN 18 &mdash; The '
        "Honey-Cake</a> &mdash; traces the chain from eye, form, and "
        "eye-consciousness through to contact, illustrating the eighteen-element "
        "scheme in action.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 16 -- Indriyasaccaniddesa
# --------------------------------------------------------------------------- #
page(
    16, "Indriyasaccaniddesa", "The Faculties and Truths",
    part=PART_3,
    meta_title="Visuddhimagga Ch. 16 — The Faculties and Truths | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 16 of the Visuddhimagga (The Path of "
        "Purification) — the twenty-two governing faculties and the four noble "
        "truths, the doctrinal center the rest of Part III unpacks into direct "
        "experiential realization. No translated text reproduced; links to the "
        "full free translation and the Pali original. From Ru-Yi Meditation "
        "Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter adds a differently oriented "
                    "scheme before turning to the doctrinal center of the whole "
                    "training"),
        ("Speaker", "Buddhaghosa, continuing Part III's analytical survey"),
        ("Form", "Two schemes: twenty-two governing faculties, then the four noble "
                 "truths, each of the latter analyzed with Chapter 1's fourfold "
                 "grid"),
        ("Length", "substantial, given twenty-two individual faculties plus "
                   "systematic treatment of each of the four truths"),
        ("Northern parallel", "The four truths appear as a shared framework across "
                              "virtually all Buddhist traditions; comparably broad "
                              "faculty schemes appear in other abhidharma systems; "
                              "this guide does not assert a specific matching "
                              "passage"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&#9734; &mdash; the faculties "
                       "list is long but enumerable; the four truths section "
                       "rewards careful, slower reading"),
    ],
    why=(
        "Chapters 14 and 15 analyzed experience through aggregates, bases, and "
        "elements &mdash; schemes that dissolve a sense of self by breaking apart "
        "what looks unified. Chapter 16 adds a differently oriented scheme, the "
        "twenty-two faculties, describing governing functions rather than static "
        "components, before turning to the four noble truths: the doctrinal center "
        "the whole training has been oriented toward from the start, and the "
        "framework the rest of Part III will spend its remaining chapters "
        "unpacking into ever greater experiential detail."),
    guide=[
        ("A different kind of scheme", [
            "Where the aggregates, bases, and elements describe components of "
            "experience, the twenty-two faculties (<em>indriya</em>, related to a "
            "root meaning something like &lsquo;ruling&rsquo; or "
            "&lsquo;predominance&rsquo;) describe governing or directive "
            "functions &mdash; each one exercising a specific kind of control "
            "within its own domain."]),
        ("Physical and personal faculties", [
            "The list opens with the six sense faculties already met as bases in "
            "Chapter 15, then adds three more governing basic physical and "
            "personal existence: femininity, masculinity, and the life "
            "(vitality) faculty."]),
        ("Feeling faculties", [
            "Five further faculties cover the varieties of feeling: bodily "
            "pleasure, bodily pain, mental joy, mental grief, and equanimity "
            "&mdash; mapping fairly closely onto Chapter 14's aggregate of "
            "feeling, but organized here by governing function rather than as a "
            "single aggregate."]),
        ("Spiritual faculties", [
            "Five faculties familiar from practice generally follow: faith, "
            "energy, mindfulness, concentration, and wisdom, each governing its "
            "own domain of development along the path."]),
        ("Three supramundane faculties", [
            "The final three faculties in the scheme track the progressive stages "
            "of awakening specifically: one present at the very moment of first "
            "realizing the path, one spanning from that realization's fruit "
            "through the higher stages, and one present only in a practitioner "
            "who has completed the training and has nothing further to realize."]),
        ("The four noble truths", [
            "The chapter then turns to what it treats as the doctrinal center of "
            "the entire training: suffering, its origin in craving, its "
            "cessation, and the path leading to that cessation &mdash; each "
            "analyzed with the same fourfold grid (characteristic, function, "
            "manifestation, proximate cause) Chapter 1 first introduced for "
            "virtue."]),
        ("Understanding versus realization", [
            "This chapter's treatment of the four truths is conceptual, laying "
            "doctrinal groundwork rather than describing the experience of "
            "realizing them directly. The chapters that follow take up that "
            "further task, turning this conceptual understanding into a "
            "step-by-step account of direct realization."]),
        ("What follows", [
            "Chapter 17 turns to dependent origination, the causal explanation "
            "behind the first two truths &mdash; suffering and its origin "
            "&mdash; that the remaining chapters build directly on."]),
    ],
    terms=[
        ("indriya",
         "&ldquo;faculty&rdquo; &mdash; this chapter's first scheme, twenty-two "
         "governing functions rather than static components."),
        ("itthindriya, purisindriya, jīvitindriya",
         "the femininity, masculinity, and life (vitality) faculties &mdash; three "
         "of the faculties governing basic physical and personal existence."),
        ("saddhindriya, viriyindriya, satindriya, samādhindriya, paññindriya",
         "the five spiritual faculties: faith, energy, mindfulness, "
         "concentration, and wisdom."),
        ("cattāri ariyasaccāni",
         "the four noble truths &mdash; this chapter's second and central scheme."),
        ("dukkha, samudaya, nirodha, magga",
         "suffering, origin, cessation, and path &mdash; the four truths "
         "individually named."),
    ],
    quiz=[
        {"q": "What two schemes does Chapter 16 cover?",
         "opts": [
             "The twenty-two faculties and the four noble truths",
             "The ten kasinas and the ten kinds of foulness",
             "The five aggregates and the eighteen elements",
             "The thirteen ascetic practices and the six recollections"],
         "correct": 0,
         "expl": "The latter treated as the doctrinal center the rest of Part III builds toward."},
        {"q": "How do the twenty-two faculties differ in character from the aggregates, bases, and elements of Chapters 14 and 15?",
         "opts": [
             "They describe governing or directive functions rather than static components",
             "They are identical in every respect to the aggregates scheme",
             "They apply only to fully awakened practitioners",
             "They describe purely physical objects with no mental component"],
         "correct": 0,
         "expl": "Each faculty exercises a specific kind of control within its own domain."},
        {"q": "Beyond the six sense faculties, which faculties govern basic physical and personal existence?",
         "opts": [
             "Femininity, masculinity, and the life (vitality) faculty",
             "Faith, energy, and mindfulness",
             "Bodily pleasure, bodily pain, and equanimity",
             "The three supramundane faculties"],
         "correct": 0,
         "expl": "Three faculties added to the six sense faculties already met in Chapter 15."},
        {"q": "What five faculties cover the varieties of feeling?",
         "opts": [
             "Bodily pleasure, bodily pain, mental joy, mental grief, and equanimity",
             "Faith, energy, mindfulness, concentration, and wisdom",
             "Eye, ear, nose, tongue, and body",
             "The four noble truths plus one"],
         "correct": 0,
         "expl": "Mapping fairly closely onto Chapter 14's aggregate of feeling, organized here by governing function."},
        {"q": "What five faculties are central to spiritual practice generally?",
         "opts": [
             "Faith, energy, mindfulness, concentration, and wisdom",
             "Femininity, masculinity, life, pleasure, and pain",
             "The four noble truths plus dependent origination",
             "Eye, ear, nose, tongue, and mind"],
         "correct": 0,
         "expl": "Each governing its own domain of development along the path."},
        {"q": "What do the final three faculties in the twenty-two-part scheme track?",
         "opts": [
             "The progressive stages of awakening, from first realization through full accomplishment",
             "The three trainings: virtue, concentration, and understanding",
             "Three different physical locations for meditation practice",
             "Three grades of monastic seniority"],
         "correct": 0,
         "expl": "One at first realization, one through the higher stages, one in a fully accomplished practitioner."},
        {"q": "What are the four noble truths?",
         "opts": [
             "Suffering, its origin, its cessation, and the path leading to cessation",
             "Virtue, concentration, understanding, and liberation",
             "The five aggregates, minus consciousness",
             "Faith, effort, mindfulness, and concentration"],
         "correct": 0,
         "expl": "Treated as the doctrinal center of the entire training."},
        {"q": "What analytical grid does the chapter apply to each of the four truths?",
         "opts": [
             "The same fourfold grid (characteristic, function, manifestation, proximate cause) from Chapter 1",
             "A grid unique to this chapter, never used elsewhere in the work",
             "No systematic grid at all; each truth is described only in a single sentence",
             "The elevenfold classification from Chapter 14"],
         "correct": 0,
         "expl": "The same method first applied to virtue, now applied to the four truths."},
        {"q": "How does this chapter's treatment of the four truths differ from what the following chapters do?",
         "opts": [
             "This chapter is conceptual groundwork; later chapters turn that understanding into direct realization",
             "This chapter is purely narrative, with no doctrinal content at all",
             "The following chapters simply repeat this chapter's content without change",
             "There is no difference; the four truths are never mentioned again"],
         "correct": 0,
         "expl": "A step-by-step account of direct realization is still to come."},
        {"q": "Where can a reader go for Chapter 16's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Governing functions", [
            "22 faculties &mdash;",
            "not static components",
        ]),
        ("Physical, feeling, spiritual", [
            "three groups of faculties,",
            "then three supramundane",
        ]),
        ("The doctrinal center", [
            "suffering, origin,",
            "cessation, path",
        ]),
        ("Understanding, then realization", [
            "conceptual groundwork here &mdash;",
            "direct realization still ahead",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/samyutta-nikaya/sn-56.11.html">SN 56.11 &mdash; '
        "Rolling Forth the Wheel of Dhamma</a> &mdash; the Buddha's first sermon, "
        "the canonical source for the four noble truths this chapter analyzes.",
        '<a href="../discourses/samyutta-nikaya/sn-56.31.html">SN 56.31 &mdash; In '
        "a Rosewood Forest</a> &mdash; a further discourse from the same "
        "collection on the four noble truths.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 17 -- Paccayākāraniddesa
# --------------------------------------------------------------------------- #
page(
    17, "Paccayākāraniddesa", "The Soil of Understanding",
    part=PART_3,
    meta_title="Visuddhimagga Ch. 17 — The Soil of Understanding | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 17 of the Visuddhimagga (The Path of "
        "Purification) — the twelve links of dependent origination, why the "
        "sequence has no fixed first cause, the middle way between eternalism and "
        "annihilationism, and why this chapter is called understanding's own soil. "
        "No translated text reproduced; links to the full free translation and the "
        "Pali original. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter supplies the causal "
                    "explanation Chapter 16 named only in outline"),
        ("Speaker", "Buddhaghosa, treating dependent origination as demanding "
                    "enough to warrant its own extensive chapter"),
        ("Form", "Twelve links worked through in causal sequence, followed by "
                 "several distinct ways of approaching the same structure and the "
                 "wrong views it rules out"),
        ("Length", "one of the longest and most demanding chapters in the whole "
                   "work; this guide covers its core structure rather than every "
                   "interpretive variant the chapter itself explores"),
        ("Northern parallel", "Dependent origination in some form is foundational "
                              "across virtually all Buddhist traditions; this guide "
                              "does not assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&starf;&starf; &mdash; the most "
                       "demanding chapter so far, both in content and in the "
                       "number of interpretive angles it offers"),
    ],
    why=(
        "Chapter 16 named the four noble truths as the doctrinal center of the "
        "path but described suffering and its origin only in outline. Chapter 17 "
        "supplies what those first two truths actually rest on: an explanation of "
        "how suffering arises and continues to arise, link by causal link, without "
        "requiring a fixed self behind the process at any point. Buddhaghosa's own "
        "structure treats this chapter as the soil understanding itself grows "
        "from &mdash; without seeing this causal account clearly, the "
        "classification schemes Chapters 14 through 16 already covered remain, in "
        "a sense, only sorted rather than truly understood."),
    guide=[
        ("Twelve links in causal sequence", [
            "The chapter works through twelve links, each conditioning the next: "
            "ignorance conditions formations; formations condition consciousness; "
            "consciousness conditions name-and-form; name-and-form conditions the "
            "six sense bases; the six sense bases condition contact; contact "
            "conditions feeling; feeling conditions craving; craving conditions "
            "clinging; clinging conditions becoming; becoming conditions birth; "
            "and birth conditions aging-and-death."]),
        ("No first cause, no fixed self", [
            "The chapter is explicit that this sequence is not a story with an "
            "absolute starting point &mdash; ignorance itself is not uncaused, "
            "but part of a closed causal circle rather than a first link in a "
            "straight line. The whole scheme is offered as an alternative to "
            "positing either a fixed, persisting self or a self simply "
            "annihilated at death: a middle way between those two extremes."]),
        ("Where the chain can be broken", [
            "While every link conditions the next, the chapter singles out where "
            "a practitioner has the most direct practical leverage over the "
            "sequence &mdash; typically the link between feeling and craving, "
            "since craving is where a largely automatic response can most "
            "plausibly be interrupted through mindfulness and understanding, even "
            "though the earlier links remain in effect for whatever has already "
            "arisen."]),
        ("Multiple ways of approaching the same structure", [
            "The chapter is notable for presenting the same twelve links through "
            "several distinct approaches &mdash; moving forward from ignorance, "
            "backward from aging-and-death, or focusing on particular subsets of "
            "links &mdash; reflecting different pedagogical needs rather than "
            "different underlying claims about how the sequence actually works."]),
        ("Why this is called the &lsquo;soil&rsquo; of understanding", [
            "Without this causal account, the earlier classification schemes "
            "&mdash; the aggregates, bases, elements, and faculties &mdash; remain "
            "descriptive rather than explanatory. Dependent origination is what "
            "makes clear how those components actually arise and interact, which "
            "the chapter treats as understanding's real ground rather than one "
            "topic among many."]),
        ("What follows", [
            "Chapters 18 through 22 turn from this conceptual account to a "
            "step-by-step description of the purifications that make dependent "
            "origination and the four truths directly, experientially clear, "
            "beginning with Chapter 18's purification of view."]),
    ],
    terms=[
        ("paṭiccasamuppāda",
         "dependent origination &mdash; this chapter's central subject, the "
         "twelve-link causal sequence explaining how suffering arises."),
        ("avijjā, saṅkhāra",
         "ignorance and formations &mdash; the first two of the twelve links."),
        ("taṇhā, upādāna",
         "craving and clinging &mdash; the two links where the chapter says a "
         "practitioner has the most direct practical leverage."),
        ("sassatavāda, ucchedavāda",
         "eternalism and annihilationism &mdash; the two extreme views dependent "
         "origination is presented as a middle way between."),
        ("paññābhūmi",
         "&ldquo;soil of understanding&rdquo; &mdash; the traditional term for "
         "this chapter's place in the overall structure of Part III."),
    ],
    quiz=[
        {"q": "What does Chapter 17 supply that Chapter 16 named only in outline?",
         "opts": [
             "The causal explanation of how suffering actually arises",
             "A fifth noble truth not mentioned in Chapter 16",
             "A complete list of all forty meditation subjects again",
             "The biography of Buddhaghosa himself"],
         "correct": 0,
         "expl": "The mechanics behind the first two of the four noble truths."},
        {"q": "How many links make up dependent origination in this chapter?",
         "opts": [
             "Twelve",
             "Four",
             "Twenty-two",
             "Eighteen"],
         "correct": 0,
         "expl": "From ignorance through to aging-and-death, each conditioning the next."},
        {"q": "What are the first two links in the sequence?",
         "opts": [
             "Ignorance conditioning formations",
             "Craving conditioning clinging",
             "Birth conditioning aging-and-death",
             "Consciousness conditioning contact"],
         "correct": 0,
         "expl": "The opening pair of the twelve-link chain."},
        {"q": "What does the chapter say about whether the sequence has an absolute first cause?",
         "opts": [
             "No; it is a closed causal circle rather than a story with a genuine starting point",
             "Yes; ignorance is entirely uncaused and stands outside the sequence",
             "Yes; the six sense bases are the true first cause",
             "The chapter declines to address the question at all"],
         "correct": 0,
         "expl": "Ignorance itself is conditioned, not an absolute beginning."},
        {"q": "What two extreme views does dependent origination chart a middle way between?",
         "opts": [
             "Eternalism (a fixed self persists) and annihilationism (nothing continues at all)",
             "Optimism and pessimism",
             "Monastic life and lay life",
             "The kasinas and the immaterial states"],
         "correct": 0,
         "expl": "The whole scheme is offered as an alternative to both extremes."},
        {"q": "Where does the chapter say a practitioner has the most direct practical leverage over the chain?",
         "opts": [
             "The link between feeling and craving",
             "The link between ignorance and formations",
             "The link between birth and aging-and-death",
             "Nowhere; the chapter says the chain cannot be interrupted at any point"],
         "correct": 0,
         "expl": "Craving is where a largely automatic response can most plausibly be interrupted through mindfulness and understanding."},
        {"q": "What is notable about how the chapter presents the twelve links?",
         "opts": [
             "It offers several distinct approaches (forward, backward, and by subsets) reflecting different pedagogical needs",
             "It presents the links in only one fixed order with no variation ever discussed",
             "It presents the links purely as a poem with no analytical content",
             "It omits several of the twelve links entirely"],
         "correct": 0,
         "expl": "Different approaches to the same underlying structure, not different underlying claims."},
        {"q": "Why is this chapter traditionally called the &lsquo;soil&rsquo; of understanding?",
         "opts": [
             "Without it, the earlier classification schemes remain descriptive rather than explanatory",
             "Because it was written while Buddhaghosa was gardening",
             "Because it discusses literal agricultural soil at length",
             "Because it is the shortest chapter in the entire work"],
         "correct": 0,
         "expl": "Dependent origination explains how the aggregates, bases, elements, and faculties actually arise and interact."},
        {"q": "What do Chapters 18 through 22 do next?",
         "opts": [
             "Turn from this conceptual account to a step-by-step description of the purifications making it directly experientially clear",
             "Return to the forty meditation subjects for further practice",
             "Repeat this chapter's content without any further development",
             "Begin an entirely new, unrelated topic with no connection to Chapter 17"],
         "correct": 0,
         "expl": "Beginning with Chapter 18's purification of view."},
        {"q": "Where can a reader go for Chapter 17's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Twelve links", [
            "ignorance to aging-and-death,",
            "each conditioning the next",
        ]),
        ("No first cause", [
            "a closed causal circle,",
            "not a starting story",
        ]),
        ("A middle way", [
            "between eternalism",
            "and annihilationism",
        ]),
        ("The soil of understanding", [
            "explaining what Chapters 14&ndash;16",
            "only classified",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/samyutta-nikaya/sn-12.1.html">SN 12.1 &mdash; '
        "Dependent Origination</a> &mdash; the canonical source discourse for the "
        "twelve-link sequence this chapter analyzes.",
        '<a href="../discourses/digha-nikaya/dn-15.html">DN 15 &mdash; The Great '
        "Discourse on Causation</a> &mdash; the canon's most extended single "
        "treatment of dependent origination.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 18 -- Diṭṭhivisuddhiniddesa
# --------------------------------------------------------------------------- #
page(
    18, "Diṭṭhivisuddhiniddesa", "Purification of View",
    part=PART_3,
    meta_title="Visuddhimagga Ch. 18 — Purification of View | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 18 of the Visuddhimagga (The Path of "
        "Purification) — distinguishing mentality from materiality directly, their "
        "mutual dependence, and why seeing this leaves no separate self standing "
        "apart from the process. No translated text reproduced; links to the full "
        "free translation and the Pali original. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter opens the third of seven "
                    "traditional purifications, and the first Part III covers"),
        ("Speaker", "Buddhaghosa, turning the doctrinal material of Chapters "
                    "14&ndash;17 into a direct, experiential exercise"),
        ("Form", "A focused exercise in distinguishing two categories directly in "
                 "one's own experience, rather than a further expansion of "
                 "classification schemes"),
        ("Length", "moderate, considerably shorter than Chapter 17's extended "
                   "treatment of dependent origination"),
        ("Northern parallel", "Mind-body analyses supporting a not-self conclusion "
                              "appear widely across Buddhist traditions; this guide "
                              "does not assert a specific matching passage"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; conceptually "
                       "continuous with the previous four chapters, though the "
                       "shift from description to direct seeing takes some care to "
                       "track"),
    ],
    why=(
        "Chapters 14 through 17 laid out doctrinal material &mdash; the "
        "aggregates, bases, elements, faculties, truths, and dependent origination "
        "&mdash; largely as concepts to be understood. Chapter 18 opens the "
        "work's third purification, following purification of virtue in Part I "
        "and purification of mind in Part II: purification of view, where a "
        "practitioner turns that conceptual material into a direct, immediate "
        "seeing of mentality and materiality as they actually operate, rather than "
        "as topics merely described."),
    guide=[
        ("The third of seven purifications", [
            "The whole work's title reflects a sevenfold scheme of purification: "
            "virtue in Part I, mind in Part II, and five further purifications "
            "Part III works through in sequence. Purification of view is the "
            "first of these five, and the first purification belonging properly "
            "to the section on understanding."]),
        ("Distinguishing mentality from materiality", [
            "The chapter's core method is direct discernment: seeing mental "
            "phenomena &mdash; feeling, perception, formations, and consciousness "
            "&mdash; as distinct in kind from material phenomena, the body and "
            "its processes, where ordinary experience blends the two together "
            "without examination."]),
        ("Two bundles of reeds", [
            "The chapter draws on a canonical image for how mentality and "
            "materiality relate: two bundles of reeds propped against each "
            "other, neither able to stand on its own. The image illustrates "
            "mutual dependence rather than either category being the more "
            "fundamental, self-sufficient reality."]),
        ("No self standing apart", [
            "The point this distinguishing exercise builds toward is direct: once "
            "mentality and materiality are seen clearly as a mutually dependent "
            "process, no further person, self, or agent is found standing apart "
            "from or behind that process &mdash; the process itself is what fully "
            "accounts for what is conventionally called a &lsquo;being&rsquo;."]),
        ("Purification, not mere information", [
            "The chapter distinguishes hearing and intellectually accepting these "
            "points from actually seeing them directly in one's own ongoing "
            "experience, moment to moment. Only the latter is what makes this "
            "stage a genuine purification, rather than simply new information "
            "layered on top of an unchanged sense of self."]),
        ("What follows", [
            "Chapter 19 turns to the next purification, overcoming doubt, by "
            "tracing mentality-materiality back through its causes &mdash; tying "
            "this chapter's work directly to the dependent origination Chapter 17 "
            "already covered."]),
    ],
    terms=[
        ("diṭṭhivisuddhi",
         "purification of view &mdash; this chapter's subject, the third of the "
         "seven traditional purifications."),
        ("nāma, rūpa",
         "mentality and materiality &mdash; the two categories this chapter has a "
         "practitioner distinguish directly."),
        ("nāmarūpapariccheda-ñāṇa",
         "the knowledge of defining mentality-and-materiality &mdash; the "
         "technical name for the insight this chapter's exercise produces."),
        ("sakkāyadiṭṭhi",
         "personality view, or self-view &mdash; the mistaken view this "
         "purification directly counters."),
        ("visuddhi",
         "&ldquo;purification&rdquo; &mdash; the general term for the sevenfold "
         "scheme this and the next four chapters continue."),
    ],
    quiz=[
        {"q": "What purification does Chapter 18 open, and where does it fall in the sevenfold scheme?",
         "opts": [
             "Purification of view, the third, following purification of virtue and purification of mind",
             "Purification of virtue, the first",
             "Purification of mind, the second",
             "The seventh and final purification"],
         "correct": 0,
         "expl": "The first of five purifications belonging to Part III specifically."},
        {"q": "What two categories does this chapter have a practitioner distinguish directly?",
         "opts": [
             "Mentality (nāma) and materiality (rūpa)",
             "Virtue and concentration",
             "The four noble truths and the twelve links",
             "The five aggregates and the four elements only"],
         "correct": 0,
         "expl": "Distinguished directly in experience, rather than described conceptually as in earlier chapters."},
        {"q": "What canonical image does the chapter use to describe how mentality and materiality relate?",
         "opts": [
             "Two bundles of reeds propped against each other",
             "A single unbreakable stone pillar",
             "A river flowing in only one direction",
             "A locked door with no key"],
         "correct": 0,
         "expl": "Illustrating that neither can stand without the other."},
        {"q": "What does the reeds image illustrate about mentality and materiality?",
         "opts": [
             "Their mutual dependence, with neither being more fundamental or self-sufficient",
             "That materiality alone is fundamentally real",
             "That mentality alone is fundamentally real",
             "That the two have no relationship to each other at all"],
         "correct": 0,
         "expl": "Neither category stands on its own without the other."},
        {"q": "What conclusion does this distinguishing exercise build toward?",
         "opts": [
             "No separate self or agent is found standing apart from the mentality-materiality process",
             "A separate, permanent self is confirmed to exist behind the process",
             "Mentality and materiality are proven to be identical",
             "The exercise reaches no conclusion of any kind"],
         "correct": 0,
         "expl": "The process itself fully accounts for what is conventionally called a being."},
        {"q": "What technical name does the chapter give to the specific insight this exercise produces?",
         "opts": [
             "Nāmarūpapariccheda-ñāṇa, the knowledge of defining mentality-and-materiality",
             "Āsavakkhaya-ñāṇa, the knowledge of the destruction of the taints",
             "Iddhividha, supernormal power",
             "Cetopariyañāṇa, penetration of minds"],
         "correct": 0,
         "expl": "The specific insight-knowledge this purification is named for."},
        {"q": "What mistaken view does this purification directly counter?",
         "opts": [
             "Personality view, or self-view (sakkāyadiṭṭhi)",
             "Wrong livelihood",
             "Disbelief in the law of kamma specifically",
             "Doubt about the existence of other realms"],
         "correct": 0,
         "expl": "Countered by seeing mentality and materiality clearly as a mutually dependent process."},
        {"q": "What distinguishes purification of view from merely accepting these facts intellectually?",
         "opts": [
             "Actually seeing them directly in one's own ongoing experience, not just as new information",
             "Memorizing the Pali terms without further practice",
             "Reading the chapter a second time",
             "There is no distinction; intellectual acceptance is sufficient on its own"],
         "correct": 0,
         "expl": "Only direct seeing makes this a genuine purification rather than added information."},
        {"q": "What does Chapter 19 do next?",
         "opts": [
             "Traces mentality-materiality back through its causes, tying this chapter's work to dependent origination",
             "Returns to the forty meditation subjects covered in Part II",
             "Repeats Chapter 18's content without further development",
             "Begins Part IV of the Visuddhimagga"],
         "correct": 0,
         "expl": "Purification by overcoming doubt, the next of the five purifications in Part III."},
        {"q": "Where can a reader go for Chapter 18's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Third of seven purifications", [
            "virtue, then mind,",
            "now view",
        ]),
        ("Mentality and materiality", [
            "distinguished directly,",
            "not just described",
        ]),
        ("Two bundles of reeds", [
            "mutual dependence,",
            "neither self-sufficient",
        ]),
        ("No self standing apart", [
            "the process itself",
            "accounts for the whole",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/samyutta-nikaya/sn-12.65.html">SN 12.65 &mdash; The '
        "City</a> &mdash; traces the mutual dependence of consciousness and "
        "name-and-form this chapter's reeds image also illustrates.",
        '<a href="../discourses/majjhima-nikaya/mn-009.html">MN 9 &mdash; Right '
        "View</a> &mdash; a systematic canonical treatment of the kind of correct "
        "seeing this purification aims at.",
    ],
)

# --------------------------------------------------------------------------- #
# Chapter 19 -- Kaṅkhāvitaraṇavisuddhiniddesa
# --------------------------------------------------------------------------- #
page(
    19, "Kaṅkhāvitaraṇavisuddhiniddesa", "Purification by Overcoming Doubt",
    part=PART_3,
    meta_title="Visuddhimagga Ch. 19 — Purification by Overcoming Doubt | Ru-Yi Meditation Center",
    meta_desc=(
        "An original reading guide to Chapter 19 of the Visuddhimagga (The Path of "
        "Purification) — tracing mentality-materiality back to its causes, the "
        "traditional sixteen kinds of doubt across past, present, and future, and "
        "the informal marker known as &lsquo;lesser stream-entry&rsquo;. No "
        "translated text reproduced; links to the full free translation and the "
        "Pali original. From Ru-Yi Meditation Center."),
    glance=[
        ("Setting", "No narrative setting; the chapter extends Chapter 18's "
                    "distinguishing exercise by tracing that same process back to "
                    "its causes"),
        ("Speaker", "Buddhaghosa, opening the fourth of the seven traditional "
                    "purifications"),
        ("Form", "A causal tracing exercise organized around resolving a "
                 "traditional set of doubts spanning three time periods"),
        ("Length", "moderate, continuous in scope with Chapter 18"),
        ("Northern parallel", "Comparable doubt-resolving analyses of causal "
                              "continuity appear elsewhere in Buddhist literature; "
                              "this guide does not assert a specific matching "
                              "passage"),
        ("Difficulty", "&starf;&starf;&starf;&#9734;&#9734; &mdash; builds directly "
                       "on Chapters 17 and 18, applying already-covered material "
                       "concretely rather than introducing much that is new"),
    ],
    why=(
        "Chapter 18 distinguished mentality from materiality directly, but left "
        "open a further question: where does this ever-changing process actually "
        "come from, and does explaining its continuity across time require "
        "anything like a fixed self, an external creator, or an uncaused "
        "beginning? Chapter 19 answers this by applying Chapter 17's dependent "
        "origination concretely to the practitioner's own mentality-materiality "
        "process, and in doing so resolves a traditional set of doubts about "
        "one's own existence across past, present, and future."),
    guide=[
        ("Tracing the causes directly", [
            "Having distinguished mentality and materiality in Chapter 18, this "
            "chapter has a practitioner trace that same process back to its "
            "conditions, confirming concretely, rather than only conceptually as "
            "in Chapter 17, that each part of the process arises from "
            "identifiable causes."]),
        ("Sixteen kinds of doubt", [
            "The chapter organizes the doubts it resolves around three time "
            "periods: doubts about one's existence in the past (did I exist "
            "before, and if so, what was I?), doubts about the future, and doubts "
            "about the present arising of the process itself &mdash; sixteen "
            "traditionally enumerated variations spread across these three "
            "periods."]),
        ("No creator, no uncaused arising", [
            "Resolving these doubts rules out two explanations the chapter treats "
            "as mistaken: that some external creator produces the process, or "
            "that it simply arises without cause at all. In their place, "
            "everything traces to identifiable, ordinary conditions, consistent "
            "with the dependent origination Chapter 17 already laid out."]),
        ("Discerning conditions", [
            "The chapter names the specific insight this work produces: seeing "
            "directly, not just conceptually, how each part of the "
            "mentality-materiality process is conditioned by what precedes it "
            "&mdash; a knowledge of discerning conditions distinct from, though "
            "built on, Chapter 18's distinguishing of mentality from "
            "materiality."]),
        ("&lsquo;Lesser stream-entry&rsquo;", [
            "The chapter notes that a practitioner who has reached this point, "
            "while not yet an actual stream-enterer, is traditionally described "
            "as having gained a kind of preliminary confidence and protection, "
            "informally called &lsquo;lesser stream-entry&rsquo; &mdash; real "
            "progress, though the formal attainment still lies ahead."]),
        ("What follows", [
            "Chapter 20 turns to the next purification: distinguishing what "
            "actually constitutes the path forward from what does not, since a "
            "range of experiences that can arise around this stage of practice "
            "are not themselves signs of further progress, however impressive "
            "they may seem."]),
    ],
    terms=[
        ("kaṅkhāvitaraṇavisuddhi",
         "purification by overcoming doubt &mdash; this chapter's subject, the "
         "fourth of the seven traditional purifications."),
        ("paccayapariggaha-ñāṇa",
         "the knowledge of discerning conditions &mdash; the specific insight "
         "this chapter's causal tracing produces."),
        ("addhā",
         "&ldquo;time period&rdquo; &mdash; past, present, and future, the three "
         "periods the traditional sixteen doubts are organized around."),
        ("cūḷasotāpanna",
         "&ldquo;lesser stream-enterer&rdquo; &mdash; the informal term for a "
         "practitioner who has reached this stage, short of the formal "
         "attainment."),
        ("paṭiccasamuppāda",
         "dependent origination &mdash; Chapter 17's causal scheme, applied here "
         "concretely to the practitioner's own mentality-materiality process."),
    ],
    quiz=[
        {"q": "What does Chapter 19 add to Chapter 18's distinguishing of mentality and materiality?",
         "opts": [
             "Tracing that same process back to its causes, applying dependent origination concretely",
             "A complete reversal of Chapter 18's conclusions",
             "An entirely new, unrelated classification scheme",
             "A return to the forty meditation subjects of Part II"],
         "correct": 0,
         "expl": "Confirming concretely, not just conceptually, that the process arises from identifiable causes."},
        {"q": "What three time periods are the traditional doubts this chapter resolves organized around?",
         "opts": [
             "Past, present, and future",
             "Morning, afternoon, and evening",
             "Youth, middle age, and old age",
             "Before ordination, during training, and after full awakening"],
         "correct": 0,
         "expl": "Doubts about one's existence spanning all three periods."},
        {"q": "How many kinds of doubt does the traditional scheme this chapter resolves enumerate?",
         "opts": [
             "Sixteen",
             "Four",
             "Forty",
             "Two"],
         "correct": 0,
         "expl": "Distributed across the three time periods."},
        {"q": "What two explanations does this chapter's work rule out?",
         "opts": [
             "An external creator producing the process, and the process arising without any cause at all",
             "Rebirth and kamma, both entirely",
             "Virtue and concentration as valid trainings",
             "The existence of the five aggregates"],
         "correct": 0,
         "expl": "Replaced by tracing everything to identifiable, ordinary conditions."},
        {"q": "What does the chapter conclude explains the mentality-materiality process's continuity instead?",
         "opts": [
             "Everything traces to identifiable, ordinary conditions, consistent with dependent origination",
             "A single unchanging self persists unchanged across all three time periods",
             "The question is declared permanently unanswerable",
             "Pure chance, with no discernible pattern at all"],
         "correct": 0,
         "expl": "Consistent with the causal scheme Chapter 17 already laid out."},
        {"q": "What specific insight-knowledge does this chapter's causal tracing produce?",
         "opts": [
             "Paccayapariggaha-ñāṇa, the knowledge of discerning conditions",
             "Nāmarūpapariccheda-ñāṇa, the knowledge of defining mentality-and-materiality",
             "Āsavakkhaya-ñāṇa, the knowledge of the destruction of the taints",
             "Iddhividha, supernormal power"],
         "correct": 0,
         "expl": "Distinct from, though built directly on, Chapter 18's distinguishing insight."},
        {"q": "What informal term describes a practitioner who has reached this stage?",
         "opts": [
             "&lsquo;Lesser stream-enterer&rsquo; (cūḷasotāpanna)",
             "A fully awakened arahant",
             "A stream-enterer in the full, formal sense",
             "A non-returner"],
         "correct": 0,
         "expl": "A marker of real progress, described in the chapter."},
        {"q": "Is &lsquo;lesser stream-entry&rsquo; the same as actual, formal stream-entry?",
         "opts": [
             "No; it is a preliminary marker of progress, not yet the formal attainment",
             "Yes, they are identical in every respect",
             "It is a higher attainment than formal stream-entry",
             "The chapter treats the two terms as complete synonyms"],
         "correct": 0,
         "expl": "Real progress, though the chapter is clear the formal attainment still lies ahead."},
        {"q": "What does Chapter 20 turn to next?",
         "opts": [
             "Distinguishing what actually constitutes the path forward from what does not",
             "A return to the ten kasinas for further practice",
             "The thirteen ascetic practices, revisited",
             "The end of the entire Visuddhimagga"],
         "correct": 0,
         "expl": "Since experiences that can arise at this stage are not all signs of genuine further progress."},
        {"q": "Where can a reader go for Chapter 19's full translated text?",
         "opts": [
             "The free PDF on Access to Insight, or the Pali original on SuttaCentral, both linked in this page's further reading",
             "Nowhere; the text is entirely unavailable to the public",
             "Only through a specific paid edition with no free alternative",
             "This page's own reading guide contains the full translated text"],
         "correct": 0,
         "expl": "As with every page in this series, since none reproduces the translation itself."},
    ],
    marginalia=[
        ("Fourth of seven purifications", [
            "tracing mentality-materiality",
            "back to its causes",
        ]),
        ("Sixteen kinds of doubt", [
            "organized across",
            "past, present, future",
        ]),
        ("No creator, no uncaused arising", [
            "everything traces to",
            "identifiable conditions",
        ]),
        ("Lesser stream-entry", [
            "real progress &mdash;",
            "not yet the formal attainment",
        ]),
    ],
    further=[
        PDF_LINK,
        SC_LINK,
        '<a href="../discourses/majjhima-nikaya/mn-002.html">MN 2 &mdash; All the '
        "Defilements</a> &mdash; the canonical source for the traditional sixteen "
        "kinds of doubt this chapter resolves.",
        '<a href="../discourses/samyutta-nikaya/sn-12.2.html">SN 12.2 &mdash; '
        "Analysis</a> &mdash; a detailed canonical breakdown of dependent "
        "origination's individual links, applied concretely in this chapter.",
    ],
)
