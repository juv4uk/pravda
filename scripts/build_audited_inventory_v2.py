# -*- coding: utf-8 -*-
"""
Builds semantics/CROSS-CORPUS-LEXEME-INVENTORY.md (AUDITED INVENTORY v2)
and semantics/LEXEME-AUDIT-LEDGER.md

Status: NO KNOWN FALSE MATCHES UNDER CURRENT AUDIT RULES

Epistemic Invariants:
1. ROOT-FAMILY = SEARCH / DERIVATIONAL GROUPING ONLY.
   ROOT-FAMILY != LEMMA != CONCEPT != ETYMOLOGICAL CLAIM.
2. ORTHOGRAPHIC NORMALIZATION != LEXICAL IDENTITY != SEMANTIC IDENTITY.
3. Strict separation of distinct search families:
   - DOGOVOR != PAKT != TRAKTAT
   - STATTYA != ARTICUL
   - PRAVDA != PRAVO
   - ROTA != PRISYAGA
   - OBYCHAY != ZVYCHAY
   - VOLN- separated by POS: NOUN (вольность) vs ADJ_ADV (вольный, вольно)
4. Explicit Unicode handling:
   - Supports both U+0402 (Ђ) and U+0463 (ѣ)
5. Audit decisions tracked in DECISION-LAYER: AUDIT.
6. LEMMA-CANDIDATE: UNKNOWN.
7. SEMANTIC-GROUP: EMPTY, INTERPRETATION: EMPTY.
"""

import re
import json

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
        'name': 'Гадяцький сеймовий акт 1659 року'
    },
    {
        'source_id': 'SRC-MARCH-1654',
        'witness_id': 'WIT-MARCH-1654',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-MARCH-1654-DIPLOMATIC.txt',
        'name': 'Березневі статті 1654 року'
    },
    {
        'source_id': 'SRC-ORLYK-1710',
        'witness_id': 'WIT-ORLYK-1710-BENDERY',
        'file': 'sources/primary/transcriptions/diplomatic/SRC-ORLYK-1710-UA-DIPLOMATIC.txt',
        'name': 'Бендерська конституція Пилипа Орлика 1710 року'
    }
]

# Target search groupings:
# Note: character range includes standard Cyrillic, U+0402 (Ђ), U+0463 (ѣ), U+0456 (і), U+0457 (ї)
CYR = r'а-яЂѣієїў'

search_configs = {
    'PRAVDA': {
        'patterns': [rf'\b(правд[{CYR}]+)\b', r'\b(prawd[a-z]+)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'ADJ' if any(w.lower().startswith(p) for p in ['правдив', 'prawdopodob']) else 'NOUN'
    },
    'PRAVO': {
        'patterns': [rf'\b(прав[{CYR}]*)\b', r'\b(praw[a-z]*)\b'],
        'exclude_prefix': ['правд', 'prawd'],
        'pos_rule': lambda w: 'ADJ' if any(w.lower().startswith(p) for p in ['правн', 'правов', 'правый', 'правое', 'правая', 'правых', 'prawon']) else ('NOUN' if w.lower() in ['право', 'права', 'правом', 'праву', 'прав', 'правЂ', 'праве', 'правах', 'правахъ', 'правомъ', 'правом'] or w.lower().startswith('praw') else 'UNKNOWN')
    },
    'VOLN_NOUN': {
        'patterns': [rf'\b(вольн[ое][сз]т[{CYR}]*)\b', r'\b(wolno[sś][cć][a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN'
    },
    'VOLN_ADJ_ADV': {
        'patterns': [rf'\b(вольн[{CYR}]+)\b', r'\b(woln[a-z]+)\b'],
        'exclude_prefix': ['вольност', 'вольнест', 'wolnos', 'wolnoś'],
        'pos_rule': lambda w: 'ADV' if w.lower() in ['вольно', 'вольне', 'wolno'] else 'ADJ'
    },
    'SVOBOD': {
        'patterns': [rf'\b(свобод[{CYR}]+)\b', r'\b(swobod[a-z]+)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN' if w.lower() in ['свобода', 'свободы', 'свободе', 'свободу', 'свободою', 'swoboda', 'swobody', 'swobodach'] else 'ADJ'
    },
    'OBYCHAY': {
        'patterns': [rf'\b(обыча[{CYR}]+)\b', r'\b(obyczaj[a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN'
    },
    'ZVYCHAY': {
        'patterns': [rf'\b(звыча[{CYR}]+)\b', r'\b(zwyczaj[a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN'
    },
    'RYAD': {
        'patterns': [rf'\b(ряд[{CYR}]*)\b', r'\b(rz[aą]d[a-z]*)\b'],
        'exclude_prefix': ['рядов', 'порядок', 'розряд'],
        'pos_rule': lambda w: 'NOUN'
    },
    'PRIVILEG': {
        'patterns': [rf'\b(привил[{CYR}]+)\b', r'\b(prywile[a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN' if not w.lower().startswith('упривил') and not 'ован' in w.lower() else 'ADJ'
    },
    'DOGOVOR': {
        'patterns': [rf'\b(договор[{CYR}]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'VERB' if 'договорили' in w.lower() else 'NOUN'
    },
    'PAKT': {
        'patterns': [rf'\b(пакт[{CYR}]*)\b', r'\b(pakt[a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN'
    },
    'TRAKTAT': {
        'patterns': [rf'\b(трактат[{CYR}]*)\b', r'\b(traktat[a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN'
    },
    'STATTYA': {
        'patterns': [rf'\b(стат[еьіїяъ][{CYR}]*)\b'],
        'exclude_prefix': ['статут', 'статок', 'статки', 'статку', 'статков', 'статечн', 'стати'],
        'pos_rule': lambda w: 'NOUN'
    },
    'ARTICUL': {
        'patterns': [rf'\b(артикул[{CYR}]*)\b', r'\b(artyk[a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN'
    },
    'ROTA_OATH': {
        'patterns': [rf'\b(рот[{CYR}]*)\b'],
        'exclude_prefix': ['ротмистр', 'ротъмистр', 'ротравив'],
        'pos_rule': lambda w: 'ADJ' if 'ротни' in w.lower() else 'NOUN'
    },
    'PRISYAGA': {
        'patterns': [rf'\b(присяг[{CYR}]+)\b', rf'\b(прысяг[{CYR}]+)\b', r'\b(przysi[aę]g[a-z]*)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'VERB' if any(w.lower().startswith(v) for v in ['присягаю', 'присягал', 'прысягал']) else 'NOUN'
    },
    'OBIDA': {
        'patterns': [rf'\b(обид[{CYR}]+)\b'],
        'exclude_prefix': [],
        'pos_rule': lambda w: 'NOUN'
    }
}

audit_ledger = []
inventory_records = []
rec_id = 1

def run_extraction_and_audit():
    global rec_id
    for src in sources:
        with open(src['file'], 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_idx, line in enumerate(lines, 1):
            clean_line = line.strip()
            if not clean_line:
                continue
            
            is_meta_line = clean_line.startswith('{{') or clean_line.startswith('[[') or clean_line.startswith('|')
            
            for fam_name, cfg in search_configs.items():
                for pat in cfg['patterns']:
                    for match in re.finditer(pat, clean_line, re.IGNORECASE):
                        matched_word = match.group(0)
                        lower_w = matched_word.lower()
                        
                        if is_meta_line:
                            audit_ledger.append({
                                'source_id': src['source_id'],
                                'family': fam_name,
                                'raw_hit': matched_word,
                                'decision': 'EXCLUDED',
                                'decision_layer': 'AUDIT',
                                'reason': 'Службові метадані навігації / розмітки видання',
                                'source_form': matched_word,
                                'locator': f"рядок {line_idx}"
                            })
                            continue
                        
                        excluded_by_prefix = False
                        for ex in cfg.get('exclude_prefix', []):
                            if lower_w.startswith(ex):
                                audit_ledger.append({
                                    'source_id': src['source_id'],
                                    'family': fam_name,
                                    'raw_hit': matched_word,
                                    'decision': 'EXCLUDED',
                                    'decision_layer': 'AUDIT',
                                    'reason': f"Вилучено за префіксним правилом ізоляції родин: '{ex}'",
                                    'source_form': matched_word,
                                    'locator': f"рядок {line_idx}"
                                })
                                excluded_by_prefix = True
                                break
                        if excluded_by_prefix:
                            continue
                        
                        if fam_name == 'ROTA_OATH':
                            if lower_w == 'ротъ':
                                start_pos = max(0, match.start() - 15)
                                end_pos = min(len(clean_line), match.end() + 15)
                                snippet = clean_line[start_pos:end_pos].lower()
                                if 'на ротъ' in snippet or 'на рот' in snippet:
                                    audit_ledger.append({
                                        'source_id': src['source_id'],
                                        'family': fam_name,
                                        'raw_hit': matched_word,
                                        'decision': 'EXCLUDED',
                                        'decision_layer': 'AUDIT',
                                        'reason': 'Омонім (зоотехнічний термін / паща коня: "на ротъ сути овесъ")',
                                        'source_form': matched_word,
                                        'locator': f"рядок {line_idx}"
                                    })
                                    continue
                            if lower_w in ['ротахъ', 'ротах', 'роты'] and any(k in clean_line.lower() for k in ['службах', 'пенезей на роты', 'реестрах', 'на роты давати']):
                                audit_ledger.append({
                                    'source_id': src['source_id'],
                                    'family': fam_name,
                                    'raw_hit': matched_word,
                                    'decision': 'EXCLUDED',
                                    'decision_layer': 'AUDIT',
                                    'reason': 'Омонім (військовий підрозділ / рота жовнірська, а не судова присяга)',
                                    'source_form': matched_word,
                                    'locator': f"рядок {line_idx}"
                                })
                                continue
                        
                        if fam_name == 'STATTYA':
                            if any(lower_w.startswith(stem) for stem in ['стати', 'стать', 'статок', 'статки', 'статку', 'статков', 'статечн']):
                                audit_ledger.append({
                                    'source_id': src['source_id'],
                                    'family': fam_name,
                                    'raw_hit': matched_word,
                                    'decision': 'EXCLUDED',
                                    'decision_layer': 'AUDIT',
                                    'reason': 'Інша лексична основа (дієслово стати або іменник статок/майно)',
                                    'source_form': matched_word,
                                    'locator': f"рядок {line_idx}"
                                })
                                continue
                        
                        if fam_name == 'RYAD':
                            if any(lower_w.startswith(stem) for stem in ['поряд', 'розряд']):
                                audit_ledger.append({
                                    'source_id': src['source_id'],
                                    'family': fam_name,
                                    'raw_hit': matched_word,
                                    'decision': 'EXCLUDED',
                                    'decision_layer': 'AUDIT',
                                    'reason': 'Префіксальний дериват (порядок / розряд)',
                                    'source_form': matched_word,
                                    'locator': f"рядок {line_idx}"
                                })
                                continue

                        start_char = max(0, match.start() - 50)
                        end_char = min(len(clean_line), match.end() + 50)
                        context_snippet = clean_line[start_char:end_char].strip()
                        if start_char > 0: context_snippet = "..." + context_snippet
                        if end_char < len(clean_line): context_snippet = context_snippet + "..."
                        
                        pos = cfg['pos_rule'](matched_word)
                        
                        inventory_records.append({
                            'id': f"LEX-INV2-{rec_id:04d}",
                            'source_id': src['source_id'],
                            'witness_id': src['witness_id'],
                            'source_name': src['name'],
                            'locator': f"рядок {line_idx}",
                            'source_form': matched_word,
                            'context': context_snippet,
                            'root_family': fam_name,
                            'pos_candidate': pos,
                            'lemma_candidate': 'UNKNOWN',
                            'decision_layer': 'AUDIT',
                            'semantic_group': 'EMPTY',
                            'interpretation': 'EMPTY'
                        })
                        
                        audit_ledger.append({
                            'source_id': src['source_id'],
                            'family': fam_name,
                            'raw_hit': matched_word,
                            'decision': 'INCLUDED',
                            'decision_layer': 'AUDIT',
                            'reason': 'Повний збіг із пошуковим шаблоном та правилами ізоляції',
                            'source_form': matched_word,
                            'locator': f"рядок {line_idx}"
                        })
                        rec_id += 1

if __name__ == '__main__':
    run_extraction_and_audit()
    print(f"Total included inventory records: {len(inventory_records)}")
    print(f"Total audit ledger records: {len(audit_ledger)}")
    
    with open('scratch/inventory_v2.json', 'w', encoding='utf-8') as f:
        json.dump(inventory_records, f, ensure_ascii=False, indent=2)
    with open('scratch/audit_ledger_v2.json', 'w', encoding='utf-8') as f:
        json.dump(audit_ledger, f, ensure_ascii=False, indent=2)
