---
layout: default
title: "Awakening of Faith in the Mahāyāna — Translation Notes"
permalink: /sutras/dasheng-qixin-lun/translation-notes/
---

# Awakening of Faith in the Mahāyāna — Translation Notes

These notes record recurring translation decisions for the Ru-Yi English translation of the *Dasheng Qixin Lun* (大乘起信論, *Awakening of Faith in the Mahāyāna*), Taishō T1666, attributed to Aśvaghoṣa and translated into Chinese by Paramārtha (真諦) in 553. They exist so that vocabulary stays consistent across all ten parts, and so that this treatise's own tathāgatagarbha-line terminology — much of it without precedent anywhere else on this site — is recorded for any later tathāgatagarbha-line text (the *Laṅkāvatāra*, the *Ratnagotravibhāga*, and so on) to inherit rather than re-coin.

## The text, and why only one version

Two Chinese translations of this treatise survive in the Taishō canon: Paramārtha's (T1666, 553 CE) and Śikṣānanda's (T1667, early eighth century). This collection translates only T1666 — the version historically more widely read, the version Fazang's commentary is keyed to, and the version later tradition defaults to whenever "the Awakening of Faith" is invoked without further qualification. T1667 is not covered here; a comparative reading across both versions would be a separate project.

The base text runs to roughly 10,600 Chinese characters, not counting the front matter (title, author, translator credit), the later monk Zhikai's (智愷) prefatory essay, or the CBETA colophon and donation notice at the close. Two homage verses (歸命盡十方… / 為欲令眾生…) open the treatise proper and are part of the root text — not, as their position immediately after the front matter might suggest, more front matter themselves — and are translated in full as part of Part 1.

## Reading-note sourcing

Per this site's commentator-vetting convention, reading notes are grounded in a named commentator rather than presented as unattributed analysis. Every reading note in this collection is drawn from Fazang's (法藏, 643–712, third patriarch of the Huayan school) own commentary, the *Dasheng Qixin Lun Yiji* (大乘起信論義記, T1846) — a text running to roughly six times the length of the root treatise itself, structured as a ten-part scholastic preamble followed by continuous line-by-line exegesis across three fascicles. The preamble is not translated here; only the line-by-line exegesis supplies reading-note material, and it addresses the base text closely enough — with only rare, short exceptions — that no reading note in this collection needed to fall back to unattributed analysis.

## Structure

| Part | Base text covers | Chinese length |
|---|---|---|
| 1 | Homage verses; 因緣分 (causes and conditions); 立義分 (establishing the doctrine) | 644 characters |
| 2 | 解釋分・顯示正義 (i): the two gates; mind as suchness | 501 characters |
| 3 | 解釋分・顯示正義 (ii): the ālayavijñāna; original/actualized enlightenment; the four marks | 643 characters |
| 4 | 解釋分・顯示正義 (iii): four mirrors; non-enlightenment; three subtle/six coarse marks | 647 characters |
| 5 | 解釋分・顯示正義 (iv): five names of will; the discriminating consciousness; six defiled minds | 1,058 characters |
| 6 | 解釋分・顯示正義 (v): the four kinds of habituation | 1,341 characters |
| 7 | 解釋分・顯示正義 (vi): the tathāgatagarbha's qualities; the buddha-bodies | 1,085 characters |
| 8 | 解釋分・對治邪執 (countering wrong attachments) | 739 characters |
| 9 | 解釋分・分別發趣道相 (distinguishing the marks of the path) | 1,669 characters |
| 10 | 修行信心分 (cultivating the practice of faith); 勸修利益分 (exhortation to practice) | 2,400 characters |

Total: 10,727 characters, verified in full against the base text via a depth-counted extraction of every page's source column, diffed with `difflib.SequenceMatcher` — 100% coverage, no gaps.

"顯示正義," the first of the three sections within 解釋分, spans Parts 2 through 7 — by far the treatise's largest single section, at roughly 5,250 characters, more than the whole of Parts 8 through 10 combined. It is split at natural doctrinal breaks (the two gates; enlightenment; non-enlightenment; the mechanics of will and consciousness; habituation; the tathāgatagarbha's positive qualities) rather than at even intervals, per Luke's own instruction not to force it into a single page.

## Core terminology

Renderings are matched first to this site's existing Yogācāra pages (*Cheng Weishi Lun*, *Abhidharmasamuccaya*, *Illuminating the Sacred Teaching*, the *Hundred Dharmas* collection) wherever the same term already appears there; where this treatise's own tathāgatagarbha-line vocabulary has no site precedent, a rendering is coined fresh and recorded here.

| Chinese | English | Notes |
|---|---|---|
| 如來藏 | tathāgatagarbha | Left untransliterated as a loanword, matching this site's *Śūraṅgama-sūtra* and *Śūraṅgama-sūtra jiǎngyì* pages. |
| 阿梨耶識 | the ālayavijñāna | Paramārtha's own transliteration — distinct in spelling from 阿賴耶識, the form used elsewhere on this site (Xuánzàng's school's later standard) — but the identical consciousness; rendered identically in English both ways. |
| 真如 | suchness | Matches this site's existing Yogācāra pages. |
| 熏習 | habituation | Matches this site's existing Yogācāra pages (vāsanā). |
| 一心 | the One Mind | Capitalized as a proper technical term specific to this treatise's own doctrine — distinct from the unrelated meditation-context senses ("one-pointedness of mind," etc.) already in use elsewhere on this site. No prior site precedent for this specific sense. |
| 二門 | the two gates | 心真如門 "the gate of mind as suchness," 心生滅門 "the gate of mind as arising-and-ceasing." Coined fresh; no prior site precedent. |
| 本覺 | original enlightenment | Coined fresh for this collection. |
| 始覺 | actualized enlightenment | Coined fresh for this collection; considered and rejected "incipient enlightenment" (misleadingly suggests only a beginning stage, when the term covers the entire graduated path through to ultimate enlightenment). |
| 不覺 | non-enlightenment | Coined fresh for this collection. |
| 究竟覺 | ultimate enlightenment | The fourth and final of the four graduated stages of actualized enlightenment. |
| 三細 | the three subtle marks | Matches the precedent already set on this site's *Śūraṅgama-sūtra jiǎngyì* translation notes, which explicitly cites this treatise's own framework. 無明業相 "the karmic mark of ignorance," 能見相 "the mark of the perceiving subject," 境界相 "the mark of the perceived realm." |
| 六麁 | the six coarse marks | Matches the same *Śūraṅgama-sūtra jiǎngyì* precedent. 智相 "the mark of discernment," 相續相 "the mark of continuity," 執取相 "the mark of grasping," 計名字相 "the mark of conceptualizing names," 起業相 "the mark of initiating karma," 業繫苦相 "the mark of suffering bound by karma." |
| 體大 / 相大 / 用大 | the greatness of essence / attributes / function | Coined fresh for this collection; no prior site precedent for this specific triad (an unrelated generic sense of 體大 appears once elsewhere on the site, in the *Mahāyānasaṃgraha*, and is unconnected to this technical triad). |
| 意 | will | The five-named function (業識/轉識/現識/智識/相續識, "the karmic consciousness," "the perceiving-turned consciousness," "the manifesting consciousness," "the discerning consciousness," "the continuing consciousness") that this treatise's own architecture places between the ālayavijñāna and the discriminating consciousness — not equivalent to manas (末那識) as named in this site's other Yogācāra pages, since this treatise's five-name scheme predates or runs parallel to the fully articulated eight-consciousness system those other pages assume. Coined fresh for this collection. |
| 意識 | the discriminating consciousness | Also glossed by the treatise itself as 分別事識, "the consciousness that discriminates objects" — the coarse, self-and-object-grasping consciousness ordinary people mistake for a unified self. |
| 六染 | the six kinds of defiled mind | 執相應染, 不斷相應染, 分別智相應染, 現色不相應染, 能見心不相應染, 根本業不相應染 — mapped in Fazang's commentary directly onto the five names of will and the three subtle/six coarse marks; see Part 5's reading notes for the full cross-reference. |
| 煩惱礙 / 智礙 | the hindrance of affliction / the hindrance to knowledge | This treatise's own two-hindrances scheme, organized by which gives rise to which (the defiled mind is the hindrance of affliction; the ignorance producing it is the hindrance to knowledge) — explicitly *not* the more familiar self-grasping/dharma-grasping distinction found in mature Yogācāra sources; see Part 5's reading notes. |
| 應身 / 報身 | the transformation body / the reward body | The two buddha-bodies this treatise distinguishes, tied respectively to the discriminating consciousness (seen by ordinary people and the two vehicles) and the karmic consciousness (seen by bodhisattvas). Matches the general two-body vocabulary used elsewhere on this site's Yogācāra pages. |
| 信成就發心 / 解行發心 / 證發心 | the resolve of faith perfected / of understanding and practice / of realization | The three stages of a bodhisattva's resolve this treatise names in 分別發趣道相 (Part 9). |
| 止觀 | calming and contemplation | Śamatha and vipaśyanā, matched to the general rendering used across this site's meditation-manual pages (*Mohe Zhiguan*, *Xiao Zhiguan Jiangyi*). Counted as a single practice-gate in this treatise's own fivefold scheme, on Fazang's explicit grounds that the two must be cultivated jointly, never separately. |
| 摩訶衍 | Mahāyāna | Kept as the Sanskrit loanword, per standard site convention. |

## What Fazang's commentary structure contributes

Fazang's exegesis repeatedly ties the treatise's several overlapping classification schemes — the five names of will, the three subtle and six coarse marks, the six kinds of defiled mind, and the bodhisattva grounds at which each is left behind — back to one another explicitly, showing they describe a single underlying structure viewed from four different angles rather than four independent doctrines. The fullest single instance of this cross-referencing is laid out in Part 5's reading notes; shorter instances recur throughout Parts 3 through 7. Where Fazang's own commentary makes such a cross-reference, this collection's reading notes reproduce it rather than only summarizing the passage in isolation, since the cross-references are themselves some of the commentary's most valuable content for a reader trying to hold the whole treatise together.

## A note for future tathāgatagarbha-line texts

This collection is, per Luke's brief, the first tathāgatagarbha-line text on this site (the Yogācāra corpus having already been complete). Several renderings coined here — "the One Mind" and "the two gates," "original enlightenment" / "actualized enlightenment" / "non-enlightenment," "the greatness of essence / attributes / function" — have no prior site precedent and were decided specifically with an eye toward reuse if this site later takes up the *Laṅkāvatāra Sūtra*, the *Ratnagotravibhāga* (*Bao Xing Lun*, 寶性論), or other texts in the same doctrinal lineage. Future translators working on such texts should check this glossary before coining fresh renderings for the same terms.
