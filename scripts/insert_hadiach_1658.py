import re
from build_hadiach_1658_claims import items

with open("/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md", "r", encoding="utf-8") as f:
    content = f.read()

# Generate markdown for all 47 items
md_blocks = []
md_blocks.append("\n## 3.4. Гадяцька комісія 1658 (Повний текст, 47 тверджень у порядку документа)")
md_blocks.append("**Свідок:** `WIT-HADIACH-COMMISSION-1658` (Pakta Hadziackie autentyczne, 16 вересня 1658 р.).")
md_blocks.append("**Принцип розмежування:** Усі 6 статей, преамбула та заключні клаузули в порядку слідування тексту. Поле `TEXTUAL-SPEAKER` фіксує суб'єкта клаузули (`COMMISSION`, `COSSACK SIDE`, `CROWN SIDE`, `JOINT FORMULA`). Жодної сучасної термінології.\n")

for it in items:
    block = f"""### {it['id']}
- **CLAIM-ID:** `{it['id']}`
- **WITNESS-ID:** `WIT-HADIACH-COMMISSION-1658`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **LOCATOR:** {it['locator']}
- **TEXTUAL-SPEAKER:** `{it['speaker']}`
- **EXACT-QUOTE:**
  > «{it['quote']}»
- **LEXICAL-TERMS:** `{it['terms']}`
- **GRAMMATICAL-ACTOR:** {it['actor']}
- **TEXTUAL-OPERATOR:** `{it['operator']}`
- **TEXTUAL-OBJECT:** {it['object']}
- **INTERPRETATION:** `EMPTY`
"""
    md_blocks.append(block)

full_hadiach_md = "\n---\n\n".join(md_blocks)

# We want to replace the old single pilot claim `### HC-HADIACH-1658-001` or insert before `### HC-HADIACH-SEJM-1659-001`.
# Let's see what is around HC-HADIACH-1658-001
pattern = r"### HC-HADIACH-1658-001\n.*?(?=### HC-HADIACH-SEJM-1659-001)"
match = re.search(pattern, content, re.DOTALL)
if match:
    new_content = content[:match.start()] + full_hadiach_md + "\n\n---\n\n" + content[match.end():]
    with open("/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully replaced HC-HADIACH-1658-001 with full 47 claims!")
else:
    print("Could not find replacement pattern!")

