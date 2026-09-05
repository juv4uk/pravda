# -*- coding: utf-8 -*-
"""
Builds semantics/CROSS-CORPUS-LEXEME-INVENTORY.md
Extracts exact occurrences of target morphological families across all 7 corpus components.

Epistemic Invariants:
1. ORTHOGRAPHIC NORMALIZATION != LEXICAL IDENTITY != SEMANTIC IDENTITY.
2. Distinct morphological families are NEVER merged prematurely:
   - 'правда' is NOT merged into 'право'.
   - 'вольность' is NOT merged into 'свобода'.
   - 'обычай' is NOT merged into 'звычай'.
   - 'ряд' is NOT merged into 'договор'.
   - 'рота' is NOT merged into 'присяга'.
   - 'обида' is NOT merged into 'преступление' or 'шкода'.
3. Each entry record format:
   - LEX-ID
   - SOURCE-ID
   - WITNESS-ID
   - LOCATOR
   - SOURCE-FORM
   - EXACT-CONTEXT
   - MORPHOLOGICAL-FAMILY
   - NORMALIZED-FORM
   - NORMALIZATION-CONFIDENCE: HIGH / MEDIUM / LOW
   - SEMANTIC-GROUP: EMPTY
   - INTERPRETATION: EMPTY
"""

import re

sources = [
    {
        'source_id': 'SRC-RP-SHORT',
        'witness_id': 'WIT-RP-SHORT-ACADEMIC',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-RP-SHORT-DIPLOMATIC.txt',
        'name': 'Руська Правда (Коротка редакція, XV ст.)'
    },
    {
        'source_id': 'SRC-RP-EXP',
        'witness_id': 'WIT-RP-EXP-TROITSKY',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-RP-EXP-DIPLOMATIC.txt',
        'name': 'Руська Правда (Простора редакція, XIV ст.)'
    },
    {
        'source_id': 'SRC-LS-1566',
        'witness_id': 'WIT-LS-1566',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-LS-1566-DIPLOMATIC.txt',
        'name': 'Литовський Статут 1566 року'
    },
    {
        'source_id': 'SRC-LS-1588',
        'witness_id': 'WIT-LS-1588',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-LS-1588-DIPLOMATIC.txt',
        'name': 'Литовський Статут 1588 року'
    },
    {
        'source_id': 'SRC-HADIACH-1658',
        'witness_id': 'WIT-HADIACH-COMMISSION-1658',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-HADIACH-1658-COMMISSION-DIPLOMATIC.txt',
        'name': 'Гадяцька комісія 1658 року'
    },
    {
        'source_id': 'SRC-HADIACH-1659',
        'witness_id': 'WIT-HADIACH-SEJM-1659',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt',
        'name': 'Сеймовий корпус Гадяцького врегулювання 1659 року'
    },
    {
        'source_id': 'SRC-MARCH-1654',
        'witness_id': 'WIT-MARCH-1654-POSOLSKIY',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-MARCH-1654-DIPLOMATIC.txt',
        'name': 'Березневі статті 1654 року'
    },
    {
        'source_id': 'SRC-ORLYK-1710',
        'witness_id': 'WIT-ORLYK-1710-BENDERY',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-ORLYK-1710-DIPLOMATIC.txt',
        'name': 'Договори і Постановлення (Бендери 1710)'
    }
]

# Morphological families to inventory
target_families = {
    'PRAVDA': {
        'patterns': [r'\b(правд[а-яѣі]+)\b', r'\b(prawd[a-z]+)\b'],
        'norm': 'правда'
    },
    'PRAVO': {
        'patterns': [r'\b(прав[а-яѣі]+)\b', r'\b(praw[a-z]+)\b'],
        'exclude_prefix': ['правд', 'prawd'],
        'norm': 'право'
    },
    'VOLNOST': {
        'patterns': [r'\b(вольн[а-яѣі]+)\b', r'\b(woln[a-z]+)\b'],
        'norm': 'вольность'
    },
    'SVOBODA': {
        'patterns': [r'\b(свобод[а-яѣі]+)\b', r'\b(swobod[a-z]+)\b'],
        'norm': 'свобода'
    },
    'OBYCHAY': {
        'patterns': [r'\b(обыча[а-яѣі]+)\b', r'\b(obyczaj[a-z]*)\b'],
        'norm': 'обычай'
    },
    'ZVYCHAY': {
        'patterns': [r'\b(звыча[а-яѣі]+)\b', r'\b(zwyczaj[a-z]*)\b'],
        'norm': 'звычай'
    },
    'RYAD': {
        'patterns': [r'\b(ряд[а-яѣі]*)\b', r'\b(rz[aą]d[a-z]*)\b'],
        'norm': 'рядъ'
    },
    'PRIVILEG': {
        'patterns': [r'\b(привил[а-яѣі]+)\b', r'\b(prywile[a-z]*)\b'],
        'norm': 'привилей'
    },
    'DOGOVOR': {
        'patterns': [r'\b(договор[а-яѣі]*)\b', r'\b(pakt[a-z]*)\b', r'\b(traktat[a-z]*)\b'],
        'norm': 'договоръ / пактъ'
    },
    'STATTYA': {
        'patterns': [r'\b(стат[а-яѣі]+)\b', r'\b(artyk[a-z]*)\b'],
        'norm': 'статья / артикулъ'
    },
    'ROTA': {
        'patterns': [r'\b(рот[а-яѣі]+)\b'],
        'norm': 'рота'
    },
    'PRISYAGA': {
        'patterns': [r'\b(присяг[а-яѣі]+)\b', r'\b(прысяг[а-яѣі]+)\b', r'\b(przysi[aę]g[a-z]*)\b'],
        'norm': 'присяга'
    },
    'OBIDA': {
        'patterns': [r'\b(обид[а-яѣі]+)\b'],
        'norm': 'обида'
    }
}

inventory_records = []
rec_id = 1

for src in sources:
    with open(src['file'], 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line_idx, line in enumerate(lines, 1):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith('{{') or clean_line.startswith('[[') or clean_line.startswith('|'):
            continue
        
        words = clean_line.split()
        for fname, fcfg in target_families.items():
            for pat in fcfg['patterns']:
                for match in re.finditer(pat, clean_line, re.IGNORECASE):
                    matched_word = match.group(0)
                    # Check exclusions
                    if 'exclude_prefix' in fcfg:
                        if any(matched_word.lower().startswith(ex) for ex in fcfg['exclude_prefix']):
                            continue
                    
                    # Extract surrounding context (approx 5-7 words before and after)
                    start_char = max(0, match.start() - 50)
                    end_char = min(len(clean_line), match.end() + 50)
                    context_snippet = clean_line[start_char:end_char].strip()
                    if start_char > 0: context_snippet = "..." + context_snippet
                    if end_char < len(clean_line): context_snippet = context_snippet + "..."
                    
                    inventory_records.append({
                        'id': f"LEX-INV-{rec_id:04d}",
                        'source_id': src['source_id'],
                        'witness_id': src['witness_id'],
                        'source_name': src['name'],
                        'locator': f"рядок {line_idx}",
                        'source_form': matched_word,
                        'context': context_snippet,
                        'family': fname,
                        'normalized': fcfg['norm'],
                        'confidence': 'HIGH'
                    })
                    rec_id += 1

print(f"Total raw lexeme occurrences inventoried: {len(inventory_records)}")

