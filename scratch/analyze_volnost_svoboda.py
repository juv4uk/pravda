import re

def parse_inventory(path):
    records = []
    current_family = None
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line_str = line.strip()
            if line_str.startswith('### ROOT-FAMILY:'):
                current_family = line_str.split(':')[1].strip()
            elif line_str.startswith('|') and not line_str.startswith('| Record ID') and not line_str.startswith('|---'):
                parts = [p.strip() for p in line_str.split('|')[1:-1]]
                if len(parts) >= 8:
                    records.append({
                        'rec_id': parts[0],
                        'family': current_family,
                        'corpus': parts[1],
                        'unit': parts[2],
                        'matched_form': parts[3],
                        'lemma': parts[4],
                        'pos': parts[5],
                        'status': parts[6],
                        'context': parts[7]
                    })
    return records

recs = parse_inventory('semantics/CROSS-CORPUS-LEXEME-INVENTORY.md')
voln_recs = [r for r in recs if r['family'] == 'VOLN-']
svob_recs = [r for r in recs if r['family'] == 'SVOBOD-']

print(f"Total VOLN-: {len(voln_recs)}")
print(f"Total SVOBOD-: {len(svob_recs)}")

print("\n--- VOLN by POS and Corpus ---")
voln_pos = {}
for r in voln_recs:
    key = (r['corpus'], r['pos'])
    voln_pos[key] = voln_pos.get(key, 0) + 1
for k, v in sorted(voln_pos.items()):
    print(f"{k}: {v}")

print("\n--- SVOBOD by POS and Corpus ---")
svob_pos = {}
for r in svob_recs:
    key = (r['corpus'], r['pos'])
    svob_pos[key] = svob_pos.get(key, 0) + 1
for k, v in sorted(svob_pos.items()):
    print(f"{k}: {v}")

print("\n--- SVOBOD matching forms ---")
for r in svob_recs:
    print(f"[{r['corpus']}] {r['matched_form']} ({r['pos']}) -> {r['context'][:80]}")

