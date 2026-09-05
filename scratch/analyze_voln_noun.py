import re

with open('scratch/voln_noun_dump.txt', 'r', encoding='utf-8') as f:
    text = f.read()

items = text.split('\n\n')
print(f"Total blocks: {len(items)}")

corpora = {}
for block in items:
    if not block.strip(): continue
    lines = block.strip().split('\n')
    m = re.match(r'\[([^\]]+)\]\s*\[([^\]]+)\]\s*(.*)', lines[0])
    if m:
        rec_id, src, loc = m.group(1), m.group(2), m.group(3)
        form_line = lines[1]
        ctx_line = lines[2]
        corpora.setdefault(src, []).append((rec_id, loc, form_line, ctx_line))

for src, recs in corpora.items():
    print(f"\n=== {src} (count: {len(recs)}) ===")
    for r in recs[:5]:
        print(f"  {r[0]} | {r[1]} | {r[2]} | {r[3][:70]}")
    if len(recs) > 5:
        print(f"  ... and {len(recs)-5} more")

