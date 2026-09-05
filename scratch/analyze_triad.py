import json
from collections import Counter

for name in ['ryad', 'dogovor', 'pakt']:
    with open(f'scratch/{name}_tokens.json') as f:
        toks = json.load(f)
    print(f"\n=== {name.upper()} ({len(toks)} tokens) ===")
    by_src = Counter(t['src'] for t in toks)
    for s, cnt in sorted(by_src.items()):
        print(f"  {s}: {cnt}")
    by_form = Counter(t['form'] for t in toks)
    print(f"  Forms: {dict(by_form)}")
    print("  Samples:")
    for t in toks[:3]:
        print(f"    [{t['id']} | {t['src']} | {t['loc']}] FORM={t['form']} -> {t['ctx'][:75]}")

