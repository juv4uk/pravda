import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    full_text = f.read()

body = full_text.split('================================================================================')[1]
pacta_end = body.find('Approbacya kommissyj Hadyackiey.')
part_a = body[:pacta_end]
part_bc = body[pacta_end:]

def clean_txt(t):
    return re.sub(r'\s+', ' ', t).strip()

claims = []

# ==========================================
# PART A: KOMMISSYA HADIACKA (pp. 297–301)
# ==========================================
# UNIT: UNIT-SEJM1659-KOMMISSYA
# Preamble + Articles 1 to 6 + Concluding formulas (37 text items as printed in Volumina Legum)

# Let us extract the structured units of Part A
# 1. Preamble
p_start = part_a.find('1. Kommissya między Stanami')
p_end = part_a.find('Religia Grecka starożytna')
preamble_quote = clean_txt(part_a[p_start:p_end])

claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "pp. 297–298",
    "claim_id": "HC-SEJM1659-KOM-PRE-001",
    "speaker": "JOINT FORMULA",
    "quote": preamble_quote,
    "terms": "Kommissya między Stanami Korony Polskiey y W. X. Lit., Hetmanem y woyskiem Zaporoskim, Bieniewskiego, Iewłaszewskiego, pod Hadiaczem 16 Septembris 1658, do obrony przystąpiło, do iedności, Pokoy wieczny",
    "actor": "Комісари Корони й ВКЛ (Бєньовський, Євлашевський); Гетьман Виговський і Військо Запорозьке",
    "operator": "CONCLUDES / DECLARES",
    "object": "Включений до сеймового зводу текст комісії про вічний мир між Станами Корони Польської і ВКЛ та Військом Запорозьким, укладений під Гадячем 16 вересня 1658 р."
})

# 2. Religia Grecka (Article 1)
# 1A: Religia Grecka starozytna
q1a_start = part_a.find('Religia Grecka starożytna')
q1a_end = part_a.find('Teyże religii Greckiey')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 298",
    "claim_id": "HC-SEJM1659-KOM-001A",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1a_start:q1a_end]),
    "terms": "Religia Grecka starożytna, starożytna Ruś do Korony przystąpiła, praerogatywach, wolnym używaniu nabożeństwa, ięzyk narodu Ruskiego, libere et publice zażywa ritus Romanus",
    "actor": "Королівська влада; церква та вірні грецької релігії",
    "operator": "CONFIRMS / GUARANTEES",
    "object": "Збереження за давньою грецькою релігією її прерогатив і вільного відправлення богослужінь усюди, де сягає руська мова, нарівні з римським обрядом."
})

# 1B: Eregowanie cerkwi i monasterow
q1b_start = part_a.find('Teyże religii Greckiey')
q1b_end = part_a.find('Co się tknie cerkiew')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 298",
    "claim_id": "HC-SEJM1659-KOM-001B",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1b_start:q1b_end]),
    "terms": "religii Greckiey, moc wolnego erygowania cerkwi zakonow monastyrow, ponawiania y naprawienia",
    "actor": "грецька церква та її вірні",
    "operator": "PERMITS",
    "object": "Надання права вільно засновувати нові церкви й монастирі та відновлювати старі."
})

# 1C: Cerkwie i dobra dawne oraz zakaz nowej fundacji przeciwnej wiary
q1c_start = part_a.find('Co się tknie cerkiew')
q1c_end = part_a.find('Panowie zaś')
if q1c_end == -1: q1c_end = part_a.find('Panowie zasie')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 298",
    "claim_id": "HC-SEJM1659-KOM-001C",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1c_start:q1c_end]),
    "terms": "cerkiew y dobr, Grecy starożytni prawosławni, post praesidium publicum iuramentum fidelitatis, Tey zasie wiary przeciwko wierze Greckiey Prawosławney cerkwi fundować nie ma, Romanae fidei liberum exercitium",
    "actor": "Grecy starożytni prawosławni; Pułkownikowie; starszyzna; stany duchowne y świeckie",
    "operator": "CONFIRMS / PROHIBITS / REQUIRES",
    "object": "Залишення церков за православними після складання присяги вірності старшиною; заборона засновувати церкви віри, протилежної православній; збереження вільного відправлення римської віри."
})

# 1D: Panowie swieccy jurysdykcja
q1d_start = part_a.find('Panowie zaś')
if q1d_start == -1: q1d_start = part_a.find('Panowie zasie')
q1d_end = part_a.find('A że w spolney oyczyznie')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 298",
    "claim_id": "HC-SEJM1659-KOM-001D",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1d_start:q1d_end]),
    "terms": "Panowie świetcy urzędnicy religii Rzymskiey żadney iurysdykcyi mieć nie będą nad duchownymi świeckiemi y zakonnikami religii Greckiey",
    "actor": "світські дідичі й урядники римської релігії; духовенство й монахи грецької релігії",
    "operator": "PROHIBITS",
    "object": "Заборона світським католицьким поміщикам та урядникам здійснювати юрисдикцію над православним духовенством і чернецтвом."
})

# 1E: Metropolita i wladycy w Senacie
q1e_start = part_a.find('A że w spolney oyczyznie')
q1e_end = part_a.find('W Woiewodztwie Kiiowskim dygnitarstwa')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "pp. 298–299",
    "claim_id": "HC-SEJM1659-KOM-001E",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1e_start:q1e_end]),
    "terms": "Ociec Metropolita Kiiowski, ze czteroma Władykami, piątym z W. X. Lit. Mścisławskim, w Senacie zasiadać ma, liberae vocis usu, po X. Arcy-Biskupie Lwowskim",
    "actor": "Київський митрополит; чотири владики; єпископ мстиславський; Сенат",
    "operator": "REQUIRES / CONFIRMS",
    "object": "Надання місць і права голосу в Сенаті Київському митрополиту та 5 владикам грецького обряду."
})

# 1F: Dygnitarstwa senatorskie
q1f_start = part_a.find('W Woiewodztwie Kiiowskim dygnitarstwa')
q1f_end = part_a.find('Więc też aby')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 299",
    "claim_id": "HC-SEJM1659-KOM-001F",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1f_start:q1f_end]),
    "terms": "dygnitarstwa Senatorskie, szlachcie ritus Graeci capacibus, Brasławskim Czerniechowskim alternatą, post decessum ritus Graeci succedere ritus Romani, bene possessionatis",
    "actor": "шляхта грецького й римського обрядів; король",
    "operator": "REQUIRES / RESERVES",
    "object": "Надання сенаторських урядів у Київському воєводстві лише шляхті грецького обряду; чергування конфесій у Брацлавському й Чернігівському воєводствах для осілої шляхти."
})

# 1G: Mieszczanie w miastach
q1g_start = part_a.find('Więc też aby')
q1g_end = part_a.find('Akademiią w Kiiowie')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 299",
    "claim_id": "HC-SEJM1659-KOM-001G",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1g_start:q1g_end]),
    "terms": "mieszczanie tak Rzymscy iako y religii Greckiey spolnych wolności zażywać maią, żadnemu religia Grecka do Magistratu przeszkodą bydź nie ma",
    "actor": "міщани римського та грецького обрядів; магістрати",
    "operator": "CONFIRMS / PROHIBITS",
    "object": "Рівність міщан обох обрядів у міських правах та недопущення дискримінації за грецьку віру при обранні до магістрату."
})

# 1H: Akademia Kiiowska oraz druga akademia i szkolnictwo
q1h_start = part_a.find('Akademiią w Kiiowie')
q1h_end = part_a.find('A ponieważ Wielmoż: Hetman')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 299",
    "claim_id": "HC-SEJM1659-KOM-001H",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q1h_start:q1h_end]),
    "terms": "Akademiią w Kiiowie erygować, iako Akademia Krakowska, żadnych sekt Aryańskiey Kalwińskiey Luterskiey, Drugą także Akademią pozwala, Grymnazya Kollegia drukarnie, in controversiis religionum",
    "actor": "Його Королівська Милість; Стани Коронні та ВКЛ; викладачі й студенти",
    "operator": "PERMITS / PROHIBITS",
    "object": "Дозвіл на відкриття Академії в Києві та другої Академії з правами Краківської за умови недопущення протестантських сект; вільне відкриття шкіл і друкарень."
})

# 2. Amnestia i granice (Article 2)
# 2A: Amnestia
q2a_start = part_a.find('A ponieważ Wielmoż: Hetman')
q2a_end = part_a.find('Nadto kaduki')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 299",
    "claim_id": "HC-SEJM1659-KOM-002A",
    "speaker": "JOINT FORMULA",
    "quote": clean_txt(part_a[q2a_start:q2a_end]),
    "terms": "odstępuiąc postronnych protekcyi powraca, wieczną amnistyą zapomnieniem wiecznym pokrywa, assekuruiąc wszelkiey kondycyi ludzie, żadney zemsty, bona fide podarowawszy",
    "actor": "Король; Стани Корони й ВКЛ; Гетьман і Військо Запорозьке; приватні особи",
    "operator": "PARDONS / PROHIBITS",
    "object": "Вічна амністія й повне забуття воєнних подій без взаємної помсти для всіх станів та учасників."
})

# 2B: Kaduki i imie amnestii
q2b_start = part_a.find('Nadto kaduki')
q2b_end = part_a.find('Wszystka Rzeczpospolita Narodu Polskiego')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 299",
    "claim_id": "HC-SEJM1659-KOM-002B",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q2b_start:q2b_end]),
    "terms": "kaduki wszystkie skassowane pro cassatis habentur, imię amnistiey święte bydź ma, in pristinum statum res et persona restituuntur, zarzucić zdradę ukarany",
    "actor": "посідачі кадуків; законні власники; сторони угоди",
    "operator": "ABOLISHES / RESTORES / PROHIBITS",
    "object": "Скасування прав на конфісковані маєтності (кадуки); відновлення прав і осіб у попередньому стані; покарання за закиди у зраді."
})

# 2C: Restitutio in integrum
q2c_start = part_a.find('Wszystka Rzeczpospolita Narodu Polskiego')
q2c_end = part_a.find('Woyska Zaporoskiego liczba')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 299",
    "claim_id": "HC-SEJM1659-KOM-002C",
    "speaker": "JOINT FORMULA",
    "quote": clean_txt(part_a[q2c_start:q2c_end]),
    "terms": "Rzeczpospolita Narodu Polskiego y W. X. Lit. y Ruskiego restituantur in integrum, w granicach y swobodach swoich zostawały, iedno ciało iedney y nierozdzielney Rzpltey",
    "actor": "Народи Польський, Литовський і Руський; Річ Посполита",
    "operator": "RESTORES / CONFIRMS",
    "object": "Відновлення трьох народів у кордонах і свободах як єдиного тіла нероздільної Речі Посполитої."
})

# 3. Woysko Zaporoskie (Article 3)
# 3A: Komput i zaciag
q3a_start = part_a.find('Woyska Zaporoskiego liczba')
q3a_end = part_a.find('Kwatery woysku')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 299",
    "claim_id": "HC-SEJM1659-KOM-003A",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q3a_start:q3a_end]),
    "terms": "Woyska Zaporoskiego liczba trzydzieści tysięcy, Zaciągowego woyska dziesięć tysięcy pod władzą Hetmana z podatkow na Seymie uchwalonych",
    "actor": "Військо Запорозьке; наймане військо; Гетьман; Сейм",
    "operator": "DETERMINES / ESTABLISHES",
    "object": "Встановлення чисельності козацького війська у 30 000 осіб та найманого війська у 10 000 під командуванням гетьмана за рахунок сеймових податків."
})

# 3B: Kwatery, wolnosci i wyjecie spod starostow
q3b_start = part_a.find('Kwatery woysku')
q3b_end = part_a.find('Z osobna zaś dła dalszego')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "pp. 299–300",
    "claim_id": "HC-SEJM1659-KOM-003B",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q3b_start:q3b_end]),
    "terms": "Kwatery woysku Zaporoskiemu, żaden dzierżawca podatkow wyciągać nie będą, ludzie rycerscy wolni od ceł myt, od sądow starostow wolni pod samego Hetmana iurysdykcyą",
    "actor": "козаки; старости й орендарі; Гетьман",
    "operator": "CONFIRMS / EXEMPTS / PROHIBITS",
    "object": "Звільнення козаків як лицарських людей від податків, мит і юрисдикції старост із підпорядкуванням суду гетьмана."
})

# 3C: Nobilitacja i wojska koronne
q3c_start = part_a.find('Z osobna zaś dła dalszego')
q3c_end = part_a.find('Dla tym lepszego tych pakt')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 300",
    "claim_id": "HC-SEJM1659-KOM-003C",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q3c_start:q3c_end]),
    "terms": "nobilitacya z każdego pułku sto, Woysk żadnych Polskich Litewskich nikt prowadzić nie ma, posiłki koronne pod regimentem Hetmana",
    "actor": "король; Гетьман; козаки; коронні війська",
    "operator": "PERMITS / PROHIBITS / SUBORDINATES",
    "object": "Нобілітація до 100 козаків із кожного полку; заборона вводу коронних військ у три воєводства та їхнє підпорядкування гетьману під час війни."
})

# 4. Hetmanat i sojusze (Article 4)
q4_start = part_a.find('Dla tym lepszego tych pakt')
q4_end = part_a.find('A iuż od tego czasu Hetman')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 300",
    "claim_id": "HC-SEJM1659-KOM-004A",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q4_start:q4_end]),
    "terms": "Hetman do końca życia swego pierwszym senatorem, wolne obieranie hetmana czterech elektorow, spolna rada y siły, Ieśli Car Moskiewski siły łączyć się maią, dobra konfiskowane przywrocone",
    "actor": "Іван Виговський; чотири електори воєводств; король; війська трьох народів",
    "operator": "CONFIRMS / REQUIRES / RESTORES",
    "object": "Довічне гетьманство Виговського; вільне обрання наступника чотирма електорами; спільна оборона проти Московського царства; повернення конфіскованих дібр."
})

# 5. Stosunki z postronnymi (Article 5)
q5_start = part_a.find('A iuż od tego czasu Hetman')
q5_end = part_a.find('Privatis wszystkim z oboiey strony')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 300",
    "claim_id": "HC-SEJM1659-KOM-005A",
    "speaker": "COSSACK SIDE",
    "quote": clean_txt(part_a[q5_start:q5_end]),
    "terms": "odstąpiwszy wszelakich protekcyi w wierności Maiestatu y Rzpltey, braterstwu z Hanem Krymskim, Legacyi żadnych przyimować nie ma do Krola odsyłać, ani woysk postronnych wprowadzać",
    "actor": "Гетьман і Військо Запорозьке; Кримський хан; король",
    "operator": "RENNOUNCES / PLEDGES / PROHIBITS",
    "object": "Відмова від сторонніх союзів, присяга на вірність королю; збереження союзу з Кримським ханом; обов'язок відсилати чужі посольства королю."
})

# 6. Reindukcja i sadownictwo (Article 6)
# 6A: Reindukcja
q6a_start = part_a.find('Privatis wszystkim z oboiey strony')
q6a_end = part_a.find('A dla rozsądzenia rożnych spraw')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 300",
    "claim_id": "HC-SEJM1659-KOM-006A",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q6a_start:q6a_end]),
    "terms": "Privatis duchownym ritus Romani świeckim do dobr bezpieczny powrot y reindukcya otwiera się za uniwersałami Krola y Hetmana",
    "actor": "католицьке духовенство; світські власники обох сторін; король; гетьман",
    "operator": "PERMITS / REQUIRES",
    "object": "Відкриття реіндукції до маєтностей у чотирьох воєводствах за спільними універсалами короля та гетьмана."
})

# 6B: Sadownictwo, urzedy ruskie i kasacja
q6b_start = part_a.find('A dla rozsądzenia rożnych spraw')
q6b_end = part_a.find('Ktorą to kommissyą')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "pp. 300–301",
    "claim_id": "HC-SEJM1659-KOM-006B",
    "speaker": "UNKNOWN",
    "quote": clean_txt(part_a[q6b_start:q6b_end]),
    "terms": "osobliwy Trybunał, Pieczętarzow Marszałkow Podskarbich z godnością Senatorską, Kancellaryi Koronney albo Litewskiey nieważne paenae 10000 kop litewskich, processy poddanych skassowane, z Carem indemnitas reputacyi",
    "actor": "судовий трибунал; руські сенатори (печатар, маршалок, підскарбій); коронна й литовська канцелярії; суди",
    "operator": "ESTABLISHES / PROHIBITS / ANNULS / ABOLISHES",
    "object": "Встановлення окремого трибуналу, вищих урядів руського народу; недійсність суперечливих королівських актів; касація процесів воєнного часу."
})

# Concluding clauses of Part A
q_concl_start = part_a.find('Ktorą to kommissyą')
claims.append({
    "unit_id": "UNIT-SEJM1659-KOMMISSYA",
    "heading": "KOMMISSYA HADIACKA",
    "page": "p. 301",
    "claim_id": "HC-SEJM1659-KOM-CONCL-001",
    "speaker": "JOINT FORMULA",
    "quote": clean_txt(part_a[q_concl_start:]),
    "terms": "przysięgą stwierdzona przez Kommissarzow y Hetmana, w prawo pospolite w konstytucyą inserowana Seymem approbowana, Czychyryńskie Starostwo do buławy, Konwokacya uniwersałem, lan Wychowski Hetman ręką własną",
    "actor": "комісари Бєньовський, Євлашевський; Гетьман Виговський; Сейм; король",
    "operator": "CONFIRMS / RATIFIES / SIGNS",
    "object": "Підтвердження комісії присягою сторін, внесення її до сеймової конституції як вічного права; закріплення Чигирина за булавою; власноручні підписи Виговського та комісарів."
})

print(f"Part A claims extracted: {len(claims)}")

# =========================================================================
# PART B & C: SEPARATELY TITLED SEJM CONSTITUTIONS (pp. 301–307)
# =========================================================================
# Let's map each heading and article in Part B/C as distinct document units

