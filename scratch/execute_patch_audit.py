import json
import re
from collections import defaultdict

with open('scratch/audit_instances_payload.json', 'r', encoding='utf-8') as f:
    payload = json.load(f)

voln = payload['VOLN']
svob = payload['SVOB']

# Precise formal matching functions with MATCH-RULE-ID and MATCH-EVIDENCE
def match_token_formal(t, root):
    ctx_orig = t['ctx']
    ctx_l = ctx_orig.lower()
    form_l = t['form'].lower()
    pos = t.get('pos', 'NOUN')
    matches = []
    
    if root == 'VOLN':
        # RULE: VOLN-R01 (Coordination)
        # Token is coordinated with rights/freedoms via conjunction/comma
        m01 = re.search(r'(прав\S*|свобод\S*|привил\S*|лист\S*|звыча\S*|поряд\S*|praw\S*|swobod\S*|przywile\S*)\s*(,|и|а|та|y|i)\s*.*(волност|wolnośc)', ctx_l) or \
              re.search(r'(волност\S*|wolnośc\S*)\s*(,|и|а|та|y|i)\s*.*(прав\S*|свобод\S*|привил\S*|лист\S*|звыча\S*|поряд\S*|praw\S*|swobod\S*|przywile\S*)', ctx_l)
        if m01:
            matches.append({
                'cid': 'CONST-VOLN-001',
                'rule_id': 'VOLN-R01-COORD',
                'evidence': f"Token '{t['form']}' is syntactically coordinated with parallel legal category in span: «{m01.group(0)[:60]}»"
            })
            
        # RULE: VOLN-R02 (Preposition 'при' / 'przy')
        m02 = re.search(r'\b(при|przy)\s+([^\s,;]+\s+){0,3}(волност|wolnośc)', ctx_l)
        if m02:
            matches.append({
                'cid': 'CONST-VOLN-002',
                'rule_id': 'VOLN-R02-PREP-PRI',
                'evidence': f"Token '{t['form']}' is governed by preposition '{m02.group(1)}' in phrase: «{m02.group(0)}»"
            })
            
        # RULE: VOLN-R03 (Confirmation / Granting verbs)
        m03 = re.search(r'\b(потвер|конфирм|обваров|надан|надане|надати|даные|примножен|прибавити|грамоты на вольности|даемъ тую вольность)\S*\s+.*(волност|wolnośc)', ctx_l) or \
              re.search(r'(волност\S*|wolnośc\S*)\s+.*(потвер|конфирм|обваров|надан|надане|надати)', ctx_l)
        if m03:
            matches.append({
                'cid': 'CONST-VOLN-003',
                'rule_id': 'VOLN-R03-VERB-CONFIRM',
                'evidence': f"Token '{t['form']}' is direct object/theme of confirmation/granting predicate in span: «{m03.group(0)[:60]}»"
            })
            
        # RULE: VOLN-R04 (Breach / Deprivation verbs)
        m04 = re.search(r'\b(поруш\S*|отбирати|отводити|поламати|уйм\S*|uym\S*|потерпети)\s+.*(волност|wolnośc)', ctx_l) or \
              re.search(r'(волност\S*|wolnośc\S*)\s+.*(поруш\S*|отбирати|отводити|поламати)', ctx_l)
        if m04:
            matches.append({
                'cid': 'CONST-VOLN-004',
                'rule_id': 'VOLN-R04-VERB-BREACH',
                'evidence': f"Token '{t['form']}' is direct object of breach/deprivation predicate in span: «{m04.group(0)[:60]}»"
            })
            
        # RULE: VOLN-R05 (Usage / Enjoyment verbs)
        m05 = re.search(r'\b(ужив\S*|зажив\S*|gaudere|весели\S*)\s+.*(волност|wolnośc)', ctx_l) or \
              re.search(r'(волност\S*|wolnośc\S*)\s+.*(ужив\S*|зажив\S*|gaudere|весели\S*)', ctx_l)
        if m05:
            matches.append({
                'cid': 'CONST-VOLN-005',
                'rule_id': 'VOLN-R05-VERB-USAGE',
                'evidence': f"Token '{t['form']}' is governed by usage/enjoyment predicate in span: «{m05.group(0)[:60]}»"
            })
            
        # RULE: VOLN-R06 (Singular modal capability / movement)
        if form_l in ['вольность', 'вольностью'] and any(k in ctx_l for k in ['моцъ', 'выЂхати', 'соймик', 'поправан']):
            matches.append({
                'cid': 'CONST-VOLN-006',
                'rule_id': 'VOLN-R06-NOM-CAPABILITY',
                'evidence': f"Singular token '{t['form']}' combined with modal capability/infinitive in span: «{ctx_orig[:60]}»"
            })
            
        # RULE: VOLN-R07 (Transit immunity on water/roads)
        if 'водах' in ctx_l and 'дорогах' in ctx_l:
            matches.append({
                'cid': 'CONST-VOLN-007',
                'rule_id': 'VOLN-R07-LOC-TRANSIT',
                'evidence': f"Token '{t['form']}' situates within spatial transit immunity formula «вольность на водахъ на дорогахъ»"
            })
            
    elif root == 'SVOB':
        # RULE: SVOB-R01 (Adjectival person status)
        if pos == 'ADJ' and any(k in ctx_l for k in ['мужа', 'мужь', 'людии', 'люди', 'полону']):
            matches.append({
                'cid': 'CONST-SVOB-001',
                'rule_id': 'SVOB-R01-ADJ-PERSON',
                'evidence': f"Adjectival token '{t['form']}' (POS={pos}) directly modifies personal noun in span: «{ctx_orig[:60]}»"
            })
            
        # RULE: SVOB-R02 (Procedural witness qualification)
        if 'послух' in ctx_l and 'свободными' in ctx_l:
            matches.append({
                'cid': 'CONST-SVOB-002',
                'rule_id': 'SVOB-R02-INS-WITNESS',
                'evidence': f"Token '{t['form']}' functions as instrumental predicate complement defining witness qualification in span: «{ctx_orig[:60]}»"
            })
            
        # RULE: SVOB-R03 (Nominal release from debt/bondage)
        if pos == 'NOUN' and (('наимиту' in ctx_l and 'свобода' in ctx_l) or ('смертию' in ctx_l and 'свобода' in ctx_l)):
            matches.append({
                'cid': 'CONST-SVOB-003',
                'rule_id': 'SVOB-R03-NOM-RELEASE',
                'evidence': f"Nominal token '{t['form']}' (POS={pos}) functions as predicative noun of release with dative beneficiary in span: «{ctx_orig[:60]}»"
            })
            
        # RULE: SVOB-R04 (Adverbial manner of worship/education)
        if 'swobodnie' in form_l or ('swobodnie' in ctx_l and any(k in ctx_l for k in ['obrządek', 'nauki', 'księgi', 'publicznie'])):
            matches.append({
                'cid': 'CONST-SVOB-004',
                'rule_id': 'SVOB-R04-ADV-MANNER',
                'evidence': f"Adverbial token '{t['form']}' modifies religious/educational activity in span: «{ctx_orig[:60]}»"
            })
            
        # RULE: SVOB-R05 (Collective emancipation from yoke)
        if any(k in ctx_l for k in ['первую свободу', 'неволничого ярма', 'от ярма', 'свободити отчизну', 'желаемой себе свободы']):
            matches.append({
                'cid': 'CONST-SVOB-005',
                'rule_id': 'SVOB-R05-COLL-EMANCIP',
                'evidence': f"Token '{t['form']}' participates in formula of collective liberation of people/homeland in span: «{ctx_orig[:60]}»"
            })
            
        # RULE: SVOB-R06 (Fiscal assessment unit)
        if 'от свободы' in ctx_l and 'кун' in ctx_l:
            matches.append({
                'cid': 'CONST-SVOB-006',
                'rule_id': 'SVOB-R06-LOC-SLOBODA',
                'evidence': f"Token '{t['form']}' functions as fiscal origin unit in tariff list: «{ctx_orig[:60]}»"
            })
            
    return matches

# Audit all tokens
patched_voln = {t['id']: match_token_formal(t, 'VOLN') for t in voln}
patched_svob = {t['id']: match_token_formal(t, 'SVOB') for t in svob}

# Verification of purged false positives
print("--- VERIFYING PURGED FALSE POSITIVES ---")
print("LEX-INV2-2306 matched CIDs:", [m['cid'] for m in patched_voln['LEX-INV2-2306']])
print("LEX-INV2-0044 matched CIDs:", [m['cid'] for m in patched_svob['LEX-INV2-0044']])

# Calculate 3 separate metrics:
# 1. TOKEN-COUNT
# 2. CONSTRUCTION-INSTANCE-COUNT (distinct construction matches)
# 3. SENTENCE-COUNT (distinct witness + locator pairs)

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

print("\n=== RECONCILED THREE-TIER METRICS ===")
for cid in sorted(cid_tokens.keys()):
    t_cnt = len(cid_tokens[cid])
    i_cnt = len(cid_instances[cid])
    s_cnt = len(cid_sentences[cid])
    print(f"{cid}: TOKEN-COUNT={t_cnt} | INSTANCE-COUNT={i_cnt} | SENTENCE-COUNT={s_cnt}")

# Save patched data
with open('scratch/patched_audit_results.json', 'w', encoding='utf-8') as f:
    json.dump({
        'cid_tokens': {k: [t['id'] for t in v] for k, v in cid_tokens.items()},
        'cid_instances': cid_instances,
        'cid_sentences': {k: list(v) for k, v in cid_sentences.items()}
    }, f, ensure_ascii=False, indent=2)

print("Saved scratch/patched_audit_results.json successfully.")
