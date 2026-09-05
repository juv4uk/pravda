# -*- coding: utf-8 -*-
"""
Constructs the complete alignment mappings between RP Short (65 atoms) and RP Expanded (160 atoms).
Each entry provides:
ALIGN-ID, SOURCE-SHORT-CLAIM, SOURCE-EXP-CLAIM, MATCH-TYPE, ALIGNMENT-CONFIDENCE, MATCH-BASIS,
SHARED-LEXEMES, TEXT-SHORT, TEXT-EXP, STRUCTURAL-DIFFERENCE, SEMANTIC-INTERPRETATION, HISTORICAL-INTERPRETATION.
"""

import re

# Load Short and Expanded atoms
with open('HISTORICAL-CLAIMS-REGISTER.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx6 = text.find('## 6. Еталонний повний блок: Руська Правда (Коротка редакція)')
idx7 = text.find('## 7. Еталонний повний блок: Руська Правда (Простора редакція)')
idx8 = text.find('## 8. ')
if idx8 == -1: idx8 = len(text)

s6 = text[idx6:idx7]
s7 = text[idx7:idx8]

c6_raw = re.findall(r'(### HC-RP-SHORT-[0-9A-Z]+.*?)(?=(?:### HC-RP-SHORT-[0-9A-Z]+|\Z))', s6, re.DOTALL)
c7_raw = re.findall(r'(### HC-RP-EXP-[0-9A-Z]+.*?)(?=(?:### HC-RP-EXP-[0-9A-Z]+|\Z))', s7, re.DOTALL)

def parse_atom(raw):
    cid = re.search(r'### (HC-RP-[0-9A-Z\-]+)', raw).group(1)
    art = re.search(r'- \*\*ARTICLE:\*\* (.*)', raw).group(1)
    loc = re.search(r'- \*\*LOCATOR:\*\* (.*)', raw).group(1)
    quote = re.search(r'- \*\*EXACT-QUOTE:\*\*\s+> (.*)', raw).group(1)
    actor = re.search(r'- \*\*GRAMMATICAL-ACTOR:\*\* (.*)', raw).group(1)
    operator = re.search(r'- \*\*TEXTUAL-OPERATOR:\*\* (.*)', raw).group(1)
    obj = re.search(r'- \*\*TEXTUAL-OBJECT:\*\* (.*)', raw).group(1)
    cond = re.search(r'- \*\*TEXTUAL-CONDITION:\*\* (.*)', raw).group(1)
    conseq = re.search(r'- \*\*TEXTUAL-CONSEQUENCE:\*\* (.*)', raw).group(1)
    terms = re.search(r'- \*\*LEXICAL-TERMS:\*\* (.*)', raw).group(1)
    return {
        'id': cid, 'article': art, 'locator': loc, 'quote': quote,
        'actor': actor, 'operator': operator, 'object': obj,
        'condition': cond, 'consequence': conseq, 'terms': terms
    }

short_atoms = {a['id']: a for a in (parse_atom(c) for c in c6_raw)}
exp_atoms = {a['id']: a for a in (parse_atom(c) for c in c7_raw)}

alignments = []
align_counter = 1

def add_align(short_id, exp_id, match_type, conf, basis, shared, diff):
    global align_counter
    aid = f"ALIGN-RP-{align_counter:03d}"
    align_counter += 1
    
    t_short = short_atoms[short_id]['quote'] if short_id and short_id != 'NONE' else "NONE"
    t_exp = exp_atoms[exp_id]['quote'] if exp_id and exp_id != 'NONE' else "NONE"
    
    alignments.append({
        "ALIGN-ID": aid,
        "SOURCE-SHORT-CLAIM": short_id if short_id else "NONE",
        "SOURCE-EXP-CLAIM": exp_id if exp_id else "NONE",
        "MATCH-TYPE": match_type,
        "ALIGNMENT-CONFIDENCE": conf,
        "MATCH-BASIS": basis,
        "SHARED-LEXEMES": shared,
        "TEXT-SHORT": t_short,
        "TEXT-EXP": t_exp,
        "STRUCTURAL-DIFFERENCE": diff,
        "SEMANTIC-INTERPRETATION": "EMPTY",
        "HISTORICAL-INTERPRETATION": "EMPTY"
    })

# Mapping core Short atoms to Expanded atoms
# Art 1
add_align("HC-RP-SHORT-001A", "HC-RP-EXP-001A", "MODIFIED-WORDING", "HIGH", "lexical, actor & object",
          "оубиеть мужъ мужа, мьстити брату брата, отцю, сыну, братучадо",
          "У Короткій редакції: «или сынови отца, любо отцю сына... любо сестриноу сынови»; у Просторій: «любо отцю, ли сыну... ли братню сынови». Сестрин син у Просторій не згадується, замінено на братнього сина.")

add_align("HC-RP-SHORT-001B", "HC-RP-EXP-001B", "MODIFIED-TARIFF", "HIGH", "lexical & category",
          "аще не будеть кто мьстя, за голову, княжь мужь, тиунъ княжь",
          "Коротка редакція встановлює 40 гривень за голову загалом при відсутності месника; Простора встановлює 80 гривень вири за княжого мужа або тиуна княжого.")

add_align("HC-RP-SHORT-001B", "HC-RP-EXP-001C", "MODIFIED-WORDING", "HIGH", "lexical & social categories",
          "русинъ, гридь, купець, мечникъ, изъгои, словенинъ, 40 гривенъ положити за нь",
          "Буквальний збіг категорій (русин, гридь, купець, мечник, ізгой, словенин) і тарифу 40 гривень; у Просторій додано «любо тивунъ боярескъ», а ябетник відсутній.")

# Art 2
add_align("HC-RP-SHORT-002A", "HC-RP-EXP-023A", "MODIFIED-WORDING", "HIGH", "lexical & condition",
          "кровавъ, синь, не искати видока",
          "У Короткій: «Или боудеть кровавъ или синь надъраженъ, то не искати емоу видока человекоу томоу»; у Просторій норма об'єднана з покаранням у 3 гривні продажі.")

add_align("HC-RP-SHORT-002B", "HC-RP-EXP-023B", "MODIFIED-WORDING", "HIGH", "lexical & procedure",
          "не будеть знамения, видокъ, конець / 60 кунъ",
          "У Короткій за відсутності знамення потрібен видок, якщо не зможе — «тоу томоу конець»; у Просторій слову проти слова потрібен видок, а хто почав — платить 60 кун.")

add_align("HC-RP-SHORT-002C", "HC-RP-EXP-024A", "MODIFIED-TARIFF", "HIGH", "lexical & consequence",
          "себе не можеть мьстити, взяти за обидоу 3 гривне / лечебное, летцю мъзда",
          "У Короткій 3 гривні за обиду потерпілому і мзда лікарю; у Просторій 3 гривні продажі князю, а потерпілому гривня лічебного.")

# Art 3
add_align("HC-RP-SHORT-003A", "HC-RP-EXP-020A", "MODIFIED-WORDING", "HIGH", "lexical & objects",
          "оударить батогомъ, чашею, рогомъ, тылеснию, 12 гривенъ",
          "Перелік знарядь удару майже тотожний (батог, жердь, чаша, ріг, тилесниця); у Просторій норма доповнена дозволом на відсіч мечем.")

add_align("HC-RP-SHORT-003B", "HC-RP-EXP-020B", "MODIFIED-WORDING", "HIGH", "procedural consequence",
          "не постигнуть, платити емоу, конець / не терпя противу оударить мечемь",
          "У Короткій при недосягненні кривдника на місці — сплата і кінець; у Просторій врегульовано право вдарити у відповідь мечем без вини.")

# Art 4
add_align("HC-RP-SHORT-004A", "HC-RP-EXP-018A", "MODIFIED-WORDING", "HIGH", "lexical & penalty",
          "оударить/оутнеть мечемь не вынезъ или рукоятию, 12 гривенъ",
          "Тариф 12 гривень тотожний; у Короткій означено як «за обидоу», у Просторій як «продаже князю, а послуху 40 кунъ».")

# Art 5
add_align("HC-RP-SHORT-005A", "HC-RP-EXP-021A", "MODIFIED-TARIFF", "HIGH", "lexical & bodily damage",
          "оутнеть руку, ногу, отпадеть, 40 гривенъ / полувирье 20 гривенъ",
          "У Короткій за відсічення руки 40 гривень; у Просторій введено поняття полувир'я 20 гривен князю та 10 гривен за вік потерпілому.")

add_align("HC-RP-SHORT-005B", "HC-RP-EXP-021A", "MODIFIED-WORDING", "MEDIUM", "bodily consequence",
          "нога цела или начьнеть храмати, чада смирять / оже ли нога цела начнеть храмати",
          "У Короткій при кульганні «чада смирять»; у Просторій детерміновано фіксовану суму потерпілому за каліцтво («тому за векъ 10 гривенъ»).")

# Art 6
add_align("HC-RP-SHORT-006A", "HC-RP-EXP-022A", "MODIFIED-WORDING", "HIGH", "lexical & tariff",
          "перстъ оутнеть которыи любо, 3 гривны за обидоу / продаже",
          "Тариф 3 гривні тотожний; у Просторій додано обов'язок сплатити самому потерпілому гривну кун.")

# Art 7
add_align("HC-RP-SHORT-007A", "HC-RP-EXP-060A", "MODIFIED-WORDING", "HIGH", "lexical & bodily object",
          "во оусе 12 гривне, в бороде 12 гривне / кто порветь бородоу 12 гривенъ",
          "У Короткій фіксовано 12 гривень за вус і 12 за бороду; у Просторій 12 гривень продажі за вирвану бороду при наявності знамення і свідків.")

# Art 8
add_align("HC-RP-SHORT-008A", "HC-RP-EXP-019A", "MODIFIED-WORDING", "HIGH", "lexical action",
          "вынезь мечь а не тнеть, гривноу положить / платити гривну кунъ",
          "Майже повний текстовий збіг норми: обнаження меча без нанесення удару тягне 1 гривну.")

# Art 9
add_align("HC-RP-SHORT-009A", "HC-RP-EXP-025A", "MODIFIED-WORDING", "HIGH", "lexical action & procedure",
          "ринеть/попъхнеть мужь мужа, 3 гривне, видока два выведеть",
          "Тотожний склад дії (штовхання) і тариф 3 гривні при двох видоках; у Просторій додано удари по обличчю чи жердиною.")

add_align("HC-RP-SHORT-009B", "HC-RP-EXP-025B", "MODIFIED-WORDING", "HIGH", "lexical & procedure",
          "варягъ или колбягъ, на ротоу / полная видока, идета на роту",
          "Особливий процесуальний статус варяга та колбяга (рота) збережено в обох текстах.")

# Art 10
add_align("HC-RP-SHORT-010A", "HC-RP-EXP-026A", "MODIFIED-WORDING", "HIGH", "lexical terms & time limits",
          "челядинъ скрыется, оу варяга любо колбяга, за три дни не выведуть, 3 гривне за обидоу/продажи",
          "Строк 3 дні, право вилучити свого челядина і стягнення 3 гривень зберігаються в обох редакціях.")

# Art 11
add_align("HC-RP-SHORT-011A", "HC-RP-EXP-027A", "IDENTICAL", "HIGH", "lexical & penalty",
          "кто поедеть/всядеть на чюжемъ коне не прошавъ, положити 3 гривне",
          "Норма практично ідентична: самовільна їзда на чужому коні карається 3 гривнями.")

# Art 12
add_align("HC-RP-SHORT-012A", "HC-RP-EXP-028A", "MODIFIED-WORDING", "HIGH", "lexical terms & objects",
          "познаеть чюжь конь, оружье, портъ въ своемь миру/городе, взяти свое, 3 гривне за обиду",
          "Ідентичний перелік речей (кінь, зброя, одяг) та санкція 3 гривні; у Короткій «в своем миру», у Просторій «в своем городе».")

# Art 13
add_align("HC-RP-SHORT-013A", "HC-RP-EXP-029A", "MODIFIED-WORDING", "HIGH", "procedural formula",
          "не рци: мое, поиди на сводъ где еси взялъ",
          "Тотожна процесуальна формула початку зводу: заборона свавільного відбирання речі.")

add_align("HC-RP-SHORT-013B", "HC-RP-EXP-031A", "MODIFIED-WORDING", "MEDIUM", "procedural limit",
          "или не поидеть, поручника за пять днии / ити до конця того свода во одиномь городе",
          "У Короткій зазначено взяття поручителя на 5 днів при відмові йти на звід; у Просторій правила зводу деталізовано за міськими та міжземельними межами.")

# Art 14
add_align("HC-RP-SHORT-014A", "NONE", "OMITTED", "HIGH", "independent archaic court",
          "възыщеть на друзе проче, запирати почнеть, ити на изводъ пред 12 человека",
          "Суд 12 мужів (ізвод перед 12 чоловіка) Короткої редакції повністю відсутній у Просторій редакції.")

add_align("HC-RP-SHORT-014B", "NONE", "OMITTED", "HIGH", "independent archaic court",
          "обидя не вдалъ достоино свои скотъ, за обидоу 3 гривне",
          "Санкція за невіддання скоту за рішенням 12 мужів відсутня у Просторій.")

# Art 15
add_align("HC-RP-SHORT-015A", "HC-RP-EXP-033A", "MODIFIED-WORDING", "HIGH", "procedure of svod",
          "челядинъ пояти, вести оу кого купилъ, до третьего",
          "Процедура зводу по челядину до третього зводу збігається за суттю та послідовністю.")

add_align("HC-RP-SHORT-015B", "HC-RP-EXP-033A", "MODIFIED-WORDING", "HIGH", "procedure of svod",
          "вдаи ты мне свои челядинъ, а своего скота ищи при видоце",
          "Формула передачі челядина на третьому зводі та пошуку вартості при свідках тотожна.")

# Art 16
add_align("HC-RP-SHORT-016A", "HC-RP-EXP-058A", "MODIFIED-WORDING", "HIGH", "lexical & social actors",
          "холопъ оударить свободна мужа, бежить въ хоромъ, господинъ не выдасть, платити 12 гривенъ",
          "Повний текстовий та санкційний збіг: при укритті холопа, що вдарив вільного мужа, господин платить 12 гривень.")

add_align("HC-RP-SHORT-016B", "HC-RP-EXP-058B", "MODIFIED-WORDING", "HIGH", "retaliation right",
          "где его налезоуть оудареныи тои мужь да бьють его / оуставиша на куны любо бити розвязавше",
          "У Короткій безумовне право бити холопа де знайдуть; у Просторій зазначено зміну закону синами Ярослава (право бити або взяти гривну за сором).")

# Art 17
add_align("HC-RP-SHORT-017A", "NONE", "OMITTED", "HIGH", "property damage to weapons/clothing",
          "изломить копье, щитъ, портъ, начнеть хотети деръжати, приати скота оу него",
          "Стаття про умисне пошкодження зброї (списа, щита) чи одягу Короткої редакції відсутня у Тексті Троїцького списку.")

add_align("HC-RP-SHORT-017B", "NONE", "OMITTED", "HIGH", "property damage to weapons/clothing",
          "аще начнеть приметати то скотомъ заплатити колько далъ боудеть",
          "Правило про повернення пошкодженої зброї з доплатою скотом відсутнє у Просторій.")

# Art 18
add_align("HC-RP-SHORT-018A", "HC-RP-EXP-001B", "MODIFIED-TARIFF", "HIGH", "bloodwite tariff",
          "оубьють огнищанина въ обидоу, платити 80 гривенъ оубиици, людемъ не надобе",
          "Тариф 80 гривень за огнищанина тотожний у ст. 18 Короткої та ст. 1 / 71 Простої редакції.")

add_align("HC-RP-SHORT-018B", "HC-RP-EXP-001B", "IDENTICAL", "HIGH", "princely servant tariff",
          "въ подъездномъ княжи 80 гривенъ",
          "Тариф 80 гривень за княжого під'їздного зафіксований в обох редакціях.")

# Art 19
add_align("HC-RP-SHORT-019A", "HC-RP-EXP-003A", "MODIFIED-WORDING", "HIGH", "lexical & verv responsibility",
          "оубьють огнищанина в разбои, оубиица не ищоуть, вирное платити въ чьеи же верви голова лежить",
          "Тотожний принцип вервної (дикої) вири за вбитого в розбої, коли вбивцю не шукають.")

# Art 20
add_align("HC-RP-SHORT-020A", "HC-RP-EXP-036A", "MODIFIED-WORDING", "HIGH", "lexical & theft self-defense",
          "оубиють огнищанина/кого оу клети или оу коровье татьбы, оубити въ пса место",
          "Тотожна норма про право безкарного вбивства нічного злодія на місці злочину («во пса место»).")

add_align("HC-RP-SHORT-020B", "HC-RP-EXP-036A", "MODIFIED-WORDING", "HIGH", "tiun extension",
          "то же поконъ и тивоуницоу",
          "Поширення того самого захисту на тіуна; у Просторій узагальнено як «кого оубиють оу клети или оу которое татбы».")

# Art 21
add_align("HC-RP-SHORT-021A", "HC-RP-EXP-010A", "IDENTICAL", "HIGH", "tiun tariff",
          "въ княжи тивоуне 80 гривенъ / за тивунъ за огнищныи 80 гривенъ",
          "Тотожний тариф 80 гривень за княжого тіуна.")

add_align("HC-RP-SHORT-021B", "HC-RP-EXP-010A", "MODIFIED-WORDING", "HIGH", "historical precedence clause",
          "конюхъ старыи оу стада 80 гривенъ, яко оуставилъ Изяславъ въ своем конюсе",
          "У Короткій збережено історичну згадку про устав Ізяслава щодо коня Дорогобужців; у Просторій просто: «и за конюшии, то 80 гривенъ».")

# Art 22
add_align("HC-RP-SHORT-022A", "HC-RP-EXP-011A", "IDENTICAL", "HIGH", "village officials tariff",
          "въ сельскомъ старосте княжи и в ратаинемъ 12 гривне / в сельскомь тивуне или в ратаинемь 12 гривенъ",
          "Тотожний тариф 12 гривень за сільського чи ратайного керівника вотчини.")

add_align("HC-RP-SHORT-022B", "HC-RP-EXP-011B", "IDENTICAL", "HIGH", "ryadovich tariff",
          "в рядовници княже 5 гривенъ / за рядовича 5 гривенъ",
          "Тотожний тариф 5 гривень за рядовича.")

# Art 23
add_align("HC-RP-SHORT-023A", "HC-RP-EXP-013A", "IDENTICAL", "HIGH", "smerd tariff",
          "въ смерде 5 гривенъ / за смердии холопъ 5 гривенъ",
          "Тотожний тариф 5 гривень за смерть смерда.")

add_align("HC-RP-SHORT-023A", "HC-RP-EXP-013A", "MODIFIED-TARIFF", "HIGH", "kholop & roba tariff",
          "въ холопе 5 гривенъ / за робу 6 гривенъ",
          "У Короткій за холопа 5 гривень; у Просторій за холопа 5 гривень, а за робу 6 гривень.")

# Art 24
add_align("HC-RP-SHORT-024A", "HC-RP-EXP-014A", "IDENTICAL", "HIGH", "nurse tariff",
          "роба кормилица, любо кормиличицъ 12 / за кормилця 12, тако же и за кормилицю",
          "Тотожний тариф 12 гривень за годувальницю чи годувальника.")

# Art 25
add_align("HC-RP-SHORT-025A", "HC-RP-EXP-040A", "IDENTICAL", "HIGH", "horse tariff",
          "за княжь конь с пятномъ 3 гривне / княжь конь 3 гривны",
          "Тотожний тариф 3 гривні за княжого таврованого коня.")

add_align("HC-RP-SHORT-025A", "HC-RP-EXP-040A", "IDENTICAL", "HIGH", "smerd horse tariff",
          "за смердеи 2 гривне / за инехъ по 2 гривны",
          "Тотожний тариф 2 гривні за простого селянського коня.")

# Art 26
add_align("HC-RP-SHORT-026A", "HC-RP-EXP-041A", "MODIFIED-TARIFF", "HIGH", "cattle tariff table",
          "кобыла 60 резанъ, волъ гривна, корова 40 резанъ, третьякь 15 кунъ, лоньщина, теля, боранъ",
          "Тарифи за худобу деталізовані; у Короткій за кобилу 60 різан, у Просторій 7 кун (або 60 кун); за вола незмінно гривна, за корову 40 кун/різан.")

# Art 27
add_align("HC-RP-SHORT-027A", "NONE", "OMITTED", "HIGH", "abduction of slaves",
          "оже оуведеть чюжь холопъ, любо робоу, платити емоу за обидоу 12 гривне",
          "Пряма стаття про зведення (уведення) чужого холопа чи роби зі штрафом 12 гривень відсутня у Троїцькому списку (замінена статтями про переймання та невідання беглого холопа).")

# Art 28
add_align("HC-RP-SHORT-028A", "HC-RP-EXP-023A", "IDENTICAL", "HIGH", "wounded man exemption",
          "приидеть кровавъ мужь любо синь, не искати ему послуха",
          "Повторення норми ст. 2 Короткої Правди про звільнення побитого від свідків (дублетна стаття). У Просторій об'єднано у ст. 23.")

# Art 29
add_align("HC-RP-SHORT-029A", "HC-RP-EXP-037A", "MODIFIED-TARIFF", "HIGH", "theft penalty single thief",
          "крадеть конь, волы, клеть, единъ кралъ: гривноу и 30 резанъ / 3 гривны и 30 кунъ",
          "У Короткій 1 гривна і 30 різан; у Просторій 3 гривни і 30 кун за крадіжку худоби в хліві чи з клети для одного злодія.")

add_align("HC-RP-SHORT-029B", "HC-RP-EXP-037B", "MODIFIED-WORDING", "HIGH", "gang theft penalty",
          "ихъ будеть 18, по три гривне и по 30 резанъ / будеть их много всемъ по 3 гривны и 30 кунъ",
          "У Короткій зазначено фіксовану кількість співучасників («18»), у Просторій генералізовано («будеть ли их много, всемъ»).")

# Art 30
add_align("HC-RP-SHORT-030A", "HC-RP-EXP-068A", "MODIFIED-WORDING", "HIGH", "bort damage",
          "въ княже борти 3 гривне, пожгоуть, изоудроуть / борть подътнеть 3 гривны продаже",
          "Тариф 3 гривні за пошкодження борті зберігається в обох редакціях.")

# Art 31
add_align("HC-RP-SHORT-031A", "HC-RP-EXP-071A", "MODIFIED-WORDING", "HIGH", "torture of smerd",
          "смердъ оумоучать безъ княжа слова, за обиду 3 гривны / смердъ мучить смерда без княжа слова, 3 гривны продажи, за муку гривна кунъ",
          "У Короткій 3 гривні за обиду за катування смерда без княжого наказу; у Просторій 3 гривні продажі князю та гривна кун за муку.")

# Art 32
add_align("HC-RP-SHORT-032A", "HC-RP-EXP-072A", "MODIFIED-WORDING", "HIGH", "torture of ognishchanin",
          "въ огнищанине, въ тивоунице, въ мечници 12 гривъне / аже огнищанина мучить, 12 гривенъ продаже, за муку гривна",
          "У Короткій 12 гривень за образу/катування вогнищанина, тіуна чи мечника; у Просторій деталізовано як 12 гривень продажі та гривна за муку.")

# Art 33
add_align("HC-RP-SHORT-033A", "HC-RP-EXP-065A", "IDENTICAL", "HIGH", "boundary violation penalty",
          "межоу переореть либо перетесъ, за обидоу 12 гривне / межю перетнеть, разореть, 12 гривенъ продажи",
          "Тотожний тариф 12 гривень за пошкодження межі (ролейної, бортної чи двірної).")

# Art 34
add_align("HC-RP-SHORT-034A", "HC-RP-EXP-073A", "MODIFIED-TARIFF", "HIGH", "boat theft penalty",
          "лодью оукрадеть, за лодью платити 30 резанъ, а продажи 60 резанъ / 60 кунъ продаже, лодию лицемь воротити, морьскую 3 гривны",
          "У Короткій 30 різан за лодь і 60 різан продажі; у Просторій 60 кун продажі князю, повернення лоді обличчям та градація (морська 3 гривни, набійна 2 гривни, човен 20 кун, струг гривна).")

# Art 35
add_align("HC-RP-SHORT-035A", "HC-RP-EXP-076A", "IDENTICAL", "HIGH", "bird theft tariff",
          "въ голоубе и въ коуряти 9 коунъ / за голубь 9 кунъ, за куря 9 кунъ",
          "Тотожний тариф 9 кун за голуба і курку.")

# Art 36
add_align("HC-RP-SHORT-036A", "HC-RP-EXP-077A", "MODIFIED-WORDING", "HIGH", "waterfowl theft tariff",
          "въ оутке, въ гоусе, въ жераве, въ лебеди 30 резанъ, продажи 60 резанъ / за гусь 30 кунъ, за лебедь 30 кунъ, за жеравль 30 кунъ",
          "Тариф відшкодування 30 кун/різан за птицю зберігається.")

# Art 37
add_align("HC-RP-SHORT-037A", "HC-RP-EXP-075A", "MODIFIED-WORDING", "HIGH", "hunting dog/bird theft",
          "чюжь песъ, ястребъ, соколъ, за обидоу 3 гривны / ястрябъ или соколъ продаже 3 гривны, а господину гривна",
          "У Короткій 3 гривні за обиду за пса, яструба чи сокола; у Просторій 3 гривні продажі та гривна господину.")

# Art 38
add_align("HC-RP-SHORT-038A", "HC-RP-EXP-036A", "IDENTICAL", "HIGH", "killing thief at night",
          "оубьють татя на своемъ дворе, оу клети, оу хлева то тои оубитъ / оубиють во пса место",
          "Тотожне визнання законним убивства нічного злодія на місці вчинення злочину.")

add_align("HC-RP-SHORT-038B", "HC-RP-EXP-036B", "IDENTICAL", "HIGH", "bringing thief at dawn",
          "до света держать, то вести его на княжь дворъ / додержать света, вести на княжь дворъ",
          "Тотожний обов'язок вести злодія на княжий двір, якщо затримано живим до світанку.")

add_align("HC-RP-SHORT-038C", "HC-RP-EXP-036B", "MODIFIED-TARIFF", "HIGH", "killing tied thief",
          "оже оубьють а люди боудоуть видели связанъ то платити в немь / платити в томь 12 гривенъ",
          "У Короткій «платити в немь» (за голову); у Просторій зафіксовано точний штраф 12 гривень.")

# Art 39
add_align("HC-RP-SHORT-039A", "HC-RP-EXP-078A", "IDENTICAL", "HIGH", "hay/wood theft",
          "сено крадоуть 9 коунъ, въ дровехъ 9 коунъ / въ сене и въ дровехъ 9 кунъ",
          "Тотожний тариф 9 кун за крадіжку сіна чи дров; у Просторій додано плату по 2 ногати за віз господину.")

# Art 40
add_align("HC-RP-SHORT-040A", "HC-RP-EXP-038A", "MODIFIED-WORDING", "HIGH", "small livestock theft",
          "оукрадоуть овъцоу, козоу, свинью, 10 оукрале по 60 резанъ продажи / скотъ на поли овце козы свиньи 60 кунъ, будеть их много то всемъ по 60",
          "Тотожний тариф 60 різан/кун продажі з кожного співучасника крадіжки дрібної худоби.")

add_align("HC-RP-SHORT-040B", "NONE", "OMITTED", "HIGH", "thief catcher reward",
          "а хто изималъ, томоу 10 резанъ",
          "Винагорода тому, хто затримав злодія (10 різан), відсутня у відповідній статті Простої редакції.")

# Art 41
add_align("HC-RP-SHORT-041A", "HC-RP-EXP-082A", "MODIFIED-TARIFF", "MEDIUM", "court fee distribution",
          "от гривни мечникоу коуна, в десятиноу 15 коунъ, князю 3 гривны / железного платити 40 кунъ, мечнику 5 кунъ",
          "Розподіл судових зборів між князем, мечником та десятиною; у Просторій перероблено на залізний урок та наклади.")

add_align("HC-RP-SHORT-041B", "HC-RP-EXP-067A", "MODIFIED-TARIFF", "MEDIUM", "court fee from 12 grivnas",
          "от 12 гривноу емъцю 70 коунъ, в десятину 2 гривне, князю 10 гривенъ / наклады 12 гривенъ, отроку 2 гривны и 20 кунъ, писцю 10 кунъ",
          "Розподіл збору від 12 гривень продажі перероблено в Просторій у систему накладів (ст. 67).")

# Art 42
add_align("HC-RP-SHORT-042A", "HC-RP-EXP-007A", "MODIFIED-WORDING", "HIGH", "virnik rations table",
          "вирникоу взяти 7 ведоръ солодоу, овенъ, полотъ, две ногате, сыры, куры, 4 коне овесъ / вирнику взяти 7 ведеръ солоду, овенъ, куна же сыръ, куръ по двою",
          "Майже дослівний збіг раціону утримання вірника (поклон вірний при Ярославі).")

add_align("HC-RP-SHORT-042B", "HC-RP-EXP-007A", "MODIFIED-TARIFF", "HIGH", "virnik money fee",
          "вирникоу 60 гривенъ и 10 резанъ и 12 веверици, переде гривна, в говение за рыбы 7 резанъ / вирнику 8 гривенъ а 10 кунъ перекладная, съсадная гривна",
          "Грошовий збір вірника: у Короткій зафіксовано сукупний обсяг («60 гривенъ и 10 резанъ и 12 веверици»), у Просторій реформовано на 8 гривень (при 40-гривневій вирі) та 16 гривень (при 80-гривневій).")

# Art 43
add_align("HC-RP-SHORT-043A", "HC-RP-EXP-091A", "MODIFIED-WORDING", "HIGH", "bridge master fee",
          "урокъ мостьниковъ, помостивше мостъ взяти от дела ногата, от городници ногата / мостнику оуроци: помостивше мостъ взяти от 10 локотъ по ногате",
          "Оплата праці мостників за будівництво нового мосту: перехід від оплати за городницю до оплати від 10 ліктів мосту.")

add_align("HC-RP-SHORT-043B", "HC-RP-EXP-091A", "MODIFIED-WORDING", "HIGH", "bridge master repair fee",
          "ветхаго моста подтвердити неколико доскъ 3, 4 или 5 то тое же / починивше мостъ колико городниць, то взяти по ногате",
          "Оплата за ремонт старого моста збережена в обох редакціях.")

# Now for ADDED atoms in RP Expanded (innovations of Expanded recension not present in Short)
# Let's see which Expanded atoms had no Short precursor:
mapped_exp_ids = set(a['SOURCE-EXP-CLAIM'] for a in alignments if a['SOURCE-EXP-CLAIM'] != 'NONE')

print(f"Total alignments from Short mapped: {len(alignments)}")
print(f"Total unique Expanded atoms mapped: {len(mapped_exp_ids)}")

all_exp_ids = sorted(exp_atoms.keys())
added_exp_ids = [eid for eid in all_exp_ids if eid not in mapped_exp_ids]
print(f"Total unmapped Expanded atoms (ADDED in Exp): {len(added_exp_ids)}")

for eid in added_exp_ids:
    e_art = exp_atoms[eid]['article']
    e_q = exp_atoms[eid]['quote']
    e_obj = exp_atoms[eid]['object']
    add_align(None, eid, "ADDED", "HIGH", "independent article in Expanded recension",
              "NONE", f"Атом відсутній у Короткій редакції Руської Правди; являє собою розширення правового регулювання Простої редакції ({e_art}).")

print(f"Total alignment entries generated: {len(alignments)}")

