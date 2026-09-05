import json

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

from scratch.generate_integrity_audit import match_frames

voln_audited = {t['id']: match_frames(t, 'VOLN') for t in voln}
svob_audited = {t['id']: match_frames(t, 'SVOB') for t in svob}

data = {
    'VOLN': voln,
    'SVOB': svob,
    'voln_audited': voln_audited,
    'svob_audited': svob_audited
}

with open('scratch/audit_instances_payload.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved scratch/audit_instances_payload.json")
