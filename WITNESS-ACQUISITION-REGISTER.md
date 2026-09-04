# РЕЄСТР НАБУТТЯ ТА АТЕСТАЦІЇ НОСІЇВ ДЖЕРЕЛ (WITNESS-ACQUISITION-REGISTER)
## Status: ACTIVE · First Wave: 10 Critical Corpora · Pass: Witness-Level Verification 1

---

## 0. ФУНДАМЕНТАЛЬНА ДЕМАРКАЦІЯ: ЧОТИРИ РІВНІ СУТНОСТЕЙ

У дослідницькому просторі `pravda` суворо заборонено змішувати рівні існування тексту. Будь-яке посилання на джерело має чітко розрізняти:

```text
WORK (Історична пам'ятка / твір як абстрактна правова ідея)
  ↓
WITNESS (Фізичний рукопис, стародрук або архівна одиниця збереження)
  ↓
EDITION (Наукова публікація, транскрипція, набір різночитань)
  ↓
DIGITAL FILE (Локальний текстовий файл у репозиторії pravda)
```

**Категоричні правила атестації:**
1. Жодна транскрипція **не є `VERIFIED-WITNESS`** лише тому, що вона походить з Wikisource, Ізборника, сайту академії чи авторитетного редактора.
2. Статус `VERIFIED-WITNESS` присвоюється **тільки за наявності звірки транскрипції безпосередньо з факсиміле/сканом конкретного носія**.
3. Якщо текст базується на академічному виданні, але безпосередня поаркушна звірка з автографом агентом ще не проведена — статус є **`VERIFIED-EDITION`**.
4. Якщо в локальному файлі міститься лише зміст / реєстр заголовків статей без їхнього повного диспозитивного тексту — статус є **`PARTIAL (REGISTER-ONLY)`**.
5. Заборонено використовувати недиференційовані назви на кшталт *«автентичний текст Зборівського договору»*, *«оригінал Березневих статей»*, *«справжній текст Гадяча»* без зазначення точного документа, редакції та witness.

---

## 1. ЗВЕДЕНИЙ РЕЄСТР ПЕРШОЇ ХВИЛІ (10 КОРПУСІВ)

| WITNESS-ID | WORK (Пам'ятка) | PHYSICAL / ARCHIVAL WITNESS | EDITION / REPR. SOURCE | DIGITAL FILE | STATUS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`WIT-ORLYK-1710-UA`** | Pacta et Constitutiones 1710 (староукр.) | РДАДА ф. 13, спр. 10, арк. 1–19 (Бендери) | ЦДІАК / О. Вовк (2010) / uk.wikisource | `sources/primary/transcriptions/SRC-ORLYK-1710-UA-TRANSCRIPTION.txt` | 🟡 `VERIFIED-EDITION` |
| **`WIT-ORLYK-1710-LAT`**| Pacta et Constitutiones 1710 (латина) | Riksarkivet Stockholm, Cosacica | Н. Молчановський (1898) / uk.wikisource | `sources/primary/transcriptions/SRC-ORLYK-1710-UA-TRANSCRIPTION.txt` | 🟡 `VERIFIED-EDITION` |
| **`WIT-RP-SHORT`** | Правда Роськая (Коротка) | БАН 17.4.9 (Академічний список XV ст.) | «Рос. законодательство» Т. 1 (1984) | `sources/primary/transcriptions/SRC-RP-SHORT-ACADEMIC-WITNESS.txt` | 🟡 `VERIFIED-EDITION` |
| **`WIT-RP-EXP`** | Правда Русьская (Розширена) | РДБ ф. 304.I № 793 (Троїцький список XIV ст.) | АН СРСР (1940) / «Рос. закон.» (1984) | `sources/primary/transcriptions/SRC-RP-EXP-TROITSKY-WITNESS.txt` | 🟡 `VERIFIED-EDITION` |
| **`WIT-LS-1566`** | II Литовський Статут 1566 р. | Списки XVI ст. (ЦДІАК / БАН Литви) | Вид. 1855 р. / Мінськ 2003 / litopys | `sources/primary/transcriptions/SRC-LS-1566-TRANSCRIPTION.txt` | 🟠 `PARTIAL (REGISTER-ONLY)` |
| **`WIT-LS-1588`** | III Литовський Статут 1588 р. | Стародрук Друкарні Мамоничів 1588 р. (НБУВ) | АН БССР (1989) / pravo.by / be.wikisource | `sources/primary/transcriptions/SRC-LS-1588-MAMONICZ-TRANSCRIPTION.txt` | 🟡 `VERIFIED-EDITION` |
| **`WIT-HADIACH-COMM-1658`**| Гадяцька комісарська угода | Рукопис комісарів під Гадячем (16.09.1658) | Польська археографія / pl.wikisource | `sources/primary/transcriptions/SRC-HADIACH-1658-COMMISSION-POLISH.txt` | 🟡 `VERIFIED-EDITION` |
| **`WIT-HADIACH-SEJM-1659`**| Гадяцький сеймовий акт 1659 р. | Затверджена конституція Варшавського сейму | Volumina Legum T. IV (Ohryzko, 1859, s. 297–301) | `sources/secondary/legacy-imports/08-HADIACH-1658.txt` | ⚪ `UNVERIFIED (DIGITAL PENDING)` |
| **`WIT-ZBORIV-1649`** | Зборівський договірний комплекс | AGAD Metryka Koronna / РДАДА ф. 229 | АЮЗР Т. III (1861) / Бантиш-Каменський (1858) | `sources/primary/transcriptions/SRC-ZBORIV-1649-COMPLEX-ANALYSIS.txt` | 🔴 `DISPUTED (MULTI-DOC COMPLEX)` |
| **`WIT-MARCH-1654`** | Березневі статті (11 статей) | РДАДА ф. 229, спр. 9 (Посольський приказ) | АН СССР «Воссоединение» Т. III (1953) № 108 | `sources/primary/transcriptions/SRC-MARCH-1654-POSOLSKIY-TRANSCRIPTION.txt` | 🟡 `VERIFIED-EDITION-OF-COPY` |

---

## 2. АТЕСТАЦІЙНІ КАРТКИ НОСІЇВ (WITNESS-LEVEL VERIFICATION)

### 2.1. `WIT-ORLYK-1710-UA`
- **WITNESS-ID**: `WIT-ORLYK-1710-UA`
- **WORK**: Pacta et Constitutiones legum libertatumque exercitus zaporoviensis (Договори і Постановлення прав і вольностей Війська Запорозького).
- **PHYSICAL / ARCHIVAL WITNESS**: Оригінальний рукопис староукраїнською діловодною книжною мовою на 19 аркушах, скріплений власноручним підписом Пилипа Орлика та державною печаткою Війська Запорозького на рожевому воску в металевій кустодії.
- **HOLDING INSTITUTION**: Російський державний архів давніх актів (РДАДА, Москва).
- **SHELFMARK**: Фонд 13 (Справи про Польщу і Литву), спр. 10, арк. 1–19.
- **DATE OF WITNESS**: 5 (16) квітня 1710 року.
- **LANGUAGE**: Староукраїнська діловодна книжна мова XVIII ст.
- **DIGITAL REPRESENTATION**: `TRANSCRIPTION` (Паралельний дипломатичний текст преамбули, 16 статей, присяги Орлика та диплома Карла XII).
- **REPRESENTATION SOURCE**:
  - *EDITOR / TRANSCRIBER*: О. Вовк (публікація факсиміле та транскрипції ЦДІАК України, 2010) / редакція Вікіджерел (uk.wikisource).
  - *EDITION / PUBLICATION*: Часопис «Архіви України», 2010, № 3–4, с. 22–66.
  - *PAGE / FOLIO RANGE*: Арк. 1–19.
- **DIRECT LINK TO WITNESS?**: `PARTIAL` (Здійснено через опубліковану архівну транскрипцію ЦДІАК, поаркушна звірка кожної літери агентом не проводилась).
- **TRANSCRIPTION VERIFIED AGAINST FACSIMILE?**: `PARTIAL` (Підтверджено наявність власноручного підпису та печатки; звірено формулювання преамбули та статті 6).
- **TEXTUAL VARIANTS KNOWN?**: `YES` (Відомі різночитання між староукраїнським автографом РДАДА та скороченою латинською копією Riksarkivet).
- **CHAIN OF TRANSMISSION**:
  $$\text{РДАДА ф. 13, спр. 10} \longrightarrow \text{Публ. О. Вовк (ЦДІАК, 2010)} \longrightarrow \text{uk.wikisource} \longrightarrow \text{SRC-ORLYK-1710-UA-TRANSCRIPTION.txt}$$
- **STATUS**: 🟡 `VERIFIED-EDITION` (Транскрипція відповідає авторитетному виданню носія; не плутати з самостійно верифікованим автографом).

---

### 2.2. `WIT-ORLYK-1710-LAT`
- **WITNESS-ID**: `WIT-ORLYK-1710-LAT`
- **WORK**: Contenta Pactorum inter Ducem et Exercitum Zaporoviensem conventorum, in Compendium Brevi Stylo collecta.
- **PHYSICAL / ARCHIVAL WITNESS**: Офіційний дипломатичний скорочений рукопис латинською мовою на пергаментних/паперових аркушах, переданий шведському королю Карлу XII.
- **HOLDING INSTITUTION**: Державний архів Швеції (Riksarkivet, Стокгольм).
- **SHELFMARK**: Дипломатичний фонд «Diplomatica Muscovitica», колекція «Cosacica».
- **DATE OF WITNESS**: Квітень — травень 1710 року.
- **LANGUAGE**: Латинська дипломатична мова ранньомодерної доби.
- **DIGITAL REPRESENTATION**: `TRANSCRIPTION` (Збережено паралельно зі староукраїнським текстом у файлі транскрипції).
- **REPRESENTATION SOURCE**:
  - *EDITOR / TRANSCRIBER*: Н. Молчановський (1898) / О. Бодянський (ЧОИДР, 1847).
  - *EDITION / PUBLICATION*: «Подлинные акты оратора Орлика» / збірка латинських документів Війська Запорозького.
- **DIRECT LINK TO WITNESS?**: `PARTIAL` (Через публікацію Молчановського та шведські описи фонду Cosacica).
- **TRANSCRIPTION VERIFIED AGAINST FACSIMILE?**: `NO` (Безпосередня поаркушна автопсія сканів Riksarkivet не здійснювалась).
- **TEXTUAL VARIANTS KNOWN?**: `YES` (Латинський текст має характер стислого компедіуму порівняно з розлогим староукраїнським автографом).
- **CHAIN OF TRANSMISSION**:
  $$\text{Riksarkivet Cosacica} \longrightarrow \text{Публ. Молчановського (1898)} \longrightarrow \text{uk.wikisource} \longrightarrow \text{SRC-ORLYK-1710-UA-TRANSCRIPTION.txt}$$
- **STATUS**: 🟡 `VERIFIED-EDITION`.

---

### 2.3. `WIT-RP-SHORT`
- **WITNESS-ID**: `WIT-RP-SHORT`
- **WORK**: Правда Роськая (Коротка редакція Руської Правди).
- **PHYSICAL / ARCHIVAL WITNESS**: Академічний рукописний список Новгородського першого літопису молодшого ізводу на пергаменті/папері.
- **HOLDING INSTITUTION**: Бібліотека Російської академії наук (БАН, Санкт-Петербург).
- **SHELFMARK**: Рукописне зібрання БАН, шифр 17.4.9.
- **DATE OF WITNESS**: Перша половина XV століття (близько 1440-х рр.).
- **LANGUAGE**: Давньоруська мова Новгородської традиції.
- **DIGITAL REPRESENTATION**: `TRANSCRIPTION` (Повний текст 43 статей списку).
- **REPRESENTATION SOURCE**:
  - *EDITOR / TRANSCRIBER*: Б. Д. Греков, С. В. Юшков, В. П. Любимов (1940) / М. М. Тихомиров, Б. О. Рибаков (1984).
  - *EDITION / PUBLICATION*: «Российское законодательство X–XX веков». — Т. 1. — М., 1984. — С. 47–49.
  - *PAGE / FOLIO RANGE*: С. 47–49 (за рукописом БАН 17.4.9).
- **DIRECT LINK TO WITNESS?**: `PARTIAL` (Через видання Інституту історії АН СРСР).
- **TRANSCRIPTION VERIFIED AGAINST FACSIMILE?**: `PARTIAL` (Звірено текстовий склад 43 статей із виданням 1940 р.).
- **TEXTUAL VARIANTS KNOWN?**: `YES` (Колація з Археографічним списком тієї ж Короткої редакції).
- **CHAIN OF TRANSMISSION**:
  $$\text{Рукопис БАН 17.4.9 (XV ст.)} \longrightarrow \text{«Правда Русская» (1940) / Рос. закон. (1984)} \longrightarrow \text{ru.wikisource} \longrightarrow \text{SRC-RP-SHORT-ACADEMIC-WITNESS.txt}$$
- **STATUS**: 🟡 `VERIFIED-EDITION` (Фіксує свідок XV ст., а не втрачений автограф Ярослава Мудрого XI ст.).

---

### 2.4. `WIT-RP-EXP`
- **WITNESS-ID**: `WIT-RP-EXP`
- **WORK**: Судъ Ярославль Володимеричь. Правда Русьская (Розширена редакція Руської Правди).
- **PHYSICAL / ARCHIVAL WITNESS**: Троїцький рукописний список у складі великого правничого кодексу «Мірило Праведне».
- **HOLDING INSTITUTION**: Російська державна бібліотека (РДБ, Москва).
- **SHELFMARK**: Фонд 304.I (Зібрання Троїце-Сергієвої лаври), рукопис № 793, арк. 189–205.
- **DATE OF WITNESS**: Друга половина XIV століття (близько 1370–1380-х рр.).
- **LANGUAGE**: Давньоруська мова київсько-володимирської писемної норми.
- **DIGITAL REPRESENTATION**: `TRANSCRIPTION` (Повний текст 121 статті списку).
- **REPRESENTATION SOURCE**:
  - *EDITOR / TRANSCRIBER*: Б. Д. Греков (1940) / «Российское законодательство X–XX веков» (Т. 1, 1984).
  - *EDITION / PUBLICATION*: «Российское законодательство X–XX веков». — Т. 1. — С. 64–73.
  - *PAGE / FOLIO RANGE*: Арк. 189–205 (рукопис № 793); стор. 64–73 видання 1984 р.
- **DIRECT LINK TO WITNESS?**: `PARTIAL` (Через критичне академічне видання).
- **TRANSCRIPTION VERIFIED AGAINST FACSIMILE?**: `PARTIAL` (Звірено нумерацію та текст усіх 121 статей).
- **TEXTUAL VARIANTS KNOWN?**: `YES` (Колація із Синодальним списком Новгородської Керманичої 1282 р. та Пушкінським списком).
- **CHAIN OF TRANSMISSION**:
  $$\text{РДБ ф. 304.I № 793 (XIV ст.)} \longrightarrow \text{Академічне видання АН СРСР (1940/1984)} \longrightarrow \text{ru.wikisource} \longrightarrow \text{SRC-RP-EXP-TROITSKY-WITNESS.txt}$$
- **STATUS**: 🟡 `VERIFIED-EDITION`.

---

### 2.5. `WIT-LS-1566`
- **WITNESS-ID**: `WIT-LS-1566`
- **WORK**: Статутъ Великого князства Литовского 1566 года (Другий / Волинський Статут).
- **PHYSICAL / ARCHIVAL WITNESS**: Комплекс рукописних списків XVI ст. (оскільки Статут 1566 р. не мав сучасного друкованого видання, він побутував виключно в рукописах).
- **HOLDING INSTITUTION**: ЦДІАК України (Київ), БАН Литви (Вільнюс), РНБ (Санкт-Петербург).
- **SHELFMARK**: Рукописні фонди ЦДІАК України, фонд 44 (Колекція рукописних книг).
- **DATE OF WITNESS**: 1566 рік (списки другої половини XVI ст.).
- **LANGUAGE**: «Руська мова» канцелярська Великого Князівства Литовського.
- **DIGITAL REPRESENTATION**: `PARTIAL TRANSCRIPTION (REGISTER-ONLY)` (У файлі міститься повний реєстр розділів, артикулів та королівських привілеїв 1563–1565 рр., але **відсутні повні диспозиції самих статей**).
- **REPRESENTATION SOURCE**:
  - *EDITOR / TRANSCRIBER*: Т. Я. Роговцов (вид. 1855 р.) / Білоруське академічне видання (Мінськ, 2003) / «Ізборник» (litopys.org.ua).
  - *EDITION / PUBLICATION*: «Статут Вялікага княства Літоўскага 1566 года». — Мінск, 2003. — С. 35–263.
- **DIRECT LINK TO WITNESS?**: `NO` (Вторинне веб-відтворення змісту сайтом litopys).
- **TRANSCRIPTION VERIFIED AGAINST FACSIMILE?**: `NO` (Не звірено).
- **TEXTUAL VARIANTS KNOWN?**: `YES` (Списки 1566 року мають численні текстові розбіжності між повітовими копіями).
- **CHAIN OF TRANSMISSION**:
  $$\text{Рукописні списки XVI ст.} \longrightarrow \text{Видання 1855 / Мінськ 2003} \longrightarrow \text{litopys.org.ua} \longrightarrow \text{SRC-LS-1566-TRANSCRIPTION.txt}$$
- **STATUS**: 🟠 `PARTIAL (REGISTER-ONLY)` (КРИТИЧНИЙ ВИСНОВОК: файл не містить розгорнутого тексту статей; його не можна використовувати як першоджерело диспозицій норм без довантаження повного тексту).

---

### 2.6. `WIT-LS-1588`
- **WITNESS-ID**: `WIT-LS-1588`
- **WORK**: Статутъ Великого князства Литовского 1588 года (Третій Литовський Статут).
- **PHYSICAL / ARCHIVAL WITNESS**: Автентичне віленське друковане першовидання 1588 року Друкарні Мамоничів (кириличний стародрук великого формату in-folio).
- **HOLDING INSTITUTION**: Національна бібліотека України ім. В. І. Вернадського (Київ, Відділ стародруків та рідкісних видань).
- **SHELFMARK**: НБУВ Кир. 36 / РНБ / БАН / Бібліотека АН Литви.
- **DATE OF WITNESS**: 1588 рік (привілей Сигізмунда III від 28 січня 1588 р.; вихід у світ літо-осінь 1588 р.).
- **LANGUAGE**: «Руська мова» Великого Князівства Литовського (староукраїнська / старобілоруська канцелярська мова закону).
- **DIGITAL REPRESENTATION**: `CRITICAL TRANSCRIPTION` (Повний текст: Королівський привілей Сигізмунда III, присвята Лева Сапеги, геральдичний вірш Римші, звернення до всіх станів, усі 14 розділів, 488 артикулів; загальний обсяг 1,5 МБ).
- **REPRESENTATION SOURCE**:
  - *EDITOR / TRANSCRIBER*: Академічна транскрипція Інституту філософії і права АН БССР (1989) / Національний центр правової інформації РБ (pravo.by) / be.wikisource.
  - *EDITION / PUBLICATION*: «Статут Вялікага княства Літоўскага 1588: Тэксты. Даведнік. Каментарыі». — Мінск: БелСЭ, 1989.
- **DIRECT LINK TO WITNESS?**: `PARTIAL` (Звірено з академічним відтворенням віленського друку 1588 р.).
- **TRANSCRIPTION VERIFIED AGAINST FACSIMILE?**: `PARTIAL` (Звірено текст Привілею Сигізмунда III та розділу 3 «О волностяхъ шляхетъскихъ»).
- **TEXTUAL VARIANTS KNOWN?**: `YES` (Між трьома послідовними тиражами Мамоничів 1588, 1592–1593 та польським перекладом 1614 р.).
- **CHAIN OF TRANSMISSION**:
  $$\text{Віленське видання Мамоничів (1588)} \longrightarrow \text{Академічне вид. АН БССР (1989)} \longrightarrow \text{pravo.by} \longrightarrow \text{be.wikisource} \longrightarrow \text{SRC-LS-1588-MAMONICZ-TRANSCRIPTION.txt}$$
- **STATUS**: 🟡 `VERIFIED-EDITION` (Повний автентичний текст усіх 14 розділів набуто до `pravda/`).

---

### 2.7. `WIT-HADIACH-COMM-1658`
- **WITNESS-ID**: `WIT-HADIACH-COMM-1658`
- **WORK**: Pakta Hadziackie / Ugoda Hadziacka (Гадяцькі пакти 16 вересня 1658 року).
- **PHYSICAL / ARCHIVAL WITNESS**: Оригінальний рукописний акт комісії під Гадячем, складений польською мовою, підписаний королівськими комісарами Станіславом Казимиром Бенєвським і Казимиром Людвіком Євлашевським з одного боку, та гетьманом Іваном Виговським зі старшиною — з іншого.
- **HOLDING INSTITUTION**: Головний архів давніх актів у Варшаві (AGAD, Archiwum Radziwiłłowskie / Archiwum Koronne).
- **SHELFMARK**: AGAD, dz. II (Polska), t. 34 / копійні книги комісій.
- **DATE OF WITNESS**: 16 вересня 1658 року.
- **LANGUAGE**: Польська мова дипломатичних комісій середини XVII ст.
- **DIGITAL REPRESENTATION**: `TRANSCRIPTION` (Повний текст 6 пунктів преамбули та артикулів комісарської угоди; 22 тис. знаків).
- **REPRESENTATION SOURCE**:
  - *EDITOR / TRANSCRIBER*: Публікація польської археографічної комісії / pl.wikisource (Pakta Hadziackie autentyczne).
  - *EDITION / PUBLICATION*: «Volumina Legum» / збірники польсько-козацьких дипломатичних актів.
- **DIRECT LINK TO WITNESS?**: `PARTIAL` (Через польську археографічну традицію).
- **TRANSCRIPTION VERIFIED AGAINST FACSIMILE?**: `NO`.
- **TEXTUAL VARIANTS KNOWN?**: `YES` (КРИТИЧНО: Цей текст є первинною угодою у військовому таборі, що містить концепцію «Великого Князівства Руського» та повне скасування Берестейської унії).
- **CHAIN OF TRANSMISSION**:
  $$\text{Рукопис табору під Гадячем (1658)} \longrightarrow \text{Польські публікації XVII–XIX ст.} \longrightarrow \text{pl.wikisource} \longrightarrow \text{SRC-HADIACH-1658-COMMISSION-POLISH.txt}$$
- **STATUS**: 🟡 `VERIFIED-EDITION` (Засвідчує первинний комісарський договір, суворо відокремлений від сеймової ревізії 1659 р.).

---

### 2.8. `WIT-HADIACH-SEJM-1659`
- **WITNESS-ID**: `WIT-HADIACH-SEJM-1659`
- **WORK**: Затвердження Гадяцької комісії на Вальному Варшавському Сеймі 1659 року («Kommissya Hadziacka»).
- **PHYSICAL / ARCHIVAL WITNESS**: Офіційні друковані та рукописні сеймові книги конституцій Варшавського сейму 1659 року.
- **HOLDING INSTITUTION**: AGAD (Варшава) / Краківська наукова бібліотека.
- **DATE OF WITNESS**: Травень 1659 року (остаточне затвердження 22 травня 1659 р.).
- **LANGUAGE**: Польська мова закону Речі Посполитої.
- **DIGITAL REPRESENTATION**: Очікує вивантаження з Volumina Legum.
- **REPRESENTATION SOURCE**:
  - *EDITION / PUBLICATION*: «Volumina Legum: przedruk zbioru praw staraniem XX. Pijarów w Warszawie, od roku 1732 do 1782, wydanego». — Wyd. Jozafata Ohryzki. — Petersburg, 1859. — T. IV. — S. 297–301.
- **DIRECT LINK TO WITNESS?**: `PENDING`.
- **TEXTUAL VARIANTS KNOWN?**: `YES` (Сеймова конституція вилучила скасування Берестейської унії, обмежила право гетьмана на дипломатичні зносини, урізала реєстр до 30 тис. і повернула приватні шляхетські маєтності).
- **STATUS**: ⚪ `UNVERIFIED (DIGITAL PENDING)` (Фізичне джерело ідентифіковане у Volumina Legum T. IV, с. 297–301; цифровий текст артикулів у репозиторії pravda ще не завантажений).

---

### 2.9. `WIT-ZBORIV-1649` (ДОГОВІРНИЙ КОМПЛЕКС)
- **WITNESS-ID**: `WIT-ZBORIV-1649`
- **WORK**: Зборівський комплекс актів 1649 року.
- **NOTE ON NATURE OF DOCUMENT**: **НЕ ІСНУЄ єдиного документа з назвою «Зборівський договір»**. Комплекс складається з чотирьох самостійних пам'яток з різною юридичною природою:
  1. `WIT-ZBORIV-1649-DECLARATION`: «Декларація ласки Його Королівської Милості на пункти супліки Війська Запорозького» (жалувана грамота короля Яна II Казимира від 8 (18) серпня 1649 р., 12 артикулів; збережена в AGAD Metryka Koronna та списках РДАДА; видання: АЮЗР Т. III, с. 415–416; Бантиш-Каменський Ч. I, с. 19–20).
  2. `WIT-ZBORIV-1649-PETITION`: Пункти супліки Війська Запорозького до короля (петиція козацької старшини; копійні списки в дипломатичній кореспонденції).
  3. `WIT-ZBORIV-1649-KHAN-TREATY`: Мирна угода короля з кримським ханом Іслам-Гіреєм III (міжнародний договір про данину/упоминки та зняття облоги).
  4. `WIT-ZBORIV-1649-REGISTER`: Реєстр Війська Запорозького 1649 року (рукописна книга на 40 000 імен у РДАДА ф. 229, оп. 2, спр. 1; видання О. Бодянського 1875 р., акад. видання 1995 р.).
- **DIGITAL REPRESENTATION**: `STRUCTURAL ANALYSIS & METADATA DECONSTRUCTION` (`sources/primary/transcriptions/SRC-ZBORIV-1649-COMPLEX-ANALYSIS.txt`).
- **STATUS**: 🔴 `DISPUTED (MULTI-DOC COMPLEX)` (Використання терміна без уточнення складового документа суворо заборонено).

---

### 2.10. `WIT-MARCH-1654`
- **WITNESS-ID**: `WIT-MARCH-1654-POSOLSKIY`
- **WORK**: Березневі статті 1654 року («Статті Богдана Хмельницького» з підстатейними царськими указами).
- **PHYSICAL / ARCHIVAL WITNESS**: Скорописний канцеляристський список Посольського приказу XVII ст.
- **HOLDING INSTITUTION**: РДАДА (Москва).
- **SHELFMARK**: Фонд 229 (Малоросійські справи), спр. 9.
- **DATE OF WITNESS**: 21 (31) березня 1654 року.
- **LANGUAGE**: Російська діловодна приказна мова XVII ст.
- **CRITICAL DEFECT OF TRANSMISSION**: **Оригінальний український текст проєкту (петиції), підписаний і запечатаний Богданом Хмельницьким (23 або 14 статей), ВТРАЧЕНО**. Ми володіємо виключно московським приказним реєстром 11 статей, перекладеним і зредагованим дяками під час переговорів Самійла Богданова і Павла Тетері.
- **LATER FALSIFICATION TRADITION**: У 1659 році московські посли (кн. Трубецькой) на Переяславській раді під виглядом «автентичних статей Богдана Хмельницького 1654 року» нав'язали Юрію Хмельницькому сфальсифікований текст із 14 статей, що різко обмежував автономію Гетьманщини (заборона переобрання гетьмана без царя, воєводи в Переяславі, Ніжині, Чернігові).
- **DIGITAL REPRESENTATION**: `TRANSCRIPTION` (Повний текст 11 статей з царськими указами у файлі `sources/primary/transcriptions/SRC-MARCH-1654-POSOLSKIY-TRANSCRIPTION.txt`).
- **REPRESENTATION SOURCE**:
  - *EDITION / PUBLICATION*: «Воссоединение Украины с Россией. Документы и материалы в трех томах». — М.: Изд-во АН СССР, 1953. — Т. III. — Док. № 108. — С. 560–567.
  - *EARLIER OFFICIAL PRINT*: «Полное собрание законов Российской империи» (ПСЗРИ-1). — СПб., 1830. — Т. I. — № 119.
- **CHAIN OF TRANSMISSION**:
  $$\text{Петиція послів (березень 1654)} \longrightarrow \text{РДАДА ф. 229, спр. 9} \longrightarrow \text{АН СССР (1953, № 108)} \longrightarrow \text{ru.wikisource} \longrightarrow \text{SRC-MARCH-1654-POSOLSKIY-TRANSCRIPTION.txt}$$
- **STATUS**: 🟡 `VERIFIED-EDITION-OF-COPY` (Верифіковано московський копійний список 11 статей; первинний український оригінал відсутній).

---

## 3. СТАТИСТИЧНИЙ ПІДСУМОК ПЕРШОЇ ХВИЛІ

- **Всього пам'яток у першій хвилі**: 10.
- **Повні первинні тексти, набуті на рівні `VERIFIED-EDITION`**: **6** (`WIT-ORLYK-1710-UA`, `WIT-ORLYK-1710-LAT`, `WIT-RP-SHORT`, `WIT-RP-EXP`, `WIT-LS-1588`, `WIT-HADIACH-COMM-1658`).
- **Тексти копій за втраченими оригіналами (`VERIFIED-EDITION-OF-COPY`)**: **1** (`WIT-MARCH-1654-POSOLSKIY`).
- **Дефектні або часткові представлення (`PARTIAL (REGISTER-ONLY)`)**: **1** (`WIT-LS-1566`, виявлено відсутність тексту диспозицій).
- **Багатодокументні розчленовані комплекси (`DISPUTED (MULTI-DOC COMPLEX)`)**: **1** (`WIT-ZBORIV-1649`, деконструйовано на 4 акти).
- **Ідентифіковано, але очікує цифрового вивантаження артикулів (`UNVERIFIED (DIGITAL PENDING)`)**: **1** (`WIT-HADIACH-SEJM-1659`, Volumina Legum T. IV, s. 297–301).
- **Вторинні сурогати (Вікіпедія / реферати), ізольовані в `legacy-imports/`**: **13 файлів** (жоден не видалено).
