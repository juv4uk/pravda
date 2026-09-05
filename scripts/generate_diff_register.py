import re
from build_hadiach_textual_diff import claims_1658, claims_1659

# Let us define the systematic alignment table
# Every alignment entry has:
# ALIGN-ID: ALIGN-HAD-XXX
# SOURCE-1658-CLAIM: [ID or NO-1658-COUNTERPART]
# SOURCE-1659-CLAIM: [ID or NO-1659-COUNTERPART]
# MATCH-TYPE: IDENTICAL / MODIFIED-WORDING / OMITTED / ADDED / REORDERED / SPLIT / MERGED / UNCERTAIN-MATCH
# ALIGNMENT-CONFIDENCE: HIGH / MEDIUM / LOW
# MATCH-BASIS: lexical / structural / same actor / same object / same heading
# SHARED-LEXEMES: ...
# STRUCTURAL-DIFFERENCE: ... (literal only)
# SEMANTIC-INTERPRETATION: EMPTY
# POLITICAL-INTERPRETATION: EMPTY

alignments = []

# Part 1: Alignments within inserted Kommissya Hadiacka (pp. 297–301)
kom_pairs = [
    ("HC-HAD1658-PRE-001", "HC-SEJM1659-KOM-PRE-001", "MODIFIED-WORDING", "HIGH", "lexical & structural",
     "Komisja, Stanami Korony Polskiej, W. X. Litewskiego, Hetmanem, Wojskiem Zaporoskim, Bieniewski, Jewłaszewski, w obozie pod Hadziaczem 16 września 1658, pokój wieczny",
     "Текст преамбули 1659 містить сеймовий запис у хронікарсько-канцелярському правописі Volumina Legum із додаванням титулу Яна Казимира та зміною окремих дієслівних форм."),

    ("HC-HAD1658-001A", "HC-SEJM1659-KOM-001A", "MODIFIED-WORDING", "HIGH", "lexical & structural",
     "Religia grecka starożytna, starożytna Ruś, do Korony Polskiej przystąpiła, prerogatywach, wolnym używaniu nabożeństwa, póki język narodu ruskiego zasięga, ritus romanus",
     "Ідентична норма за змістом; у 1659 додано латинську вставку 'cum Sacra Synazi' та нормалізовано синтаксис Volumina Legum."),

    ("HC-HAD1658-001B", "HC-SEJM1659-KOM-001B", "IDENTICAL", "HIGH", "lexical & structural",
     "religii greckiej daje się moc wolnego erygowania cerkwi, zakonów, monastyrów nowych, ponawiania i naprawiania",
     "Буквальний збіг тексту за винятком діловодної орфографії XVII ст."),

    ("HC-HAD1658-001C", "HC-SEJM1659-KOM-001C", "MERGED", "HIGH", "lexical & structural",
     "cerkwi i dóbr z dawna fundowanych, greccy starożytni prawosławni, pułkowników i inszą starszyznę, ab utrinque, wiary przeciwnej",
     "У тексті 1659 положення 1658 про повернення церков за пів року після присяги старшини об'єднано в одному абзаці з забороною фундувати церкви протилежної віри; у 1659 відсутня згадка про скасування Берестейської унії ('A Unia, która dotąd Rzeczpospolitą mieszała, tak się znosi')."),

    ("HC-HAD1658-001D", "HC-SEJM1659-KOM-001C", "SPLIT", "HIGH", "lexical & structural",
     "wiary przeciwnej prawosławnej cerkwi fundować nie ma, rzymska wiara liberum exercitium conceditur",
     "У тексті 1659 фраза про скасування унії опущена, а заборона нової фундації протилежної віри та дозвіл римського обряду увійшли до єдиного комплексу статті."),

    ("HC-HAD1658-001E", "HC-SEJM1659-KOM-001D", "IDENTICAL", "HIGH", "lexical & structural",
     "Panowie świeccy, urzędnicy Jego Królewskiej Mości religii rzymskiej, żadnej jurysdycji mieć nie będą nad duchownymi, świeckimi i zakonnikami religii greckiej, prócz należnego pasterza",
     "Буквальний збіг тексту клаузули."),

    ("HC-HAD1658-001F", "HC-SEJM1659-KOM-001E", "IDENTICAL", "HIGH", "lexical & structural",
     "Metropolita Kijowski ze czterema władykami łuckim lwowskim przemyskim chełmskim i piątym mścisławskim w Senacie zasiadać ma z prawem głosu po Arcybiskupie Lwowskim",
     "Буквальний збіг переліку 6 ієрархів та порядку сенаторського старшинства."),

    ("HC-HAD1658-001G", "HC-SEJM1659-KOM-001F", "MODIFIED-WORDING", "HIGH", "lexical & structural",
     "W województwie kijowskim dygnitarstwa senatorskie szlachcie ritus graeci capacibus, bracławskim czernihowskim alternatio, natis et bene possessionatis",
     "У тексті 1659 додано точне формулювання 'natis, et bene possessionatis' щодо обов'язкової осілості кандидатів."),

    ("HC-HAD1658-001H", "NO-1659-COUNTERPART", "OMITTED", "HIGH", "structural",
     "Hetman dla Wojsk Ruskich pierwszym senatorem w tych trzech województwach, jurysdykcja kijowska do jego dyspozycji, nastawienie podwojewodzego",
     "Клаузула 1658 про безпосереднє надання гетьману повноважень призначати підвоєводу й урядників до набуття володіння воєводством відсутня в тексті комiсії видання 1659 на с. 299."),

    ("HC-HAD1658-001I", "HC-SEJM1659-KOM-001G", "IDENTICAL", "HIGH", "lexical & structural",
     "mieszczanie rzymscy jako religii greckiej spólnych wolności zażywać mają żadnemu religia grecka do Magistratu przeszkodą być nie ma",
     "Буквальний збіг клаузули про права міщан."),

    ("HC-HAD1658-001J", "HC-SEJM1659-KOM-001H", "MERGED", "HIGH", "lexical & structural",
     "Akademię w Kijowie erygować, jako Akademia Krakowska, żadnych sekt ariańskiej kalwińskiej luterskiej",
     "У тексті 1659 положення про Київську академію, другу академію та гімназії/друкарні об'єднані в послідовний текстовий блок на с. 299."),

    ("HC-HAD1658-001K", "HC-SEJM1659-KOM-001H", "MERGED", "HIGH", "lexical & structural",
     "Drugą także Akademię pozwala tam gdzie jej miejsce upatrzą z takimi prawami bez sekt",
     "Об'єднано у загальний освітній розділ у виданні 1659."),

    ("HC-HAD1658-001L", "HC-SEJM1659-KOM-001H", "MERGED", "HIGH", "lexical & structural",
     "Gimnazja kollegia szkoły i drukarnie stawiać wolno in controversiis religionum sine laesione Majestatis Regiae",
     "Об'єднано у загальний освітній розділ у виданні 1659; формулювання латинських застережень тотожні."),

    ("HC-HAD1658-002A", "HC-SEJM1659-KOM-002A", "IDENTICAL", "HIGH", "lexical & structural",
     "Wielmożny Hetman z Wojskiem Zaporoskim powraca, wieczną amnistią zapomnieniem wiecznym pokrywa, żadnej zemsty, sercem chrześcijańskim bona fide",
     "Буквальний збіг тексту статті про амністію."),

    ("HC-HAD1658-002B", "HC-SEJM1659-KOM-002B", "MERGED", "HIGH", "lexical & structural",
     "kaduki wszystkie skasowane pro cassatis habentur, własnym posesorom wolno zawładnąć sub poena infamiae",
     "У тексті 1659 об'єднано в один абзац із клаузулою про святість амністії."),

    ("HC-HAD1658-002C", "HC-SEJM1659-KOM-002B", "MERGED", "HIGH", "lexical & structural",
     "imię aministiej święte, in pristinum statum res et persona restituuntur, zarzucić zdradę ukarany za naruszenie ugody",
     "У тексті 1659 йде безпосередньо після скасування кадуків."),

    ("HC-HAD1658-002D", "HC-SEJM1659-KOM-002C", "IDENTICAL", "HIGH", "lexical & structural",
     "Rzeczpospolita Narodu Polskiego i W. X. Litewskiego i Ruskiego restituantur in integrum w granicach swoich i swobodach, jedno ciało jednej i nierozdzielnej Rzeczypospolitej",
     "Буквальний збіг формули про три народи Речі Посполитої."),

    ("HC-HAD1658-003A", "HC-SEJM1659-KOM-003A", "MERGED", "HIGH", "lexical & structural",
     "Wojska Zaporoskiego liczba trzydzieści tysięcy, na Regestrze poda",
     "У 1659 зафіксовано точну цифру 30 000 (без рукописного варіанту 'albo sześćdziesiąt tysięcy') поруч із 10 000 найманого війська."),

    ("HC-HAD1658-003B", "HC-SEJM1659-KOM-003A", "MERGED", "HIGH", "lexical & structural",
     "zaciągowego wojska dziesięć tysięcy pod władzą Hetmana z podatków na Sejmie uchwalonych",
     "Об'єднано з компутом 30 000 в одному положенні."),

    ("HC-HAD1658-003C", "HC-SEJM1659-KOM-003B", "IDENTICAL", "HIGH", "lexical & structural",
     "kwatery wojsku, żaden dzierżawca podatków wyciągać nie będzie, ludzie rycerscy wolni od ceł myt, od sądów starostów wolni pod samego hetmana jurysdykcją",
     "Буквальний збіг тексту клаузули про квартири й звільнення від податків та судів."),

    ("HC-HAD1658-003D", "HC-SEJM1659-KOM-003C", "MERGED", "HIGH", "lexical & structural",
     "Hetman prezentować będzie, nobilitacja z nadaniem wszelakich wolności, z każdego pułku sto",
     "У 1659 положення про нобілітацію по 100 з полку та заборону введення коронних військ надруковані поспіль на с. 300."),

    ("HC-HAD1658-003E", "HC-SEJM1659-KOM-003C", "MERGED", "HIGH", "lexical & structural",
     "wojsk żadnych polskich litewskich nikt prowadzić nie ma, posiłki koronne pod regimentem Hetmana",
     "Буквальний збіг другої частини положення."),

    ("HC-HAD1658-004A", "HC-SEJM1659-KOM-004A", "MERGED", "HIGH", "lexical & structural",
     "Hetman do końca życia swego pierwszym senatorem, wolne obieranie hetmana, czterech elektorów",
     "У 1659 стаття 4 подана суцільним текстом; згадка про братів гетьмана збережена."),

    ("HC-HAD1658-004B", "NO-1659-COUNTERPART", "OMITTED", "HIGH", "structural",
     "Mennica dla bicia wszelakich pieniędzy w Kijowie albo gdzie sposobnym będzie wedle jednej ligii i z osobą królewską",
     "Клаузула 1658 про відкриття монетного двору в Києві відсутня в тексті комісії видання 1659 (с. 300)."),

    ("HC-HAD1658-004C", "HC-SEJM1659-KOM-004A", "MERGED", "HIGH", "lexical & structural",
     "spólna rada i spólne siły przeciw każdemu nieprzyjacielowi, wolna nawigacja na Czarne Morze",
     "Включено в загальний текст статті 4 у 1659."),

    ("HC-HAD1658-004D", "HC-SEJM1659-KOM-004A", "MERGED", "HIGH", "lexical & structural",
     "jeśli car moskiewski prowincji przywrócić nie zechce, siły koronne litewskie i zaporoskie łączyć się i wojować będą",
     "Включено в загальний текст статті 4 у 1659."),

    ("HC-HAD1658-004E", "HC-SEJM1659-KOM-004A", "MERGED", "HIGH", "lexical & structural",
     "dobra królewszczyzny sumy pieniężne przywrócone, zasługi w wojsku kompensowane i zapłacone",
     "Включено в завершення статті 4 у 1659."),

    ("HC-HAD1658-005A", "HC-SEJM1659-KOM-005A", "MERGED", "HIGH", "lexical & structural",
     "Hetman z Wojskiem Zaporoskim odstąpiwszy wszelakich protekcji wierności i posłuszeństwie Najjaśniejszego Majestatu i Rzeczypospolitej",
     "У 1659 вся стаття 5 подана як цілісний текстовий блок на с. 300."),

    ("HC-HAD1658-005B", "HC-SEJM1659-KOM-005A", "MERGED", "HIGH", "lexical & structural",
     "nie derogując nic braterstwu z Chanem Krymskim, z carem moskiewskim",
     "Включено до статті 5 у 1659; збережено застереження щодо кримського хана."),

    ("HC-HAD1658-005C", "HC-SEJM1659-KOM-005A", "MERGED", "HIGH", "lexical & structural",
     "legacji żadnych od postronnych przyjmować nie ma do Króla odsyłać",
     "Включено до статті 5 у 1659."),

    ("HC-HAD1658-005D", "HC-SEJM1659-KOM-005A", "MERGED", "HIGH", "lexical & structural",
     "ani wojsk postronnych wprowadzać ani porozumienia mieć na szkodę Rzeczypospolitej",
     "Включено до статті 5 у 1659."),

    ("HC-HAD1658-006A", "HC-SEJM1659-KOM-006A", "MERGED", "HIGH", "lexical & structural",
     "privatis wszystkim duchownym ritus romani świeckim do dóbr dziedzicznych starostw dzierżaw bezpieczny powrót i reinductio otwiera się",
     "Стаття 6 розділена на реіндукційну частину та судову/урядову частину."),

    ("HC-HAD1658-006B", "HC-SEJM1659-KOM-006A", "MERGED", "HIGH", "lexical & structural",
     "czas powrotu Król z Hetmanem naznaczyć ma, za uniwersałami Króla i Hetmana",
     "Включено до реіндукційної частини на с. 300."),

    ("HC-HAD1658-006C", "HC-SEJM1659-KOM-006B", "MERGED", "HIGH", "lexical & structural",
     "dla rozsądzenia spraw osobliwy trybunał, owruckie żytomierskie starostwa sądowe",
     "У 1659 зафіксовано створення окремого трибуналу та судових староств."),

    ("HC-HAD1658-006D", "HC-SEJM1659-KOM-006B", "MERGED", "HIGH", "lexical & structural",
     "osobnych Pieczętarzów Marszałków Podskarbich z godnością senatorską, nic przeciwnego nie pieczętować",
     "У 1659 збережено положення про руських печатників, маршалків і підскарбіїв."),

    ("HC-HAD1658-006E", "HC-SEJM1659-KOM-006B", "MERGED", "HIGH", "lexical & structural",
     "do Pieczętarzów urzędu i kancelarii należeć będą duchowne beneficja, sądy z miast dekreta zadworne i sejmowe",
     "Включено до компетенції Руської канцелярії."),

    ("HC-HAD1658-006F", "HC-SEJM1659-KOM-006B", "MERGED", "HIGH", "lexical & structural",
     "przeciwnego z Kancelarii Koronnej albo Litewskiej nieważne poenae dziesięciu tysięcy kop litewskich",
     "Збережено штраф у 10 000 кіп та недійсність суперечливих грамот."),

    ("HC-HAD1658-006G", "HC-SEJM1659-KOM-006B", "MERGED", "HIGH", "lexical & structural",
     "procesy względem poddanych o swawolę najazdów zaborów szkód skasowane",
     "Збережено касацію позовів воєнного часу."),

    ("HC-HAD1658-006H", "HC-SEJM1659-KOM-006B", "MERGED", "HIGH", "lexical & structural",
     "z carem moskiewskim indemnitas reputacji i teraźniejszego postanowienia",
     "Збережено вимогу захисту честі й угоди у відносинах із Москвою."),

    ("HC-HAD1658-CONCL-001", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "Komisję Komisarze i Hetman przysięgą potwierdzili, przysięgą z Senatu potwierdzona będzie",
     "У виданні 1659 заключні клаузули комісії надруковані цілісним блоком на с. 300–301."),

    ("HC-HAD1658-CONCL-002", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "przysięgi Króla Komisarze assekurują",
     "Включено до заключного блоку на с. 301."),

    ("HC-HAD1658-CONCL-003", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "przysięgi pułkowników starszyzny po Sejmie przed Komisarzami",
     "Включено до заключного блоку на с. 301."),

    ("HC-HAD1658-CONCL-004", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "w prawo pospolite w konstytucję inserowana Sejmem aprobowana",
     "Включено до заключного блоку на с. 301."),

    ("HC-HAD1658-CONCL-005", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "do Buławy Wielkiej Ruskiej Czychyryńskie Starostwo continetur w przywileju Chmielnickiego",
     "Включено до заключного блоку на с. 301."),

    ("HC-HAD1658-CONCL-006", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "Hetman od rezydencji przy Królu ma być wolen",
     "Включено до заключного блоку на с. 301."),

    ("HC-HAD1658-CONCL-007", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "Konwokacja województwom kijowskiemu bracławskiemu czernihowskiemu po Sejmie uniwersałem złożona będzie",
     "Включено до заключного блоку на с. 301."),

    ("HC-HAD1658-CONCL-008", "HC-SEJM1659-KOM-CONCL-001", "MERGED", "HIGH", "lexical & structural",
     "Działo się w taborze pod Hadiaczem 16 Septembris 1658, Jan Wyhowski hetman ręką własną",
     "Включено підпис гетьмана Виговського та комісарів на с. 301.")
]

align_idx = 1
for pair in kom_pairs:
    alignments.append({
        "align_id": f"ALIGN-HAD-{align_idx:03d}",
        "src_1658": pair[0],
        "src_1659": pair[1],
        "match_type": pair[2],
        "confidence": pair[3],
        "basis": pair[4],
        "shared_lex": pair[5],
        "struct_diff": pair[6]
    })
    align_idx += 1

# Part 2: Alignments between 1658 clauses and separate 1659 Sejm statutory acts (Approbatio, grants, nobilitations, oaths)
# Many 1659 acts implement or expand upon general commitments in 1658, but represent separate legal instruments.
statute_links = [
    ("HC-HAD1658-CONCL-004", "HC-SEJM1659-APP-002A", "MODIFIED-WORDING", "HIGH", "same object & legal mandate",
     "kommissyą Hadyacką, approbuiemy y za prawo wieczne mieć chcemy, in volumen legum inferuiemy",
     "Клаузула 1658 про внесення комісії в конституцію отримує відповідну ухвалу Сейму 1659 (ст. 2 Approbacya), але Сейм додає застереження 'Salvis pactis z Kurfirsztem Brandeburczykiem'."),

    ("NO-1658-COUNTERPART", "HC-SEJM1659-APP-002B", "ADDED", "HIGH", "heading & legal act",
     "konstytucyą 1638 y skrypt ad archivum dany abroguiemy",
     "Пряма норма про анулювання сеймової ординації 1638 р. та таємного запису сформульована в сеймовому тексті 1659 як окрема законодавча постанова."),

    ("HC-HAD1658-001C", "HC-SEJM1659-CERK-003", "MODIFIED-WORDING", "MEDIUM", "same object & actors",
     "cerkwie, dobra cerkiewne, Kommissarzow naznaczonych",
     "Загальне зобов'язання 1658 передати церковні маєтності православним через комісарів розгорнуто в окрему сеймову конституцію 1659 (ст. 3) з поіменним списком комісарів."),

    ("HC-HAD1658-001E", "HC-SEJM1659-CLERGY-004", "MODIFIED-WORDING", "HIGH", "same actor & object",
     "duchowni religii Greckiey, od poddaństwa podatkow pańszczyzn uwalniamy, pod iurysdykcyą pasterzow zostawali",
     "Заборона юрисдикції поміщиків над грецьким духовенством (1658) оформлена в 1659 як окрема сеймова конституція (ст. 4) з детальним звільненням від феодальних повинностей."),

    ("NO-1658-COUNTERPART", "HC-SEJM1659-LASK-005", "ADDED", "HIGH", "heading & actor",
     "Deklaracya łaski naszey woysku Zaporoskiemu, z poddaństwem nawrocili",
     "Окрема сеймова конституція (ст. 5) урочистої монаршої декларації прощення козацькому війську."),

    ("HC-HAD1658-003D", "HC-SEJM1659-NOB-GEN-006", "MODIFIED-WORDING", "HIGH", "same object",
     "nobilitacya ludzi w dziele rycerskim z woyska Zaporoskiego do kleynotu szlachectwa",
     "Загальна норма 1658 про нобілітацію до 100 козаків із кожного полку оформлена в 1659 окремою вступною конституцією (ст. 6)."),

    ("NO-1658-COUNTERPART", "HC-SEJM1659-TERECH-007", "ADDED", "HIGH", "heading & object",
     "monaster Terechtymirowski, miasteczko Terechtymirow, z przewozem y z szynkami",
     "Окрема сеймова конституція 1659 (ст. 7) про закріплення Трахтемирова за військом; у тексті 1658 відсутня."),

    ("NO-1658-COUNTERPART", "HC-SEJM1659-LUBBAR-008", "ADDED", "HIGH", "heading & actor",
     "Iana na Wyhowie Wyhowskiego Hetmana, Starostwo Lubomelskie y Barskie prawem wiecznym dziedzicznym",
     "Окреме сеймове надання Любомля і Бара Виговському (ст. 8); у тексті комісії 1658 прямо не фігурує (там згадано лише Чигирин до булави)."),

    ("NO-1658-COUNTERPART", "HC-SEJM1659-OATH-GEN-040", "ADDED", "HIGH", "heading & structural",
     "Przysięga, roty przysiąg do prawa pospolitego wnosimy",
     "Окрема сеймова вступна стаття (ст. 40) про внесення повних текстів присяг до права pospolite."),

    ("HC-HAD1658-CONCL-001", "HC-SEJM1659-OATH-PRYM-041", "SPLIT", "HIGH", "same actor & oath text",
     "Wacław z Leszna Arcybiskup Gnieźnieński Primas, przysięga pod Hadiaczem",
     "Зобов'язання 1658 щодо присяги Примаса на Сеймі реалізовано у вигляді конкретної надрукованої роти присяги (ст. 41)."),

    ("HC-HAD1658-CONCL-001", "HC-SEJM1659-OATH-WILN-042", "SPLIT", "HIGH", "same actor & oath text",
     "Ian Zawisza Biskup Wileński, przysięga",
     "Рота присяги єпископа Віленського надрукована як окремий нормативний текст (ст. 42)."),

    ("HC-HAD1658-CONCL-001", "HC-SEJM1659-OATH-HET-043", "SPLIT", "HIGH", "same actor & oath text",
     "Hetmani Koronni y W. X. Lit. Potocki Lubomirski Sapieha Gosiewski",
     "Рота присяги чотирьох гетьманів обох народів (ст. 43)."),

    ("HC-HAD1658-CONCL-001", "HC-SEJM1659-OATH-CHANC-044", "SPLIT", "HIGH", "same actor & oath text",
     "Pieczętarze Oboyga Narodow Prażmowski Leszczyński Pac Naruszewicz",
     "Рота присяги чотирьох канцлерів і підканцлерів (ст. 44)."),

    ("HC-HAD1658-CONCL-001", "HC-SEJM1659-OATH-MARSZ-045", "SPLIT", "HIGH", "same actor & oath text",
     "Ian Gniński Marszałek Izby Poselskiey",
     "Рота присяги маршалка Посольської ізби (ст. 45)."),

    ("HC-HAD1658-CONCL-003", "HC-SEJM1659-OATH-RUS-046", "MODIFIED-WORDING", "HIGH", "same actor & oath text",
     "Posłowie W. X. Ruskiego y woysk Zaporoskich przysięgamy",
     "Присяга козацьких та руських послів і старшин у Сеймі (ст. 46) зафіксована з поіменним переліком 25 осіб."),

    ("NO-1658-COUNTERPART", "HC-SEJM1659-REZYD-047", "ADDED", "HIGH", "heading & calendar schedule",
     "Rezydenci przy boku naszym po ćwierciach roku",
     "Сеймовий графік сенаторів-резидентів при королі по кварталах року; у договорі 1658 відсутній.")
]

for st in statute_links:
    alignments.append({
        "align_id": f"ALIGN-HAD-{align_idx:03d}",
        "src_1658": st[0],
        "src_1659": st[1],
        "match_type": st[2],
        "confidence": st[3],
        "basis": st[4],
        "shared_lex": st[5],
        "struct_diff": st[6]
    })
    align_idx += 1

# Part 3: Record all specific individual grants and nobilitations of 1659 (articles 9 to 39) as ADDED with NO-1658-COUNTERPART
indiv_nob_claims = [
    ("HC-SEJM1659-DANWYH-009", "Danina Danielowi Wyhowskiemu"),
    ("HC-SEJM1659-KONWYH-010", "Danina Konstantemu Wyhowskiemu"),
    ("HC-SEJM1659-CHMIEL-011", "Deklaracya łaski Ierzemu Chmielnickiemu"),
    ("HC-SEJM1659-NOSACZ-012", "Nobilitacya Tymoszowi Nosaczowi"),
    ("HC-SEJM1659-HULAN-013", "Danina Hrehoremu Hułanickiemu"),
    ("HC-SEJM1659-STEMBL-014", "Danina Stęblowa (Fedor Wyhowski)"),
    ("HC-SEJM1659-SULIM-015", "Deklaracya łaski Szlachetnym Sulimom"),
    ("HC-SEJM1659-ZARUD-016", "Nobilitacya Samuelowi Zarudnemu"),
    ("HC-SEJM1659-LESN-017", "Nobilitacya Hrehoremu Leśnickiemu"),
    ("HC-SEJM1659-ZLOT-018", "Nobilitacya Wasiłowi Złotarence Złotarzewskiemu"),
    ("HC-SEJM1659-WERESCZ-019", "Danina Prokopowi Weresczacze"),
    ("HC-SEJM1659-KOWAL-020", "Nobilitacya Kowalewskiemu, Kapłońskim, Bohatyrowiczowi, etc."),
    ("HC-SEJM1659-SAMCZ-021", "Nobilitacya Iakimowi Samczence"),
    ("HC-SEJM1659-PAPK-022", "Nobilitacya Papkiewiczowi, Porywaiowi, Surcie"),
    ("HC-SEJM1659-OLIW-023", "Indygenat Danielowi Oliwemberkowi"),
    ("HC-SEJM1659-PEKUL-024", "Nobilitacya Pekulickim y Iskrzyckim"),
    ("HC-SEJM1659-ANDRY-025", "Nobilitacya Kiryłowi Andryiowiczowi"),
    ("HC-SEJM1659-KRECH-026", "Fundatio monastera Krechowskiego"),
    ("HC-SEJM1659-GONASZ-028", "Danina oycu Gonaszewskiemu"),
    ("HC-SEJM1659-ROMAN-029", "Nobilitacya Andrzeiowi Romanence"),
    ("HC-SEJM1659-MITCZ-030", "Nobilitacya Wasiłowi Mitczence"),
    ("HC-SEJM1659-MAZAR-031", "Nobilitacya Ianowi Mazarakiemu"),
    ("HC-SEJM1659-MAZIEP-032", "Danina Adamowi Maziepie"),
    ("HC-SEJM1659-FECK-033", "Nobilitacya Ostaphowi Feckowiczowi"),
    ("HC-SEJM1659-BULYH-034", "Nobilitacya Maxymowi Bułydze"),
    ("HC-SEJM1659-WART-035", "Nobilitacya Krzysztofowi Wartereszowicowi"),
    ("HC-SEJM1659-CIC-036", "Nobilitacya Thymoszowi Ciciurze"),
    ("HC-SEJM1659-WOYTK-037", "Nobilitacya Bazylemu Woytkiewiczowi"),
    ("HC-SEJM1659-KALEN-038", "Nobilitacya Bohdanowi Kaleniczence"),
    ("HC-SEJM1659-DERZ-039", "Nobilitacya Stefanowi Derżeniewskiemu")
]

for cid, desc in indiv_nob_claims:
    alignments.append({
        "align_id": f"ALIGN-HAD-{align_idx:03d}",
        "src_1658": "NO-1658-COUNTERPART",
        "src_1659": cid,
        "match_type": "ADDED",
        "confidence": "HIGH",
        "basis": "individual statutory grant in Sejm record",
        "shared_lex": "nobilitacja / danina",
        "struct_diff": f"Окремий персональний сеймовий привілей 1659 р. ({desc}), виданий у контексті загального зобов'язання нобілітації старшини, але оформлений окремою конституцією зі своїм заголовком."
    })
    align_idx += 1

print(f"Total alignment entries built: {len(alignments)}")

# Check audit metrics
matched_1658 = set(a["src_1658"] for a in alignments if a["src_1658"] != "NO-1658-COUNTERPART")
matched_1659 = set(a["src_1659"] for a in alignments if a["src_1659"] != "NO-1659-COUNTERPART")

print(f"Unique 1658 claims aligned: {len(matched_1658)} / 47")
print(f"Unique 1659 claims aligned: {len(matched_1659)} / 66")

unmatched_1658 = set(claims_1658.keys()) - matched_1658
unmatched_1659 = set(claims_1659.keys()) - matched_1659

print(f"Unmatched 1658 claims: {len(unmatched_1658)}")
print(f"Unmatched 1659 claims: {len(unmatched_1659)}")

