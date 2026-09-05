# -*- coding: utf-8 -*-
"""
Applies final calibration patch to dictionary/PRAVDA.md and dictionary/ROTA.md:
1. Split every Usage-Grammar block into:
   - OPERATOR-SOURCE / OPERATOR-GLOSS
   - ACTOR-SOURCE / ACTOR-RECONSTRUCTION
   - COMPLEMENT-SOURCE / COMPLEMENT-GLOSS
   - CONDITION-SOURCE / CONDITION-RECONSTRUCTION
   - CONSEQUENCE-SOURCE / CONSEQUENCE-INFERENCE
2. Remove modern legal categories from OBSERVED claims (e.g. 'неделіктоздатність', 'легітимація').
3. Do not silently translate:
   - 'выдавати' -> 'зачитувати' (keep as issue/deliver/hand over with lexical support noted).
   - 'правда' -> 'judicial protection' (keep source-near).
4. Add CLAIM-DEPENDENCY: explicit provenance and observation links for senses and diachronic hypotheses.
5. Calibrate method statement: "Method calibrated on two pilot entries; remaining error modes may emerge."
"""

# ----------------- PATCH PRAVDA.md -----------------
with open('dictionary/PRAVDA.md', 'r', encoding='utf-8') as f:
    p_text = f.read()

pravda_new_grammar = """### 5. РІВЕНЬ 6: ОПЕРАЦІЙНА ГРАМАТИКА ТА РЕЄСТР ТВЕРДЖЕНЬ (USAGE-GRAMMAR & CLAIMS)

> **МЕТОДОЛОГІЧНЕ РОЗМЕЖУВАННЯ В ГРАМАТИЦІ:**
> ```text
> SOURCE-OBSERVED (буквально присутнє в тексті)
>         ≠
> CONTEXT-RECONSTRUCTED (відновлене з найближчого синтаксичного контексту)
>         ≠
> GLOSS (значення за історичним словником)
>         ≠
> RESEARCH-INFERENCE (дослідницька реконструкція інституційного наслідку)
> ```

#### А. Операційна граматика слововжитку (Usage-Grammar):

1. **`правду железо`** (`SRC-RP-EXP` ряд. 65, ст. 17):
   - **OPERATOR-SOURCE:** `[еліпсис]` (відсутнє дієслово в реченні)
   - **OPERATOR-RECONSTRUCTION:** `[призначатися / бути способом доказу]` [INFERENCE]
   - **ACTOR-SOURCE:** `[не названий у виразі]`
   - **ACTOR-RECONSTRUCTION:** Сторони спору («имъ»), суд [CONTEXT-RECONSTRUCTED]
   - **COMPLEMENT-SOURCE:** `правду` (знахідний відмінок)
   - **COMPLEMENT-GLOSS:** «оправданіе, очищеніе присягою или желЂзомъ» [LEX-EVID-003, LEX-EVID-004]
   - **INSTRUMENT-SOURCE:** `железо`
   - **INSTRUMENT-GLOSS:** судове випробування розпеченим залізом (ордалія) [LEX-EVID-004]
   - **CONDITION-SOURCE:** *«Искавше ли послуха, не налезуть, а истьця начнеть головою клепати»* (свідка немає, звинувачення у вбивстві) [SOURCE-OBSERVED]
   - **CONSEQUENCE-INFERENCE:** Проходження випробування залізом визначає правоту однієї зі сторін [RESEARCH-INFERENCE].

2. **`дати емоу правдоу`** (`SRC-RP-EXP` ряд. 172, ст. 52):
   - **OPERATOR-SOURCE:** `дати` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `[не названий у підрядній частині; контекстуально: влада / господар]` [CONTEXT-RECONSTRUCTED]
   - **RECIPIENT-SOURCE:** `емоу` (закупникові) [SOURCE-OBSERVED]
   - **OBJECT-SOURCE:** `правдоу` [SOURCE-OBSERVED]
   - **OBJECT-GLOSS:** «суд, судебное разбирательство» [LEX-EVID-004: СДРЯ Т. VII, с. 342]
   - **CONDITION-SOURCE:** *«Аже закупъ бежить от господы... идеть ли искатъ кунъ, а явлено ходить, или ко князю или к судьямъ бежить обиды деля своего господина»* [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** *«то про то не робять его»* (не обертають у повного холопа) [SOURCE-OBSERVED].

3. **`на правду не вылазити`** (`SRC-RP-EXP` ряд. 258, ст. 81):
   - **OPERATOR-SOURCE:** `не вылазити` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `холопу` [SOURCE-OBSERVED]
   - **COMPLEMENT-SOURCE:** `на правду` [SOURCE-OBSERVED]
   - **COMPLEMENT-GLOSS:** участь у судовому очищенні / свідчення [LEX-EVID-003]
   - **CONDITION-SOURCE:** *«будеть ли послухъ холопъ»* (холопа виставлено свідком) [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** Свідчення холопа не допускається, окрім випадку прямої згоди позивача (*«но оже хощеть истець...»*) [SOURCE-OBSERVED].

4. **`ку правде склонъные`** (`SRC-LS-1588` ряд. 4584, розд. 11 ст. 7):
   - **OPERATOR-SOURCE:** `прихилятисе` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `вряд нашъ` (судовий урядник) [SOURCE-OBSERVED]
   - **COMPLEMENT-SOURCE:** `ку правде` [SOURCE-OBSERVED]
   - **COMPLEMENT-GLOSS:** «до істини / доведеності злочину» [LEX-EVID-006]
   - **CONDITION-SOURCE:** *«припатруючися и уважаючи пилне и бачне часъ, местце, знаки подобенства и всякие иные причины»* [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** Купець допускається до присяги з меншим числом співприсяжників (*«самотреть»*) [SOURCE-OBSERVED].

5. **`правды ся выведывати`** (`SRC-LS-1588` ряд. 4984, розд. 11 ст. 25):
   - **OPERATOR-SOURCE:** `выведывати ся` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `шкрутаторове` (офіційні слідчі) [SOURCE-OBSERVED]
   - **OBJECT-SOURCE:** `правды` [SOURCE-OBSERVED]
   - **OBJECT-GLOSS:** фактичні обставини скоєного злочину («правдиве сознати то, чого будутъ сведоми») [LEX-EVID-006]
   - **CONDITION-SOURCE:** Слідчий виїзд на місце події [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** Складання письмового звіту під печатками шляхти і возного [SOURCE-OBSERVED].

6. **`чтоб делали правду`** (`SRC-MARCH-1654` ряд. 24, ст. 3):
   - **OPERATOR-SOURCE:** `делали` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `присланые люди / зборщики` [SOURCE-OBSERVED]
   - **OBJECT-SOURCE:** `правду` [SOURCE-OBSERVED]
   - **OBJECT-GLOSS:** чесне виконання без здирництва («правду робити — чинити справедливість») [LEX-EVID-007]
   - **CONDITION-SOURCE:** Збір грошових і хлібних доходів на царське величество [SOURCE-OBSERVED]
   - **CONSEQUENCE-RECONSTRUCTION:** Запобігання зловживанням при оподаткуванні [RESEARCH-INFERENCE].

---

#### Б. Реєстр наукових тверджень та ланцюжки виведення (Claim Dependency Ledger):

- **PRAVDA-USAGE-001 (OBSERVED):** У тексті Просторого списку Руської Правди (ст. 17) вираз «правду железо» синтаксично поєднує іменник «правду» з іменником «железо» в контексті відсутності свідка при звинуваченні у вбивстві. [PRIMARY]
- **PRAVDA-USAGE-002 (OBSERVED):** У тексті Просторого списку (ст. 52) засвідчено конструкцію «дати емоу правдоу» щодо закупа, який шукає судового розгляду проти господаря. [PRIMARY]
- **PRAVDA-USAGE-003 (OBSERVED):** У тексті Просторого списку (ст. 81) засвідчено заборону «холопу на правду не вылазити» у випадку залучення холопа як послуха. [PRIMARY]
- **PRAVDA-USAGE-004 (OBSERVED):** У тексті Литовського Статуту 1588 року іменник «правда» зафіксовано в контекстах слідчого допиту: «ку правде склонъные» (розд. 11 ст. 7) та «правды ся выведывати» (розд. 11 ст. 25). [PRIMARY]
- **PRAVDA-USAGE-005 (OBSERVED):** У Березневих статтях 1654 року зафіксовано вимогу «чтоб делали правду» до збирачів доходів. [PRIMARY]

- **PRAVDA-SENSE-001 (SENSE CANDIDATE / PROVISIONAL):**
  - **CLAIM:** У Руській Правді слово «правда» вживається не як абстрактне етичне поняття, а як технічний процесуальний засіб вирішення спору (ордалія або судове свідчення).
  - **CLAIM-DEPENDENCY:**
    - Базується на: [PRIMARY: `PRAVDA-USAGE-001`, `PRAVDA-USAGE-002`, `PRAVDA-USAGE-003`].
    - Підтверджено лексикографією: [HISTORICAL-DICTIONARY: `LEX-EVID-003`, `LEX-EVID-004`].
  - **STATUS:** `PROVISIONAL SENSE CANDIDATE`

- **PRAVDA-DIA-001 (DIACHRONIC HYPOTHESIS):**
  - **CLAIM:** В обстеженому корпусі спостерігається зміна граматичного оточення: у давньоруських нормах «правда» є самостійною процесуальною подією («правду железо», «дати правду»), тоді як у текстах XVI–XVIII ст. вона функціонує переважно як об'єкт слідчого з'ясування обставин («правды ся выведывати») або модус чесного виконання посадових дій («делали правду»).
  - **CLAIM-DEPENDENCY:**
    - Базується на зіставленні: [PRIMARY: `PRAVDA-USAGE-001..003` vs `PRAVDA-USAGE-004..005`].
    - Лексикографічна підтримка: [`LEX-EVID-005`, `LEX-EVID-006`, `LEX-EVID-007`].
  - **STATUS:** `PROVISIONAL HYPOTHESIS`
"""

start_p = "### 5. РІВЕНЬ 6: ОПЕРАЦІЙНА ГРАМАТИКА"
end_p = "### 6. РІВЕНЬ 7: ПОРІВНЯННЯ ДОСЛІДЖУВАНОЇ ПАРИ"
if start_p in p_text and end_p in p_text:
    part1 = p_text.split(start_p)[0]
    part2 = p_text.split(end_p)[1]
    with open('dictionary/PRAVDA.md', 'w', encoding='utf-8') as f:
        f.write(part1 + pravda_new_grammar + "\n---\n\n### 6. РІВЕНЬ 7: ПОРІВНЯННЯ ДОСЛІДЖУВАНОЇ ПАРИ" + part2)
    print("PRAVDA.md patched with calibrated grammar and claim dependencies.")

# ----------------- PATCH ROTA.md -----------------
with open('dictionary/ROTA.md', 'r', encoding='utf-8') as f:
    r_text = f.read()

rota_new_grammar = """### 5. РІВЕНЬ 6: ОПЕРАЦІЙНА ГРАМАТИКА ТА РЕЄСТР ТВЕРДЖЕНЬ (USAGE-GRAMMAR & CLAIMS)

> **МЕТОДОЛОГІЧНЕ РОЗМЕЖУВАННЯ В ГРАМАТИЦІ:**
> ```text
> SOURCE-OBSERVED (буквально присутнє в тексті)
>         ≠
> CONTEXT-RECONSTRUCTED (відновлене з найближчого синтаксичного контексту)
>         ≠
> GLOSS (значення за історичним словником)
>         ≠
> RESEARCH-INFERENCE (дослідницька реконструкція інституційного наслідку)
> ```

#### А. Операційна граматика слововжитку (Usage-Grammar):

1. **`то на ротоу`** (`SRC-RP-SHORT` ряд. 28, ст. 10):
   - **OPERATOR-SOURCE:** `[еліпсис]` (відсутнє дієслово руху в реченні)
   - **OPERATOR-RECONSTRUCTION:** `[іти / ставати на присягу]` [CONTEXT-RECONSTRUCTED]
   - **ACTOR-SOURCE:** `варягъ или колбягъ` [SOURCE-OBSERVED]
   - **COMPLEMENT-SOURCE:** `на ротоу` [SOURCE-OBSERVED]
   - **COMPLEMENT-GLOSS:** «клятва, судебная присяга» [LEX-EVID-009, LEX-EVID-010]
   - **CONDITION-SOURCE:** *«аще боудеть роусинъ... а выведеть; или боудеть варягъ или колбягъ»* (відсутність свідків-видоків) [SOURCE-OBSERVED]
   - **CONSEQUENCE-INFERENCE:** Складання клятви розв'язує спір за відсутності сторонніх свідків [RESEARCH-INFERENCE].

2. **`роте ему ити по свое куны`** (`SRC-RP-EXP` ряд. 65, ст. 17):
   - **OPERATOR-SOURCE:** `ити` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `ему` (позивачеві / кредитору) [SOURCE-OBSERVED]
   - **COMPLEMENT-SOURCE:** `роте` (давальний/місцевий відмінок) [SOURCE-OBSERVED]
   - **OBJECT-SOURCE:** `по свое куны` [SOURCE-OBSERVED]
   - **CONDITION-SOURCE:** *«аже мене [дву гривенъ]»* (сума позову менше двох гривень) [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** Позивач іде на клятву для повернення своїх грошей [SOURCE-OBSERVED].

3. **`послуси поидуть на роту`** (`SRC-RP-EXP` ряд. 141, ст. 43):
   - **OPERATOR-SOURCE:** `поидуть` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `послуси` (свідки) [SOURCE-OBSERVED]
   - **COMPLEMENT-SOURCE:** `на роту` [SOURCE-OBSERVED]
   - **CONDITION-SOURCE:** *«Аже кто взищеть кунъ на друзе, а онъ ся начнеть запирати, то оже на нь выведеть послуси»* [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** *«а онъ возметь свое куны»* (стягнення заборгованості) [SOURCE-OBSERVED].

4. **`роту тое присеги от писара взявши`** (`SRC-LS-1588` ряд. 2156, розд. 4 ст. 67):
   - **OPERATOR-SOURCE:** `взявши` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `сторона противная, противъ которое маеть быти прысега чинена` [SOURCE-OBSERVED]
   - **SOURCE-OF-ITEM:** `от писара с подъписью руки его` [SOURCE-OBSERVED]
   - **OBJECT-SOURCE:** `роту тое присеги` [SOURCE-OBSERVED]
   - **OBJECT-GLOSS:** «текст або формула присяги» [LEX-EVID-011: СЛМ Вип. 31, с. 61]
   - **CONDITION-SOURCE:** Суд відклав присягу на третій день [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** Сторона веде свого опонента до присяги перед возним та двома шляхтичами [SOURCE-OBSERVED].

5. **`возный роту выдавати маеть`** (`SRC-LS-1588` ряд. 2156, розд. 4 ст. 67):
   - **OPERATOR-SOURCE:** `выдавати` [SOURCE-OBSERVED]
   - **OPERATOR-GLOSS:** видавати, вручати, оголошувати формулу присяги [LEX-EVID-011: вимагає текстового розрізнення між фізичною видачею аркуша та усним проголошенням]
   - **ACTOR-SOURCE:** `возный` [SOURCE-OBSERVED]
   - **OBJECT-SOURCE:** `роту` [SOURCE-OBSERVED]
   - **CONDITION-SOURCE:** Проведення процедури присяги на третій день перед судом [SOURCE-OBSERVED]
   - **CONSEQUENCE-RECONSTRUCTION:** Забезпечення офіційного тексту клятви для особи, що присягає [RESEARCH-INFERENCE].

6. **`присегу вделати ротою судьи земъского`** (`SRC-LS-1588` ряд. 1604, розд. 4 ст. 25):
   - **OPERATOR-SOURCE:** `вделати` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** `староста замъковъ и дворовъ нашихъ судовыхъ` [SOURCE-OBSERVED]
   - **OBJECT-SOURCE:** `присегу на суды` [SOURCE-OBSERVED]
   - **INSTRUMENT-SOURCE:** `ротою судьи земъского` [SOURCE-OBSERVED]
   - **INSTRUMENT-GLOSS:** нормативний текст присяги за зразком земського судді [LEX-EVID-011]
   - **CONDITION-SOURCE:** Початок виконання судових обов'язків [SOURCE-OBSERVED]
   - **CONSEQUENCE-SOURCE:** *«а поколь того не учинить, потуль врядомъ своимъ шафовати не можеть»* [SOURCE-OBSERVED].

7. **`вεдлугъ роты публичнε үхвалεной выконати`** (`SRC-ORLYK-1710` ряд. 198, ст. 6):
   - **OPERATOR-SOURCE:** `выконати` [SOURCE-OBSERVED]
   - **ACTOR-SOURCE:** Старшини та радники перед вступом до ради [CONTEXT-RECONSTRUCTED]
   - **OBJECT-SOURCE:** `формалную присягу` [SOURCE-OBSERVED]
   - **STANDARD-SOURCE:** `вεдлугъ роты публичнε үхвалεной` [SOURCE-OBSERVED]
   - **STANDARD-GLOSS:** «ведлуг формули присяги» [LEX-EVID-012: Тимченко Т. 2, с. 720]
   - **CONSEQUENCE-SOURCE:** Участь у справах Генеральної Ради [CONTEXT-RECONSTRUCTED].

---

#### Б. Реєстр наукових тверджень та ланцюжки виведення (Claim Dependency Ledger):

- **ROTA-USAGE-001 (OBSERVED):** У Руській Правді (XI–XV ст.) слово `рота` сполучається виключно з дієсловами пересування та процесуального стану («ити на роту», «поидуть на роту», «роте ити»). [PRIMARY]
- **ROTA-USAGE-002 (OBSERVED):** У Литовському Статуті 1588 року слово `рота` сполучається з дієсловами отримання та надання матеріального об'єкта («взявши от писара с подъписью», «выдавати»), а також виступає в орудному відмінку як нормативний зразок («ротою судьи земъского»). [PRIMARY]
- **ROTA-USAGE-003 (OBSERVED):** У Бендерській конституції 1710 року слово `рота` виступає об'єктом відповідності у прийменниковій конструкції («вεдлугъ роты публичнε үхвалεной») при дієслові «присягу выконати». [PRIMARY]

- **ROTA-PRISYAGA-COOCCUR-001 (OBSERVED FACT):** У тексті Статуту 1588 р. лексеми `рота` і `присяга` зафіксовані в межах спільних синтаксичних комплексів (рядки 1344, 1604, 2156, 3728), де `присяга` є обов'язком або дією, а `рота` — приписаним текстом формули. [PRIMARY]

- **ROTA-SENSE-001 (SENSE CANDIDATE / PROVISIONAL):**
  - **CLAIM:** У текстах XI–XV ст. (Руська Правда) референтом слова `рота` є усна ритуальна дія принесення судової клятви перед громадою та Богом.
  - **CLAIM-DEPENDENCY:**
    - Базується на: [PRIMARY: `ROTA-USAGE-001`].
    - Підтверджено словниками: [HISTORICAL-DICTIONARY: `LEX-EVID-009`, `LEX-EVID-010`].
  - **STATUS:** `PROVISIONAL SENSE CANDIDATE`

- **ROTA-SENSE-002 (SENSE CANDIDATE / PROVISIONAL):**
  - **CLAIM:** У пам'ятках 1588 та 1710 років референтом слова `рота` виступає приписаний формуляр або текст присяги, який отримують від писаря або за яким урядовець виконує присягу.
  - **CLAIM-DEPENDENCY:**
    - Базується на: [PRIMARY: `ROTA-USAGE-002`, `ROTA-USAGE-003`, `ROTA-PRISYAGA-COOCCUR-001`].
    - Підтверджено словниками: [HISTORICAL-DICTIONARY: `LEX-EVID-011`, `LEX-EVID-012`].
  - **STATUS:** `PROVISIONAL SENSE CANDIDATE`

- **ROTA-DIA-001 (DIACHRONIC HYPOTHESIS):**
  - **CLAIM:** В обстеженому корпусі спостерігається зміна синтаксичної поведінки слова: від назви самої судової дії (іти на роту) до позначення матеріального документа / формуляра клятви (роту взяти від писаря, присягати ротою судді), тоді як функцію позначення загальної дії клятви перебрало на себе дієслово `присягати`.
  - **CLAIM-DEPENDENCY:**
    - Базується на зіставленні: [PRIMARY: `ROTA-USAGE-001` vs `ROTA-USAGE-002..003`].
    - Лексикографічна підтримка: [`LEX-EVID-009`, `LEX-EVID-011`].
  - **STATUS:** `PROVISIONAL HYPOTHESIS`
"""

start_r = "### 5. РІВЕНЬ 6: ОПЕРАЦІЙНА ГРАМАТИКА"
end_r = "### 6. РІВЕНЬ 7: ПОРІВНЯННЯ ДОСЛІДЖУВАНОЇ ПАРИ"
if start_r in r_text and end_r in r_text:
    r_part1 = r_text.split(start_r)[0]
    r_part2 = r_text.split(end_r)[1]
    with open('dictionary/ROTA.md', 'w', encoding='utf-8') as f:
        f.write(r_part1 + rota_new_grammar + "\n---\n\n### 6. РІВЕНЬ 7: ПОРІВНЯННЯ ДОСЛІДЖУВАНОЇ ПАРИ" + r_part2)
    print("ROTA.md patched with calibrated grammar and claim dependencies.")
