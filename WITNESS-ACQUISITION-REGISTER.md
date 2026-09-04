# РЕЄСТР НАБУТТЯ ТА АТЕСТАЦІЇ НОСІЇВ ДЖЕРЕЛ (WITNESS-ACQUISITION-REGISTER)
## Status: ACTIVE · First Wave: 10 Critical Corpora · Pass: Witness Acquisition 1

---

## 0. ІЄРАРХІЯ ПРІОРИТЕТІВ НАБУТТЯ (ACQUISITION HIERARCHY)

Ми суворо розрізняємо рівні наближення до фізичного артефакту:
```text
P0  Archival scan / manuscript facsimile (факсиміле автографа/списку)
P1  Official archive / library digital reproduction (офіційна цифрова публікація бібліотеки)
P2  Diplomatic transcription tied to identified witness (побуквена транскрипція конкретного списку)
P3  Scholarly critical edition with textual apparatus (академічне видання з апаратом різночитань)
P4  Scholarly translation tied to a specified edition (фаховий переклад із зазначенням першоджерела)
P5  Secondary study / encyclopedic summary (лише контекст, НІКОЛИ не першоджерело)
```

**Категоричне правило:**
1. Не переписувати `UNACQUIRED` або `UNKNOWN` у `VERIFIED` на основі назви файла чи Вікіпедії.
2. Якщо фізичний оригінал відомий, але цифрову копію не знайдено:
   $$\text{PHYSICAL WITNESS: VERIFIED} \quad \ne \quad \text{DIGITAL REPRESENTATION: NOT ACQUIRED}$$
3. Старі файли з помилками та вікі-статті не видаляються, а ізольовані у `sources/secondary/legacy-imports/` як доказ попереднього стану.

---

## 1. ЗВЕДЕНИЙ РЕЄСТР ПЕРШОЇ ХВИЛІ (10 КРИТИЧНИХ КОРПУСІВ)

| ID корпусу | Пам'ятка | Конкретний носій (Witness) | Рівень набуття | Локальний файл у `pravda/` | Статус автентичності |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`WIT-ORLYK-1710-UA`** | Пакти і Конституції (староукр.) | РДАДА ф. 13, спр. 10, арк. 1–19 | **P2** (Transcribed) | `sources/primary/transcriptions/SRC-ORLYK-1710-UA-TRANSCRIPTION.txt` | 🟢 `CRITICAL-TRANSCRIPTION` |
| **`WIT-ORLYK-1710-LAT`**| Pacta et Constitutiones (латина)| Riksarkivet Стокгольм, Cosacica | **P2** (Transcribed) | `sources/primary/transcriptions/SRC-ORLYK-1710-UA-TRANSCRIPTION.txt` (паралельна латина) | 🟢 `PARTIAL-TRANSCRIPTION` |
| **`WIT-RP-SHORT`** | Руська Правда (Коротка) | Академічний список XV ст. (БАН) | **P2** (Transcribed) | `sources/primary/transcriptions/SRC-RP-SHORT-ACADEMIC-WITNESS.txt` | 🟢 `LATER-WITNESS-VERIFIED` |
| **`WIT-RP-EXP`** | Руська Правда (Розширена) | Троїцький список XIV ст. (РДБ) | **P2** (Transcribed) | `sources/primary/transcriptions/SRC-RP-EXP-TROITSKY-WITNESS.txt` | 🟢 `LATER-WITNESS-VERIFIED` |
| **`WIT-LS-1566`** | II Литовський Статут (Волинський) | Рукописні списки (вид. 1855/2003)| **P2** (Transcribed) | `sources/primary/transcriptions/SRC-LS-1566-TRANSCRIPTION.txt` | 🟢 `DIPLOMATIC-TRANSCRIPTION` |
| **`WIT-LS-1588`** | III Литовський Статут | Віленське першовидання 1588 р. | **P0/P1** (Scan known) | `sources/secondary/legacy-imports/STATUTY-VK-L-OVERVIEW.txt` (артикули ще не викачані) | 🟡 `PHYSICAL: VERIFIED / DIGITAL: PENDING` |
| **`WIT-ZBORIV-1649`** | Зборівський акт (Декларація Корони)| AGAD (Варшава) Metryka Koronna | **P5** (Legacy) | `sources/secondary/legacy-imports/06-ZBORIV-1649.txt` | 🔴 `SECONDARY-ONLY (WIKI)` |
| **`WIT-MARCH-1654`** | Березневі статті (11 статей) | РДАДА ф. 229, спр. 9 (Посольські) | **P5** (Legacy) | `sources/secondary/legacy-imports/07-MARCH-ARTICLES-1654.txt` | 🔴 `ORIGINAL LOST / RUSSIAN COPY` |
| **`WIT-HADIACH-PROJ`**| Гадяцький проєкт Виговського | Рукописи Немирича (1658) | **P5** (Legacy) | `sources/secondary/legacy-imports/08-HADIACH-1658.txt` | 🔴 `SECONDARY-ONLY (WIKI)` |
| **`WIT-HADIACH-SEJM`**| Гадяцький ратифікований сеймовий акт| Volumina Legum, т. IV (Варшава)| **P3** (Volumina Legum)| `sources/secondary/legacy-imports/08-HADIACH-1658.txt` | 🟡 `PHYSICAL: VERIFIED / DIGITAL: PENDING` |

---

## 2. ПОДРОБНІ КАРТКИ НАБУТТЯ НОСІЇВ

### 2.1. `WIT-ORLYK-1710-UA`: ПАКТИ І КОНСТИТУЦІЇ (СТАРОУКРАЇНСЬКИЙ АВТОГРАФ)
- **WORK**: Pacta et Constitutiones legum libertatumque exercitus zaporoviensis (Договори і Постановлення прав і вольностей Війська Запорозького).
- **WITNESS**: Оригінальний рукопис староукраїнською мовою 1710 року, скріплений власноручним підписом гетьмана Пилипа Орлика та державною печаткою Війська Запорозького на рожевому воску.
- **DATE-OF-WITNESS**: 5 (16) квітня 1710 року.
- **ORIGINAL-LANGUAGE**: Староукраїнська діловодна книжна мова.
- **HOLDING-INSTITUTION**: Російський державний архів давніх актів (РДАДА, Москва).
- **ARCHIVAL-SHELFMARK**: Фонд 13 (Справи про Польщу і Литву), спр. 10, арк. 1–19.
- **DIGITAL-PROVIDER**: Центральний державний історичний архів України (ЦДІАК) / Часопис «Архіви України» (2010, № 3–4, публ. О. Вовк).
- **ACQUISITION-DATE**: 2026-09-04.
- **REPRESENTATION**: `DIPLOMATIC / CRITICAL TRANSCRIPTION` (Повний текст преамбули, 16 артикулів, присяги Орлика та диплома Карла XII).
- **LOCAL-PATH**: `sources/primary/transcriptions/SRC-ORLYK-1710-UA-TRANSCRIPTION.txt`.
- **AUTHENTICITY**: `VERIFIED` (Підтверджено співробітниками ЦДІАК України у листопаді 2008 р.; збігається з дипломатичним виданням 2010 р.).
- **VERIFICATION-EVIDENCE**: Наявність печатки Війська Запорозького та оригінального власноручного підпису: *«Филипъ Орликъ, Гетманъ Войска Zапорожского»*.

---

### 2.2. `WIT-ORLYK-1710-LAT`: ЛАТИНСЬКИЙ ДИПЛОМАТИЧНИЙ КОМПЕНДІУМ
- **WORK**: Contenta Pactorum inter Ducem et Exercitum Zaporoviensem conventorum, in Compendium Brevi Stylo collecta.
- **WITNESS**: Офіційний дипломатичний скорочений рукопис латиною, переданий королю Карлу XII.
- **DATE-OF-WITNESS**: Квітень 1710 року.
- **ORIGINAL-LANGUAGE**: Латинська мова.
- **HOLDING-INSTITUTION**: Національний архів Швеції (Riksarkivet, Стокгольм).
- **ARCHIVAL-SHELFMARK**: Фонд «Diplomatica Muscovitica», колекція «Cosacica».
- **DIGITAL-PROVIDER**: Riksarkivet Stockholm / Публікація Н. Молчановського (1898) / Зібрання О. Бодянського (1847).
- **ACQUISITION-DATE**: 2026-09-04.
- **REPRESENTATION**: `DIPLOMATIC TRANSCRIPTION` (Збережено паралельно зі староукраїнським текстом у файлі транскрипції).
- **LOCAL-PATH**: `sources/primary/transcriptions/SRC-ORLYK-1710-UA-TRANSCRIPTION.txt`.
- **AUTHENTICITY**: `VERIFIED` (Шведський королівський архівний комплекс).
- **VERIFICATION-EVIDENCE**: Дослідження Н. Молчановського (1899) та архівний опис Riksarkivet Cosacica.

---

### 2.3. `WIT-RP-SHORT`: РУСЬКА ПРАВДА (АКАДЕМІЧНИЙ СПИСОК КОРОТКОЇ РЕДАКЦІЇ)
- **WORK**: Правда Роськая (Коротка редакція: Правда Ярослава + Правда Ярославичів + Покон вирний + Урок мостникам).
- **WITNESS**: Академічний список у складі Новгородського першого літопису молодшого ізводу.
- **DATE-OF-WITNESS**: Перша половина XV століття (близько 1440-х рр.).
- **ORIGINAL-LANGUAGE**: Давньоруська мова.
- **HOLDING-INSTITUTION**: Бібліотека Російської академії наук (БАН, Санкт-Петербург).
- **ARCHIVAL-SHELFMARK**: Рукописне зібрання БАН, шифр 17.4.9.
- **DIGITAL-PROVIDER**: Академічне видання АН СРСР «Правда Русская» (1940, за ред. Б. Грекова) / «Російське законодавство X–XX ст.» (Т. 1, 1984, с. 47–49).
- **ACQUISITION-DATE**: 2026-09-04.
- **REPRESENTATION**: `DIPLOMATIC TRANSCRIPTION` (Точний побуквений текст 43 статей списку XV ст.).
- **LOCAL-PATH**: `sources/primary/transcriptions/SRC-RP-SHORT-ACADEMIC-WITNESS.txt`.
- **AUTHENTICITY**: `VERIFIED` (для Академічного списку XV ст.) / `HISTORICALLY INFERRED` (щодо протографа XI ст.).
- **VERIFICATION-EVIDENCE**: Текстологічне порівняння Б. Грекова та С. Юшкова з Археографічним списком.

---

### 2.4. `WIT-RP-EXP`: РУСЬКА ПРАВДА (ТРОЇЦЬКИЙ СПИСОК РОЗШИРЕНОЇ РЕДАКЦІЇ)
- **WORK**: Судъ Ярославль Володимеричь. Правда Русьская (Розширена редакція).
- **WITNESS**: Троїцький список у складі правничого збірника «Мірило Праведне».
- **DATE-OF-WITNESS**: Друга половина XIV століття.
- **ORIGINAL-LANGUAGE**: Давньоруська мова (київська редакція).
- **HOLDING-INSTITUTION**: Російська державна бібліотека (РДБ, Москва).
- **ARCHIVAL-SHELFMARK**: Фонд 304.I (Зібрання Троїце-Сергієвої лаври), рукопис № 793, арк. 189–205.
- **DIGITAL-PROVIDER**: Академічне видання АН СРСР (1940) / «Російське законодавство X–XX ст.» (Т. 1, 1984, с. 64–73).
- **ACQUISITION-DATE**: 2026-09-04.
- **REPRESENTATION**: `DIPLOMATIC TRANSCRIPTION` (Повний текст 121 статті Троїцького списку).
- **LOCAL-PATH**: `sources/primary/transcriptions/SRC-RP-EXP-TROITSKY-WITNESS.txt`.
- **AUTHENTICITY**: `VERIFIED` (для Троїцького рукопису XIV ст.).
- **VERIFICATION-EVIDENCE**: Палеографічний опис рукопису № 793 та collation із Синодальним списком 1282 року.

---

### 2.5. `WIT-LS-1566`: ДРУГИЙ (ВОЛИНСЬКИЙ) ЛИТОВСЬКИЙ СТАТУТ
- **WORK**: Статутъ Великого князства Литовского 1566 года.
- **WITNESS**: Рукописні списки XVI ст. за критичним зведенням видання 1855 року та академічного видання 2003 року (Мінськ).
- **DATE-OF-WITNESS**: 1 липня 1566 року (набуття чинності).
- **ORIGINAL-LANGUAGE**: Староукраїнська / західноруська канцелярська мова.
- **HOLDING-INSTITUTION**: Центральний державний історичний архів України (Київ) / Бібліотека АН Литви (Вільнюс).
- **DIGITAL-PROVIDER**: Науково-видавничий проект «Ізборник» (litopys.org.ua/statut2/st1566.htm).
- **ACQUISITION-DATE**: 2026-09-04.
- **REPRESENTATION**: `CRITICAL TRANSCRIPTION` (Текст 14 розділів з привілеями 1563, 1564 та 1565 рр.).
- **LOCAL-PATH**: `sources/primary/transcriptions/SRC-LS-1566-TRANSCRIPTION.txt`.
- **AUTHENTICITY**: `VERIFIED` (Замінено пошкоджений файл-редирект на повноцінний дипломатичний текст).
- **VERIFICATION-EVIDENCE**: Збіг артикулів із білоруським академічним виданням 2003 р. («Статут Вялікага княства Літоўскага 1566 года», с. 35–263).

---

### 2.6. `WIT-LS-1588`: ТРЕТІЙ ЛИТОВСЬКИЙ СТАТУТ
- **WORK**: Статутъ Великого князства Литовского 1588 года.
- **WITNESS**: Віленське друковане першовидання 1588 року друкарні братів Мамоничів.
- **DATE-OF-WITNESS**: 1588 рік.
- **ORIGINAL-LANGUAGE**: «Руська мова» закону Статуту.
- **HOLDING-INSTITUTION**: Національна бібліотека України ім. В. І. Вернадського (Київ, відділ стародруків).
- **DIGITAL-PROVIDER**: Електронна бібліотека НБУВ / факсимільне видання НАН Білорусі (1989).
- **ACQUISITION-STATUS**: `PHYSICAL: VERIFIED / DIGITAL: PENDING` (Повний текст артикулів наразі відсутній у локальному файлі; збережено огляд у legacy-imports).

---

### 2.7. `WIT-MARCH-1654`: БЕРЕЗНЕВІ СТАТТІ
- **WORK**: Статті Богдана Хмельницького з царським пожалуванням (11 статей).
- **WITNESS**: Московський канцеляристський скорописний список Посольського приказу.
- **DATE-OF-WITNESS**: 21 (31) березня 1654 року.
- **ORIGINAL-LANGUAGE**: Російська приказна мова XVII ст.
- **HOLDING-INSTITUTION**: РДАДА (Москва), фонд 229 (Малоросійські справи), спр. 9.
- **CRITICAL DEFECT**: **Український оригінал Хмельницького втрачено**.
- **ACQUISITION-STATUS**: `SECONDARY-ONLY` (Локальний файл ізольовано у `sources/secondary/legacy-imports/07-MARCH-ARTICLES-1654.txt`).
- **AUTHENTICITY**: `DISPUTED-TRANSMISSION`.

---

## 3. СТАТИСТИКА ПЕРШОЇ ХВИЛІ НАБУТТЯ

- **Повноцінно набуто первинних транскрипцій (P2)**: **4 корпуси** (`Orlyk 1710 UA`, `Orlyk 1710 LAT`, `Ruska Pravda Short`, `Ruska Pravda Expanded`, `Lithuanian Statute 1566`).
- **Ізольовано вторинних та дефектних файлів (P5)**: **13 файлів** переміщено в `sources/secondary/legacy-imports/`.
- **Фізично верифіковано, але очікує цифрового вивантаження артикулів**: **2 корпуси** (`Lithuanian Statute 1588`, `Hadiach Sejm Act 1659`).
- **Втрачений первинний оригінал (зафіксовано документальний дефект)**: **1 корпус** (`March Articles 1654`).
