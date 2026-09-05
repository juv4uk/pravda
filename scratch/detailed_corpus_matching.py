import json
import re

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

# Let's inspect why many tokens returned 0 matched constructions.
# Look at the actual context of unassigned VOLN tokens:
unassigned_v = []
for t in voln:
    ctx = t['ctx']
    ctx_l = ctx.lower()
    # Check if coordination
    is_coord = any(k in ctx_l for k in ['прав', 'praw', 'свобод', 'swobod', 'привил', 'przywilei', 'звыча', 'zwyczaj', 'поряд'])
    # Check if prep 'при'
    is_pri = 'при ' in ctx_l or 'przy ' in ctx_l
    # Check if governing verb
    vbs = [v for v in ['захова', 'зостав', 'потвер', 'конфирм', 'обваров', 'нада', 'поруш', 'поламат', 'отбира', 'отвод', 'ужив', 'зажив', 'gaudere', 'весел', 'привлащ', 'підняв'] if v in ctx_l]
    unassigned_v.append({
        'id': t['id'],
        'src': t['src'],
        'loc': t['loc'],
        'form': t['form'],
        'is_coord': is_coord,
        'is_pri': is_pri,
        'verbs': vbs,
        'ctx': ctx
    })

print(f"Total analyzed VOLN tokens: {len(unassigned_v)}")
print("Sample of first 10:")
for x in unassigned_v[:10]:
    print(f"[{x['id']} | {x['src']} | {x['loc']}] FORM={x['form']} | coord={x['is_coord']} | pri={x['is_pri']} | verbs={x['verbs']}")
    print(f"   CTX: {x['ctx'][:80]}")

