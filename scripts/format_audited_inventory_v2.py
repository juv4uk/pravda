# -*- coding: utf-8 -*-
"""
Writes semantics/CROSS-CORPUS-LEXEME-INVENTORY.md (AUDITED INVENTORY v2)
and semantics/LEXEME-AUDIT-LEDGER.md

Status: NO KNOWN FALSE MATCHES UNDER CURRENT AUDIT RULES
"""
import json
from collections import Counter

with open('scratch/inventory_v2.json', 'r', encoding='utf-8') as f:
    recs = json.load(f)

with open('scratch/audit_ledger_v2.json', 'r', encoding='utf-8') as f:
    ledger = json.load(f)

sources = ['SRC-RP-SHORT', 'SRC-RP-EXP', 'SRC-LS-1566', 'SRC-LS-1588', 'SRC-HADIACH-1658', 'SRC-HADIACH-1659', 'SRC-MARCH-1654', 'SRC-ORLYK-1710']
families = sorted(list(set(r['root_family'] for r in recs)))

matrix = {fam: {src: 0 for src in sources} for fam in families}
for r in recs:
    matrix[r['root_family']][r['source_id']] += 1

# Generate Inventory Markdown
md = []
md.append("""# СИСТЕМАТИЧНИЙ КРОС-КОРПУСНИЙ РЕЄСТР ЛЕКСЕМ (ВЕРСІЯ 2)
## CROSS-CORPUS-LEXEME-INVENTORY v2 (Audited Derivational Groupings & Locators)

> **СТАТУС АУДИТУ:** `NO KNOWN FALSE MATCHES UNDER CURRENT AUDIT RULES`
> **DECISION-LAYER:** `AUDIT`

> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ЕПІСТЕМОЛОГІЧНІ ІНВАРІАНТИ:**
> 1. **ROOT-FAMILY = SEARCH / DERIVATIONAL GROUPING ONLY**:
>    ```text
>    ROOT-FAMILY (Search Grouping)
>                 ≠
>               LEMMA
>                 ≠
>              CONCEPT
>                 ≠
>         ETYMOLOGICAL CLAIM
>    ```
>    - Назва групи (наприклад, `PRAVO`, `VOLN_NOUN`, `ROTA_OATH`) є суто технічним пошуковим класифікатором вимірювального інструмента, а не твердженням про єдине історичне чи етимологічне значення.
> 2. **THREE-TIER ISOLATION PRINCIPLE**:
>    ```text
>    ORTHOGRAPHIC NORMALIZATION
>                ≠
>        LEXICAL IDENTITY
>                ≠
>        SEMANTIC IDENTITY
>    ```
>    - Категорично **ЗАБОРОНЕНО** об'єднувати різні морфологічні чи словотвірні родини (*правда* і *право*; *вольность* і *вольный/вольно*; *обычай* і *звычай*; *договоръ*, *пактъ* і *трактатъ*; *стаття* і *артикулъ*; *рота* і *присяга*; *обида* і *шкода/злочин*) у спільне поняття.
> 3. **EXPLICIT UNICODE HANDLING**:
>    - Інструмент підтримує повні історичні кодові позиції кирилиці, зокрема обидва графічні варіанти ятя: U+0402 (`Ђ`) у тексті Статуту 1566 року та U+0463 (`ѣ`) у Статуті 1588 року та інших пам'ятках.
> 4. **REPRESENTATION INVARIANTS**:
>    - `LEMMA-CANDIDATE: UNKNOWN` (жодної модернізації чи передчасної нормалізації).
>    - `SEMANTIC-GROUP: EMPTY`
>    - `INTERPRETATION: EMPTY`
> 5. **CORPUS COVERAGE**: Охоплено 8 дипломатичних свідків (L1 digital derivatives) від XI/XII–XV ст. до 1710 року:
>    - `SRC-RP-SHORT`: Руська Правда (Коротка редакція, Академічний список)
>    - `SRC-RP-EXP`: Руська Правда (Простора редакція, Троицький список)
>    - `SRC-LS-1566`: Литовський Статут 1566 року (усі 14 розділів)
>    - `SRC-LS-1588`: Литовський Статут 1588 року (усі 14 розділів)
>    - `SRC-HADIACH-1658`: Гадяцька комісія 1658 року
>    - `SRC-HADIACH-1659`: Гадяцький сеймовий акт 1659 року (Volumina Legum)
>    - `SRC-MARCH-1654`: Березневі статті 1654 року (Посольський список)
>    - `SRC-ORLYK-1710`: Бендерська конституція Пилипа Орлика 1710 року
>    *(Зборівський комплекс 1649 р. знаходиться на етапі підготовки окремих свідків і не включений).*

---

## 1. ЗВЕДЕНА МАТРИЦЯ РОЗПОДІЛУ ЛЕКСЕМ (AUDITED DISTRIBUTION MATRIX v2)

""")

# Table
header_row = "| ROOT-FAMILY (Search Group) | " + " | ".join(sources) + " | Всього |"
separator_row = "|---|" + "---|" * (len(sources) + 1)
md.append(header_row)
md.append(separator_row)

for fam in families:
    row = [str(matrix[fam][src]) for src in sources]
    total = sum(matrix[fam][src] for src in sources)
    md.append(f"| **`{fam}`** | " + " | ".join(row) + f" | **{total}** |")

total_by_src = [str(sum(matrix[fam][src] for fam in families)) for src in sources]
grand_total = len(recs)
md.append(f"| **РАЗОМ ПО СВІДКАХ** | " + " | ".join(total_by_src) + f" | **{grand_total}** |\n")

md.append("""---

## 2. РЕЄСТР ВЕРИФІКОВАНИХ СЛОВОВЖИТКІВ (AUDITED ENTRIES)

""")

for r in recs:
    entry = f"""### {r['id']}
- **LEX-ID:** `{r['id']}`
- **SOURCE-ID:** `{r['source_id']}`
- **WITNESS-ID:** `{r['witness_id']}`
- **LOCATOR:** {r['locator']}
- **SOURCE-FORM:** `{r['source_form']}`
- **EXACT-CONTEXT:**
  > {r['context']}
- **ROOT-FAMILY:** `{r['root_family']}`
- **POS-CANDIDATE:** `{r['pos_candidate']}`
- **LEMMA-CANDIDATE:** `{r['lemma_candidate']}`
- **DECISION-LAYER:** `{r['decision_layer']}`
- **SEMANTIC-GROUP:** `{r['semantic_group']}`
- **INTERPRETATION:** `{r['interpretation']}`
"""
    md.append(entry)

out_inv = 'semantics/CROSS-CORPUS-LEXEME-INVENTORY.md'
with open(out_inv, 'w', encoding='utf-8') as f:
    f.write("\n---\n\n".join(md))
print(f"Written {len(recs)} audited entries to {out_inv}")

# Generate Audit Ledger Markdown
ledger_md = []
ledger_md.append("""# РЕЄСТР АУДИТОРСЬКИХ РІШЕНЬ (AUDIT LEDGER v2)
## LEXEME-AUDIT-LEDGER (Traceability of Inclusions & Exclusions)

> **СТАТУС:** `AUDIT TRACEABILITY LEDGER`
> **DECISION-LAYER:** `AUDIT`
> Кожен рядок фіксує точне аудиторське рішення щодо включення або вилучення текстового збігу з переліком підстав (омоніми, метадані, префіксні вилучення іншої лексичної основи).

| SOURCE | ROOT-FAMILY | RAW-HIT | DECISION | REASON | SOURCE-FORM | LOCATOR |
|:---|:---|:---|:---:|:---|:---|:---|
""")

for l in ledger:
    row = f"| `{l['source_id']}` | `{l['family']}` | `{l['raw_hit']}` | **{l['decision']}** | {l['reason']} | `{l['source_form']}` | {l['locator']} |"
    ledger_md.append(row)

out_led = 'semantics/LEXEME-AUDIT-LEDGER.md'
with open(out_led, 'w', encoding='utf-8') as f:
    f.write("\n".join(ledger_md))
print(f"Written {len(ledger)} audit decisions to {out_led}")
