import json

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

from scratch.map_every_token import audit_voln_token, audit_svob_token

unassigned_voln = [t for t in voln if len(audit_voln_token(t)) == 0]
print(f"Unassigned VOLN: {len(unassigned_voln)}")
for t in unassigned_voln[:10]:
    print(f"[{t['id']} | {t['src']} | {t['loc']}] FORM={t['form']}")
    print(f"   CTX: {t['ctx']}")

unassigned_svob = [t for t in svob if len(audit_svob_token(t)) == 0]
print(f"\nUnassigned SVOB: {len(unassigned_svob)}")
for t in unassigned_svob[:10]:
    print(f"[{t['id']} | {t['src']} | {t['loc']}] FORM={t['form']} | POS={t['pos']}")
    print(f"   CTX: {t['ctx']}")

