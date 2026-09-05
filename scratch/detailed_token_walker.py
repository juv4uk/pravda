import json

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

# Print all 88 VOLN contexts to see their true construction families
for i, t in enumerate(voln, 1):
    print(f"[{i:02d}] {t['id']} | {t['src']} | {t['loc']} | FORM={t['form']}")
    print(f"     CTX: {t['ctx']}")

