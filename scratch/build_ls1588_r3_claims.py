import re
import sys
import os

from meta_r3_part1 import meta_r3
from meta_r3_part2 import meta_r3_p2

all_meta = {**meta_r3, **meta_r3_p2}

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/SRC-LS-1588-MAMONICZ-TRANSCRIPTION.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()[780:1161]

art_indices = []
for i, l in enumerate(lines):
    m = re.search(r"===\s*Артыкулъ\s+(\d+)", l)
    if m:
        art_indices.append((int(m.group(1)), i))

articles_data = []
for idx, (num, start_line) in enumerate(art_indices):
    end_line = art_indices[idx+1][1] if idx+1 < len(art_indices) else len(lines)
    chunk = lines[start_line:end_line]
    title = ""
    body_lines = []
    for l in chunk[1:]:
        sl = l.strip()
        if not sl: continue
        if not title:
            title = sl
        else:
            body_lines.append(sl)
    body = "\n\n".join(body_lines)
    articles_data.append((num, title, body))

output = []
output.append("## 9. Литовський Статут 1588 року — Розділ 3: «О волностяхъ шляхетъскихъ и о розмноженью великого князства литовского» (Повний блок, Усі 51 артикул)")
output.append("---\n")
output.append("**Свідок:** `WIT-LS-1588-MAMONICZ-PRINCEPS` (Стародрук Віленської друкарні Мамоничів 1588 р.; видання АН БССР, Мінськ, 1989).")
output.append("\n**Принцип розмежування:** Усі 51 артикул Третього розділу Статуту в строгому порядку слідування тексту. Повна відсутність інтерпретацій та сучасної термінології (`INTERPRETATION: EMPTY`).")
output.append("\n---\n")

for num, title, body in articles_data:
    cid = f"HC-LS1588-R3-{num:03d}"
    m = all_meta[num]
    
    # Format quote with markdown blockquote
    quote_lines = [f"  > «{title}"]
    if body:
        quote_lines.append(f"  \n  {body}»")
    else:
        quote_lines[0] += "»"
    quote_text = "\n".join(quote_lines)
    
    card = f"""### {cid}
- **CLAIM-ID:** `{cid}`
- **WITNESS-ID:** `WIT-LS-1588-MAMONICZ-PRINCEPS`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **LOCATOR:** Розділ 3, Артыкулъ {num} (Видання АН БССР 1989 / Мамоничі 1588, с. 63–112)
- **EXACT-QUOTE:**
{quote_text}
- **LEXICAL-TERMS:** `{m['terms']}`
- **GRAMMATICAL-ACTOR:** {m['actors']}
- **TEXTUAL-OPERATOR:** `{m['operators']}`
- **TEXTUAL-OBJECT:** {m['object']}
- **INTERPRETATION:** `EMPTY`

---
"""
    output.append(card)

full_md = "\n".join(output)

with open('/home/agents/GitHub/pravda/scratch/LS1588_R3_GENERATED.md', 'w', encoding='utf-8') as f:
    f.write(full_md)

print("Generated full LS 1588 Rozdil 3 markdown block with", len(articles_data), "claims!")
