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

print("--- SVOBODA PLURALITY ---")
svob_pl = 0
svob_sg = 0
for s in svob:
    form = s['form'].lower()
    if form in ['свободахъ', 'свободъ', 'свободами', 'swobodach', 'свободи']:
        svob_pl += 1
    else:
        svob_sg += 1
print(f"Svoboda forms: total={len(svob)}, plural-like={svob_pl}, singular/other={svob_sg}")

print("\n--- VOLNOST PLURALITY ---")
voln_pl = 0
voln_sg = 0
for v in voln_n:
    form = v['form'].lower()
    if form in ['вольностяхъ', 'вольностей', 'вольности', 'вольностях', 'wolności', 'wolnościami', 'вольностеи', 'волносьти']:
        voln_pl += 1
    elif form in ['вольность', 'вольностью', 'wolność']:
        voln_sg += 1
    else:
        voln_pl += 1
print(f"Volnost noun forms: total={len(voln_n)}, plural/oblique={voln_pl}, singular nominative/accusative={voln_sg}")

print("\n--- VERBS GOVERNING VOLNOST ---")
verbs = ['заховати', 'уживати', 'заживати', 'порушити', 'потвердити', 'отбирати', 'отводити', 'привлащати', 'гадувати', 'примножити', 'обваровати', 'держати']
for v in voln_n:
    ctx = v['ctx'].lower()
    found = [vb for vb in verbs if vb in ctx]
    if found:
        print(f"[{v['src']}] verb={found} -> {v['ctx'][:80]}")

print("\n--- ADJECTIVES MODIFYING VOLNOST ---")
adjs = ['шляхец', 'хрестіян', 'посполит', 'давн', 'стародавн', 'войсков', 'військ', 'руськ', 'козац']
for v in voln_n:
    ctx = v['ctx'].lower()
    found = [a for a in adjs if a in ctx]
    if found:
        print(f"[{v['src']}] adj={found} -> {v['ctx'][:80]}")

