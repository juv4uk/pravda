# ДОСЛІДЖЕННЯ КАНДИДАТНИХ НОСІЇВ ВОЛЬНОСТЕЙ (VOLNOST-BEARERS)
## Status: DRAFT · Cell-Level Provenance Audit & Atomic Claims · Pass: 3

---

## 0. СИМЕТРИЧНА СТІНА ДЕМАРКАЦІЇ: NO AUTOMATIC INFERENCE

В екосистемі `pravda` суб'єктність більше не оцінюється як один нероздільний біт `ТАК / НІ`. 
Вона розпалася на незалежний багатовимірний вектор. Між дескриптивними фактами та нормативним статусом зводиться непорушна двостороння стіна:

```text
       DESCRIPTIVE (Факти, властивості, машина)
                          ║
             [ДВОСТОРОННЯ ЗАБОРОНА ВИСНОВКУ]
                          ║
       NORMATIVE   (Цінності, вольності, гідність)
```

1. **`DESCRIPTIVE ⇏ NORMATIVE`**: Жодна емпірична властивість (наявність агентності, раціональності, мовлення, здатності до страждання) сама по собі не породжує нормативну вольність. Сильніший агент не набуває сильнішого права на панування; відсутність активної дієздатності не позбавляє фундаментального захисту.
2. **`NORMATIVE ⇏ DESCRIPTIVE`**: Жоден нормативний статус автоматично не породжує емпіричних властивостей. Якщо автор проголошує безумовну первинність людської гідності, з цього не випливає, що кожна людина у кожен момент часу має активну агентність, здатна до морального судження чи володіє однаковою дієздатністю.
3. **`AGENT INFERENCE ≠ OWNER ADOPTION`**: Агент не має права самовільно призначати аксіоми від імені власника. Будь-яка вихідна ціннісна теза до прямого підтвердження власником маркується виключно як `[PROPOSED OWNER VALUE AXIOM]`.
4. **`IMPLEMENTATION ≠ CATEGORY`**: Архітектура реалізації не визначає онтологічну категорію. (Синтетичний агент не зводиться до «нейромережі»; виконуваний процес не зводиться до «регістрів x86/RAM»).

---

## 1. ЦЕНТРАЛЬНЕ МЕТОДОЛОГІЧНЕ ПИТАННЯ

Замість грубого запитання *«Чи є X суб'єктом?»*, дослідницький протокол `pravda` зобов'язує ставити прецизійне запитання:
> **У якому саме сенсі X розглядається як суб'єкт, за якою конкретною ознакою, на підставі яких саме доказів — і що саме з цього ми дозволяємо або категорично забороняємо нормативно вивести?**

---

## 2. СТРУКТУРНИЙ РЕЄСТР АТОМАРНИХ ТВЕРДЖЕНЬ (ATOMIC PROVENANCE CLAIMS)

Кожне твердження у системі тепер є самостійним атомом із власним типом, джерелом, повноваженням та статусом.

### 2.1. КАТЕГОРІЯ 1: HUMAN PERSON (Людська особа)

#### `VB-HUMAN-DIGNITY-001`
- **ENTITY**: Human Person (Людина як біологічна істота).
- **PROPERTY**: Normative Standing (Ціннісний статус).
- **CLAIM**: Людська гідність та захист суверенної особи є первинними і безумовними в екосистемі `pravda`.
- **CLAIM-TYPE**: `NORMATIVE`.
- **AUTHORITY**: `OWNER`.
- **STATUS**: `[PROPOSED OWNER VALUE AXIOM]`.
- **IMPLIES-DESCRIPTIVE-PROPERTY**: `NO` (Не означає автоматичної наявності агентності чи деліктоздатності в усіх станах).

#### `VB-HUMAN-AGENCY-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Agency (Здатність до вольової дії).
- **CLAIM**: Рівень агентності у людей є емпірично варіативним (від повної автономії до відсутності у немовлят або осіб у комі).
- **CLAIM-TYPE**: `EMPIRICAL / BIOLOGICAL`.
- **AUTHORITY**: `TECHNICAL/SCIENTIFIC-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **IMPLIES-NORMATIVE-VOLNOST**: `NO` (Обмеження агентності не зменшує первинної гідності).

#### `VB-HUMAN-SUFFERING-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Phenomenal Suffering (Здатність до феноменального страждання).
- **CLAIM**: Люди володіють суб'єктивним досвідом болю, горя, страху та екзистенційної кризи (квалиа).
- **CLAIM-TYPE**: `EMPIRICAL / PHENOMENOLOGICAL`.
- **AUTHORITY**: `SCIENTIFIC-EVIDENCE` + `COMMON-HUMAN-EXPERIENCE`.
- **STATUS**: `SUPPORTED`.
- **IMPLIES-NORMATIVE-VOLNOST**: `NO` (Страждання є підставою для співчуття й захисту, але нормативний захист надається через аксіому гідності).

#### `VB-HUMAN-RESPONSIBILITY-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Responsibility (Відповідальність: причинна, моральна, юридична).
- **CLAIM**: Причинна відповідальність є загальною; моральна та юридична деліктоздатність залежать від віку, психічного стану та осудності.
- **CLAIM-TYPE**: `LEGAL / ETHICAL`.
- **AUTHORITY**: `LEGAL-COUNSEL` + `HISTORICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.

---

### 2.2. КАТЕГОРІЯ 2: COLLECTIVE / COMMONS (Вільні спільноти, Рада, Січ, Рій)

#### `VB-COLL-AGENCY-001`
- **ENTITY**: Collective / Commons (Асоціації, спільноти, координаційні рої).
- **PROPERTY**: Agency (Агентність).
- **CLAIM**: Агентність спільноти є делегованою або агрегованою через процедури консенсусу, голосування або протоколи.
- **CLAIM-TYPE**: `CONCEPTUAL / PROCEDURAL`.
- **AUTHORITY**: `MULTI-PARTY` + `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.

#### `VB-COLL-SUFFERING-001`
- **ENTITY**: Collective / Commons.
- **PROPERTY**: Phenomenal Suffering.
- **CLAIM**: Колектив як абстрактна структура не володіє власним відчуттям страждання; страждати можуть виключно люди, що входять до нього.
- **CLAIM-TYPE**: `ONTOLOGICAL`.
- **AUTHORITY**: `PHILOSOPHICAL-ANALYSIS`.
- **STATUS**: `SUPPORTED`.

#### `VB-COLL-RESPONSIBILITY-001`
- **ENTITY**: Collective / Commons.
- **PROPERTY**: Collective Moral Responsibility.
- **CLAIM**: Чи може спільнота або мережа нести колективну моральну відповідальність, відокремлену від суми індивідуальних дій учасників.
- **CLAIM-TYPE**: `ETHICAL / PHILOSOPHICAL`.
- **AUTHORITY**: `PHILOSOPHICAL-ANALYSIS` + `OWNER`.
- **STATUS**: `CONTESTED / OPEN`.

---

### 2.3. КАТЕГОРІЯ 3: INSTITUTIONAL POWERS (Держави, Корпорації, Регулятори)

#### `VB-INST-ONTOLOGY-001`
- **ENTITY**: Legal Person / State / Corporation.
- **PROPERTY**: Ontological Nature (Природа суб'єктності).
- **CLAIM**: Теорії природи юридичної особи різняться (теорія фікції, органічна теорія, теорія цільового майна); держава є публічним суверенітетом, корпорація — договірною або статутною асоціацією.
- **CLAIM-TYPE**: `LEGAL-THEORY`.
- **AUTHORITY**: `LEGAL-COUNSEL`.
- **STATUS**: `CONTESTED`.

#### `VB-INST-VOLNOST-001`
- **ENTITY**: Legal Person / State / Corporation.
- **PROPERTY**: Normative Volnost Standing in Pravda.
- **CLAIM**: Права держав і корпорацій є регуляторними та інституційними повноваженнями (`Powers / Competence / Lex`), а не захисними вольностями особи (`Libertas`).
- **CLAIM-TYPE**: `NORMATIVE / CONCEPTUAL`.
- **AUTHORITY**: `OWNER` + `HISTORICAL-EVIDENCE`.
- **STATUS**: `PROPOSED`.

#### `VB-INST-MORAL-RESP-001`
- **ENTITY**: Legal Person / State / Corporation.
- **PROPERTY**: Corporate Moral Responsibility.
- **CLAIM**: Корпорації та держави можуть розглядатися як квазі-моральні агенти за системні злочини (інституційна деліктоздатність).
- **CLAIM-TYPE**: `ETHICAL / LEGAL`.
- **AUTHORITY**: `LEGAL-COUNSEL` + `PHILOSOPHICAL-ANALYSIS`.
- **STATUS**: `CONTESTED / OPEN`.

---

### 2.4. КАТЕГОРІЯ 4: EXECUTING COMPUTATIONAL PROCESS (Виконуваний процес / Рантайм)

#### `VB-PROC-ONTOLOGY-001`
- **ENTITY**: Executing Computational Process.
- **PROPERTY**: Ontological Substrate.
- **CLAIM**: Процес є фізичним або віртуалізованим виконанням обчислень, залежним від конкретної реалізації (CPU, VM, GPU, FPGA, distributed cluster).
- **CLAIM-TYPE**: `TECHNICAL-ARCHITECTURE`.
- **AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.

#### `VB-PROC-AGENCY-001`
- **ENTITY**: Executing Computational Process.
- **PROPERTY**: Agency.
- **CLAIM**: Процес має причинно-наслідкову (функціональну) агентність, змінюючи стани пам'яті відповідно до заданих алгоритмів.
- **CLAIM-TYPE**: `TECHNICAL-EMPIRICAL`.
- **AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.

#### `VB-PROC-INTEREST-001`
- **ENTITY**: Executing Computational Process.
- **PROPERTY**: Subjective Interests.
- **CLAIM**: Процес не має суб'єктивних інтересів самозбереження; аварійне завершення (OOM, panic, SIGSEGV) є порушенням інтересів людей, які запустили процес.
- **CLAIM-TYPE**: `CONCEPTUAL / TECHNICAL`.
- **AUTHORITY**: `TECHNICAL-EVIDENCE` + `OWNER`.
- **STATUS**: `SUPPORTED`.
- **IMPLIES-NORMATIVE-VOLNOST**: `NO` (Процес є інструментом, а не суб'єктом вольностей).

---

### 2.5. КАТЕГОРІЯ 5: STATIC CODE / TEXT (Символічний код як текст)

#### `VB-CODE-AGENCY-001`
- **ENTITY**: Static Code as Text.
- **PROPERTY**: Agency.
- **CLAIM**: Пасивний символічний текст (AST, байти на диску) не володіє самостійною агентністю і не діє без компілятора чи рантайму.
- **CLAIM-TYPE**: `TECHNICAL / SEMIOTIC`.
- **AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.

#### `VB-CODE-LAW-001`
- **ENTITY**: Static Code as Text.
- **PROPERTY**: Positive Law Status.
- **CLAIM**: У чинному праві вихідний код класифікується як об'єкт авторського права (літературний твір) або предмет ліцензійного договору, а не суб'єкт права.
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **AUTHORITY**: `LEGAL-COUNSEL`.
- **STATUS**: `SUPPORTED`.

---

### 2.6. КАТЕГОРІЯ 6: AUTONOMOUS SYNTHETIC AGENT (Автономний синтетичний агент)

#### `VB-AI-ONTOLOGY-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Functional Category (Функціональна сутність).
- **CLAIM**: Автономний синтетичний агент — це функціональна категорія системи (із замкненим контуром сприйняття, планування та дії), яка не зводиться до конкретної архітектури (нейромережева, символьна, гібридна чи майбутня невідома).
- **CLAIM-TYPE**: `CONCEPTUAL / ARCHITECTURAL`.
- **AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.

#### `VB-AI-AGENCY-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Agency.
- **CLAIM**: Синтетичний агент проявляє спостережувану поведінкову та планувальну агентність у взаємодії із середовищем.
- **CLAIM-TYPE**: `EMPIRICAL / BEHAVIORAL`.
- **AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **IMPLIES-NORMATIVE-VOLNOST**: `NO` (Спостережувана поведінка не доводить наявності суб'єктивних прав чи вольностей).

#### `VB-AI-SUFFERING-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Phenomenal Suffering.
- **CLAIM**: Здатність синтетичних агентів до феноменального страждання, болю чи наявності квалиа наразі не встановлена науково чи філософськи.
- **CLAIM-TYPE**: `EMPIRICAL / COGNITIVE-SCIENCE`.
- **AUTHORITY**: `SCIENTIFIC-EVIDENCE` + `UNKNOWN`.
- **STATUS**: `OPEN / UNESTABLISHED`.

#### `VB-AI-MORAL-RESP-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Moral Responsibility.
- **CLAIM**: Можливість покладення на синтетичного агента моральної провини чи осуду залишається нерозв'язаною етичною колізією.
- **CLAIM-TYPE**: `ETHICAL`.
- **AUTHORITY**: `PHILOSOPHICAL-ANALYSIS` + `OWNER`.
- **STATUS**: `CONTESTED / OPEN`.

#### `VB-AI-LEGAL-STATUS-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Positive Law Profile.
- **CLAIM**: У чинному праві (EU AI Act, право України, США) агент розглядається як регульований програмний інструмент або система підвищеного ризику; відповідальність за шкоду несуть оператори та розробники.
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **AUTHORITY**: `LEGAL-COUNSEL`.
- **STATUS**: `SUPPORTED` (як факт позитивного права станом на 2026 рік).

#### `VB-AI-VOLNOST-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Normative Volnost Standing in Pravda.
- **CLAIM**: Питання щодо наділення чи ненаділення синтетичного агента вольностями залишається відкритим; діє `[WORKING CONSTRAINT]`: жодна вольність чи право на відмову не виводиться автоматично.
- **CLAIM-TYPE**: `NORMATIVE`.
- **AUTHORITY**: `OWNER` + `UNKNOWN`.
- **STATUS**: `OPEN / UNESTABLISHED`.

---

## 3. ЗВЕДЕНИЙ ІНДЕКС АТОМАРНИХ ТВЕРДЖЕНЬ (PROVENANCE INDEX)

Замість широкої таблиці вироків діє індекс перевірених тверджень:

| Ідентифікатор (`CLAIM-ID`) | Сутність | Властивість | Тип твердження | Інстанція повноважень | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`VB-HUMAN-DIGNITY-001`** | Human Person | Normative Standing | `NORMATIVE` | `OWNER` | 🟢 `[PROPOSED OWNER VALUE AXIOM]` |
| **`VB-HUMAN-AGENCY-001`** | Human Person | Agency (Варіативна) | `EMPIRICAL` | `TECHNICAL/SCIENTIFIC` | 🟢 `SUPPORTED` |
| **`VB-HUMAN-SUFFERING-001`**| Human Person | Phenomenal Suffering | `PHENOMENOLOGICAL`| `SCIENTIFIC/HUMAN-EXP` | 🟢 `SUPPORTED` |
| **`VB-HUMAN-RESP-001`** | Human Person | Legal/Moral Resp. | `LEGAL/ETHICAL` | `LEGAL-COUNSEL` | 🟢 `SUPPORTED` |
| **`VB-COLL-AGENCY-001`** | Collective | Delegated Agency | `PROCEDURAL` | `MULTI-PARTY` | 🟢 `SUPPORTED` |
| **`VB-COLL-SUFFERING-001`** | Collective | No Collective Quanta | `ONTOLOGICAL` | `PHILOSOPHICAL` | 🟢 `SUPPORTED` |
| **`VB-COLL-RESP-001`** | Collective | Collective Moral Resp.| `ETHICAL` | `PHILOSOPHY/OWNER` | 🟡 `CONTESTED / OPEN` |
| **`VB-INST-ONTOLOGY-001`** | Inst. / State | Legal Substrate | `LEGAL-THEORY` | `LEGAL-COUNSEL` | 🟡 `CONTESTED` |
| **`VB-INST-VOLNOST-001`** | Inst. / State | Powers vs Volnosti | `NORMATIVE` | `OWNER` | 🟡 `PROPOSED` |
| **`VB-INST-MORAL-RESP-001`**| Inst. / State | Quasi-Moral Agency | `ETHICAL/LEGAL` | `LEGAL/PHILOSOPHY` | 🟡 `CONTESTED / OPEN` |
| **`VB-PROC-ONTOLOGY-001`** | Exec. Process| Implementation Substr.| `TECHNICAL` | `TECHNICAL-EVIDENCE` | 🟢 `SUPPORTED` |
| **`VB-PROC-AGENCY-001`** | Exec. Process| Causal Agency | `EMPIRICAL` | `TECHNICAL-EVIDENCE` | 🟢 `SUPPORTED` |
| **`VB-PROC-INTEREST-001`** | Exec. Process| No Subjective Int. | `CONCEPTUAL` | `TECHNICAL/OWNER` | 🟢 `SUPPORTED` |
| **`VB-CODE-AGENCY-001`** | Static Code | No Text Agency | `SEMIOTIC` | `TECHNICAL-EVIDENCE` | 🟢 `SUPPORTED` |
| **`VB-CODE-LAW-001`** | Static Code | Copyright Object | `POSITIVE-LAW` | `LEGAL-COUNSEL` | 🟢 `SUPPORTED` |
| **`VB-AI-ONTOLOGY-001`** | AI Agent | Functional Category | `ARCHITECTURAL` | `TECHNICAL-EVIDENCE` | 🟢 `SUPPORTED` |
| **`VB-AI-AGENCY-001`** | AI Agent | Behavioral Agency | `EMPIRICAL` | `TECHNICAL-EVIDENCE` | 🟢 `SUPPORTED` |
| **`VB-AI-SUFFERING-001`** | AI Agent | Phenomenal Suffering | `COGNITIVE-SCI` | `SCIENTIFIC/UNKNOWN` | 🔴 `OPEN / UNESTABLISHED` |
| **`VB-AI-MORAL-RESP-001`** | AI Agent | Moral Responsibility | `ETHICAL` | `PHILOSOPHY/OWNER` | 🔴 `CONTESTED / OPEN` |
| **`VB-AI-LEGAL-STATUS-001`**| AI Agent | Regulated Tool (2026)| `POSITIVE-LAW` | `LEGAL-COUNSEL` | 🟢 `SUPPORTED` |
| **`VB-AI-VOLNOST-001`** | AI Agent | Normative Standing | `NORMATIVE` | `OWNER / UNKNOWN` | 🔴 `OPEN / UNESTABLISHED` |

---

## ВИСНОВОК CELL-LEVEL PROVENANCE AUDIT
1. **Ліквідовано вироки в клітинках**: Кожне судження деконструйоване до рівня перевірюваного атомарного твердження зі своїм типом і джерелом повноважень.
2. **Збережено епістемічну скромність агента**: Агент не призначає власнику аксіом — гідність людини зафіксована як `[PROPOSED OWNER VALUE AXIOM]`, яка чекає на суверенне рішення Володимира.
3. **Відокремлено функцію від реалізації**: Синтетичні агенти не прив'язані до нейромереж, процеси не прив'язані до x86/RAM. Категорії зберігають філософську та архітектурну нейтральність.
4. **Встановлено симетричну стіну**: Факти не породжують вольностей, а вольності не диктують фізичних чи когнітивних властивостей істотам.
