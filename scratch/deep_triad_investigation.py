import json

with open('scratch/ryad_tokens.json') as f: ryad = json.load(f)
with open('scratch/dogovor_tokens.json') as f: dog = json.load(f)
with open('scratch/pakt_tokens.json') as f: pakt = json.load(f)

print("=== ALL RYAD TOKENS ===")
for t in ryad:
    print(f"[{t['src']} | {t['loc']}] {t['form']} ({t['pos']}) -> {t['ctx']}")

print("\n=== ALL DOGOVOR TOKENS ===")
for t in dog:
    print(f"[{t['src']} | {t['loc']}] {t['form']} ({t['pos']}) -> {t['ctx']}")

print("\n=== ALL PAKT TOKENS ===")
for t in pakt:
    print(f"[{t['src']} | {t['loc']}] {t['form']} ({t['pos']}) -> {t['ctx']}")

