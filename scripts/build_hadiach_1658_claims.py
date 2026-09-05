import re

with open("/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-1658-COMMISSION-DIPLOMATIC.txt", "r", encoding="utf-8") as f:
    text = f.read()

body = text.split("================================================================================")[1]
lines = body.split("\n")

def clean_txt(t):
    return t.replace("<br>", "").strip()

items = [
    # Preamble
    {
        "id": "HC-HAD1658-PRE-001",
        "locator": "Преамбула, Рядки 22–24",
        "speaker": "JOINT FORMULA",
        "quote": f"{clean_txt(lines[12])} {clean_txt(lines[13])} {clean_txt(lines[14])} {clean_txt(lines[15])}",
        "terms": "Komisja, Korony Polskiej i Wielkiego Księstwa Litewskiego, Hetmanem i Wojskiem Zaporoskim, Komisarzów, w obozie pod Hadziaczem, obrony swojej przystąpiło, do jedności, pokój wieczny",
        "actor": "Комісари Корони й ВКЛ (Бєньовський, Євлашевський); Гетьман Іван Виговський і Військо Запорозьке",
        "operator": "CONCLUDES / DECLARES",
        "object": "Укладення вічного миру між Станами Корони Польської і Великого Князівства Литовського та Військом Запорозьким у таборі під Гадячем після військового протистояння."
    },
    # Art 1
    {
        "id": "HC-HAD1658-001A",
        "locator": "Стаття 1, Рядок 26",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[16])[3:], # strip "1. "
        "terms": "Religia grecka starożytna, starożytna Ruś, prerogatywach, wolnym używaniu nabożeństwa, język narodu ruskiego, procesjach, obrządek rzymski",
        "actor": "Королівська влада; церква та вірні грецької релігії",
        "operator": "CONFIRMS / GUARANTEES",
        "object": "Збереження за давньою грецькою релігією її прерогатив і вільного відправлення богослужінь у містах і селах Корони й ВКЛ, на Сеймах, у війську й Трибуналах нарівні з римським обрядом."
    },
    {
        "id": "HC-HAD1658-001B",
        "locator": "Стаття 1, Рядок 27",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[17]),
        "terms": "religii greckiej, wolnego erygowania cerkwi, zakonów, monastyrów, ponawiania i naprawiania",
        "actor": "вірні та духовні грецької релігії",
        "operator": "PERMITS",
        "object": "Надання права вільно засновувати нові церкви, монастирі й ордени, а також відновлювати й ремонтувати старі."
    },
    {
        "id": "HC-HAD1658-001C",
        "locator": "Стаття 1, Рядок 28",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[18]),
        "terms": "cerkwi i dóbr, religii greckiej starożytnej fundowanych, greccy starożytni prawosławni, przysięgi na wierność, pułkowników i inszą starszyznę, Komisarzów",
        "actor": "грецькі православні (graeci disuniti); полковники та старшина Війська Запорозького; спільні комісари",
        "operator": "REQUIRES / RESTORES",
        "object": "Залишення церков і давніх церковних маєтностей за православними; передача їх комісарами обох сторін протягом пів року після складання присяги на вірність полковниками й старшиною."
    },
    {
        "id": "HC-HAD1658-001D",
        "locator": "Стаття 1, Рядок 29",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[19]),
        "terms": "Unia znosi się, rzymskiego nabożeństwa, greckiego unitskiego, żaden z duchownego i świeckiego cerkwi nie ma fundować, rzymska wiara liberum exercitium conceditur",
        "actor": "духовні й світські стани; вірні грецького та римського обрядів",
        "operator": "PROHIBITS / PERMITS / ABOLISHES",
        "object": "Скасування унії в Короні та ВКЛ; надання вибору переходу до римського чи уніатського обряду; довічна заборона засновувати церкви протилежної віри; дозвіл вільного відправлення римської віри в Київському, Брацлавському й Чернігівському воєводствах."
    },
    {
        "id": "HC-HAD1658-001E",
        "locator": "Стаття 1, Рядок 30",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[20]),
        "terms": "Panowie świeccy, urzędnicy religii rzymskiej, żadnej jurysdycji mieć nie będą, duchownymi, świeckimi i zakonnikami religii greckiej, prócz należnego pasterza",
        "actor": "пани світські та урядники римської релігії; духовні й монахи грецької релігії",
        "operator": "PROHIBITS",
        "object": "Заборона світським дідичам та урядникам римської релігії здійснювати юрисдикцію над духовними, світськими особами та монахами грецької релігії (підлягають лише власному пастирю)."
    },
    {
        "id": "HC-HAD1658-001F",
        "locator": "Стаття 1, Рядок 31",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[21]),
        "terms": "Metropolita Kijowski, czterema władykami, piątym z W. X. Litewskiego, w Senacie zasiadać ma, libera vocio usu, ritus romani, po Arcybiskupie Lwowskim",
        "actor": "Митрополит Київський; чотири єпископи (луцький, львівський, перемишльський, холмський); єпископ мстиславський",
        "operator": "REQUIRES / CONFIRMS",
        "object": "Надання Київському митрополиту та 5 владикам місць і права голосу в Сенаті нарівні з римо-католицьким духовенством із визначенням порядку старшинства."
    },
    {
        "id": "HC-HAD1658-001G",
        "locator": "Стаття 1, Рядок 32",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[22]),
        "terms": "dygnitarstwa senatorskie, szlachcie obrządku greckiego, alternatio, post decessum, mieszkają tam i mają dobra",
        "actor": "шляхта грецького обряду; шляхта римського обряду; король",
        "operator": "REQUIRES / RESERVES",
        "object": "Надання сенаторських гідностей у Київському воєводстві лише осілій шляхті грецького обряду; чергування (alternatio) сенаторських посад між грецьким і римським обрядами у Брацлавському та Чернігівському воєводствах."
    },
    {
        "id": "HC-HAD1658-001H",
        "locator": "Стаття 1, Рядок 33",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[23]),
        "terms": "Hetman dla Wojsk Ruskich, pierwszym senatorem, wszystka jurysdykcja kijowska, nastawienie podwojewodzego i innych urzędników",
        "actor": "Гетьман Військ Руських",
        "operator": "CONFIRMS / RESERVES",
        "object": "Визнання Гетьмана Військ Руських першим сенатором у трьох воєводствах та надання йому повної київської юрисдикції, включно з призначенням підвоєводи й інших урядників, до набуття володіння воєводством."
    },
    {
        "id": "HC-HAD1658-001I",
        "locator": "Стаття 1, Рядок 34",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[24]),
        "terms": "mieszczanie rzymscy, religii greckiej, spólnej wolności swobód, żadnemu religia grecka do Magistratu przeszkodą być nie ma",
        "actor": "міщани римської та грецької релігії",
        "operator": "CONFIRMS / PROHIBITS",
        "object": "Зрівняння міщан грецького й римського обрядів у міських вольностях і свободах у Короні та ВКЛ; заборона вважати грецьку релігію перешкодою для доступу до магістрату."
    },
    {
        "id": "HC-HAD1658-001J",
        "locator": "Стаття 1, Рядок 35",
        "speaker": "CROWN SIDE",
        "quote": clean_txt(lines[25]),
        "terms": "Akademię w Kijowie erygować, prerogatywami i wolnościami, jako Akademia Krakowska, żadnych sekt ariańskiej kalwińskiej luterskiej, insze szkoły przenieść",
        "actor": "Його Королівська Милість; Стани Коронні; Київська академія",
        "operator": "PERMITS / PROHIBITS",
        "object": "Дозвіл на заснування Академії в Києві з правами й вольностями Краківської академії за умови недопущення аріанських, кальвінських і лютеранських викладачів і студентів; перенесення інших шкіл з Києва."
    },
    {
        "id": "HC-HAD1658-001K",
        "locator": "Стаття 1, Рядок 36",
        "speaker": "CROWN SIDE",
        "quote": clean_txt(lines[26]),
        "terms": "Drugą także Akademię pozwala, gdzie jej miejsce sposobne upatrzą, praw i wolności, bez sekt ariańskiej kalwińskiej i luterskiej, żadne insze szkoły erygowane nie będą",
        "actor": "Його Королівська Милість; Стани Коронні та ВКЛ",
        "operator": "PERMITS / PROHIBITS",
        "object": "Дозвіл на заснування другої Академії у відповідному місці з тими самими правами й антисектантськими умовами та забороною відкривати поруч інші школи."
    },
    {
        "id": "HC-HAD1658-001L",
        "locator": "Стаття 1, Рядок 37",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[27]),
        "terms": "Gimnazja kollegia szkoły i drukarnie, bez trudności stanowić wolno, księgi drukować in controversiis religionum, nie obrażając Majestatu Króla",
        "actor": "засновники шкіл і друкарень",
        "operator": "PERMITS / PROHIBITS",
        "object": "Дозвіл вільно відкривати гімназії, колегії, школи й друкарні та друкувати релігійно-полемічні книги без образ королівського маєстату й пасквілів."
    },
    # Art 2
    {
        "id": "HC-HAD1658-002A",
        "locator": "Стаття 2, Рядок 39",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[29])[3:], # strip "2. "
        "terms": "odstępując postronnych protekcji powraca, wieczną amnistią, zapomnieniem wiecznym pokrywa, asekurując wszelkiej kondycji ludzi, żadnej zemsty, sercem chrześcijańskim, bona fide",
        "actor": "Король; Стани Корони й ВКЛ; Гетьман і Військо Запорозьке; шляхта й приватні особи",
        "operator": "PARDONS / PROHIBITS / GUARANTEES",
        "object": "Оголошення вічної амністії й повного забуття воєнних дій для всіх станів і учасників; взаємна відмова від помсти й звільнення від обов'язків за попередніми союзами."
    },
    {
        "id": "HC-HAD1658-002B",
        "locator": "Стаття 2, Рядок 40",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[30]),
        "terms": "kaduki wszystkie, Wojska Zaporoskiego, pod szlachtą przy Szwedach, skasowane, pro cassatio, z ksiąg eliminatis, własnym possesorom wolno zawładnąć, sub paena infamia",
        "actor": "посідачі кадуків; законні власники дібр; судова влада",
        "operator": "ABOLISHES / RESTORES / PROHIBITS",
        "object": "Касація всіх прав на конфісковані маєтності (кадуки), наданих під час війни проти козаків і шляхти; повернення майна законним власникам під загрозою інфамії."
    },
    {
        "id": "HC-HAD1658-002C",
        "locator": "Стаття 2, Рядок 41",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[31]),
        "terms": "imię aministiej święte, in pristinum statum res et persona restituntur, zarzucić zdradę śmiał, ukarany za naruszenie ugody, inquisitia z obu rąk",
        "actor": "усі особи; органи слідства обох сторін",
        "operator": "PROTECTS / PROHIBITS / REQUIRES",
        "object": "Недоторканність амністії; відновлення осіб і майна у попередньому статусі; суворе покарання за публічні чи приватні звинувачення у зраді зі спільним розслідуванням наклепів."
    },
    {
        "id": "HC-HAD1658-002D",
        "locator": "Стаття 2, Рядок 42",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[32]),
        "terms": "Rzeczpospolita Narodu Polskiego i W. X. Litewskiego i Ruskiego, restituantur in integrum, w granicach swoich i swobodach, wolnej elekcji, jedno ciało jednej i nierozdzielnej Rzeczypospolitej, bez różnicy o wiarę",
        "actor": "Народи Польський, Литовський і Руський; Річ Посполита",
        "operator": "RESTORES / CONFIRMS / GUARANTEES",
        "object": "Відновлення трьох народів у кордонах і свободах як єдиного тіла нероздільної Речі Посполитої зі збереженням рад, судів, вільної елекції королів та релігійного миру."
    },
    # Art 3
    {
        "id": "HC-HAD1658-003A",
        "locator": "Стаття 3, Рядок 44",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[34])[3:], # strip "3. "
        "terms": "Wojska Zaporoskiego liczba trzydzieści tysięcy, sześćdziesiąt tysięcy, na Regestrze poda",
        "actor": "Військо Запорозьке; Гетьман Запорозький",
        "operator": "DETERMINES",
        "object": "Встановлення чисельності козацького компуту (реєстру) у 30 000 або 60 000 осіб за поданням Гетьмана."
    },
    {
        "id": "HC-HAD1658-003B",
        "locator": "Стаття 3, Рядок 45",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[35]),
        "terms": "Zaciągowego wojska dziesięć tysięcy, pod władzą Hetmana, z podatków na Sejmie uchwalonych",
        "actor": "Гетьман; наймане військо; Сейм",
        "operator": "ESTABLISHES / REQUIRES",
        "object": "Формування 10 000 найманого війська під командуванням Гетьмана з утриманням із сеймових податків трьох воєводств."
    },
    {
        "id": "HC-HAD1658-003C",
        "locator": "Стаття 3, Рядок 46",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[36]),
        "terms": "Kwatery Wojsku Zaporoskiemu, wolności przywilejami nadane konfirmuje, żaden dzierżawca starosta podatków wyciągać nie będą, ludzie rycerscy, wolni od ceł myt, od sądów starostów wolni, pod jurysdykcją hetmana, napoje łowy pożytki",
        "actor": "козаки Війська Запорозького; старости, орендарі, дідичі; Гетьман",
        "operator": "CONFIRMS / EXEMPTS / PROHIBITS",
        "object": "Підтвердження традиційних квартир і вольностей козаків як лицарських людей; повне звільнення від податків, мит і юрисдикції старост та поміщиків із підпорядкуванням виключно гетьманському суду; збереження промислів."
    },
    {
        "id": "HC-HAD1658-003D",
        "locator": "Стаття 3, Рядок 47",
        "speaker": "CROWN SIDE",
        "quote": clean_txt(lines[37]),
        "terms": "Hetman Wojsk Ruskich prezentować będzie, nobilitacja z nadaniem wszelakich wolności szlacheckich, z każdego pułku sto",
        "actor": "Його Королівська Милість; Гетьман Військ Руських; козаки, що нобілітуються",
        "operator": "PERMITS / CONFERS",
        "object": "Надання шляхетства з усіма вольностями за поданням Гетьмана з розрахунку до 100 осіб від кожного козацького полку."
    },
    {
        "id": "HC-HAD1658-003E",
        "locator": "Стаття 3, Рядок 48",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[38]),
        "terms": "Wojsk żadnych polskich litewskich cudzoziemskich nikt prowadzić nie ma, posiłki koronne pod regimentem Hetmana Wojsk Ruskich",
        "actor": "коронні, литовські та іноземні війська; Гетьман Військ Руських",
        "operator": "PROHIBITS / SUBORDINATES",
        "object": "Заборона вводити коронні, литовські чи чужоземні війська у три воєводства; підпорядкування можливих коронних допоміжних військ Гетьману Руському у разі війни."
    },
    # Art 4
    {
        "id": "HC-HAD1658-004A",
        "locator": "Стаття 4, Рядок 50",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[40])[3:].strip(), # strip "4. "
        "terms": "Hetman Wojsk Ruskich do końca życia swego, pierwszym senatorem, wolne obieranie hetmana, czterech elektorów, braci hetmana",
        "actor": "Іван Виговський; чотири електори трьох воєводств; король",
        "operator": "CONFIRMS / ESTABLISHES",
        "object": "Довічне збереження гетьманства та першого сенаторського місця за Виговським; встановлення вільного обрання наступних гетьманів чотирма електорами від воєводств із правом балотування братів гетьмана."
    },
    {
        "id": "HC-HAD1658-004B",
        "locator": "Стаття 4, Рядок 51",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[41]),
        "terms": "Mennica dla bicia wszelakich pieniędzy w Kijowie, wedle jednej ligii i z osobą królewską",
        "actor": "монетний двір; король",
        "operator": "PERMITS / REQUIRES",
        "object": "Дозвіл відкрити монетний двір у Києві для карбування монети єдиної стопи з королівським зображенням."
    },
    {
        "id": "HC-HAD1658-004C",
        "locator": "Стаття 4, Рядок 52",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[42]),
        "terms": "Spólna rada i spólne siły przeciw każdemu nieprzyjacielowi, wolna nawigacja na Czarne Morze",
        "actor": "три народи Речі Посполитої",
        "operator": "REQUIRES / ASPIRES",
        "object": "Зобов'язання спільної ради й оборони трьох народів проти ворогів та спільних зусиль для забезпечення вільного судноплавства Чорним морем."
    },
    {
        "id": "HC-HAD1658-004D",
        "locator": "Стаття 4, Рядок 53",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[43]),
        "terms": "car moskiewski prowincji nie zechce, siły koronne litewskie i Wojska Ruskie Zaporoskie pod regimentem Hetmana swego łączyć się",
        "actor": "цар московський; коронні, литовські та запорозькі війська",
        "operator": "REQUIRES",
        "object": "Обов'язок спільних воєнних дій коронних, литовських і запорозьких сил під проводом власного гетьмана у разі відмови царя повернути провінції або нападу на Річ Посполиту."
    },
    {
        "id": "HC-HAD1658-004E",
        "locator": "Стаття 4, Рядок 54",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[44]),
        "terms": "Dobra królewszczyzny sumy pieniężne, obywatelów ruskiej ziemi, konfiskowane przywrócone być mają, zasługi w wojsku kompensowane i zapłacone",
        "actor": "повернені обивателі руської землі; скарб",
        "operator": "RESTORES / COMPENSATES",
        "object": "Повернення конфіскованих маєтностей і сум особам, що повертаються до Речі Посполитої; виплата винагороди за військову службу нарівні з іншими військами."
    },
    # Art 5
    {
        "id": "HC-HAD1658-005A",
        "locator": "Стаття 5, Рядок 56",
        "speaker": "COSSACK SIDE",
        "quote": clean_txt(lines[46])[3:].strip(), # strip "5. "
        "terms": "odstąpiwszy wszelakich postronnych protekcji, wierności poddaństwie i posłuszeństwie Najjaśniejszego Majestatu i Rzeczypospolitej",
        "actor": "Гетьман і Військо Запорозьке; Його Королівська Милість",
        "operator": "RENNOUNCES / PLEDGES",
        "object": "Відмова від будь-яких сторонніх протекцій та обіцянка вічної вірності, підданства й послуху польському королю та всій Речі Посполитій."
    },
    {
        "id": "HC-HAD1658-005B",
        "locator": "Стаття 5, Рядок 57",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[47]),
        "terms": "Nie derogując braterstwu z Chanem Krymskim, salua integritate Reipublica, z carem moskiewskim",
        "actor": "Гетьман і Військо Запорозьке; Кримський хан; Московський цар",
        "operator": "RESERVES / PERMITS",
        "object": "Збереження братерського союзу з Кримським ханом і можливість миру з Московським царем за умови збереження цілісності Речі Посполитої."
    },
    {
        "id": "HC-HAD1658-005C",
        "locator": "Стаття 5, Рядок 58",
        "speaker": "COSSACK SIDE",
        "quote": clean_txt(lines[48]),
        "terms": "Legacji żadnych od postronnych przyjmować nie ma, do Jego Królewskiej Mości odsyłać będzie",
        "actor": "Гетьман Запорозький; іноземні посли",
        "operator": "PROHIBITS / REQUIRES",
        "object": "Заборона приймати іноземні посольства та обов'язок відсилати їх до короля."
    },
    {
        "id": "HC-HAD1658-005D",
        "locator": "Стаття 5, Рядок 59",
        "speaker": "COSSACK SIDE",
        "quote": clean_txt(lines[49]),
        "terms": "ani wojsk postronnych wprowadzać, porozumienia mieć na szkodę Rzeczypospolitej, z dokładem Jego Królewskiej Mości",
        "actor": "Гетьман Запорозький",
        "operator": "PROHIBITS / RESERVES",
        "object": "Заборона вводити чужі війська й вести переговори на шкоду Речі Посполитій без відома й дозволу короля."
    },
    # Art 6
    {
        "id": "HC-HAD1658-006A",
        "locator": "Стаття 6, Рядок 61",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[51])[3:].strip(), # strip "6. "
        "terms": "Primatis duchownym obrządku rzymskiego, świeckim z obojej strony do dóbr dziedzicznych starostw dzierżaw, bezpieczny powrót i reinductio",
        "actor": "римо-католицьке духовенство; світські дідичі й орендарі обох сторін",
        "operator": "PERMITS / RESTORES",
        "object": "Відкриття безпечного повернення (реіндукції) католицького духовенства та світських дідичів обох сторін до своїх маєтностей і староств у чотирьох воєводствах, ВКЛ, Білій Русі та Сіверщині."
    },
    {
        "id": "HC-HAD1658-006B",
        "locator": "Стаття 6, Рядок 62",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[52]),
        "terms": "Czas powrócenia i rendukcji naznaczyć ma, za uniwersałem Króla i Hetmana, wzajemne porozumienie",
        "actor": "Його Королівська Милість; Гетьман Запорозький",
        "operator": "REQUIRES / RESERVES",
        "object": "Встановлення порядку й термінів повернення виключно за спільними універсалами та узгодженням короля й гетьмана."
    },
    {
        "id": "HC-HAD1658-006C",
        "locator": "Стаття 6, Рядок 63",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[53]),
        "terms": "dla rozsądzenia spraw kryminalnych potocznych, osobliwy trybunał, owruckie i żytomierskie starostwa sądowe",
        "actor": "козаки; трибунал трьох воєводств",
        "operator": "ESTABLISHES / PERMITS",
        "object": "Створення окремого судового трибуналу для кримінальних і поточних справ у трьох воєводствах за обраним ними самими порядком, а також судових староств в Овручі та Житомирі."
    },
    {
        "id": "HC-HAD1658-006D",
        "locator": "Стаття 6, Рядок 64",
        "speaker": "CROWN SIDE",
        "quote": clean_txt(lines[54]),
        "terms": "narodowi ruskiemu osobnych Pieczętarzów, Marszałków i Podskarbich, godności senatorskie, nic przeciwnego postanowieniu pieczętować nie będą",
        "actor": "Його Королівська Милість і Річ Посполита; урядники руського народу (Печатники, Маршалки, Підскарбії)",
        "operator": "PERMITS / REQUIRES / PROHIBITS",
        "object": "Надання руському народові окремих вищих урядників (Печатників, Маршалків, Підскарбіїв) із сенаторською гідністю та забороною скріплювати печаткою будь-які акти, що суперечать угоді."
    },
    {
        "id": "HC-HAD1658-006E",
        "locator": "Стаття 6, Рядок 65",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[55]),
        "terms": "do Pieczętarzów urzędu i kancelarii należeć będą, duchowne greckie beneficja, sądy z miast królewskich dekreta zadworne i sejmowe",
        "actor": "Печатники та Канцелярія Руська; король",
        "operator": "DELIMITS / RESERVES",
        "object": "Підпорядкування Руській канцелярії справ грецьких бенефіцій у шести воєводствах, а також міських, задвірних і сеймових судів трьох воєводств."
    },
    {
        "id": "HC-HAD1658-006F",
        "locator": "Стаття 6, Рядок 66",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[56]),
        "terms": "przeciwnego z Kancelarii Koronnej albo Litewskiej nieważne, paenae dziesięciu tysięcy kop litewskich, sąd przed Królem",
        "actor": "Канцелярія Коронна; Канцелярія Литовська; порушники привілеїв; король",
        "operator": "ANNULS / PENALIZES",
        "object": "Визнання недійсними будь-яких актів коронної чи литовської канцелярій усупереч цій угоді та покарання порушників штрафом у 10 000 кіп литовських через суд перед королем."
    },
    {
        "id": "HC-HAD1658-006G",
        "locator": "Стаття 6, Рядок 67",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[57]),
        "terms": "procesy względem poddanych o swawolę, najazdów zaborów szkód skasowane, ziemskie grodzkie trybunalskie",
        "actor": "суди земські, гродські, трибунальські; шляхта й піддані",
        "operator": "ABOLISHES",
        "object": "Касація всіх судових позовів і вироків проти підданих за звинуваченнями у с сваволі, наїздах, пограбуваннях та збитках воєнного часу в чотирьох воєводствах."
    },
    {
        "id": "HC-HAD1658-006H",
        "locator": "Стаття 6, Рядок 68",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[58]),
        "terms": "Z carem Moskiewskim do zawarcia pakt, indemnitas reputacji, teraźniejszego postanowienia praecament",
        "actor": "король і Стани; цар московський; Гетьман і Військо Запорозьке",
        "operator": "REQUIRES",
        "object": "Вимога обов'язкового збереження честі й умов цієї угоди для Гетьмана й Війська Запорозького у разі майбутнього укладення миру з Московським царем."
    },
    # Concluding Clauses
    {
        "id": "HC-HAD1658-CONCL-001",
        "locator": "Заключні статті, Рядок 70",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[60]),
        "terms": "przysięgą potwierdzili, przysięgą cielesną z Senatu przez Arcybiskupa Prymasa i Biskupa Wileńskiego, czterech Hetmanow i Pieczętarzow, Marszałka na Sejmie",
        "actor": "Комісари; Гетьман Виговський; Примас, єпископи, гетьмани, печатарі, маршалок посольської ізби",
        "operator": "PLEDGES / REQUIRES",
        "object": "Складення присяги комісарами та гетьманом на місці; зобов'язання підтвердження присягою сенаторів, чотирьох гетьманів, печатарів і маршалка на найближчому Сеймі."
    },
    {
        "id": "HC-HAD1658-CONCL-002",
        "locator": "Заключні статті, Рядок 71",
        "speaker": "CROWN SIDE",
        "quote": clean_txt(lines[61]),
        "terms": "przysięgi Jego Królewskiej Mości, uczynić raczy, Komisarze ascecurują",
        "actor": "Його Королівська Милість; пани Комісари",
        "operator": "PLEDGES / GUARANTEES",
        "object": "Порука королівських комісарів щодо складання присяги королем на прохання Війська Запорозького."
    },
    {
        "id": "HC-HAD1658-CONCL-003",
        "locator": "Заключні статті, Рядок 72",
        "speaker": "COSSACK SIDE",
        "quote": clean_txt(lines[62]),
        "terms": "Przysięgi pułkowników, setników i wszystkiej starszyzny Wojska Zaporoskiego po Sejmie",
        "actor": "полковники, сотники та вся старшина Війська Запорозького; призначені комісари",
        "operator": "PLEDGES / REQUIRES",
        "object": "Обов'язок складення присяги полковниками, сотниками та всією козацькою старшиною після Сейму перед призначеними комісарами."
    },
    {
        "id": "HC-HAD1658-CONCL-004",
        "locator": "Заключні статті, Рядок 73",
        "speaker": "JOINT FORMULA",
        "quote": clean_txt(lines[63]),
        "terms": "wieczną wagę miała, w prawo pospolite w konstytucję włączona, Sejmem aprobowana, za wieczne nieodzowne prawo",
        "actor": "Сейм Речі Посполитої",
        "operator": "REQUIRES / RATIFIES",
        "object": "Вимога включення всього тексту комісії без змін до сеймової конституції як вічного й непорушного загальнодержавного права."
    },
    {
        "id": "HC-HAD1658-CONCL-005",
        "locator": "Заключні статті, Рядок 74",
        "speaker": "COMMISSION",
        "quote": clean_txt(lines[64]),
        "terms": "Do Buławy Wielkiej Ruskiej, czehryńskie starostwo, w przywileju Bohdana Chmielnickiego conferowanym",
        "actor": "Булава Велика Руська; Богдан Хмельницький",
        "operator": "CONFIRMS / ATTACHES",
        "object": "Закріплення Чигиринського староства за посадою гетьмана (Великою Руською булавою) за привілеєм Богдана Хмельницького."
    },
    {
        "id": "HC-HAD1658-CONCL-006",
        "locator": "Заключні статті, Рядок 75",
        "speaker": "CROWN SIDE",
        "quote": clean_txt(lines[65]),
        "terms": "Hetman Wojsk Ruskich od rezydencji przy Jego Królewskiej Mości ma być wolny",
        "actor": "Гетьман Військ Руських",
        "operator": "EXEMPTS",
        "object": "Звільнення Гетьмана Військ Руських від обов'язку постійної резиденції при королівському дворі."
    },
    {
        "id": "HC-HAD1658-CONCL-007",
        "locator": "Заключні статті, Рядок 76",
        "speaker": "CROWN SIDE",
        "quote": clean_txt(lines[66]),
        "terms": "Convocatia województwom kijowskiemu, bracławskiemu, czernihowskiemu po Sejmie uniwersałem",
        "actor": "Його Королівська Милість; обивателі трьох воєводств",
        "operator": "REQUIRES",
        "object": "Обов'язок скликання королівським універсалом конвокації трьох воєводств після сейму."
    },
    {
        "id": "HC-HAD1658-CONCL-008",
        "locator": "Підпис і датування, Рядки 77–80",
        "speaker": "COSSACK SIDE",
        "quote": f"{clean_txt(lines[67])} / - / {clean_txt(lines[69])} {clean_txt(lines[70])}",
        "terms": "w taborze pod Hadziaczem, Jan Wyhowski hetman wojsk Zaporowskich ręką własną",
        "actor": "Іван Виговський, гетьман військ Запорозьких",
        "operator": "SIGNS / SEALS",
        "object": "Особистий власноручний підпис і печатка гетьмана Івана Виговського від імені всього Війська Запорозького в таборі під Гадячем 16 вересня 1658 р."
    }
]

print(f"Total extracted items: {len(items)}")

forbidden = [
    "суверенітет", "sovereignty", "автономія", "autonomy", "сегрегація", "segregation",
    "дискримінація", "discrimination", "права меншин", "minority rights", "національні права",
    "демократія", "democracy", "окупація", "occupation", "федерація", "federation",
    "конфедерація", "confederation", "релігійна свобода", "religious freedom",
    "національна держава", "national state", "публічний бюджет", "public budget",
    "монарх", "monarch", "правовий статус", "піддані як громадяни"
]

all_clean = True
for it in items:
    blob = f"{it['terms']} {it['actor']} {it['object']}"
    for f_term in forbidden:
        if re.search(r'\b' + re.escape(f_term) + r'\b', blob, re.IGNORECASE):
            print(f"FORBIDDEN in {it['id']}: {f_term}")
            all_clean = False

if all_clean:
    print("ALL 41 CLAIMS ARE CLEAN FROM FORBIDDEN TERMS!")
