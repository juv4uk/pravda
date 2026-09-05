from meta_r3_part1 import meta_r3
from meta_r3_part2 import meta_r3_p2
from check_forbidden_terms import check_text

all_meta = {**meta_r3, **meta_r3_p2}
assert len(all_meta) == 51, f"Expected 51 items, got {len(all_meta)}"

violations = 0
for num, m in sorted(all_meta.items()):
    for field in ['actors', 'operators', 'object', 'terms']:
        hits = check_text(m[field])
        if hits:
            print(f"Violation in Art {num} field {field}: {hits} -> {m[field]}")
            violations += 1

if violations == 0:
    print("ALL 51 METADATA BLOCKS PASSED LINTER WITH ZERO VIOLATIONS!")
else:
    print(f"Total violations found: {violations}")
