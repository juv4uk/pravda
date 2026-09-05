# -*- coding: utf-8 -*-
import sys
sys.path.append('scripts')
from build_pure_rp_short_atoms import atoms

def format_atom(a):
    lines = [
        f"### {a['CLAIM-ID']}",
        f"- **CLAIM-ID:** `{a['CLAIM-ID']}`",
        f"- **WITNESS-ID:** `{a['WITNESS-ID']}`",
        f"- **FIDELITY:** `{a['FIDELITY']}`",
        f"- **ARTICLE:** {a['ARTICLE']}"
    ]
    if a.get('PARALLEL-ARTICLE'):
        lines.append(f"- **PARALLEL-ARTICLE:** {a['PARALLEL-ARTICLE']}")
    lines.extend([
        f"- **LOCATOR:** {a['LOCATOR']}",
        f"- **EXACT-QUOTE:**\n  > {a['EXACT-QUOTE']}",
        f"- **LEXICAL-TERMS:** `{a['LEXICAL-TERMS']}`",
        f"- **GRAMMATICAL-ACTOR:** {a['GRAMMATICAL-ACTOR']}",
        f"- **TEXTUAL-OPERATOR:** `{a['TEXTUAL-OPERATOR']}`",
        f"- **TEXTUAL-OBJECT:** {a['TEXTUAL-OBJECT']}",
        f"- **TEXTUAL-CONDITION:** {a['TEXTUAL-CONDITION']}",
        f"- **TEXTUAL-CONSEQUENCE:** {a['TEXTUAL-CONSEQUENCE']}",
        f"- **INTERPRETATION:** `{a['INTERPRETATION']}`"
    ])
    return "\n".join(lines)

header = """## 6. Еталонний повний блок: Руська Правда (Коротка редакція) — Усі статті 1–43 (Академічний список)

**Свідок:** `WIT-RP-SHORT-ACADEMIC` (Академічний список половини XV ст., вид.: Російське законодавство X–XX ст., Т. 1. М., 1984, с. 47–49).  
**Принцип екстракції:** Повна суцільна екстракція всіх 43 статей джерела з послідовною атомарною декомпозицією на основі зміни CONDITION / ACTOR / OPERATOR / OBJECT / CONSEQUENCE (65 текстових атомів). Чистий extraction-layer (`INTERPRETATION: EMPTY`), суворе дотримання автентичних source-near формулювань без модерної парафрази (0 modern legal terms, 0 paraphrase drift hits), послідовна нумерація за свідком.

---
"""

formatted_atoms = "\n\n---\n\n".join(format_atom(a) for a in atoms)
full_block = header + "\n" + formatted_atoms + "\n\n---\n\n"

with open("scratch/purified_section6.md", "w", encoding="utf-8") as f:
    f.write(full_block)

print(f"Generated {len(atoms)} purified RP Short atoms in scratch/purified_section6.md")
