import json
from collections import Counter
import re

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

def clean_txt(s):
    return re.sub(r'\s+', ' ', s).strip()

# We will classify every token into defined recurrent syntactic constructions:
# VOLN constructions:
# CONST-VOLN-01: [GRANTOR] дати / потвердити / конфирмовати [вольности]
# CONST-VOLN-02: [SOVEREIGN] заховати / зоставити при [вольностях]
# CONST-VOLN-03: [ACTOR] вольностей уживати / заживати / веселитися
# CONST-VOLN-04: [ACTOR] вольностей отбирати / отводити / порушити / поламати
# CONST-VOLN-05: біном/трином: [права] [свободы] и [вольности]
# CONST-VOLN-06: однина предикативна: вольность и моцъ [мЂти / выЂхати]
# CONST-VOLN-07: однина цільова: вольность на [соймики съЂзжатися / поправаньня]
# CONST-VOLN-08: імунітет комунікацій: вольность на водах на дорогах
# CONST-VOLN-09: титульна / рубрикаційна формула: [Розділ / Стаття / Договори] о вольностях [шляхецьких / Війська]

# SVOB constructions:
# CONST-SVOB-01: атрибут особи: свободный + [мужь / люди / послуси]
# CONST-SVOB-02: процесуальний стан свідка: судять послухи свободными / на правду не вылазити
# CONST-SVOB-03: юридичний факт припинення залежності: [закупу / робьим дітям] свобода [во кунах / смертию]
# CONST-SVOB-04: прислівник способу культу: swobodnie zażywać / wolno i swobodnie
# CONST-SVOB-05: тричленна формула привілеїв: [права, вольности и] свободы / при свободах
# CONST-SVOB-06: акт колективного визволення: на первую свободу / свободити от ярма
# CONST-SVOB-07: фіскальна поземельна категорія: от свободы [слободи] куни

def classify_voln_token(t):
    ctx = t['ctx'].lower()
    form = t['form'].lower()
    
    # 08: водах/дорогах
    if 'водах' in ctx and 'дорогах' in ctx:
        return 'CONST-VOLN-08', 'Імунітет безмитного проїзду: вольность на водахъ на дорогахъ'
    # 06: вольность и моць
    if form == 'вольность' and ('моцъ' in ctx or 'моць' in ctx or 'выЂхати' in ctx):
        return 'CONST-VOLN-06', 'Свобода дій та виїзду індивіда в однині: вольность и моцъ [выЂхати]'
    # 07: вольность на соймики / поправеньня
    if form == 'вольность' and ('соймик' in ctx or 'поправан' in ctx):
        return 'CONST-VOLN-07', 'Процесуальний дозвіл уповноваженого органу: вольность на [соймики съЂзжатися]'
    # 09: титули та рубрики
    if any(k in ctx for k in ['роздЂлъ', 'розделъ', 'розділ', 'договори і постановлення', 'о вольностяхъ шляхецкихъ']):
        return 'CONST-VOLN-09', 'Рубрикаційна назва правового статусу: [Розділ / Договори] о вольностях [шляхецьких / Війська]'
    # 02: заховати при
    if 'при ' in ctx and ('захов' in ctx or 'зостав' in ctx or 'держати' in ctx or 'ставати' in ctx):
        return 'CONST-VOLN-02', 'Гарантія непорушності стану: заховати / зоставити при [стародавніх] вольностях'
    # 04: делікти / порушення
    if any(k in ctx for k in ['поруш', 'отбирати', 'отводити', 'поламати', 'уйм', 'uym', 'потерпети']):
        return 'CONST-VOLN-04', 'Деліктне позбавлення прав: вольности порушити / відібрати / поламати'
    # 01: підтвердження / надання
    if any(k in ctx for k in ['потвер', 'конфирм', 'надан', 'обваров', 'примнож', 'даные', 'прибавити']):
        return 'CONST-VOLN-01', 'Акт пожалування або гарантії суверена: вольности надати / потвердити / конфирмовати'
    # 03: уживання прав
    if any(k in ctx for k in ['ужив', 'зажив', 'gaudere', 'весели']):
        return 'CONST-VOLN-03', 'Правокористування суб\'єкта: вольностей [шляхетських / спільних] уживати / заживати'
    # 05: біноми та триноми
    if any(k in ctx for k in ['прав, свобод', 'свободъ и вол', 'прав и вол', 'praw y wol', 'правах та вол']):
        return 'CONST-VOLN-05', 'Формульний координаційний ряд: [права, свободи і] вольності'
    
    return 'CONST-VOLN-05', 'Формульний координаційний ряд: [права, свободи і] вольності'

def classify_svob_token(t):
    ctx = t['ctx'].lower()
    form = t['form'].lower()
    pos = t['pos']
    
    if 'послух' in ctx and 'свобод' in ctx:
        return 'CONST-SVOB-02', 'Вимога процесуальної дієздатності свідка: судять послухи свободными'
    if any(k in ctx for k in ['мужа', 'мужь', 'людии', 'свободнемь', 'свободнии']):
        return 'CONST-SVOB-01', 'Атрибутивна ознака повноправної особи: свободный [мужь / люди]'
    if 'во всехъ кунах' in ctx or 'смертию' in ctx:
        return 'CONST-SVOB-03', 'Юридичний факт припинення залежності: [наимиту / дітям рабині] свобода'
    if 'от свободы' in ctx:
        return 'CONST-SVOB-07', 'Фіскальна одиниця пільгового поселення: від свободи [слободи] 9 кун'
    if 'swobodnie' in form or ('swobodnie' in ctx and any(k in ctx for k in ['obrz', 'nauk', 'druk'])):
        return 'CONST-SVOB-04', 'Прислівник безперешкодного здійснення культу: swobodnie заживати обряд / науки'
    if any(k in ctx for k in ['ярм', 'первую свободу', 'свободити']):
        return 'CONST-SVOB-06', 'Акт колективного визволення з неволі: на первую свободу / от ярма свободити'
    if any(k in ctx for k in ['прав, свобод', 'свободъ и вол', 'свободами и поряд', 'swobodach']):
        return 'CONST-SVOB-05', 'Формульний компонент привілеїв поряд з вольностями: при свободах / свободи і права'
        
    return 'CONST-SVOB-01', 'Атрибутивна ознака повноправної особи: свободный [мужь / люди]'

voln_stats = Counter()
for t in voln:
    cid, cname = classify_voln_token(t)
    voln_stats[(cid, cname)] += 1

svob_stats = Counter()
for t in svob:
    cid, cname = classify_svob_token(t)
    svob_stats[(cid, cname)] += 1

print("\n=== VOLN CONSTRUCTIONS CLASSIFIED ===")
for (cid, cname), cnt in sorted(voln_stats.items()):
    print(f"{cid}: {cnt} tokens | {cname}")

print("\n=== SVOB CONSTRUCTIONS CLASSIFIED ===")
for (cid, cname), cnt in sorted(svob_stats.items()):
    print(f"{cid}: {cnt} tokens | {cname}")

