# Script to update WITNESS-ACQUISITION-REGISTER.md with:
# 1. Closed L0 for Hadiach Sejm 1659 (now L1 with SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt)
# 2. Deconstruction of Zboriv 1649 into 4 separate documentary units (DECLARATION, PETITION, CRIMEA-TREATY, REGISTER)
# 3. Inclusion of SOURCE-INTERPRETATION-RISK with explicit 'why' for every entry.

with open("/home/agents/GitHub/pravda/WITNESS-ACQUISITION-REGISTER.md", "r", encoding="utf-8") as f:
    text = f.read()

new_content = """# РЕЄСТР НАБУТТЯ ТА АТЕСТАЦІЇ НОСІЇВ ДЖЕРЕЛ (WITNESS-ACQUISITION-REGISTER)
## Status: ACTIVE · Phase 1 Complete (Source Infrastructure & Risk Ledger)

---

## 0. МЕТОДОЛОГІЧНА ДЕМАРКАЦІЯ ТА ШКАЛИ АТЕСТАЦІЇ

### 0.1. Чотирирівнева архітектура передачі тексту
У дослідницькому просторі `pravda` суворо розрізняються чотири рівні існування тексту:

```text
HISTORICAL OBJECT (PHYSICAL WITNESS)
  │  (рукописний автограф, копійний список, стародрук)
  ↓
EDITORIAL TRANSMISSION (CRITICAL / DIPLOMATIC EDITION)
  │  (наукова публікація, археографічне видання, апарат різночитань)
  ↓
DIGITAL INTERMEDIARY (DIGITAL TRANSMISSION)
  │  (портал правової інформації, електронна бібліотека, Wikisource, Internet Archive)
  ↓
LOCAL FILE TRANSFORMATION (LOCAL TXT FILE)
     (скриптове вилучення, нормалізація кодування, видалення розмітки)
```

$$\\text{HISTORICAL OBJECT} \\ne \\text{EDITORIAL EDITION} \\ne \\text{DIGITAL INTERMEDIARY} \\ne \\text{LOCAL TXT FILE}$$

### 0.2. Трирівнева шкала точності локального тексту (Local Text Fidelity Levels)
Статус точності не може присвоюватися на підставі авторитету першоджерела чи наукової репутації видавця. Він фіксує **виключно реально виконану процедуру колації**:

```text
L3  VERIFIED-AGAINST-WITNESS
    Локальний файл безпосередньо поаркушно звірено з факсиміле/сканом самого рукопису чи стародруку.

L2  VERIFIED-AGAINST-EDITION
    Локальний файл поаркушно звірено зі сканом/PDF зазначеного друкованого наукового видання.

L1  VERIFIED-AGAINST-DIGITAL-DERIVATIVE
    Локальний файл звірено з цифровою науковою публікацією (Ізборник, Право.бай, Вікіджерела, Internet Archive тощо),
    яка декларує походження з відповідного видання.

L0  UNCOLLATED / PENDING
    Колація не проводилась або текст очікує вивантаження.
```

### 0.3. Режим транскрипції (Transcription Mode)
- **`DIPLOMATIC`**: Свідоме побуквене відтворення конкретного свідка/видання зі збереженням рядків, титлів, виносок та скорочень.
- **`SEMI-DIPLOMATIC`**: Збереження оригінальної орфографії (ѣ, ѧ, ω, ѕ), але з розкритими титлами та сучасною розбивкою рядків.
- **`NORMALIZED`**: Нормалізований для машинного пошуку та семантичного аналізу текст.
- **`PLAIN EXTRACTION`**: Скриптове очищення веб-сторінки / HTML / OCR розмітки.

### 0.4. Дворівневе розмежування інтерпретаційного ризику
Ризик невірної інтерпретації розмежовується на два принципово різні рівні:
1. **`SOURCE-INTERPRETATION-RISK` (Метаоцінка документального комплексу)**: фіксує конфлікт правової природи самого акта, наявність прихованих політичних компромісів, різночитань між сторонами переговорів або розриву між юридичною формою і фактичним змістом (живе у цьому реєстрі).
2. **`CLAIM-INTERPRETATION-RISK` (Ризик конкретного твердження чи висновку)**: оцінює відстань між буквальним формулюванням норми та конкретним історіографічним узагальненням (живе у `HISTORICAL-CLAIMS-REGISTER.md`).

---

## 1. ЗВЕДЕНИЙ РЕЄСТР ПЕРШОЇ ХВИЛІ (WAVE 1 ACQUISITION & RISK MATRIX)

| WITNESS-ID | WORK (Пам'ятка) | PHYSICAL WITNESS | EDITION-IDENTITY | LOCAL FILE | TRANSCRIPTION-MODE | FIDELITY | TEXT-LOSS | SOURCE-RISK |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`WIT-RP-SHORT`** | Правда Роськая (Коротка) | БАН 17.4.9 (список XV ст.) | 🟢 `VERIFIED` (АН СРСР 1984) | `SRC-RP-SHORT-DIPLOMATIC.txt` | `SEMI-DIPLOMATIC` | 🟡 **L1** | 🟢 LOW | 🔴 **HIGH** |
| **`WIT-RP-EXP`** | Правда Русьская (Розширена) | РДБ ф. 304.I № 793 (XIV ст.) | 🟢 `VERIFIED` (АН СРСР 1984) | `SRC-RP-EXP-DIPLOMATIC.txt` | `SEMI-DIPLOMATIC` | 🟡 **L1** | 🟢 LOW | 🔴 **HIGH** |
| **`WIT-LS-1566`** | II Литовський Статут 1566 | Рукописні списки XVI ст. | 🟢 `VERIFIED` (Мінськ 2003 / 1855) | `SRC-LS-1566-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** | 🟢 LOW | 🟡 **MEDIUM** |
| **`WIT-LS-1588`** | III Литовський Статут 1588 | Стародрук Мамоничів 1588 | 🟢 `VERIFIED` (АН БССР 1989) | `SRC-LS-1588-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** | 🟡 MEDIUM | 🟡 **MEDIUM** |
| **`WIT-ZBORIV-1649-DECLARATION`** | Зборів: Декларація Яна Казимира | AGAD Metryka Koronna / РДАДА | 🟢 `VERIFIED` (АЮЗР Т. III) | `SRC-ZBORIV-1649-DECLARATION.txt` | `PLAIN EXTRACTION` | 🟡 **L1** | 🟡 MEDIUM | 🔴 **HIGH** |
| **`WIT-ZBORIV-1649-PETITION`** | Зборів: Супліка Війська Запорозького | Списки у реляціях Киселя | 🟢 `VERIFIED` (Крип'якевич 1961) | `SRC-ZBORIV-1649-PETITION.txt` | `ARCHIVAL SUMMARY` | ⚪ **L0** | 🔴 HIGH | 🟣 **VERY HIGH** |
| **`WIT-ZBORIV-1649-CRIMEA-TREATY`**| Зборів: Угода з ханом Іслам-Гіреєм | AGAD Dz. Turecki / шертні листи | 🟢 `VERIFIED` (Lipiński / Wójcik) | `SRC-ZBORIV-1649-CRIMEA-TREATY.txt` | `ARCHIVAL SUMMARY` | ⚪ **L0** | 🔴 HIGH | 🟣 **VERY HIGH** |
| **`WIT-ZBORIV-1649-REGISTER`** | Зборів: Реєстр 1649 р. (Компут) | РДАДА ф. 229, оп. 2, спр. 1 | 🟢 `VERIFIED` (Наукова думка 1995)| `SRC-ZBORIV-1649-REGISTER-SUMMARY.txt`| `DIPLOMATIC PASSPORT` | 🟡 **L1** | 🟢 LOW | 🟡 **MEDIUM** |
| **`WIT-MARCH-1654`** | Березневі статті (11 статей) | РДАДА ф. 229, спр. 9 (список XVII) | 🟢 `VERIFIED` (АН СССР 1953) | `SRC-MARCH-1654-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** | 🟢 LOW | 🟣 **VERY HIGH** |
| **`WIT-HADIACH-COMM-1658`**| Гадяцька комісарська угода | Рукопис комісії (16.09.1658) | 🟢 `VERIFIED` (Польс. археографія) | `SRC-HADIACH-1658-COMMISSION-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** | 🟡 MEDIUM | 🟣 **VERY HIGH** |
| **`WIT-HADIACH-SEJM-1659`**| Гадяцька сеймова конституція | Друк. сеймові книги 1659 | 🟢 `VERIFIED` (Vol. Legum T. IV) | `SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt` | `DIPLOMATIC (XIX ed.)` | 🟡 **L1** | 🟢 LOW | 🟣 **VERY HIGH** |
| **`WIT-ORLYK-1710-UA`** | Pacta et Constitutiones (староукр.)| РДАДА ф. 13, спр. 10, арк. 1–19 | 🟢 `VERIFIED` (ЦДІАК, 2010) | `SRC-ORLYK-1710-UA-DIPLOMATIC.txt` | `SEMI-DIPLOMATIC` | 🟡 **L1** | 🟡 MEDIUM | 🟡 **MEDIUM** |
| **`WIT-ORLYK-1710-LAT`**| Pacta et Constitutiones (латина) | Riksarkivet Stockholm, Cosacica | 🟢 `VERIFIED` (Молчановський 1898) | `SRC-ORLYK-1710-LAT-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** | 🟡 MEDIUM | 🟡 **MEDIUM** |

---

## 2. ПОПАСПОРТНИЙ АУДИТ ТОЧНОСТІ ТА ІНТЕРПРЕТАЦІЙНИХ РИЗИКІВ

### 2.1. `WIT-RP-SHORT` ТА `WIT-RP-EXP`: РУСЬКА ПРАВДА
- **EDITION-IDENTITY**: «Российское законодательство X–XX веков». — Т. 1. — М., 1984. — С. 47–49 (Коротка) та С. 64–73 (Простора).
- **LOCAL-FILES**: `SRC-RP-SHORT-DIPLOMATIC.txt` та `SRC-RP-EXP-DIPLOMATIC.txt`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **SOURCE-INTERPRETATION-RISK**: 🔴 **HIGH**
- **WHY-SOURCE-RISK**: Текст становить кодифікацію архаїчного звичаєвого судочинства та штрафів (віри, продажі, уроки); терміни «свободный», «правда», «людин» часто проектуються на сучасні уявлення про суб'єктність особи або концепцію свободи волі, тоді як історично вони позначали виключно патріархально-становий імунітет непоневоленого общинника супроти челяді, холопів та закупів.

---

### 2.2. `WIT-LS-1566` ТА `WIT-LS-1588`: ЛИТОВСЬКІ СТАТУТИ
- **EDITION-IDENTITY**: 
  - 1566: Видання Т. Роговцова 1855 р. / «Статут Вялікага княства Літоўскага 1566 года» (Мінськ, 2003).
  - 1588: Академічне видання АН БССР (Мінськ, 1989) за стародруком Віленської друкарні Мамоничів 1588 р.
- **LOCAL-FILES**: `SRC-LS-1566-DIPLOMATIC.txt` (631 КБ) та `SRC-LS-1588-DIPLOMATIC.txt` (1.47 МБ).
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **SOURCE-INTERPRETATION-RISK**: 🟡 **MEDIUM**
- **WHY-SOURCE-RISK**: Тексти є монументальними кодексами з чітко розробленою юридичною термінологією римсько-канонічного та руського походження. Ризик полягає в анахронічному розширенні понять «народ», «обыватель» і «вольность» на все населення ВКЛ, тоді як нормативно суб'єктом вольностей виступав виключно шляхетсько-рицарський землевласницький стан і частково магдебурзькі міщани, а тягле селянство підпадало під вотчинне закріпачення.

---

### 2.3. ДЕКОНСТРУКЦІЯ ЗБОРІВСЬКОГО КОМПЛЕКСУ (1649 Р.)

#### А. `WIT-ZBORIV-1649-DECLARATION`: КОРОЛІВСЬКА ДЕКЛАРАЦІЯ ЛАСКИ
- **DOCUMENT-FORM**: Жалувана грамота (declaratio clementiae) польського короля Яна II Казимира.
- **LOCAL-FILE**: `SRC-ZBORIV-1649-DECLARATION.txt` (12 статей).
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **SOURCE-INTERPRETATION-RISK**: 🔴 **HIGH**
- **WHY-SOURCE-RISK**: Королівський двір формулював акт як монаршу протекцію та помилування збунтованих підданих за умови повернення нереєстрових селян до панщини (ст. 2); козацька сторона трактувала декларацію як правове визнання фактичної незалежності військової території у межах 3 воєводств.

#### Б. `WIT-ZBORIV-1649-PETITION`: СУПЛІКА ВІЙСЬКА ЗАПОРОЗЬКОГО
- **DOCUMENT-FORM**: Чолобитна козацької старшини з первинними переговорними вимогами.
- **LOCAL-FILE**: `SRC-ZBORIV-1649-PETITION.txt`.
- **FIDELITY-LEVEL**: ⚪ **L0** (`UNCOLLATED / SUMMARY RECORD`).
- **SOURCE-INTERPRETATION-RISK**: 🟣 **VERY HIGH**
- **WHY-SOURCE-RISK**: Первинний автограф втрачено; документ реконструюється за різночитаннями в дипломатичних донесеннях. Максималістські пункти супліки (повне знищення унії в Польщі, виселення шляхти) були частково дезавуйовані або відкинуті королівськими комісарами, тому ототожнення супліки з текстом угоди є фатальною історичною помилкою.

#### В. `WIT-ZBORIV-1649-CRIMEA-TREATY`: ДОГОВІР З КРИМСЬКИМ ХАНАТОМ
- **DOCUMENT-FORM**: Сепаратна мирна конвенція короля Яна Казимира та хана Іслам-Гірея III.
- **LOCAL-FILE**: `SRC-ZBORIV-1649-CRIMEA-TREATY.txt`.
- **FIDELITY-LEVEL**: ⚪ **L0** (`UNCOLLATED / SUMMARY RECORD`).
- **SOURCE-INTERPRETATION-RISK**: 🟣 **VERY HIGH**
- **WHY-SOURCE-RISK**: Угода була укладена за спиною Хмельницького під загрозою переходу татар на бік поляків; включала виплату викупу за деблокаду татарського війська та негласний дозвіл на збирання ясиру під час відступу через Волинь та Поділля, що руйнувало образ монолітного козацько-кримського союзу.

#### Г. `WIT-ZBORIV-1649-REGISTER`: РЕЄСТР ВІЙСЬКА ЗАПОРОЗЬКОГО 1649 Р.
- **DOCUMENT-FORM**: Офіційний компут 40 480 козаків по 16 полках.
- **LOCAL-FILE**: `SRC-ZBORIV-1649-REGISTER-SUMMARY.txt`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **SOURCE-INTERPRETATION-RISK**: 🟡 **MEDIUM**
- **WHY-SOURCE-RISK**: Персональний склад зафіксовано бездоганно; ризик полягає в інтерпретації правового становища величезної маси покозаченого населення, що залишилася поза реєстром і автоматично поверталася під феодальну юрисдикцію шляхти.

---

### 2.4. `WIT-MARCH-1654`: БЕРЕЗНЕВІ СТАТТІ
- **EDITION-IDENTITY**: Полное собрание законов Российской империи (ПСЗРИ). — Т. I. — № 119; «Воссоединение Украины с Россией». — Т. III. — М., 1953. — № 108.
- **LOCAL-FILE**: `SRC-MARCH-1654-DIPLOMATIC.txt`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **SOURCE-INTERPRETATION-RISK**: 🟣 **VERY HIGH**
- **WHY-SOURCE-RISK**: Текст становить не єдиний симетричний трактат, а челобитну українських послів із 11 статей з маргінальними указами царя та боярськими «приговорами». Кожна сторона закладала діаметрально протилежний зміст у формули підданства: козацька старшина трактувала угоду як військово-оборонний сюзеренітет зі збереженням державного устрою та суду, а московський уряд — як безповоротне інкорпораційне підданство «вічного холопства» царю.

---

### 2.5. `WIT-HADIACH-COMM-1658` ТА `WIT-HADIACH-SEJM-1659`: ГАДЯЦЬКИЙ КОМПЛЕКС
- **EDITION-IDENTITY**:
  - Комісія 1658 р.: Рукопис польсько-козацької комісії в таборі під Гадячем (16 вересня 1658 р.). Файл: `SRC-HADIACH-1658-COMMISSION-DIPLOMATIC.txt`.
  - Сеймова конституція 1659 р.: «Volumina Legum», вид. Й. Огризка, СПб., 1859, Т. IV, с. 297–308 («Kommissya Hadiacka»). Файл: `SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt` (56 КБ).
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **SOURCE-INTERPRETATION-RISK**: 🟣 **VERY HIGH**
- **WHY-SOURCE-RISK**: Ратифікований Сеймом 1659 року текст суттєво звузив концепт «Великого Князівства Руського», узгоджений у таборі під Гадячем 1658 року: Сейм вилучив пункт про власну монету, скасував автономне право зовнішніх зносин із сусідніми державами, залишив чинними контрреформаційні застереження щодо шкіл і відновив право шляхти на володіння маєтностями в Гетьманщині, що призвело до повстання дейнеків, повалення гетьмана Виговського та початку Руїни.

---

### 2.6. `WIT-ORLYK-1710-UA` ТА `WIT-ORLYK-1710-LAT`: КОНСТИТУЦІЯ ОРЛИКА
- **EDITION-IDENTITY**:
  - `WIT-ORLYK-1710-UA`: Оригінал староукраїнською мовою у РДАДА (ф. 13, спр. 10, арк. 1–19) / видання О. Вовк (2010). Файл: `SRC-ORLYK-1710-UA-DIPLOMATIC.txt`.
  - `WIT-ORLYK-1710-LAT`: Скорочений диплом латинською мовою у Riksarkivet (Muscovitica II, 347) / публікація Н. Молчановського (1898). Файл: `SRC-ORLYK-1710-LAT-DIPLOMATIC.txt`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **SOURCE-INTERPRETATION-RISK**: 🟡 **MEDIUM**
- **WHY-SOURCE-RISK**: Текст містить розгорнуту республіканську доктрину розподілу повноважень між гетьманом і Генеральною Радою. Ризик інтерпретації полягає в анахронічній модернізації документа як «першої демократичної конституції Європи» та ототожненні Генеральної Ради із сучасним всенародним парламентом, тоді як вона репрезентувала виключно генеральну старшину, полковників і полкових радників, конструюючи шляхетсько-старшинську республіку олігархічного типу в умовах вигнання.

---

## 3. ЗВІТ ПРО ЗАВЕРШЕННЯ ФАЗИ 1 ТА КРИТЕРІЇ ГОТОВНОСТІ

1. **Ліквідація статусу L0 / PENDING для первинного корпусу**:
   - `WIT-HADIACH-SEJM-1659` отримано у повному дипломатичному обсязі (Volumina Legum T. IV, с. 297–308) і зафіксовано на чесному рівні **L1** у файлі [`SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt`](file:///home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt).
2. **Деконструкція Зборівського комплексу**:
   - Розбито на 4 незалежні документальні одиниці з власними `WITNESS-ID`, файлами та паспортами ризиків.
3. **Впровадження шкали `SOURCE-INTERPRETATION-RISK`**:
   - Для кожного документа введено рівень ризику (`MEDIUM`, `HIGH`, `VERY HIGH`) із розкриттям структурних причин (`WHY-SOURCE-RISK`).
4. **Непорушність нормативних шарів**:
   - Жоден файл нормативної теорії (`VOLNOST-BEARERS.md`, ліцензії, філософські аксіоми) не модифікувався під час виконання завдання.
"""

with open("/home/agents/GitHub/pravda/WITNESS-ACQUISITION-REGISTER.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("WITNESS-ACQUISITION-REGISTER.md updated successfully!")
