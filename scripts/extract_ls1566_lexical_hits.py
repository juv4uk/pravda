import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-LS-1566-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Parse text into article units
chapter_splits = list(re.finditer(r'=== ЧАСТИНА (\d+): ([^=]+) ===', text))
units = []
for i in range(len(chapter_splits)):
    c_start = chapter_splits[i].end()
    c_end = chapter_splits[i+1].start() if i+1 < len(chapter_splits) else len(text)
    part_num = chapter_splits[i].group(1)
    ch_title = chapter_splits[i].group(2).strip()
    ch_text = text[c_start:c_end]
    
    art_splits = list(re.finditer(r'(?:^|\n)АРТЫКУЛЪ\s+(\d+)\.', ch_text))
    if not art_splits:
        units.append({
            'part': part_num,
            'chapter': ch_title,
            'article': 'ПРИВІЛЕЇ',
            'locator': f'Частина {part_num}: {ch_title}',
            'text': ch_text.strip()
        })
    else:
        preface = ch_text[:art_splits[0].start()].strip()
        if len(preface) > 50:
            units.append({
                'part': part_num,
                'chapter': ch_title,
                'article': 'ВСТУП ДО РОЗДІЛУ',
                'locator': f'{ch_title}, Вступ',
                'text': preface
            })
        for j in range(len(art_splits)):
            a_num = art_splits[j].group(1)
            a_start = art_splits[j].start()
            a_end = art_splits[j+1].start() if j+1 < len(art_splits) else len(ch_text)
            art_content = ch_text[a_start:a_end].strip()
            units.append({
                'part': part_num,
                'chapter': ch_title,
                'article': f'Артикул {a_num}',
                'locator': f'{ch_title}, Артикул {a_num}',
                'text': art_content
            })

# 2. Vocabulary patterns
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

# 3. Find hits across units
hits = []
hit_id_seq = 1

for u in units:
    u_text = u['text']
    # Check Tier A hits in this unit
    unit_a_hits = []
    for root_name, pat in tier_a_roots.items():
        found = list(re.finditer(pat, u_text, re.IGNORECASE))
        if found:
            # take matched forms
            forms = list(set(m.group(0) for m in found))
            unit_a_hits.append((root_name, forms, 'CORE'))
            
    # Check Tier B hits in this unit
    unit_b_hits = []
    for root_name, pat in tier_b_roots.items():
        found = list(re.finditer(pat, u_text, re.IGNORECASE))
        if found:
            forms = list(set(m.group(0) for m in found))
            unit_b_hits.append((root_name, forms, 'CONTEXT'))
            
    if unit_a_hits or unit_b_hits:
        hits.append({
            'unit': u,
            'tier_a': unit_a_hits,
            'tier_b': unit_b_hits
        })

print(f"Units containing lexical hits: {len(hits)} / {len(units)}")
units_with_core = [h for h in hits if h['tier_a']]
print(f"Units containing CORE (Tier A) hits: {len(units_with_core)}")
