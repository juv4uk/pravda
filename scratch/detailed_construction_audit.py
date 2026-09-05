import json

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

# Inspect what is inside CONST-VOLN-05
from collections import Counter
import re

coord_contexts = []
for t in voln:
    ctx = t['ctx']
    ctx_l = ctx.lower()
    form = t['form']
    # check verbs
    verbs = []
    for v in ['захова', 'зостав', 'держати', 'ставати', 'потвер', 'конфирм', 'обваров', 'нада', 'поруш', 'поламати', 'отбирати', 'отводити', 'ужив', 'зажив', 'gaudere', 'привлащати', 'підняв']:
        if v in ctx_l:
            verbs.append(v)
    coord_contexts.append((t['src'], t['loc'], form, verbs, ctx[:80]))

print(f"Total analyzed VOLN: {len(coord_contexts)}")
print("Sample with verbs:")
for c in coord_contexts[:15]:
    print(c[0], c[1], c[2], c[3], "-->", c[4])

