#!/usr/bin/env python3
"""
Build the chanting book for the Buddha-Recitation Service (念佛法會儀軌).

Output:
  community/dharma-events/liturgy/index.html

Every chanted passage is rendered as Chinese characters with pinyin under each
character, followed by a plain-English rendering. The noon offering text is
read in Taiwanese, so it carries Chinese and English only.

Edit the content below, then re-run:
    python3 scripts/liturgy_build.py
Requires: pip install pypinyin
"""
import os, re, html
from pypinyin import pinyin, Style

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'community', 'dharma-events', 'liturgy', 'index.html')

PUNCT = '，。、；：？！「」『』（）《》〈〉…—　 '

# Liturgical readings that differ from everyday Mandarin. Longest match wins.
READINGS = {
    '南無': 'ná mó', '阿彌陀': 'ā mí tuó', '佛': 'fó', '舍': 'shè', '弗': 'fú', '稽首': 'qǐ shǒu', '薄伽梵': 'bó qié fàn',
    '苾芻': 'bì chú', '室羅伐': 'shì luó fá', '逝多': 'shì duō', '給孤獨': 'jǐ gū dú',
    '祇樹': 'qí shù', '藥叉': 'yào chā', '揵闥婆': 'qián tà pó', '阿蘇羅': 'ā sū luó',
    '阿修羅': 'ā xiū luó', '琰魔': 'yǎn mó', '泥犁': 'ní lí', '安隱': 'ān wěn',
    '重說': 'chóng shuō', '應、正': 'yìng x zhèng', '無為': 'wú wéi', '千子': 'qiān zǐ', '應知': 'yīng zhī',
    '應善': 'yīng shàn', '應至心': 'yīng zhì xīn', '為濟': 'wèi jì', '為諸': 'wèi zhū',
    '何者為三': 'hé zhě wéi sān', '調御': 'tiáo yù', '調順': 'tiáo shùn', '調伏': 'tiáo fú',
    '強力': 'qiáng lì', '非強力': 'fēi qiǎng lì', '少年': 'shào nián', '長存': 'cháng cún',
    '長喘': 'cháng chuǎn', '還漂': 'huán piāo', '還自纏': 'huán zì chán', '可厭': 'kě yàn',
    '惡業': 'è yè', '醜惡': 'chǒu è', '切身': 'qiè shēn', '他將': 'tā jiāng',
    '宿鳥': 'sù niǎo', '妙華': 'miào huā', '沈溺': 'chén nì', '乾': 'gān',
    '無過': 'wú guò', '不過': 'bú guò', '不越': 'bú yuè', '不被': 'bú bèi', '不見': 'bú jiàn',
    '不滅': 'bú miè', '不暫': 'bú zàn', '不稱意': 'bú chèn yì', '稱意': 'chèn yì',
    '不可愛': 'bù kě ài', '相纏縛': 'xiāng chán fù', '相救濟': 'xiāng jiù jì', '相守': 'xiāng shǒu',
    '相好': 'xiàng hǎo', '圍遶': 'wéi rào', '飜': 'fān', '慞惶': 'zhāng huáng',
    '羸': 'léi', '蠲': 'juān', '汲': 'jí', '行化': 'xíng huà', '當行': 'dāng xíng', '行入': 'xíng rù',
    '不行': 'bù xíng', '勤行': 'qín xíng', '處': 'chù', '覺': 'jué', '眾': 'zhòng',
    '說': 'shuō', '樂': 'lè', '了': 'liǎo', '著': 'zhuó', '藏': 'zàng', '度': 'dù',
    '轉輪王': 'zhuǎn lún wáng', '宛轉': 'wǎn zhuǎn', '紺': 'gàn', '咸': 'xián', '塗': 'tú',
    '迴向': 'huí xiàng', '四重恩': 'sì chóng ēn', '一報身': 'yí bào shēn', '一心': 'yì xīn',
    '一時': 'yì shí', '一代': 'yí dài', '一事': 'yí shì', '大悲': 'dà bēi', '菩薩': 'pú sà',
    '涅槃': 'niè pán', '繭': 'jiǎn', '傍': 'páng', '怨家': 'yuàn jiā', '糧食': 'liáng shí',
    '支節': 'zhī jié', '悉分離': 'xī fēn lí', '伺命': 'sì mìng', '盡': 'jìn', '鎮': 'zhèn',
    '并': 'bìng', '並': 'bìng', '歎': 'tàn', '漂': 'piāo', '吞': 'tūn', '晝': 'zhòu',
    '瑩': 'yíng', '資': 'zī', '華遍': 'huā biàn', '已': 'yǐ',
}
_KEYS = sorted(READINGS, key=len, reverse=True)


def auto_pinyin(text):
    """Return one pinyin syllable (or '') per character of text."""
    out = [None] * len(text)
    i = 0
    while i < len(text):
        for k in _KEYS:
            if text.startswith(k, i):
                for j, syl in enumerate(READINGS[k].split()):
                    out[i + j] = syl
                i += len(k)
                break
        else:
            i += 1
    base = pinyin(text, style=Style.TONE, errors=lambda x: [''] * len(x))
    flat = [p[0] for p in base]
    if len(flat) != len(text):  # pypinyin grouped something; fall back per char
        flat = [pinyin(c, style=Style.TONE, errors=lambda x: [''])[0][0] for c in text]
    return [('' if c in PUNCT else (out[n] or flat[n])) for n, c in enumerate(text)]


def cells(text, py=None):
    """HTML for a line: each character stacked over its pinyin."""
    py = py or auto_pinyin(text)
    parts = []
    for c, p in zip(text, py):
        if c in PUNCT:
            if c.strip() and parts:
                parts[-1][0] += c
            continue
        parts.append([c, p])
    return ''.join('<span><b>%s</b><i>%s</i></span>' % (html.escape(c), p) for c, p in parts)


def seg(lines, en, note=None, pin=True):
    """One passage: Chinese line(s) (+ pinyin) and its English rendering."""
    if isinstance(lines, str):
        lines = [lines]
    h = ['<div class="lt-seg">']
    for ln in lines:
        if pin:
            py = None
            if isinstance(ln, tuple):
                ln, py = ln
            h.append('<div class="lt-zh">%s</div>' % cells(ln, py))
        else:
            h.append('<div class="lt-zh lt-plain">%s</div>' % html.escape(ln))
    if note:
        h.append('<p class="lt-note">%s</p>' % note)
    if en:
        h.append('<p class="lt-en">%s</p>' % en)
    h.append('</div>')
    return '\n'.join(h)


# ---------------------------------------------------------------- 無常經
WUCHANG = [
 ('h', 'Opening verses · Homage to the Three Jewels'),
 (['稽首歸依無上士，常起弘誓大悲心，', '為濟有情生死流，令得涅槃安隱處。',
   '大捨防非忍無倦，一心方便正慧力，', '自利利他悉圓滿，故號調御天人師。'],
  'I bow and take refuge in the Unsurpassed One, who always rouses great vows and a heart of great compassion. To carry beings across the river of birth and death, he leads them to the safe ground of nirvana. Tireless in giving, in moral discipline, and in patience; single-minded, skillful, and truly wise — his own good and the good of others are both made complete. So he is called the Tamer, the Teacher of gods and humans.'),
 (['稽首歸依妙法藏，三四二五理圓明，', '七八能開四諦門，修者咸到無為岸。',
   '法雲法雨潤群生，能除熱惱蠲眾病，', '難化之徒使調順，隨機引導非強力。'],
  'I bow and take refuge in the treasury of the wonderful Dharma. Its three fours and two fives shine with complete clarity; its seven and its eight open the gate of the Four Noble Truths. (Together these are the thirty-seven factors of awakening.) All who practice it reach the far shore of the unconditioned. Like cloud and rain, the Dharma nourishes everything that lives, cooling the fever of affliction and curing every ill. Those who are hard to teach it gently tames, guiding each according to capacity and never by force.'),
 (['稽首歸依真聖眾，八輩上人能離染，', '金剛智杵破邪山，永斷無始相纏縛。',
   '始從鹿苑至雙林，隨佛一代弘真教，', '各稱本緣行化已，灰身滅智寂無生。'],
  'I bow and take refuge in the true noble Sangha — the eight kinds of noble ones who have left every stain behind. With the diamond pestle of wisdom they shatter the mountain of wrong views and cut forever the bonds that have held us since time without beginning. From the Deer Park to the twin sal trees they followed the Buddha, spreading the true teaching through his whole lifetime. Each one, having finished the work of teaching, laid body and mind to rest in the stillness of the unborn.'),
 (['稽首總敬三寶尊，是謂正因能普濟，', '生死迷愚鎮沈溺，咸令出離至菩提。'],
  'I bow in reverence to all Three Jewels together — the true cause by which everyone can be rescued. Beings lost in birth and death, long sunk in confusion: may they all be led out and reach awakening.'),

 ('h', 'Verses on impermanence'),
 (['生者皆歸死，容顏盡變衰，', '強力病所侵，無能免斯者。'],
  'All who are born return to death. Every fair face fades. Even the strong are overtaken by illness. No one escapes.'),
 (['假使妙高山，劫盡皆壞散，', '大海深無底，亦復皆枯竭，', '大地及日月，時至皆歸盡，', '未曾有一事，不被無常吞。'],
  'Even Mount Sumeru will crumble when the eon ends. The bottomless ocean will run dry. The earth, the sun, the moon — when the time comes, all are gone. There has never been a single thing that impermanence did not swallow.'),
 (['上至非想處，下至轉輪王，', '七寶鎮隨身，千子常圍遶，', '如其壽命盡，須臾不暫停，', '還漂死海中，隨緣受眾苦。'],
  'From the highest heaven, beyond all perception, down to the wheel-turning king — always with his seven treasures, encircled by a thousand sons — when the lifespan is used up, it does not pause for an instant. Back they drift into the sea of death, to meet whatever suffering their actions bring.'),
 (['循環三界內，猶如汲井輪，', '亦如蠶作繭，吐絲還自纏。'],
  'Round and round within the three realms we turn, like a wheel drawing water from a well; like a silkworm spinning its cocoon, wrapped in its own thread.'),
 (['無上諸世尊，獨覺聲聞眾，', '尚捨無常身，何況於凡夫。'],
  'Even the unsurpassed Buddhas, the solitary awakened ones, and the noble disciples gave up their impermanent bodies. How much more so we ordinary people!'),
 (['父母及妻子，兄弟并眷屬，', '目觀生死隔，云何不愁歎。'],
  'Father and mother, wife and children, brothers, sisters, all our kin — we watch death part us from them. How could we not grieve?'),
 (['是故勸諸人，諦聽真實法，', '共捨無常處，當行不死門。', '佛法如甘露，除熱得清涼，', '一心應善聽，能滅諸煩惱。'],
  'So I urge everyone: listen closely to the true Dharma. Together let us leave the place of impermanence and walk through the gate of the deathless. The Buddha’s teaching is like sweet dew: it cools the fever and brings relief. Listen with one mind — it can put out every affliction.'),

 ('h', 'The sutra'),
 ('如是我聞：一時薄伽梵在室羅伐城逝多林給孤獨園。爾時佛告諸苾芻：「有三種法，於諸世間是不可愛、是不光澤、是不可念、是不稱意。何者為三？謂老、病、死。',
  'Thus have I heard. At one time the Blessed One was staying at Śrāvastī, in Jeta’s Grove, Anāthapiṇḍada’s park. There the Buddha said to the monks: “There are three things in this world that no one loves, that have no luster, that no one wants to think about, and that please no one. What three? Old age, sickness, and death.'),
 ('汝諸苾芻，此老病死於諸世間實不可愛、實不光澤、實不可念、實不稱意。若老、病、死世間無者，如來、應、正等覺不出於世，為諸眾生說所證法及調伏事。',
  '“Monks, old age, sickness, and death are truly unloved, truly without luster, truly unwelcome in thought, and truly pleasing to no one. Yet if there were no aging, sickness, and death in the world, a Tathāgata — worthy and fully awakened — would not appear in the world to teach beings the truth he has realized and the way to train the mind.'),
 ('是故應知此老、病、死，於諸世間是不可愛、是不光澤、是不可念、是不稱意。由此三事，如來、應、正等覺出現於世，為諸眾生說所證法及調伏事。」',
  '“Know, then, that aging, sickness, and death are what no one in the world loves or welcomes. And it is exactly because of these three that a Buddha appears in the world and teaches the Dharma he has realized and the way to tame the mind.”'),
 (['爾時世尊重說頌曰：', '「外事莊彩咸歸壞，內身衰變亦同然，', '唯有勝法不滅亡，諸有智人應善察。'],
  'Then the World-Honored One said it again in verse: “Outer things, however finely adorned, all go to ruin; the body within decays in the same way. Only the supreme Dharma does not perish. The wise should look into this carefully.'),
 (['此老病死皆共嫌，形儀醜惡極可厭，', '少年容貌暫時住，不久咸悉見枯羸。', '假使壽命滿百年，終歸不免無常逼，', '老病死苦常隨逐，恒與眾生作無利。」'],
  '“Aging, sickness, and death — everyone dislikes them; their look is ugly and hard to bear. The face of youth stays only a moment; soon it is withered and thin. Even a life of a full hundred years cannot avoid the press of impermanence. The pains of aging, sickness, and death follow us always and never do beings any good.”'),
 ('爾時世尊說是經已，諸苾芻眾、天、龍、藥叉、揵闥婆、阿蘇羅等，皆大歡喜，信受奉行。',
  'When the World-Honored One had spoken this sutra, the monks, the gods, nāgas, yakṣas, gandharvas, asuras, and all the others rejoiced greatly, accepted it in faith, and put it into practice.'),

 ('h', 'Closing verses'),
 (['常求諸欲境，不行於善事，', '云何保形命，不見死來侵？', '命根氣欲盡，支節悉分離，', '眾苦與死俱，此時徒歎恨。'],
  'Always chasing after pleasures, never doing what is good — how will you protect this body and this life? Do you not see death coming? When the last breath is about to go and the joints come apart, pain arrives together with death. By then regret is useless.'),
 (['兩目俱飜上，死刀隨業下，', '意想並慞惶，無能相救濟。', '長喘連胸急，短氣喉中乾，', '死王催伺命，親屬徒相守。'],
  'The eyes roll upward; the blade of death falls according to our karma. The mind is in panic, and no one can save us. Long gasps tighten the chest; short breaths dry the throat. The lord of death hurries his messengers, while our relatives can only stand by and watch.'),
 (['諸識皆昏昧，行入險城中，', '親知咸棄捨，任彼繩牽去。', '將至琰魔王，隨業而受報，', '勝因生善道，惡業墮泥犁。'],
  'Consciousness grows dim and enters a perilous city. Family and friends all fall away, and one is led off on a rope. Brought before King Yama, each receives what their own actions have earned: good causes lead to a happy birth, harmful deeds to a fall into hell.'),
 (['明眼無過慧，黑闇不過癡，', '病不越怨家，大怖無過死。', '有生皆必死，造罪苦切身，', '當勤策三業，恒修於福智。'],
  'No eye is brighter than wisdom; no darkness is deeper than delusion. No enemy is worse than sickness; no terror is greater than death. All who are born must die, and wrongdoing brings pain that cuts close. So work diligently with body, speech, and mind, and keep cultivating merit and wisdom.'),
 (['眷屬皆捨去，財貨任他將，', '但持自善根，險道充糧食。'],
  'Relatives all leave us; wealth is carried off by others. We take with us only our own roots of goodness — provisions for the dangerous road.'),
 (['譬如路傍樹，暫息非久停，', '車馬及妻兒，不久皆如是。', '譬如群宿鳥，夜聚旦隨飛，', '死去別親知，乖離亦如是。'],
  'Like a tree by the roadside: we rest a moment and do not stay. Carriages, horses, spouse, and children are soon just like that. Like birds roosting together: gathered at night, flown apart at dawn. So death parts us from those we love.'),
 (['唯有佛菩提，是真歸仗處，', '依經我略說，智者善應思。'],
  'Only the Buddha’s awakening is a true place of refuge. I have said this briefly, following the sutras; let the wise reflect on it well.'),
 (['天阿蘇羅藥叉等，來聽法者應至心，', '擁護佛法使長存，各各勤行世尊教。', '諸有聽徒來至此，或在地上或居空，', '常於人世起慈心，晝夜自身依法住。'],
  'Gods, asuras, yakṣas, and all who have come to hear the Dharma: listen with a sincere heart. Protect the Buddha’s teaching so that it may long endure, and each of you diligently practice what the World-Honored One taught. All listeners gathered here, on the ground or in the air: always hold kindness toward the human world, and day and night abide in the Dharma yourselves.'),
 (['願諸世界常安隱，無邊福智益群生，', '所有罪業並消除，遠離眾苦歸圓寂。', '恒用戒香塗瑩體，常持定服以資身，', '菩提妙華遍莊嚴，隨所住處常安樂。'],
  'May every world be always at peace. May boundless merit and wisdom benefit all that lives. May all wrongdoing be wiped away; may all leave suffering behind and return to perfect peace. Anoint the body with the fragrance of moral discipline, clothe it in the robe of concentration, adorn it everywhere with the flowers of awakening — and wherever you dwell, may you always be at ease.'),
]

# ---------------------------------------------------------------- 阿彌陀經
AMITUO = [
 ('h', 'The assembly'),
 ('如是我聞。一時，佛在舍衛國，祇樹給孤獨園。與大比丘僧，千二百五十人俱，皆是大阿羅漢，眾所知識。',
  'Thus have I heard. At one time the Buddha was staying near Śrāvastī, in Jeta’s Grove, Anāthapiṇḍada’s park, together with a great community of 1,250 monks — all great arhats, well known to everyone.'),
 ('長老舍利弗，摩訶目犍連，摩訶迦葉，摩訶迦旃延，摩訶俱絺羅，離婆多，周利槃陀伽，難陀，阿難陀，羅睺羅，憍梵波提，賓頭盧頗羅墮，迦留陀夷，摩訶劫賓那，薄拘羅，阿㝹樓馱，如是等諸大弟子。',
  'Among them were the elders Śāriputra, Mahāmaudgalyāyana, Mahākāśyapa, Mahākātyāyana, Mahākauṣṭhila, Revata, Śuddhipanthaka, Nanda, Ānanda, Rāhula, Gavāṃpati, Piṇḍola Bhāradvāja, Kālodāyin, Mahākapphiṇa, Vakkula, and Aniruddha — these and other great disciples.'),
 ('並諸菩薩摩訶薩，文殊師利法王子，阿逸多菩薩，乾陀訶提菩薩，常精進菩薩，與如是等諸大菩薩。及釋提桓因等，無量諸天大眾俱。',
  'There were also great bodhisattvas — Mañjuśrī the Dharma Prince, Ajita (Maitreya), Gandhahastin, and Ever-Diligent — along with Śakra, lord of the gods, and countless heavenly beings.'),

 ('h', 'The Land of Utmost Bliss'),
 ('爾時佛告長老舍利弗，從是西方，過十萬億佛土，有世界名曰極樂，其土有佛，號阿彌陀，今現在說法。',
  'Then the Buddha said to the elder Śāriputra: “West of here, beyond a hundred thousand million Buddha-lands, there is a world called Utmost Bliss (Sukhāvatī). In that land there is a Buddha named Amitābha, who is teaching the Dharma right now.'),
 ('舍利弗，彼土何故名為極樂。其國眾生，無有眾苦，但受諸樂，故名極樂。',
  '“Śāriputra, why is that land called Utmost Bliss? The beings there know no suffering at all; they experience only happiness. That is why it is called Utmost Bliss.'),
 ('又舍利弗，極樂國土，七重欄楯，七重羅網，七重行樹，皆是四寶周帀圍繞，是故彼國名為極樂。',
  '“That land is ringed by seven tiers of railings, seven layers of netting, and seven rows of trees, all made of the four precious things. That, too, is why it is called Utmost Bliss.'),
 ('又舍利弗，極樂國土，有七寶池，八功德水，充滿其中。池底純以金沙布地。四邊階道，金、銀、瑠璃、玻瓈合成。上有樓閣，亦以金、銀、琉璃、玻瓈、硨磲、赤珠、瑪瑙、而嚴飾之。池中蓮華，大如車輪，青色青光，黃色黃光，赤色赤光，白色白光，微妙香潔。舍利弗，極樂國土，成就如是功德莊嚴。',
  '“There are pools of the seven jewels, filled with water of eight fine qualities; their beds are covered with gold sand. On all four sides are stairways of gold, silver, lapis lazuli, and crystal, and above them stand pavilions adorned with gold, silver, lapis lazuli, crystal, mother-of-pearl, red pearls, and agate. The lotuses in the pools are as large as chariot wheels — blue ones shining blue, yellow shining yellow, red shining red, white shining white — delicate, fragrant, and pure. Śāriputra, the Land of Utmost Bliss is complete with such splendor and virtue.'),
 ('又舍利弗，彼佛國土，常作天樂，黃金為地，晝夜六時，雨天曼陀羅華。其土眾生，常以清旦，各以衣祴，盛眾妙華，供養他方十萬億佛。即以食時，還到本國，飯食經行。舍利弗，極樂國土，成就如是功德莊嚴。',
  '“In that Buddha-land heavenly music is always playing and the ground is gold. Six times each day and night, mandārava blossoms rain from the sky. In the clear early morning the beings there gather these wonderful flowers in the folds of their robes and offer them to a hundred thousand million Buddhas in other worlds. By mealtime they are home again, to eat and then to walk in meditation. Śāriputra, the Land of Utmost Bliss is complete with such splendor and virtue.'),
 ('復次舍利弗。彼國常有種種奇妙雜色之鳥，白鶴、孔雀、鸚鵡、舍利、迦陵頻伽，共命之鳥。是諸眾鳥，晝夜六時，出和雅音。其音演暢五根、五力、七菩提分、八聖道分、如是等法。其土眾生，聞是音已，皆悉念佛、念法、念僧。',
  '“In that land there are always many kinds of rare and beautiful birds of every color: white cranes, peacocks, parrots, śāri birds, kalaviṅkas, and two-headed jīvaṃjīva birds. Six times each day and night they sing in gentle, harmonious voices, and their song proclaims the five faculties, the five powers, the seven factors of awakening, the noble eightfold path, and other teachings. Hearing it, the beings of that land all turn their minds to the Buddha, the Dharma, and the Sangha.'),
 ('舍利弗，汝勿謂此鳥，實是罪報所生。所以者何，彼佛國土，無三惡道。舍利弗，其佛國土，尚無惡道之名，何況有實。是諸眾鳥，皆是阿彌陀佛，欲令法音宣流，變化所作。',
  '“Do not think these birds were born as the result of bad karma. Why? In that Buddha-land the three lower realms do not exist — not even their names are heard there, let alone the realities. Amitābha Buddha himself brings these birds into being so that the sound of the Dharma may flow everywhere.'),
 ('舍利弗，彼佛國土，微風吹動，諸寶行樹，及寶羅網，出微妙音，譬如百千種樂，同時俱作。聞是音者，自然皆生念佛、念法、念僧之心。舍利弗，其佛國土，成就如是功德莊嚴。',
  '“When a soft breeze stirs the rows of jeweled trees and the jeweled nets, they give off delicate, wonderful sounds, like a hundred thousand instruments playing together. In all who hear it, the wish to be mindful of the Buddha, the Dharma, and the Sangha arises naturally. Śāriputra, that Buddha-land is complete with such splendor and virtue.'),

 ('h', 'Amitābha: infinite light, infinite life'),
 ('舍利弗，於汝意云何，彼佛何故號阿彌陀。舍利弗，彼佛光明無量。照十方國，無所障礙，是故號為阿彌陀。又舍利弗。彼佛壽命，及其人民，無量無邊阿僧祇劫，故名阿彌陀。舍利弗，阿彌陀佛成佛以來，於今十劫。',
  '“What do you think, Śāriputra — why is that Buddha called Amitābha? His light is measureless; it shines on the lands of the ten directions and nothing obstructs it. So he is called Amitābha, ‘Infinite Light.’ And his lifespan, and that of his people, lasts for measureless, boundless, incalculable eons. So he is also called ‘Infinite Life.’ Ten eons have passed since Amitābha became a Buddha.'),
 ('又舍利弗，彼佛有無量無邊聲聞弟子，皆阿羅漢，非是算數之所能知。諸菩薩眾，亦復如是。舍利弗，彼佛國土，成就如是功德莊嚴。',
  '“That Buddha has countless disciples, all arhats, more than any counting can reckon; the assembly of bodhisattvas is just as vast. Śāriputra, that Buddha-land is complete with such splendor and virtue.'),
 ('又舍利弗，極樂國土，眾生生者，皆是阿鞞跋致。其中多有一生補處，其數甚多，非是算數所能知之，但可以無量無邊阿僧祇說。',
  '“All beings born in the Land of Utmost Bliss never fall back on the path. Many among them are in their final life before Buddhahood — so many that they cannot be counted; one can only say ‘measureless, boundless, incalculable.’'),

 ('h', 'How to be born there'),
 ('舍利弗，眾生聞者，應當發願，願生彼國。所以者何，得與如是諸上善人俱會一處。',
  '“Those who hear this should make the vow: ‘May I be born in that land.’ Why? Because there they will be together in one place with people of such supreme goodness.'),
 ('舍利弗，不可以少善根福德因緣，得生彼國。舍利弗，若有善男子善女人，聞說阿彌陀佛，執持名號，若一日，若二日，若三日，若四日，若五日，若六日，若七日，一心不亂。其人臨命終時，阿彌陀佛，與諸聖眾，現在其前。是人終時，心不顛倒，即得往生阿彌陀佛極樂國土。',
  '“One cannot be born there with only a little goodness, merit, or favorable conditions. If a good man or good woman hears of Amitābha Buddha and holds fast to his name — for one day, two days, three, four, five, six, or seven days — with a mind single and undistracted, then at the end of life Amitābha Buddha and the assembly of sages will appear before that person. At the moment of death the mind will not be confused, and that person will at once be born in Amitābha’s Land of Utmost Bliss.'),
 ('舍利弗，我見是利，故說此言。若有眾生，聞是說者，應當發願，生彼國土。',
  '“I see this benefit, Śāriputra, and so I say: all beings who hear this teaching should vow to be born in that land.'),

 ('h', 'The Buddhas of the six directions bear witness'),
 ('舍利弗，如我今者，讚歎阿彌陀佛不可思議功德之利。東方亦有阿閦鞞佛，須彌相佛，大須彌佛，須彌光佛，妙音佛，如是等恆河沙數諸佛，各於其國，出廣長舌相，徧覆三千大千世界，說誠實言。汝等眾生，當信是稱讚不可思議功德，一切諸佛所護念經。',
  '“Just as I now praise the inconceivable merits of Amitābha Buddha, so in the East there are Akṣobhya Buddha, Sumeru-Appearance Buddha, Great Sumeru Buddha, Sumeru-Light Buddha, Wonderful-Sound Buddha, and Buddhas as many as the sands of the Ganges. Each in his own land puts forth his broad, long tongue, covering a billion worlds, and speaks these true words: ‘All of you should trust this sutra, which praises inconceivable merits and which all Buddhas protect and keep in mind.’'),
 ('舍利弗，南方世界，有日月燈佛，名聞光佛，大燄肩佛，須彌燈佛，無量精進佛，如是等恆河沙數諸佛，各於其國，出廣長舌相，徧覆三千大千世界，說誠實言。汝等眾生，當信是稱讚不可思議功德，一切諸佛所護念經。',
  '“In the worlds of the South there are Sun-Moon-Lamp Buddha, Renowned-Light Buddha, Great-Blazing-Shoulders Buddha, Sumeru-Lamp Buddha, Infinite-Vigor Buddha, and Buddhas as many as the sands of the Ganges. Each in his own land speaks the same true words: ‘Trust this sutra, which all Buddhas protect and keep in mind.’'),
 ('舍利弗，西方世界，有無量壽佛，無量相佛，無量幢佛，大光佛，大明佛，寶相佛，淨光佛，如是等恆河沙數諸佛，各於其國，出廣長舌相，徧覆三千大千世界，說誠實言。汝等眾生，當信是稱讚不可思議功德，一切諸佛所護念經。',
  '“In the worlds of the West there are Infinite-Life Buddha, Infinite-Appearance Buddha, Infinite-Banner Buddha, Great-Light Buddha, Great-Brightness Buddha, Jewel-Appearance Buddha, Pure-Light Buddha, and Buddhas as many as the sands of the Ganges. Each in his own land speaks the same true words: ‘Trust this sutra, which all Buddhas protect and keep in mind.’'),
 ('舍利弗，北方世界，有燄肩佛，最勝音佛，難沮佛，日生佛，網明佛，如是等恆河沙數諸佛，各於其國，出廣長舌相，徧覆三千大千世界，說誠實言。汝等眾生，當信是稱讚不可思議功德，一切諸佛所護念經。',
  '“In the worlds of the North there are Blazing-Shoulders Buddha, Supreme-Sound Buddha, Hard-to-Defeat Buddha, Sun-Born Buddha, Net-of-Light Buddha, and Buddhas as many as the sands of the Ganges. Each in his own land speaks the same true words: ‘Trust this sutra, which all Buddhas protect and keep in mind.’'),
 ('舍利弗，下方世界，有師子佛，名聞佛，名光佛，達摩佛，法幢佛，持法佛，如是等恆河沙數諸佛，各於其國，出廣長舌相，徧覆三千大千世界，說誠實言。汝等眾生，當信是稱讚不可思議功德，一切諸佛所護念經。',
  '“In the worlds below there are Lion Buddha, Renown Buddha, Famed-Light Buddha, Dharma Buddha, Dharma-Banner Buddha, Upholder-of-the-Dharma Buddha, and Buddhas as many as the sands of the Ganges. Each in his own land speaks the same true words: ‘Trust this sutra, which all Buddhas protect and keep in mind.’'),
 ('舍利弗，上方世界，有梵音佛，宿王佛，香上佛，香光佛，大燄肩佛，雜色寶華嚴身佛，娑羅樹王佛，寶華德佛，見一切義佛，如須彌山佛，如是等恆河沙數諸佛，各於其國，出廣長舌相，徧覆三千大千世界，說誠實言。汝等眾生，當信是稱讚不可思議功德，一切諸佛所護念經。',
  '“In the worlds above there are Brahma-Sound Buddha, Constellation-King Buddha, Supreme-Fragrance Buddha, Fragrant-Light Buddha, Great-Blazing-Shoulders Buddha, Body-Adorned-with-Many-Colored-Jewel-Flowers Buddha, Sāla-Tree-King Buddha, Jewel-Flower-Virtue Buddha, Seeing-All-Meanings Buddha, Like-Mount-Sumeru Buddha, and Buddhas as many as the sands of the Ganges. Each in his own land speaks the same true words: ‘Trust this sutra, which all Buddhas protect and keep in mind.’'),

 ('h', 'Faith and the vow'),
 ('舍利弗，於汝意云何，何故名為一切諸佛所護念經。舍利弗，若有善男子善女人，聞是經受持者，及聞諸佛名者，是諸善男子善女人，皆為一切諸佛之所護念，皆得不退轉於阿耨多羅三藐三菩提。是故舍利弗，汝等皆當信受我語，及諸佛所說。',
  '“Why is this called ‘the sutra protected and kept in mind by all Buddhas’? Any good man or woman who hears this sutra and holds to it, and who hears the names of these Buddhas, is protected and kept in mind by all the Buddhas, and will never turn back from supreme, perfect awakening. Therefore, Śāriputra, all of you should trust and accept my words and the words of all the Buddhas.'),
 ('舍利弗，若有人，已發願，今發願，當發願，欲生阿彌陀佛國者。是諸人等，皆得不退轉於阿耨多羅三藐三菩提。於彼國土，若已生，若今生，若當生，是故舍利弗，諸善男子善女人，若有信者，應當發願，生彼國土。',
  '“Whoever has vowed, now vows, or will vow to be born in Amitābha’s land will never turn back from supreme, perfect awakening; they have been born there, are being born there, or will be born there. So, Śāriputra, every good man and woman who has faith should vow to be born in that land.'),
 ('舍利弗，如我今者，稱讚諸佛不可思議功德，彼諸佛等，亦稱讚我不可思議功德。而作是言，釋迦牟尼佛，能為甚難希有之事。能於娑婆國土，五濁惡世，劫濁、見濁、煩惱濁、眾生濁、命濁中，得阿耨多羅三藐三菩提。為諸眾生，說是一切世間難信之法。',
  '“Just as I now praise the inconceivable merits of the Buddhas, they praise mine too, saying: ‘Śākyamuni Buddha has done something extremely difficult and rare. In the Sahā world, in an evil age of five corruptions — of the times, of views, of afflictions, of beings, and of lifespan — he attained supreme, perfect awakening, and for the sake of all beings he teaches this Dharma that the whole world finds hard to believe.’'),
 ('舍利弗，當知我於五濁惡世，行此難事，得阿耨多羅三藐三菩提，為一切世間說此難信之法，是為甚難。',
  '“Know this, Śāriputra: in this evil age of five corruptions I did this difficult thing, attained supreme, perfect awakening, and taught the whole world this hard-to-believe Dharma. That is difficult indeed.”'),
 ('佛說此經已，舍利弗及諸比丘，一切世間天人阿修羅等，聞佛所說，歡喜信受，作禮而去。',
  'When the Buddha had finished speaking this sutra, Śāriputra, the monks, and all the gods, humans, and asuras of the world rejoiced at what they had heard, accepted it in faith, bowed, and departed.'),
]

# Sutra-specific readings (transliterated names and liturgical pronunciations).
AMITUO_READINGS = {
    '舍衛': 'shè wèi', '比丘': 'bǐ qiū', '俱': 'jù', '阿羅漢': 'ā luó hàn', '長老': 'zhǎng lǎo',
    '摩訶': 'mó hē', '目犍連': 'mù jiān lián', '迦葉': 'jiā shè', '迦旃延': 'jiā zhān yán',
    '俱絺羅': 'jù chī luó', '離婆多': 'lí pó duō', '周利槃陀伽': 'zhōu lì pán tuó qié',
    '難陀': 'nán tuó', '阿難陀': 'ā nán tuó', '羅睺羅': 'luó hóu luó', '憍梵波提': 'jiāo fàn bō tí',
    '賓頭盧頗羅墮': 'bīn tóu lú pō luó duò', '迦留陀夷': 'jiā liú tuó yí',
    '劫賓那': 'jié bīn nuó', '薄拘羅': 'bó jū luó', '阿㝹樓馱': 'ā nóu lóu tuó',
    '文殊師利': 'wén shū shī lì', '阿逸多': 'ā yì duō', '乾陀訶提': 'qián tuó hē tí',
    '釋提桓因': 'shì tí huán yīn', '極樂': 'jí lè', '諸樂': 'zhū lè', '天樂': 'tiān yuè',
    '種樂': 'zhǒng yuè', '種種': 'zhǒng zhǒng', '名為': 'míng wéi', '號為': 'hào wéi',
    '黃金為地': 'huáng jīn wéi dì', '皆為': 'jiē wéi', '能為': 'néng wéi', '是為': 'shì wéi',
    '為諸': 'wèi zhū', '為一切': 'wèi yí qiè', '七重': 'qī chóng', '欄楯': 'lán shǔn',
    '行樹': 'háng shù', '周帀': 'zhōu zā', '瑠璃': 'liú lí', '琉璃': 'liú lí', '玻瓈': 'bō lí',
    '硨磲': 'chē qú', '瑪瑙': 'mǎ nǎo', '華': 'huā',
    '雨天': 'yù tiān', '衣祴': 'yī gé', '盛': 'chéng',
    '供養': 'gòng yàng', '還到': 'huán dào', '飯食': 'fàn shí', '經行': 'jīng xíng',
    '鸚鵡': 'yīng wǔ', '迦陵頻伽': 'jiā líng pín qié', '和雅': 'hé yǎ', '演暢': 'yǎn chàng',
    '菩提分': 'pú tí fēn', '道分': 'dào fēn', '惡道': 'è dào', '惡世': 'è shì',
    '阿僧祇': 'ā sēng qí', '算數': 'suàn shù', '阿鞞跋致': 'ā pí bá zhì', '一生補處': 'yì shēng bǔ chù',
    '其數': 'qí shù', '一處': 'yí chù', '少善根': 'shǎo shàn gēn', '一日': 'yí rì',
    '一切': 'yí qiè', '不亂': 'bú luàn', '不退轉': 'bú tuì zhuǎn', '不可': 'bù kě', '顛倒': 'diān dǎo',
    '阿閦鞞': 'ā chù pí', '須彌相': 'xū mí xiàng', '寶相': 'bǎo xiàng', '無量相': 'wú liàng xiàng',
    '舌相': 'shé xiàng', '恆河沙數': 'héng hé shā shù', '徧覆': 'biàn fù', '稱讚': 'chēng zàn',
    '燄肩': 'yàn jiān', '幢': 'chuáng', '難沮': 'nán jǔ', '師子': 'shī zǐ', '宿王': 'xiù wáng',
    '娑羅': 'suō luó', '娑婆': 'suō pó', '阿耨多羅三藐三菩提': 'ā nòu duō luó sān miǎo sān pú tí',
    '釋迦牟尼': 'shì jiā móu ní', '甚難': 'shèn nán', '難信': 'nán xìn', '難事': 'nán shì',
    '希有': 'xī yǒu', '五濁': 'wǔ zhuó', '濁': 'zhuó', '煩惱': 'fán nǎo', '作禮': 'zuò lǐ',
    '知識': 'zhī shí', '現在說法': 'xiàn zài shuō fǎ', '現在其前': 'xiàn zài qí qián',
    '說': 'shuō', '廣長舌相': 'guǎng cháng shé xiàng', '弟子': 'dì zǐ', '男子': 'nán zǐ', '法王子': 'fǎ wáng zǐ',
    '行此': 'xíng cǐ', '大眾': 'dà zhòng', '晝': 'zhòu', '尚': 'shàng', '共命': 'gòng mìng',
}

# ---------------------------------------------------------------- 往生咒 (transliteration; fixed readings)
WANGSHENG = [
 ('南無阿彌多婆夜', 'ná mó ā mí duō pó yè'), ('哆他伽多夜', 'duō tuō qié duō yè'),
 ('哆地夜他', 'duō dí yé tuō'), ('阿彌利都婆毗', 'ā mí lì dū pó pí'),
 ('阿彌利哆', 'ā mí lì duō'), ('悉耽婆毗', 'xī dān pó pí'),
 ('阿彌唎哆', 'ā mí lì duō'), ('毗迦蘭帝', 'pí jiā lán dì'),
 ('阿彌唎哆', 'ā mí lì duō'), ('毗迦蘭多', 'pí jiā lán duō'),
 ('伽彌膩', 'qié mí ní'), ('伽伽那', 'qié qié nuó'),
 ('枳多迦利', 'zhǐ duō jiā lí'), ('娑婆訶', 'suō pó hē'),
]

# ---------------------------------------------------------------- 讚佛偈
ZANFO = [
 ('阿彌陀佛身金色，相好光明無等倫。', 'Amitābha Buddha’s body is the color of gold; the radiance of his noble features is beyond compare.'),
 ('白毫宛轉五須彌，紺目澄清四大海。', 'The white curl between his brows winds like five Mount Sumerus; his deep-blue eyes are as clear as the four great oceans.'),
 ('光中化佛無數億，化菩薩眾亦無邊。', 'Within his light appear countless millions of Buddhas, and bodhisattvas without number.'),
 ('四十八願度眾生，九品咸令登彼岸。', 'By his forty-eight vows he carries living beings across; through nine grades of lotus birth he brings them all to the other shore.'),
 ('南無西方極樂世界，大慈大悲阿彌陀佛。', 'Homage to Amitābha Buddha of great kindness and great compassion, in the Western Land of Utmost Bliss.'),
]

HUIXIANG = [
 ('願以此功德，莊嚴佛淨土。', 'May the merit of this practice adorn the Buddha’s Pure Land.'),
 ('上報四重恩，下濟三塗苦。', 'May it repay the four great kindnesses above, and relieve the suffering of the three lower realms below.'),
 ('若有見聞者，悉發菩提心。', 'May all who see or hear of it give rise to the mind of awakening.'),
 ('盡此一報身，同生極樂國。', 'And when this one life is over, may we be born together in the Land of Utmost Bliss.'),
]

# ---------------------------------------------------------------- 午供 · 文疏 (Chinese + English only)
SHUWEN = [
 ('The merit of the gathering',
  ['修齋功德力，集福妙難量；', '諸佛生歡喜，龍天降吉祥。'],
  'The power of merit from keeping the fast and practicing together gathers blessings too wonderful to measure. May the Buddhas rejoice, and may the nāgas and gods who protect the Dharma send down good fortune.'),
 ('The teaching and its many gates',
  ['伏以：', '大教遠流，示一乘歸元之路；', '神功叵測，開眾生方便之門。'],
  'With deep respect we say: the great teaching has flowed down through the ages, showing the One Vehicle — the road back to the source. Its power is beyond measuring, and it opens for living beings many gates of skillful means.'),
 ('Where we are, and why we have come',
  ['今據：', '一泗天下，南瞻部洲，', '台灣省南投縣信義鄉陽和巷八十號，', '奉佛植福延禧，', '誦經消災解厄，', '添補運途，保命長生。'],
  'Here in this human world of Jambudvīpa — at No. 80, Yanghe Lane, Xinyi Township, Nantou County, Taiwan — we honor the Buddha to plant blessings and extend good fortune, and we recite the sutra so that calamities may be averted and hardships resolved, that the road ahead may be smoother, and that life may be safe and long.'),
 ('Those who are gathered',
  ['今有如意精舍釋子達慧帶領，', '所有參加念佛善男信女等眾，', '合會眾等虔誠焚香禮拜。'],
  'Today, led by the monastic Da-hui of Ru-Yi Meditation Center, all the good men and faithful women who have come to recite the Buddha’s name — the whole assembly together — sincerely offer incense and bow.'),
 ('Calling on the Buddhas and bodhisattvas',
  ['南無娑婆世界本師釋迦牟尼佛', '南無消災延壽藥師佛', '南無極樂世界無量壽佛', '南無大悲觀世音菩薩',
   '南無弘願地藏王菩薩', '南無護法韋馱尊天菩薩', '南無伽藍聖眾菩薩', '南無十方三世一切諸佛菩薩', '各寶金蓮座下。'],
  'Homage to our original teacher in this Sahā world, Śākyamuni Buddha. Homage to the Medicine Buddha, who dispels calamity and lengthens life. Homage to the Buddha of Infinite Life (Amitābha) in the Land of Utmost Bliss. Homage to the greatly compassionate Bodhisattva Avalokiteśvara (Guanyin). Homage to Bodhisattva Kṣitigarbha of the great vow. Homage to the Dharma protector Skanda (Weituo). Homage to the guardian sages of the monastery. Homage to all Buddhas and bodhisattvas of the ten directions and the three times — before each of your jeweled golden lotus thrones.'),
 ('Our condition',
  ['恭申意者，', '言念參加念佛，敬點光明燈者，', '忝處人倫，濫沾聖化；', '無明內障，日積有漏之因；',
   '妄境外搖，累積無殃之垢；', '竛竮于崎嶇道上，那得歸來；', '耽著於朽宅之中，難求出離。'],
  'We respectfully state our intention. We who have come to recite the Buddha’s name and to light the lamps of brightness are humbled to have been born human and to have been touched, undeserving, by the holy teaching. Yet ignorance blocks us from within, and day by day we pile up the causes of further suffering; illusory things shake us from without, and the grime of our faults gathers. Alone and stumbling on a rough road, how are we to find the way home? Clinging to a crumbling house, we find it hard to seek the way out.'),
 ('Turning toward the Dharma',
  ['欣逢聖教，敢不傾心？', '是於涓向今日，就於如意精舍，敬請善侶。'],
  'Having had the joy of meeting the holy teaching, how could we not give it our whole heart? And so we have chosen this day, come to Ru-Yi, and respectfully invited our good companions in practice.'),
 ('What we practice today',
  ['啟誦：', '佛說阿彌陀經全卷，', '念佛一永日，', '加持諸佛真言。'],
  'We begin our recitation: the Amitābha Sutra in full, a whole day of reciting the Buddha’s name, and the mantras of the Buddhas.'),
 ('The offering',
  ['是日呈獻香花果品，上奉', '十方三寶、萬德千尊，', '並及諸天護法、一切神祇，', '光降法筵，慈悲納受。'],
  'On this day we present incense, flowers, and fruit, offering them up to the Three Jewels of the ten directions and to the countless holy ones of perfect virtue, and also to the heavenly Dharma protectors and all guardian spirits. May you grace this Dharma gathering with your presence and, in your compassion, accept these offerings.'),
 ('Light and rain',
  ['佛光普照，菩薩加被；', '千生業障頓消，累世愆尤蠲除。', '佛光遠蔭，將暗室而重光；', '法雨普沾，使枯枝而再潤。'],
  'May the Buddha’s light shine everywhere, and may the bodhisattvas protect and bless us. May the karmic obstacles of a thousand lifetimes melt away at once, and the faults of many lives be washed clean. May the Buddha’s light shelter us far and wide, bringing brightness back to a darkened room. May the rain of the Dharma fall on all, so that the withered branch turns green again.'),
 ('For the world',
  ['更祈：', '風調雨順，國泰民安；', '四時無災，八節有慶。'],
  'We pray further: may wind and rain come in their season; may the country be at peace and its people safe; may the four seasons pass without disaster, and every festival of the year be a time of joy.'),
 ('For each person and family',
  ['男增百福，女納千祥；', '正信三寶，般若智以現前，菩提心而不退；', '元辰光彩，壽命延長；', '財源廣進，利路亨通；', '所求如意，降大吉祥。'],
  'May the men gain a hundred blessings and the women receive a thousand kinds of good fortune. May all have true faith in the Three Jewels; may the wisdom of prajñā arise, and may the mind of awakening never fall back. May each one’s life shine bright and be long. May livelihoods prosper and the way ahead be open. May every wholesome wish be fulfilled, and may great good fortune descend.'),
 ('Closing',
  ['謹疏', '上聞', '時維中華民國　年　月　日', '如意精舍再稽首禮拜上申'],
  'With reverence, this petition is offered up to be heard. Dated this day, Ru-Yi Meditation Center once more bows to the ground and respectfully submits it.'),
]

# ================================================================ render
def render_text(items, extra=None):
    global READINGS, _KEYS
    saved = (READINGS, _KEYS)
    if extra:
        READINGS = dict(READINGS, **extra)
        _KEYS = sorted(READINGS, key=len, reverse=True)
    out = []
    for it in items:
        if it[0] == 'h':
            out.append('<h3 class="lt-sub">%s</h3>' % it[1])
        else:
            out.append(seg(it[0], it[1]))
    READINGS, _KEYS = saved
    return '\n'.join(out)


def render_pairs(pairs):
    return '\n'.join(seg(zh, en) for zh, en in pairs)


def mantra_html():
    parts = []
    for zh, py in WANGSHENG:
        parts.append('<em>%s</em>' % cells(zh, py.split()))
    return '<div class="lt-seg"><div class="lt-zh">%s</div></div>' % ''.join(parts)


def shuwen_html():
    out = []
    for title, lines, en in SHUWEN:
        out.append('<h3 class="lt-sub">%s</h3>' % title)
        out.append(seg(lines, en, pin=False))
    return '\n'.join(out)


NAMO = cells('南無阿彌陀佛')
AMITUOFO = cells('阿彌陀佛')

PAGE = r'''---
layout: default
title: Chanting Book · Buddha-Recitation Service
permalink: /community/dharma-events/liturgy/
excerpt: Follow the whole day of the monthly Buddha-Recitation Service at Ru-Yi — every chant in Chinese, pinyin, and plain English.
---

<style>
  /* ============ CHANTING BOOK — bespoke ============ */
  .lt-zhfont{font-family:'PingFang TC','Apple LiGothic Medium','Microsoft JhengHei',sans-serif;}
  .lt-hero{background:linear-gradient(160deg,#2a1710 0%,#5c2412 55%,#8c2f12 100%);color:#fff;padding:78px 0 62px;}
  .lt-wrap{max-width:860px;margin:0 auto;padding:0 22px;}
  .lt-hero .eyebrow{color:#f0c98a;letter-spacing:.2em;font-size:12.5px;text-transform:uppercase;font-weight:600;}
  .lt-hero .eyebrow a{color:inherit;text-decoration:none;border-bottom:1px solid rgba(240,201,138,.5);}
  .lt-hero h1{font-family:'Playfair Display',serif;font-weight:600;color:#fff;font-size:clamp(36px,6.4vw,62px);line-height:1.05;margin:14px 0 6px;}
  .lt-hero .zh{font-family:'PingFang TC','Apple LiGothic Medium','Microsoft JhengHei',sans-serif;font-size:21px;letter-spacing:.3em;color:#f3d9a8;}
  .lt-hero p{max-width:620px;margin-top:18px;font-size:18px;line-height:1.68;color:#f1e9e2;}

  /* how to read */
  .lt-how{background:#fff;padding:44px 0 10px;}
  .lt-key{border:1px solid #ece4d5;border-radius:12px;background:#fffaf0;padding:22px 24px;}
  .lt-key h2{font-family:'Playfair Display',serif;font-size:22px;color:#1a1a1a;margin:0 0 10px;}
  .lt-key p{font-size:16px;line-height:1.66;color:#4a4d53;margin:0 0 8px;}
  .lt-key p:last-child{margin-bottom:0;}

  /* day at a glance */
  .lt-day{background:#fff;padding:26px 0 46px;}
  .lt-day ol{list-style:none;margin:0;padding:0;display:grid;gap:10px;}
  .lt-day a{display:flex;gap:18px;align-items:center;border:1px solid #ece4d5;border-radius:12px;padding:14px 18px;text-decoration:none;background:#fff;transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease;}
  .lt-day a:hover{transform:translateX(3px);border-color:#ddd0bb;box-shadow:0 14px 30px -20px rgba(60,50,30,.55);text-decoration:none;}
  .lt-day .t{flex-shrink:0;width:92px;font-family:'Playfair Display',serif;font-size:19px;font-weight:600;color:#8c2f12;}
  .lt-day .n{font-size:17px;font-weight:600;color:#1a1a1a;line-height:1.3;}
  .lt-day .s{font-size:14px;color:#8a857c;margin-top:2px;}

  /* sticky toolbar */
  .lt-bar{position:sticky;top:64px;z-index:20;background:rgba(244,241,236,.96);backdrop-filter:blur(6px);border-top:1px solid #e6ddcb;border-bottom:1px solid #e6ddcb;}
  .lt-bar-in{max-width:860px;margin:0 auto;padding:8px 22px;display:flex;gap:8px;align-items:center;overflow-x:auto;white-space:nowrap;}
  .lt-bar a,.lt-bar button{flex-shrink:0;font:600 13px 'Inter',sans-serif;color:#5a3a22;background:#fff;border:1px solid #e0d5c0;border-radius:30px;padding:6px 13px;text-decoration:none;cursor:pointer;}
  .lt-bar a:hover,.lt-bar button:hover{border-color:#b8431c;color:#8c2f12;text-decoration:none;}
  .lt-bar button[aria-pressed="false"]{color:#a59f93;background:transparent;text-decoration:line-through;}
  .lt-bar .sep{flex-shrink:0;width:1px;height:20px;background:#d9cdb8;margin:0 4px;}

  /* sessions */
  .lt-sess{padding:66px 0 30px;background:#fff;scroll-margin-top:110px;}
  .lt-sess:nth-of-type(even){background:#faf8f4;}
  .lt-sess .time{display:inline-block;background:#8c2f12;color:#fff;font-family:'Playfair Display',serif;font-size:15px;letter-spacing:.14em;font-weight:600;padding:6px 18px;border-radius:30px;}
  .lt-sess h2{font-family:'Playfair Display',serif;font-size:clamp(28px,4.4vw,40px);line-height:1.1;color:#1a1a1a;margin:16px 0 4px;}
  .lt-sess .zhsub{font-family:'PingFang TC','Apple LiGothic Medium','Microsoft JhengHei',sans-serif;font-size:18px;color:#8c2f12;letter-spacing:.12em;margin-bottom:14px;}
  .lt-sess .intro{font-size:17px;line-height:1.7;color:#4a4d53;margin:0 0 8px;}
  .lt-text{scroll-margin-top:110px;margin-top:40px;}
  .lt-text>h2{font-size:clamp(24px,3.6vw,32px);}
  .lt-sub{font-family:'Inter',sans-serif;font-size:12.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#3f7565;margin:42px 0 14px;padding-top:18px;border-top:1px solid #e6ddcb;}

  .lt-seg{margin:0 0 30px;}
  .lt-zh{font-family:'PingFang TC','Apple LiGothic Medium','Microsoft JhengHei',sans-serif;line-height:1.2;margin-bottom:6px;}
  .lt-zh span{display:inline-flex;flex-direction:column;align-items:center;vertical-align:top;margin:0 5px 12px 0;min-width:1.5em;}
  .lt-zh em{font-style:normal;display:inline-block;white-space:nowrap;margin-right:18px;}
  .lt-zh b{font-weight:500;font-size:calc(25px*var(--lt-scale,1));color:#1a1a1a;line-height:1.25;white-space:nowrap;}
  .lt-zh i{font-style:normal;font-family:'Inter',sans-serif;font-size:calc(12.5px*var(--lt-scale,1));color:#8c2f12;line-height:1.3;letter-spacing:0;}
  .lt-zh.lt-plain{font-size:calc(22px*var(--lt-scale,1));line-height:1.75;color:#1a1a1a;margin-bottom:0;}
  .lt-seg .lt-plain:last-of-type{margin-bottom:10px;}
  .lt-en{font-size:calc(17px*var(--lt-scale,1));line-height:1.72;color:#3a3d43;margin:4px 0 0;padding-left:16px;border-left:3px solid #e6d3b0;}
  .lt-note{font-size:15px;line-height:1.6;color:#7a756c;margin:0 0 8px;font-style:italic;}
  .lt-nopy .lt-zh i{display:none;}
  .lt-nopy .lt-zh span{min-width:0;margin:0 0 4px;}
  .lt-noen .lt-en{display:none;}

  .lt-callout{border:1px solid #eddcb6;background:linear-gradient(180deg,#fffaf0,#fff);border-radius:12px;padding:20px 22px;margin:22px 0 30px;}
  .lt-callout p{font-size:16.5px;line-height:1.68;color:#4a4d53;margin:0 0 8px;}
  .lt-callout p:last-child{margin-bottom:0;}
  .lt-callout strong{color:#1a1a1a;}
  .lt-jump{display:inline-block;margin:6px 10px 0 0;background:#8c2f12;color:#fff;font-weight:600;font-size:15px;padding:10px 20px;border-radius:8px;text-decoration:none;}
  .lt-jump:hover{background:#a53a18;text-decoration:none;color:#fff;}

  .lt-end{background:#f4f1ec;padding:54px 0 70px;text-align:center;}
  .lt-end p{font-size:16px;line-height:1.7;color:#5a5d63;max-width:620px;margin:0 auto 14px;}
  .lt-end a{color:#8c2f12;font-weight:600;}
  @media(max-width:560px){
    .lt-zh b{font-size:calc(22px*var(--lt-scale,1));}
    .lt-zh i{font-size:calc(11.5px*var(--lt-scale,1));}
    .lt-day .t{width:74px;font-size:17px;}
  }
  @media print{.lt-bar,.site-header,.site-footer{display:none!important;}.lt-sess{padding:20px 0;}}
</style>

<section class="lt-hero">
  <div class="lt-wrap">
    <div class="eyebrow"><a href="/community/dharma-events/">Dharma Events</a> · Chanting Book</div>
    <h1>The Buddha-Recitation Service</h1>
    <div class="zh">念佛法會儀軌</div>
    <p>Everything we chant on a monthly retreat day, in the order we chant it. Each passage is given in Chinese with pinyin beneath every character, followed by its meaning in plain English — so you can join in with your voice and know what you are saying.</p>
  </div>
</section>

<section class="lt-how">
  <div class="lt-wrap">
    <div class="lt-key">
      <h2>How to use this page</h2>
      <p><strong>Follow the pinyin</strong> under each character to chant along. The wooden fish keeps the beat: one character, one strike. If you lose your place, simply listen and rejoin at the next line.</p>
      <p><strong>Read the English</strong> under each passage for its meaning. It is a plain rendering for understanding, not a word-for-word translation.</p>
      <p>Use the buttons in the bar below to hide the pinyin or the English, or to make the text larger.</p>
    </div>
  </div>
</section>

<section class="lt-day">
  <div class="lt-wrap">
    <ol>
      <li><a href="#morning"><span class="t">5:00 AM</span><span><div class="n">Morning Service</div><div class="s">早課 · The Sutra on Impermanence</div></span></a></li>
      <li><a href="#first"><span class="t">9:00 AM</span><span><div class="n">First Incense</div><div class="s">第一支香 · Amitābha Sutra, Praise of the Buddha, walking recitation</div></span></a></li>
      <li><a href="#noon"><span class="t">Midday</span><span><div class="n">Noon Offering</div><div class="s">午供 · The petition read before the Buddha</div></span></a></li>
      <li><a href="#afternoon1"><span class="t">1:30 PM</span><span><div class="n">Afternoon · First Incense</div><div class="s">下午第一支香 · Praise of the Buddha, walking recitation</div></span></a></li>
      <li><a href="#afternoon2"><span class="t">3:00 PM</span><span><div class="n">Afternoon · Second Incense</div><div class="s">下午第二支香 · Praise of the Buddha, walking recitation</div></span></a></li>
    </ol>
  </div>
</section>

<div class="lt-bar" id="ltBar">
  <div class="lt-bar-in">
    <a href="#morning">5:00</a>
    <a href="#first">9:00</a>
    <a href="#noon">Noon</a>
    <a href="#afternoon1">1:30</a>
    <a href="#afternoon2">3:00</a>
    <span class="sep"></span>
    <button type="button" id="ltPy" aria-pressed="true">Pinyin</button>
    <button type="button" id="ltEn" aria-pressed="true">English</button>
    <button type="button" id="ltSmaller" aria-label="Smaller text">A−</button>
    <button type="button" id="ltBigger" aria-label="Larger text">A+</button>
  </div>
</div>

<div id="ltBook">

<!-- ===== 5:00 MORNING ===== -->
<section class="lt-sess" id="morning">
  <div class="lt-wrap">
    <span class="time">5:00 AM</span>
    <h2>Morning Service</h2>
    <div class="zhsub">早課 · 佛說無常經</div>
    <p class="intro">The day begins before dawn with <em>The Sutra on Impermanence</em>, translated into Chinese by the Tang-dynasty monk Yijing (義淨). Its message is short and direct: everyone ages, falls ill, and dies — and it is exactly because of this that a Buddha appears in the world to teach. We chant it to begin the day awake to how precious the day is.</p>
__WUCHANG__
  </div>
</section>

<!-- ===== 9:00 FIRST INCENSE ===== -->
<section class="lt-sess" id="first">
  <div class="lt-wrap">
    <span class="time">9:00 AM</span>
    <h2>First Incense</h2>
    <div class="zhsub">第一支香 · 阿彌陀經 · 讚佛偈 · 繞佛</div>
    <p class="intro">A practice period is called a “stick of incense” (一支香), after the old way of timing a session by how long one stick takes to burn. The first one has three parts: we chant the <a href="#amitabha">Amitābha Sutra</a>, sing the <a href="#praise">Praise of the Buddha</a>, and then <a href="#walking">walk in a circle reciting the Buddha’s name</a>.</p>

    <div class="lt-text" id="amitabha">
      <h2>The Amitābha Sutra</h2>
      <div class="zhsub">佛說阿彌陀經 · 姚秦三藏法師鳩摩羅什譯</div>
      <p class="intro">Translated by Kumārajīva around 402 CE. The Buddha describes the Pure Land of Amitābha, explains how to be born there by holding the Buddha’s name with an undistracted mind, and tells how the Buddhas of every direction vouch for this teaching.</p>
__AMITUO__
    </div>

    <div class="lt-text" id="dharani">
      <h2>The Rebirth Dhāraṇī</h2>
      <div class="zhsub">往生咒 · 拔一切業障根本得生淨土陀羅尼 · 三遍</div>
      <p class="intro">Chanted three times after the sutra. A dhāraṇī is a string of Sanskrit sounds kept for its sound rather than translated; the Chinese characters only spell out the syllables. Its full title means “the dhāraṇī that pulls out karmic obstacles by the root and brings birth in the Pure Land.”</p>
__WANGSHENG__
    </div>

    <div class="lt-text" id="praise">
      <h2>Praise of the Buddha</h2>
      <div class="zhsub">讚佛偈</div>
      <p class="intro">Eight sung lines describing Amitābha Buddha, ending with a line of homage. The melody is slow; each character is held for several beats.</p>
__ZANFO__
    </div>

    <div class="lt-text" id="walking">
      <h2>Walking Recitation</h2>
      <div class="zhsub">繞佛 · 念佛</div>
      <p class="intro">After the praise we leave our places and walk slowly, clockwise and in single file, palms joined, reciting the Buddha’s name together. Follow the person in front of you. We begin with the six-syllable name and, as the pace quickens, shorten it to four syllables. When the bell signals, we return to our places and sit to continue reciting in stillness.</p>
      <div class="lt-seg">
        <div class="lt-zh">__NAMO__</div>
        <p class="lt-en">“Homage to Amitābha Buddha” — I take refuge in the Buddha of Infinite Light and Infinite Life.</p>
      </div>
      <div class="lt-seg">
        <div class="lt-zh">__AMITUOFO__</div>
        <p class="lt-en">“Amitābha Buddha” — the name alone, repeated with one mind.</p>
      </div>
    </div>

    <div class="lt-text" id="dedication">
      <h2>Dedication of Merit</h2>
      <div class="zhsub">迴向偈</div>
      <p class="intro">A session closes by giving away whatever good has come of it.</p>
__HUIXIANG__
    </div>
  </div>
</section>

<!-- ===== NOON OFFERING ===== -->
<section class="lt-sess" id="noon">
  <div class="lt-wrap">
    <span class="time">Midday</span>
    <h2>Noon Offering</h2>
    <div class="zhsub">午供 · 念佛祈安消災吉祥文疏</div>
    <p class="intro">Before the midday meal, food, flowers, and incense are offered to the Buddha. During the offering the Master reads aloud a formal petition (文疏) on behalf of everyone present: who we are, where we have gathered, what we have practiced today, and what we pray for.</p>
    <div class="lt-callout">
      <p><strong>No pinyin here.</strong> The Master reads this text in Taiwanese (Hokkien), not Mandarin, so Mandarin pinyin would not match what you hear. Simply listen, palms joined, and follow the meaning in English.</p>
    </div>
__SHUWEN__
  </div>
</section>

<!-- ===== 1:30 ===== -->
<section class="lt-sess" id="afternoon1">
  <div class="lt-wrap">
    <span class="time">1:30 PM</span>
    <h2>Afternoon · First Incense</h2>
    <div class="zhsub">下午第一支香 · 讚佛偈 · 繞佛</div>
    <p class="intro">The afternoon sessions are simpler. There is no sutra: we sing the Praise of the Buddha, then walk and sit reciting the Buddha’s name.</p>
    <div class="lt-callout">
      <p><strong>1.</strong> Praise of the Buddha (讚佛偈) &nbsp; <strong>2.</strong> Walking recitation (繞佛)</p>
      <a class="lt-jump" href="#praise">Go to the Praise of the Buddha ↑</a>
    </div>
  </div>
</section>

<!-- ===== 3:00 ===== -->
<section class="lt-sess" id="afternoon2">
  <div class="lt-wrap">
    <span class="time">3:00 PM</span>
    <h2>Afternoon · Second Incense</h2>
    <div class="zhsub">下午第二支香 · 讚佛偈 · 繞佛</div>
    <p class="intro">The same as the 1:30 session: the Praise of the Buddha, then walking and seated recitation, closing the day with the dedication of merit.</p>
    <div class="lt-callout">
      <p><strong>1.</strong> Praise of the Buddha (讚佛偈) &nbsp; <strong>2.</strong> Walking recitation (繞佛) &nbsp; <strong>3.</strong> Dedication of merit (迴向)</p>
      <a class="lt-jump" href="#praise">Go to the Praise of the Buddha ↑</a>
      <a class="lt-jump" href="#dedication">Go to the Dedication ↑</a>
    </div>
  </div>
</section>

</div>

<section class="lt-end">
  <div class="lt-wrap">
    <p>Chinese texts: <em>Foshuo Wuchang Jing</em> (Taishō 801) and <em>Foshuo Amituo Jing</em> (Taishō 366). The English renderings were prepared by Ru-Yi Meditation Center to convey the meaning for those chanting along; they are not word-for-word translations.</p>
    <p><a href="/community/dharma-events/">← Back to Dharma Events and this year’s dates</a></p>
  </div>
</section>

<script>
(function(){
  var book=document.getElementById('ltBook'),scale=1;
  function tog(id,cls){
    var b=document.getElementById(id);
    b.addEventListener('click',function(){
      var on=b.getAttribute('aria-pressed')==='true';
      b.setAttribute('aria-pressed',on?'false':'true');
      book.classList.toggle(cls,on);
    });
  }
  tog('ltPy','lt-nopy'); tog('ltEn','lt-noen');
  function size(d){scale=Math.min(1.6,Math.max(.8,scale+d));book.style.setProperty('--lt-scale',scale);}
  document.getElementById('ltBigger').addEventListener('click',function(){size(.15);});
  document.getElementById('ltSmaller').addEventListener('click',function(){size(-.15);});
})();
</script>
'''


def main():
    page = (PAGE
            .replace('__WUCHANG__', render_text(WUCHANG))
            .replace('__AMITUO__', render_text(AMITUO, AMITUO_READINGS))
            .replace('__WANGSHENG__', mantra_html())
            .replace('__ZANFO__', render_pairs(ZANFO))
            .replace('__HUIXIANG__', render_pairs(HUIXIANG))
            .replace('__SHUWEN__', shuwen_html())
            .replace('__NAMO__', NAMO)
            .replace('__AMITUOFO__', AMITUOFO))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(page)
    print('wrote', os.path.relpath(OUT, ROOT), len(page), 'bytes')


if __name__ == '__main__':
    main()
