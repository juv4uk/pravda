# -*- coding: utf-8 -*-
"""
Builds initial historical dictionary entry cards in dictionary/*.md
from audited inventory v2 records.

Architecture:
LEVEL 1 — FORM (distinct wordforms, frequency, distribution)
LEVEL 2 — LEXEME CANDIDATE (root/derivational search family, POS)
LEVEL 3 — USAGE CLUSTERS (structural constructions, collocations)
LEVEL 4 — SENSES: NOT YET ESTABLISHED (empirically empty, no modern assignment)
LEVEL 5 — HISTORICAL INTERPRETATION: PENDING
"""

import json
from collections import defaultdict, Counter

with open('scratch/inventory_v2.json', 'r', encoding='utf-8') as f:
    inventory = json.load(f)

# Map families to dictionary filename & title
family_meta = {
    'PRAVDA': ('PRAVDA.md', 'ПРАВДА', 'PRAVD-'),
    'PRAVO': ('PRAVO.md', 'ПРАВО', 'PRAV-'),
    'VOLN_NOUN': ('VOLNOST.md', 'ВОЛЬНОСТЬ', 'VOLN- (NOUN)'),
    'VOLN_ADJ_ADV': ('VOLNYJ_VOLNO.md', 'ВОЛЬНЫЙ / ВОЛЬНО', 'VOLN- (ADJ/ADV)'),
    'SVOBOD': ('SVOBODA.md', 'СВОБОДА', 'SVOBOD-'),
    'ROTA_OATH': ('ROTA.md', 'РОТА', 'ROT- (OATH)'),
    'PRISYAGA': ('PRISYAGA.md', 'ПРИСЯГА', 'PRISYAG-'),
    'OBIDA': ('OBIDA.md', 'ОБИДА', 'OBID-'),
    'RYAD': ('RYAD.md', 'РЯДЪ', 'RYAD-'),
    'OBYCHAY': ('OBYCHAY.md', 'ОБЫЧАЙ', 'OBYCHAY-'),
    'ZVYCHAY': ('ZVYCHAY.md', 'ЗВЫЧАЙ', 'ZVYCHAY-'),
    'PRIVILEG': ('PRIVILEG.md', 'ПРИВИЛЕЙ', 'PRIVILEG-'),
    'DOGOVOR': ('DOGOVOR.md', 'ДОГОВОРЪ', 'DOGOVOR-'),
    'PAKT': ('PAKT.md', 'ПАКТЪ', 'PAKT-'),
    'TRAKTAT': ('TRAKTAT.md', 'ТРАКТАТЪ', 'TRAKTAT-'),
    'STATTYA': ('STATTYA.md', 'СТАТЬЯ', 'STATTYA-'),
    'ARTICUL': ('ARTICUL.md', 'АРТИКУЛЪ', 'ARTICUL-')
}

grouped = defaultdict(list)
for r in inventory:
    grouped[r['root_family']].append(r)

for fam_code, (filename, entry_title, root_label) in family_meta.items():
    recs = grouped.get(fam_code, [])
    if not recs:
        continue
    
    total_hits = len(recs)
    forms_counter = Counter(r['source_form'] for r in recs)
    sources_counter = Counter(r['source_id'] for r in recs)
    pos_counter = Counter(r['pos_candidate'] for r in recs)
    
    # Chronological earliest witness
    earliest_rec = recs[0]
    
    md = []
    md.append(f"# СЛОВНИКОВА СТАТТЯ КОРПУСУ: {entry_title}")
    md.append(f"## HISTORICAL DICTIONARY ENTRY: `{entry_title}`\n")
    md.append("> **МЕТОДОЛОГІЧНИЙ ПРИНЦИП:**")
    md.append("> Словник накопичує значення виключно з документальних свідчень і контекстів уживання.")
    md.append("> Категорично **ЗАБОРОНЕНО** призначати наперед сучасні юридичні дефініції.\n")
    md.append("> ```text")
    md.append("> FORM clustering ≠ LEXEME identity ≠ SENSE identity ≠ CONCEPT identity")
    md.append("> ```\n")
    
    # LEVEL 1 & 2
    md.append("### 1. РІВЕНЬ 1 І 2: МОРФОЛОГІЯ ТА ДИСТРИБУЦІЯ (FORMS & DISTRIBUTION)\n")
    md.append(f"- **ENTRY:** `{entry_title}`")
    md.append(f"- **ROOT-FAMILY (Search Grouping):** `{root_label}`")
    md.append(f"- **LEMMA-CANDIDATE:** `UNKNOWN`")
    pos_str = ", ".join(f"{p} ({c})" for p, c in pos_counter.most_common())
    md.append(f"- **POS-CANDIDATE:** `{pos_str}`")
    md.append(f"- **TOTAL ATTESTED TOKENS:** **{total_hits}**")
    md.append(f"- **EARLIEST WITNESS IN CURRENT CORPUS:** `{earliest_rec['source_id']}` ({earliest_rec['locator']}) — словоформа: `{earliest_rec['source_form']}`\n")
    
    md.append("#### Зафіксовані словоформи (Attested Source Forms):")
    for form, cnt in forms_counter.most_common():
        md.append(f"- `{form}`: {cnt} входжень")
    
    md.append("\n#### Розподіл за свідками (Witness Distribution):")
    for src, cnt in sources_counter.most_common():
        md.append(f"- `{src}`: {cnt} входжень")
    
    # LEVEL 3: CONCORDANCE SAMPLES
    md.append("\n---\n\n### 2. РІВЕНЬ 3: КОНКОРДАНС ТА ВЖИВАННЯ (CONCORDANCE SAMPLES)\n")
    md.append("> Нижче наведено зафіксовані контексти слововжитку без будь-якої інтерпретації:\n")
    
    # Show up to 25 representative contexts if total > 25, or all if <= 25
    sample_recs = recs[:30]
    for idx, r in enumerate(sample_recs, 1):
        md.append(f"**[{r['id']}]** `{r['source_id']}` ({r['locator']}) | форма: `{r['source_form']}`")
        md.append(f"> {r['context']}\n")
    
    if len(recs) > 30:
        md.append(f"> *...ще {len(recs) - 30} слововжитків зафіксовано в інвентарі [semantics/CROSS-CORPUS-LEXEME-INVENTORY.md](../semantics/CROSS-CORPUS-LEXEME-INVENTORY.md).*\n")
    
    # LEVEL 4: USAGE CLUSTERS & COLLOCATIONS
    md.append("---\n\n### 3. РІВЕНЬ 4: СТРУКТУРНІ КЛАСТЕРИ ВЖИВАННЯ (USAGE CLUSTERS)\n")
    md.append("- **RECURRING SYNTACTIC PATTERNS:** `PENDING FORMAL COLLOCATION EXTRACTION`")
    md.append("- **CO-OCCURRING SEARCH FAMILIES:** `PENDING N-GRAM AUDIT`")
    md.append("- **CANDIDATE SENSES:** `NOT YET ESTABLISHED`")
    md.append("- **SENSE RELATION:** `UNKNOWN`\n")
    
    # LEVEL 5: RESEARCH PROPOSITIONS
    md.append("---\n\n### 4. РІВЕНЬ 5: СТАТУС ТЛУМАЧЕННЯ (INTERPRETATION LAYER)\n")
    md.append("- **MODERN EQUIVALENT:** `NOT ASSIGNED`")
    md.append("- **HISTORICAL INTERPRETATION:** `PENDING`")
    md.append("- **RESEARCH QUESTIONS TO INVESTIGATE:**")
    md.append(f"  1. Чи є зафіксовані словоформи `{entry_title}` представленням одного значення, чи різнорідних інституційних практик?")
    md.append("  2. Які стійкі формули (колокації) супроводжують цей слововжиток у різні історичні періоди?")
    md.append("  3. Чи змінюється дистрибуція словоформи при переході між правовими традиціями?")
    
    filepath = f"dictionary/{filename}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(md))
    print(f"Generated {filepath} ({total_hits} tokens)")

print("All dictionary cards generated successfully.")
