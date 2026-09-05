import json
import re
from collections import defaultdict, Counter

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

# Calibrated regex matching on normalized strings
def match_frames(t, root):
    ctx_l = t['ctx'].lower().replace('Ђ', 'е').replace('ѣ', 'е').replace('ε', 'е').replace('і', 'и').replace('і', 'и')
    form_l = t['form'].lower()
    frames = []
    
    if root == 'VOLN':
        # 1. CONST-VOLN-001: Координаційний ряд прав і вольностей
        # Умова: сполучення з правами, свободами, привілеями, листами, звичаями через сполучник або кому
        if any(k in ctx_l for k in ['прав, свобод', 'свобод и вол', 'прав и вол', 'praw y wol', 'правах та вол', 
                                    'прав витчизни и вольностей', 'права та вольности', 'права и вольности', 
                                    'правами й вольностями', 'листы и вольности', 'правах и вольностях',
                                    'волностями, свободами', 'прав, вольностей', 'прав и вольностей']):
            frames.append('CONST-VOLN-001')
            
        # 2. CONST-VOLN-002: Конструкція [при + вольностях]
        if 'при вольност' in ctx_l or 'przy wolnoś' in ctx_l or 'при свободах и волност' in ctx_l or 'при правах та волност' in ctx_l or 'при правах и волност' in ctx_l:
            frames.append('CONST-VOLN-002')
            
        # 3. CONST-VOLN-003: Дієслово конфірмації/гарантії + вольності
        if any(k in ctx_l for k in ['потвер', 'конфирм', 'обваров', 'надан', 'надане', 'надати', 'даные', 'примножен', 'прибавити', 'грамоты на вольности', 'даем тую вольность']):
            frames.append('CONST-VOLN-003')
            
        # 4. CONST-VOLN-004: Дієслово делікту/порушення/позбавлення + вольності
        if any(k in ctx_l for k in ['поруш', 'отбирати', 'отводити', 'поламати', 'уйм', 'uym', 'потерпети', 'порушеньня']):
            frames.append('CONST-VOLN-004')
            
        # 5. CONST-VOLN-005: Дієслово користування + вольності
        if any(k in ctx_l for k in ['ужив', 'зажив', 'gaudere', 'весели']):
            frames.append('CONST-VOLN-005')
            
        # 6. CONST-VOLN-006: Однинна конструкція виїзду/моці
        if form_l in ['вольность', 'вольностью'] and ('моц' in ctx_l or 'выехати' in ctx_l or 'соймик' in ctx_l or 'поправан' in ctx_l):
            frames.append('CONST-VOLN-006')
            
        # 7. CONST-VOLN-007: Конструкція безмитності [на водах на дорогах]
        if 'водах' in ctx_l and 'дорогах' in ctx_l:
            frames.append('CONST-VOLN-007')
            
    elif root == 'SVOB':
        # 1. CONST-SVOB-001: Атрибутивне означення особи
        if any(k in ctx_l for k in ['мужа', 'мужь', 'людии', 'люди', 'послух', 'полону', 'свободнемь', 'свободнии']):
            frames.append('CONST-SVOB-001')
            
        # 2. CONST-SVOB-002: Вимога дієздатності свідка
        if 'послух' in ctx_l and 'свободными' in ctx_l:
            frames.append('CONST-SVOB-002')
            
        # 3. CONST-SVOB-003: Факт припинення залежності
        if ('наимиту' in ctx_l and 'свобода' in ctx_l) or ('смертию' in ctx_l and 'свобода' in ctx_l):
            frames.append('CONST-SVOB-003')
            
        # 4. CONST-SVOB-004: Спосіб відправлення культу
        if 'swobodnie' in form_l or ('swobodnie' in ctx_l and any(k in ctx_l for k in ['obrz', 'nauk', 'druk', 'publicznie'])):
            frames.append('CONST-SVOB-004')
            
        # 5. CONST-SVOB-005: Колективне визволення народу
        if any(k in ctx_l for k in ['первую свободу', 'неволничого ярма', 'от ярма', 'свободити', 'желаемой себе свободы', 'колишньои свободи']):
            frames.append('CONST-SVOB-005')
            
        # 6. CONST-SVOB-006: Поземельна одиниця слободи
        if 'от свободы' in ctx_l and 'кун' in ctx_l:
            frames.append('CONST-SVOB-006')
            
    return frames

voln_audited = {t['id']: match_frames(t, 'VOLN') for t in voln}
svob_audited = {t['id']: match_frames(t, 'SVOB') for t in svob}

# Build precise table
tokens_per_frame = defaultdict(list)
instances_per_frame = defaultdict(set)

for tid, fs in voln_audited.items():
    t = next(x for x in voln if x['id'] == tid)
    for f in fs:
        tokens_per_frame[f].append(tid)
        instances_per_frame[f].add((t['src'], t['loc']))

for tid, fs in svob_audited.items():
    t = next(x for x in svob if x['id'] == tid)
    for f in fs:
        tokens_per_frame[f].append(tid)
        instances_per_frame[f].add((t['src'], t['loc']))

print("=== AUDITED CONSTRUCTION METRICS ===")
for cid in sorted(tokens_per_frame.keys()):
    toks = tokens_per_frame[cid]
    insts = instances_per_frame[cid]
    print(f"{cid}: TOKEN-COUNT={len(toks)} | INSTANCE-COUNT={len(insts)}")

# Multi-membership mapping
print("\n=== MULTI-MEMBERSHIP TOKENS ===")
multi_v = {tid: fs for tid, fs in voln_audited.items() if len(fs) > 1}
print(f"VOLN tokens with >1 frame: {len(multi_v)}")
for tid, fs in multi_v.items():
    t = next(x for x in voln if x['id'] == tid)
    print(f"  {tid} [{t['src']} | {t['loc']}] -> {fs}")

multi_s = {tid: fs for tid, fs in svob_audited.items() if len(fs) > 1}
print(f"SVOB tokens with >1 frame: {len(multi_s)}")
for tid, fs in multi_s.items():
    t = next(x for x in svob if x['id'] == tid)
    print(f"  {tid} [{t['src']} | {t['loc']}] -> {fs}")

