import re

def parse_entries(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    entries = text.split('### LEX-INV2-')[1:]
    parsed = []
    for e in entries:
        lines = e.strip().split('\n')
        rec_id = lines[0].strip()
        data = {}
        for l in lines[1:]:
            if l.startswith('- **'):
                m = re.match(r'- \*\*([^:]+)\*\*:\s*`?([^`\n]+)`?', l)
                if m:
                    data[m.group(1)] = m.group(2).strip('` ')
        data['rec_id'] = 'LEX-INV2-' + rec_id
        parsed.append(data)
    return parsed

entries = parse_entries('semantics/CROSS-CORPUS-LEXEME-INVENTORY.md')
print(f"Parsed {len(entries)} entries")

voln_noun = [e for e in entries if e.get('ROOT-FAMILY') == 'VOLN_NOUN']
voln_adj = [e for e in entries if e.get('ROOT-FAMILY') == 'VOLN_ADJ_ADV']
svobod = [e for e in entries if e.get('ROOT-FAMILY') == 'SVOBOD']

print(f"VOLN_NOUN: {len(voln_noun)}")
print(f"VOLN_ADJ_ADV: {len(voln_adj)}")
print(f"SVOBOD: {len(svobod)}")

with open('scratch/svobod_summary.txt', 'w', encoding='utf-8') as f:
    for e in svobod:
        f.write(f"[{e.get('SOURCE-ID')}] {e.get('LOCATOR')} | Form: {e.get('SOURCE-FORM')} | POS: {e.get('POS-CANDIDATE')} | Root: {e.get('ROOT-FAMILY')}\n  Context: {e.get('EXACT-CONTEXT')}\n\n")

with open('scratch/voln_noun_summary.txt', 'w', encoding='utf-8') as f:
    for e in voln_noun:
        f.write(f"[{e.get('SOURCE-ID')}] {e.get('LOCATOR')} | Form: {e.get('SOURCE-FORM')} | POS: {e.get('POS-CANDIDATE')} | Root: {e.get('ROOT-FAMILY')}\n  Context: {e.get('EXACT-CONTEXT')}\n\n")

with open('scratch/voln_adj_summary.txt', 'w', encoding='utf-8') as f:
    for e in voln_adj:
        f.write(f"[{e.get('SOURCE-ID')}] {e.get('LOCATOR')} | Form: {e.get('SOURCE-FORM')} | POS: {e.get('POS-CANDIDATE')} | Root: {e.get('ROOT-FAMILY')}\n  Context: {e.get('EXACT-CONTEXT')}\n\n")

print("Summaries written to scratch/")
