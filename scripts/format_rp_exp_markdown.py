# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('scripts')
from build_atoms_data_part1 import atoms_part1
from build_atoms_data_part2 import atoms_part2
from build_atoms_data_part3 import atoms_part3
from build_atoms_data_part4 import atoms_part4
from build_atoms_data_part5 import atoms_part5

with open('/home/agents/GitHub/pravda/scratch/rp_exp_raw_articles.json', 'r', encoding='utf-8') as f:
    raw_articles = json.load(f)

art_dict = {a[0]: (a[1], a[2]) for a in raw_articles}
all_atoms = atoms_part1 + atoms_part2 + atoms_part3 + atoms_part4 + atoms_part5

output_lines = []
output_lines.append("## 7. Еталонний повний блок: Руська Правда (Простора редакція) — Усі статті 1–115 (Троїцький список)\n")
output_lines.append("**Свідок:** `WIT-RP-EXP-TROITSKY` (Троїцький список другої половини XIV ст., вид.: Російське законодавство X–XX ст., Т. 1. М., 1984, с. 64–73).  ")
output_lines.append("**Принцип екстракції:** Суцільна послідовна екстракція всіх 115 статей свідка в порядку документа з атомарною декомпозицією на основі зміни CONDITION / ACTOR / OPERATOR / OBJECT / CONSEQUENCE (160 текстових атомів). Чистий extraction-layer (`INTERPRETATION: EMPTY`), збереження лексики та назв категорій/осіб/процедур джерела, нумерація за свідком із паралельним зазначенням нумерації Грекова/Тихомирова там, де вона надійно встановлена.\n")
output_lines.append("---\n")

for a in all_atoms:
    cid = a['claim_id']
    art_no = a['art']
    line_no, _ = art_dict[art_no]
    par = a['par']
    
    output_lines.append(f"### {cid}")
    output_lines.append(f"- **CLAIM-ID:** `{cid}`")
    output_lines.append(f"- **WITNESS-ID:** `WIT-RP-EXP-TROITSKY`")
    output_lines.append(f"- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`")
    output_lines.append(f"- **ARTICLE:** Артикул {art_no}")
    if par:
        output_lines.append(f"- **PARALLEL-ARTICLE:** `{par}`")
    output_lines.append(f"- **LOCATOR:** Троїцький список, ст. {art_no} (SRC-RP-EXP-DIPLOMATIC.txt, рядок {line_no})")
    output_lines.append(f"- **EXACT-QUOTE:**")
    output_lines.append(f"  > «{a['quote']}»")
    output_lines.append(f"- **GRAMMATICAL-ACTOR:** {a['actor']}")
    output_lines.append(f"- **TEXTUAL-OPERATOR:** `{a['operator']}`")
    output_lines.append(f"- **TEXTUAL-OBJECT:** {a['object']}")
    output_lines.append(f"- **TEXTUAL-CONDITION:** {a['condition']}")
    output_lines.append(f"- **TEXTUAL-CONSEQUENCE:** {a['consequence']}")
    output_lines.append(f"- **LEXICAL-TERMS:** `{a['terms']}`")
    output_lines.append(f"- **INTERPRETATION:** `EMPTY`\n")
    output_lines.append("---\n")

md_content = "\n".join(output_lines)
with open('/home/agents/GitHub/pravda/scratch/rp_exp_claims_block.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Generated Markdown block with {len(all_atoms)} atoms ({len(md_content)} bytes).")
