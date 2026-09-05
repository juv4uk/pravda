import json

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

print("=== SAME-SENTENCE CO-OCCURRENCES IN CORPUS ===")

# Check exact sentences where both roots co-occur
hits = []
for v in voln:
    for s in svob:
        if v['src'] == s['src'] and v['loc'] == s['loc']:
            hits.append((v, s))

print(f"Total matching row hits: {len(hits)}")
for v, s in hits:
    print(f"[{v['src']} | {v['loc']}]")
    print(f"  VOLN: {v['form']} ({v['num']}, {v['case']})")
    print(f"  SVOB: {s['form']} ({s['pos']}, {s['num']}, {s['case']})")
    print(f"  CTX: {v['ctx']}")
    print("-" * 50)

