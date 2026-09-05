import re
import json

def load_blocks(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    items = text.split('\n\n')
    records = []
    for block in items:
        if not block.strip(): continue
        lines = block.strip().split('\n')
        m = re.match(r'\[([^\]]+)\]\s*\[([^\]]+)\]\s*(.*)', lines[0])
        if m:
            rec_id, src, loc = m.group(1), m.group(2), m.group(3)
            form_m = re.search(r'FORM:\s*(\S+)\s*\(([^)]+)\)', lines[1])
            form = form_m.group(1) if form_m else ""
            pos = form_m.group(2) if form_m else ""
            ctx = lines[2].replace('CTX:', '').strip()
            records.append({
                'id': rec_id,
                'src': src,
                'loc': loc,
                'form': form,
                'pos': pos,
                'ctx': ctx
            })
    return records

svob_records = load_blocks('scratch/svobod_dump.txt')
voln_records = load_blocks('scratch/voln_noun_dump.txt')

print(f"SVOB: {len(svob_records)}, VOLN_NOUN: {len(voln_records)}")

# Language mapping
def detect_lang(src, form, ctx):
    if src in ['SRC-HADIACH-1658', 'SRC-HADIACH-1659']:
        # Most of Hadiach is Polish, check if Cyrillic or Latin script
        if any('\u0400' <= c <= '\u04FF' for c in form):
            return "Early Modern Ruthenian / Ukrainian"
        return "Early Modern Polish"
    elif src in ['SRC-RP-SHORT', 'SRC-RP-EXP']:
        return "Old Rus / Church Slavonic recension"
    elif src in ['SRC-LS-1566', 'SRC-LS-1588']:
        return "Chancery Ruthenian (Grand Duchy of Lithuania)"
    elif src == 'SRC-MARCH-1654':
        return "Muscovite / Chancery Russian / Ruthenian bilingual exchange"
    elif src == 'SRC-ORLYK-1710':
        return "Old Ukrainian / Middle Ukrainian (Hetmanate chancery standard)"
    return "Unknown"

print("Language sample check:")
for r in voln_records[:3]:
    print(r['id'], r['src'], detect_lang(r['src'], r['form'], r['ctx']))
for r in svob_records[:3]:
    print(r['id'], r['src'], detect_lang(r['src'], r['form'], r['ctx']))

