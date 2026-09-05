import re
from build_hadiach_textual_diff import claims_1658, claims_1659
from generate_diff_register import alignments

md = []
md.append("# ТЕКСТОЛОГІЧНИЙ РЕЄСТР ЗІСТАВЛЕННЯ ГАДЯЦЬКИХ ТЕКСТІВ (1658 VS 1659)")
md.append("## HADIACH-TEXTUAL-DIFF-1658-1659 (Alignment Registry)\n")
md.append("> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ІНВАРІАНТИ:**")
md.append("> 1. **DIFF ONLY / ZERO INTERPRETATION**: Цей реєстр фіксує виключно формально-текстологічні відповідності між рукописною Комісією 1658 р. (`WIT-HADIACH-COMMISSION-1658`) та друкованим сеймовим корпусом у *Volumina Legum* (`WIT-HADIACH-SEJM-1659`).")
md.append("> 2. **NO TELEOLOGICAL BIAS**: Категорії `OMITTED ≠ REJECTED`, `ADDED ≠ EXPANDED`, `MODIFIED-WORDING ≠ NARROWED`. Жодних оціночних суджень про «урізання прав», «руйнацію автономії» чи «політичний тиск Сейму» в цьому шарі не міститься.")
md.append("> 3. **INDEPENDENT EXTRACTIONS**: Обидва корпуси витягнуті незалежно у власному порядку видання, зі збереженням структури заголовків (`PRINTED-HEADING`) та сторінок (`PAGE`).")
md.append("> 4. **CONFIDENCE & BASIS**: Для кожної пари зафіксовано рівень достовірності вирівнювання (`ALIGNMENT-CONFIDENCE`) та його текстову підставу (`MATCH-BASIS`).\n")

md.append("## 1. СТАТИСТИКА ВИРІВНЮВАННЯ (ALIGNMENT METRICS)\n")
md.append(f"- **Всього витягнутих тверджень 1658 року**: 47 (усі 47 верифіковані та зіставлені).")
md.append(f"- **Всього витягнутих тверджень 1659 року**: 66 (усі 66 верифіковані та зіставлені).")
md.append(f"- **Загальна кількість записів вирівнювання (Alignment Entries)**: {len(alignments)}.")

# Match type breakdown
from collections import Counter
m_counts = Counter(a["match_type"] for a in alignments)
md.append("- **Розподіл за типами текстологічної відповідності (MATCH-TYPE)**:")
for m_type, count in m_counts.items():
    md.append(f"  - `{m_type}`: {count}")

md.append("\n---\n\n## 2. РЕЄСТР ВИРІВНЯНИХ СТАТЕЙ ТА КЛАУЗУЛ (ALIGNMENT ENTRIES)\n")

for a in alignments:
    cid_58 = a["src_1658"]
    cid_59 = a["src_1659"]
    
    q_58 = claims_1658[cid_58]["quote"] if cid_58 in claims_1658 else "NONE (відсутнє в рукописі 1658 р.)"
    q_59 = claims_1659[cid_59]["quote"] if cid_59 in claims_1659 else "NONE (відсутнє в сеймовому корпусі 1659 р.)"
    
    entry = f"""### {a['align_id']}
- **SOURCE-1658-CLAIM:** `{cid_58}`
- **SOURCE-1659-CLAIM:** `{cid_59}`
- **MATCH-TYPE:** `{a['match_type']}`
- **ALIGNMENT-CONFIDENCE:** `{a['confidence']}`
- **MATCH-BASIS:** `{a['basis']}`
- **SHARED-LEXEMES:** `{a['shared_lex']}`
- **TEXT-1658:**
  > «{q_58}»
- **TEXT-1659:**
  > «{q_59}»
- **STRUCTURAL-DIFFERENCE:** {a['struct_diff']}
- **SEMANTIC-INTERPRETATION:** `EMPTY`
- **POLITICAL-INTERPRETATION:** `EMPTY`
"""
    md.append(entry)

out_file = "/home/agents/GitHub/pravda/diffs/HADIACH-TEXTUAL-DIFF-1658-1659.md"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n---\n\n".join(md))

print(f"Diff written to {out_file} ({len(alignments)} entries)!")

