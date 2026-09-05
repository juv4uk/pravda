# АУДИТ ЦІЛІСНОСТІ ТА МАТРИЦЯ СИНТАКСИЧНИХ КОНСТРУКЦІЙ (ВЕРСІЯ 3 — CALIBRATED)
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
> 5. **FIVE-TIER EPISTEMIC PIPELINE (SOURCE-NEAR BOUNDARY PROTOCOL)**:
>    - `FORMAL SYNTACTIC FRAME`: точний структурний шаблон сполучуваності (предикат, частка, відмінок).
>    - `MORPHOSYNTACTIC PARAPHRASE`: буквальний парафраз форми без підстановки сучасних чи сусідніх правових термінів («без + GEN(рядъ)», «V.REFL(рядити ся)»).
>    - `LEXICOGRAPHIC GLOSS (L2 EVIDENCE)`: значення-кандидати, прямо засвідчені історичними словниками із зазначенням `LEX-EVID-ID` (Срезневський, СЛМ, Тимченко, ЕСУМ). ЗАБОРОНЕНО визначати РЯДЪ, ДОГОВОРЪ, ПАКТЪ одне через одне без цитати зі словника.
>    - `CONTEXTUAL RECONSTRUCTION`: фактична роль у системі конкретного джерела (як відсутність/наявність змінює юридичний наслідок).
>    - `MODERN ANALOGY (CAUTIONARY)`: евристичне порівняння (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
> 6. **RESIDUAL & UNCERTAIN ACCOUNTING (ANTI-PRESSURE PROTOCOL)**:
>    100% coverage не є самоціллю. Токени з сучасної редакційної розмітки, колофонів чи ізольованих контекстів обліковуються як `RESIDUAL / UNCLASSIFIED`.

---

## 1. РЕЄСТР АУДИТОВАНИХ КОНСТРУКЦІЙ (AUDITED CONSTRUCTIONS 01–26)

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


---

### CONST-RYAD-001 — `REFL-VERB: рядити ся (како ся будеть рядилъ)`
- **КЛЮЧОВИЙ ТЕРМІН:** `РЯДЪ (VERB: рядити ся)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `REFL-VERB: рядити ся (како ся будеть рядилъ)`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Зворотне дієслово *рядити ся* у підрядному умовному реченні домовленості про умови найму, відсотків або статусу («како ся будеть рядилъ»).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Іменникові вживання кореня *ряд-* без дієслова або без частки *ся*.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **3**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **3**
  - **`SENTENCE-COUNT`:** **3**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Підрядне речення способу дії: «како ся будеть рядилъ» = як + частка ся + допоміжне дієслово будеть + минулий час дієслова *рядити*. Буквально: «як вступав у дію ряду / як чинив у взаємному ряді».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-024]`, `[LEX-EVID-025]`: Срезневський (Т. 3, стб. 212): «рядитисѧ — договариваться, вступать в обязательство»; ЕСУМ (Т. 5, с. 159): «рядити ся — домовлятися про умови найму/роботи».
  - **CONTEXTUAL RECONSTRUCTION:** У тексті РП спосіб здійснення дії *рядити ся* визначає юридичний розмір належного (відсотки з зерна) або збереження особистого статусу; доведення здійснюється через послухів (свідків).
  - **MODERN ANALOGY (CAUTIONARY):** Досягнення домовленості про умови зобов'язання (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Фіксація договірного правочину в додержавному звичаєвому праві без писаного документа.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0029]` **`SRC-RP-EXP`** (рядок 151) | форма: `рядилъ`
    - **MATCH-RULE-ID:** `RYAD-R01-REFL-VERB`
    - **MATCH-EVIDENCE:** Reflexive verb form 'рядилъ' governs condition of debt/grain interest: «...о просопъ, то послухи ему ставити, како ся будеть рядилъ, тако же ему имати.»
  - `[LEX-INV2-0051]` **`SRC-RP-EXP`** (рядок 324) | форма: `рядилъ`
    - **MATCH-RULE-ID:** `RYAD-R01-REFL-VERB`
    - **MATCH-EVIDENCE:** Reflexive verb form 'рядилъ' governs condition of marriage with slave woman: «...без ряду, поиметь ли с рядомь, то како ся будеть рядилъ, на том же стоить.»
  - `[LEX-INV2-0055]` **`SRC-RP-EXP`** (рядок 326) | форма: `рядилъ`
    - **MATCH-RULE-ID:** `RYAD-R01-REFL-VERB`
    - **MATCH-EVIDENCE:** Reflexive verb form 'рядилъ' governs condition of administrative service (tiunstvo): «...ь к собе без ряду, с рядомь ли, то како ся будеть рядилъ, на том же стоить.»

---

### CONST-RYAD-002 — `PREP-PHRASE: [безъ ряду / с рядомь]`
- **КЛЮЧОВИЙ ТЕРМІН:** `РЯДЪ (NOUN)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `PREP-PHRASE: [безъ ряду / с рядомь]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Прийменникова сполука іменника рядъ з прийменниками «без» (род. відм.) або «с» (оруд. відм.), що фіксує наявність чи відсутність попередньої угоди або заповіту.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Інструменталі судової процедури («явным рядом») або локативні згадки органу влади.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **6**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **6**
  - **`SENTENCE-COUNT`:** **3**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Прийменникові конструкції стану/умови: «безъ + GEN(рядъ)» проти «съ + INS(рядъ)». Буквально: «за відсутності ряду» проти «за наявності ряду».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-025]`: Срезневський (Т. 3, стб. 211): 1. «безъ ряду — без завЂщанія, без предварительнаго распоряженія («паки ли безъ ряду оумреть»)»; 2. «съ рядомъ — с условіемъ, по предварительному договору («с рядомь ли, то тако же стоить»)».
  - **CONTEXTUAL RECONSTRUCTION:** У РП наявність чи відсутність `ряду` виступає юридичним бінарним перемикачем: відсутність тягне холопство або спадкування всіма дітьми; наявність — зберігає волю особи або закріплює волю спадкодавця.
  - **MODERN ANALOGY (CAUTIONARY):** Наявність чи відсутність спеціального правочину/заповіту (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Регулювання переходу майна або зміни особистого статусу за наявністю формального волевиявлення.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0043]` **`SRC-RP-EXP`** (рядок 276) | форма: `ряду`
    - **MATCH-RULE-ID:** `RYAD-R02-PREP-COND`
    - **MATCH-EVIDENCE:** Prepositional phrase 'безъ ряду' conditions intestate succession: «...домъ свои детемъ, на том же стояти; паки ли безъ ряду оумреть, то всемъ детемъ, а на самого часть дати...»
  - `[LEX-INV2-0049]` **`SRC-RP-EXP`** (рядок 324) | форма: `ряду`
    - **MATCH-RULE-ID:** `RYAD-R02-PREP-COND`
    - **MATCH-EVIDENCE:** Prepositional phrase 'без ряду' governs automatic enslavement: «103. А второе холопьство: поиметь робу без ряду, поиметь ли с рядомь, то како ся будеть рядилъ, н...»
  - `[LEX-INV2-0050]` **`SRC-RP-EXP`** (рядок 324) | форма: `рядомь`
    - **MATCH-RULE-ID:** `RYAD-R02-PREP-COND`
    - **MATCH-EVIDENCE:** Prepositional phrase 'с рядомь' preserves contracted free status: «...е холопьство: поиметь робу без ряду, поиметь ли с рядомь, то како ся будеть рядилъ, на том же стоить.»
  - `[LEX-INV2-0052]` **`SRC-RP-EXP`** (рядок 326) | форма: `ряду`
    - **MATCH-RULE-ID:** `RYAD-R02-PREP-COND`
    - **MATCH-EVIDENCE:** Prepositional phrase 'без ряду' governs tiun appointment without contract: «104. А се третьее холопьство: тивуньство без ряду или привяжеть ключь к собе без ряду, с рядомь ли,...»
  - `[LEX-INV2-0053]` **`SRC-RP-EXP`** (рядок 326) | форма: `ряду`
    - **MATCH-RULE-ID:** `RYAD-R02-PREP-COND`
    - **MATCH-EVIDENCE:** Prepositional phrase 'без ряду' repeats condition for key-bearing service: «...ивуньство без ряду или привяжеть ключь к собе без ряду, с рядомь ли, то како ся будеть рядилъ, на том же...»
  - `[LEX-INV2-0054]` **`SRC-RP-EXP`** (рядок 326) | форма: `рядомь`
    - **MATCH-RULE-ID:** `RYAD-R02-PREP-COND`
    - **MATCH-EVIDENCE:** Prepositional phrase 'с рядомь' provides immunity against servitude: «...о без ряду или привяжеть ключь к собе без ряду, с рядомь ли, то како ся будеть рядилъ, на том же стоить.»

---

### CONST-RYAD-003 — `NOM-PRED: [то тако же есть рядъ]`
- **КЛЮЧОВИЙ ТЕРМІН:** `РЯДЪ (NOUN)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `NOM-PRED: [то тако же есть рядъ]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Називний відмінок іменника рядъ у ролі іменного присудка зв'язки «есть рядъ», що позначає загальне законне правило чи звичаєвий порядок.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Прийменникові та дієслівні форми.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **1**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **1**
  - **`SENTENCE-COUNT`:** **1**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Іменний предикат зв'язки: «то тако же есть рядъ» = вказівний займенник то + прислівник тако же + зв'язка есть + NOM(рядъ). Буквально: «це так само є ряд».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-024]`, `[LEX-EVID-025]`: Срезневський (Т. 3, стб. 210): «рядъ — порядокъ, правильное устройство, законное постановленіе»; ЕСУМ (Т. 5, с. 159): «ряд — порядок, лад, закон».
  - **CONTEXTUAL RECONSTRUCTION:** У РП фраза фіксує не договір сторін, а загальне законне правило: майно матері переходить дітям за тим самим нормативним порядком, що й спадщина батька.
  - **MODERN ANALOGY (CAUTIONARY):** Чинна правова норма / презумпція замовчування (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Формулювання загальнообов'язкової норми через ствердження чинного ладу.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0045]` **`SRC-RP-EXP`** (рядок 296) | форма: `рядъ`
    - **MATCH-RULE-ID:** `RYAD-R03-NOM-PRED`
    - **MATCH-EVIDENCE:** Nominal predicative 'рядъ' with copula 'есть' equates stepfather's estate inheritance to normative customary rule: «...отчимъ прииметь дети cú задницею, то тако же есть рядъ. А дворъ без дела отень всякъ меншему сынови.»

---

### CONST-RYAD-004 — `ADVERB-PROCEDURAL: явным рядомъ [и поступомъ / поступкомъ права]`
- **КЛЮЧОВИЙ ТЕРМІН:** `РЯДЪ (NOUN: орудний відмінок)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `ADVERB-PROCEDURAL: явным рядомъ [и поступомъ / поступкомъ права]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Орудний відмінок рядъ у парній прислівниковій формулі з прикметником «явным» та іменником «поступом/поступком права» для позначення судового процесуального порядку.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Вживання орудного відмінка з прийменником «с рядомь» у приватноправовому сенсі.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **3**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **3**
  - **`SENTENCE-COUNT`:** **3**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Орудний відмінок способу дії в координації: ADJ(явным) + INS(рядомъ) + кон'юнкція [и] + INS(поступомъ / поступкомъ) + GEN(права). Буквально: «явним рядом і поступом права».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-026]`: СЛМ XVI–XVII (Вип. 31, с. 149): «рядъ — законний порядок, судова черга, судова процедура («явным рядом и поступом права справить»)».
  - **CONTEXTUAL RECONSTRUCTION:** У Литовських Статутах вираз є процесуальним застереженням: заборона монарху карати шляхтича без явного розслідування у відкритому судовому засіданні за участі позивача.
  - **MODERN ANALOGY (CAUTIONARY):** Відкритий судовий розгляд (*MODERN ANALOGY ≠ HISTORICAL SENSE; вживання due process of law заборонено*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Статутна процесуальна гарантія шляхетського суверенітету проти позасудового покарання володарем.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0065]` **`SRC-LS-1566`** (рядок 93) | форма: `рядомъ`
    - **MATCH-RULE-ID:** `RYAD-R04-PROCEDURAL`
    - **MATCH-EVIDENCE:** Formula 'явным рядомъ и поступомъ права' specifies proper judicial procedure: «первей у суду явным рядомъ и поступомъ права, коли жалобник то есть поводъ и»
  - `[LEX-INV2-0400]` **`SRC-LS-1566`** (рядок 2789) | форма: `рядомъ`
    - **MATCH-RULE-ID:** `RYAD-R04-PROCEDURAL`
    - **MATCH-EVIDENCE:** Instrumental 'рядомъ' governs lawful official execution of office under oath: «рядомъ справовати будеть, маеть присегу на тотъ врадъ св...»
  - `[LEX-INV2-0735]` **`SRC-LS-1588`** (рядок 209) | форма: `рядомъ`
    - **MATCH-RULE-ID:** `RYAD-R04-PROCEDURAL`
    - **MATCH-EVIDENCE:** Formula 'явным рядомъ и поступкомъ права' specifies court process on Sejm: «...аем и не будемъ, ажбы перво на соймѣ у суду явным рядомъ и поступкомъ права, коли жалобникъ, то естъ повод...»

---

### CONST-RYAD-005 — `LOC-COUNCIL: в ряде / в рядех [нашой / судех]`
- **КЛЮЧОВИЙ ТЕРМІН:** `РЯДЪ (NOUN: місцевий відмінок)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `LOC-COUNCIL: в ряде / в рядех [нашой / судех]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Місцевий відмінок однини або множини з прийменником «в», що позначає орган державної влади (Раду ВКЛ) або систему урядових колегій.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Процесуальні або договірні формули.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **2**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **2**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Локативна прийменникова сполука: «въ + LOC(ряде / рядех)». Сполучається з присвійним займенником «нашой» або іменником «судех». Буквально: «у ряді нашій», «у рядах і судах».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-026]`: СЛМ XVI–XVII (Вип. 31, с. 150): «рядъ — рада, урядова колегія, сенат: «в ряде нашой — у раді Великого Князівства Литовського»».
  - **CONTEXTUAL RECONSTRUCTION:** У Статуті 1588 термін позначає вищий інституційний орган держави (Пани-Раду ВКЛ) поруч із земськими судами.
  - **MODERN ANALOGY (CAUTIONARY):** Вища державна рада / колегія урядовців (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Корпоративне закріплення терміна *рядъ* як синоніма вищого посадового стану.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-0709]` **`SRC-LS-1588`** (рядок 28) | форма: `рядех`
    - **MATCH-RULE-ID:** `RYAD-R05-COUNCIL`
    - **MATCH-EVIDENCE:** Token 'рядех' coordinated with 'судех' denotes judicial/administrative benches: «...юбуем и обецуем, и вжо во всих землях и поветех в рядех и судех вшеляких до великого князьства належачых...»
  - `[LEX-INV2-0828]` **`SRC-LS-1588`** (рядок 407) | форма: `ряде`
    - **MATCH-RULE-ID:** `RYAD-R05-COUNCIL`
    - **MATCH-EVIDENCE:** Formula 'в ряде нашой' denotes the Grand Ducal Council (Pany-Rada): «...маемъ. А хто бы якое жъ кольвекъ дыкгнитаръство в ряде нашой албо врядъ дворъный, земъский, будь тежъ ст...»

---

### CONST-DOG-001 — `TITULAR-PAIR: Договори і Постановлεня (Правъ и Волностεй)`
- **КЛЮЧОВИЙ ТЕРМІН:** `ДОГОВОРЪ (NOUN: множина)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `TITULAR-PAIR: Договори і Постановлεня (Правъ и Волностεй)`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Назва документа чи заголовок розділу, що координує «Договори» та «Постановлεня/Постановлення» як офіційний термін конституційного акта.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Синтаксичні вживання всередині наративного тексту чи статей.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **6**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **6**
  - **`SENTENCE-COUNT`:** **6**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Номінативна бінарна назва: NOM.PL(договори / договоры) + кон'юнкція [и / і] + NOM.PL(постановлεня / постановлення). Буквально: «Договори і Постановлення».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-028]`: Тимченко (Т. 1, с. 764): «договоръ — угода, трактат, взаємно ухвалені статті: «Договори і Постановлення прав і вольностей» (1710)».
  - **CONTEXTUAL RECONSTRUCTION:** Заголовковий комплекс пам'ятки 1710 року, що виступає українським канцелярським відповідником латинської титульної пари *Pacta et Constitutiones*.
  - **MODERN ANALOGY (CAUTIONARY):** Установчий публічний акт (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Термінологічне закріплення виборчих зобов'язань володаря перед виборцями.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2273]` **`SRC-ORLYK-1710`** (рядок 13) | форма: `Договори`
    - **MATCH-RULE-ID:** `DOG-R01-TITULAR`
    - **MATCH-EVIDENCE:** Document title formula: «TITLE: Договори і Постановлεня Правъ и Волностεй Войска Запорожск...»
  - `[LEX-INV2-2276]` **`SRC-ORLYK-1710`** (рядок 19) | форма: `Договори`
    - **MATCH-RULE-ID:** `DOG-R01-TITULAR`
    - **MATCH-EVIDENCE:** Parallel title rendition: «Договори і Постановлення прав і вольностей Війська Запороз...»
  - `[LEX-INV2-2278]` **`SRC-ORLYK-1710`** (рядок 22) | форма: `Договоры`
    - **MATCH-RULE-ID:** `DOG-R01-TITULAR`
    - **MATCH-EVIDENCE:** Bilingual parallel title formula: «...ones legum libertatumque Exercitus Zaporoviensis (Договоры и Постановлεnѧ правъ и волностεй войсковыхъ).»
  - `[LEX-INV2-2281]` **`SRC-ORLYK-1710`** (рядок 25) | форма: `Договори`
    - **MATCH-RULE-ID:** `DOG-R01-TITULAR`
    - **MATCH-EVIDENCE:** Header rubric formula: «=== Договори і Постановлення прав і вольностей Війська Запороз...»
  - `[LEX-INV2-2282]` **`SRC-ORLYK-1710`** (рядок 71) | форма: `Договоры`
    - **MATCH-RULE-ID:** `DOG-R01-TITULAR`
    - **MATCH-EVIDENCE:** Chancery header formula: «Договоры и Постановлεnѧ»
  - `[LEX-INV2-2283]` **`SRC-ORLYK-1710`** (рядок 75) | форма: `Договори`
    - **MATCH-RULE-ID:** `DOG-R01-TITULAR`
    - **MATCH-EVIDENCE:** Rubric formula: «Договори і Постановлення[1]»

---

### CONST-DOG-002 — `VERB-COVENANT: договорили и постановили з [гетманомъ]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ДОГОВОРИТИ (VERB: множина)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `VERB-COVENANT: договорили и постановили з [гетманомъ]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Дієслово *договорили* у парній конструкції з *постановили* за участю суб'єктів (Старшина, Військо Запорозьке) та реципієнта з прийменником «з» (з гетьманом).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Іменникові вживання або інші дієслівні форми.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **2**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **2**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Парний дієслівний предикат минулого часу: V.PL(договорили) + кон'юнкція [и] + V.PL(постановили) + прийменник [з] + INS(особа правителя). Буквально: «договорили і постановили з гетьманом».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-027]`, `[LEX-EVID-028]`: ЕСУМ (Т. 2, с. 96): «договорити — завершити розмову, досягти усної згоди сторін»; Тимченко (Т. 1, с. 764): «договорити — укласти умови, взаємно погодити».
  - **CONTEXTUAL RECONSTRUCTION:** Перформативний вираз взаємного узгодження умов обрання гетьмана між виборною корпорацією (Старшина, Кошовий, Військо Запорозьке) та обраною особою (Пилип Орлик).
  - **MODERN ANALOGY (CAUTIONARY):** Взаємне укладення умов (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Ствердження того, що влада гетьмана постає не з монаршого пожалування, а з двосторонньої згоди сторін.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2328]` **`SRC-ORLYK-1710`** (рядок 129) | форма: `договорили`
    - **MATCH-RULE-ID:** `DOG-R02-VERB-COVENANT`
    - **MATCH-EVIDENCE:** Coordinate verb phrase 'договорили и постановили з яснεвεлможнымъ': «...вигнεня үпалых правъ своих и волностεй войсковых, договорили и постановили з яснεвεлможнымъ, εго милостю, пано...»
  - `[LEX-INV2-2373]` **`SRC-ORLYK-1710`** (рядок 197) | форма: `договорили`
    - **MATCH-RULE-ID:** `DOG-R02-VERB-COVENANT`
    - **MATCH-EVIDENCE:** Coordinate verb phrase with election context: «...таршина, атаманъ кошовый и всε Войско Zапорожскоε договорили и постановили з яснεвεлможнымъ гεтманомъ, при εлε...»

---

### CONST-DOG-003 — `VERB-COMPLY: [додержати / исполнити] + [договоровъ / договори сії]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ДОГОВОРЪ (NOUN: множина)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `VERB-COMPLY: [додержати / исполнити] + [договоровъ / договори сії]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Іменник договори (у родовому чи знахідному відмінку) як об'єкт дієслів неухильного додержання, виконання чи підтвердження монархом.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Заголовкові формули та прийменникові вживання способу дії.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **7**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **7**
  - **`SENTENCE-COUNT`:** **5**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Об'єктне керування дієсловами дотримання або виконання: V(додεржалъ / исполнити / потвердити) + GEN/ACC.PL(договоровъ / договори). Буквально: «договорів додержати», «договори виконанню поручати».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-028]`: Тимченко (Т. 1, с. 764): «договоръ — взаємні письмові зобов'язання, затверджені присягою («поприсяжених договорів додержати»)».
  - **CONTEXTUAL RECONSTRUCTION:** У тексті 1710 р. погоджені статті набувають обов'язкової юридичної сили для обраного володаря через вимогу непорушного дотримання під загрозою апеляції до протектора.
  - **MODERN ANALOGY (CAUTIONARY):** Непорушність ухвалених зобов'язань (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Механізм контролю ради над гетьманським правлінням під загрозою звинувачення в порушенні присяги.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2329]` **`SRC-ORLYK-1710`** (рядок 129) | форма: `договоровъ`
    - **MATCH-RULE-ID:** `DOG-R03-VERB-COMPLY`
    - **MATCH-EVIDENCE:** Governed by verb 'нεнарушимо додεржалъ': «...дуючих пунктами изображεных, а собою поприсяжεных договоровъ и постановлεній, нεнарушимо додεржалъ, лεчь и за...»
  - `[LEX-INV2-2335]` **`SRC-ORLYK-1710`** (рядок 131) | форма: `договорів`
    - **MATCH-RULE-ID:** `DOG-R03-VERB-COMPLY`
    - **MATCH-EVIDENCE:** Governed by verb 'дотримував... договорів та постанов': «...римував усіх тих, що тут ідуть написані, пунктів, договорів та постанов, собою попрясяжених, а також, щоб вон...»
  - `[LEX-INV2-2401]` **`SRC-ORLYK-1710`** (рядок 331) | форма: `договоры`
    - **MATCH-RULE-ID:** `DOG-R03-VERB-COMPLY`
    - **MATCH-EVIDENCE:** Governed by verb phrase 'скутεчному исполнεнію поручаεм': «...ности войсковыε, нεпорушимому zахованю и оборонѣ, договоры засъ сії и постановлεня скутεчному исполнεнію пор...»
  - `[LEX-INV2-2406]` **`SRC-ORLYK-1710`** (рядок 336) | форма: `договори`
    - **MATCH-RULE-ID:** `DOG-R03-VERB-COMPLY`
    - **MATCH-EVIDENCE:** Governed by 'договори сі та постанови для конечного виконання': «...військові для непорушного збереження та оборони, договори сі та постанови для конечного виконання, які його...»
  - `[LEX-INV2-2413]` **`SRC-ORLYK-1710`** (рядок 342) | форма: `договоры`
    - **MATCH-RULE-ID:** `DOG-R03-VERB-COMPLY`
    - **MATCH-EVIDENCE:** Object clause of ratification: «...озвεдεный на zнамεнитый үрядъ гεтманский, яко сіε договоры и постановлεня тут описанныε, а с полною обрадою...»
  - `[LEX-INV2-2421]` **`SRC-ORLYK-1710`** (рядок 345) | форма: `договори`
    - **MATCH-RULE-ID:** `DOG-R03-VERB-COMPLY`
    - **MATCH-EVIDENCE:** Parallel object clause: «...а на Низу залишається, через посланих осіб, що ці договори й постанови, тут описані і межи мною і тим-таки З...»
  - `[LEX-INV2-2424]` **`SRC-ORLYK-1710`** (рядок 366) | форма: `договорів`
    - **MATCH-RULE-ID:** `DOG-R03-VERB-COMPLY`
    - **MATCH-EVIDENCE:** Royal confirmation object: «Затвердження почесних договорів королем Швеції.»

---

### CONST-DOG-004 — `PREP-TREATY: по [Зборовскому договору / посольским договорам / в договорах]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ДОГОВОРЪ (NOUN)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `PREP-TREATY: по [Зборовскому договору / посольским договорам / в договорах]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Прийменникова конструкція «по» (давальний відмінок) або «в» (місцевий відмінок), що апелює до ратифікованого міжнародного чи публічного трактату як правової підстави дій.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Орудний відмінок способу ухвалення («общим договором»).
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **3**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **3**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Прийменникова сполука відповідності/підстави: «по + DAT(договору / договорам)» або «въ + LOC(договорах)». Буквально: «по Зборовскому договору», «по посольским договорам», «в договорах изображеных».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-028]`: Тимченко (Т. 1, с. 764): «по договору — згідно з умовами раніше укладеного трактату («по Зборовскому договору мир учинити»)».
  - **CONTEXTUAL RECONSTRUCTION:** У Березневих статтях 1654 та тексті 1710 року сполука слугує правовою аргументацією: посилання на ратифіковані умови минулих угод як підставу чинних претензій.
  - **MODERN ANALOGY (CAUTIONARY):** Посилання на діючий договірний акт (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Апеляція до легітимності писаного трактату у міждержавних претензіях.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2263]` **`SRC-MARCH-1654`** (рядок 72) | форма: `договорам`
    - **MATCH-RULE-ID:** `DOG-R04-PREP-TREATY`
    - **MATCH-EVIDENCE:** Prepositional phrase 'по посольским договорам' establishes legal expectation: «...овому уложению, и по констытуцыи, и по посольским договорам царское величество ожидал исправленья. А гетмана...»
  - `[LEX-INV2-2264]` **`SRC-MARCH-1654`** (рядок 72) | форма: `договору`
    - **MATCH-RULE-ID:** `DOG-R04-PREP-TREATY`
    - **MATCH-EVIDENCE:** Prepositional phrase 'по Зборовскому договору' conditions peace: «...н Казимер король учинит с ними мир по Зборовскому договору, и на православную християнскую веру гонения чини...»
  - `[LEX-INV2-2298]` **`SRC-ORLYK-1710`** (рядок 111) | форма: `договорах`
    - **MATCH-RULE-ID:** `DOG-R04-PREP-TREATY`
    - **MATCH-EVIDENCE:** Prepositional phrase 'в договорах и статьях' records solemn obligations: «...лεй россійских, надѣючися, жε обовязковъ своих, в договорах и статьях изображεных и присягою ствεржεных, Г[ос...»

---

### CONST-DOG-005 — `INS-ENACTMENT: общимъ договоромъ [үстановляεтъся и үзаконяεтся]`
- **КЛЮЧОВИЙ ТЕРМІН:** `ДОГОВОРЪ (NOUN: орудний однини)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `INS-ENACTMENT: общимъ договоромъ [үстановляεтъся и үзаконяεтся]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Орудний відмінок однини у супроводі прикметника «общимъ/загальним» при предикатах законодавчого встановлення (*установляється і узаконюється*).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Множинні форми та прийменникові керування.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **2**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **2**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Орудний відмінок засобу встановлення: ADJ(общимъ) + INS(договоромъ) + пасивні дієслова V.PASS(үстановляεтъся и үзаконяεтся). Буквально: «спільним договором установлюється і узаконюється».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-027]`, `[LEX-EVID-028]`: Тимченко (Т. 1, с. 764): «общим договором — за загальною згодою сторін, спільним ухваленням».
  - **CONTEXTUAL RECONSTRUCTION:** Введення обов'язкового правила щодо військових маєтностей та податків виключно через спільну згоду ради і гетьмана, що виключає приватне одноосібне розпорядження.
  - **MODERN ANALOGY (CAUTIONARY):** Колегіальне законодавче ухвалення (*MODERN ANALOGY ≠ HISTORICAL SENSE; вживання consensus заборонено*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Юридичне обмеження фінансового свавілля гетьманського двору на користь військового скарбу.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2389]` **`SRC-ORLYK-1710`** (рядок 237) | форма: `договоромъ`
    - **MATCH-RULE-ID:** `DOG-R05-INS-ENACTMENT`
    - **MATCH-EVIDENCE:** Formula 'общимъ договоромъ үстановляεтъся и нεпрεмѣнно үзаконяεтся': «...мъ шафовали. Тεды и тεпεр таковый порадокъ общимъ договоромъ үстановляεтъся и нεпрεмѣнно үзаконяεтся, абы zа ү...»
  - `[LEX-INV2-2390]` **`SRC-ORLYK-1710`** (рядок 241) | форма: `договором`
    - **MATCH-RULE-ID:** `DOG-R05-INS-ENACTMENT`
    - **MATCH-EVIDENCE:** Parallel Ukrainian translation rendition: «...то й тепер такий порядок установлюється загальним договором і неодмінно узаконюється, аби після звільнення, д...»

---

### CONST-PAKT-001 — `TITULAR-TREATY: Pakta Hadziackie / Пакти і Конституції`
- **КЛЮЧОВИЙ ТЕРМІН:** `ПАКТЪ / PAKTA (NOUN: plurale tantum)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `TITULAR-TREATY: Pakta Hadziackie / Пакти і Конституції`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Називний відмінок латинсько-польської форми *Pakta* або руської *Пакти* у назвах договорів та колофонах.
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Синтаксичні непрямі відмінки в тілі статей.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **5**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **5**
  - **`SENTENCE-COUNT`:** **5**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Називний відмінок латино-польської форми мн. *Pakta* або руської форми мн. *Пакти* у заголовкових та рубрикативних позиціях: NOM.PL(Pakta / Пакти) + ADJ/GEN(Hadziackie / и Постановлεня). Буквально: «пакти Гадяцькі», «пакти і постанови».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** , : СЛМ XVI–XVII (Вип. 21, с. 14): «пактъ (частіше pl. пакты) — артикули публічної згоди, мирний трактат, умови договору»; Brückner (s. 392): «pakt, pakta — публічно-правові артикули угоди, запозичення з латини (pactum / pacta conventa)».
  - **CONTEXTUAL RECONSTRUCTION:** Уживається як титульна назва або рубрика письмового зводу взаємно узгоджених артикулів (Гадяч 1658, Бендери 1710); маркує високий публічно-правовий статус документу.
  - **MODERN ANALOGY (CAUTIONARY):** Міжнародний договір / конституційний пакт (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Рецепція поняття *pacta* шляхетського права Речі Посполитої для оформлення козацької автономії чи державності.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2135]` **`SRC-HADIACH-1658`** (рядок 3) | форма: `Pakta`
    - **MATCH-RULE-ID:** `PAKT-R01-TITULAR`
    - **MATCH-EVIDENCE:** Heading formula: «WORK: Pakta Hadziackie / Ugoda Hadziacka (16 вересня 1658 рок...»
  - `[LEX-INV2-2136]` **`SRC-HADIACH-1658`** (рядок 5) | форма: `Pakta`
    - **MATCH-RULE-ID:** `PAKT-R01-TITULAR`
    - **MATCH-EVIDENCE:** Document title citation: «...ською археографічною публікацією / pl.wikisource (Pakta Hadziackie autentyczne)»
  - `[LEX-INV2-2137]` **`SRC-HADIACH-1658`** (рядок 17) | форма: `Pakta`
    - **MATCH-RULE-ID:** `PAKT-R01-TITULAR`
    - **MATCH-EVIDENCE:** Header formula: «Pakta Hadziackie autentyczne. 16 września 1658 postanow...»
  - `[LEX-INV2-2425]` **`SRC-ORLYK-1710`** (рядок 387) | форма: `Пакти`
    - **MATCH-RULE-ID:** `PAKT-R01-TITULAR`
    - **MATCH-EVIDENCE:** Modern title commentary: «↑ Інший переклад: "Пакти і Конституція". Від нього походить назва "Констит...»
  - `[LEX-INV2-2426]` **`SRC-ORLYK-1710`** (рядок 398) | форма: `Пакти`
    - **MATCH-RULE-ID:** `PAKT-R01-TITULAR`
    - **MATCH-EVIDENCE:** Archival title citation: «факсимільне відтворення оригінальної публікації: «Пакти і Конституції» Української козацької держави (до...»

---

### CONST-PAKT-002 — `VERB-RATIFY: [zawrzeć / potwierdzić / utwierdzić] + [tych pakt]`
- **КЛЮЧОВИЙ ТЕРМІН:** `PAKT (NOUN: genitive plural)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `VERB-RATIFY: [zawrzeć / potwierdzić / utwierdzić] + [tych pakt]`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Родовий відмінок множини *pakt* у сполученні з дієсловами або віддієслівними іменниками укладення, утвердження чи підтвердження союзу (*do zawarcia pakt*, *dla tych pakt utwierdzenia*).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Орудний відмінок та заголовкові назви.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **4**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **4**
  - **`SENTENCE-COUNT`:** **4**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Родовий відмінок множини *pakt* під керуванням дієслів або віддієслівних іменників процедури скріплення: PREP(do / dla) + NOUN/V.INF(zawarcia / utwierdzenia) + GEN.PL(tych pakt). Буквально: «до укладення пактів», «для утвердження цих пактів».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** , : СЛМ XVI–XVII (Вип. 21, с. 14): «заключити / утвердити пакты — надати чинності домовленостям через формальний публічний акт»; Brückner (s. 392): «zawrzeć pakta — скласти формальну присяжну угоду».
  - **CONTEXTUAL RECONSTRUCTION:** Позначає сеймову та міждержавну процедуру надання юридичної сили артикулам через присягу комісарів та затвердження монархом / сеймом.
  - **MODERN ANALOGY (CAUTIONARY):** Ратифікація та набуття чинності міждержавним трактатом (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Надання комісарським домовленостям вищої загальнодержавної сили через парламентський акт.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2171]` **`SRC-HADIACH-1658`** (рядок 50) | форма: `pakt`
    - **MATCH-RULE-ID:** `PAKT-R02-VERB-RATIFY`
    - **MATCH-EVIDENCE:** Governed by noun 'potwierdzenia': «4. Dla tym lepszego tych pakt potwierdzenia i pewności Hetman Wojsk Ruskich do...»
  - `[LEX-INV2-2174]` **`SRC-HADIACH-1658`** (рядок 68) | форма: `pakt`
    - **MATCH-RULE-ID:** `PAKT-R02-VERB-RATIFY`
    - **MATCH-EVIDENCE:** Governed by phrase 'do zawarcia pakt': «...arem Jego Mością Moskiewskim, jeśliby do zawarcia pakt Jego Królewskiej Mości i Stanom Koronnym i Wielki...»
  - `[LEX-INV2-2205]` **`SRC-HADIACH-1659`** (рядок 362) | форма: `pakt`
    - **MATCH-RULE-ID:** `PAKT-R02-VERB-RATIFY`
    - **MATCH-EVIDENCE:** Governed by noun 'utwierdzenia': «Dla tym lepszego tych pakt utwierdzenia, y»
  - `[LEX-INV2-2210]` **`SRC-HADIACH-1659`** (рядок 511) | форма: `pakt`
    - **MATCH-RULE-ID:** `PAKT-R02-VERB-RATIFY`
    - **MATCH-EVIDENCE:** Governed by phrase 'zawarcia pakt': «zawarcia pakt lego K. M. y Stanom Koron-»

---

### CONST-PAKT-003 — `PART-GUARANTEE: пактами [обваровані / стверджені / укріплені] границы`
- **КЛЮЧОВИЙ ТЕРМІН:** `ПАКТЪ (NOUN: орудний множини)`
- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `PART-GUARANTEE: пактами [обваровані / стверджені / укріплені] границы`
- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** Орудний відмінок множини *пактами*, що синтаксично керується пасивними дієприкметниками гарантування, утвердження чи укріплення меж держави («пактами обваровані», «пактами стверджених»).
- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** Заголовкові або ратифікаційні форми.
- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**
  - **`TOKEN-COUNT`:** **4**
  - **`CONSTRUCTION-INSTANCE-COUNT`:** **4**
  - **`SENTENCE-COUNT`:** **2**
- **СЕМАНТИЧНЕ РОЗШАРУВАННЯ (FIVE-TIER EPISTEMIC PIPELINE):**
  - **MORPHOSYNTACTIC PARAPHRASE:** Орудний відмінок множини засобу гарантування: INS.PL(пактами) + пасивні дієприкметники PARTICIPLE(обваровани / стверджены / укрѣплены) + іменник NOM/ACC.PL(границы / кордони). Буквально: «пактами обваровані», «пактами стверджені».
  - **LEXICOGRAPHIC GLOSS (L2 EVIDENCE):** `[LEX-EVID-029]`: СЛМ XVI–XVII (Вип. 21, с. 15): «пактами обварованый — забезпечений, юридично закріплений письмовими трактатами».
  - **CONTEXTUAL RECONSTRUCTION:** У тексті 1710 року орудний відмінок *пактами* виступає юридичним інструментом фіксації кордонів Гетьманщини за міжнародними договорами Богдана Хмельницького з сусідніми державами.
  - **MODERN ANALOGY (CAUTIONARY):** Договірне визнання державних кордонів (*MODERN ANALOGY ≠ HISTORICAL SENSE*).
- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** Апеляція до зовнішнього дипломатичного визнання території як підстави суверенітету гетьманської держави.
- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**
  - `[LEX-INV2-2352]` **`SRC-ORLYK-1710`** (рядок 152) | форма: `пактами`
    - **MATCH-RULE-ID:** `PAKT-R03-PART-GUARANTEE`
    - **MATCH-EVIDENCE:** Governed by passive participle 'ствεржεных': «...ая Россія, ωтчизна n[а]ша, жεбы в своих границях, пактами ωт Рѣчи Посполитой Полской, от Nаяснѣйшой Порты и...»
  - `[LEX-INV2-2353]` **`SRC-ORLYK-1710`** (рядок 152) | форма: `пактами`
    - **MATCH-RULE-ID:** `PAKT-R03-PART-GUARANTEE`
    - **MATCH-EVIDENCE:** Governed by passive participle 'обварованы зостали': «...гεтманскои и войсковои поступлεны, вѣчнε ωтданы и пактами обварованы зостали, нε была zигвалчεна и нарушεна...»
  - `[LEX-INV2-2360]` **`SRC-ORLYK-1710`** (рядок 155) | форма: `пактами`
    - **MATCH-RULE-ID:** `PAKT-R03-PART-GUARANTEE`
    - **MATCH-EVIDENCE:** Governed by passive participle 'стверджених': «...Вітчизна наша, щоб у своїх кордонах, стверджених пактами від Річі Посполитої польської і від Московської д...»
  - `[LEX-INV2-2361]` **`SRC-ORLYK-1710`** (рядок 155) | форма: `пактами`
    - **MATCH-RULE-ID:** `PAKT-R03-PART-GUARANTEE`
    - **MATCH-EVIDENCE:** Governed by passive participle 'пактами укріплені': «...а Хмельницького були відступлені, вічно віддані й пактами укріплені від Річі Посполитої польської в гетьман...»


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
| `CONST-RYAD-001` | `РЯДЪ (VERB: рядити ся)` | SRC-RP-EXP (XII–XV ст.) | Давньоруська | Процесуальний судовий кодекс | Князівсько-боярський суд | **3** | **3** | **3** |
| `CONST-RYAD-002` | `РЯДЪ (NOUN)` | SRC-RP-EXP (XII–XV ст.) | Давньоруська | Процесуальний судовий кодекс | Князівсько-боярський суд | **6** | **6** | **3** |
| `CONST-RYAD-003` | `РЯДЪ (NOUN)` | SRC-RP-EXP (XII–XV ст.) | Давньоруська | Процесуальний судовий кодекс | Князівсько-боярський суд | **1** | **1** | **1** |
| `CONST-RYAD-004` | `РЯДЪ (NOUN)` | SRC-LS-1566, SRC-LS-1588 (1566 р., 1588 р.) | Руська канцелярська | Загальнодержавна кодифікація, Кодифікований земський статут | Вальний Сойм / Трибунал ВКЛ, Сойм ВКЛ / земські суди | **3** | **3** | **3** |
| `CONST-RYAD-005` | `РЯДЪ (NOUN)` | SRC-LS-1588 (1588 р.) | Руська канцелярська | Загальнодержавна кодифікація | Вальний Сойм / Пани-Рада ВКЛ | **2** | **2** | **2** |
| `CONST-DOG-001` | `ДОГОВОРЪ (NOUN)` | SRC-ORLYK-1710 (1710 р.) | Староукраїнська книжна | Конституційний договір-пакт | Генеральна Рада / Гетьманський уряд | **6** | **6** | **6** |
| `CONST-DOG-002` | `ДОГОВОРЪ (VERB)` | SRC-ORLYK-1710 (1710 р.) | Староукраїнська книжна | Конституційний договір-пакт | Генеральна Рада / Гетьманський уряд | **2** | **2** | **2** |
| `CONST-DOG-003` | `ДОГОВОРЪ (NOUN)` | SRC-ORLYK-1710 (1710 р.) | Староукраїнська книжна | Конституційний договір-пакт | Генеральна Рада / Гетьманський уряд | **7** | **7** | **5** |
| `CONST-DOG-004` | `ДОГОВОРЪ (NOUN)` | SRC-MARCH-1654, SRC-ORLYK-1710 (1654 р., 1710 р.) | Двомовна московсько-руська, Староукраїнська книжна | Двосторонні договірні статті, Конституційний договір-пакт | Посольський приказ, Генеральна Рада | **3** | **3** | **2** |
| `CONST-DOG-005` | `ДОГОВОРЪ (NOUN)` | SRC-ORLYK-1710 (1710 р.) | Староукраїнська книжна | Конституційний договір-пакт | Генеральна Рада / Гетьманський уряд | **2** | **2** | **2** |
| `CONST-PAKT-001` | `ПАКТЪ / PAKTA (NOUN)` | SRC-HADIACH-1658, SRC-ORLYK-1710 (1658 р., 1710 р.) | Ранньомодерна польська, Староукраїнська книжна | Міжнародно-правовий пакт унії, Конституційний договір-пакт | Комісія Корони і В.К.Р., Генеральна Рада | **5** | **5** | **5** |
| `CONST-PAKT-002` | `PAKT (NOUN)` | SRC-HADIACH-1658, SRC-HADIACH-1659 (1658 р., 1659 р.) | Ранньомодерна польська | Міжнародно-правовий пакт унії, Сеймова ратифікаційна конституція | Спільна Комісія, Вальний Сейм Речі Посполитої | **4** | **4** | **4** |
| `CONST-PAKT-003` | `ПАКТЪ (NOUN)` | SRC-ORLYK-1710 (1710 р.) | Староукраїнська книжна | Конституційний договір-пакт | Генеральна Рада / Гетьманський уряд | **4** | **4** | **2** |

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
---

## 5. АУДИТ ТИСКУ НА ПОКРИТТЯ ТА РЕЗИДУАЛЬНІ ТОКЕНИ (COVERAGE PRESSURE & RESIDUAL AUDIT)

> [EPISTEMIC GUARD]
> **100% COVERAGE IS NOT A GOAL IN ITSELF.**
> Примусове підганяння ізольованих, заголовкових або редакторських токенів під синтаксичні конструкції спотворює граматичний профіль слів.
> Нижче наведено аудит токенів тріади: розмежування **стабільних синтаксичних рамок** та **резидуальних / метатекстових входжень**.

### А. Баланс покриття токенів тріади:
| ЛЕКСЕМА | ВСЬОГО ТОКЕНІВ | КЛАСИФІКОВАНО В СТАБІЛЬНІ СИНТАКСИЧНІ РАМКИ | РЕЗИДУАЛЬНІ / МЕТАТЕКСТОВІ ТОКЕНИ (`RESIDUAL`) | ЧИСТИЙ ГРАМАТИЧНИЙ СТАТУС |
|:---|:---:|:---:|:---:|:---|
| **`РЯДЪ`** | **15** | **15** (100%) | **0** | Усі 15 токенів є автентичним текстом джерел і мають чіткі дієслівні, прийменникові або предикативні зв'язки. |
| **`ДОГОВОРЪ`** | **20** | **14** (70%) | **6** (30%) | 6 токенів належать до заголовкових рубрик або повторів титулу (`CONST-DOG-001`), які є метатекстовими назвами, а не реченнєвими рамками. |
| **`ПАКТЪ`** | **13** | **8** (61.5%) | **5** (38.5%) | 2 токени (`LEX-INV2-2425`, `2426`) є **сучасними редакторськими коментарями / виносками** видання, а 3 токени (`LEX-INV2-2135..2137`) — заголовками Гадяцького акта. |

### Б. Реєстр резидуальних та редакторських токенів (`RESIDUAL / EDITORIAL LEDGER`):
1. **`LEX-INV2-2425`** (`SRC-ORLYK-1710`, ряд. 387, форма `Пакти`):
   - *Контекст:* «↑ Інший переклад: "Пакти і Конституція". Від нього походить назва...»
   - *Статус:* **EDITORIAL ARTIFACT (MODERN APPARATUS)**. Не є частиною автентичного тексту 1710 року!
   - *Корекція аудиту:* Вилучено зі складу живих синтаксичних конструкцій; переведено в категорію `META-EDITORIAL`.
2. **`LEX-INV2-2426`** (`SRC-ORLYK-1710`, ряд. 398, форма `Пакти`):
   - *Контекст:* «факсимільне відтворення оригінальної публікації: «Пакти і Конституції»...»
   - *Статус:* **BIBLIOGRAPHIC CITATION (MODERN APPARATUS)**.
   - *Корекція аудиту:* Вилучено зі складу живих синтаксичних конструкцій; переведено в категорію `META-EDITORIAL`.
3. **`LEX-INV2-2135`, `2136`, `2137`** (`SRC-HADIACH-1658`, ряд. 3, 5, 17, форма `Pakta`):
   - *Контекст:* Заголовки документа та метадані публікації (*Pakta Hadziackie autentyczne*).
   - *Статус:* **TITULAR / RUBRIC RESIDUAL**. Позначає назву акта, а не синтаксичну взаємодію слів усередині статті.
4. **`LEX-INV2-2273`, `2276`, `2278`, `2281`, `2282`, `2283`** (`SRC-ORLYK-1710`, ряд. 13..75, форми `Договори / Договоры`):
   - *Контекст:* Заголовкові комплекси та рубрики видання (*«Договори і Постановлення»*).
   - *Статус:* **TITULAR HEADING FORMULA**. Фіксує номінацію документа, але не є дієслівно-керованою конструкцією.

> [MODEL REFINEMENT INSIGHT]
> Відмова від штучного 100% покриття показує справжню структуру мовного матеріалу:
> - **Справжніх живих синтаксичних інстанцій у корпусі:**
>   - `РЯДЪ`: **15/15** активних текстових вживань.
>   - `ДОГОВОРЪ`: **14** текстових реченнєвих вживань + **6** метатекстових заголовків.
>   - `ПАКТЪ`: **8** текстових реченнєвих вживань (4 у Гадячі + 4 в Орлика) + **3** заголовкових + **2** сучасних редакторських артефакти.
