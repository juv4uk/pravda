import re

def load_data(filename):
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

svob = load_data('scratch/svobod_dump.txt')
voln_n = load_data('scratch/voln_noun_dump.txt')

print(f"=== SVOBODA / СВОБОДНЫЙ ({len(svob)}) ===")
# Count singular vs plural, noun vs adj
svob_nouns = [s for s in svob if s['pos'] == 'NOUN' or 'свобод' in s['form'].lower()]
for s in svob:
    print(f"[{s['src']} | {s['loc']}] {s['form']} ({s['pos']}) -> {s['ctx']}")

print("\n=== VOLNOST NOUN SAMPLE BY CORPUS ===")
for s in voln_n[:15]:
    print(f"[{s['src']} | {s['loc']}] {s['form']} -> {s['ctx']}")

