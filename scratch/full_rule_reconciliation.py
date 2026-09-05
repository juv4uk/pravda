import json
import re
from collections import defaultdict, Counter

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

# Formalized explicit regex inclusion rules
# VOLN constructions:
# CONST-VOLN-001: Coordinate series [права] [свободи] [вольності]
#   Inclusion: Co-occurrence within +-5 words of прав* / свобод* / przywilej* / звича* / лист* linked by coordinative conjunction
# CONST-VOLN-002: Prepositional frame [при / przy] + VOLNOST
#   Inclusion: 'при' or 'przy' immediately or with intervening adjectives modifying вольності/wolności
# CONST-VOLN-003: Verb of confirmation/granting + VOLNOST
#   Inclusion: потвердити / конфирмовати / обварувати / дати / надавати governing вольності
# CONST-VOLN-004: Verb of breach/deprivation/derogation + VOLNOST
#   Inclusion: порушити / отбирати / отводити / поламати / na ujmę / ujma governing вольності
# CONST-VOLN-005: Verb of usage/enjoyment + VOLNOST
#   Inclusion: уживати / заживати / gaudere / веселитися governing вольностей
# CONST-VOLN-006: Singular вольность + [моцъ / выЂхати]
#   Inclusion: Singular вольность in combination with modal capability or movement
# CONST-VOLN-007: Prepositional frame [на водах на дорогах] + VOLNOST
#   Inclusion: вольность specifically situated on waterways/roads (transit immunity)

# SVOB constructions:
# CONST-SVOB-001: свободный + [мужь / люди / послуси / полонені]
#   Inclusion: Adjectival form attributive to person nouns
# CONST-SVOB-002: судять послухи свободными
#   Inclusion: Rule specifying procedural qualification of witness
# CONST-SVOB-003: [наимиту / дітям рабині] свобода
#   Inclusion: Dative recipient + nominal свобода indicating release from debt or servitude
# CONST-SVOB-004: swobodnie [zażywać / odprawować]
#   Inclusion: Adverb swobodnie modifying religious or academic practice
# CONST-SVOB-005: [на первую свободу / от ярма свободити]
#   Inclusion: Political/collective liberation of people/homeland from foreign yoke
# CONST-SVOB-006: від свободи [слободи] куни
#   Inclusion: Fiscal/customs assessment per sloboda settlement

def match_all(t, root):
    ctx_l = t['ctx'].lower()
    form_l = t['form'].lower()
    matches = []
    
    if root == 'VOLN':
        # 001 Coordination
        if re.search(r'(прав\S*|свобод\S*|привил\S*|лист\S*|звыча\S*|поряд\S*|praw\S*|swobod\S*|przywile\S*)\s*(,|и|а|та|y|i)\s*.*(волност|wolnośc)', ctx_l) or \
           re.search(r'(волност\S*|wolnośc\S*)\s*(,|и|а|та|y|i)\s*.*(прав\S*|свобод\S*|привил\S*|лист\S*|звыча\S*|поряд\S*|praw\S*|swobod\S*|przywile\S*)', ctx_l):
            matches.append('CONST-VOLN-001')
            
        # 002 Prepositional 'при'
        if re.search(r'\b(при|przy)\s+([^\s,;]+\s+){0,3}(волност|wolnośc)', ctx_l):
            matches.append('CONST-VOLN-002')
            
        # 003 Confirmation / granting
        if any(k in ctx_l for k in ['потвер', 'конфирм', 'обваров', 'надан', 'надане', 'надати', 'даные', 'примножен', 'прибавити', 'грамоты на вольности']):
            matches.append('CONST-VOLN-003')
            
        # 004 Breach / deprivation
        if any(k in ctx_l for k in ['поруш', 'отбирати', 'отводити', 'поламати', 'уйм', 'uym', 'потерпети', 'порушеньня']):
            matches.append('CONST-VOLN-004')
            
        # 005 Usage / enjoyment
        if any(k in ctx_l for k in ['ужив', 'зажив', 'gaudere', 'весели']):
            matches.append('CONST-VOLN-005')
            
        # 006 Singular capability / movement
        if form_l == 'вольность' and ('моцъ' in ctx_l or 'выЂхати' in ctx_l or 'соймик' in ctx_l or 'поправан' in ctx_l):
            matches.append('CONST-VOLN-006')
            
        # 007 Water / road immunity
        if 'водах' in ctx_l and 'дорогах' in ctx_l:
            matches.append('CONST-VOLN-007')
            
    elif root == 'SVOB':
        # 001 Attributive person
        if any(p in ctx_l for p in ['мужа', 'мужь', 'людии', 'люди', 'послух', 'полону', 'свободнемь', 'свободнии']):
            matches.append('CONST-SVOB-001')
            
        # 002 Procedural witness rule
        if 'послух' in ctx_l and 'свободными' in ctx_l:
            matches.append('CONST-SVOB-002')
            
        # 003 Debt / servitude release
        if ('наимиту' in ctx_l and 'свобода' in ctx_l) or ('смертию' in ctx_l and 'свобода' in ctx_l):
            matches.append('CONST-SVOB-003')
            
        # 004 Swobodnie worship / printing
        if 'swobodnie' in form_l or ('swobodnie' in ctx_l and any(k in ctx_l for k in ['obrządek', 'nauki', 'księgi', 'publicznie'])):
            matches.append('CONST-SVOB-004')
            
        # 005 Collective emancipation
        if any(k in ctx_l for k in ['первую свободу', 'неволничого ярма', 'от ярма', 'свободити отчизну', 'желаемой себе свободы']):
            matches.append('CONST-SVOB-005')
            
        # 006 Sloboda settlement unit
        if 'от свободы' in ctx_l and 'кун' in ctx_l:
            matches.append('CONST-SVOB-006')
            
    return matches

voln_res = {}
for t in voln:
    voln_res[t['id']] = match_all(t, 'VOLN')

svob_res = {}
for t in svob:
    svob_res[t['id']] = match_all(t, 'SVOB')

print("VOLN token match summary:")
c_v = Counter(len(v) for v in voln_res.values())
print("Distribution of matches per token:", c_v)

print("\nSVOB token match summary:")
c_s = Counter(len(v) for v in svob_res.values())
print("Distribution of matches per token:", c_s)

# Exact counts
inst_counts = defaultdict(set)
token_counts = defaultdict(list)

for tid, ms in voln_res.items():
    t = next(x for x in voln if x['id'] == tid)
    for cid in ms:
        token_counts[cid].append(tid)
        inst_counts[cid].add((t['src'], t['loc']))

for tid, ms in svob_res.items():
    t = next(x for x in svob if x['id'] == tid)
    for cid in ms:
        token_counts[cid].append(tid)
        inst_counts[cid].add((t['src'], t['loc']))

print("\n=== RECONCILED TABLE: TOKEN-COUNT vs INSTANCE-COUNT ===")
for cid in sorted(token_counts.keys()):
    t_cnt = len(token_counts[cid])
    i_cnt = len(inst_counts[cid])
    print(f"{cid}: TOKEN-COUNT = {t_cnt} | INSTANCE-COUNT = {i_cnt}")

