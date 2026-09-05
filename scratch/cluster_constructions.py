import json
import re
from collections import defaultdict

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

print(f"Total tokens: VOLN={len(voln)}, SVOB={len(svob)}")

# Cluster VOLN
# Let's inspect recurrent patterns:
# 1. Coordinate binom/trinom: [прав / свобод] + вольностей
# 2. Prepositional frame: при + вольностях
# 3. Preservation / confirmation: заховати / потвердити / конфирмовати + вольности
# 4. Deprivation / violation: порушати / отбирати / поламати + вольности
# 5. Enjoyment / exercise: уживати / заживати / gaudere + вольностей
# 6. Singular freedom of action: вольность + [на/поправаньня/выЂхати]
# 7. Immunity on roads/water: вольность на водах на дорогах

voln_clusters = defaultdict(list)
for r in voln:
    ctx = r['ctx'].lower()
    form = r['form'].lower()
    
    assigned = False
    if 'вод' in ctx and 'дорог' in ctx and 'вольност' in form:
        voln_clusters['CONST-VOLN-001 (Імунітет проїзду/митний: вольность на водах на дорогах)'].append(r)
        assigned = True
    elif form == 'вольность' and any(k in ctx for k in ['соймик', 'выЂхати', 'поправаньня', 'моцъ']):
        voln_clusters['CONST-VOLN-002 (Свобода дії/вибору в однині: вольность + INF/на-ACC)'].append(r)
        assigned = True
    elif 'при ' in ctx and 'волност' in ctx:
        voln_clusters['CONST-VOLN-003 (Формула непорушного володіння: при [стародавніх] вольностях [заховати/зоставити])'].append(r)
        assigned = True
    elif any(k in ctx for k in ['поруш', 'отбирати', 'отводити', 'поламати', 'уйм', 'uym']):
        voln_clusters['CONST-VOLN-004 (Делікт проти статусу: вольности порушити / відібрати / поламати)'].append(r)
        assigned = True
    elif any(k in ctx for k in ['потвер', 'конфирм', 'обваров', 'примнож']):
        voln_clusters['CONST-VOLN-005 (Акт визнання/гарантії: вольности потвердити / конфирмовати / обварувати)'].append(r)
        assigned = True
    elif any(k in ctx for k in ['ужив', 'зажив', 'gaudere', 'весели']):
        voln_clusters['CONST-VOLN-006 (Реалізація прав/користування: вольностей [шляхетських/спільних] заживати / уживати)'].append(r)
        assigned = True
    elif any(k in ctx for k in ['договори і постановлення', 'права і вольности', 'прав і вольностей', 'praw y wolności']):
        voln_clusters['CONST-VOLN-007 (Формульний біном/трином: права і вольності [Війська/стану])'].append(r)
        assigned = True
    else:
        voln_clusters['CONST-VOLN-008 (Інші станові та титульні контексти вольностей)'].append(r)

print("\n=== VOLN CLUSTERS ===")
for k, v in sorted(voln_clusters.items()):
    print(f"{k}: {len(v)} tokens")
    for item in v[:2]:
        print(f"   [{item['src']}] {item['form']} -> {item['ctx'][:70]}")

# Cluster SVOB
# 1. Attributive personal status: свободный + [мужь/послухъ/людие]
# 2. Legal release from debt/bondage: [наимиту/імъ] свобода [во всех кунах / смертию]
# 3. Freedom of cult/conscience: swobodnie zażywać / wolno i swobodnie
# 4. National emancipation from yoke: на первую свободу народ козацкий / свободити от ярма
# 5. Trinomial formula component: [права, вольности и] свободы
# 6. Toponymic / land assessment: от свободы 9 кун

svob_clusters = defaultdict(list)
for r in svob:
    ctx = r['ctx'].lower()
    form = r['form'].lower()
    pos = r['pos']
    
    if any(m in ctx for m in ['мужа', 'мужь', 'послух', 'людии', 'полону']):
        svob_clusters['CONST-SVOB-001 (Особистий правовий статус: свободный + [мужь / послухъ / людие])'].append(r)
    elif 'во всехъ кунах' in ctx or 'смертию' in ctx:
        svob_clusters['CONST-SVOB-002 (Юридичний факт звільнення: [комусь] свобода [во кунах / смертию])'].append(r)
    elif 'от свободы' in ctx:
        svob_clusters['CONST-SVOB-003 (Поземельно-фіскальна одиниця: від свободи [слободи] куни)'].append(r)
    elif 'swobodnie' in form or ('swobodnie' in ctx and 'obrz' in ctx):
        svob_clusters['CONST-SVOB-004 (Спосіб безперешкодної дії: swobodnie заживати обряд / науки)'].append(r)
    elif any(k in ctx for k in ['ярм', 'первую свободу', 'отчизну']):
        svob_clusters['CONST-SVOB-005 (Колективне визволення з неволі: на свободу / от ярма свободити)'].append(r)
    elif any(k in ctx for k in ['прав, свобод', 'свободъ и вольностей', 'свободами и порядками', 'swobodach']):
        svob_clusters['CONST-SVOB-006 (Формульний компонент гарантій: при свободах [і вольностях])'].append(r)
    else:
        svob_clusters['CONST-SVOB-007 (Інші вживання кореня свобод-)'].append(r)

print("\n=== SVOB CLUSTERS ===")
for k, v in sorted(svob_clusters.items()):
    print(f"{k}: {len(v)} tokens")
    for item in v[:2]:
        print(f"   [{item['src']}] {item['form']} -> {item['ctx'][:70]}")

