#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the Four Hundred Characters course (Ru-Yi Academy, Layer 5).

Outputs:
  /courses/four-hundred-characters/index.html
  /courses/four-hundred-characters/session-1..4/index.html

Character ranks and occurrence counts are measured over the 1,482 texts tagged
三藏/經 in the Taisho canon (26,422,454 characters). See fh_freq.py.

Re-run after editing content:
    python3 scripts/fh_build.py
Idempotent — safe to run repeatedly.
"""
import os, io, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "courses", "four-hundred-characters")
CANON_TOTAL = 26422454

# --------------------------------------------------------------------------
# palette: ink, cinnabar (the red of seal paste and of 硃批 annotation), paper
# --------------------------------------------------------------------------
CSS = """<style>
  .fh{--ink:#1f1c18;--ink-mid:#3c362e;--ink-soft:#6f6659;
      --cinnabar:#b02e26;--cinnabar-deep:#7d1d18;--cinnabar-pale:#f0dfdb;
      --paper:#f8f3e8;--paper-deep:#efe7d6;--line:#e4dccb;--jade:#2f6d5e;
      --zh:'PingFang TC','Apple LiGothic Medium','Microsoft JhengHei',sans-serif;
      --zh-serif:'Songti TC','Apple LiSung','PingFang TC',serif;}
  .fh *{box-sizing:border-box;}
  .fh-wrap{max-width:760px;margin:0 auto;padding:0 26px;}
  .fh-wrap.wide{max-width:900px;}
  .fh .zh{font-family:var(--zh);}

  .js .fh [data-rv]{opacity:0;transform:translateY(20px);transition:opacity .75s cubic-bezier(.22,.61,.36,1),transform .75s cubic-bezier(.22,.61,.36,1);}
  .js .fh [data-rv].in{opacity:1;transform:none;}

  .fh-crumb{background:var(--paper);border-bottom:1px solid var(--line);}
  .fh-crumb .fh-wrap{padding:14px 26px;font-size:13.5px;color:var(--ink-soft);}
  .fh-crumb a{color:var(--cinnabar-deep);text-decoration:none;}
  .fh-crumb a:hover{text-decoration:underline;}

  .fh-hero{background:
      radial-gradient(120% 90% at 86% 8%,rgba(176,46,38,.26),transparent 60%),
      linear-gradient(158deg,#3c352c 0%,#282320 48%,#14120f 100%);color:#fff;}
  .fh-hero-in{max-width:760px;margin:0 auto;padding:56px 26px 50px;}
  .fh-eyebrow{font-size:12.5px;letter-spacing:.22em;text-transform:uppercase;color:#e0a59c;font-weight:600;}
  .fh-hero h1{font-family:'Playfair Display',serif;font-weight:600;font-size:clamp(30px,5vw,48px);line-height:1.1;margin:12px 0 10px;}
  .fh-hero .subt{font-style:italic;font-size:18px;color:#ded6c8;}
  .fh-hero .lede{font-size:17px;line-height:1.7;color:#cfc7b8;margin:16px 0 0;max-width:58ch;}
  .fh-hero .rd{margin-top:24px;font-size:14px;color:#bfb6a6;display:flex;flex-wrap:wrap;gap:8px 18px;}
  .fh-hero .rd b{color:#e0a59c;}
  .fh-hero-zh{font-family:var(--zh-serif);font-size:clamp(17px,3.9vw,26px);line-height:1.9;
    letter-spacing:.04em;color:#fff;margin:26px 0 0;}
  .fh-hero-gloss{font-style:italic;color:#a9a091;font-size:14.5px;line-height:1.65;margin:10px 0 0;max-width:60ch;}

  .fh-body{background:#fff;padding:44px 0 30px;}
  .fh-body p{font-size:17.5px;line-height:1.78;color:var(--ink-mid);margin:0 0 20px;}
  .fh-body.paper{background:var(--paper);}

  .fh-part{margin:52px 0 22px;padding-top:26px;border-top:2px solid var(--line);}
  .fh-part:first-child{margin-top:0;padding-top:0;border-top:0;}
  .fh-part .pn{font-size:12px;letter-spacing:.2em;text-transform:uppercase;font-weight:800;color:var(--cinnabar);}
  .fh-part h2{font-family:'Playfair Display',serif;font-size:clamp(24px,3.8vw,32px);color:var(--ink);margin:6px 0 0;line-height:1.14;}
  .fh-part h2 .rf{display:block;font-size:15px;font-style:italic;font-weight:400;color:var(--ink-soft);margin-top:5px;}

  /* stat band */
  .fh-stats{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
    grid-template-columns:repeat(auto-fit,minmax(150px,1fr));margin:0 0 24px;}
  .fh-stat{background:#fff;padding:18px 16px;}
  .fh-stat b{display:block;font-family:'Playfair Display',serif;font-size:28px;line-height:1.05;
    color:var(--cinnabar-deep);font-variant-numeric:tabular-nums;}
  .fh-stat span{display:block;font-size:12.5px;color:var(--ink-soft);margin-top:6px;line-height:1.45;}

  /* character tiles */
  .fh-tiles{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 10px;padding:0;list-style:none;}
  .fh-tile{all:unset;cursor:pointer;display:flex;flex-direction:column;align-items:center;
    width:74px;padding:10px 4px 8px;background:var(--paper);border:1px solid var(--line);
    transition:border-color .15s,transform .15s;}
  .fh-tile:hover{border-color:var(--cinnabar);transform:translateY(-1px);}
  .fh-tile:focus-visible{outline:2px solid var(--cinnabar);outline-offset:2px;}
  .fh-tile .ch{font-family:var(--zh-serif);font-size:32px;line-height:1.15;color:var(--ink);}
  .fh-tile .rk{font-size:10.5px;color:var(--ink-soft);font-variant-numeric:tabular-nums;letter-spacing:.03em;}
  .fh-tile[aria-expanded="true"]{border-color:var(--cinnabar);background:var(--cinnabar-pale);}
  .fh-tile.block .ch{color:var(--ink-soft);}

  .fh-card{border:1px solid var(--line);border-left:3px solid var(--cinnabar);background:var(--paper);
    padding:16px 18px;margin:0 0 20px;}
  .fh-card h3{font-family:'Playfair Display',serif;font-size:20px;color:var(--ink);margin:0 0 4px;line-height:1.3;}
  .fh-card .chb{font-family:var(--zh-serif);font-size:26px;color:var(--cinnabar-deep);margin-right:9px;}
  .fh-card p{font-size:15px;line-height:1.65;margin:6px 0 0;}
  .fh-card dl{margin:12px 0 0;display:grid;grid-template-columns:auto 1fr;gap:2px 14px;font-size:13.5px;}
  .fh-card dt{color:var(--ink-soft);}
  .fh-card dd{margin:0;font-variant-numeric:tabular-nums;color:var(--ink-mid);}
  .fh-hint{font-size:13.5px;color:var(--ink-soft);font-style:italic;}

  /* scripture box */
  .fh-frame{font-family:var(--zh-serif);font-size:clamp(17px,3.5vw,23px);line-height:2.05;
    letter-spacing:.03em;background:var(--paper);border:1px solid var(--line);
    border-left:3px solid var(--cinnabar);padding:22px 20px;color:var(--ink);}
  .fh-frame.center{text-align:center;}
  .fh-fixed{color:var(--ink);}
  .fh-slot{color:var(--cinnabar-deep);border-bottom:2px solid var(--cinnabar);padding-bottom:1px;}
  .fh-en{font-size:15px;color:var(--ink-soft);font-style:italic;line-height:1.66;margin:14px 0 0;}
  .fh-swap{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 0;padding:0;list-style:none;}
  .fh-swap button{all:unset;cursor:pointer;font-size:13px;font-weight:600;padding:7px 14px;
    border:1px solid var(--line);border-radius:999px;color:var(--ink-mid);background:#fff;transition:all .15s;}
  .fh-swap button:hover{border-color:var(--cinnabar);color:var(--cinnabar-deep);}
  .fh-swap button:focus-visible{outline:2px solid var(--cinnabar);outline-offset:2px;}
  .fh-swap button[aria-pressed="true"]{background:var(--ink);color:#fff;border-color:var(--ink);}

  /* side-by-side comparison */
  .fh-twins{display:grid;gap:14px;margin:22px 0 0;}
  .fh-twin{background:#fff;border:1px solid var(--line);padding:18px 20px;}
  .fh-body.paper .fh-twin{background:#fff;}
  .fh-twin .who{font-size:11.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;
    color:var(--ink-soft);margin:0 0 10px;}
  .fh-twin .txt{font-family:var(--zh-serif);font-size:clamp(16px,3.2vw,20px);line-height:1.95;
    letter-spacing:.03em;color:var(--ink);margin:0;}
  .fh-twin .txt.full{font-size:clamp(15px,2.9vw,18px);line-height:2.05;}
  .fh mark{background:var(--cinnabar-pale);color:var(--cinnabar-deep);padding:0 3px;font-weight:600;}

  /* exercises */
  .fh-ex{border-top:1px solid var(--line);padding-top:20px;margin-top:20px;}
  .fh-ex:first-of-type{border-top:0;padding-top:0;margin-top:0;}
  .fh-ex .q{font-family:var(--zh-serif);font-size:20px;line-height:1.9;letter-spacing:.03em;
    color:var(--ink);margin:0 0 12px;}
  .fh-reveal{all:unset;cursor:pointer;font-size:12.5px;font-weight:700;letter-spacing:.08em;
    text-transform:uppercase;color:var(--cinnabar-deep);border-bottom:1px solid var(--cinnabar);padding-bottom:1px;}
  .fh-reveal:focus-visible{outline:2px solid var(--cinnabar);outline-offset:3px;}
  .fh-ans{margin-top:14px;border-left:2px solid var(--jade);padding-left:14px;}
  .fh-ans p{font-size:15.5px;margin:0 0 8px;}
  .fh-ans p:last-child{margin-bottom:0;}
  .fh-ans .sm{font-size:14px;color:var(--ink-soft);}

  /* tables */
  .fh-tscroll{overflow-x:auto;margin:22px 0 0;}
  .fh table{width:100%;border-collapse:collapse;font-size:14.5px;}
  .fh th,.fh td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);color:var(--ink-mid);}
  .fh th{font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);font-weight:700;}
  .fh td.n{text-align:right;font-variant-numeric:tabular-nums;}
  .fh td.zh{font-family:var(--zh);font-size:16px;}

  /* session list on the index */
  .fh-sess{display:grid;gap:14px;margin:24px 0 0;padding:0;list-style:none;}
  .fh-sesscard{border:1px solid var(--line);background:#fff;padding:20px 22px;display:block;
    text-decoration:none;transition:border-color .15s,transform .15s;}
  .fh-sesscard:hover{border-color:var(--cinnabar);transform:translateY(-1px);}
  .fh-sesscard .sn{font-size:11.5px;letter-spacing:.18em;text-transform:uppercase;font-weight:800;color:var(--cinnabar);}
  .fh-sesscard h3{font-family:'Playfair Display',serif;font-size:22px;color:var(--ink);margin:6px 0 4px;line-height:1.2;}
  .fh-sesscard .zht{font-family:var(--zh);font-size:14.5px;color:var(--ink-soft);margin:0 0 8px;}
  .fh-sesscard p{font-size:15px;line-height:1.6;color:var(--ink-mid);margin:0;}

  /* prev / next */
  .fh-nav{border-top:2px solid var(--line);margin-top:48px;padding:26px 0 0;
    display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between;}
  .fh-nav a{font-size:14.5px;color:var(--cinnabar-deep);text-decoration:none;font-weight:600;}
  .fh-nav a:hover{text-decoration:underline;}
  .fh-nav .sp{color:var(--ink-soft);font-weight:400;}

  .fh-note{background:var(--paper-deep);border:1px solid var(--line);padding:18px 20px;margin:24px 0 0;}
  .fh-note h4{font-family:'Playfair Display',serif;font-size:18px;color:var(--ink);margin:0 0 6px;}
  .fh-note p{font-size:15px;line-height:1.66;margin:0;}

  .fh-method{background:var(--ink);color:#b8afa0;padding:36px 0 40px;}
  .fh-method h4{font-family:'Playfair Display',serif;font-size:19px;color:#fff;margin:0 0 10px;}
  .fh-method p{font-size:14.5px;line-height:1.7;margin:0 0 12px;max-width:66ch;}
  .fh-method code{font-size:13px;color:#e0a59c;}
  .fh-method a{color:#e0a59c;}

  @media (prefers-reduced-motion:reduce){.fh *{transition:none !important;}}
</style>"""

# --------------------------------------------------------------------------
# character data — rank and occurrences in the sutra canon
# --------------------------------------------------------------------------
CH = {
 "如":(4,347740,"thus, like, in accordance with","Half of 如是. Also the 如 of 如來, Tathāgata."),
 "是":(3,367401,"this; to be","Third most common character in the canon."),
 "我":(33,140942,"I, me","Ānanda's I. Later, the self the teaching dismantles."),
 "聞":(93,66260,"to hear, to have heard","Hearing, not reading."),
 "一":(5,327176,"one, a single",""),
 "時":(30,142112,"time, occasion","一時 = on one occasion."),
 "佛":(8,279420,"Buddha","Short for 佛陀, a transliteration of buddha."),
 "在":(104,60593,"to be at, to be located in","Swaps with 住 across recensions."),
 "舍":(164,39250,"[sound only] śrā-; also: dwelling","Phonetic here. Its ordinary sense is a house."),
 "衛":(672,4956,"[sound only] -vastī","Rare outside place names. Do not drill it."),
 "國":(212,29259,"country, land, city-state",""),
 "祇":(514,8317,"[sound only] Jeta","The prince who owned the grove."),
 "樹":(294,18680,"tree, grove","祇樹 = Jeta's grove."),
 "給":(686,4689,"to give, to provide","Sense, not sound — part of a translated name."),
 "孤":(836,3038,"orphaned, parentless","Rarest character in the sentence."),
 "獨":(380,13576,"alone, solitary","給孤獨 = the giver to the orphaned and solitary."),
 "園":(552,6912,"park, garden",""),
 "與":(142,42286,"together with","Opens the assembly clause."),
 "大":(20,188034,"great, large",""),
 "比":(144,41949,"[sound only] bhi-",""),
 "丘":(173,37774,"[sound only] -kṣu","比丘 = bhikṣu, a fully ordained monk."),
 "眾":(35,139035,"assembly, multitude, community","Alternates with 僧 (saṅgha) in this slot."),
 "千":(161,39758,"thousand",""),
 "二":(29,149754,"two",""),
 "百":(180,36256,"hundred","千二百五十 = 1,250."),
 "五":(105,60469,"five",""),
 "十":(44,119354,"ten",""),
 "人":(32,141119,"person, people",""),
 "俱":(333,16048,"all together, all present","Closes the clause. Chinese has no plural ending; 俱 does the work."),
 "爾":(116,53068,"that, thereupon","Almost only ever seen in 爾時."),
 "世":(25,162306,"world, age",""),
 "尊":(67,95003,"honored, venerable","世尊 = World-Honored One, the Buddha."),
 "告":(232,26799,"to tell, to address [downward]","The Buddha 告 a disciple. Never the reverse."),
 "白":(187,35104,"to address respectfully [upward]","A disciple 白 the Buddha. Its plain sense is white."),
 "言":(36,136909,"to say; words","Closes a speech formula: …告…言."),
 "問":(267,21996,"to ask",""),
 "答":(378,13716,"to answer",""),
 "何":(41,126627,"what, why","何以故 = why is that?"),
 "故":(17,209111,"reason, cause; therefore","Both the question and the answer hinge on it."),
 "復":(55,105773,"again, further","復次 = furthermore, the canon's paragraph break."),
 "次":(158,40044,"next, in order",""),
 "從":(135,43635,"from",""),
 "座":(466,9919,"seat",""),
 "起":(179,36338,"to rise",""),
 "合":(101,61876,"to join, to put together",""),
 "掌":(520,7988,"palm of the hand","合掌 = palms joined, añjali."),
 "恭":(492,9004,"reverent",""),
 "敬":(306,17730,"respectful","恭敬 = reverently."),
 "無":(1,528802,"there is not; without","The single most common character in the canon."),
 "不":(2,432503,"not [before a verb]","Second most common."),
 "非":(77,77968,"is not; other than [before a noun]","The third negation, and the sharpest."),
 "空":(46,115605,"empty, emptiness","śūnya. Not nothingness."),
 "色":(102,61394,"form, matter; color","rūpa, the first of the five aggregates."),
 "若":(11,251669,"if; whether … or","Lists alternatives: 若…若…若…"),
 "有":(7,283671,"to have; there is","The opposite pole to 無."),
 "相":(51,112606,"characteristic, mark, appearance","lakṣaṇa. What a thing presents itself as."),
 "想":(159,40032,"perception, conception",""),
 "即":(82,75273,"precisely, is exactly","即是 = is precisely. 即非 = is precisely not."),
 "實":(168,38311,"in reality, actually",""),
 "得":(21,183260,"to obtain, to attain",""),
 "者":(16,219596,"the one who …","Turns a verb into its agent."),
 "量":(113,54705,"measure","無量 = immeasurable."),
 "數":(221,27909,"number","無數 = countless."),
 "邊":(258,22796,"edge, limit","無邊 = boundless."),
 "滅":(129,46053,"to extinguish, to cease",""),
 "度":(257,22996,"to cross over, to liberate","滅度 = to bring to final release."),
 "觀":(114,54256,"to contemplate, to observe","觀自在 = Contemplating Freely, Xuanzang's Avalokiteśvara."),
 "自":(65,96269,"self, oneself",""),
 "行":(26,160571,"to practice; conduct","Also the 行 of the five aggregates."),
 "深":(219,28337,"deep, profound",""),
 "般":(115,53890,"[sound only] pra-","般若 = prajñā, wisdom."),
 "波":(70,85485,"[sound only] pā-",""),
 "羅":(22,174549,"[sound only] -ra-","One of the busiest phonetic characters in the canon."),
 "蜜":(84,72781,"[sound only] -mitā","波羅蜜多 = pāramitā, perfection."),
 "多":(54,106479,"many; [sound only] -tā",""),
 "照":(396,12705,"to illuminate, to see clearly",""),
 "見":(57,104615,"to see",""),
 "蘊":(774,3605,"aggregate, heap","skandha. Rare as a character; always this term."),
 "皆":(92,68491,"all, in every case",""),
 "苦":(126,47619,"suffering","duḥkha."),
 "厄":(1227,1262,"distress, calamity","Rare. Appears here and little else."),
 "子":(47,114931,"child; son","舍利子 = Śāriputra, in Xuanzang's rendering."),
 "利":(94,65917,"benefit; [sound only] -ri-",""),
 "異":(259,22781,"different from",""),
 "受":(69,85760,"sensation, feeling","vedanā, the second aggregate."),
 "識":(156,40148,"consciousness","vijñāna, the fifth aggregate."),
 "諸":(9,260196,"all, the various","Marks a plural. No plural ending exists."),
 "法":(6,285068,"dharma — teaching, thing, phenomenon","Sixth most common character, and the hardest to translate."),
 "垢":(453,10353,"defiled, stained",""),
 "淨":(24,165488,"pure, clean",""),
 "增":(227,27114,"to increase",""),
 "減":(652,5218,"to decrease",""),
 "眼":(193,33873,"eye",""),
 "耳":(293,18778,"ear",""),
 "鼻":(337,15830,"nose",""),
 "舌":(343,15438,"tongue",""),
 "身":(60,99267,"body",""),
 "意":(99,62812,"mind, mental faculty","The sixth sense organ in Buddhist reckoning."),
 "聲":(150,41196,"sound",""),
 "香":(200,32180,"scent",""),
 "味":(387,13263,"taste",""),
 "觸":(203,31242,"touch",""),
 "界":(48,114329,"realm, field, sphere","dhātu. 眼界 = the field of the eye."),
 "乃":(106,59163,"and so; thereupon","乃至 = and so on up to."),
 "至":(74,81883,"to reach, up to",""),
 "明":(108,57121,"bright; clarity","無明 = ignorance, avidyā."),
 "盡":(205,30964,"to exhaust, to end",""),
 "老":(475,9530,"old, aging",""),
 "死":(224,27417,"death","老死 = aging and death."),
 "集":(283,20197,"to gather; arising","The second noble truth."),
 "道":(81,75432,"path, way","The fourth noble truth."),
 "智":(39,131524,"knowledge, wisdom",""),
 "埵":(846,2950,"[sound only] -tva","菩提薩埵 = bodhisattva, written out in full."),
 "依":(256,23002,"to rely on, in dependence on",""),
 "罣":(1336,1011,"obstruction, snag","Rare. 罣礙 = hindrance."),
 "礙":(367,14000,"obstacle",""),
 "恐":(662,5100,"fear",""),
 "怖":(460,10264,"terror","恐怖 = dread."),
 "遠":(272,21621,"far, to keep far from",""),
 "離":(95,64929,"to leave, to be free of","遠離 = to leave far behind."),
 "顛":(740,4001,"upside down",""),
 "倒":(623,5628,"inverted","顛倒 = topsy-turvy, delusion."),
 "夢":(627,5578,"dream",""),
 "究":(558,6851,"to investigate; ultimate",""),
 "竟":(312,17444,"end, finally","究竟 = ultimate, final."),
 "涅":(339,15627,"[sound only] nir-",""),
 "槃":(338,15826,"[sound only] -vāṇa","涅槃 = nirvāṇa."),
 "三":(28,153039,"three",""),
 "神":(148,41456,"divine, numinous",""),
 "上":(71,85189,"above, supreme","無上 = unsurpassed."),
 "等":(40,131274,"equal; and so on","無等等 = unequalled among equals."),
 "能":(53,106732,"to be able to",""),
 "除":(281,20449,"to remove",""),
 "真":(117,52947,"true, real",""),
 "虛":(229,26911,"empty, hollow, false","不虛 = not false."),
 "說":(31,141862,"to speak, to expound",""),
 "曰":(124,49492,"says, as follows",""),
 "菩":(13,236338,"[sound only] bo-",""),
 "薩":(10,257588,"[sound only] -dhi-sattva","菩薩 is short for 菩提薩埵."),
 "提":(87,72003,"[sound only] -dhi",""),
 "阿":(85,72608,"[sound only] a-",""),
 "耨":(436,11111,"[sound only] -nu-",""),
 "藐":(456,10289,"[sound only] -myak-","阿耨多羅三藐三菩提 = anuttara-samyak-saṃbodhi."),
 "咒":(3627,31,"spell, incantation","See the note on 呪 — this form is the rare one."),
 "揭":(1287,1100,"[sound only] ga-","Pure sound: the mantra is not translated at all."),
 "帝":(366,14167,"[sound only] -te",""),
 "僧":(381,13573,"[sound only] saṃ-; also: monastic community",""),
 "莎":(676,4813,"[sound only] svā-",""),
 "訶":(80,76065,"[sound only] -hā",""),
}


def data_js(chars):
    seen, out = set(), []
    for c in chars:
        if c in seen or c not in CH:
            continue
        seen.add(c)
        r, n, en, note = CH[c]
        out.append('"%s":{r:%d,n:%d,en:%s,note:%s}' % (c, r, n, json.dumps(en), json.dumps(note)))
    return "{" + ",".join(out) + "}"


JS = """<script>
(function(){
  "use strict";
  document.documentElement.classList.add('js');
  var DATA = __DATA__;
  var GROUPS = __GROUPS__;

  function fmt(n){ return n.toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, ","); }

  function render(cardEl, ch){
    var d = DATA[ch]; if(!d) return;
    var pct = d.n / __TOTAL__ * 100;
    cardEl.innerHTML = '<div class="fh-card">'
      + '<h3><span class="chb" lang="zh-Hant">' + ch + '</span>' + d.en + '</h3>'
      + (d.note ? '<p>' + d.note + '</p>' : '')
      + '<dl><dt>Rank in the sutras</dt><dd>#' + d.r + '</dd>'
      + '<dt>Times it occurs</dt><dd>' + fmt(d.n) + '</dd>'
      + '<dt>Share of the canon</dt><dd>' + (pct < 0.02 ? pct.toFixed(3) : pct.toFixed(2)) + '%</dd>'
      + '</dl></div>';
  }

  GROUPS.forEach(function(g){
    var host = document.getElementById(g.host), card = document.getElementById(g.card);
    if(!host || !card) return;
    g.chars.split("").forEach(function(ch){
      var d = DATA[ch]; if(!d) return;
      var li = document.createElement("li");
      var b = document.createElement("button");
      b.type = "button";
      b.className = "fh-tile" + ((g.dim||"").indexOf(ch) > -1 ? " block" : "");
      b.setAttribute("aria-expanded","false");
      b.innerHTML = '<span class="ch" lang="zh-Hant">' + ch + '</span><span class="rk">#' + d.r + '</span>';
      b.addEventListener("click", function(){
        Array.prototype.forEach.call(host.querySelectorAll(".fh-tile"), function(t){
          t.setAttribute("aria-expanded","false");
        });
        b.setAttribute("aria-expanded","true");
        render(card, ch);
      });
      li.appendChild(b); host.appendChild(li);
    });
  });

  Array.prototype.forEach.call(document.querySelectorAll(".fh-reveal"), function(btn){
    btn.addEventListener("click", function(){
      var ans = btn.parentNode.querySelector(".fh-ans"); if(!ans) return;
      var open = ans.hidden === false;
      ans.hidden = open;
      btn.setAttribute("aria-expanded", String(!open));
      btn.textContent = open ? "Reveal" : "Hide";
    });
  });

  var swap = document.querySelectorAll(".fh-swap button");
  if(swap.length){
    var sv=document.getElementById("s-verb"), sp=document.getElementById("s-place"),
        sn=document.getElementById("s-num"), fe=document.getElementById("frame-en");
    Array.prototype.forEach.call(swap, function(b){
      b.addEventListener("click", function(){
        Array.prototype.forEach.call(swap, function(o){ o.setAttribute("aria-pressed","false"); });
        b.setAttribute("aria-pressed","true");
        if(sv) sv.textContent = b.getAttribute("data-v");
        if(sp) sp.textContent = b.getAttribute("data-p");
        if(sn) sn.textContent = b.getAttribute("data-n");
        if(fe) fe.textContent = b.getAttribute("data-en");
      });
    });
  }

  GROUPS.forEach(function(g){
    var host = document.getElementById(g.host);
    if(host){ var first = host.querySelector(".fh-tile"); if(first) first.click(); }
  });

  /* scroll reveal — same behavior as the other Academy courses */
  var rv = Array.prototype.slice.call(document.querySelectorAll('.fh [data-rv]'));
  var ticking = false;
  function sweep(){
    ticking = false;
    var vh = window.innerHeight || document.documentElement.clientHeight;
    for (var i = rv.length - 1; i >= 0; i--){
      var r = rv[i].getBoundingClientRect();
      if (r.top < vh * 0.92){ rv[i].classList.add('in'); rv.splice(i,1); }
    }
  }
  function onScroll(){ if(!ticking){ ticking = true; requestAnimationFrame(sweep); } }
  window.addEventListener('scroll', onScroll, {passive:true});
  window.addEventListener('resize', onScroll);
  window.addEventListener('pageshow', sweep);
  document.addEventListener('visibilitychange', function(){ if(!document.hidden){ sweep(); } });
  sweep();
})();
</script>"""


METHOD = """
  <section class="fh-method">
    <div class="fh-wrap">
      <h4>Where the numbers come from</h4>
      <p>Every frequency on this page was counted, not estimated. The corpus is the 1,482 texts tagged
        <code>三藏/經</code> in the Taishō canon — 26,422,454 Chinese characters after stripping front
        matter, headings, and the CBETA apparatus. Ranks are positions in the frequency list built from
        that corpus; formula counts are string occurrences, given with the number of separate sutras they
        appear in, because a formula used 10,000 times in one text is a quirk while one used in 700 texts
        is a convention.</p>
      <p>Counting scripture separately from commentary matters. Run the same analysis over a corpus that
        includes the śāstras and the vocabulary tilts hard toward Abhidharma technical terms, and the
        character list ends up teaching you to read treatises rather than sutras. This course teaches
        sutras first. On how Ru-Yi translates and why, see
        <a href="{{ '/dharma/translation-method/' | relative_url }}">Translation Method</a>.</p>
    </div>
  </section>
"""


def crumb(label):
    return ('\n  <nav class="fh-crumb"><div class="fh-wrap">'
            '<a href="{{ \'/courses/\' | relative_url }}">Ru-Yi Academy</a> → '
            '<a href="{{ \'/courses/four-hundred-characters/\' | relative_url }}">Four Hundred Characters</a>'
            ' → %s</div></nav>\n' % label)


def nav(prev, nxt):
    left = ('<a href="{{ \'%s\' | relative_url }}">← %s</a>' % prev) if prev else '<span class="sp">Start of the course</span>'
    right = ('<a href="{{ \'%s\' | relative_url }}">%s →</a>' % nxt) if nxt else \
            '<a href="{{ \'/courses/\' | relative_url }}">Back to the Academy →</a>'
    return '\n      <div class="fh-nav">%s%s</div>\n' % (left, right)


def write(relpath, front, body, groups):
    chars = "".join(g["chars"] for g in groups)
    js = (JS.replace("__DATA__", data_js(chars))
            .replace("__GROUPS__", json.dumps(groups, ensure_ascii=False))
            .replace("__TOTAL__", str(CANON_TOTAL)))
    doc = front + "\n" + CSS + "\n\n<div class=\"fh\">\n" + body + "\n</div>\n\n" + js + "\n"
    path = os.path.join(OUT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(doc)
    missing = sorted(set(c for c in chars if c not in CH))
    bad = "{{" in doc.replace("{{ '", "\x00").replace("{{ site", "\x00")
    return relpath, len(set(chars)), missing, bad


def fm(title, permalink, excerpt):
    return ('---\nlayout: default\ntitle: "%s"\npermalink: %s\nexcerpt: %s\n---'
            % (title, permalink, excerpt))


# ==========================================================================
# course index
# ==========================================================================
IDX_BODY = """
  <nav class="fh-crumb"><div class="fh-wrap"><a href="{{ '/courses/' | relative_url }}">Ru-Yi Academy</a> &rarr; Four Hundred Characters</div></nav>

  <section class="fh-hero">
    <div class="fh-hero-in">
      <div class="fh-eyebrow">Layer 5 &middot; Read the original</div>
      <h1>Four Hundred Characters</h1>
      <div class="subt">四百字讀經 &middot; four sessions</div>
      <p class="lede">The Academy's first five layers &mdash; 0 through 4 &mdash; taught you the Dharma in English, from texts translated on this site. This layer teaches you to read those texts in Chinese &mdash; not fluently, and not all of them, but enough that a bilingual page becomes something you read rather than something you admire.</p>
      <div class="rd">
        <span><b>Assumes</b> no Chinese at all</span>
        <span><b>You will not</b> write, speak, or listen &mdash; only read</span>
        <span><b>By the end</b> one complete sutra, in the original</span>
      </div>
    </div>
  </section>

  <div class="fh-body">
    <div class="fh-wrap">

      <div class="fh-part"><div class="pn">The premise</div><h2>Buddhist Chinese is a small language</h2></div>

      <p data-rv>To read a Chinese newspaper you need something like three thousand characters. Scripture is not a newspaper. It is a closed body of translated text, produced by a handful of workshops over roughly a thousand years, and it repeats itself relentlessly &mdash; which is precisely what makes it learnable by an adult with an hour a week.</p>

      <p data-rv>We counted every sutra in the Taishō canon &mdash; 1,482 texts, 26,422,454 characters &mdash; and built the frequency list. Here is what it says.</p>

      <div class="fh-stats" data-rv>
        <div class="fh-stat"><b>26.4M</b><span>characters of scripture</span></div>
        <div class="fh-stat"><b>7,549</b><span>distinct characters used</span></div>
        <div class="fh-stat"><b>576</b><span>characters to cover 90%</span></div>
        <div class="fh-stat"><b>90</b><span>characters to cover half</span></div>
      </div>

      <div class="fh-tscroll" data-rv>
        <table>
          <thead><tr><th>Learn this many characters</th><th class="n">and you can read</th></tr></thead>
          <tbody>
            <tr><td>90</td><td class="n">50.0%</td></tr>
            <tr><td>328</td><td class="n">80.0%</td></tr>
            <tr><td>400</td><td class="n">83.9%</td></tr>
            <tr><td>576</td><td class="n">90.0%</td></tr>
            <tr><td>887</td><td class="n">95.0%</td></tr>
            <tr><td>1,824</td><td class="n">99.0%</td></tr>
          </tbody>
        </table>
      </div>

      <p data-rv style="margin-top:22px">The course is named for the four hundred mark. That is not a finish line &mdash; it is the point where a page of scripture stops being a wall and becomes a text with gaps in it, which is a completely different situation to be in.</p>

      <div class="fh-part"><div class="pn">The method</div><h2>Formulas, not flashcards</h2></div>

      <p data-rv>Nobody reads a sutra character by character, and this course does not ask you to start that way. Scripture is built from fixed blocks &mdash; an opening frame, a speech formula, a gesture of respect, a transliterated Sanskrit name &mdash; that recur unchanged across hundreds of texts with a few variable slots. You learn the block, and the variable slots are where your attention goes.</p>

      <p data-rv>This also solves the problem that stops most beginners. Scripture's rarest characters almost never appear alone; they arrive inside those blocks. <span class="zh">祇樹給孤獨園</span> contains four characters you would meet almost nowhere else, and you will never need to know them individually. Your four hundred characters get spent on connective tissue instead.</p>

      <div class="fh-part"><div class="pn">The sessions</div><h2>Four sittings, one sutra at the end</h2></div>

      <p data-rv>Sessions 1 to 3 walk straight down the opening of a single text, the Diamond Sutra, in order &mdash; because the only honest way to learn to read scripture is to read some. Session 4 changes texts and reads the Heart Sutra entire.</p>

      <ul class="fh-sess">
        <li data-rv><a class="fh-sesscard" href="{{ '/courses/four-hundred-characters/session-1/' | relative_url }}">
          <div class="sn">Session 1</div>
          <h3>How Every Sutra Opens</h3>
          <p class="zht">如是我聞：一時，佛在舍衛國祇樹給孤獨園</p>
          <p>The formula that opens four in every ten sutras in the canon &mdash; and why the same twenty-two characters begin both the Diamond Sutra and the Amitabha Sutra, one character apart.</p>
        </a></li>
        <li data-rv><a class="fh-sesscard" href="{{ '/courses/four-hundred-characters/session-2/' | relative_url }}">
          <div class="sn">Session 2</div>
          <h3>At That Time, the World-Honored One</h3>
          <p class="zht">爾時，世尊告……言</p>
          <p>The canon gives you no quotation marks and no tenses, yet you can always tell who addressed whom. Speech in Classical Chinese carries its social direction in the verb.</p>
        </a></li>
        <li data-rv><a class="fh-sesscard" href="{{ '/courses/four-hundred-characters/session-3/' | relative_url }}">
          <div class="sn">Session 3</div>
          <h3>The Grammar of Not</h3>
          <p class="zht">無 &middot; 不 &middot; 非</p>
          <p>The most common character in the Buddhist canon is <span class="zh">無</span>. The second is <span class="zh">不</span>. Three negations, three different jobs, and the distinction between them is the highest-yield hour in the course.</p>
        </a></li>
        <li data-rv><a class="fh-sesscard" href="{{ '/courses/four-hundred-characters/session-4/' | relative_url }}">
          <div class="sn">Session 4</div>
          <h3>Two Hundred Sixty Characters</h3>
          <p class="zht">般若波羅蜜多心經</p>
          <p>The Heart Sutra is 260 characters long and uses only 117 distinct ones. You read all of it, in order, to the last syllable of the mantra. Nothing is summarized.</p>
        </a></li>
      </ul>

      <div class="fh-note" data-rv>
        <h4>What this course does not claim</h4>
        <p>It will not make you fluent, it does not teach you to write or speak, and it covers four sessions of a subject that could fill forty. What it gives you is the threshold where the Chinese column of a bilingual page becomes usable: you read the original, get most of it, and check the English for the rest &mdash; instead of reading the English and glancing respectfully at the Chinese. Every translation on this site is laid out for exactly that.</p>
      </div>

    </div>
  </div>
"""

# ==========================================================================
# sessions
# ==========================================================================
S1_GROUPS = [
    {"host":"frame-tiles","card":"frame-card","chars":"如是我聞一時佛在","dim":""},
    {"host":"place-tiles","card":"place-card","chars":"舍衛國祇樹給孤獨園","dim":"衛給孤祇園"},
    {"host":"asm-tiles","card":"asm-card","chars":"與大比丘眾千二百五十人俱","dim":""},
]

S1_BODY = crumb("Session 1") + """
  <section class="fh-hero">
    <div class="fh-hero-in">
      <div class="fh-eyebrow">Session 1 &middot; The opening frame</div>
      <h1>How Every Sutra Opens</h1>
      <p class="lede">By the end of this session you will have read the first sentence of the Diamond Sutra in Chinese &mdash; not a translation of it, the sentence itself. The same sentence opens the Amitabha Sutra almost character for character.</p>
      <p class="fh-hero-zh" lang="zh-Hant">如是我聞：一時，佛在舍衛國祇樹給孤獨園，<br>與大比丘眾千二百五十人俱。</p>
      <p class="fh-hero-gloss">Thus have I heard. At one time, the Buddha was in the land of Śrāvastī, in Jeta's Grove, the Park of the Giver to the Orphaned and Solitary, together with a great assembly of bhikṣus, one thousand two hundred fifty in all.</p>
    </div>
  </section>

  <div class="fh-body">
    <div class="fh-wrap">

      <div class="fh-part"><div class="pn">Part 1</div><h2>Read the frame, then the filling</h2></div>

      <p data-rv>Scripture is built from formulas &mdash; fixed blocks that recur across hundreds of texts with a few variable slots. Learn one formula and you have the opening of half the canon. Tap a sutra below to drop its own details into the slots.</p>

      <div class="fh-frame" lang="zh-Hant" data-rv><span class="fh-fixed">如是我聞：一時，佛</span><span class="fh-slot" id="s-verb">在</span><span class="fh-slot" id="s-place">舍衛國祇樹給孤獨園</span><span class="fh-fixed">，與大比丘眾</span><span class="fh-slot" id="s-num">千二百五十人</span><span class="fh-fixed">俱。</span></div>
      <ul class="fh-swap" data-rv>
        <li><button type="button" data-v="在" data-p="舍衛國祇樹給孤獨園" data-n="千二百五十人" data-en="&hellip;was in the land of Śrāvastī, in Jeta's Grove, the Park of the Giver to the Orphaned and Solitary, together with a great assembly of bhikṣus, 1,250 in all." aria-pressed="true">Diamond Sutra 金剛經</button></li>
        <li><button type="button" data-v="在" data-p="舍衛國祇樹給孤獨園" data-n="千二百五十人" data-en="Identical — except that this text writes the assembly as 比丘僧 rather than 比丘眾. One character apart." aria-pressed="false">Amitabha Sutra 阿彌陀經</button></li>
        <li><button type="button" data-v="住" data-p="王舍城耆闍崛山中" data-n="萬二千人" data-en="&hellip;dwelt on Mount Gṛdhrakūṭa at Rājagṛha, together with a great assembly of bhikṣus, twelve thousand in all." aria-pressed="false">Lotus Sutra 法華經</button></li>
        <li><button type="button" data-v="在" data-p="王舍城耆闍崛山中" data-n="及菩薩眾" data-en="&hellip;was on Mount Gṛdhrakūṭa at Rājagṛha, together with a great assembly of bhikṣus and an assembly of bodhisattvas. (The long recension, T0253.)" aria-pressed="false">Heart Sutra 心經</button></li>
      </ul>
      <p class="fh-en" id="frame-en">&hellip;was in the land of Śrāvastī, in Jeta's Grove, the Park of the Giver to the Orphaned and Solitary, together with a great assembly of bhikṣus, 1,250 in all.</p>

      <p data-rv style="margin-top:24px">Notice what did <em>not</em> move. <span class="zh">如是我聞</span>, <span class="zh">一時，佛</span>, and <span class="zh">與大比丘眾…俱</span> hold still in all four. Only the verb, the place, and the headcount change.</p>

      <div class="fh-part"><div class="pn">Part 2</div><h2>Eight characters, 6.55% of the canon</h2></div>

      <p data-rv>These eight open the sentence. Together they occur <strong>1,731,644 times</strong> across the sutras &mdash; one character in every fifteen you will ever meet. None ranks lower than 104th. Tap any of them.</p>

      <ul class="fh-tiles" id="frame-tiles"></ul>
      <div id="frame-card"><p class="fh-hint">Tap a character above.</p></div>

      <p data-rv><span class="zh">如是我聞</span> is Ānanda speaking. At the first council he recited what he had heard, and every recitation opens by saying so: <em>thus</em> &mdash; <span class="zh">如是</span>, like-this &mdash; <em>have I heard</em>. It stands at the head of <strong>596 of the 1,482 sutras</strong>.</p>

      <p data-rv><span class="zh">一時</span> is doing something careful. It does not mean "once upon a time" and it does not give a date. It means <em>on one occasion</em> &mdash; a single stretch of time the sutra declines to locate. The tradition is precise about what it does not claim to know.</p>

      <div class="fh-part"><div class="pn">Part 3</div><h2>The place is one word, not nine</h2></div>

      <p data-rv>Here is where beginners waste months. <span class="zh">舍衛國祇樹給孤獨園</span> looks like nine characters to memorize, and four of them are genuinely rare &mdash; <span class="zh">孤</span> ranks 836th, <span class="zh">給</span> 686th, <span class="zh">衛</span> 672nd. You would meet them almost nowhere else.</p>

      <p data-rv>So do not learn them as characters. Learn the whole string as one proper noun, the way you learned <em>Massachusetts</em>. It appears <strong>2,100 times across 245 sutras</strong>, always meaning the same garden outside the same city.</p>

      <ul class="fh-tiles" id="place-tiles"></ul>
      <div id="place-card"><p class="fh-hint">Tap a character above.</p></div>

      <p data-rv>One detail worth carrying with you, because it shows how Kumārajīva worked. The name has two halves and he treated them oppositely. <span class="zh">舍衛</span> is <em>sound</em>: Śrāvastī pushed through Chinese phonetics, meaning nothing in Chinese at all. <span class="zh">給孤獨</span> is <em>sense</em>: the donor's name was Anāthapiṇḍika, "he who gives to the destitute," and rather than transliterate it he translated it &mdash; give, orphaned, solitary. Same name, same line, two strategies.</p>

      <p data-rv>Once you can see that switch happening, a great deal of Buddhist Chinese stops being arbitrary.</p>

      <div class="fh-part"><div class="pn">Part 4</div><h2>Who was there</h2></div>

      <p data-rv>The assembly clause closes the opening. <span class="zh">與大比丘眾…俱</span> &mdash; <em>together with a great assembly of bhikṣus&hellip; all present</em> &mdash; wraps a number in the middle. The clause appears in <strong>264 sutras</strong>; the number inside it is what changes.</p>

      <ul class="fh-tiles" id="asm-tiles"></ul>
      <div id="asm-card"><p class="fh-hint">Tap a character above.</p></div>

      <p data-rv><span class="zh">比丘</span> is sound again (<em>bhikṣu</em>), and <span class="zh">俱</span> is the quiet hinge at the end &mdash; <em>all of them, together</em>. Chinese has no plural ending, so <span class="zh">俱</span> does that work by sitting at the close of the clause.</p>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap wide">
      <div class="fh-part"><div class="pn">Part 5</div><h2>You have just read two sutras</h2></div>
      <p data-rv>These are the opening lines of two of the most recited texts in East Asian Buddhism, as Kumārajīva left them. Read them against each other.</p>
      <div class="fh-twins">
        <div class="fh-twin" data-rv>
          <p class="who">Diamond Sutra &middot; T0235 &middot; 金剛般若波羅蜜經</p>
          <p class="txt" lang="zh-Hant">如是我聞：一時，佛在舍衛國祇樹給孤獨園，與大比丘<mark>眾</mark>千二百五十人俱。</p>
        </div>
        <div class="fh-twin" data-rv>
          <p class="who">Amitabha Sutra &middot; T0366 &middot; 佛說阿彌陀經</p>
          <p class="txt" lang="zh-Hant">如是我聞：一時，佛在舍衛國祇樹給孤獨園，與大比丘<mark>僧</mark>千二百五十人俱，皆是大阿羅漢，眾所知識。</p>
        </div>
      </div>
      <p data-rv style="margin-top:22px">Twenty-two characters, and they differ in exactly one: <span class="zh">眾</span> against <span class="zh">僧</span>. Both name the monastic community; the second is the word that gave English <em>Sangha</em>. One sentence learned, two sutras opened.</p>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 6</div><h2>Check yourself<span class="rf">Work each line out before you reveal it</span></h2></div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">如是我聞：一時佛住王舍城耆闍崛山。</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"Thus have I heard. At one time the Buddha dwelt on Mount Gṛdhrakūṭa at Rājagṛha."</p>
          <p class="sm">Ratnakūṭa Sutra 大寶積經, T0310. The verb shifted from <span class="zh">在</span> to <span class="zh">住</span> &mdash; <em>was at</em> becoming <em>dwelt at</em> &mdash; and the assembly clause is simply dropped. <span class="zh">王舍城</span> is sense-for-sense: king–house–city, Rājagṛha.</p>
        </div>
      </div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">爾時，世尊食時，著衣持鉢，入舍衛大城乞食。</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"At that time, when it was time to eat, the World-Honored One put on his robe, took up his bowl, and entered the great city of Śrāvastī to beg for food."</p>
          <p class="sm">The Diamond Sutra's next sentence. Two new formulas arrive here: <span class="zh">爾時</span> (<em>at that time</em>) occurs 42,743 times across 1,020 sutras, and <span class="zh">世尊</span> (<em>World-Honored One</em>) 67,271 times across 1,009. Session 2 is built on them.</p>
        </div>
      </div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">如是我聞：一時佛在王舍城耆闍崛山中，與大比丘眾及菩薩眾俱。</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"Thus have I heard. At one time the Buddha was on Mount Gṛdhrakūṭa at Rājagṛha, together with a great assembly of bhikṣus and an assembly of bodhisattvas."</p>
          <p class="sm">The Heart Sutra, T0253 &mdash; the long recension, which has an opening. The short version most people recite drops the frame entirely and starts at <span class="zh">觀自在菩薩</span>. Here the headcount slot holds no number at all: <span class="zh">及菩薩眾</span>, <em>and an assembly of bodhisattvas</em>.</p>
        </div>
      </div>

      <div class="fh-part"><div class="pn">Next</div><h2>Session 2 &mdash; At That Time, the World-Honored One</h2></div>
      <p data-rv>The opening formula gets you into the room. The next one moves the scene along, and it is the most common structure in the canon: <span class="zh">爾時，世尊告……言</span>. Once you have it you can follow who is speaking to whom through any sutra on the shelf, which is most of what reading scripture consists of.</p>
      <p data-rv style="font-size:15px;color:var(--ink-soft)">Running total after Session 1: <strong>29 characters</strong>, 2 formulas, and the opening of the Diamond Sutra read in the original.</p>
""" + nav(None, ("/courses/four-hundred-characters/session-2/", "Session 2")) + """
    </div>
  </div>
""" + METHOD

S2_GROUPS = [
    {"host":"nar-tiles","card":"nar-card","chars":"爾時世尊","dim":""},
    {"host":"spk-tiles","card":"spk-card","chars":"白告言問答","dim":""},
    {"host":"ges-tiles","card":"ges-card","chars":"從座起合掌恭敬","dim":"座掌恭敬"},
    {"host":"con-tiles","card":"con-card","chars":"何故是復次","dim":""},
]

S2_BODY = crumb("Session 2") + """
  <section class="fh-hero">
    <div class="fh-hero-in">
      <div class="fh-eyebrow">Session 2 &middot; Following the conversation</div>
      <h1>At That Time, the World-Honored One</h1>
      <p class="lede">Session 1 got you into the room. Now you have to follow the conversation &mdash; and the canon gives you no quotation marks, no capital letters, and no verb tenses to do it with. What it gives you instead is a set of formulas that mark who spoke, in which direction, and what kind of move they were making.</p>
      <p class="fh-hero-zh" lang="zh-Hant">時，長者須菩提在大眾中即從座起，偏褒右肩，<br>右膝著地，合掌恭敬而白佛言</p>
      <p class="fh-hero-gloss">Then the elder Subhūti rose from his seat in the assembly, bared his right shoulder, placed his right knee on the ground, joined his palms in reverence, and addressed the Buddha, saying&hellip;</p>
    </div>
  </section>

  <div class="fh-body">
    <div class="fh-wrap">

      <div class="fh-part"><div class="pn">Part 1</div><h2>This is the next sentence</h2></div>

      <p data-rv>Last session you read the opening of the Diamond Sutra: the Buddha at Jeta's Grove with 1,250 monks. Two sentences later he has walked into Śrāvastī, begged his food, come back, washed his feet, and sat down. Then the sentence above happens, and the sutra proper begins.</p>

      <p data-rv>We are not skipping around. Sessions 1, 2, and 3 walk straight down the opening of one text, in order, which is the only honest way to learn to read one.</p>

      <div class="fh-stats" data-rv>
        <div class="fh-stat"><b>42,743</b><span>occurrences of 爾時, across 1,020 sutras</span></div>
        <div class="fh-stat"><b>67,271</b><span>occurrences of 世尊, across 1,009 sutras</span></div>
        <div class="fh-stat"><b>13,381</b><span>occurrences of 白佛言, across 747 sutras</span></div>
        <div class="fh-stat"><b>13,090</b><span>occurrences of 佛告, across 740 sutras</span></div>
      </div>

      <div class="fh-part"><div class="pn">Part 2</div><h2>爾時 &mdash; the cut between shots</h2></div>

      <p data-rv><span class="zh">爾時</span> means <em>at that time</em>, and it does the work a paragraph break or a scene change does in English. It appears in <strong>1,020 of the canon's 1,482 sutras</strong> &mdash; sixty-nine percent &mdash; and when you see it, the camera has moved.</p>

      <p data-rv>It pairs almost always with <span class="zh">世尊</span>, <em>World-Honored One</em>, which is what the texts call the Buddha when they are being formal about him. <span class="zh">佛</span> is his name in narration; <span class="zh">世尊</span> is how he is addressed and how the narrator refers to him at a solemn moment. Both are extremely common and they are not interchangeable in tone.</p>

      <ul class="fh-tiles" id="nar-tiles"></ul>
      <div id="nar-card"><p class="fh-hint">Tap a character above.</p></div>

      <p data-rv>One practical note: <span class="zh">爾</span> ranks 116th in the canon and you will meet it almost nowhere except inside <span class="zh">爾時</span>. Do not learn it as a word. Learn the pair.</p>

      <div class="fh-part"><div class="pn">Part 3</div><h2>Speech has a direction<span class="rf">The most useful thing in this session</span></h2></div>

      <p data-rv>Classical Chinese marks the <em>social direction</em> of speech in the verb itself, and the canon is rigid about it.</p>

      <p data-rv>A disciple speaking to the Buddha uses <span class="zh">白</span>: <span class="zh">白佛言</span>, <em>addressed the Buddha, saying</em>. The ordinary meaning of <span class="zh">白</span> is the color white; here it is a verb, and it means to report upward to someone senior. It occurs <strong>13,381 times across 747 sutras</strong>.</p>

      <p data-rv>The Buddha speaking to a disciple uses <span class="zh">告</span>: <span class="zh">佛告須菩提</span>, <em>the Buddha told Subhūti</em>. It occurs <strong>13,090 times across 740 sutras</strong> &mdash; almost exactly as often, which makes sense, since scripture is mostly people taking turns.</p>

      <p data-rv><strong>The two are never swapped.</strong> A monk does not <span class="zh">告</span> the Buddha. So when you find either verb you immediately know which way the sentence is pointing, before you have understood a single other word in it.</p>

      <ul class="fh-tiles" id="spk-tiles"></ul>
      <div id="spk-card"><p class="fh-hint">Tap a character above.</p></div>

      <p data-rv><span class="zh">言</span> closes the formula. It sits at the end &mdash; <span class="zh">白佛言</span>, <span class="zh">佛告須菩提…言</span> &mdash; and everything after it is the quotation. That is your quotation mark.</p>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 4</div><h2>The body of respect</h2></div>

      <p data-rv>Before Subhūti says anything he does five things: <span class="zh">從座起</span> rises from his seat, <span class="zh">偏褒右肩</span> bares his right shoulder, <span class="zh">右膝著地</span> puts his right knee to the ground, <span class="zh">合掌</span> joins his palms, <span class="zh">恭敬</span> reverently. Then he speaks.</p>

      <p data-rv>Notice the ranks. <span class="zh">偏</span> is 1,184th in the canon. <span class="zh">褒</span> is 1,436th. <span class="zh">肩</span> is 1,101st, <span class="zh">膝</span> 1,034th. These are genuinely rare characters &mdash; and you have just met all four in a single clause.</p>

      <p data-rv>This is the same lesson as the garden in Session 1, and it is the central skill of the course, so here it is as a rule:</p>

      <div class="fh-note" data-rv>
        <h4>When rare characters cluster, you are looking at a block</h4>
        <p>Scripture's rarest characters almost never appear alone. They arrive in fixed strings &mdash; a place name, a gesture, a title, a transliterated Sanskrit word &mdash; that recur unchanged across hundreds of texts. Recognize the string; do not drill the characters. Your four hundred characters are spent on the connective tissue, not on these.</p>
      </div>

      <ul class="fh-tiles" id="ges-tiles"></ul>
      <div id="ges-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 5</div><h2>何以故 &mdash; the canon interrogates itself</h2></div>

      <p data-rv>Buddhist scripture argues, and it argues by asking itself questions. Three connectives carry almost all of that structure, and once you can see them the shape of an argument appears on the page even where the content is still beyond you.</p>

      <div class="fh-tscroll" data-rv>
        <table>
          <thead><tr><th>Connective</th><th>Force</th><th class="n">Times</th><th class="n">Sutras</th></tr></thead>
          <tbody>
            <tr><td class="zh">何以故</td><td>Why is that? &mdash; a question the text then answers itself</td><td class="n">25,706</td><td class="n">457</td></tr>
            <tr><td class="zh">是故</td><td>Therefore &mdash; the conclusion is arriving</td><td class="n">19,513</td><td class="n">764</td></tr>
            <tr><td class="zh">復次</td><td>Furthermore &mdash; a new point, the canon's paragraph break</td><td class="n">18,551</td><td class="n">489</td></tr>
          </tbody>
        </table>
      </div>

      <p data-rv style="margin-top:22px"><span class="zh">何以故</span> is not a rhetorical flourish. It is a structural signal: the sentence before it was a claim, and the sentence after it is the reason. In the Diamond Sutra it appears again and again, and each time it tells you the text is about to undercut what it just said.</p>

      <ul class="fh-tiles" id="con-tiles"></ul>
      <div id="con-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap wide">
      <div class="fh-part"><div class="pn">Part 6</div><h2>A complete exchange<span class="rf">Four turns, in the order the text gives them</span></h2></div>
      <p data-rv>Here is Subhūti's question and the Buddha's reply, in sequence. Read it for the traffic pattern first &mdash; who is speaking to whom &mdash; and only then for the content. Watch the speech verb change on every turn, and then vanish.</p>
      <div class="fh-twins">
        <div class="fh-twin" data-rv>
          <p class="who">Turn 1 &middot; Subhūti asks &middot; upward</p>
          <p class="txt" lang="zh-Hant">而<mark>白佛言</mark>：「希有世尊！如來善護念諸菩薩，善付囑諸菩薩。世尊！善男子、善女人，發阿耨多羅三藐三菩提心，應云何住？云何降伏其心？」</p>
          <p class="fh-en">&hellip;and addressed the Buddha, saying: "How rare, World-Honored One! The Thus-Come One well watches over the bodhisattvas, well entrusts the bodhisattvas. World-Honored One — a good man or good woman who has set their mind on unsurpassed perfect awakening: how should they abide? How should they subdue their mind?"</p>
        </div>
        <div class="fh-twin" data-rv>
          <p class="who">Turn 2 &middot; the Buddha approves &middot; bare <span class="zh">佛言</span>, no addressee</p>
          <p class="txt" lang="zh-Hant"><mark>佛言</mark>：「善哉，善哉！須菩提！如汝所說：『如來善護念諸菩薩，善付囑諸菩薩。』汝今諦聽，當為汝說。」</p>
          <p class="fh-en">The Buddha said: "Excellent, excellent! Subhūti! It is as you say — the Thus-Come One well watches over the bodhisattvas, well entrusts the bodhisattvas. Listen closely now, and I will tell you." Here the verb is the bare <span class="zh">佛言</span> with nobody named: he is answering, not initiating.</p>
        </div>
        <div class="fh-twin" data-rv>
          <p class="who">Turn 3 &middot; Subhūti assents &middot; no speech verb at all</p>
          <p class="txt" lang="zh-Hant">「唯然。世尊！願樂欲聞。」</p>
          <p class="fh-en">"Just so. World-Honored One! Gladly would we hear it." Seven characters, and nothing marks who is speaking. The canon drops the formula once the turn-taking is established, exactly as English drops "he said" in a fast exchange. The vocative <span class="zh">世尊</span> is the only clue, and it is enough — only a disciple would use it.</p>
        </div>
        <div class="fh-twin" data-rv>
          <p class="who">Turn 4 &middot; the Buddha begins &middot; downward</p>
          <p class="txt" lang="zh-Hant"><mark>佛告</mark>須菩提：「諸菩薩摩訶薩應如是降伏其心&hellip;」</p>
          <p class="fh-en">The Buddha told Subhūti: "The bodhisattva-mahāsattvas should subdue their mind thus&hellip;" The verb returns, and with an addressee, because a new movement is starting.</p>
        </div>
      </div>
      <p data-rv style="margin-top:22px">Four turns, four different ways of marking speech: <span class="zh">白佛言</span> going up, bare <span class="zh">佛言</span> answering, nothing at all, then <span class="zh">佛告</span> going back down. In Classical Chinese scripture the speech verb <em>is</em> the punctuation.</p>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 7</div><h2>Check yourself</h2></div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">爾時世尊告阿難言：「此是無量壽佛極樂世界。」</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"At that time the World-Honored One addressed Ānanda, saying: 'This is the Land of Ultimate Bliss of the Buddha of Immeasurable Life.'"</p>
          <p class="sm">Ratnakūṭa Sutra 大寶積經, T0310. The complete downward formula: <span class="zh">爾時</span> scene change, <span class="zh">世尊</span> speaker, <span class="zh">告</span> direction, <span class="zh">阿難</span> addressee, <span class="zh">言</span> quotation opens. <span class="zh">世尊告</span> alone occurs 4,002 times across 439 sutras. The next sentence in the original tells Ānanda to rise and <span class="zh">合掌恭敬</span> &mdash; the gesture block from Part 4.</p>
        </div>
      </div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">爾時，須菩提白佛言：「世尊！當何名此經？我等云何奉持？」佛告須菩提&hellip;</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"At that time Subhūti addressed the Buddha, saying: 'World-Honored One! What should this sutra be called? How are we to uphold it?' The Buddha told Subhūti&hellip;"</p>
          <p class="sm">Both directions in one passage, from the Diamond Sutra itself: <span class="zh">白</span> going up, then <span class="zh">告</span> coming back down. Subhūti is asking what to name the text he is sitting inside. Note the two question words &mdash; <span class="zh">當何名</span> what should it be called, <span class="zh">云何</span> in what manner &mdash; both built on <span class="zh">何</span>.</p>
        </div>
      </div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">何以故？若取非法相，即著我、人、眾生、壽者。是故不應取法，不應取非法。</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"Why is that? If one grasps the mark of non-dharma, one is attached to self, to person, to being, to life span. Therefore one should not grasp at dharmas, nor grasp at non-dharmas."</p>
          <p class="sm">Both connectives doing their jobs in one breath: <span class="zh">何以故</span> opens the reason, <span class="zh">是故</span> lands the conclusion. And <span class="zh">非</span> appears twice &mdash; the third negation, which is Session 3's business. Diamond Sutra, T0235.</p>
        </div>
      </div>

      <div class="fh-part"><div class="pn">Next</div><h2>Session 3 &mdash; The Grammar of Not</h2></div>
      <p data-rv>You can now get into a sutra and follow who is talking. What they are actually saying is mostly negative &mdash; and that is not a figure of speech. The most common character in the entire Buddhist canon is <span class="zh">無</span>, <em>there is not</em>. The second is <span class="zh">不</span>. Together they account for one character in every twenty-seven.</p>
      <p data-rv style="font-size:15px;color:var(--ink-soft)">Running total after Session 2: <strong>48 characters</strong>, 9 formulas, and the opening of the Diamond Sutra read in the original.</p>
""" + nav(("/courses/four-hundred-characters/session-1/", "Session 1"),
          ("/courses/four-hundred-characters/session-3/", "Session 3")) + """
    </div>
  </div>
""" + METHOD

S3_GROUPS = [
    {"host":"neg-tiles","card":"neg-card","chars":"無不非","dim":""},
    {"host":"jf-tiles","card":"jf-card","chars":"即是相我","dim":""},
    {"host":"if-tiles","card":"if-card","chars":"若有想空","dim":""},
    {"host":"pay-tiles","card":"pay-card","chars":"實得者量數邊滅度","dim":""},
]

S3_BODY = crumb("Session 3") + """
  <section class="fh-hero">
    <div class="fh-hero-in">
      <div class="fh-eyebrow">Session 3 &middot; The negations</div>
      <h1>The Grammar of Not</h1>
      <p class="lede">The most common character in the Buddhist canon is 無 &mdash; <em>there is not</em>. The second most common is 不 &mdash; <em>not</em>. Between them they are one character in every twenty-seven you will ever read. This is not a stylistic tic. Buddhist Chinese is, statistically, a language for saying what is not the case.</p>
      <p class="fh-hero-zh" lang="zh-Hant">是諸法空相，不生不滅，不垢不淨，不增不減。</p>
      <p class="fh-hero-gloss">These dharmas are empty of characteristics: not arising, not ceasing; not defiled, not pure; not increasing, not decreasing.</p>
    </div>
  </section>

  <div class="fh-body">
    <div class="fh-wrap">

      <div class="fh-part"><div class="pn">Part 1</div><h2>Two characters, one in twenty-seven</h2></div>

      <div class="fh-stats" data-rv>
        <div class="fh-stat"><b>#1</b><span>無 &mdash; 528,802 times, 2.00% of the canon</span></div>
        <div class="fh-stat"><b>#2</b><span>不 &mdash; 432,503 times, 1.64%</span></div>
        <div class="fh-stat"><b>#77</b><span>非 &mdash; 77,968 times, 0.30%</span></div>
        <div class="fh-stat"><b>3.64%</b><span>無 and 不 combined</span></div>
      </div>

      <p data-rv>For comparison: <span class="zh">佛</span>, the Buddha himself, is only the eighth most common character in his own scriptures. <span class="zh">無</span> beats him by a factor of two.</p>

      <div class="fh-part"><div class="pn">Part 2</div><h2>Three negations, three jobs<span class="rf">Get this one distinction straight and it does more for your reading than the next hundred characters</span></h2></div>

      <p data-rv>English uses <em>not</em> for nearly everything. Classical Chinese does not, and the difference is grammatical rather than stylistic.</p>

      <div class="fh-card" data-rv>
        <h3><span class="chb" lang="zh-Hant">無</span>before a noun &mdash; <em>there is no ___</em></h3>
        <p>It denies existence, or strips an attribute away. <span class="zh">無色</span> &mdash; there is no form. <span class="zh">無我</span> &mdash; there is no self. <span class="zh">無所得</span> &mdash; there is nothing attained. Think of it as the opposite of <span class="zh">有</span>, <em>there is</em>, which ranks seventh.</p>
      </div>
      <div class="fh-card" data-rv>
        <h3><span class="chb" lang="zh-Hant">不</span>before a verb &mdash; <em>does not ___</em></h3>
        <p>It denies an action or a quality. <span class="zh">不生</span> &mdash; does not arise. <span class="zh">不滅</span> &mdash; does not cease. <span class="zh">不異</span> &mdash; is not different from. The line in the hero above is six of these in a row.</p>
      </div>
      <div class="fh-card" data-rv>
        <h3><span class="chb" lang="zh-Hant">非</span>before a noun predicate &mdash; <em>is not ___</em></h3>
        <p>It denies an identification. <span class="zh">非菩薩</span> &mdash; is not a bodhisattva. <span class="zh">非相</span> &mdash; is not a characteristic. Where <span class="zh">無</span> says the thing is absent, <span class="zh">非</span> says the thing is present but is not what you called it. That is a sharper and more dangerous instrument, and the Perfection of Wisdom literature runs on it.</p>
      </div>

      <ul class="fh-tiles" id="neg-tiles"></ul>
      <div id="neg-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 3</div><h2>即是 &middot; 即非</h2></div>

      <p data-rv><span class="zh">即</span> means <em>precisely, is exactly</em>. It is the hinge on which the Diamond Sutra turns, and it swings both ways. <span class="zh">即是</span> asserts an identity in the strongest available terms: <span class="zh">色即是空</span>, form is precisely emptiness. <span class="zh">即非</span> denies one in the same breath.</p>

      <div class="fh-frame center" lang="zh-Hant" data-rv>我相即是非相</div>

      <p data-rv style="margin-top:20px"><em>The characteristic of self is precisely a non-characteristic.</em> Not "self does not exist" &mdash; that would be <span class="zh">無我</span>, and the text says that elsewhere. This is the harder move: the mark is there, and it is not what it presents itself as.</p>

      <ul class="fh-tiles" id="jf-tiles"></ul>
      <div id="jf-card"><p class="fh-hint">Tap a character above.</p></div>

      <p data-rv>The same structure one sentence earlier: <span class="zh">若菩薩有我相、人相、眾生相、壽者相，即非菩薩。</span> &mdash; <em>If a bodhisattva has the mark of a self, of a person, of a being, of a life span &mdash; then they are precisely not a bodhisattva.</em> One <span class="zh">若</span>, four <span class="zh">相</span>, one <span class="zh">即非</span>. You have the grammar for the whole sentence.</p>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 4</div><h2>若 &hellip; 若 &hellip; and then four negations at once</h2></div>

      <p data-rv><span class="zh">若</span> ranks eleventh in the canon. It means <em>if</em>, but its commonest job is listing alternatives: <em>whether &hellip; or &hellip; or &hellip;</em>. Here is the Buddha enumerating every kind of being he has vowed to liberate:</p>

      <div class="fh-frame" lang="zh-Hant" data-rv>若卵生、若胎生、若濕生、若化生，若有色、若無色，若有想、若無想，若非有想非無想</div>

      <p data-rv style="margin-top:20px">Born from eggs, from a womb, from moisture, by transformation; with form or without form; with perception or without perception &mdash; and then the last item, which is doing something else entirely.</p>

      <p data-rv><span class="zh">非有想非無想</span>. <em>Neither with perception nor without perception.</em> The text has already given you <span class="zh">有想</span> and <span class="zh">無想</span> as a clean pair, and now it negates both of them, together, with <span class="zh">非</span>. Six characters, four negations, and a category that neither of the previous two exhausts.</p>

      <p data-rv>This is the single most characteristic move in Mahāyāna argument, and you have just read it in the original.</p>

      <ul class="fh-tiles" id="if-tiles"></ul>
      <div id="if-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap wide">
      <div class="fh-part"><div class="pn">Part 5</div><h2>One sentence with the whole sutra in it</h2></div>
      <p data-rv>This comes a few lines after the passage above. It is the Diamond Sutra's thesis, and there is nothing in it you have not now met.</p>
      <div class="fh-twins">
        <div class="fh-twin" data-rv>
          <p class="who">Diamond Sutra &middot; T0235</p>
          <p class="txt" lang="zh-Hant">如是滅度<mark>無量</mark>、<mark>無數</mark>、<mark>無邊</mark>眾生，<mark>實無</mark>眾生得滅度<mark>者</mark>。</p>
          <p class="fh-en">"Thus he brings to final release immeasurable, countless, boundless beings &mdash; and in reality there is no being who is brought to release."</p>
        </div>
      </div>
      <p data-rv style="margin-top:22px">Three <span class="zh">無</span> compounds pile up the scale &mdash; <span class="zh">無量</span> beyond measure, <span class="zh">無數</span> beyond counting, <span class="zh">無邊</span> beyond limit &mdash; and then a fourth <span class="zh">無</span> takes the whole thing back. <span class="zh">實</span> marks the register shift: <em>in reality</em>. And <span class="zh">者</span> at the end turns the verb into its agent: not "no release" but "no one who is released."</p>
      <ul class="fh-tiles" id="pay-tiles"></ul>
      <div id="pay-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 6</div><h2>Check yourself<span class="rf">Which negation, and why</span></h2></div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">色不異空，空不異色。</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"Form is not different from emptiness; emptiness is not different from form."</p>
          <p class="sm"><span class="zh">不</span>, because <span class="zh">異</span> (to differ from) is a verb. Using <span class="zh">無</span> here would say "there is no difference," which is a claim about difference rather than about form. From the Heart Sutra, which you read in full next session.</p>
        </div>
      </div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">是故，空中無色，無受、想、行、識。</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"Therefore, in emptiness there is no form, no sensation, perception, volition, or consciousness."</p>
          <p class="sm"><span class="zh">無</span> twice over a list, because every one of these is a noun. And <span class="zh">是故</span> from Session 2 tells you a conclusion is landing.</p>
        </div>
      </div>

      <div class="fh-ex" data-rv>
        <p class="q" lang="zh-Hant">如來說第一波羅蜜，非第一波羅蜜。</p>
        <button class="fh-reveal" type="button" aria-expanded="false">Reveal</button>
        <div class="fh-ans" hidden>
          <p>"The Thus-Come One speaks of the foremost perfection &mdash; which is not the foremost perfection."</p>
          <p class="sm"><span class="zh">非</span>, because what is being denied is an identification, not an existence. The thing was named; the name does not hold. Neither <span class="zh">無</span> nor <span class="zh">不</span> would carry this, and the Diamond Sutra does it dozens of times.</p>
        </div>
      </div>

      <div class="fh-part"><div class="pn">Next</div><h2>Session 4 &mdash; Two Hundred Sixty Characters</h2></div>
      <p data-rv>You now have the opening frame, the dialogue formulas, and the grammar of negation. That is enough to read a complete Buddhist scripture from the first character to the last, so that is what happens next. The Heart Sutra is 260 characters long and uses only 117 distinct ones. Twenty-one of those 260 characters are <span class="zh">無</span>.</p>
      <p data-rv style="font-size:15px;color:var(--ink-soft)">Running total after Session 3: <strong>65 characters</strong>, 16 formulas, and the thesis of the Diamond Sutra read in the original.</p>
""" + nav(("/courses/four-hundred-characters/session-2/", "Session 2"),
          ("/courses/four-hundred-characters/session-4/", "Session 4")) + """
    </div>
  </div>
""" + METHOD

S4_GROUPS = [
    {"host":"agg-tiles","card":"agg-card","chars":"五蘊色受想行識","dim":"蘊"},
    {"host":"sen-tiles","card":"sen-card","chars":"眼耳鼻舌身意聲香味觸界","dim":""},
    {"host":"tra-tiles","card":"tra-card","chars":"般波羅蜜多菩薩埵","dim":"般波羅蜜埵"},
    {"host":"end-tiles","card":"end-card","chars":"罣礙恐怖遠離顛倒夢究竟涅槃","dim":"罣顛倒夢究竟涅槃"},
]

S4_BODY = crumb("Session 4") + """
  <section class="fh-hero">
    <div class="fh-hero-in">
      <div class="fh-eyebrow">Session 4 &middot; A whole sutra</div>
      <h1>Two Hundred Sixty Characters</h1>
      <p class="lede">This is the session the first three were for. The Heart Sutra is 260 characters long, uses only 117 distinct ones, and eighty-nine percent of them sit in the canon's top four hundred. You are going to read all of it &mdash; every character, in order, to the last syllable of the mantra. Nothing will be summarized for you.</p>
      <p class="fh-hero-zh" lang="zh-Hant">觀自在菩薩行深般若波羅蜜多時，<br>照見五蘊皆空，度一切苦厄。</p>
      <p class="fh-hero-gloss">When the Bodhisattva Who Contemplates Freely was practicing the deep perfection of wisdom, he saw clearly that the five aggregates are all empty, and he crossed beyond all suffering and distress.</p>
    </div>
  </section>

  <div class="fh-body">
    <div class="fh-wrap">

      <div class="fh-part"><div class="pn">Part 1</div><h2>Why this text</h2></div>

      <div class="fh-stats" data-rv>
        <div class="fh-stat"><b>260</b><span>characters in the whole sutra</span></div>
        <div class="fh-stat"><b>117</b><span>distinct characters used</span></div>
        <div class="fh-stat"><b>89.2%</b><span>of them in the canon's top 400</span></div>
        <div class="fh-stat"><b>21&times;</b><span>occurrences of 無 &mdash; 8% of the text</span></div>
      </div>

      <p data-rv>The Heart Sutra is the most recited text in East Asian Buddhism and the shortest complete sutra in the canon. It is also almost entirely built out of Session 3: <span class="zh">無</span> twenty-one times, <span class="zh">不</span> nine times, <span class="zh">空</span> seven times. If you can handle three negations and a handful of nouns, you can handle this.</p>

      <p data-rv>We are reading Xuanzang's version, T0251, finished in 649. Note his opening: <span class="zh">觀自在菩薩</span>, <em>the Bodhisattva Who Contemplates Freely</em>. Kumārajīva had rendered the same name <span class="zh">觀世音</span>, <em>Regarder of the World's Sounds</em> &mdash; the form that became Guanyin. Same bodhisattva, two translators, two readings of the Sanskrit.</p>

      <div class="fh-part"><div class="pn">Part 2</div><h2>The opening<span class="rf">One of six</span></h2></div>

      <div class="fh-frame" lang="zh-Hant" data-rv>觀自在菩薩行深般若波羅蜜多時，照見五蘊皆空，度一切苦厄。</div>
      <p class="fh-en">When the Bodhisattva Who Contemplates Freely was practicing the deep perfection of wisdom, he saw clearly that the five aggregates are all empty, and he crossed beyond all suffering and distress.</p>

      <p data-rv style="margin-top:22px"><span class="zh">時</span> at the end of the first clause is Session 1's <span class="zh">一時</span> doing a different job: here it marks <em>when</em> something was happening, not <em>once upon a time</em>. Chinese has no tense, so a bare <span class="zh">時</span> carries the whole "while he was doing X" construction.</p>

      <p data-rv>The <span class="zh">五蘊</span>, five aggregates, are the inventory of a person: form, sensation, perception, volition, consciousness. They arrive as a set and come back twice more in this text, so learn them here.</p>

      <ul class="fh-tiles" id="agg-tiles"></ul>
      <div id="agg-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 3</div><h2>Form and emptiness, four ways</h2></div>
      <div class="fh-frame" lang="zh-Hant" data-rv>舍利子！色不異空，空不異色，色即是空，空即是色；受、想、行、識，亦復如是。</div>
      <p class="fh-en">Śāriputra! Form is not different from emptiness, emptiness is not different from form; form is precisely emptiness, emptiness is precisely form. Sensation, perception, volition, and consciousness are likewise the same.</p>
      <p data-rv style="margin-top:22px">Four clauses, and the move from the first pair to the second is the point. <span class="zh">不異</span> says <em>not different from</em> &mdash; a cautious, negative formulation. <span class="zh">即是</span> says <em>is precisely</em> &mdash; the positive identity, asserted flat out. The text says the weaker thing first and then the stronger, in both directions.</p>
      <p data-rv>Then <span class="zh">亦復如是</span> &mdash; <em>likewise the same</em> &mdash; and the other four aggregates are folded in without repeating the argument. That formula occurs 8,143 times across 440 sutras; it is how scripture avoids saying everything four times.</p>

      <div class="fh-part"><div class="pn">Part 4</div><h2>Six negations in a row</h2></div>
      <div class="fh-frame" lang="zh-Hant" data-rv>舍利子！是諸法空相，不生不滅，不垢不淨，不增不減。</div>
      <p class="fh-en">Śāriputra! These dharmas are empty of characteristics: not arising, not ceasing; not defiled, not pure; not increasing, not decreasing.</p>
      <p data-rv style="margin-top:22px">Three pairs of opposites, each pair canceled with <span class="zh">不</span>, because every one of these words is a verb. Arising and ceasing; defilement and purity; increase and decrease. The pairs are not random &mdash; they answer the three things one might still want to claim about something declared empty: that it began, that it is stained or clean, that it can grow.</p>
      <p data-rv><span class="zh">諸</span> at the front is doing the plural: <span class="zh">諸法</span>, <em>the dharmas</em>, all phenomena whatsoever. Chinese has no plural ending, so <span class="zh">諸</span> ranks ninth in the canon on that job alone.</p>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 5</div><h2>Emptying the inventory<span class="rf">The passage people find overwhelming, and the easiest in the sutra</span></h2></div>
      <div class="fh-frame" lang="zh-Hant" data-rv>是故，空中無色，無受、想、行、識；無眼、耳、鼻、舌、身、意；無色、聲、香、味、觸、法；無眼界，乃至無意識界；無無明亦無無明盡，乃至無老死亦無老死盡；無苦、集、滅、道；無智，亦無得。</div>
      <p class="fh-en">Therefore, in emptiness there is no form, no sensation, perception, volition, or consciousness; no eye, ear, nose, tongue, body, or mind; no form, sound, scent, taste, touch, or dharma; no field of the eye, and so on up to no field of mind-consciousness; no ignorance and no end of ignorance, and so on up to no aging-and-death and no end of aging-and-death; no suffering, arising, cessation, or path; no knowledge and no attainment.</p>
      <p data-rv style="margin-top:22px">It is a list of lists with one word in front of each: <span class="zh">無</span>.</p>
      <p data-rv>Six sense organs. Six sense objects. The eighteen fields, abbreviated with <span class="zh">乃至</span> &mdash; <em>and so on up to</em> &mdash; which saves the text from printing all eighteen. The twelve links of dependent arising, abbreviated the same way, from <span class="zh">無明</span> ignorance at one end to <span class="zh">老死</span> aging-and-death at the other. The four noble truths: <span class="zh">苦集滅道</span>. Then knowledge and attainment.</p>
      <p data-rv><span class="zh">乃至</span> is the pair to take away from this section. It appears twice here and it does what an ellipsis does &mdash; <em>first item &hellip; and so on up to &hellip; last item</em> &mdash; for a list the reader is assumed to know by heart.</p>
      <ul class="fh-tiles" id="sen-tiles"></ul>
      <div id="sen-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 6</div><h2>What follows from having nothing to gain</h2></div>
      <div class="fh-frame" lang="zh-Hant" data-rv>以無所得故，菩提薩埵依般若波羅蜜多故，心無罣礙；無罣礙故，無有恐怖，遠離顛倒夢想，究竟涅槃。三世諸佛依般若波羅蜜多故，得阿耨多羅三藐三菩提。</div>
      <p class="fh-en">Because there is nothing attained: the bodhisattva, relying on the perfection of wisdom, has a mind without hindrance; and having no hindrance, has no dread, leaves inverted dreaming far behind, and reaches final nirvāṇa. The buddhas of the three times, relying on the perfection of wisdom, attain unsurpassed perfect awakening.</p>
      <p data-rv style="margin-top:22px">Watch <span class="zh">故</span> here. Session 2 gave it to you inside <span class="zh">何以故</span> and <span class="zh">是故</span>; in this passage it appears four times as a clause-final <em>because</em>, chaining cause to cause: because nothing is attained &rarr; because they rely on wisdom &rarr; because there is no hindrance &rarr; therefore no dread. The logic is carried entirely by one character in one position.</p>
      <p data-rv><span class="zh">菩提薩埵</span> is worth noticing. This is <em>bodhisattva</em> transliterated in full, four characters. The familiar <span class="zh">菩薩</span> is an abbreviation of it &mdash; first and third characters only &mdash; which is why <span class="zh">薩</span> ranks tenth in the canon while <span class="zh">埵</span> ranks 846th.</p>
      <ul class="fh-tiles" id="tra-tiles"></ul>
      <div id="tra-card"><p class="fh-hint">Tap a character above.</p></div>
      <p data-rv>The same applies to <span class="zh">阿耨多羅三藐三菩提</span> &mdash; nine characters, pure sound, <em>anuttara-samyak-saṃbodhi</em>, unsurpassed perfect complete awakening. You met it in Session 2 in Subhūti's question. Do not parse it. Recognize it.</p>
      <ul class="fh-tiles" id="end-tiles"></ul>
      <div id="end-card"><p class="fh-hint">Tap a character above.</p></div>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 7</div><h2>The mantra, untranslated</h2></div>
      <div class="fh-frame" lang="zh-Hant" data-rv>故知般若波羅蜜多是大神咒、是大明咒、是無上咒、是無等等咒，能除一切苦，真實不虛，故說般若波羅蜜多咒。即說咒曰：揭帝揭帝般羅揭帝般羅僧揭帝菩提莎婆訶</div>
      <p class="fh-en">Therefore know that the perfection of wisdom is the great numinous mantra, the great bright mantra, the unsurpassed mantra, the mantra unequalled among equals; it can remove all suffering; it is true and not false. Therefore the mantra of the perfection of wisdom is spoken. And it is spoken thus: gate gate pāragate pārasaṃgate bodhi svāhā.</p>
      <p data-rv style="margin-top:22px">Four <span class="zh">是…咒</span> clauses in parallel, each escalating: <span class="zh">大神</span> great and numinous, <span class="zh">大明</span> great and bright, <span class="zh">無上</span> unsurpassed, <span class="zh">無等等</span> &mdash; literally <em>no-equal-equal</em>, unequalled even among things that have no equal. Two of the four are built with <span class="zh">無</span>.</p>
      <p data-rv>Then the text stops translating. The last fourteen characters are sound and nothing else &mdash; Sanskrit pushed through Chinese phonetics, meaning nothing in Chinese. A reader in 649 could pronounce it and could not read it, which was the point.</p>
      <div class="fh-note" data-rv>
        <h4>A note on 咒 &mdash; you will meet a different character</h4>
        <p>This edition writes <span class="zh">咒</span>. The canon overwhelmingly does not: <span class="zh">呪</span> appears <strong>17,301 times across 589 sutras</strong>, while <span class="zh">咒</span> appears only <strong>31 times in 15</strong>. They are the same word and the same meaning &mdash; <span class="zh">呪</span> is the form the old blocks were cut with, <span class="zh">咒</span> the form modern editions prefer. Expect <span class="zh">呪</span> everywhere else you read, and do not treat it as a new character.</p>
      </div>
    </div>
  </div>

  <div class="fh-body paper">
    <div class="fh-wrap wide">
      <div class="fh-part"><div class="pn">Part 8</div><h2>You have read a sutra</h2></div>
      <p data-rv>Here it is entire, with no English beside it. Four sessions ago this was a wall.</p>
      <div class="fh-twins">
        <div class="fh-twin" data-rv>
          <p class="who">般若波羅蜜多心經 &middot; T0251 &middot; 玄奘譯 &middot; 649 CE</p>
          <p class="txt full" lang="zh-Hant">觀自在菩薩行深般若波羅蜜多時，照見五蘊皆空，度一切苦厄。舍利子！色不異空，空不異色，色即是空，空即是色；受、想、行、識，亦復如是。舍利子！是諸法空相，不生不滅，不垢不淨，不增不減。是故，空中無色，無受、想、行、識；無眼、耳、鼻、舌、身、意；無色、聲、香、味、觸、法；無眼界，乃至無意識界；無無明亦無無明盡，乃至無老死亦無老死盡；無苦、集、滅、道；無智，亦無得。以無所得故，菩提薩埵依般若波羅蜜多故，心無罣礙；無罣礙故，無有恐怖，遠離顛倒夢想，究竟涅槃。三世諸佛依般若波羅蜜多故，得阿耨多羅三藐三菩提。故知般若波羅蜜多是大神咒、是大明咒、是無上咒、是無等等咒，能除一切苦，真實不虛，故說般若波羅蜜多咒。即說咒曰：揭帝揭帝般羅揭帝般羅僧揭帝菩提莎婆訶</p>
        </div>
      </div>
    </div>
  </div>

  <div class="fh-body">
    <div class="fh-wrap">
      <div class="fh-part"><div class="pn">Part 9</div><h2>What four hundred characters actually buys</h2></div>
      <p data-rv>You are not fluent, and this course will not make you fluent. What you have is different and more useful than it sounds: you can now open a Chinese sutra and find the handholds. You know where the opening frame ends and the text proper begins. You know who is speaking to whom. You can tell a denial of existence from a denial of identity. You can recognize a transliterated block and stop trying to parse it.</p>
      <p data-rv>That is the threshold where a bilingual edition becomes usable rather than decorative &mdash; where you read the Chinese, get most of it, and check the English for the rest, instead of reading the English and glancing at the Chinese. Every translation on this site is laid out for exactly that; the <a href="{{ '/sutras/' | relative_url }}">sūtra collection</a> is the place to go next.</p>
      <p data-rv style="font-size:15px;color:var(--ink-soft)">Running total after Session 4: <strong>102 characters</strong> taught explicitly, 19 formulas, the opening of the Diamond Sutra and the whole of the Heart Sutra read in the original.</p>
""" + nav(("/courses/four-hundred-characters/session-3/", "Session 3"), None) + """
    </div>
  </div>
""" + METHOD


PAGES = [
    ("index.html",
     fm("Four Hundred Characters",
        "/courses/four-hundred-characters/",
        "A four-session course in reading Chinese Buddhist scripture in the original — 576 characters cover ninety percent of the sutra canon, and the course takes you from no Chinese at all to reading the Heart Sutra entire."),
     IDX_BODY, []),
    ("session-1/index.html",
     fm("Session 1 · How Every Sutra Opens (Four Hundred Characters)",
        "/courses/four-hundred-characters/session-1/",
        "Session 1 of Four Hundred Characters — the opening formula that begins four in every ten sutras in the canon, and why the Diamond and Amitabha sutras start with the same twenty-two characters, one character apart."),
     S1_BODY, S1_GROUPS),
    ("session-2/index.html",
     fm("Session 2 · At That Time, the World-Honored One (Four Hundred Characters)",
        "/courses/four-hundred-characters/session-2/",
        "Session 2 of Four Hundred Characters — the speech formulas of Classical Chinese scripture, where the verb itself tells you whether a disciple is addressing the Buddha or the Buddha a disciple."),
     S2_BODY, S2_GROUPS),
    ("session-3/index.html",
     fm("Session 3 · The Grammar of Not (Four Hundred Characters)",
        "/courses/four-hundred-characters/session-3/",
        "Session 3 of Four Hundred Characters — 無, 不 and 非 are the canon's three negations, the first two are its two most common characters, and the difference between them is the highest-yield hour in the course."),
     S3_BODY, S3_GROUPS),
    ("session-4/index.html",
     fm("Session 4 · Two Hundred Sixty Characters (Four Hundred Characters)",
        "/courses/four-hundred-characters/session-4/",
        "Session 4 of Four Hundred Characters — the whole Heart Sutra read in Chinese, all 260 characters in order, from Avalokiteśvara's contemplation to the last syllable of the mantra."),
     S4_BODY, S4_GROUPS),
]

if __name__ == "__main__":
    for relpath, front, body, groups in PAGES:
        p, n, missing, bad = write(relpath, front, body, groups)
        flag = ""
        if missing:
            flag += "  MISSING=%s" % missing
        if bad:
            flag += "  STRAY-LIQUID"
        print("  %-24s tiles=%-3d%s" % (p, n, flag))
    print("\nWrote %d pages to courses/four-hundred-characters/" % len(PAGES))
