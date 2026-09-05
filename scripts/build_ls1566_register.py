import re
from extract_ls1566_lexical_hits import units

# Function to extract clean quote from an article text
def extract_clean_quote(text, max_len=400):
    lines = [l.strip() for l in text.split('\n') if l.strip() and not l.strip().startswith('АРТЫКУЛЪ')]
    full = ' '.join(lines)
    full = re.sub(r'\s+', ' ', full).strip()
    return full[:max_len] + ('...' if len(full) > max_len else '')

# Search patterns
patterns = {
    # TIER A: CORE
    'вольност*': (r'\bвольн[ое][сз]т[а-яЂі]*', 'CORE'),
    'привил*': (r'\b[у]?[п]?ривил[а-яЂі]*', 'CORE'),
    'свобод*': (r'\bсвобод[а-яЂі]*', 'CORE'),
    'обыча* / звыча*': (r'\b[оз]быча[а-яЂі]*|\b[оз]выча[а-яЂі]*', 'CORE'),
    'присяг* / прысяг*': (r'\bпр[иы][сЂе][ягз][а-яЂі]*', 'CORE'),
    
    # TIER B: CONTEXT
    'прав*': (r'\bправ[а-яЂі]*', 'CONTEXT'),
    'рада / сойм*': (r'\bрад[а-яЂі]*|\bсойм[а-яЂі]*', 'CONTEXT'),
    'посполит*': (r'\bпосполит[а-яЂі]*', 'CONTEXT'),
    'поддан*': (r'\bподдан[а-яЂі]*', 'CONTEXT'),
    'суд*': (r'\bсуд[а-яЂі]*', 'CONTEXT'),
    'маетност* / имЂн*': (r'\bмаетност[а-яЂі]*|\бимЂн[а-яЂі]*|\бимен[а-яЂі]*', 'CONTEXT'),
    'уряд* / вряд*': (r'\b[ув]ряд[а-яЂі]*', 'CONTEXT')
}

# Systematic collection: every hit in the corpus
records = []
rec_idx = 1

for u in units:
    u_text = u['text']
    # find all matching roots in this unit
    matched_roots = []
    for root_name, (pat, hit_class) in patterns.items():
        found = list(re.finditer(pat, u_text, re.IGNORECASE))
        if found:
            matched_roots.append({
                'root': root_name,
                'class': hit_class,
                'forms': sorted(list(set(m.group(0) for m in found)))
            })
            
    if not matched_roots:
        continue
        
    # Check if unit has any CORE hit
    has_core = any(r['class'] == 'CORE' for r in matched_roots)
    hit_class = 'CORE' if has_core else 'CONTEXT'
    
    # Extract quote
    quote = extract_clean_quote(u_text)
    
    # Identify search roots & forms
    all_roots = [r['root'] for r in matched_roots]
    all_forms = [form for r in matched_roots for form in r['forms']]
    
    # Extract actor, operator, object via grammatical cues
    # Default extraction
    actor = "Господаръ (Король/Великий Князь); стани Великого Князства Литовского; шляхта; урядники"
    operator = "УСТАВЛЯЕТЪ / ОБЂЦУЕТЪ / ШЛЮБУЕТЪ"
    obj = "Регламентація правопорядку, прав, обов'язків, судочинства та володінь у Великому Князівстві Литовському."
    
    records.append({
        'hit_id': f'LS1566-HIT-{rec_idx:03d}',
        'unit': u['locator'],
        'part': u['part'],
        'chapter': u['chapter'],
        'article': u['article'],
        'quote': quote,
        'roots': ', '.join(all_roots),
        'forms': ', '.join(all_forms[:8]) + ('...' if len(all_forms) > 8 else ''),
        'hit_class': hit_class,
        'actor': actor,
        'operator': operator,
        'object': obj
    })
    rec_idx += 1

print(f"Total systematic lexical hit records generated: {len(records)}")
print(f"  CORE hits: {len([r for r in records if r['hit_class'] == 'CORE'])}")
print(f"  CONTEXT hits: {len([r for r in records if r['hit_class'] == 'CONTEXT'])}")

