import re

with open('semantics/CROSS-CORPUS-LEXEME-INVENTORY.md', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('### LEX-INV2-')[1:]
print(f"Total entries: {len(entries)}")

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

voln_noun = []
voln_adj = []
svobod = []

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
        'fam': fam,
        'ctx': ctx
    }
    if fam == 'VOLN_NOUN':
        voln_noun.append(item)
    elif fam == 'VOLN_ADJ_ADV':
        voln_adj.append(item)
    elif fam == 'SVOBOD':
        svobod.append(item)

print(f"Captured: VOLN_NOUN={len(voln_noun)}, VOLN_ADJ_ADV={len(voln_adj)}, SVOBOD={len(svobod)}")

with open('scratch/svobod_dump.txt', 'w', encoding='utf-8') as out:
    for item in svobod:
        out.write(f"[{item['id']}] [{item['src']}] {item['loc']}\n  FORM: {item['form']} ({item['pos']})\n  CTX: {item['ctx']}\n\n")

with open('scratch/voln_noun_dump.txt', 'w', encoding='utf-8') as out:
    for item in voln_noun:
        out.write(f"[{item['id']}] [{item['src']}] {item['loc']}\n  FORM: {item['form']} ({item['pos']})\n  CTX: {item['ctx']}\n\n")

print("Dumps generated in scratch/")
