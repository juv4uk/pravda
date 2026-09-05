import re
from collections import Counter

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

print(f"Loaded SVOBOD: {len(svob)}")
print(f"Loaded VOLN_NOUN: {len(voln_n)}")

# 1. Forms breakdown
def analyze_forms(recs, title):
    print(f"\n=== FORMS BREAKDOWN: {title} ===")
    forms = Counter(r['form'] for r in recs)
    for f, c in forms.most_common():
        print(f"  {f}: {c}")

analyze_forms(svob, "SVOBOD")
analyze_forms(voln_n, "VOLN_NOUN")

# 2. Witness breakdown
def analyze_witnesses(recs, title):
    print(f"\n=== WITNESS BREAKDOWN: {title} ===")
    wits = Counter(r['src'] for r in recs)
    for w, c in wits.most_common():
        print(f"  {w}: {c}")

analyze_witnesses(svob, "SVOBOD")
analyze_witnesses(voln_n, "VOLN_NOUN")

# 3. Co-occurrence analysis
print("\n=== CO-OCCURRENCE: PRAVA, VOLNOSTI, SVOBODY ===")
co_occur = []
for v in voln_n:
    ctx = v['ctx'].lower()
    if 'свобод' in ctx or 'swobod' in ctx:
        co_occur.append(('VOLN_RECORD', v['id'], v['src'], v['loc'], v['ctx']))

for s in svob:
    ctx = s['ctx'].lower()
    if 'волност' in ctx or 'wolnoś' in ctx:
        co_occur.append(('SVOB_RECORD', s['id'], s['src'], s['loc'], s['ctx']))

print(f"Total co-occurrence hits: {len(co_occur)}")
for hit in co_occur:
    print(f"[{hit[0]} | {hit[1]} | {hit[2]} | {hit[3]}] -> {hit[4]}")

