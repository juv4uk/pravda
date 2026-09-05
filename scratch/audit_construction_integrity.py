import json
import re
from collections import defaultdict, Counter

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

print(f"Loaded {len(voln)} VOLN and {len(svob)} SVOB tokens.")

# Rule definitions and multi-label assignment
# A single token can belong to 0..N constructions!

def match_constructions(token, root):
    ctx = token['ctx']
    ctx_l = ctx.lower()
    form = token['form']
    form_l = form.lower()
    matched = []
    
    if root == 'VOLN':
        # CONST-VOLN-001: [прав/свобод] + вольностей (coordination)
        # Inclusion: presence of coordination with rights or freedoms
        if any(w in ctx_l for w in ['прав, свобод', 'свободъ и вол', 'прав и вол', 'praw y wol', 'правах та вол', 'прав Вітчизни і вольностей', 'права та вольності', 'права і вольності', 'правами й вольностями']):
            matched.append('CONST-VOLN-001')
            
        # CONST-VOLN-002: при + [стародавніх] вольностях [заховати / зоставити / stawać]
        # Inclusion: preposition 'при' governing вольності/wolności
        if re.search(r'\bпри\s+([^\s,;]+\s+){0,3}(волност|wolnośc)', ctx_l):
            matched.append('CONST-VOLN-002')
            
        # CONST-VOLN-003: [потвердити / конфирмовати / обварувати / надати] + вольности
        # Inclusion: verb of confirmation/granting governing вольності
        if any(v in ctx_l for v in ['потвер', 'конфирм', 'обваров', 'надан', 'надане', 'примножен', 'прибавити', 'грамоты на вольности']):
            matched.append('CONST-VOLN-003')
            
        # CONST-VOLN-004: [порушити / отбирати / отводити / поламати / na ujmę] + вольности
        # Inclusion: verb or noun of deprivation, breach, or derogation
        if any(v in ctx_l for v in ['поруш', 'отбирати', 'отводити', 'поламати', 'уйм', 'uym', 'потерпети']):
            matched.append('CONST-VOLN-004')
            
        # CONST-VOLN-005: вольностей + [уживати / заживати / gaudere / веселитися]
        # Inclusion: verb of usage/enjoyment
        if any(v in ctx_l for v in ['ужив', 'зажив', 'gaudere', 'весели']):
            matched.append('CONST-VOLN-005')
            
        # CONST-VOLN-006: вольность и моцъ [выЂхати / продати]
        # Inclusion: singular вольность coordinated with моцъ or governing infinitive of movement
        if form_l == 'вольность' and ('моцъ' in ctx_l or 'выЂхати' in ctx_l):
            matched.append('CONST-VOLN-006')
            
        # CONST-VOLN-007: вольность на водахъ на дорогахъ
        # Inclusion: singular вольность + prepositional frame 'на водах на дорогах'
        if 'водах' in ctx_l and 'дорогах' in ctx_l:
            matched.append('CONST-VOLN-007')
            
    elif root == 'SVOB':
        # CONST-SVOB-001: свободный + [мужь / люди / послухи / полонені]
        # Inclusion: adjectival form attributive to person nouns
        if any(p in ctx_l for p in ['мужа', 'мужь', 'людии', 'люди', 'послух', 'полону']):
            matched.append('CONST-SVOB-001')
            
        # CONST-SVOB-002: судять послухи свободными
        # Inclusion: specific procedural witness competency rule in RP
        if 'послух' in ctx_l and 'свободными' in ctx_l:
            matched.append('CONST-SVOB-002')
            
        # CONST-SVOB-003: [наимиту / дітям рабині] свобода [во кунах / смертию]
        # Inclusion: dative recipient + nominal predicative свобода indicating release
        if ('наимиту' in ctx_l and 'свобода' in ctx_l) or ('смертию' in ctx_l and 'свобода' in ctx_l):
            matched.append('CONST-SVOB-003')
            
        # CONST-SVOB-004: swobodnie [zażywać / odprawować / drukować]
        # Inclusion: adverb swobodnie modifying religious or academic practice
        if 'swobodnie' in form_l or ('swobodnie' in ctx_l and any(k in ctx_l for k in ['obrządek', 'nauki', 'księgi'])):
            matched.append('CONST-SVOB-004')
            
        # CONST-SVOB-005: на первую свободу / от неволничого ярма свободити
        # Inclusion: collective liberation of people/homeland from yoke
        if any(k in ctx_l for k in ['первую свободу', 'неволничого ярма', 'от ярма', 'свободити отчизну']):
            matched.append('CONST-SVOB-005')
            
        # CONST-SVOB-006: от свободы 9 кунъ
        # Inclusion: fiscal assessment unit in RP
        if 'от свободы' in ctx_l and 'кун' in ctx_l:
            matched.append('CONST-SVOB-006')

    return matched

# Audit every token
voln_matches = {}
for t in voln:
    ms = match_constructions(t, 'VOLN')
    voln_matches[t['id']] = ms

svob_matches = {}
for t in svob:
    ms = match_constructions(t, 'SVOB')
    svob_matches[t['id']] = ms

# Multi-membership statistics
voln_multi = Counter(len(ms) for ms in voln_matches.values())
svob_multi = Counter(len(ms) for ms in svob_matches.values())

print("=== MULTI-MEMBERSHIP (TOKEN -> N CONSTRUCTIONS) ===")
print("VOLN token membership distribution:", voln_multi)
print("SVOB token membership distribution:", svob_multi)

# Overlap details
overlaps = [(tid, ms) for tid, ms in voln_matches.items() if len(ms) > 1]
print(f"\nTotal VOLN tokens belonging to >1 construction: {len(overlaps)}")
for tid, ms in overlaps[:5]:
    t = next(x for x in voln if x['id'] == tid)
    print(f"  {tid} [{t['src']} | {t['loc']}] -> {ms}")
    print(f"     CTX: {t['ctx'][:75]}")

overlaps_s = [(tid, ms) for tid, ms in svob_matches.items() if len(ms) > 1]
print(f"\nTotal SVOB tokens belonging to >1 construction: {len(overlaps_s)}")
for tid, ms in overlaps_s:
    t = next(x for x in svob if x['id'] == tid)
    print(f"  {tid} [{t['src']} | {t['loc']}] -> {ms}")
    print(f"     CTX: {t['ctx'][:75]}")

# Construction counts: separate INSTANCE-COUNT from TOKEN-COUNT
# To compute INSTANCE-COUNT: group by (witness, loc, construction_id)
# Because multiple tokens in the exact same sentence/unit may be part of the SAME construction instance!
print("\n=== RECONCILED CONSTRUCTION STATS ===")
c_tokens = defaultdict(list)
c_instances = defaultdict(set)

for tid, ms in voln_matches.items():
    t = next(x for x in voln if x['id'] == tid)
    for c in ms:
        c_tokens[c].append(tid)
        c_instances[c].add((t['src'], t['loc']))

for tid, ms in svob_matches.items():
    t = next(x for x in svob if x['id'] == tid)
    for c in ms:
        c_tokens[c].append(tid)
        c_instances[c].add((t['src'], t['loc']))

for cid in sorted(list(c_tokens.keys())):
    tok_cnt = len(c_tokens[cid])
    inst_cnt = len(c_instances[cid])
    print(f"{cid}: TOKEN-COUNT={tok_cnt} | INSTANCE-COUNT={inst_cnt}")

