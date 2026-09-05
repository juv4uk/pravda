import re
import json
from collections import defaultdict, Counter

with open('semantics/CROSS-CORPUS-LEXEME-INVENTORY.md', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('### LEX-INV2-')[1:]
print(f"Total inventory entries: {len(entries)}")

def get_field(entry_text, field_name):
    m = re.search(r'- \*\*' + field_name + r':\*\*\s*`?([^\n`]+)`?', entry_text)
    if m:
        return m.group(1).strip()
    return ""

def get_context(entry_text):
    m = re.search(r'- \*\*EXACT-CONTEXT:\*\*\s*\n\s*> (.*)', entry_text)
    if m:
        return m.group(1).strip()
    return ""

ryad_tokens = []
dogovor_tokens = []
pakt_tokens = []

for e in entries:
    fam = get_field(e, 'ROOT-FAMILY')
    rec_id = 'LEX-INV2-' + e.split('\n')[0].strip()
    src = get_field(e, 'SOURCE-ID')
    loc = get_field(e, 'LOCATOR')
    form = get_field(e, 'SOURCE-FORM')
    pos = get_field(e, 'POS-CANDIDATE')
    ctx = get_context(e)
    item = {
        'id': rec_id,
        'src': src,
        'loc': loc,
        'form': form,
        'pos': pos,
        'ctx': ctx
    }
    if fam == 'RYAD':
        ryad_tokens.append(item)
    elif fam == 'DOGOVOR':
        dogovor_tokens.append(item)
    elif fam == 'PAKT':
        pakt_tokens.append(item)

print(f"Captured: RYAD={len(ryad_tokens)}, DOGOVOR={len(dogovor_tokens)}, PAKT={len(pakt_tokens)}")

with open('scratch/ryad_tokens.json', 'w', encoding='utf-8') as f:
    json.dump(ryad_tokens, f, ensure_ascii=False, indent=2)

with open('scratch/dogovor_tokens.json', 'w', encoding='utf-8') as f:
    json.dump(dogovor_tokens, f, ensure_ascii=False, indent=2)

with open('scratch/pakt_tokens.json', 'w', encoding='utf-8') as f:
    json.dump(pakt_tokens, f, ensure_ascii=False, indent=2)

print("Saved tokens to scratch/*.json")
