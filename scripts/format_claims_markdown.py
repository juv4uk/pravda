import sys
import re

from generate_rp_short_register import claims_data, raw_articles

output_lines = []
output_lines.append("## 6. Еталонний повний блок: Руська Правда (Коротка редакція) — Усі статті 1–43 (Академічний список)\n")
output_lines.append("**Свідок:** `WIT-RP-SHORT-ACADEMIC` (Академічний список половини XV ст., вид.: Російське законодавство X–XX ст., Т. 1. М., 1984, с. 47–49).  ")
output_lines.append("**Принцип екстракції:** Суцільна послідовна екстракція 43/43 статей у порядку джерела без лексичного відбору та без вибірковості. Чистий extraction-layer (`INTERPRETATION: EMPTY`).\n")
output_lines.append("---\n")

for c in claims_data:
    art_no = c['art']
    line_no, exact_quote = raw_articles[art_no]
    cid = c['id']
    
    output_lines.append(f"### {cid}")
    output_lines.append(f"- **CLAIM-ID:** `{cid}`")
    output_lines.append(f"- **WITNESS-ID:** `WIT-RP-SHORT-ACADEMIC`")
    output_lines.append(f"- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`")
    output_lines.append(f"- **ARTICLE:** Артикул {art_no}")
    output_lines.append(f"- **LOCATOR:** Академічний список, ст. {art_no} (SRC-RP-SHORT-DIPLOMATIC.txt, рядок {line_no})")
    output_lines.append(f"- **EXACT-QUOTE:**")
    output_lines.append(f"  > «{exact_quote}»")
    output_lines.append(f"- **LEXICAL-TERMS:** `{c['terms']}`")
    output_lines.append(f"- **GRAMMATICAL-ACTOR:** {c['actor']}")
    output_lines.append(f"- **TEXTUAL-OPERATOR:** `{c['operator']}`")
    output_lines.append(f"- **TEXTUAL-OBJECT:** {c['object']}")
    output_lines.append(f"- **INTERPRETATION:** `EMPTY`\n")
    output_lines.append("---\n")

md_block = "\n".join(output_lines)
with open('/home/agents/GitHub/pravda/scratch/rp_short_claims_block.md', 'w', encoding='utf-8') as f:
    f.write(md_block)

print(f"Generated markdown block with {len(claims_data)} claims, size: {len(md_block)} bytes.")
