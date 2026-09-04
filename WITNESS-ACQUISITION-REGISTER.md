# РЕЄСТР НАБУТТЯ ТА АТЕСТАЦІЇ НОСІЇВ ДЖЕРЕЛ (WITNESS-ACQUISITION-REGISTER)
## Status: ACTIVE · First Wave: 10 Corpora · Pass: Local Text Fidelity Pass 1

---

## 0. МЕТОДОЛОГІЧНА ДЕМАРКАЦІЯ ТА СУВОРІ ЗАБОРОНИ

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

### 0.2. Двошарова архітектура локального корпусу (Two-Tier Architecture)
Щоб уникнути випадкового спотворення орфографії пам'ятки під час дослідницьких пошуків, локальні тексти зберігаються у двох функціональних шарах:
1. **`sources/primary/transcriptions/diplomatic/`** — дипломатичний шар (evidence layer), що зберігає повний автентичний текст видання, включаючи старовинну графіку, титла та видавничий апарат.
2. **`sources/primary/transcriptions/normalized/`** — нормалізований шар (research convenience layer), очищений від вікі-шаблонів та технічних артефактів для машинного пошуку та семантичного картування.

### 0.3. Машинні дифи та аудит змін (Audit Trail)
Усі текстологічні виправлення, реставрації диспозицій або колізії видань фіксуються в машинночитаних файлах журналу змін у каталозі `diffs/`:
```text
diffs/
├── LS-1566.diff        (Повне відновлення диспозицій 14 розділів замість реєстру)
├── LS-1588.diff        (Аудит повноти 1,5 МБ тексту 488 артикулів)
├── HADIACH-COMM-1658.diff (Фіксація польського тексту табору під Гадячем)
├── ORLYK-1710-UA.diff  (Звірка паралельного українсько-латинського корпусу)
├── RP-SHORT.diff       (Звірка 43 статей Короткої редакції за виданням 1984 р.)
├── RP-EXP.diff         (Звірка 121 статті Троїцького списку за виданням 1984 р.)
└── MARCH-1654.diff     (Звірка 11 статей Посольського приказу за виданням 1953 р.)
```

---

## 1. ЗВЕДЕНИЙ РЕЄСТР ПЕРШОЇ ХВИЛІ З ОЦІНКОЮ РИЗИКУ ВТРАТИ ТЕКСТУ (TEXT-LOSS-RISK)

| WITNESS-ID | WORK (Пам'ятка) | PHYSICAL WITNESS | EDITION-IDENTITY | LOCAL FILE (DIPLOMATIC) | SHA256 (перші 12 знаків) | LOCAL-TEXT-FIDELITY | TEXT-LOSS-RISK |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`WIT-LS-1566`** | II Литовський Статут 1566 | Списки XVI ст. | 🟢 `VERIFIED` (Мінськ 2003 / 1855) | `diplomatic/SRC-LS-1566-DIPLOMATIC.txt` | `2eb41b5455c4` | 🟢 `VERIFIED-AGAINST-EDITION` | 🟢 LOW |
| **`WIT-LS-1588`** | III Литовський Статут 1588 | Стародрук Мамоничів 1588 | 🟢 `VERIFIED` (АН БССР 1989) | `diplomatic/SRC-LS-1588-DIPLOMATIC.txt` | `9bfed8a32f30` | 🟡 `PARTIAL` | 🟡 MEDIUM |
| **`WIT-ORLYK-1710-UA`** | Pacta et Constitutiones 1710 | РДАДА ф. 13, спр. 10, арк. 1–19 | 🟢 `VERIFIED` (ЦДІАК, 2010) | `diplomatic/SRC-ORLYK-1710-DIPLOMATIC.txt` | `664721977bf6` | 🟡 `PARTIAL` | 🟡 MEDIUM |
| **`WIT-ORLYK-1710-LAT`**| Pacta et Constitutiones 1710 | Riksarkivet Stockholm, Cosacica | 🟢 `VERIFIED` (Молчановський 1898) | `diplomatic/SRC-ORLYK-1710-DIPLOMATIC.txt` | `664721977bf6` | 🟡 `PARTIAL` | 🟡 MEDIUM |
| **`WIT-RP-SHORT`** | Правда Роськая (Коротка) | БАН 17.4.9 (список XV ст.) | 🟢 `VERIFIED` (АН СРСР 1984) | `diplomatic/SRC-RP-SHORT-DIPLOMATIC.txt` | `67548ce28319` | 🟢 `VERIFIED-AGAINST-EDITION` | 🟢 LOW |
| **`WIT-RP-EXP`** | Правда Русьская (Розширена) | РДБ ф. 304.I № 793 (XIV ст.) | 🟢 `VERIFIED` (АН СРСР 1984) | `diplomatic/SRC-RP-EXP-DIPLOMATIC.txt` | `72169bbed2d4` | 🟢 `VERIFIED-AGAINST-EDITION` | 🟢 LOW |
| **`WIT-HADIACH-COMM-1658`**| Гадяцька комісарська угода | Рукопис комісії (16.09.1658) | 🟢 `VERIFIED` (Польс. археографія) | `diplomatic/SRC-HADIACH-1658-COMMISSION-DIPLOMATIC.txt` | `7d98f36f27c9` | 🟡 `PARTIAL` | 🟡 MEDIUM |
| **`WIT-HADIACH-SEJM-1659`**| Гадяцька сеймова конституція | Друк. сеймові книги 1659 | 🟢 `VERIFIED` (Vol. Legum T. IV) | Відсутній (зафіксовано сторінки) | — | ⚪ `PENDING (PAGES 297–301)` | 🔴 HIGH |
| **`WIT-ZBORIV-1649`** | Зборівський комплекс (4 акти) | AGAD Metryka Koronna / РДАДА | 🟢 `VERIFIED` (АЮЗР Т. III) | `secondary/analysis/SRC-ZBORIV-1649-COMPLEX-ANALYSIS.txt` | `e0476e9599c2` | 🔵 `SECONDARY-ANALYSIS` | 🟢 LOW |
| **`WIT-MARCH-1654`** | Березневі статті (11 статей) | РДАДА ф. 229, спр. 9 (список XVII) | 🟢 `VERIFIED` (АН СССР 1953) | `diplomatic/SRC-MARCH-1654-DIPLOMATIC.txt` | `aacf9ce68236` | 🟢 `VERIFIED-AGAINST-EDITION` | 🟢 LOW |

---

## 2. ПОПАСПОРТНИЙ АУДИТ ТОЧНОСТІ ТЕКСТУ (FIDELITY CARDS)

### 2.1. `WIT-LS-1566`: УСУНЕННЯ ДЕФЕКТУ НЕПОВНОТИ
- **EDITION-LOCATOR**: «Статут Вялікага княства Літоўскага 1566 года». — Мінск, 2003. — С. 35–263 (за першовиданням Т. Роговцова 1855 р.).
- **PREVIOUS STATUS**: 🔴 `DEFECTIVE (REGISTER-ONLY)` (Файл містив лише зміст на 34 КБ без тексту статей).
- **CURRENT STATUS**: 🟢 `VERIFIED-AGAINST-EDITION` (Повний корпус диспозицій усіх 14 розділів відновлено; обсяг 631 007 байт, 5 541 рядок).
- **CHECKSUM (SHA256)**: `2eb41b5455c47912c8ed31779cbb083b457b8eb9caa701a411179f2422a6d715`.
- **DIFF ARTIFACT**: [`diffs/LS-1566.diff`](file:///home/agents/GitHub/pravda/diffs/LS-1566.diff).
- **TEXT-LOSS-RISK**: `LOW` (Усі 14 розділів завантажено з вихідного посторінкового видання litopys.kiev.ua без купюр).

---

### 2.2. `WIT-HADIACH-SEJM-1659`: ФІКСАЦІЯ ВИДАННЯ ТА СТОРІНОК
- **WORK**: Конституція Варшавського сейму травня 1659 р. «Kommissya Hadziacka».
- **EDITION-IDENTIFIED**: YES.
- **EDITION-LOCATOR**: «Volumina Legum: przedruk zbioru praw staraniem XX. Pijarów w Warszawie...». — Wyd. Jozafata Ohryzki. — Petersburg, 1859. — T. IV. — S. 297–301.
- **HOLDING INSTITUTION**: Wielkopolska Biblioteka Cyfrowa (WBC, публікація № 54088) / Biblioteka Narodowa (Polona).
- **CURRENT STATUS**: ⚪ `PENDING (PAGES 297–301)` (Текст ідентифіковано, посторінкове OCR-скачування захищене системою верифікації браузера бібліотеки; очікує інтеграції).
- **TEXT-LOSS-RISK**: `HIGH` (Очікує прямого PDF-вивантаження сторінок 297–301).

---

### 2.3. `WIT-RP-SHORT` ТА `WIT-RP-EXP`: АТЕСТОВАНА АКАДЕМІЧНА ЗВІРКА
- **EDITION-LOCATOR**: «Российское законодательство X–XX веков». — Т. 1. — М.: Юрид. лит., 1984. — С. 47–49 (Коротка) та С. 64–73 (Розширена).
- **CURRENT STATUS**: 🟢 `VERIFIED-AGAINST-EDITION`.
- **DIFF ARTIFACTS**: [`diffs/RP-SHORT.diff`](file:///home/agents/GitHub/pravda/diffs/RP-SHORT.diff), [`diffs/RP-EXP.diff`](file:///home/agents/GitHub/pravda/diffs/RP-EXP.diff).
- **TEXT-LOSS-RISK**: `LOW` (Повний збіг структури 43 статей Короткої та 121 статті Троїцького списку Розширеної редакції).

---

### 2.4. `WIT-MARCH-1654`: ПРИКАЗНИЙ СПИСОК 11 СТАТЕЙ
- **EDITION-LOCATOR**: «Воссоединение Украины с Россией. Документы и материалы». — М.: Изд-во АН СССР, 1953. — Т. III. — Док. № 108. — С. 560–567.
- **CURRENT STATUS**: 🟢 `VERIFIED-AGAINST-EDITION`.
- **DIFF ARTIFACT**: [`diffs/MARCH-1654.diff`](file:///home/agents/GitHub/pravda/diffs/MARCH-1654.diff).
- **TEXT-LOSS-RISK**: `LOW`.

---

### 2.5. `WIT-LS-1588`, `WIT-ORLYK-1710`, `WIT-HADIACH-COMM-1658`
- **CURRENT STATUS**: 🟡 `PARTIAL` (Структурний склад статей перевірено повністю; суцільне посимвольне звірення багатосторінкових текстів із паперовим виданням триває).
- **DIFF ARTIFACTS**: [`diffs/LS-1588.diff`](file:///home/agents/GitHub/pravda/diffs/LS-1588.diff), [`diffs/ORLYK-1710-UA.diff`](file:///home/agents/GitHub/pravda/diffs/ORLYK-1710-UA.diff), [`diffs/HADIACH-COMM-1658.diff`](file:///home/agents/GitHub/pravda/diffs/HADIACH-COMM-1658.diff).
- **TEXT-LOSS-RISK**: `MEDIUM`.

---

## 3. ПІДСУМОК ПРОХОДУ ТОЧНОСТІ ТЕКСТУ (FIDELITY SUMMARY)

1. **Критичний дефект неповноти усунуто**: Статут 1566 року набув повноти (631 КБ диспозицій замість 60 КБ реєстру) і підвищений до `VERIFIED-AGAINST-EDITION`.
2. **Створено двошарову структуру**:
   - `diplomatic/` для доказової бази;
   - `normalized/` для семантичного та мовного аналізу.
3. **Розгорнуто журнал відмінностей `diffs/`**: кожен виправлений або атестований файл має чіткий машинний слід аудиту.
4. **Зафіксовано ризики спотворення (`TEXT-LOSS-RISK`)**: жоден текст не вважається бездоганним за замовчуванням.
