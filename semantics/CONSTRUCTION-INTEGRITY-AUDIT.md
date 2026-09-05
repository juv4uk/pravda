# АУДИТ ЦІЛІСНОСТІ ТА МАТРИЦЯ СИНТАКСИЧНИХ КОНСТРУКЦІЙ (ВЕРСІЯ 2 — CALIBRATED)
## CONSTRUCTION-INTEGRITY-AUDIT.md (Rigorous Boundaries, Explicit Rules, Three-Tier Metrics)

> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ЕПІСТЕМОЛОГІЧНІ ІНВАРІАНТИ:**
> 1. **FORMAL PATTERNS OVER INTERPRETIVE LABELS**:
>    Кожна конструкція ідентифікується за суворим синтаксичним шаблоном (предикат, прийменник, відмінок, зв'язка). Назви конструкцій є суто дескриптивними формулами форми, а не змістовними визначеннями.
> 2. **THREE-TIER SEPARATED METRICS**:
>    - `TOKEN-COUNT`: кількість окремих лексемних входжень (словоформ), охоплених конструкцією.
>    - `CONSTRUCTION-INSTANCE-COUNT`: кількість окремих підтверджених фактів спрацювання правила конструкції.
>    - `SENTENCE-COUNT`: кількість унікальних текстових речень / артикулів / рядків джерела.
> 3. **RULE-BASED MANY-TO-MANY MULTI-MEMBERSHIP**:
>    Один токен може одночасно належати до кількох рамок ЛИШЕ за наявності окремого документального доказу для кожного правила (`MATCH-RULE-ID` + `MATCH-EVIDENCE`). Жодного включення за «тематичною спорідненістю».
> 4. **PROVISIONAL STATUS OF CAUSALITY (CORRELATION ≠ CAUSATION)**:
>    Збіг певної конструкції з певним жанром чи епохою фіксується як емпірична кореляція. Будь-які твердження про жанрову зумовленість маркуються строго як `GENRE-HYPOTHESIS` (PROVISIONAL).

---

## 1. РЕЄСТР АУДИТОВАНИХ КОНСТРУКЦІЙ (AUDITED CONSTRUCTIONS 01–13)

### CONST-SVOB-001 — `ADJ-ATTR: свободный + [мужь / люди / послухи]`
- **КЛЮЧОВИЙ ТЕРМІН:** `СВОБОДНЫЙ (ADJ)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `ADJ-ATTR: свободный + [мужь / люди / послухи]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Прикметник свободный (короткий або повний) виступає атрибутивним означенням при іменниках зі значенням людини чи соціальної групи.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Субстантивовані вживання без референта-людини або предикативні форми іменника свобода.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **5**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **5**
  - **`SENTENCE-COUNT`:** **5**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Особистий соціально-юридичний статус не-холопа. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Базова дихотомія давньоруського права між вільною людиною та об'єктом власності. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0022]` **`SRC-RP-EXP`** (рядок 105) | форма: `свободна`
    - **MATCH-RULE-ID:** `SVOB-R01-ADJ-PERSON`
    - **MATCH-EVIDENCE:** Adjectival token 'свободна' (POS=ADJ) directly modifies personal noun/status in span: «...гу, или конь, или портъ, или скотину, то выведеть свободна мужа два»
  - `[LEX-INV2-0034]` **`SRC-RP-EXP`** (рядок 182) | форма: `свободнемь`
    - **MATCH-RULE-ID:** `SVOB-R01-ADJ-PERSON`
    - **MATCH-EVIDENCE:** Adjectival token 'свободнемь' (POS=ADJ) directly modifies personal noun/status in span: «...иеть ли не смысля пьянъ, а без вины, то яко же въ свободнемь платеж»
  - `[LEX-INV2-0038]` **`SRC-RP-EXP`** (рядок 194) | форма: `свободна`
    - **MATCH-RULE-ID:** `SVOB-R01-ADJ-PERSON`
    - **MATCH-EVIDENCE:** Adjectival token 'свободна' (POS=ADJ) directly modifies personal noun/status in span: «58. А се аже холопъ оударить свободна мужа, а оубежить в хоромъ, а гос»
  - `[LEX-INV2-0042]` **`SRC-RP-EXP`** (рядок 260) | форма: `свободныхъ`
    - **MATCH-RULE-ID:** `SVOB-R01-ADJ-PERSON`
    - **MATCH-EVIDENCE:** Adjectival token 'свободныхъ' (POS=ADJ) directly modifies personal noun/status in span: «...окъ, кто си в чемь емлеть. Аже иметь на железо по свободныхъ людии »
  - `[LEX-INV2-0058]` **`SRC-RP-EXP`** (рядок 348) | форма: `свободнии`
    - **MATCH-RULE-ID:** `SVOB-R01-ADJ-PERSON`
    - **MATCH-EVIDENCE:** Adjectival token 'свободнии' (POS=ADJ) directly modifies personal noun/status in span: «...выдати, паки ли а выкупаеть господинъ; аже будуть свободнии с нимь »

---

### CONST-SVOB-002 — `INS.PL-PRED: судять послухи свободными`
- **КЛЮЧОВИЙ ТЕРМІН:** `СВОБОДНЫЙ (ADJ)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `INS.PL-PRED: судять послухи свободными`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Орудний відмінок множини свободными у складі судового правила оцінки свідків із прямою опозицією до холопа.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Інші вживання прикметника свободный поза нормативною формулою дієздатності свідка.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **1**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **1**
  - **`SENTENCE-COUNT`:** **1**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Вимога особистої свободи як передумова правоздатності свідчити на суді. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Процесуальна ізоляція невільного населення від сакральної дії присяги. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0041]` **`SRC-RP-EXP`** (рядок 258) | форма: `свободными`
    - **MATCH-RULE-ID:** `SVOB-R02-INS-WITNESS`
    - **MATCH-EVIDENCE:** Token 'свободными' functions as instrumental predicate complement defining witness qualification in span: «81. Ты тяже все судять послухи свободными, будеть ли послухъ холопъ, т»

---

### CONST-SVOB-003 — `DAT + NOM.SG: [комусь] свобода [во кунах / смертию]`
- **КЛЮЧОВИЙ ТЕРМІН:** `СВОБОДА (NOUN)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `DAT + NOM.SG: [комусь] свобода [во кунах / смертию]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Іменник свобода в називному відмінку однини при давальному відмінку особи (наимиту, ім) та обставині умови (во кунах, смертию).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Всі вживання свободи у множині в дипломатичних пактах XVII ст.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **2**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **2**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Автоматичний юридичний факт припинення залежності. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Нормативний захист закупа від перетворення на повного раба через сваволю кредитора. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0033]` **`SRC-RP-EXP`** (рядок 182) | форма: `свобода`
    - **MATCH-RULE-ID:** `SVOB-R03-NOM-RELEASE`
    - **MATCH-EVIDENCE:** Nominal token 'свобода' (POS=NOUN) functions as predicative noun of release with dative beneficiary: «...и. Продасть ли господинъ закупа обель, то наимиту свобода во всехъ »
  - `[LEX-INV2-0044]` **`SRC-RP-EXP`** (рядок 292) | форма: `свобода`
    - **MATCH-RULE-ID:** `SVOB-R03-NOM-RELEASE`
    - **MATCH-EVIDENCE:** Nominal token 'свобода' (POS=NOUN) functions as predicative noun of release with dative beneficiary: «...ь робьи дети оу мужа, то задници имъ не имати, но свобода имъ смерт»

---

### CONST-SVOB-004 — `ADV-MANNER: swobodnie [zażywać / odprawować]`
- **КЛЮЧОВИЙ ТЕРМІН:** `SWOBODNIE (ADV)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `ADV-MANNER: swobodnie [zażywać / odprawować]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Прислівник swobodnie, що модифікує дієслова здійснення релігійного культу, навчання або друку книг.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Іменникові форми swoboda / swobodach.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **2**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **2**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Спосіб безперешкодного і безпечного відправлення духовних практик. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Становлення концепту релігійної толерантності та захисту конфесійного миру. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2139]` **`SRC-HADIACH-1658`** (рядок 26) | форма: `swobodnie`
    - **MATCH-RULE-ID:** `SVOB-R04-ADV-MANNER`
    - **MATCH-EVIDENCE:** Adverbial token 'swobodnie' modifies religious/educational practice in span: «...ich zgoła, tak jak nabożeństwa swego publicznie i swobodnie [libere»
  - `[LEX-INV2-2149]` **`SRC-HADIACH-1658`** (рядок 37) | форма: `swobodnie`
    - **MATCH-RULE-ID:** `SVOB-R04-ADV-MANNER`
    - **MATCH-EVIDENCE:** Adverbial token 'swobodnie' modifies religious/educational practice in span: «...ebować będą bez trudności stanowić będzie wolno i swobodnie [liberę»

---

### CONST-SVOB-005 — `ACC.SG / INF: [на первую свободу / свободити от ярма]`
- **КЛЮЧОВИЙ ТЕРМІН:** `СВОБОДА (NOUN) / СВОБОДИТИ (VERB)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `ACC.SG / INF: [на первую свободу / свободити от ярма]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Іменник свобода в однині або дієслово свободити при семантичних актантах «народ козацький», «вітчизна», «ярмо».
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Особисте звільнення холопа чи закупа в Руській Правді.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **3**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **3**
  - **`SENTENCE-COUNT`:** **3**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Стан політичної незалежності колективного суб'єкта від чужоземного панування. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Трансформація особистого статусу звільнення в ідею суверенного самовизначення спільноти. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2296]` **`SRC-ORLYK-1710`** (рядок 111) | форма: `свободу`
    - **MATCH-RULE-ID:** `SVOB-R05-COLL-EMANCIP`
    - **MATCH-EVIDENCE:** Token 'свободу' participates in formula of collective liberation of people/homeland: «...ваючися, ни во вѣки враждуючи, а хотячи на пεрвую свободу помянутый»
  - `[LEX-INV2-2320]` **`SRC-ORLYK-1710`** (рядок 123) | форма: `свободы`
    - **MATCH-RULE-ID:** `SVOB-R05-COLL-EMANCIP`
    - **MATCH-EVIDENCE:** Token 'свободы' participates in formula of collective liberation of people/homeland: «...Войско Zапорожскоε, нε отчаεваючися жεлаεмой сεбѣ свободы, а полага»
  - `[LEX-INV2-2340]` **`SRC-ORLYK-1710`** (рядок 139) | форма: `свободити`
    - **MATCH-RULE-ID:** `SVOB-R05-COLL-EMANCIP`
    - **MATCH-EVIDENCE:** Token 'свободити' participates in formula of collective liberation of people/homeland: «...ружіεмъ nаяснѣйшого короля εго милости швεдскаго, свободити отчизну»

---

### CONST-SVOB-006 — `PREP-GEN: от свободы [ЧИСЛО] кунъ`
- **КЛЮЧОВИЙ ТЕРМІН:** `СВОБОДА (NOUN)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `PREP-GEN: от свободы [ЧИСЛО] кунъ`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Прийменник «от» + родовий відмінок однини свободы у переліку митних або поземельних тарифів.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Звільнення особи від повинності.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **1**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **1**
  - **`SENTENCE-COUNT`:** **1**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Фіскальна одиниця пільгового поселення (слобода). `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Економічне стимулювання колонізації земель через надання тимчасового імунітету від зборів. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0047]` **`SRC-RP-EXP`** (рядок 318) | форма: `свободы`
    - **MATCH-RULE-ID:** `SVOB-R06-LOC-SLOBODA`
    - **MATCH-EVIDENCE:** Token 'свободы' functions as fiscal origin unit in tariff list: «...бес трии кунъ, тако же и отъ ролеиное земли, а от свободы 9 кунъ.»

---

### CONST-VOLN-001 — `COORDINATION: [права / свободи / привілеї] + [вольності]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ВОЛЬНОСТЬ / WOLNOŚĆ`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `COORDINATION: [права / свободи / привілеї] + [вольності]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Лексема вольності/wolności перебуває у прямому координаційному зв'язку зі словами права, свободи, привілеї, листи або звичаї через сполучники «і», «та», «або» чи кому.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Контексти, де вольності вжито ізольовано без переліку суміжних юридичних категорій або де слово є неузгодженим додатком до іншого іменника.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **14**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **14**
  - **`SENTENCE-COUNT`:** **10**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Кумулятивне вичерпне позначення всього правового доробку та статусу спільноти/стану. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Юридичне кліше для запобігання прогалин у нормативному регулюванні (hendiadys / pleonasm). `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0195]` **`SRC-LS-1566`** (рядок 1366) | форма: `вольности`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольности' is syntactically coordinated with parallel legal category in span: «тогды таковые листы и вольности его вжо никоторое моцы мЂти не будеть,»
  - `[LEX-INV2-0703]` **`SRC-LS-1588`** (рядок 28) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностей' is syntactically coordinated with parallel legal category in span: «...ими обетницами ни одно примноженыя прав, свобод и вольностей шляхет»
  - `[LEX-INV2-0704]` **`SRC-LS-1588`** (рядок 28) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностей' is syntactically coordinated with parallel legal category in span: «...мы вдячни от них будучи, и хотячи им завжды прав, вольностей и своб»
  - `[LEX-INV2-0705]` **`SRC-LS-1588`** (рядок 28) | форма: `вольности`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольности' is syntactically coordinated with parallel legal category in span: «...тою ж прысегою нашою которую есьмо на вси права и вольности, велико»
  - `[LEX-INV2-0729]` **`SRC-LS-1588`** (рядок 112) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностей' is syntactically coordinated with parallel legal category in span: «найвышому сторожу всих прав и вольностей наших, пана»
  - `[LEX-INV2-2186]` **`SRC-HADIACH-1659`** (рядок 213) | форма: `wolności`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'wolności' is syntactically coordinated with parallel legal category in span: «wać będzie praw y wolności, lecz taką iaką y»
  - `[LEX-INV2-2274]` **`SRC-ORLYK-1710`** (рядок 19) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностей' is syntactically coordinated with parallel legal category in span: «Договори і Постановлення прав і вольностей Війська Запорозького»
  - `[LEX-INV2-2279]` **`SRC-ORLYK-1710`** (рядок 25) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностей' is syntactically coordinated with parallel legal category in span: «=== Договори і Постановлення прав і вольностей Війська Запорозького ==»
  - `[LEX-INV2-2287]` **`SRC-ORLYK-1710`** (рядок 81) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностей' is syntactically coordinated with parallel legal category in span: «Прав і вольностей Війська Запорозького між Ясновельможним паном Пил...»
  - `[LEX-INV2-2305]` **`SRC-ORLYK-1710`** (рядок 113) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностей' is syntactically coordinated with parallel legal category in span: «...ого оборонця святого православ'я, прав Вітчизни і вольностей військ»
  - `[LEX-INV2-2306]` **`SRC-ORLYK-1710`** (рядок 113) | форма: `вольностях`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольностях' is syntactically coordinated with parallel legal category in span: «...Запорізьке та народ вільний руський при правах та вольностях непору»
  - `[LEX-INV2-2307]` **`SRC-ORLYK-1710`** (рядок 113) | форма: `вольності`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольності' is syntactically coordinated with parallel legal category in span: «...исленними винахідливими способами змогла права та вольності Війська»
  - `[LEX-INV2-2316]` **`SRC-ORLYK-1710`** (рядок 119) | форма: `вольності`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольності' is syntactically coordinated with parallel legal category in span: «...не військо, міста забрати в свою область, права і вольності поламат»
  - `[LEX-INV2-2332]` **`SRC-ORLYK-1710`** (рядок 131) | форма: `вольності`
    - **MATCH-RULE-ID:** `VOLN-R01-COORD`
    - **MATCH-EVIDENCE:** Token 'вольності' is syntactically coordinated with parallel legal category in span: «...ю були значно надвередили давні порядки, права та вольності військо»

---

### CONST-VOLN-002 — `PREP-PHRASE: при + [вольностяхъ / wolnościach]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ВОЛЬНОСТЬ / WOLNOŚĆ`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `PREP-PHRASE: при + [вольностяхъ / wolnościach]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Прийменникова конструкція «при» / «przy», що безпосередньо керує місцевим відмінком множини іменника вольності (при вольностях).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Вживання вольностей з іншими прийменниками («на вольности», «до вольностей», «з вольностей»).
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **3**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **3**
  - **`SENTENCE-COUNT`:** **3**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Стан збереження чинного правового статусу без погіршення. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Синтаксична формула консервації традиційного права перед лицем зміни правителя чи унії. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2163]` **`SRC-HADIACH-1658`** (рядок 46) | форма: `wolnościach`
    - **MATCH-RULE-ID:** `VOLN-R02-PREP-PRI`
    - **MATCH-EVIDENCE:** Token 'wolnościach' is governed by preposition 'при'/'przy' in span: «...dane konfirmuje, zachowując ich przy starodawnych wolnościach i zwy»
  - `[LEX-INV2-2199]` **`SRC-HADIACH-1659`** (рядок 312) | форма: `wolnościach`
    - **MATCH-RULE-ID:** `VOLN-R02-PREP-PRI`
    - **MATCH-EVIDENCE:** Token 'wolnościach' is governed by preposition 'при'/'przy' in span: «chowuiąc ich przy starodawnych wolnościach,»
  - `[LEX-INV2-2306]` **`SRC-ORLYK-1710`** (рядок 113) | форма: `вольностях`
    - **MATCH-RULE-ID:** `VOLN-R02-PREP-PRI`
    - **MATCH-EVIDENCE:** Token 'вольностях' is governed by preposition 'при'/'przy' in span: «...Запорізьке та народ вільний руський при правах та вольностях непору»

---

### CONST-VOLN-003 — `VERB-GOV: [потвердити / конфирмовати / надати] + [вольности]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ВОЛЬНОСТЬ / WOLNOŚĆ`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `VERB-GOV: [потвердити / конфирмовати / надати] + [вольности]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Вольності виступають прямим додатком або об'єктом при дієсловах позитивної конфірмації, пожалування чи обварування правителем.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Дієслова загального вживання без семантики офіційного визнання (наприклад, чути, бачити, знати).
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **3**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **3**
  - **`SENTENCE-COUNT`:** **3**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Акт монаршого або договірного санкціонування чинності привілеїв. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Легітимація влади монарха через зобов'язання дотримуватися прав підданих. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0703]` **`SRC-LS-1588`** (рядок 28) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R03-VERB-CONFIRM`
    - **MATCH-EVIDENCE:** Token 'вольностей' is direct object/theme of confirmation or granting predicate in span: «...ими обетницами ни одно примноженыя прав, свобод и вольностей шляхет»
  - `[LEX-INV2-0892]` **`SRC-LS-1588`** (рядок 921) | форма: `вольности`
    - **MATCH-RULE-ID:** `VOLN-R03-VERB-CONFIRM`
    - **MATCH-EVIDENCE:** Token 'вольности' is direct object/theme of confirmation or granting predicate in span: «...вилья земъские стародавные и ново отъ насъ даные, вольности и звыча»
  - `[LEX-INV2-2267]` **`SRC-MARCH-1654`** (рядок 88) | форма: `вольности`
    - **MATCH-RULE-ID:** `VOLN-R03-VERB-CONFIRM`
    - **MATCH-EVIDENCE:** Token 'вольности' is direct object/theme of confirmation or granting predicate in span: «...Запорожское пожалует свои государские грамоты на вольности ваши дат»

---

### CONST-VOLN-004 — `VERB-GOV: [порушити / отбирати / поламати] + [вольности]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ВОЛЬНОСТЬ / WOLNOŚĆ`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `VERB-GOV: [порушити / отбирати / поламати] + [вольности]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Вольності виступають прямим об'єктом при дієсловах або іменниках делікту, відібрання, зламу, утиску чи порушення.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Порушення інших об'єктів (порушити спокій, відібрати маєток), якщо вольності не фігурують у складі конструкції.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **8**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **8**
  - **`SENTENCE-COUNT`:** **6**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Юридична кваліфікація неправомірного посягання на статус підданих. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Правове обґрунтування опору володареві (ius resistendi) через порушення умов пакту. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0146]` **`SRC-LS-1566`** (рядок 1007) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'вольностей' is direct object of breach/deprivation/derogation predicate in span: «свободъ и вольностей и правъ въ нихъ отбирати и отводити, и ни якимъ о»
  - `[LEX-INV2-2193]` **`SRC-HADIACH-1659`** (рядок 281) | форма: `wolności`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'wolności' is direct object of breach/deprivation/derogation predicate in span: «Pany na uymę granic, abo wolności tych na-»
  - `[LEX-INV2-2306]` **`SRC-ORLYK-1710`** (рядок 113) | форма: `вольностях`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'вольностях' is direct object of breach/deprivation/derogation predicate in span: «...Запорізьке та народ вільний руський при правах та вольностях непору»
  - `[LEX-INV2-2307]` **`SRC-ORLYK-1710`** (рядок 113) | форма: `вольності`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'вольності' is direct object of breach/deprivation/derogation predicate in span: «...исленними винахідливими способами змогла права та вольності Війська»
  - `[LEX-INV2-2316]` **`SRC-ORLYK-1710`** (рядок 119) | форма: `вольності`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'вольності' is direct object of breach/deprivation/derogation predicate in span: «...не військо, міста забрати в свою область, права і вольності поламат»
  - `[LEX-INV2-2318]` **`SRC-ORLYK-1710`** (рядок 119) | форма: `вольностях`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'вольностях' is direct object of breach/deprivation/derogation predicate in span: «...ше в непорушних, але і в розширених і розмножених вольностях, відда»
  - `[LEX-INV2-2386]` **`SRC-ORLYK-1710`** (рядок 205) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'вольностей' is direct object of breach/deprivation/derogation predicate in span: «...потреба, на Раді його вити про порушення прав та вольностей вітчизн»
  - `[LEX-INV2-2404]` **`SRC-ORLYK-1710`** (рядок 336) | форма: `вольності`
    - **MATCH-RULE-ID:** `VOLN-R04-VERB-BREACH`
    - **MATCH-EVIDENCE:** Token 'вольності' is direct object of breach/deprivation/derogation predicate in span: «...ітчизні нелади для премудрого справлення, прав та вольності військо»

---

### CONST-VOLN-005 — `VERB-GOV: [уживати / заживати / gaudere] + [вольностей]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ВОЛЬНОСТЬ / WOLNOŚĆ`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `VERB-GOV: [уживати / заживати / gaudere] + [вольностей]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Вольності у родовому або орудному відмінку при дієсловах правокористування (уживати, заживати, веселитися, gaudere).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Контексти, де дієслово заживати стосується інших об'єктів (заживати покою, уживати ліків).
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **4**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **4**
  - **`SENTENCE-COUNT`:** **4**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Фактичне здійснення та володіння визнаними правами. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Критерій повноправної належності особи чи інституції до привілейованого стану. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0179]` **`SRC-LS-1566`** (рядок 1235) | форма: `вольностеи`
    - **MATCH-RULE-ID:** `VOLN-R05-VERB-USAGE`
    - **MATCH-EVIDENCE:** Token 'вольностеи' is governed by usage/enjoyment predicate in span: «...не показалъ, тогды хотя имЂнье купитъ, предсе зъ вольностеи шляхецс»
  - `[LEX-INV2-0853]` **`SRC-LS-1588`** (рядок 793) | форма: `вольностей`
    - **MATCH-RULE-ID:** `VOLN-R05-VERB-USAGE`
    - **MATCH-EVIDENCE:** Token 'вольностей' is governed by usage/enjoyment predicate in span: «...твъ хрестияньских, ровнуючи а однако маючи и тыхъ вольностей уживаю»
  - `[LEX-INV2-2145]` **`SRC-HADIACH-1658`** (рядок 35) | форма: `wolnościami`
    - **MATCH-RULE-ID:** `VOLN-R05-VERB-USAGE`
    - **MATCH-EVIDENCE:** Token 'wolnościami' is governed by usage/enjoyment predicate in span: «...ny Koronne erygować, która takimi prerogatywami i wolnościami ma si»
  - `[LEX-INV2-2184]` **`SRC-HADIACH-1659`** (рядок 199) | форма: `wolnościami`
    - **MATCH-RULE-ID:** `VOLN-R05-VERB-USAGE`
    - **MATCH-EVIDENCE:** Token 'wolnościami' is governed by usage/enjoyment predicate in span: «praerogatywami y wolnościami ma gaudere, iako»

---

### CONST-VOLN-006 — `NOM/ACC.SG: вольность [и моцъ] + [INF / на-ACC]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ВОЛЬНОСТЬ`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `NOM/ACC.SG: вольность [и моцъ] + [INF / на-ACC]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Іменник вольность в однині сполучений із модальними поняттями («моцъ») або керує інфінітивом дії чи прийменником «на» + акузатив органу (соймик).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Всі форми множини (вольности, вольностей).
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **4**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **4**
  - **`SENTENCE-COUNT`:** **4**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Конкретний правовий дозвіл або індивідуальна дієздатність. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Визнання правоздатності індивіда на пересування та участь у становому представництві. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0161]` **`SRC-LS-1566`** (рядок 1141) | форма: `вольность`
    - **MATCH-RULE-ID:** `VOLN-R06-NOM-CAPABILITY`
    - **MATCH-EVIDENCE:** Singular token 'вольность' combined with modal capability/infinitive in span: «панства нашого Великого Князства Литовского мЂли вольность и моцъ выЂх»
  - `[LEX-INV2-0162]` **`SRC-LS-1566`** (рядок 1142) | форма: `вольность`
    - **MATCH-RULE-ID:** `VOLN-R06-NOM-CAPABILITY`
    - **MATCH-EVIDENCE:** Singular token 'вольность' combined with modal capability/infinitive in span: «...хъ земль нашихъ Великого Князства Литовского мЂли вольность и моцъ»
  - `[LEX-INV2-0706]` **`SRC-LS-1588`** (рядок 28) | форма: `вольность`
    - **MATCH-RULE-ID:** `VOLN-R06-NOM-CAPABILITY`
    - **MATCH-EVIDENCE:** Singular token 'вольность' combined with modal capability/infinitive in span: «...а потом завжды кагды одно того потребовати будеть вольность поправа»
  - `[LEX-INV2-0897]` **`SRC-LS-1588`** (рядок 927) | форма: `вольность`
    - **MATCH-RULE-ID:** `VOLN-R06-NOM-CAPABILITY`
    - **MATCH-EVIDENCE:** Singular token 'вольность' combined with modal capability/infinitive in span: «...того паньства, великого князства литовского, мели вольность и моцъ »

---

### CONST-VOLN-007 — `PREP-LOC: вольность на водахъ на дорогахъ`
- **КЛЮЧОВИЙ ТЕРМІН:** `ВОЛЬНОСТЬ`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `PREP-LOC: вольность на водахъ на дорогахъ`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Іменник вольность сполучений із локативним просторовим виразом «на водах на дорогах» (сухим і водним шляхом).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Загальні згадки про дороги чи води без слова вольность.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **2**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **2**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** Митний імунітет та право безперешкодного транзиту товарів. `[PROVISIONAL]`
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Економічний привілей шляхти на безмитний експорт продукції власного фільварку. `[PROVISIONAL]`
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0102]` **`SRC-LS-1566`** (рядок 501) | форма: `вольность`
    - **MATCH-RULE-ID:** `VOLN-R07-LOC-TRANSIT`
    - **MATCH-EVIDENCE:** Token 'вольность' situates within spatial transit formula «вольность на водахъ на дорогахъ»: «вольность на водахъ на дорогахъ, то естъ сухимъ путемъ и во...»
  - `[LEX-INV2-0821]` **`SRC-LS-1588`** (рядок 383) | форма: `вольность`
    - **MATCH-RULE-ID:** `VOLN-R07-LOC-TRANSIT`
    - **MATCH-EVIDENCE:** Token 'вольность' situates within spatial transit formula «вольность на водахъ на дорогахъ»: «...етъскимъ, шляхъте в томъ панстве нашомъ даемъ тую вольность на вода»

---

## 2. МАТРИЦЯ МУЛЬТИ-ПРИНАЛЕЖНОСТІ (MULTI-MEMBERSHIP ANALYSIS)

Оскільки синтаксичні конструкції накладаються одна на одну, нижче зафіксовано всі випадки, де один токен бере участь одразу в кількох структурних рамках, підтверджених незалежними правилами:

| ТОКЕН-ID | СВІДОК ТА РЯДОК | СЛОВОФОРМА | ПІДТВЕРДЖЕНІ ПРАВИЛА (MATCH-RULE-IDS) | СИНТАКСИЧНИЙ ДОКАЗ ПЕРЕТИНУ |
|:---|:---|:---:|:---|:---|
| `LEX-INV2-0703` | **`SRC-LS-1588`** (рядок 28) | `вольностей` | `CONST-VOLN-001 (VOLN-R01-COORD); CONST-VOLN-003 (VOLN-R03-VERB-CONFIRM)` | *«...ими обетницами ни одно примноженыя прав, свобод и вольностей шляхетских, але розширьнья»* |
| `LEX-INV2-2306` | **`SRC-ORLYK-1710`** (рядок 113) | `вольностях` | `CONST-VOLN-004 (VOLN-R04-VERB-BREACH); CONST-VOLN-001 (VOLN-R01-COORD); CONST-VOLN-002 (VOLN-R02-PREP-PRI)` | *«...Запорізьке та народ вільний руський при правах та вольностях непорушно буде під її обор»* |
| `LEX-INV2-2307` | **`SRC-ORLYK-1710`** (рядок 113) | `вольності` | `CONST-VOLN-004 (VOLN-R04-VERB-BREACH); CONST-VOLN-001 (VOLN-R01-COORD)` | *«...исленними винахідливими способами змогла права та вольності Війська Запорозького, нею ж»* |
| `LEX-INV2-2316` | **`SRC-ORLYK-1710`** (рядок 119) | `вольності` | `CONST-VOLN-004 (VOLN-R04-VERB-BREACH); CONST-VOLN-001 (VOLN-R01-COORD)` | *«...не військо, міста забрати в свою область, права і вольності поламати, Запорозьке низове»* |

---

## 3. БАГАТОВИМІРНА МАТРИЦЯ РОЗПОДІЛУ (MULTI-DIMENSIONAL MATRIX)

Зіставлення 5 вимірів: **ТЕРМІН × КОНСТРУКЦІЯ × ЧАС × МОВА × ЖАНР × ІНСТИТУЦІЯ**:

| CONSTRUCTION-ID | ТЕРМІН | СВІДКИ (ЧАС) | МОВА (`LANGUAGE-OF-PASSAGE`) | ДЖЕРЕЛЬНИЙ ЖАНР (`GENRE`) | ЮРИСДИКЦІЯ / ІНСТИТУЦІЯ | `TOKEN-COUNT` | `INSTANCE-COUNT` | `SENTENCE-COUNT` |
|:---|:---:|:---:|:---|:---|:---|:---:|:---:|:---:|
| `CONST-SVOB-001` | `СВОБОДНЫЙ (ADJ)` | SRC-RP-EXP (XII–XV ст.) | Давньоруська | Процесуальний судовий кодекс | Князівсько-боярський суд | **5** | **5** | **5** |
| `CONST-SVOB-002` | `СВОБОДНЫЙ (ADJ)` | SRC-RP-EXP (XII–XV ст.) | Давньоруська | Процесуальний судовий кодекс | Князівсько-боярський суд | **1** | **1** | **1** |
| `CONST-SVOB-003` | `СВОБОДА (NOUN)` | SRC-RP-EXP (XII–XV ст.) | Давньоруська | Процесуальний судовий кодекс | Князівсько-боярський суд | **2** | **2** | **2** |
| `CONST-SVOB-004` | `SWOBODNIE (ADV)` | SRC-HADIACH-1658 (1658 р.) | Ранньомодерна польська | Міжнародно-правовий пакт унії | Спільна Комісія Корони і В.К.Р. | **2** | **2** | **2** |
| `CONST-SVOB-005` | `СВОБОДА (NOUN) / СВОБОДИТИ (VERB)` | SRC-ORLYK-1710 (1710 р.) | Староукраїнська книжна | Конституційний договір-пакт | Генеральна Рада / Гетьманський уряд | **3** | **3** | **3** |
| `CONST-SVOB-006` | `СВОБОДА (NOUN)` | SRC-RP-EXP (XII–XV ст.) | Давньоруська | Процесуальний судовий кодекс | Князівсько-боярський суд | **1** | **1** | **1** |
| `CONST-VOLN-001` | `ВОЛЬНОСТЬ / WOLNOŚĆ` | SRC-HADIACH-1659, SRC-LS-1566, SRC-LS-1588, SRC-ORLYK-1710 (1566 р., 1588 р., 1659 р., 1710 р.) | Ранньомодерна польська, Руська канцелярська, Староукраїнська книжна | Загальнодержавна кодифікація, Кодифікований земський статут, Конституційний договір-пакт, Сеймова ратифікаційна конституція | Вальний Сойм / Трибунал ВКЛ, Генеральна Рада / Гетьманський уряд, Сейм Речі Посполитої (Volumina Legum), Сойм ВКЛ / земські суди | **14** | **14** | **10** |
| `CONST-VOLN-002` | `ВОЛЬНОСТЬ / WOLNOŚĆ` | SRC-HADIACH-1658, SRC-HADIACH-1659, SRC-ORLYK-1710 (1658 р., 1659 р., 1710 р.) | Ранньомодерна польська, Староукраїнська книжна | Конституційний договір-пакт, Міжнародно-правовий пакт унії, Сеймова ратифікаційна конституція | Генеральна Рада / Гетьманський уряд, Сейм Речі Посполитої (Volumina Legum), Спільна Комісія Корони і В.К.Р. | **3** | **3** | **3** |
| `CONST-VOLN-003` | `ВОЛЬНОСТЬ / WOLNOŚĆ` | SRC-LS-1588, SRC-MARCH-1654 (1588 р., 1654 р.) | Московсько-руська двомовна, Руська канцелярська | Двосторонні договірні статті, Загальнодержавна кодифікація | Вальний Сойм / Трибунал ВКЛ, Посольський приказ / Військо Запорозьке | **3** | **3** | **3** |
| `CONST-VOLN-004` | `ВОЛЬНОСТЬ / WOLNOŚĆ` | SRC-HADIACH-1659, SRC-LS-1566, SRC-ORLYK-1710 (1566 р., 1659 р., 1710 р.) | Ранньомодерна польська, Руська канцелярська, Староукраїнська книжна | Кодифікований земський статут, Конституційний договір-пакт, Сеймова ратифікаційна конституція | Генеральна Рада / Гетьманський уряд, Сейм Речі Посполитої (Volumina Legum), Сойм ВКЛ / земські суди | **8** | **8** | **6** |
| `CONST-VOLN-005` | `ВОЛЬНОСТЬ / WOLNOŚĆ` | SRC-HADIACH-1658, SRC-HADIACH-1659, SRC-LS-1566, SRC-LS-1588 (1566 р., 1588 р., 1658 р., 1659 р.) | Ранньомодерна польська, Руська канцелярська | Загальнодержавна кодифікація, Кодифікований земський статут, Міжнародно-правовий пакт унії, Сеймова ратифікаційна конституція | Вальний Сойм / Трибунал ВКЛ, Сейм Речі Посполитої (Volumina Legum), Сойм ВКЛ / земські суди, Спільна Комісія Корони і В.К.Р. | **4** | **4** | **4** |
| `CONST-VOLN-006` | `ВОЛЬНОСТЬ` | SRC-LS-1566, SRC-LS-1588 (1566 р., 1588 р.) | Руська канцелярська | Загальнодержавна кодифікація, Кодифікований земський статут | Вальний Сойм / Трибунал ВКЛ, Сойм ВКЛ / земські суди | **4** | **4** | **4** |
| `CONST-VOLN-007` | `ВОЛЬНОСТЬ` | SRC-LS-1566, SRC-LS-1588 (1566 р., 1588 р.) | Руська канцелярська | Загальнодержавна кодифікація, Кодифікований земський статут | Вальний Сойм / Трибунал ВКЛ, Сойм ВКЛ / земські суди | **2** | **2** | **2** |

---

## 4. ДИСЦИПЛІНА ВИСНОВКІВ: КОРЕЛЯЦІЇ ПРОТИ ПРИЧИННОСТІ

```text
CORRELATION ≠ CAUSALITY PROTOCOL

1. GENRE-HYPOTHESIS-001 (PROVISIONAL):
   The observed absence of VOLN- constructions in the Old Rus witnesses (RP-SHORT, RP-EXP)
   correlates with the judicial-torts genre of those documents. Whether this reflects an authentic
   absence in the spoken/legal language of the 11th-12th centuries or is an artifact of the surviving
   codification genres cannot be resolved without contemporaneous contractual witnesses.

2. LANGUAGE-HYPOTHESIS-001 (PROVISIONAL):
   The syntactic behavior of 'wolność' and 'swoboda' in Hadiach (1658-1659) strictly belongs to the
   Early Modern Polish parliamentary and treaty tradition. Formal cognacy with Chancery Ruthenian
   'вольность' does not imply identical semantic evolution.

3. MULTI-MEMBERSHIP FINDING:
   Multi-membership is restricted strictly to verified formal rule matches (MATCH-RULE-ID).
   Lexeme tokens participating simultaneously in coordination (права та вольності) and
   predicate breach (вольності поламати) are accounted for separately under TOKEN-COUNT,
   INSTANCE-COUNT, and SENTENCE-COUNT.
```