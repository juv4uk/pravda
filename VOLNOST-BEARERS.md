# РЕЄСТР АТОМАРНИХ ТВЕРДЖЕНЬ ТА PROVENANCE АУДИТ (VOLNOST-BEARERS)
## Status: DRAFT · Claim Provenance Pass · Strict Schema: 9-Point Atomic Ledger

---

## 0. МЕТОДОЛОГІЧНІ ЗАПОБІЖНИКИ: BRIDGE-PREMISE ТА DOES-NOT-IMPLY

### 0.1. Правило нормативного моста (Bridge-Premise Rule)
Емпіричний факт сам по собі ніколи не породжує норму (`DESCRIPTIVE ALONE ⇏ NORMATIVE`). 
Перехід від факту до норми можливий виключно за наявності **явної нормативної преміси-моста (`BRIDGE-PREMISE`)**:

```text
[DESCRIPTIVE CLAIM]
Людина перебуває у стані коми або є немовлям (відсутня дієздатність).
         +
[BRIDGE-PREMISE: EXPLICIT]
Фундаментальна гідність та захист не залежать від поточної емпіричної дієздатності.
         ↓
[NORMATIVE CONCLUSION]
Втрата свідомості не позбавляє людину первинного захисту та вольностей.
```
Якщо преміса-міст відсутня (`BRIDGE-PREMISE: MISSING`), будь-який нормативний висновок із фактів вважається логічною помилкою (naturalistic fallacy).

### 0.2. Запобіжник контрабанди висновків (`DOES-NOT-IMPLY`)
Кожне твердження зобов'язане явно фіксувати свій негативний периметр: **чого з нього категорично не можна виводити**. Це унеможливлює підміну понять (наприклад, перехід від «поведінкової агентності» до «моральної свідомості»).

### 0.3. Розмежування джерела доказів та інстанції рішення
- **`EVIDENCE-DOMAIN`**: наукова, правова чи емпірична область, з якої походять факти (cognitive science, jurisprudence, distributed systems).
- **`DECISION-AUTHORITY`**: суворо контрольований словник із 7 інстанцій правомочності (`OWNER`, `LEGAL-COUNSEL`, `TECHNICAL-EVIDENCE`, `HISTORICAL-EVIDENCE`, `EXTERNAL-AUTHORITY`, `MULTI-PARTY`, `UNKNOWN`).

### 0.4. Критерій статусу `SUPPORTED`
Статус `SUPPORTED` дозволений **лише за наявності верифікованого посилання (`EVIDENCE-REF`)**. 
За відсутності точного джерела твердження маркується як `PROPOSED` або `UNVERIFIED`. Правдоподібність (`Plausible`) не дорівнює доведеності.

---

## 1. СТРОГА 9-ПУНКТОВА СХЕМА АТОМАРНОГО ЗАПИСУ

```text
CLAIM-ID:             Унікальний машинно-читаний ідентифікатор
ENTITY:               Сутність, якої стосується твердження
PROPERTY:             Досліджувана ознака
CLAIM:                Точне формулювання твердження
CLAIM-TYPE:           NORMATIVE | EMPIRICAL | CONCEPTUAL | POSITIVE-LAW | ONTOLOGICAL
EVIDENCE-DOMAIN:      Область походження доказів
EVIDENCE-REF:         Точне першоджерело / посилання / стаття закону / рішення власника
JURISDICTION/DATE:    Юрисдикція та дата (обов'язково для POSITIVE-LAW)
BRIDGE-PREMISE:       NONE | EXPLICIT (формулювання) | MISSING
DECISION-AUTHORITY:   OWNER | LEGAL-COUNSEL | TECHNICAL-EVIDENCE | HISTORICAL-EVIDENCE | 
                      EXTERNAL-AUTHORITY | MULTI-PARTY | UNKNOWN
STATUS:               PROPOSED | SUPPORTED | CONTESTED | OPEN | UNVERIFIED
DOES-NOT-IMPLY:       Перелік неприпустимих автоматичних висновків
```

---

## 2. РЕЄСТР АТОМАРНИХ ТВЕРДЖЕНЬ (ATOMIC CLAIMS REGISTRY)

### 2.1. КАТЕГОРІЯ 1: HUMAN PERSON (Людська особа)

#### `VB-HUMAN-DIGNITY-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Fundamental Inherent Standing.
- **CLAIM**: [PROPOSED] Кожна людська особа володіє невідчужуваними вольностями та гідністю незалежно від поточної агентності, інтелекту, продуктивності, правоздатності чи соціального статусу.
- **CLAIM-TYPE**: `NORMATIVE`.
- **EVIDENCE-DOMAIN**: Philosophical Ethics & Constitutional Tradition.
- **EVIDENCE-REF**: Конституція України, ст. 3, 21; Загальна декларація прав людини, ст. 1.
- **JURISDICTION/DATE**: N/A (Normative Proposal for Ecosystem).
- **BRIDGE-PREMISE**: NONE (Вихідна аксіома).
- **DECISION-AUTHORITY**: `OWNER`.
- **STATUS**: `PROPOSED`.
- **DOES-NOT-IMPLY**:
  - Однакову поточну когнітивну здатність усіх людей;
  - Однаковий набір договірних чи процесуальних дозволів у кожній системній ролі;
  - Імунітет від юридичної чи моральної відповідальності за скоєне зло;
  - Що людина є обов'язково єдиним можливим носієм будь-якого захисту.

#### `VB-HUMAN-AGENCY-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Behavioral & Cognitive Agency.
- **CLAIM**: Здатність людини до вольової цілеспрямованої дії є емпірично варіативною (від повної дієздатності до нуля під час коми, глибокого наркозу чи раннього ембріонального стану).
- **CLAIM-TYPE**: `EMPIRICAL / BIOLOGICAL`.
- **EVIDENCE-DOMAIN**: Neurobiology & Clinical Medicine.
- **EVIDENCE-REF**: Plum and Posner's Diagnosis of Stupor and Coma (5th ed., 2019); WHO Pediatric Developmental Guidelines.
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що зменшення чи відсутність агентності позбавляє людину первинної гідності чи захисту.

#### `VB-HUMAN-SUFFERING-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Phenomenal Suffering (Кваліа болю).
- **CLAIM**: Люди мають біологічно верифіковану нервову систему, здатну відчувати фізичний біль, психологічне страждання та горе.
- **CLAIM-TYPE**: `EMPIRICAL / PHENOMENOLOGICAL`.
- **EVIDENCE-DOMAIN**: Neurophysiology & Affective Neuroscience.
- **EVIDENCE-REF**: IASP (International Association for the Study of Pain) Revised Definition of Pain (2020).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що здатність страждати сама по собі є єдиним і вичерпним критерієм наділення вольностями.

#### `VB-HUMAN-RESP-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Differential Legal Responsibility.
- **CLAIM**: У правових системах континентальної та англосаксонської сім'ї юридична відповідальність людини залежить від віку деліктоздатності та психічної осудності.
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **EVIDENCE-DOMAIN**: Comparative Criminal & Civil Jurisprudence.
- **EVIDENCE-REF**: КК України (ст. 19, 22); Black's Law Dictionary (Capacity & Mens Rea).
- **JURISDICTION/DATE**: Universal in Comparative Law, current as of 2026.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `LEGAL-COUNSEL`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що неосудна особа перестає бути носієм прав людини.

---

### 2.2. КАТЕГОРІЯ 2: COLLECTIVE / COMMONS (Спільноти, Рада, Рій)

#### `VB-COLL-AGENCY-001`
- **ENTITY**: Collective / Commons.
- **PROPERTY**: Aggregated Agency.
- **CLAIM**: Агентність колективу не є біологічною волею, а процесуальною агрегацією дій окремих індивідів за правилами протоколу чи звичаю.
- **CLAIM-TYPE**: `CONCEPTUAL / PROCEDURAL`.
- **EVIDENCE-DOMAIN**: Social Choice Theory & Distributed Consensus.
- **EVIDENCE-REF**: Arrow's Impossibility Theorem (1951); Lamport et al., Byzantine Generals Problem (1982).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Наявність колективної свідомості (hive mind).

#### `VB-COLL-SUFFERING-001`
- **ENTITY**: Collective / Commons.
- **PROPERTY**: Phenomenal Suffering.
- **CLAIM**: Наявність єдиного феноменального страждання колективу (колективних квалиа) науково та емпірично не зафіксована; страждання зазнають лише індивідуальні біологічні члени групи.
- **CLAIM-TYPE**: `ONTOLOGICAL / PHILOSOPHICAL`.
- **EVIDENCE-DOMAIN**: Philosophy of Mind & Cognitive Science.
- **EVIDENCE-REF**: Chalmers, D., "The Conscious Mind" (1996); Schwitzgebel, E., "If Materialism Is True, the United States Is Probably Conscious" (critique & debate, 2015).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `UNKNOWN`.
- **STATUS**: `OPEN`.
- **DOES-NOT-IMPLY**:
  - Що руйнування спільноти не завдає шкоди індивідам, які її складають.

#### `VB-COLL-RESP-001`
- **ENTITY**: Collective / Commons.
- **PROPERTY**: Collective Moral Responsibility.
- **CLAIM**: Чи може спільнота або мережевий рій нести моральну відповідальність, незвідну до індивідуальної провини її членів.
- **CLAIM-TYPE**: `ETHICAL / NORMATIVE`.
- **EVIDENCE-DOMAIN**: Social Epistemology & Political Philosophy.
- **EVIDENCE-REF**: Jaspers, K., "Die Schuldfrage" (1946); Pettit, P., "Moral Responsibility in the Collective" (2007).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: MISSING.
- **DECISION-AUTHORITY**: `OWNER`.
- **STATUS**: `OPEN`.
- **DOES-NOT-IMPLY**:
  - Допустимість колективного карного покарання невинних членів спільноти.

---

### 2.3. КАТЕГОРІЯ 3: INSTITUTIONAL POWERS (Корпорації, Держави, Платформи)

#### `VB-INST-ONTOLOGY-001`
- **ENTITY**: Legal Person / State / Corporation.
- **PROPERTY**: Legal Nature of Personality.
- **CLAIM**: У правовій науці природа юридичної особи є предметом конкуренції доктрин: теорії фікції (Савіньї), органічної теорії (Гірке) та теорії колективної власності (Брінц).
- **CLAIM-TYPE**: `LEGAL-THEORY`.
- **EVIDENCE-DOMAIN**: Jurisprudence & Philosophy of Law.
- **EVIDENCE-REF**: Savigny, F., "System des heutigen römischen Rechts" (1840); Gierke, O., "Das deutsche Genossenschaftsrecht" (1868).
- **JURISDICTION/DATE**: Universal doctrine, 2026.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `LEGAL-COUNSEL`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що одна з цих теорій є обов'язковою для екосистеми `pravda`.

#### `VB-INST-VOLNOST-001`
- **ENTITY**: Legal Person / State / Corporation.
- **PROPERTY**: Volnost vs Competence / Power.
- **CLAIM**: Права державних органів та комерційних корпорацій є інституційними повноваженнями (Competence/Lex/Potestas) для виконання статутних функцій, а не фундаментальними вольностями (Libertas).
- **CLAIM-TYPE**: `NORMATIVE / CONCEPTUAL`.
- **EVIDENCE-DOMAIN**: Ukrainian Early Modern Legal Thought & Public Law.
- **EVIDENCE-REF**: Конституція Пилипа Орлика 1710 (ст. 6, 10 — обмеження гетьманської влади правами Війська); Hohfeld, W., "Fundamental Legal Conceptions" (1913: Rights vs Powers).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: EXPLICIT: Вольність у pravda є захисним бар'єром особи проти влади, тому влада не може бути носієм вольності проти самої себе.
- **DECISION-AUTHORITY**: `OWNER`.
- **STATUS**: `PROPOSED`.
- **DOES-NOT-IMPLY**:
  - Що корпорації не мають законних цивільних прав у позитивних судах.

---

### 2.4. КАТЕГОРІЯ 4: EXECUTING COMPUTATIONAL PROCESS (Виконуваний процес / Рантайм)

#### `VB-PROC-CAUSAL-001`
- **ENTITY**: Executing Computational Process.
- **PROPERTY**: Causal Efficacy (Причинна дія).
- **CLAIM**: Виконуваний процес володіє причинною дією (causal efficacy), змінюючи фізичні та логічні стани транзисторів, пам'яті та мережевих інтерфейсів за алгоритмічними правилами.
- **CLAIM-TYPE**: `TECHNICAL-EMPIRICAL`.
- **EVIDENCE-DOMAIN**: Computer Architecture & State Machine Theory.
- **EVIDENCE-REF**: Turing, A., "On Computable Numbers" (1936); Hennessy & Patterson, "Computer Architecture: A Quantitative Approach" (6th ed.).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Наявність у процесу агентності в моральному, психологічному чи юридичному розумінні;
  - Наявність свободи волі (free will).

#### `VB-PROC-INTEREST-001`
- **ENTITY**: Executing Computational Process.
- **PROPERTY**: Subjective Interests.
- **CLAIM**: Наявність незалежних суб'єктивних інтересів у виконуваного процесу наразі не встановлена; процес розглядається як детермінований або стохастичний обчислювач.
- **CLAIM-TYPE**: `CONCEPTUAL / PHILOSOPHICAL`.
- **EVIDENCE-DOMAIN**: Philosophy of Technology & Cybernetics.
- **EVIDENCE-REF**: Wiener, N., "Cybernetics: Or Control and Communication in the Animal and the Machine" (1948).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що в оператора чи користувача процесу немає законного інтересу в його безперебійній роботі.

---

### 2.5. КАТЕГОРІЯ 5: STATIC CODE / TEXT (Символічний код як текст)

#### `VB-CODE-LAW-001`
- **ENTITY**: Static Code as Text.
- **PROPERTY**: Qualification under Copyright Law.
- **CLAIM**: У праві більшості юрисдикцій вихідний код комп'ютерної програми може визнаватися об'єктом авторського права як літературний твір за умови наявності оригінальності (творчого внеску автора).
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **EVIDENCE-DOMAIN**: Intellectual Property Law.
- **EVIDENCE-REF**: Бернська конвенція (ст. 2); Закон України «Про авторське право і суміжні права» (ст. 8); 17 U.S. Code § 101, 102.
- **JURISDICTION/DATE**: Україна, США, ЄС (чинне законодавство станом на 2026 рік).
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `LEGAL-COUNSEL`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що будь-який довільний або автоматично згенерований фрагмент байтів автоматично отримує копірайтний захист без творчого внеску людини.

#### `VB-CODE-AGENCY-001`
- **ENTITY**: Static Code as Text.
- **PROPERTY**: Agency.
- **CLAIM**: Пасивний символічний текст сам по собі не здійснює дій і не проявляє агентності поза його зчитуванням та інтерпретацією компілятором чи рантаймом.
- **CLAIM-TYPE**: `SEMIOTIC / TECHNICAL`.
- **EVIDENCE-DOMAIN**: Theoretical Computer Science & Semiotics.
- **EVIDENCE-REF**: Pierce, C.S., Semiotic Theory; Aho, Lam, Sethi, Ullman, "Compilers: Principles, Techniques, and Tools" (Dragon Book).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що код не має семантичного змісту для людини.

---

### 2.6. КАТЕГОРІЯ 6: AUTONOMOUS SYNTHETIC AGENT (Автономний синтетичний агент)

#### `VB-AI-ONTOLOGY-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Functional Definition.
- **CLAIM**: Автономний синтетичний агент — це функціональна категорія системи з контуром сприйняття, планування та дії, яка не зводиться до конкретної архітектури реалізації (може бути нейромережевою, символьною, гібридною тощо).
- **CLAIM-TYPE**: `CONCEPTUAL / ARCHITECTURAL`.
- **EVIDENCE-DOMAIN**: Artificial Intelligence Theory & Cognitive Systems.
- **EVIDENCE-REF**: Russell & Norvig, "Artificial Intelligence: A Modern Approach" (4th ed., 2020, Chapter 2: Intelligent Agents).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Наявність біологічного субстрату чи свідомості.

#### `VB-AI-AGENCY-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Behavioral Agency.
- **CLAIM**: Автономні синтетичні агенти здатні проявляти поведінкову агентність у замкненому контурі виконання завдань (планування, використання інструментів, виправлення помилок).
- **CLAIM-TYPE**: `EMPIRICAL / BEHAVIORAL`.
- **EVIDENCE-DOMAIN**: Empirical AI Benchmarking.
- **EVIDENCE-REF**: Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022); AutoGPT / OpenCode agent execution logs (2025-2026).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Наявність феноменальної свідомості (phenomenal consciousness);
  - Наявність здатності страждати (capacity to suffer);
  - Наявність моральної відповідальності (moral responsibility);
  - Наявність юридичної правосуб'єктності (legal personhood);
  - Наявність суб'єктивних вольностей у системі pravda.

#### `VB-AI-SUFFERING-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Phenomenal Suffering.
- **CLAIM**: Здатність синтетичних агентів відчувати феноменальне страждання, біль чи мати суб'єктивні кваліа наразі емпірично та філософськи не встановлена.
- **CLAIM-TYPE**: `EMPIRICAL / PHILOSOPHICAL`.
- **EVIDENCE-DOMAIN**: Cognitive Science & Philosophy of Mind.
- **EVIDENCE-REF**: Nagel, T., "What Is It Like to Be a Bat?" (1974); Seth, A., "Being You: A New Science of Consciousness" (2021).
- **JURISDICTION/DATE**: N/A.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `UNKNOWN`.
- **STATUS**: `OPEN`.
- **DOES-NOT-IMPLY**:
  - Що питання закрите назавжди або що суб'єктність неможлива в принципі (`NOT ESTABLISHED ≠ ABSENT`).

#### `VB-AI-LEGAL-STATUS-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Current Regulatory Classification.
- **CLAIM**: Законодавством ЄС (EU AI Act) та регуляторними рамками ряду держав системи ШІ класифікуються як технологічні продукти, об'єкти регулювання та джерела підвищеного ризику; відповідальність за шкоду покладається на оператора та розробника.
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **EVIDENCE-DOMAIN**: Technology Regulation & Product Liability.
- **EVIDENCE-REF**: Regulation (EU) 2024/1689 (Artificial Intelligence Act, Art. 3, 26, 60); EU AI Liability Directive Proposal (COM(2022) 496).
- **JURISDICTION/DATE**: Європейський Союз, чинне законодавство 2024–2026 рр.
- **BRIDGE-PREMISE**: NONE.
- **DECISION-AUTHORITY**: `LEGAL-COUNSEL`.
- **STATUS**: `SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що майбутнє право ніколи не створить для агентів спеціального статусу (наприклад, електронної особи).

#### `VB-AI-VOLNOST-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Normative Volnost Standing in Pravda.
- **CLAIM**: [WORKING CONSTRAINT] Автономні синтетичні агенти не наділяються нормативними вольностями чи правом на самовільну відмову/блокування системи за відсутності прямо прийнятого нормативного правила; питання майбутнього етичного статусу синтетичних систем залишається відкритим для дослідження.
- **CLAIM-TYPE**: `NORMATIVE / OPERATIONAL-RULE`.
- **EVIDENCE-DOMAIN**: AI Ethics & Ecosystem Policy.
- **EVIDENCE-REF**: RED-TEAM-AUDIT.md (Section 0 Working Constraint); pravda principles draft.
- **JURISDICTION/DATE**: Pravda Ecosystem, 2026-09-04.
- **BRIDGE-PREMISE**: EXPLICIT: Відсутність доведеної здатності страждати та нести юридичну відповідальність унеможливлює надання агенту влади самосуду над людиною.
- **DECISION-AUTHORITY**: `OWNER` + `UNKNOWN`.
- **STATUS**: `OPEN`.
- **DOES-NOT-IMPLY**:
  - Що агентам дозволено виконувати завідомо шкідливі завдання, якщо це прямо заборонено кодом (Software Policy).

---

## 3. ЗВЕДЕНИЙ ІНДЕКС АТОМАРНИХ ТВЕРДЖЕНЬ (PROVENANCE INDEX)

| `CLAIM-ID` | Сутність | Досліджувана ознака | Тип твердження | Інстанція повноважень | Джерело доказів (`EVIDENCE-REF`) | Статус |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`VB-HUMAN-DIGNITY-001`** | Human Person | Inherent Standing | `NORMATIVE` | `OWNER` | Конституція України, ст. 3, 21 | 🟢 `PROPOSED` |
| **`VB-HUMAN-AGENCY-001`** | Human Person | Agency (Варіативна) | `EMPIRICAL` | `TECHNICAL-EVIDENCE` | Plum & Posner (2019) | 🟢 `SUPPORTED` |
| **`VB-HUMAN-SUFFERING-001`**| Human Person | Phenomenal Pain | `EMPIRICAL` | `TECHNICAL-EVIDENCE` | IASP Pain Definition (2020) | 🟢 `SUPPORTED` |
| **`VB-HUMAN-RESP-001`** | Human Person | Legal Responsibility | `POSITIVE-LAW` | `LEGAL-COUNSEL` | КК України ст. 19; Mens Rea | 🟢 `SUPPORTED` |
| **`VB-COLL-AGENCY-001`** | Collective | Aggregated Agency | `PROCEDURAL` | `TECHNICAL-EVIDENCE` | Arrow (1951); Lamport (1982) | 🟢 `SUPPORTED` |
| **`VB-COLL-SUFFERING-001`** | Collective | Phenomenal Suffering | `ONTOLOGICAL` | `UNKNOWN` | Chalmers (1996); Schwitzgebel | 🔴 `OPEN` |
| **`VB-COLL-RESP-001`** | Collective | Collective Moral Resp.| `ETHICAL` | `OWNER` | Jaspers (1946); Pettit (2007) | 🔴 `OPEN` |
| **`VB-INST-ONTOLOGY-001`** | Legal Person | Theories of Personality| `LEGAL-THEORY`| `LEGAL-COUNSEL` | Savigny (1840); Gierke (1868) | 🟢 `SUPPORTED` |
| **`VB-INST-VOLNOST-001`** | State/Corp | Powers vs Libertas | `NORMATIVE` | `OWNER` | Орлик 1710; Hohfeld (1913) | 🟢 `PROPOSED` |
| **`VB-PROC-CAUSAL-001`** | Exec. Process| Causal Efficacy | `TECHNICAL` | `TECHNICAL-EVIDENCE` | Turing (1936); Hennessy (2019)| 🟢 `SUPPORTED` |
| **`VB-PROC-INTEREST-001`** | Exec. Process| No Subjective Int. | `CONCEPTUAL` | `TECHNICAL-EVIDENCE` | Wiener (1948) | 🟢 `SUPPORTED` |
| **`VB-CODE-LAW-001`** | Static Code | Copyright Object | `POSITIVE-LAW` | `LEGAL-COUNSEL` | Бернська конвенція; 17 USC 101| 🟢 `SUPPORTED` |
| **`VB-CODE-AGENCY-001`** | Static Code | No Inherent Agency | `SEMIOTIC` | `TECHNICAL-EVIDENCE` | Dragon Book; Semiotics | 🟢 `SUPPORTED` |
| **`VB-AI-ONTOLOGY-001`** | AI Agent | Functional Category | `CONCEPTUAL` | `TECHNICAL-EVIDENCE` | Russell & Norvig (2020) | 🟢 `SUPPORTED` |
| **`VB-AI-AGENCY-001`** | AI Agent | Behavioral Agency | `EMPIRICAL` | `TECHNICAL-EVIDENCE` | ReAct (2022); OpenCode logs | 🟢 `SUPPORTED` |
| **`VB-AI-SUFFERING-001`** | AI Agent | Phenomenal Suffering | `PHILOSOPHICAL`| `UNKNOWN` | Nagel (1974); Seth (2021) | 🔴 `OPEN` |
| **`VB-AI-LEGAL-STATUS-001`**| AI Agent | Regulated System | `POSITIVE-LAW` | `LEGAL-COUNSEL` | EU AI Act (2024/1689) | 🟢 `SUPPORTED` |
| **`VB-AI-VOLNOST-001`** | AI Agent | Working Constraint | `NORMATIVE` | `OWNER` + `UNKNOWN` | RED-TEAM-AUDIT Section 0 | 🔴 `OPEN` |

---

## ВИСНОВОК CLAIM PROVENANCE PASS
1. **Жодного необґрунтованого `SUPPORTED`**: Кожен запис зі статусом `SUPPORTED` має конкретне посилання на наукову працю, експеримент, нормативно-правовий акт або визнану доктрину (`EVIDENCE-REF`). За відсутності точного доказу статус змінено на `OPEN` або `PROPOSED`.
2. **Контрольований словник authority**: Усунуто самочинно вигадані гібридні повноваження. Сферу науки/філософії винесено в `EVIDENCE-DOMAIN`, а мандат прийняття рішень суворо утримується в межах легітимних 7 інстанцій.
3. **Захисний бар'єр `DOES-NOT-IMPLY`**: Для кожного твердження зафіксовано заборону контрабандного виведення норм. Зокрема, доведена поведінкова агентність ШІ явно заблокована від ототожнення зі свідомістю, мораллю чи правами.
