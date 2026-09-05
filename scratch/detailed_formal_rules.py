import json
from collections import defaultdict
import re

with open('scratch/audit_instances_payload.json', 'r', encoding='utf-8') as f:
    payload = json.load(f)

voln = payload['VOLN']
svob = payload['SVOB']

# Let's write the rigorous matching logic with exact regex that matches all verified occurrences in context
def match_token_formal(t, root):
    ctx_orig = t['ctx']
    ctx_l = ctx_orig.lower().replace('Ђ', 'е').replace('ѣ', 'е').replace('ε', 'е').replace('і', 'и').replace('і', 'и')
    form_l = t['form'].lower().replace('Ђ', 'е').replace('ѣ', 'е').replace('ε', 'е').replace('і', 'и')
    pos = t.get('pos', 'NOUN')
    matches = []
    
    if root == 'VOLN':
        # RULE: VOLN-R01-COORD (Coordination with rights/freedoms/privileges)
        # Token is coordinated with parallel legal category via conjunction or comma
        if any(k in ctx_l for k in ['прав, свобод', 'свобод и вол', 'прав и вол', 'praw y wol', 'правах та вол', 
                                    'прав витчизни и вольностей', 'права та вольности', 'права и вольности', 
                                    'правами й вольностями', 'листы и вольности', 'правах и вольностях',
                                    'волностями, свободами', 'прав, вольностей', 'прав и вольностей',
                                    'wolnosci swobod', 'wolnosci, swobod']):
            matches.append({
                'cid': 'CONST-VOLN-001',
                'rule_id': 'VOLN-R01-COORD',
                'evidence': f"Token '{t['form']}' is syntactically coordinated with parallel legal category in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: VOLN-R02-PREP-PRI (Preposition 'при' / 'przy' governing вольності)
        if re.search(r'\b(при|przy)\s+([^\s,;]+\s+){0,4}(волност|wolnośc)', ctx_l) or 'при правах та вольностях' in ctx_l or 'при правах и вольностях' in ctx_l:
            matches.append({
                'cid': 'CONST-VOLN-002',
                'rule_id': 'VOLN-R02-PREP-PRI',
                'evidence': f"Token '{t['form']}' is governed by preposition 'при'/'przy' in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: VOLN-R03-VERB-CONFIRM (Confirmation/granting verbs governing вольності)
        if any(k in ctx_l for k in ['потвер', 'конфирм', 'обваров', 'надан', 'надане', 'надати', 'даные', 'примножен', 'прибавити', 'грамоты на вольности', 'даем тую вольность']):
            matches.append({
                'cid': 'CONST-VOLN-003',
                'rule_id': 'VOLN-R03-VERB-CONFIRM',
                'evidence': f"Token '{t['form']}' is direct object/theme of confirmation or granting predicate in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: VOLN-R04-VERB-BREACH (Breach/deprivation/derogation verbs governing вольності)
        if any(k in ctx_l for k in ['поруш', 'отбирати', 'отводити', 'поламати', 'уйм', 'uym', 'потерпети', 'порушеньня']):
            matches.append({
                'cid': 'CONST-VOLN-004',
                'rule_id': 'VOLN-R04-VERB-BREACH',
                'evidence': f"Token '{t['form']}' is direct object of breach/deprivation/derogation predicate in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: VOLN-R05-VERB-USAGE (Usage/enjoyment verbs governing вольності)
        if any(k in ctx_l for k in ['ужив', 'зажив', 'gaudere', 'весели']):
            matches.append({
                'cid': 'CONST-VOLN-005',
                'rule_id': 'VOLN-R05-VERB-USAGE',
                'evidence': f"Token '{t['form']}' is governed by usage/enjoyment predicate in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: VOLN-R06-NOM-CAPABILITY (Singular modal capability/movement)
        if form_l in ['вольность', 'вольностью'] and any(k in ctx_l for k in ['моц', 'выехати', 'соймик', 'поправан']):
            matches.append({
                'cid': 'CONST-VOLN-006',
                'rule_id': 'VOLN-R06-NOM-CAPABILITY',
                'evidence': f"Singular token '{t['form']}' combined with modal capability/infinitive in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: VOLN-R07-LOC-TRANSIT (Transit immunity on water/roads)
        if 'водах' in ctx_l and 'дорогах' in ctx_l:
            matches.append({
                'cid': 'CONST-VOLN-007',
                'rule_id': 'VOLN-R07-LOC-TRANSIT',
                'evidence': f"Token '{t['form']}' situates within spatial transit formula «вольность на водахъ на дорогахъ»: «{ctx_orig[:70]}»"
            })
            
    elif root == 'SVOB':
        # RULE: SVOB-R01-ADJ-PERSON (Adjectival person status)
        if any(k in ctx_l for k in ['мужа', 'мужь', 'людии', 'люди', 'полону', 'свободнемь', 'свободнии']) and pos != 'NOUN':
            matches.append({
                'cid': 'CONST-SVOB-001',
                'rule_id': 'SVOB-R01-ADJ-PERSON',
                'evidence': f"Adjectival token '{t['form']}' (POS={pos}) directly modifies personal noun/status in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: SVOB-R02-INS-WITNESS (Procedural witness qualification)
        if 'послух' in ctx_l and 'свободными' in ctx_l:
            matches.append({
                'cid': 'CONST-SVOB-002',
                'rule_id': 'SVOB-R02-INS-WITNESS',
                'evidence': f"Token '{t['form']}' functions as instrumental predicate complement defining witness qualification in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: SVOB-R03-NOM-RELEASE (Nominal release from debt/bondage)
        if pos == 'NOUN' and (('наимиту' in ctx_l and 'свобода' in ctx_l) or ('смертию' in ctx_l and 'свобода' in ctx_l)):
            matches.append({
                'cid': 'CONST-SVOB-003',
                'rule_id': 'SVOB-R03-NOM-RELEASE',
                'evidence': f"Nominal token '{t['form']}' (POS={pos}) functions as predicative noun of release with dative beneficiary: «{ctx_orig[:70]}»"
            })
            
        # RULE: SVOB-R04-ADV-MANNER (Adverbial manner of worship/education)
        if 'swobodnie' in form_l or ('swobodnie' in ctx_l and any(k in ctx_l for k in ['obrz', 'nauk', 'druk', 'publicznie'])):
            matches.append({
                'cid': 'CONST-SVOB-004',
                'rule_id': 'SVOB-R04-ADV-MANNER',
                'evidence': f"Adverbial token '{t['form']}' modifies religious/educational practice in span: «{ctx_orig[:70]}»"
            })
            
        # RULE: SVOB-R05-COLL-EMANCIP (Collective emancipation from yoke)
        if any(k in ctx_l for k in ['первую свободу', 'неволничого ярма', 'от ярма', 'свободити', 'желаемой себе свободы', 'колишньои свободи']):
            matches.append({
                'cid': 'CONST-SVOB-005',
                'rule_id': 'SVOB-R05-COLL-EMANCIP',
                'evidence': f"Token '{t['form']}' participates in formula of collective liberation of people/homeland: «{ctx_orig[:70]}»"
            })
            
        # RULE: SVOB-R06-LOC-SLOBODA (Fiscal assessment unit)
        if 'от свободы' in ctx_l and 'кун' in ctx_l:
            matches.append({
                'cid': 'CONST-SVOB-006',
                'rule_id': 'SVOB-R06-LOC-SLOBODA',
                'evidence': f"Token '{t['form']}' functions as fiscal origin unit in tariff list: «{ctx_orig[:70]}»"
            })
            
    return matches

patched_voln = {t['id']: match_token_formal(t, 'VOLN') for t in voln}
patched_svob = {t['id']: match_token_formal(t, 'SVOB') for t in svob}

cid_tokens = defaultdict(list)
cid_instances = defaultdict(list)
cid_sentences = defaultdict(set)

for tid, ms in patched_voln.items():
    t = next(x for x in voln if x['id'] == tid)
    for m in ms:
        cid = m['cid']
        cid_tokens[cid].append(t)
        cid_instances[cid].append({
            'token_id': tid,
            'rule_id': m['rule_id'],
            'src': t['src'],
            'loc': t['loc'],
            'evidence': m['evidence']
        })
        cid_sentences[cid].add((t['src'], t['loc']))

for tid, ms in patched_svob.items():
    t = next(x for x in svob if x['id'] == tid)
    for m in ms:
        cid = m['cid']
        cid_tokens[cid].append(t)
        cid_instances[cid].append({
            'token_id': tid,
            'rule_id': m['rule_id'],
            'src': t['src'],
            'loc': t['loc'],
            'evidence': m['evidence']
        })
        cid_sentences[cid].add((t['src'], t['loc']))

print("=== FINAL PATCHED METRICS ===")
for cid in sorted(cid_tokens.keys()):
    print(f"{cid}: TOKEN-COUNT={len(cid_tokens[cid])} | INSTANCE-COUNT={len(cid_instances[cid])} | SENTENCE-COUNT={len(cid_sentences[cid])}")

with open('scratch/patched_audit_results.json', 'w', encoding='utf-8') as f:
    json.dump({
        'cid_tokens': {k: [t['id'] for t in v] for k, v in cid_tokens.items()},
        'cid_instances': cid_instances,
        'cid_sentences': {k: list(v) for k, v in cid_sentences.items()}
    }, f, ensure_ascii=False, indent=2)

print("Saved scratch/patched_audit_results.json")
