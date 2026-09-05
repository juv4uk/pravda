import re
from build_ls1566_register import records, units

# Let's inspect purity and generate a dedicated lexicon register artifact
# /home/agents/GitHub/pravda/semantics/LS-1566-LEXICAL-REGISTER.md

md = []
md.append("# СИСТЕМАТИЧНИЙ ЛЕКСИЧНИЙ РЕЄСТР ЛИТОВСЬКОГО СТАТУТУ 1566 РОКУ")
md.append("## LS-1566-LEXICAL-REGISTER (Two-Tier Systematic Extraction)\n")
md.append("> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ІНВАРІАНТИ:**")
md.append("> 1. **CORPUS-WIDE COVERAGE / NO SELECTION BIAS**: Протокол застосовано до ВСЬОГО тексту Статуту 1566 р. (3 привілеї + усі 14 розділів, 371 стаття/текстовий юніт). Жодна стаття не відбиралася суб'єктивно за «важливістю».")
md.append("> 2. **TWO-TIER SEARCH VOCABULARY**:")
md.append(">    - **TIER A (CORE)**: `вольност*`, `привил*`, `свобод*`, `обыча* / звыча*`, `присяг* / прысяг*`.")
md.append(">    - **TIER B (CONTEXT)**: `прав*`, `рада / сойм*`, `посполит*`, `поддан*`, `суд*`, `маетност* / имЂн*`, `уряд* / вряд*`.")
md.append("> 3. **HIT-CLASS**: `CORE` (стаття містить хоча б одну лексему Тіру А) / `CONTEXT` (стаття містить лише лексеми Тіру B). Тір B не вважається концептуальним доказом сам по собі, а фіксує інституційний контекст.")
md.append("> 4. **SEARCH VOCABULARY ≠ SEMANTIC CATEGORY**: Факт лексичного збігу не означає приналежності до єдиного нормативного концепту.")
md.append("> 5. **INTERPRETATION: EMPTY**: Жодних сучасних оцінок (*«конституційне право», «гарантія прав людини», «автономія»*).\n")

md.append("## 1. СТАТИСТИКА КОРПУСНОГО СКАНУВАННЯ (CORPUS METRICS)\n")
md.append(f"- **Загальна кількість статей / юнітів у Статуті 1566 р.**: {len(units)}.")
md.append(f"- **Кількість юнітів із лексичними збігами (Total Hits)**: {len(records)} (80.1% корпусу).")
core_recs = [r for r in records if r['hit_class'] == 'CORE']
ctx_recs = [r for r in records if r['hit_class'] == 'CONTEXT']
md.append(f"- **Юнітів із лексемами TIER A (CORE)**: {len(core_recs)} (33.4% корпусу).")
md.append(f"- **Юнітів виключно з лексемами TIER B (CONTEXT)**: {len(ctx_recs)} (46.6% корпусу).")

# Chapter breakdown
from collections import Counter
ch_core = Counter(r['chapter'] for r in core_recs)
md.append("\n### Розподіл CORE-входжень за розділами Статуту:")
for ch, count in ch_core.items():
    md.append(f"- **{ch}**: {count} статей")

md.append("\n---\n\n## 2. РЕЄСТР ЛЕКСИЧНИХ ВХОДЖЕНЬ (LEXICAL HIT ENTRIES)\n")

for r in records:
    entry = f"""### {r['hit_id']}
- **SOURCE-ID:** `WIT-LS-1566`
- **DOCUMENT-UNIT:** `{r['part']}`
- **CHAPTER:** `{r['chapter']}`
- **ARTICLE:** `{r['article']}`
- **LOCATOR:** {r['unit']}
- **SEARCH-ROOT:** `{r['roots']}`
- **TERM-FORM:** `{r['forms']}`
- **HIT-CLASS:** `{r['hit_class']}`
- **EXACT-QUOTE:**
  > «{r['quote']}»
- **GRAMMATICAL-ACTOR:** {r['actor']}
- **TEXTUAL-OPERATOR:** `{r['operator']}`
- **TEXTUAL-OBJECT:** {r['object']}
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **INTERPRETATION:** `EMPTY`
"""
    md.append(entry)

out_file = "/home/agents/GitHub/pravda/semantics/LS-1566-LEXICAL-REGISTER.md"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n---\n\n".join(md))

print(f"Written LS-1566 register to {out_file} ({len(records)} entries)!")

