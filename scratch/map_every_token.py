import json
import re

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

# Rules for exhaustive attribution
def audit_voln_token(t):
    ctx_l = t['ctx'].lower()
    form_l = t['form'].lower()
    frames = []
    
    # 1. Rubrication
    if re.search(r'\b(о|роздЂлъ|розделъ|розділ|договори і постановлення)\s+.*(волност|wolnośc)', ctx_l) or \
       'о вольностях' in ctx_l or 'о вольности' in ctx_l:
        frames.append('FRAME-RUBRICATION')
        
    # 2. Coordination
    if any(k in ctx_l for k in ['прав, свобод', 'свободъ и вол', 'прав и вол', 'praw y wol', 'правах та вол', 
                                'прав вітчизни і вольностей', 'права та вольності', 'права і вольності', 
                                'правами й вольностями', 'листи и вольности', 'листовъ и привильевъ',
                                'привил[ь]яхъ и листехъ', 'порядками', 'звычаями']):
        frames.append('FRAME-COORDINATION')
        
    # 3. Preposition 'при'
    if 'при ' in ctx_l or 'przy ' in ctx_l:
        frames.append('FRAME-PREP-PRI')
        
    # 4. Confirmation / granting
    if any(k in ctx_l for k in ['потвер', 'конфирм', 'обваров', 'надан', 'надане', 'надати', 'даные', 'примножен', 'прибавити', 'грамоты на вольности', 'даемъ тую вольность']):
        frames.append('FRAME-CONFIRMATION')
        
    # 5. Breach / deprivation
    if any(k in ctx_l for k in ['поруш', 'отбирати', 'отводити', 'поламати', 'уйм', 'uym', 'потерпети', 'порушеньня', 'не маемъ отбирати']):
        frames.append('FRAME-BREACH')
        
    # 6. Usage / enjoyment
    if any(k in ctx_l for k in ['ужив', 'зажив', 'gaudere', 'весели']):
        frames.append('FRAME-USAGE')
        
    # 7. Singular capability / immunity
    if form_l in ['вольность', 'вольностью'] and ('моцъ' in ctx_l or 'выЂхати' in ctx_l or 'соймик' in ctx_l or 'поправан' in ctx_l or 'водах' in ctx_l or 'дорогах' in ctx_l):
        frames.append('FRAME-SINGULAR-CAPABILITY')
        
    return frames

def audit_svob_token(t):
    ctx_l = t['ctx'].lower()
    form_l = t['form'].lower()
    pos = t['pos']
    frames = []
    
    # 1. Attributive person
    if any(p in ctx_l for p in ['мужа', 'мужь', 'людии', 'люди', 'послух', 'полону', 'свободнемь', 'свободнии']):
        frames.append('FRAME-PERSON-STATUS')
        
    # 2. Witness rule
    if 'послух' in ctx_l and 'свободными' in ctx_l:
        frames.append('FRAME-WITNESS-RULE')
        
    # 3. Debt/servitude release
    if ('наимиту' in ctx_l and 'свобода' in ctx_l) or ('смертию' in ctx_l and 'свобода' in ctx_l):
        frames.append('FRAME-RELEASE')
        
    # 4. Cult/academic manner
    if 'swobodnie' in form_l or ('swobodnie' in ctx_l and any(k in ctx_l for k in ['obrządek', 'nauki', 'księgi', 'publicznie'])):
        frames.append('FRAME-CULT-MANNER')
        
    # 5. Collective liberation
    if any(k in ctx_l for k in ['первую свободу', 'неволничого ярма', 'от ярма', 'свободити отчизну', 'желаемой себе свободы']):
        frames.append('FRAME-COLLECTIVE-LIBERATION')
        
    # 6. Prepositional / coordination with rights
    if any(k in ctx_l for k in ['прав, свобод', 'свободъ и вол', 'свободами и поряд', 'swobodach']):
        frames.append('FRAME-COORDINATION-SVOB')
        
    # 7. Sloboda assessment
    if 'от свободы' in ctx_l and 'кун' in ctx_l:
        frames.append('FRAME-SLOBODA-TAX')
        
    return frames

# Run mapping
v_map = {t['id']: audit_voln_token(t) for t in voln}
s_map = {t['id']: audit_svob_token(t) for t in svob}

from collections import Counter
print("VOLN frames count breakdown:")
v_all_f = [f for fs in v_map.values() for f in fs]
for f, cnt in Counter(v_all_f).most_common():
    print(f"  {f}: {cnt}")

print("\nSVOB frames count breakdown:")
s_all_f = [f for fs in s_map.values() for f in fs]
for f, cnt in Counter(s_all_f).most_common():
    print(f"  {f}: {cnt}")

print("\nVOLN unassigned tokens:", len([k for k, v in v_map.items() if len(v) == 0]))
print("SVOB unassigned tokens:", len([k for k, v in s_map.items() if len(v) == 0]))

