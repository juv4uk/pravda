# -*- coding: utf-8 -*-
"""
Builds diffs/RP-SHORT-EXP-TEXTUAL-DIFF.md:
Alignment registry between Ruska Pravda Short Recension (Academic List, 65 atoms)
and Ruska Pravda Expanded Recension (Troitsky List, 160 atoms).

Methodology & Invariants:
1. DIFF ONLY / ZERO INTERPRETATION: Formal alignment registry only.
2. NO TELEOLOGICAL BIAS: OMITTED != REJECTED, ADDED != EXPANDED, MODIFIED-WORDING != NARROWED.
3. MATCH-TYPE categories:
   - IDENTICAL
   - MODIFIED-WORDING
   - MODIFIED-TARIFF
   - SPLIT
   - MERGED
   - OMITTED
   - ADDED
4. ALIGNMENT-CONFIDENCE: HIGH / MEDIUM / LOW
5. MATCH-BASIS: lexical / structural / same actor / same object / same condition / same procedure
6. SEMANTIC-INTERPRETATION: EMPTY
7. HISTORICAL-INTERPRETATION: EMPTY
"""

import re

# Load Short and Expanded atoms from HISTORICAL-CLAIMS-REGISTER.md
with open('HISTORICAL-CLAIMS-REGISTER.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx6 = text.find('## 6. Еталонний повний блок: Руська Правда (Коротка редакція)')
idx7 = text.find('## 7. Еталонний повний блок: Руська Правда (Простора редакція)')
idx8 = text.find('## 8. ')
if idx8 == -1: idx8 = len(text)

s6 = text[idx6:idx7]
s7 = text[idx7:idx8]

c6_raw = re.findall(r'(### HC-RP-SHORT-[0-9A-Z]+.*?)(?=(?:### HC-RP-SHORT-[0-9A-Z]+|\Z))', s6, re.DOTALL)
c7_raw = re.findall(r'(### HC-RP-EXP-[0-9A-Z]+.*?)(?=(?:### HC-RP-EXP-[0-9A-Z]+|\Z))', s7, re.DOTALL)

def parse_atom(raw):
    cid = re.search(r'### (HC-RP-[0-9A-Z\-]+)', raw).group(1)
    art = re.search(r'- \*\*ARTICLE:\*\* (.*)', raw).group(1)
    loc = re.search(r'- \*\*LOCATOR:\*\* (.*)', raw).group(1)
    quote = re.search(r'- \*\*EXACT-QUOTE:\*\*\s+> (.*)', raw).group(1)
    actor = re.search(r'- \*\*GRAMMATICAL-ACTOR:\*\* (.*)', raw).group(1)
    operator = re.search(r'- \*\*TEXTUAL-OPERATOR:\*\* (.*)', raw).group(1)
    obj = re.search(r'- \*\*TEXTUAL-OBJECT:\*\* (.*)', raw).group(1)
    cond = re.search(r'- \*\*TEXTUAL-CONDITION:\*\* (.*)', raw).group(1)
    conseq = re.search(r'- \*\*TEXTUAL-CONSEQUENCE:\*\* (.*)', raw).group(1)
    terms = re.search(r'- \*\*LEXICAL-TERMS:\*\* (.*)', raw).group(1)
    return {
        'id': cid, 'article': art, 'locator': loc, 'quote': quote,
        'actor': actor, 'operator': operator, 'object': obj,
        'condition': cond, 'consequence': conseq, 'terms': terms
    }

short_atoms = {a['id']: a for a in (parse_atom(c) for c in c6_raw)}
exp_atoms = {a['id']: a for a in (parse_atom(c) for c in c7_raw)}

print(f"Loaded {len(short_atoms)} Short atoms and {len(exp_atoms)} Expanded atoms.")

