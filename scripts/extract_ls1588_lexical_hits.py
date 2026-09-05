import re
from parse_ls1588_articles import units_1588

# EXACT FROZEN PATTERNS FROM LS-1566
tier_a_roots = {
    'вольност*': r'\bвольн[ое][сз]т[а-яЂі]*',
    'привил*': r'\b[у]?[п]?ривил[а-яЂі]*',
    'свобод*': r'\bсвобод[а-яЂі]*',
    'обыча* / звыча*': r'\b[оз]быча[а-яЂі]*|\b[оз]выча[а-яЂі]*',
    'присяг* / прысяг*': r'\bпр[иы][сЂе][ягз][а-яЂі]*'
}

tier_b_roots = {
    'прав*': r'\bправ[а-яЂі]*',
    'рада / сойм*': r'\bрад[а-яЂі]*|\bсойм[а-яЂі]*',
    'посполит*': r'\bпосполит[а-яЂі]*',
    'поддан*': r'\bподдан[а-яЂі]*',
    'суд*': r'\bсуд[а-яЂі]*',
    'маетност* / имЂн*': r'\bмаетност[а-яЂі]*|\бимЂн[а-яЂі]*|\бимен[а-яЂі]*',
    'уряд* / вряд*': r'\b[ув]ряд[а-яЂі]*'
}

hits_1588 = []
for u in units_1588:
    u_text = u['text']
    unit_a_hits = []
    for root_name, pat in tier_a_roots.items():
        found = list(re.finditer(pat, u_text, re.IGNORECASE))
        if found:
            forms = sorted(list(set(m.group(0) for m in found)))
            unit_a_hits.append((root_name, forms, 'CORE'))
            
    unit_b_hits = []
    for root_name, pat in tier_b_roots.items():
        found = list(re.finditer(pat, u_text, re.IGNORECASE))
        if found:
            forms = sorted(list(set(m.group(0) for m in found)))
            unit_b_hits.append((root_name, forms, 'CONTEXT'))
            
    if unit_a_hits or unit_b_hits:
        hits_1588.append({
            'unit': u,
            'tier_a': unit_a_hits,
            'tier_b': unit_b_hits
        })

print(f"Total units parsed in LS-1588: {len(units_1588)}")
print(f"Units containing lexical hits: {len(hits_1588)} / {len(units_1588)}")
core_hits_1588 = [h for h in hits_1588 if h['tier_a']]
print(f"Units containing CORE (Tier A) hits: {len(core_hits_1588)}")

# Chapter breakdown for CORE hits in 1588
from collections import Counter
ch_core = Counter(h['unit']['chapter'] for h in core_hits_1588)
print("\nDistribution of CORE (Tier A) hits across chapters in LS-1588:")
for ch, c in ch_core.items():
    print(f"  {ch[:65]:65s}: {c:3d} articles")
