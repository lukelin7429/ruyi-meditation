---
layout: default
title: "Treatise on the Sūtra of the Ten Grounds — Translation Notes"
permalink: /sutras/dasabhumika-shastra/translation-notes/
---

# Treatise on the Sūtra of the Ten Grounds — Translation Notes

These notes record recurring translation decisions for the Ru-Yi English translation of the *Daśabhūmikasūtra-śāstra* (十地經論, *Treatise on the Sūtra of the Ten Grounds*), Taishō T1522, Vasubandhu's commentary on the "Ten Grounds" chapter of the Avataṃsaka Sūtra, translated into Chinese by Bodhiruci and collaborators in the Northern Wei. They exist so that vocabulary — ten ground-names, a recurring fourfold-fruit structure, and a great deal of enumerated Yogācāra and Abhidharma terminology — stays consistent across all fifty-two parts, and so that this treatise's own vocabulary is recorded for any later Huayan-line text on this site to inherit rather than re-coin.

## The text

The *Daśabhūmikasūtra-śāstra* is Vasubandhu's fascicle-by-fascicle commentary on the Daśabhūmika, the "Ten Grounds" chapter of the Avataṃsaka Sūtra (華嚴經, the tenth of the sūtra's own chapters in the sixty-fascicle recension, chapter twenty-two in the eighty-fascicle recension) — the sūtra passage that gave the Huayan school its later systematic account of the bodhisattva path's ten grounds. Bodhiruci's translation (T1522), completed with collaborators early in the sixth century under the Northern Wei, is the standard version and the only one this collection translates. The base text runs to twelve fascicles and roughly 109,094 Chinese characters, counting the treatise's own front matter, section headings, and fascicle-break markers along with the continuous prose of sūtra and commentary; the depth-counted extraction of every page's own source column that this collection's per-page verification relies on accounts for 107,650 of those characters; the remaining span is front matter and fascicle-division headers, which this project treats as part of the base text but does not reproduce as separate translated content on any single page.

The sūtra portion embedded within the treatise — spoken in the voice of Vajragarbha Bodhisattva, empowered by the Buddha to teach — and Vasubandhu's own commentary are translated together throughout, exactly as they appear interleaved in the base text, with the sūtra passages marked "Sūtra:" and the commentary marked "Commentary:" in every source and translation column.

## Reading-note sourcing

Per this site's commentator-vetting convention, reading notes are grounded in a named commentator rather than presented as unattributed analysis. This collection is the first on this site to draw on two successive named commentators rather than one throughout.

Parts 1 through 23 draw on Jingying Huiyuan's (淨影慧遠, 523–592) 十地經論義記 (X0753). Huiyuan's commentary survives only in part: his own manuscript physically ends partway through the Third Ground, Prabhākarī, breaking off just before the treatise's closing King-and-samādhi passage for that ground — his own colophon records the interruption plainly, "end of fascicle four" (十地義記卷第四末終), with a closing methodological note (自後諸地皆同此判，宜須記知, "every ground hereafter follows this same division; this should be carefully noted and remembered") that reads as knowingly written for a commentary its author expected not to finish. Part 23's own reading notes mark this handoff directly.

Parts 24 through 52 draw on Fazang's (法藏, 643–712, third patriarch of the Huayan school) 華嚴經探玄記 (T1733). Fazang's commentary is not keyed to this treatise directly — it is his own systematic exegesis of the full Avataṃsaka Sūtra, organized by his own sevenfold analytical framework (ten gates of general interpretation applied to each chapter) rather than running paragraph-by-paragraph alongside Vasubandhu's commentary the way Huiyuan's does. Where Fazang's exposition of the Daśabhūmika chapter addresses a passage this treatise also comments on, this collection's reading notes draw on that exposition; where the two texts' own organizing structures diverge, the notes say so rather than forcing an alignment neither author intended. The two commentators occasionally comment on the very same passage from genuinely different angles — Part 23's reading notes show Fazang's fourfold division of the Third Ground's closing fruit matching Huiyuan's own almost clause for clause, but assigning one of the ten qualities of patience a finer, more specific gloss than Huiyuan's own bundled reading — a case kept in the notes deliberately, since the disagreement is itself instructive.

## Structure

The treatise's twelve fascicles divide, by the sūtra's own account, into ten bodhisattva grounds (daśabhūmi), each named, each given its own closing etymology, and each — from the Second Ground onward — opened by a numbered set of "ten" qualities or minds that arouse entry into it. This collection's fifty-two parts map onto the twelve fascicles as follows:

| Ground | Fascicles | Parts |
|---|---|---|
| Ground 1 — Pramuditā, the Ground of Joy | 1–3 | 1–14 |
| Ground 2 — Vimalā, the Ground Free of Defilement | 4 | 15–19 |
| Ground 3 — Prabhākarī, the Luminous Ground | 5 | 20–23 |
| Ground 4 — Arciṣmatī, the Blazing Ground | 6 | 24–25 |
| Ground 5 — Sudurjayā, the Ground Difficult to Conquer | 7 | 26–28 |
| Ground 6 — Abhimukhī, the Ground of Direct Presence | 8 | 29–32 |
| Ground 7 — Dūraṅgamā, the Far-Reaching Ground | 9 | 33–35 |
| Ground 8 — Acalā, the Immovable Ground | 10 | 36–40 |
| Ground 9 — Sādhumatī, the Ground of Excellent Wisdom | 11 | 41–45 |
| Ground 10 — Dharmameghā, the Ground of the Dharma-Cloud | 12 | 46–52 |

Per-part detail, with the Chinese-character length of each page's own source column (root text and embedded commentary together, as extracted and verified via the depth-counted `extract_top_level_blocks` method in `scripts/verify_dasabhumika_page.py`):

| Part | Base text covers | Chinese length |
|---|---|---|
| 1 | Opening assembly; Vajragarbha's entry into samādhi; buddhas' empowerment in twenty clauses | 2,617 |
| 2 | Empowerment of speech, mind, body; the ten grounds named and briefly glossed | 2,976 |
| 3 | Vimuktacandra's first request; Vajragarbha's silence and first refusal | 2,165 |
| 4 | Second refusal; the assembly's joint request | 1,735 |
| 5 | The buddhas' light completes the request | 1,957 |
| 6 | Vajragarbha's eleven verses; the request finally complete | 2,632 |
| 7 | Arousal of the thought of enlightenment; entry into the First Ground | 1,833 |
| 8 | Why it is called the Ground of Joy: thirty clauses of joy | 1,639 |
| 9 | Abiding: faith, practice, dedication; the six perfections paired with defilement and antidote | 1,532 |
| 10 | The first five of the ten great vows | 1,855 |
| 11 | Vows six through ten | 2,114 |
| 12 | The ten inexhaustible clauses; three contemplations behind great compassion | 1,973 |
| 13 | The Great Renunciation; the fruit of gentle taming | 1,676 |
| 14 | The fruits of advancing forth, gathered retribution, vow and wisdom; First Ground complete | 2,230 |
| 15 | Ten straightforward minds; departure from killing through slander | 2,106 |
| 16 | The ten wholesome courses complete; gathering wholesome dharmas begins | 1,927 |
| 17 | The three vehicles from one practice; the ten unwholesome courses' full reckoning | 2,283 |
| 18 | Nine kinds of afflicted beings; the great flood | 2,195 |
| 19 | Final contemplations on suffering beings; threefold fruit; Second Ground complete | 1,799 |
| 20 | Ten kinds of profound mindfulness; world-weariness; a world without refuge | 2,065 |
| 21 | Seeking the Dharma; renouncing wealth; the eight absorptions | 2,752 |
| 22 | The four immeasurables; mastery of spiritual power | 2,271 |
| 23 | Non-arising of dharmas; the ten qualities of patience; Third Ground complete | 1,326 |
| 24 | Arciṣmatī begins: illumination-entry; the thirty-seven factors of enlightenment | 2,496 |
| 25 | Deeds never done; ripened practice; closing fruit; Fourth Ground complete | 2,363 |
| 26 | Sudurjayā begins: ten equal minds; the Four Noble Truths | 2,311 |
| 27 | The orphaned without refuge; twenty titles of mastery | 2,051 |
| 28 | Mastery of worldly treatises and crafts; closing fruit; Fifth Ground complete | 2,083 |
| 29 | Abhimukhī begins: ten equal dharmas; the mind-only declaration | 2,034 |
| 30 | The twelve links in full; the contemplation that guards against error | 1,808 |
| 31 | Ten modes of contemplation; the gate of liberation through emptiness | 2,319 |
| 32 | Emptiness-samādhis; closing fruit; Sixth Ground complete | 1,991 |
| 33 | Dūraṅgamā begins: ten surpassing practices; the buddhas' boundless state | 2,758 |
| 34 | Why the Seventh Ground alone is called excellent | 2,051 |
| 35 | Profound remoteness free of activity; closing fruit; Seventh Ground complete | 2,237 |
| 36 | Acalā begins: gathering skillful means; acquiescence to non-arising | 1,952 |
| 37 | The seven exhortations | 1,634 |
| 38 | Purifying buddha-lands: the three masteries; the ten bodies | 2,761 |
| 39 | Ten kinds of mastery; threefold great excellence; the ground's ten names | 1,736 |
| 40 | Entry into buddha-nature; closing fruit; Eighth Ground complete | 1,827 |
| 41 | Sādhumatī begins: the Dharma teacher's skillful means; the thickets begin | 2,163 |
| 42 | Thickets of faculties, latent tendencies, birth-destinies, habitual tendencies | 1,777 |
| 43 | The threefold grouping; the great Dharma teacher; the four unhindered wisdoms begin | 2,197 |
| 44 | Eight marks of the four unhindered wisdoms | 1,947 |
| 45 | Ten kinds of dhāraṇī; boundless eloquence; closing fruit; Ninth Ground complete | 1,971 |
| 46 | Dharmameghā begins: the Vimalā samādhi; the great jewel lotus-throne | 2,463 |
| 47 | The coronation: investiture by the buddhas' light; sevenfold greatness of wisdom | 1,896 |
| 48 | Explaining the name Dharma-Cloud: the ground's own threefold account | 2,131 |
| 49 | Spiritual power unsurpassed and surpassed: a world folded into a mote of dust | 1,239 |
| 50 | The assembly beholds the bodhisattva's spiritual power | 2,444 |
| 51 | The pond of practice; the ten great mountain-kings | 1,454 |
| 52 | The great ocean; the wish-fulfilling jewel; the treatise's own close | 1,898 |

Total across all fifty-two source columns: 107,650 characters — verified page by page via the depth-counted extraction method above, each page's own coverage additionally checked against the base text with `difflib.SequenceMatcher`.

## Core terminology

Renderings are matched first to this site's existing Yogācāra pages (*Cheng Weishi Lun*, the *Hundred Dharmas* collection, *Madhyāntavibhāga*) wherever the same term already appears there; the ten ground-names themselves are left as Sanskrit loanwords throughout, matched by their English glosses established from the treatise's own etymological passages (Parts 8, 19, 23, 25, 28, 32, 35, 39–40, 45, 48).

| Chinese | English | Notes |
|---|---|---|
| 十地 | the ten grounds (daśabhūmi) | The treatise's own subject; each ground is a bodhisattva's stage of realization, not merely a stage of practice. |
| 歡喜地 | Pramuditā, the Ground of Joy | First Ground. Named and glossed in thirty clauses of joy in Part 8. |
| 離垢地 | Vimalā, the Ground Free of Defilement | Second Ground. Named for freedom from the taint of broken precepts. |
| 明地 | Prabhākarī, the Luminous Ground | Third Ground. |
| 焰地 | Arciṣmatī, the Blazing Ground | Fourth Ground. Named through the simile of a wish-fulfilling jewel's light (Part 25). |
| 難勝地 | Sudurjayā, the Ground Difficult to Conquer | Fifth Ground. |
| 現前地 | Abhimukhī, the Ground of Direct Presence | Sixth Ground. Site of the "three realms are mind-only" declaration (Part 29). |
| 遠行地 | Dūraṅgamā, the Far-Reaching Ground | Seventh Ground. |
| 不動地 | Acalā, the Immovable Ground | Eighth Ground. Entered through the acquiescence to non-arising; roused from quiescence by the seven exhortations (Part 37). |
| 善慧地 | Sādhumatī, the Ground of Excellent Wisdom | Ninth Ground. Named for the four unhindered wisdoms. |
| 法雲地 | Dharmameghā, the Ground of the Dharma-Cloud | Tenth and final Ground. Named in three senses in Part 48. |
| 金剛藏 | Vajragarbha [Bodhisattva] | Literally "vajra-treasury" or "vajra-matrix" — the bodhisattva empowered by the buddhas of the ten directions to teach this Dharma-gate; the treatise's own principal speaker. |
| 解脫月 | Vimuktacandra [Bodhisattva] | The bodhisattva whose repeated requests, across Parts 3–6, open the treatise, and whose further questions punctuate several later grounds (e.g. Part 34's dialogue on the Seventh Ground). |
| 調柔果 | the fruit of gentle taming | One of the fourfold "fruit of comparative excellence" named in Part 13 — Huiyuan's own etymology: "refining faith and the rest is what is meant by 'gentle taming.'" Illustrated by gold refined again and again in fire. |
| 發趣果 | the fruit of advancing forth | The second of the fourfold fruit — the capacity, once a ground is fulfilled, to set out toward the next. |
| 攝報果 | the fruit of gathered retribution | The third of the fourfold fruit — the visible karmic result, most often a bodhisattva's rebirth as a specific kind of king (Jambudvīpa's king in the First Ground, a Wheel-Turning King in the Second, and so on). |
| 願智果 | the fruit of vow and wisdom | The fourth of the fourfold fruit — inner realization through the power of vow together with self-mastery in the wisdom of teaching. From the Second Ground onward, this fourfold fruit is regularly abbreviated to a recurring threefold pattern — gathered retribution, vow and wisdom, and a closing named simile explaining the ground's own etymology — dropping "advancing forth" as no longer needing separate restatement. |
| 無生法忍 | acquiescence to the non-arising of dharmas (anutpattika-dharma-kṣānti) | The realization by which a bodhisattva enters the Eighth Ground, Acalā (Part 36); analyzed by the commentary there into four distinct kinds of non-arising. |
| 四無礙智 | the four unhindered wisdoms | 法無礙 (of dharmas), 義無礙 (of meaning), 辭無礙 (of language), 樂說無礙 (of eloquence) — the four wisdoms whose exposition gives the Ninth Ground, Sādhumatī, its very name (Parts 43–44). |
| 陀羅尼 | dhāraṇī | Left untransliterated as a loanword throughout, matching standard site convention; ten distinct named dhāraṇīs are enumerated at the Ninth Ground's close (Part 45). |
| 稠林 | thicket | A dense, tangled proliferation of mental or karmic activity a bodhisattva must thoroughly know in order to teach — eleven named thickets (mind, afflictions, karma, faculties, latent tendencies, birth-destinies, habitual tendencies, and others) analyzed across Parts 41–43 as the Ninth Ground's most distinctive feature. |
| 十種平等深淨心 | the ten kinds of equal, pure mind | The recurring structure by which a bodhisattva is said to enter each ground from the Second onward — ten named minds or dharmas, particular to each ground, given at the very opening of that ground's own exposition (e.g. Part 26 for the Fifth Ground). |
| 三界虛妄，但是一心作 | "the three realms are illusory, being nothing but the making of one mind" | The treatise's single most historically consequential line (Part 29) — cited, per Fazang's own note, by every later treatise establishing the doctrine of Consciousness-Only. |
| 十二因緣 / 十二有支 | the twelve links of dependent origination | Traced from ignorance to aging-and-death, expounded at length across Parts 29–31 within the Sixth Ground, Abhimukhī. |
| 三聚 | the three groups | The correctly settled, the wrongly settled, and the undetermined groups of sentient beings — the final "thicket" analyzed in the Ninth Ground (Part 43), fivefold subdivided by the commentary. |
| 四無量心 | the four immeasurables | Loving-kindness, compassion, sympathetic joy, and equanimity, cultivated "vast, immeasurable, and free of enmity" in Part 22. |
| 四攝法 | the four means of attraction | Giving, kind speech, beneficial conduct, and cooperation — the bodhisattva's fourfold method of teaching and gathering sentient beings, named across several grounds (e.g. Part 28). |
| 三十七道品 | the thirty-seven factors of enlightenment | Enumerated in full at the opening of the Fourth Ground, Arciṣmatī (Part 24). |
| 波羅蜜 | pāramitā | Left untransliterated as "pāramitā" throughout, following standard site convention; the treatise pairs one pāramitā with special emphasis to each of the ten grounds. |
| 淨心 / 深心 | pure mind / deep mind | Matched to this site's existing Yogācāra usage; the "deep mind" in particular recurs as the specific object purified at several grounds' openings. |

## A note on this collection's dual-commentary structure

This is the first collection on this site to draw its reading notes from two different named commentators across a single work, rather than one commentator throughout. The Huiyuan-to-Fazang handoff at Part 23 is a fact about what survives, not an editorial choice — Huiyuan's own manuscript simply stops mid-treatise, in the middle of the Third Ground, and no later portion of his commentary on this text is known to survive. Readers moving from Part 23 into Part 24 will notice the shift in commentarial voice directly: Huiyuan comments paragraph by paragraph alongside Vasubandhu's own text, tracking its structure closely; Fazang comments as part of a vastly larger, independently organized exposition of the whole Avataṃsaka Sūtra, and this collection's reading notes draw on the portions of that larger work that speak to the passage at hand.
