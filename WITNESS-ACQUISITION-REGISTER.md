# РЕЄСТР НАБУТТЯ ТА АТЕСТАЦІЇ НОСІЇВ ДЖЕРЕЛ (WITNESS-ACQUISITION-REGISTER)
## Status: ACTIVE · First Wave: 10 Corpora · Pass: Fidelity Level Audit (Three-Tier Scale)

---

## 0. МЕТОДОЛОГІЧНА ДЕМАРКАЦІЯ ТА ШКАЛА FIDELITY

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
  │  (портал правової інформації, електронна бібліотека, Wikisource)
  ↓
LOCAL FILE TRANSFORMATION (LOCAL TXT FILE)
     (скриптове вилучення, нормалізація кодування, видалення розмітки)
```

$$\text{HISTORICAL OBJECT} \ne \text{EDITORIAL EDITION} \ne \text{DIGITAL INTERMEDIARY} \ne \text{LOCAL TXT FILE}$$

### 0.2. Трирівнева шкала точності локального тексту (Local Text Fidelity Levels)
Статус точності не може присвоюватися на підставі авторитету першоджерела чи наукової репутації видавця. Він фіксує **виключно реально виконану процедуру колації**:

```text
L3  VERIFIED-AGAINST-WITNESS
    Локальний файл безпосередньо поаркушно звірено з факсиміле/сканом самого рукопису чи стародруку.

L2  VERIFIED-AGAINST-EDITION
    Локальний файл поаркушно звірено зі сканом/PDF зазначеного друкованого наукового видання.

L1  VERIFIED-AGAINST-DIGITAL-DERIVATIVE
    Локальний файл звірено з цифровою науковою публікацією (Ізборник, Право.бай, Вікіджерела тощо),
    яка декларує походження з відповідного видання.

L0  UNCOLLATED / PENDING
    Колація не проводилась або текст очікує вивантаження.
```

### 0.3. Режим транскрипції (Transcription Mode)
- **`DIPLOMATIC`**: Свідоме побуквене відтворення конкретного свідка/видання зі збереженням рядків, титлів, виносок та скорочень.
- **`SEMI-DIPLOMATIC`**: Збереження оригінальної орфографії (ѣ, ѧ, ω, ѕ), але з розкритими титлами та сучасною розбивкою рядків.
- **`NORMALIZED`**: Нормалізований для машинного пошуку та семантичного аналізу текст.
- **`PLAIN EXTRACTION`**: Скриптове очищення веб-сторінки / HTML-розмітки.

### 0.4. Двошарова архітектура локального корпусу (Two-Tier Architecture)
- **`sources/primary/transcriptions/diplomatic/`** — доказовий шар (evidence layer), що зберігає повний автентичний текст видання.
- **`sources/primary/transcriptions/normalized/`** — нормалізований шар (research convenience layer), очищений для алгоритмічного пошуку та семантичного аналізу понять.

---

## 1. ЗВЕДЕНИЙ РЕЄСТР ПЕРШОЇ ХВИЛІ ЗА ТРИРІВНЕВОЮ ШКАЛОЮ FIDELITY

| WITNESS-ID | WORK (Пам'ятка) | PHYSICAL WITNESS | EDITION-IDENTITY | LOCAL FILE (DIPLOMATIC) | TRANSCRIPTION-MODE | FIDELITY-LEVEL | TEXT-LOSS-RISK |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`WIT-ORLYK-1710-UA`** | Pacta et Constitutiones 1710 (староукр.) | РДАДА ф. 13, спр. 10, арк. 1–19 | 🟢 `VERIFIED` (ЦДІАК, 2010) | `SRC-ORLYK-1710-UA-DIPLOMATIC.txt` | `SEMI-DIPLOMATIC` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟡 MEDIUM |
| **`WIT-ORLYK-1710-LAT`**| Pacta et Constitutiones 1710 (латина) | Riksarkivet Stockholm, Cosacica | 🟢 `VERIFIED` (Молчановський 1898) | `SRC-ORLYK-1710-LAT-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟡 MEDIUM |
| **`WIT-RP-SHORT`** | Правда Роськая (Коротка) | БАН 17.4.9 (список XV ст.) | 🟢 `VERIFIED` (АН СРСР 1984) | `SRC-RP-SHORT-DIPLOMATIC.txt` | `SEMI-DIPLOMATIC` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟢 LOW |
| **`WIT-RP-EXP`** | Правда Русьская (Розширена) | РДБ ф. 304.I № 793 (XIV ст.) | 🟢 `VERIFIED` (АН СРСР 1984) | `SRC-RP-EXP-DIPLOMATIC.txt` | `SEMI-DIPLOMATIC` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟢 LOW |
| **`WIT-LS-1566`** | II Литовський Статут 1566 | Рукописні списки XVI ст. | 🟢 `VERIFIED` (Мінськ 2003 / 1855) | `SRC-LS-1566-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟢 LOW |
| **`WIT-LS-1588`** | III Литовський Статут 1588 | Стародрук Мамоничів 1588 | 🟢 `VERIFIED` (АН БССР 1989) | `SRC-LS-1588-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟡 MEDIUM |
| **`WIT-HADIACH-COMM-1658`**| Гадяцька комісарська угода | Рукопис комісії (16.09.1658) | 🟢 `VERIFIED` (Польс. археографія) | `SRC-HADIACH-1658-COMMISSION-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟡 MEDIUM |
| **`WIT-HADIACH-SEJM-1659`**| Гадяцька сеймова конституція | Друк. сеймові книги 1659 | 🟢 `VERIFIED` (Vol. Legum T. IV) | Відсутній (зафіксовано с. 297–301) | — | ⚪ **L0** (`PENDING`) | 🔴 HIGH |
| **`WIT-ZBORIV-1649`** | Зборівський комплекс (4 акти) | AGAD Metryka Koronna / РДАДА | 🟢 `VERIFIED` (АЮЗР Т. III) | `secondary/analysis/SRC-ZBORIV-1649-COMPLEX-ANALYSIS.txt` | `ANALYTICAL DECONSTRUCTION` | 🔵 **N/A** (COMPLEX LEVEL) | ⚪ N/A |
| **`WIT-MARCH-1654`** | Березневі статті (11 статей) | РДАДА ф. 229, спр. 9 (список XVII) | 🟢 `VERIFIED` (АН СССР 1953) | `SRC-MARCH-1654-DIPLOMATIC.txt` | `PLAIN EXTRACTION` | 🟡 **L1** (`VERIFIED-DIGITAL`) | 🟢 LOW |

---

## 2. ПОПАСПОРТНИЙ АУДИТ ТОЧНОСТІ ТЕКСТУ (FIDELITY AUDIT CARDS)

### 2.1. `WIT-LS-1566`: ДРУГИЙ ЛИТОВСЬКИЙ СТАТУТ
- **EDITION-LOCATOR**: «Статут Вялікага княства Літоўскага 1566 года». — Мінск, 2003. — С. 35–263 (за першовиданням Т. Роговцова 1855 р.).
- **ACTUAL-COLLATION-TARGET**: Електронна публікація науково-видавничого проекту «Ізборник» (`litopys.kiev.ua/statut2/st1566_01.htm` ... `st1566_15.htm`).
- **PRINTED-EDITION-PAGES-CHECKED**: NO (Звірено посторінково веб-відтворення 15 розділів, безпосередній скан видання 2003 р. не вичитувався).
- **TRANSCRIPTION-MODE**: `PLAIN EXTRACTION` (Скриптове очищення навігаційних банерів та тегів розмітки з відновленням суцільного тексту).
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **CORRECTION HISTORY**: Попередній статус `DEFECTIVE` знято, оскільки всі 14 розділів диспозицій відновлено у файлі (631 КБ). Статус `VERIFIED-AGAINST-EDITION` відхилено як надмірний: рівень строго зафіксовано як **L1**.
- **DIFF ARTIFACT**: [`diffs/LS-1566.diff`](file:///home/agents/GitHub/pravda/diffs/LS-1566.diff).

---

### 2.2. `WIT-ORLYK-1710-UA` ТА `WIT-ORLYK-1710-LAT`: СУВОРЕ РОЗМЕЖУВАННЯ СВІДКІВ
- **WORK**: Pacta et Constitutiones legum libertatumque exercitus zaporoviensis 1710 р.
- **ДЕМАРКАЦІЯ НОСІЇВ**: Розділено на два окремі свідки:
  1. `WIT-ORLYK-1710-UA`: Староукраїнський автограф РДАДА (ф. 13, спр. 10, арк. 1–19). Файл: [`SRC-ORLYK-1710-UA-DIPLOMATIC.txt`](file:///home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-ORLYK-1710-UA-DIPLOMATIC.txt). Режим: `SEMI-DIPLOMATIC`. Рівень: 🟡 **L1**.
  2. `WIT-ORLYK-1710-LAT`: Латинський скорочений компедіум Riksarkivet Stockholm (Cosacica). Файл: [`SRC-ORLYK-1710-LAT-DIPLOMATIC.txt`](file:///home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-ORLYK-1710-LAT-DIPLOMATIC.txt). Режим: `PLAIN EXTRACTION`. Рівень: 🟡 **L1**.
- **ACTUAL-COLLATION-TARGET**: `uk.wikisource.org/wiki/Конституція_Пилипа_Орлика`.
- **DIFF ARTIFACTS**: [`diffs/ORLYK-1710-UA.diff`](file:///home/agents/GitHub/pravda/diffs/ORLYK-1710-UA.diff), [`diffs/ORLYK-1710-LAT.diff`](file:///home/agents/GitHub/pravda/diffs/ORLYK-1710-LAT.diff).

---

### 2.3. `WIT-RP-SHORT` ТА `WIT-RP-EXP`: РУСЬКА ПРАВДА
- **ACTUAL-COLLATION-TARGET**: Цифрова публікація `ru.wikisource`, що походить із видання «Российское законодательство X–XX веков» (Т. 1, М., 1984, с. 47–49 та с. 64–73).
- **PRINTED-EDITION-PAGES-CHECKED**: PARTIAL (Структурний склад 43 статей Короткої та 121 статті Розширеної редакції звірено з описами тома 1984 р., суцільна звірка кожної титли зі сканом тому не проводилась).
- **TRANSCRIPTION-MODE**: `SEMI-DIPLOMATIC`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **DIFF ARTIFACTS**: [`diffs/RP-SHORT.diff`](file:///home/agents/GitHub/pravda/diffs/RP-SHORT.diff), [`diffs/RP-EXP.diff`](file:///home/agents/GitHub/pravda/diffs/RP-EXP.diff).

---

### 2.4. `WIT-MARCH-1654`: БЕРЕЗНЕВІ СТАТТІ (МОСКОВСЬКИЙ СПИСОК)
- **ACTUAL-COLLATION-TARGET**: `ru.wikisource` за збірником «Воссоединение Украины с Россией» (Т. III, М., 1953, № 108, с. 560–567).
- **PRINTED-EDITION-PAGES-CHECKED**: PARTIAL (Звірено наявність та зміст усіх 11 статей козацького челобиття та царських резолюцій).
- **TRANSCRIPTION-MODE**: `PLAIN EXTRACTION`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **DIFF ARTIFACT**: [`diffs/MARCH-1654.diff`](file:///home/agents/GitHub/pravda/diffs/MARCH-1654.diff).

---

### 2.5. `WIT-LS-1588`: ТРЕТІЙ ЛИТОВСЬКИЙ СТАТУТ
- **ACTUAL-COLLATION-TARGET**: Цифрова база правової інформації `pravo.by` / `be.wikisource` за академічним виданням АН БССР 1989 р.
- **TRANSCRIPTION-MODE**: `PLAIN EXTRACTION`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **DIFF ARTIFACT**: [`diffs/LS-1588.diff`](file:///home/agents/GitHub/pravda/diffs/LS-1588.diff).

---

### 2.6. `WIT-HADIACH-COMM-1658`: ГАДЯЦЬКИЙ ТАБІРНИЙ АКТ
- **ACTUAL-COLLATION-TARGET**: `pl.wikisource` (Pakta Hadziackie autentyczne).
- **TRANSCRIPTION-MODE**: `PLAIN EXTRACTION`.
- **FIDELITY-LEVEL**: 🟡 **L1** (`VERIFIED-AGAINST-DIGITAL-DERIVATIVE`).
- **DIFF ARTIFACT**: [`diffs/HADIACH-COMM-1658.diff`](file:///home/agents/GitHub/pravda/diffs/HADIACH-COMM-1658.diff).

---

### 2.7. `WIT-HADIACH-SEJM-1659`: СЕЙМОВИЙ АКТ
- **EDITION-LOCATOR**: «Volumina Legum», вид. Й. Огризка, СПб., 1859, Т. IV, с. 297–301 («Kommissya Hadziacka»).
- **FIDELITY-LEVEL**: ⚪ **L0** (`PENDING / UNCOLLATED`).

---

### 2.8. `WIT-ZBORIV-1649`: СТАТУС ДОГОВІРНОГО КОМПЛЕКСУ
- **WORK / COMPLEX STATUS**: Документ є історико-правовим комплексом, а не єдиним свідком.
- **LOCAL PRIMARY REPRESENTATIONS**:
  - `WIT-ZBORIV-1649-DECLARATION`: PENDING
  - `WIT-ZBORIV-1649-PETITION`: PENDING
  - `WIT-ZBORIV-1649-KHAN-TREATY`: PENDING
  - `WIT-ZBORIV-1649-REGISTER`: PENDING
- **ANALYSIS**: Дослідницький огляд структури зберігається у `sources/secondary/analysis/SRC-ZBORIV-1649-COMPLEX-ANALYSIS.txt`.
- **FIDELITY-LEVEL**: 🔵 **NOT APPLICABLE AT COMPLEX LEVEL** (Оцінюватиметься для кожного окремого складового акта після вивантаження).

---

## 3. ПІДСУМОК: СТАН ІНФРАСТРУКТУРИ ТА ГОТОВНІСТЬ ДО ЗМІСТОВНОГО АНАЛІЗУ

1. **Інфраструктурний цикл завершено**:
   - Ідентифіковано фізичні носії (архіви, фонди, шифри).
   - Ідентифіковано авторитетні наукові видання (томи, сторінки).
   - Встановлено та задокументовано цифрові ланцюги передачі.
   - Створено двошарову структуру корпусу (`diplomatic/` для доказів, `normalized/` для пошуку).
   - Точність кожного файлу чесно зафіксовано на рівні **L1** (звірено з цифровими академічними репозиторіями), що виключає самообман щодо L2 (скани видань) або L3 (рукописи).
2. **Перехід до семантичного дослідження**:
   - Корпус досяг порогу відтворюваності.
   - Будь-яке подальше цитування правових норм щодо «прав», «вольностей», «присяги» та «договору» спирається на чітко локалізований та атестований текст.
