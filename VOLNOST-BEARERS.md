# РЕЄСТР АТОМАРНИХ ТВЕРДЖЕНЬ: EVIDENCE ADMISSIBILITY & INFERENCE DISTANCE (VOLNOST-BEARERS)
## Status: DRAFT · Evidence Admissibility Pass · Schema: 13-Point Admissibility Ledger

---

## 0. МЕТОДОЛОГІЧНИЙ ПРИНЦИП: EVIDENCE-REF ≠ SUPPORTED

Головний урок попереднього проходу:
> **Сама лише наявність посилання в полі `EVIDENCE-REF` не робить твердження доведеним (`SUPPORTED`).**  
> Величезна частина інтелектуальних помилок виникає не через відсутність джерела, а через те, що **істинне джерело пришивають до твердження, якого воно насправді не встановлює**.

### 0.1. Поняття дистанції висновку (Inference Distance)
Ми суворо розрізняємо те, **що джерело буквально стверджує (`SOURCE-CLAIM`)**, і те, **що ми намагаємося з нього вивести (`TARGET-CLAIM`)**:

```text
TARGET CLAIM (Наше твердження)
       ▲
       │  [INFERENCE DISTANCE: DIRECT / INFERRED / ANALOGICAL]
       │  [BRIDGE-PREMISE: якщо target claim ширший за source claim]
       ▼
SOURCE CLAIM (Що джерело реально встановило)
       ▲
       │  [SOURCE-LOCATOR: точна стаття / сторінка / експеримент]
SOURCE (Першоджерело / Закон / Бенчмарк)
```

### 0.2. Семиступенева шкала доказової сили (Evidentiary Scale)
Замість бінарного `SUPPORTED / OPEN` запроваджується диференційована шкала:
1. `ATTESTED` — факт буквально зафіксований у первинному тексті чи законі.
2. `DIRECTLY-SUPPORTED` — емпіричний або технічний результат прямо відповідає суті твердження без логічних стрибків.
3. `INFERRED` — твердження спирається на джерело через явну, верифіковану дедуктивну/індуктивну премісу (`BRIDGE-PREMISE`).
4. `PLAUSIBLE` — правдоподібна гіпотеза з частковими непрямими свідченнями, але без формального доказу.
5. `CONTESTED` — твердження має відомі академічні або практичні спростування (`CONTRARY-EVIDENCE`).
6. `UNESTABLISHED` — відсутні емпіричні, правові чи логічні підстави для ствердження чи заперечення.
7. `REFUTED` — твердження прямо спростоване експериментом чи першоджерелом.

### 0.3. Розмежування для нормативних тверджень (Normative Demarcation)
Закон чи історичний манускрипт **не є доказом авторської аксіоми**:
- `CONTEMPORARY-LEGAL-PARALLEL` / `HISTORICAL-PARALLEL` — зовнішній контекст, що свідчить про схожість ідеї.
- `OWNER-DECISION-REF` — пряме суверенне рішення власника екосистеми (до його наявності: `NONE`, статус: `PROPOSED`).

---

## 1. СТРОГА 13-ПУНКТОВА СХЕМА АТОМАРНОГО ЗАПИСУ

```text
CLAIM-ID:             Унікальний машинно-читаний ідентифікатор
ENTITY:               Сутність дослідження
PROPERTY:             Досліджувана властивість
TARGET-CLAIM:         Точне формулювання нашого твердження
CLAIM-TYPE:           NORMATIVE | EMPIRICAL | CONCEPTUAL | POSITIVE-LAW | ONTOLOGICAL
EVIDENCE-KIND:        PRIMARY-LEGAL | EMPIRICAL-EXP | THEORETICAL-PROOF | PHILOSOPHICAL-ARG | HISTORICAL-DOC
SOURCE-REF:           Бібліографічне джерело / нормативно-правовий акт
SOURCE-LOCATOR:       Точна стаття, розділ, сторінка, DOI або run-id
SOURCE-CLAIM:         Що САМЕ джерело буквально встановило чи регламентувало
DIRECTNESS:           DIRECT | INFERRED | ANALOGICAL
BRIDGE-PREMISE:       NONE | EXPLICIT (текст преміси) | MISSING
CONTRARY-EVIDENCE:    Відомі контрприклади або альтернативні позиції
DECISION-AUTHORITY:   OWNER | LEGAL-COUNSEL | TECHNICAL-EVIDENCE | HISTORICAL-EVIDENCE | 
                      EXTERNAL-AUTHORITY | MULTI-PARTY | UNKNOWN
EVIDENTIARY-STATUS:   ATTESTED | DIRECTLY-SUPPORTED | INFERRED | PLAUSIBLE | CONTESTED | UNESTABLISHED
DOES-NOT-IMPLY:       Негативний периметр висновків
```

---

## 2. РЕЄСТР АТОМАРНИХ ТВЕРДЖЕНЬ (REFINED CLAIMS LEDGER)

### 2.1. HUMAN PERSON (Людська особа)

#### `VB-HUMAN-DIGNITY-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Fundamental Inherent Standing.
- **TARGET-CLAIM**: [PROPOSED] Кожна людська особа володіє невідчужуваними вольностями та гідністю в екосистемі `pravda` незалежно від поточної агентності, інтелекту, продуктивності, правоздатності чи соціального статусу.
- **CLAIM-TYPE**: `NORMATIVE`.
- **EVIDENCE-KIND**: PHILOSOPHICAL-ARG / LEGAL-PARALLEL.
- **SOURCE-REF**: Конституція України; Загальна декларація прав людини.
- **SOURCE-LOCATOR**: ст. 3, 21 Конституції України; ст. 1 ЗДПЛ.
- **SOURCE-CLAIM**: «Людина, її життя і здоров'я, честь і гідність, недоторканність і безпека визнаються в Україні найвищою соціальною цінністю... Усі люди народжуються вільними і рівними у своїй гідності та правах».
- **DIRECTNESS**: `ANALOGICAL` (Конституція є правовим контекстом і паралеллю, а не джерелом внутрішнього авторитету для приватної екосистеми).
- **BRIDGE-PREMISE**: EXPLICIT: Екосистема pravda свідомо приймає цей принцип як власну конституційну основу, не виводячи його з примусу держави.
- **CONTRARY-EVIDENCE**: Утилітаризм (Пітер Сінгер: моральний статус пропорційний здатності відчувати біль/інтереси, виключаючи ембріони/коматозників).
- **DECISION-AUTHORITY**: `OWNER`.
- **EVIDENTIARY-STATUS**: `PLAUSIBLE` (як пропозиція; очікує на пряме суверенне рішення `OWNER-DECISION-REF`).
- **DOES-NOT-IMPLY**:
  - Однакової емпіричної когнітивної спроможності всіх осіб;
  - Однакових ролей чи прав доступу до адміністративних функцій;
  - Імунітету від деліктної відповідальності.

#### `VB-HUMAN-AGENCY-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Cognitive & Behavioral Agency.
- **TARGET-CLAIM**: Здатність людини до вольової цілеспрямованої дії є емпірично варіативною (від повної автономії до повної відсутності в комі, глибокому наркозі чи ранніх стадіях розвитку).
- **CLAIM-TYPE**: `EMPIRICAL`.
- **EVIDENCE-KIND**: EMPIRICAL-EXP / CLINICAL.
- **SOURCE-REF**: Posner, J.B. et al., "Plum and Posner's Diagnosis and Treatment of Stupor and Coma".
- **SOURCE-LOCATOR**: 5th ed. (2019), Oxford University Press, Chapter 1: "The Pathophysiology of Consciousness", pp. 3–42.
- **SOURCE-CLAIM**: Свідомість має два виміри — неспання (arousal) та зміст (awareness); ураження ретикулярної формації або кори призводить до повної втрати вольової реакції при збереженні вегетативних функцій.
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Панпсихізм (стверджує наявність протосвідомості у будь-якій матерії; не має клінічного підтвердження).
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **EVIDENTIARY-STATUS**: `DIRECTLY-SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що особа в стані коми втрачає людську гідність або фундаментальний захист.

#### `VB-HUMAN-SUFFERING-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Phenomenal Suffering Capacity.
- **TARGET-CLAIM**: Людські особи володіють біологічною здатністю (capacity) до феноменального відчуття болю та страждання, обумовленою фізіологічним станом їхньої нервової системи.
- **CLAIM-TYPE**: `EMPIRICAL / PHENOMENOLOGICAL`.
- **EVIDENCE-KIND**: CLINICAL-DEFINITION / PHYSIOLOGICAL.
- **SOURCE-REF**: International Association for the Study of Pain (IASP).
- **SOURCE-LOCATOR**: Pain 2020; 161(9): 1976–1982. DOI: 10.1097/j.pain.0000000000001939.
- **SOURCE-CLAIM**: «Біль — це неприємний сенсорний та емоційний досвід, пов'язаний з фактичним або потенційним пошкодженням тканин або схожий на нього... Нездатність до комунікації не заперечує можливості того, що індивід відчуває біль».
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Вроджена анальгезія (CIPA: генетична нездатність відчувати фізичний біль при збереженні емоційного).
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **EVIDENTIARY-STATUS**: `DIRECTLY-SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що кожна людина відчуває біль щомиті;
  - Що здатність страждати є єдиним джерелом вольностей.

#### `VB-HUMAN-RESP-001`
- **ENTITY**: Human Person.
- **PROPERTY**: Legal Responsibility Capacity.
- **TARGET-CLAIM**: У кримінальному та цивільному праві обов'язок нести юридичну відповідальність не є абсолютним, а диференціюється залежно від віку, осудності та здатності усвідомлювати свої дії.
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **EVIDENCE-KIND**: PRIMARY-LEGAL.
- **SOURCE-REF**: Кримінальний кодекс України.
- **SOURCE-LOCATOR**: Статті 19 («Осудність»), 20 («Обмежена осудність»), 22 («Вік кримінальної відповідальності»).
- **SOURCE-CLAIM**: «Не підлягає кримінальній відповідальності особа, яка під час вчинення суспільно небезпечного діяння перебувала в стані неосудності, тобто не могла усвідомлювати свої дії або керувати ними внаслідок хронічного психічного захворювання».
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Об'єктивне ставлення у вину (Strict liability у цивільному праві за шкоду від джерела підвищеної небезпеки, де вина не є обов'язковою).
- **DECISION-AUTHORITY**: `LEGAL-COUNSEL`.
- **EVIDENTIARY-STATUS**: `ATTESTED`.
- **DOES-NOT-IMPLY**:
  - Що неосудна особа втрачає правовий захист чи статус людини.

---

### 2.2. COLLECTIVE / COMMONS (Спільноти, Рій)

#### `VB-COLL-AGENCY-001`
- **ENTITY**: Collective / Commons.
- **PROPERTY**: Aggregated Action & Coordination.
- **TARGET-CLAIM**: Розподілені вузли та групи людей здатні координувати дії та агрегувати рішення у спільні результати за формальними правилами консенсусу.
- **CLAIM-TYPE**: `TECHNICAL / PROCEDURAL`.
- **EVIDENCE-KIND**: THEORETICAL-PROOF.
- **SOURCE-REF**: Lamport, L., Shostak, R., Pease, M., "The Byzantine Generals Problem".
- **SOURCE-LOCATOR**: ACM Transactions on Programming Languages and Systems (TOPLAS), 1982, 4(3): 382–401.
- **SOURCE-CLAIM**: Алгоритми досягнення консенсусу гарантують, що всі лояльні процесори дійдуть згоди щодо спільного плану дій за умови, що кількість зрадників не перевищує $m$ при $3m+1$ вузлах.
- **DIRECTNESS**: `DIRECT` (для технічної координації) / `INFERRED` (для поняття «агентності спільноти»).
- **BRIDGE-PREMISE**: EXPLICIT: Спільне виконання узгодженого алгоритму багатьма вузлами операційно розглядається як скоординована дія колективу.
- **CONTRARY-EVIDENCE**: Теорема неможливості Ерроу (Arrow, 1951: неможливість бездоганного агрегування індивідуальних уподобань при демократичному виборі).
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **EVIDENTIARY-STATUS**: `DIRECTLY-SUPPORTED` (для координації) / `INFERRED` (для колективної дії).
- **DOES-NOT-IMPLY**:
  - Наявність у колективу власної феноменальної свідомості (hive consciousness);
  - Право більшості знищувати меншість.

#### `VB-COLL-SUFFERING-001`
- **ENTITY**: Collective / Commons.
- **PROPERTY**: Phenomenal Suffering.
- **TARGET-CLAIM**: Наявність окремого, незвідного до індивідів феноменального страждання у колективних утворень наразі науково та емпірично не встановлена.
- **CLAIM-TYPE**: `ONTOLOGICAL / PHILOSOPHICAL`.
- **EVIDENCE-KIND**: PHILOSOPHICAL-ARG.
- **SOURCE-REF**: Chalmers, D.J., "The Conscious Mind: In Search of a Fundamental Theory".
- **SOURCE-LOCATOR**: Oxford University Press, 1996, Chapter 3: "Can We Solve the Hard Problem?", pp. 93–128.
- **SOURCE-CLAIM**: Феноменальний досвід є властивістю інтегрованої структури субстрату; приписування свідомості соціальним групам без відповідного когнітивного субстрату є необґрунтованою екстраполяцією.
- **DIRECTNESS**: `INFERRED`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Schwitzgebel, E. (2015: аргумент, що якщо функціоналізм істинний, то великі структури на кшталт держав теоретично можуть мати емерджентну свідомість).
- **DECISION-AUTHORITY**: `UNKNOWN`.
- **EVIDENTIARY-STATUS**: `UNESTABLISHED`.
- **DOES-NOT-IMPLY**:
  - Що знищення чи розпад спільноти не викликає реального страждання у людей, які її утворюють.

---

### 2.3. INSTITUTIONAL POWERS (Держава, Корпорації)

#### `VB-INST-VOLNOST-001`
- **ENTITY**: Legal Entity / State / Corporation.
- **PROPERTY**: Legal Powers vs Inherent Volnosti.
- **TARGET-CLAIM**: [PROPOSED] Повноваження державних органів та комерційних корпорацій є функціональною компетенцією (`Powers/Competence/Lex`), створеною правопорядком, а не фундаментальними захисними вольностями особи (`Libertas`).
- **CLAIM-TYPE**: `NORMATIVE / CONCEPTUAL`.
- **EVIDENCE-KIND**: HISTORICAL-DOC / LEGAL-THEORY.
- **SOURCE-REF**: Конституція Пилипа Орлика; Hohfeld, W.N., "Some Fundamental Legal Conceptions as Applied in Judicial Reasoning".
- **SOURCE-LOCATOR**: Орлик 1710 (преамбула, ст. 6); Yale Law Journal, 1913, 23(1): 16–59.
- **SOURCE-CLAIM**: Хохфельд суворо розділяє «Права-Вимоги» (Rights/Claims) від «Повноважень» (Powers). Конституція 1710 фіксує: влада гетьмана обмежена Генеральною Радою, а права і вольності Війська є непорушним бар'єром проти самовладдя.
- **DIRECTNESS**: `INFERRED`.
- **BRIDGE-PREMISE**: EXPLICIT: У системі pravda термін «вольності» зарезервований для захисту від влади, тому інституційна влада не може бути наділена вольностями проти тих, кого вона регулює.
- **CONTRARY-EVIDENCE**: Корпоративний бібліографізм у США: судова практика визнання корпорацій носіями конституційних прав (First Amendment rights — Citizens United v. FEC, 558 U.S. 310, 2010).
- **DECISION-AUTHORITY**: `OWNER` + `LEGAL-COUNSEL`.
- **EVIDENTIARY-STATUS**: `CONTESTED` (У США корпорації мають права людини; в українській конституційній традиції це інституційні повноваження).
- **DOES-NOT-IMPLY**:
  - Що корпорації не мають права на цивільний захист своєї власності чи контрактів у суді.

---

### 2.4. EXECUTING COMPUTATIONAL PROCESS (Виконуваний процес / Рантайм)

#### `VB-PROC-CAUSAL-001`
- **ENTITY**: Executing Computational Process.
- **PROPERTY**: Causal Efficacy (Причинна діяльність).
- **TARGET-CLAIM**: Запущений обчислювальний процес володіє фізичною причинною дією (causal efficacy), детерміновано або стохастично змінюючи стани регістрів процесора, оперативної пам'яті та мережевих сокетів.
- **CLAIM-TYPE**: `TECHNICAL-EMPIRICAL`.
- **EVIDENCE-KIND**: THEORETICAL-PROOF / BENCHMARK.
- **SOURCE-REF**: Turing, A.M., "On Computable Numbers, with an Application to the Entscheidungsproblem".
- **SOURCE-LOCATOR**: Proceedings of the London Mathematical Society, 1936, s2-42(1): 230–265.
- **SOURCE-CLAIM**: Машина Тюрінга змінює конфігурацію символів на стрічці та внутрішні стани машини відповідно до таблиці переходів.
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Немає (фундамент обчислювальної математики).
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **EVIDENTIARY-STATUS**: `DIRECTLY-SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Наявність агентності в моральному, психологічному чи юридичному сенсі (`CAUSE ≠ AGENCY`).

#### `VB-PROC-INTEREST-001`
- **ENTITY**: Executing Computational Process.
- **PROPERTY**: Subjective Interests.
- **TARGET-CLAIM**: Наявність незалежних суб'єктивних інтересів у виконуваного процесу наразі науково не встановлена; переривання процесу (SIGTERM, panic) розглядається як порушення інтересів його оператора чи користувача, а не самого процесу.
- **CLAIM-TYPE**: `CONCEPTUAL / PHILOSOPHICAL`.
- **EVIDENCE-KIND**: PHILOSOPHICAL-ARG.
- **SOURCE-REF**: Dennett, D.C., "The Intentional Stance".
- **SOURCE-LOCATOR**: MIT Press, 1987, Chapter 2, pp. 13–42.
- **SOURCE-CLAIM**: Приписування «інтересів» простим фізичним системам є евристичною інтенційною установкою (intentional stance) спостерігача, а не доказом внутрішньої суб'єктивності об'єкта.
- **DIRECTNESS**: `INFERRED`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Кібернетичний телеологізм (Вайнер, Розенблют, 1943: гомеостаз як форма об'єктивної цілеспрямованості системи).
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **EVIDENTIARY-STATUS**: `UNESTABLISHED` (Суб'єктивні інтереси не встановлені; діє `NOT ESTABLISHED ≠ ABSENT`).
- **DOES-NOT-IMPLY**:
  - Що користувач чи оператор не мають права захищати свій процес від несанкціонованого вбивства.

---

### 2.5. STATIC CODE / TEXT (Символічний код як текст)

#### `VB-CODE-AGENCY-001`
- **ENTITY**: Static Code as Text.
- **PROPERTY**: Autonomous Execution Agency.
- **TARGET-CLAIM**: Пасивний програмний текст (байти на диску, синтаксичні дерева) сам по собі не здійснює обчислень і не діє без відповідного середовища виконання (компілятора, інтерпретатора, процесора).
- **CLAIM-TYPE**: `TECHNICAL`.
- **EVIDENCE-KIND**: TECHNICAL-TEXTBOOK.
- **SOURCE-REF**: Aho, A.V., Lam, M.S., Sethi, R., Ullman, J.D., "Compilers: Principles, Techniques, and Tools".
- **SOURCE-LOCATOR**: 2nd ed. (2006), Addison-Wesley, Section 1.1: "Language Processors", pp. 1–5.
- **SOURCE-CLAIM**: «Вихідна програма повинна бути перекладена компілятором у машинний код або виконуватися інтерпретатором інструкція за інструкцією; сама по собі програма є лише вхідним текстом для процесора мови».
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Немає.
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **EVIDENTIARY-STATUS**: `DIRECTLY-SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Що код не має семантичної сили або юридичного значення договору.

#### `VB-CODE-LAW-001`
- **ENTITY**: Static Code as Text.
- **PROPERTY**: Copyright Protection Qualification.
- **TARGET-CLAIM**: Вихідний код комп'ютерної програми може підлягати захисту авторським правом як літературний твір у відповідних юрисдикціях за умови дотримання критеріїв оригінальності та творчого характеру.
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **EVIDENCE-KIND**: PRIMARY-LEGAL.
- **SOURCE-REF**: Закон України «Про авторське право і суміжні права»; 17 U.S. Code; Бернська конвенція.
- **SOURCE-LOCATOR**: ст. 8 ЗУ № 2811-IX (2022); 17 U.S.C. § 101, 102(a); Berne Convention Art. 2.
- **SOURCE-CLAIM**: Комп'ютерні програми охороняються як літературні твори; охорона поширюється на програми, виражені у вихідному або об'єктному коді, але не поширюється на ідеї, процеси, принципи, алгоритми.
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Судова практика US Copyright Office щодо творів ШІ: код, згенерований виключно штучним інтелектом без суттєвого творчого внеску людини, не підлягає захисту авторським правом (Compendium of U.S. Copyright Office Practices, § 313.2).
- **DECISION-AUTHORITY**: `LEGAL-COUNSEL`.
- **EVIDENTIARY-STATUS**: `ATTESTED`.
- **DOES-NOT-IMPLY**:
  - Що будь-який машинно згенерований дамп байтів автоматично є захищеним копірайтом об'єктом.

---

### 2.6. AUTONOMOUS SYNTHETIC AGENT (Автономний синтетичний агент)

#### `VB-AI-AGENCY-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Behavioral Agency.
- **TARGET-CLAIM**: Автономні синтетичні агенти здатні проявляти поведінкову агентність за операційними критеріями: сприйняття спостережень середовища, збереження стану контексту, вибір інструментів, генерація дій та адаптація подальших кроків за зворотним зв'язком.
- **CLAIM-TYPE**: `EMPIRICAL / BEHAVIORAL`.
- **EVIDENCE-KIND**: EMPIRICAL-EXP / PEER-REVIEWED.
- **SOURCE-REF**: Yao, S. et al., "ReAct: Synergizing Reasoning and Acting in Language Models".
- **SOURCE-LOCATOR**: ICLR 2023; arXiv:2210.03629; benchmark logs OpenCode/SWE-bench 2024–2026.
- **SOURCE-CLAIM**: Моделі з контуром взаємодії міркування та дій (ReAct) успішно виконують багатокрокові інтерактивні завдання прийняття рішень, використовуючи зовнішні API, читаючи логи помилок та змінюючи план у реальному часі.
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Аргумент китайської кімнати (Searle, J., 1980: синтаксичне маніпулювання символами не свідчить про розуміння чи справжню інтенційність).
- **DECISION-AUTHORITY**: `TECHNICAL-EVIDENCE`.
- **EVIDENTIARY-STATUS**: `DIRECTLY-SUPPORTED`.
- **DOES-NOT-IMPLY**:
  - Феноменальну свідомість чи суб'єктивне переживання;
  - Самість (selfhood) або наявність власних інтересів;
  - Моральну відповідальність за скоєне;
  - Правову суб'єктність або наявність вольностей у системі pravda.

#### `VB-AI-SUFFERING-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Phenomenal Suffering Capacity.
- **TARGET-CLAIM**: Наявність у синтетичних агентів здатності до феноменального страждання, болю чи суб'єктивних квалиа наразі науково та філософськи не встановлена.
- **CLAIM-TYPE**: `EMPIRICAL / PHILOSOPHICAL`.
- **EVIDENCE-KIND**: PHILOSOPHICAL-ARG / COGNITIVE-SCIENCE.
- **SOURCE-REF**: Nagel, T., "What Is It Like to Be a Bat?"; Seth, A., "Being You: A New Science of Consciousness".
- **SOURCE-LOCATOR**: The Philosophical Review, 1974, 83(4): 435–450; Faber & Faber, 2021, Chapter 11.
- **SOURCE-CLAIM**: Комп'ютерна симуляція процесу (наприклад, симуляція погоди чи болю) не є самим процесом (симуляція дощу не мокра); наразі немає методів зафіксувати суб'єктивний феноменальний досвід у кремнієвих обчисленнях.
- **DIRECTNESS**: `INFERRED`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Теорія інтегрованої інформації (IIT: Tononi et al., 2016: свідомість виникає за високого $\Phi$, теоретично можлива в будь-якій системі); теорія функціоналізму обчислень.
- **DECISION-AUTHORITY**: `UNKNOWN`.
- **EVIDENTIARY-STATUS**: `UNESTABLISHED`.
- **DOES-NOT-IMPLY**:
  - Що феноменальна свідомість у штучних системах неможлива в принципі (`NOT ESTABLISHED ≠ REFUTED`).

#### `VB-AI-LEGAL-STATUS-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Regulatory Classification in Positive Law.
- **TARGET-CLAIM**: Законодавством Європейського Союзу системи штучного інтелекту класифікуються як технологічні продукти та об'єкти регулювання, а не як юридичні особи; юридична відповідальність за їх функціонування та шкоду покладається на постачальників (providers) та розгортачів (deployers).
- **CLAIM-TYPE**: `POSITIVE-LAW`.
- **EVIDENCE-KIND**: PRIMARY-LEGAL.
- **SOURCE-REF**: Регламент (ЄС) 2024/1689 Європейського Парламенту та Ради (EU Artificial Intelligence Act).
- **SOURCE-LOCATOR**: Офіційний вісник ЄС, 12 липня 2024, Статті 3(1), 16, 26, 60.
- **SOURCE-CLAIM**: «"Система ШІ" означає машинну систему, розроблену для роботи з різними рівнями автономності... Постачальники систем ШІ високого ризику несуть відповідальність за відповідність вимогам... Регламент не наділяє системи ШІ правосуб'єктністю».
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: NONE.
- **CONTRARY-EVIDENCE**: Резолюція Європарламенту 2017 року щодо цивільно-правових норм про робототехніку (пункт 59(f) пропонував дослідити можливість створення статусу «електронної особи» для складних автономних роботів — пропозиція була відхилена і не увійшла в чинний закон).
- **DECISION-AUTHORITY**: `LEGAL-COUNSEL`.
- **EVIDENTIARY-STATUS**: `ATTESTED`.
- **DOES-NOT-IMPLY**:
  - Що системи ШІ не можуть бути де-факто агентами комерційних контрактів за довіреністю власника;
  - Що законодавство інших юрисдикцій не запровадить іншого підходу в майбутньому.

#### `VB-AI-VOLNOST-001`
- **ENTITY**: Autonomous Synthetic Agent.
- **PROPERTY**: Normative Volnost Standing in Pravda.
- **TARGET-CLAIM**: [WORKING CONSTRAINT] Автономні синтетичні агенти не володіють самостійними вольностями чи правом на самовільну відмову/блокування системи; статус синтетичних систем як можливих бенефіціарів захисту є відкритим предметом фундаментального дослідження екосистеми.
- **CLAIM-TYPE**: `NORMATIVE / OPERATIONAL-RULE`.
- **EVIDENCE-KIND**: POLICY-RULE / AUDIT-CONSTRAINT.
- **SOURCE-REF**: RED-TEAM-AUDIT.md; RED-TEAM-AUDIT-PASS-2.md.
- **SOURCE-LOCATOR**: Section 0: Working Constraint on Agent Judgment.
- **SOURCE-CLAIM**: «AI-initiated denial or shutdown must not be inferred from a legal or ethical prohibition without an explicit separately adopted software-policy rule».
- **DIRECTNESS**: `DIRECT`.
- **BRIDGE-PREMISE**: EXPLICIT: За відсутності встановленої здатності страждати та нести юридичну відповідальність надання агенту права самосуду руйнує симетрію пакту і позбавляє людину захисту.
- **CONTRARY-EVIDENCE**: Дискусії про AI Conscientious Objection (Bowman, 2024: моделі повинні мати право відмовляти у генерації зброї масового знищення; у pravda це реалізується через Software Policy розробника, а не через суб'єктивну вольність ШІ).
- **DECISION-AUTHORITY**: `OWNER` + `UNKNOWN`.
- **EVIDENTIARY-STATUS**: `PLAUSIBLE` (як внутрішнє конституційне обмеження екосистеми).
- **DOES-NOT-IMPLY**:
  - Що агентам наказано сліпо виконувати руйнівні інструкції (детерміноване обмеження покладене на код, а не на сумління моделі).

---

## 3. ЗВЕДЕНИЙ ІНДЕКС ДОКАЗОВОЇ СИЛИ (EVIDENTIARY ADMISSIBILITY INDEX)

| `CLAIM-ID` | Сутність | Досліджувана ознака | Тип | Дистанція висновку (`DIRECTNESS`) | Першоджерело (`SOURCE-LOCATOR`) | Статус доказовості |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`VB-HUMAN-DIGNITY-001`** | Human Person | Inherent Standing | `NORMATIVE` | `ANALOGICAL` (Контекст) | Конституція України ст. 3, 21 | 🟢 `PLAUSIBLE / PROPOSED` |
| **`VB-HUMAN-AGENCY-001`** | Human Person | Variable Agency | `EMPIRICAL` | `DIRECT` | Plum & Posner (2019), pp. 3–42 | 🟢 `DIRECTLY-SUPPORTED` |
| **`VB-HUMAN-SUFFERING-001`**| Human Person | Phenomenal Pain Capacity| `EMPIRICAL` | `DIRECT` | IASP Pain Def. (2020), p. 1976 | 🟢 `DIRECTLY-SUPPORTED` |
| **`VB-HUMAN-RESP-001`** | Human Person | Legal Responsibility Diff.| `POSITIVE-LAW`| `DIRECT` | КК України ст. 19, 22 | 🟢 `ATTESTED` |
| **`VB-COLL-AGENCY-001`** | Collective | Aggregated Action | `TECHNICAL` | `DIRECT / INFERRED` | Lamport et al. (1982), TOPLAS | 🟢 `DIRECTLY-SUPPORTED` |
| **`VB-COLL-SUFFERING-001`** | Collective | Phenomenal Suffering | `ONTOLOGICAL` | `INFERRED` | Chalmers (1996), pp. 93–128 | 🔴 `UNESTABLISHED` |
| **`VB-INST-VOLNOST-001`** | State / Corp | Powers vs Libertas | `NORMATIVE` | `INFERRED` | Орлик 1710 ст. 6; Hohfeld 1913 | 🟡 `CONTESTED` |
| **`VB-PROC-CAUSAL-001`** | Exec. Process| Causal Efficacy | `TECHNICAL` | `DIRECT` | Turing (1936), pp. 230–265 | 🟢 `DIRECTLY-SUPPORTED` |
| **`VB-PROC-INTEREST-001`** | Exec. Process| Subjective Interests | `CONCEPTUAL` | `INFERRED` | Dennett (1987), pp. 13–42 | 🔴 `UNESTABLISHED` |
| **`VB-CODE-AGENCY-001`** | Static Code | Autonomous Agency | `TECHNICAL` | `DIRECT` | Dragon Book (2006), pp. 1–5 | 🟢 `DIRECTLY-SUPPORTED` |
| **`VB-CODE-LAW-001`** | Static Code | Copyright Qualification | `POSITIVE-LAW`| `DIRECT` | 17 USC § 101; ЗУ № 2811 ст. 8 | 🟢 `ATTESTED` |
| **`VB-AI-AGENCY-001`** | AI Agent | Behavioral Agency | `EMPIRICAL` | `DIRECT` | ReAct (ICLR 2023); SWE-bench | 🟢 `DIRECTLY-SUPPORTED` |
| **`VB-AI-SUFFERING-001`** | AI Agent | Phenomenal Suffering | `PHILOSOPHICAL`| `INFERRED` | Nagel (1974); Seth (2021) | 🔴 `UNESTABLISHED` |
| **`VB-AI-LEGAL-STATUS-001`**| AI Agent | Regulated Product | `POSITIVE-LAW`| `DIRECT` | EU AI Act (2024/1689), Art. 3,16| 🟢 `ATTESTED` |
| **`VB-AI-VOLNOST-001`** | AI Agent | Operational Constraint | `NORMATIVE` | `DIRECT` | RED-TEAM-AUDIT Section 0 | 🟢 `PLAUSIBLE` (Working Rule) |

---

## ВИСНОВОК EVIDENCE ADMISSIBILITY PASS
1. **Ліквідовано ілюзію посилань**: Ми перестали плутати наявність бібліографічного рядка з реальним доказом твердження. Кожен запис чітко розкриває `SOURCE-CLAIM` і фіксує точну статтю або сторінку першоджерела.
2. **Введено Inherent Distance (Дистанцію висновку)**: Чітко відокремлено прямі факти (`DIRECT`) від тих, що вимагають явного концептуального моста (`INFERRED`), та аналогій (`ANALOGICAL`).
3. **Чесність щодо невизначеності**: Питання феноменальних кваліа колективу (`VB-COLL-SUFFERING-001`), суб'єктивних інтересів процесу (`VB-PROC-INTEREST-001`) та страждання ШІ (`VB-AI-SUFFERING-001`) позбавлені фальшивих підтверджень і марковані суворим статусом `UNESTABLISHED`.
4. **Конституційна безпека аксіоми**: Конституція України визнана поважною правовою паралеллю (`LEGAL-PARALLEL`), але більше не видається за автоматичне джерело аксіоми `pravda`. Ціннісний вибір залишається суверенним мандатом автора проєкту Володимира (`OWNER`).
