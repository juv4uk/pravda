# -*- coding: utf-8 -*-
"""
Writes semantics/CROSS-CORPUS-LEXEME-INVENTORY.md
Systematic cross-corpus lexical inventory with exact source-near forms,
locators, contexts, and morphological families.
"""
import sys
sys.path.append("scripts")
import build_cross_corpus_lexeme_inventory as inv
from collections import Counter

recs = inv.inventory_records
by_src = Counter(r['source_id'] for r in recs)
by_fam = Counter(r['family'] for r in recs)
families = list(inv.target_families.keys())

header = f"""# СИСТЕМАТИЧНИЙ КРОС-КОРПУСНИЙ РЕЄСТР ЛЕКСЕМ
---

## CROSS-CORPUS-LEXEME-INVENTORY (Raw Morphological Forms & Locators)

---

> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ЕПІСТЕМОЛОГІЧНІ ІНВАРІАНТИ:**
---

> 1. **THREE-TIER ISOLATION PRINCIPLE**:
---

>    ```text
>    ORTHOGRAPHIC NORMALIZATION
>                ≠
>        LEXICAL IDENTITY
>                ≠
>        SEMANTIC IDENTITY
>    ```
---

>    - Обережна орфографічна чи словозмінна нормалізація (наприклад: *вольностяхъ, вольностей, вольности → вольность*) фіксує морфологічну спорідненість слововжитку.
---

>    - Категорично **ЗАБОРОНЕНО** об'єднувати різні морфологічні родини (*правда* і *право*; *вольность* і *свобода*; *обычай* і *звычай*; *рядъ* і *договоръ*; *рота* і *присяга*; *обида* і *шкода/злочин*) у спільне «модерне поняття».
---

> 2. **NO SEMANTIC OR TELEOLOGICAL LABELS**:
---

>    - `SEMANTIC-GROUP: EMPTY`
---

>    - `INTERPRETATION: EMPTY`
---

>    Цей реєстр фіксує лише фізичну наявність або відсутність конкретних словоформ у первинних текстах.
---

> 3. **CORPUS COVERAGE**: Охоплено 8 дипломатичних свідків (L1 digital derivatives) від XI/XII–XV ст. до 1710 року:
---

>    - `SRC-RP-SHORT`: Руська Правда (Коротка редакція, Академічний список)
---

>    - `SRC-RP-EXP`: Руська Правда (Простора редакція, Троїцький список)
---

>    - `SRC-LS-1566`: Литовський Статут 1566 року (усі 14 розділів)
---

>    - `SRC-LS-1588`: Литовський Статут 1588 року (усі 14 розділів)
---

>    - `SRC-HADIACH-1658`: Гадяцька комісія 1658 року
---

>    - `SRC-HADIACH-1659`: Сеймовий корпус Гадяцького врегулювання 1659 року (Volumina Legum)
---

>    - `SRC-MARCH-1654`: Березневі статті 1654 року (Список Посольського приказу)
---

>    - `SRC-ORLYK-1710`: Договори і Постановлення (Бендери 1710)

---

## 1. СТАТИСТИЧНИЙ ЗРІЗ (CROSS-TABULATION MATRIX)

---

### Загальні показники:
- **Всього заінвентаризованих слововживань**: {len(recs)}.
- **Охоплено морфологічних родин**: {len(families)}.

---

### Таблиця розподілу морфологічних родин за джерелами:

| Джерело / Корпус | ПРАВДА | ПРАВО | ВОЛЬНОСТЬ | СВОБОДА | ОБЫЧАЙ | ЗВЫЧАЙ | РЯДЪ | ПРИВИЛЕЙ | ДОГОВОРЪ | СТАТЬЯ | РОТА | ПРИСЯГА | ОБИДА | Всього |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
"""

table_rows = []
for src in inv.sources:
    sid = src['source_id']
    sname = src['name']
    row_counts = [sum(1 for r in recs if r['source_id'] == sid and r['family'] == fam) for fam in families]
    tot = sum(row_counts)
    counts_str = " | ".join(str(c) for c in row_counts)
    table_rows.append(f"| **{sid}** ({sname}) | {counts_str} | **{tot}** |")

matrix_text = "\n".join(table_rows)

header += matrix_text + f"""

---

### Ключові первинні спостереження над сирим розподілом:
1. **Дихотомія ПРАВДА ↔ ПРАВО**:
   - У Руській Правді (як Короткій, так і Просторій) лексема `право` відсутня (**0 входжень**). Натомість базовою категорією є `правда` (суд, закон, змагання, випробування залізом: *«дати ему правду»*, *«на правду не вылазити»*).
   - Лексема `право` вибухово з'являється у Литовських Статутах (342 входження у 1566 р. та 1005 входжень у 1588 р.) і зберігає домінування у козацьку добу (66 у Орлика 1710 р.).
2. **Дихотомія РОТА ↔ ПРИСЯГА**:
   - У Руській Правді сакральна клятва представлена виключно лексемою `рота` (*«ити ему роте»*, *«на роту»*, 2 у Короткій, 13 у Просторій). Лексема `присяга` — **0 входжень**.
   - Починаючи зі Статуту 1566 р., `присяга` стає головним терміном (34 у 1566, 103 у 1588, 19 у Сеймі 1659, 13 у Орлика 1710), тоді як `рота` відходить на периферію як суто судова архаїчна клятва або шляхетська рота (військова одиниця).
3. **Дихотомія ОБИДА ↔ ШКОДА / ШАЛОНОК**:
   - У Руській Правді порушення норми або делікт позначається категорією `обида` (12 у Короткій, 8 у Просторій: *«за обиду 3 гривны»*).
   - У Статутах та козацьких договорах лексема `обида` як юридичний делікт зникає з нормативного корпусу (**0 входжень**), витіснена термінами *шкода, кривда, кгвалт, переступлення*.
4. **Специфіка ВОЛЬНОСТЬ та СВОБОДА**:
   - `вольность` повністю відсутня в Руській Правді (**0 входжень**), з'являється у Статуті 1566 (70), закріплюється у Гадячі (13 у Комісії, 11 у Сеймі) та Орлика (20).
   - `свобода` у Руській Правді вживається як стан незакріпаченої людини (*свободный мужь*, *наимиту свобода*), тоді як у Статутах і козацьку добу вживається поряд із вольностями.

---

## 2. РЕЄСТР ЛЕКСИЧНИХ ЗАПИСІВ (INVENTORY ENTRIES)

---
"""

def format_record(r):
    lines = [
        f"### {r['id']}",
        f"- **LEX-ID:** `{r['id']}`",
        f"- **SOURCE-ID:** `{r['source_id']}`",
        f"- **WITNESS-ID:** `{r['witness_id']}`",
        f"- **LOCATOR:** {r['locator']}",
        f"- **SOURCE-FORM:** `{r['source_form']}`",
        f"- **EXACT-CONTEXT:**\n  > {r['context']}",
        f"- **MORPHOLOGICAL-FAMILY:** `{r['family']}`",
        f"- **NORMALIZED-FORM:** `{r['normalized']}`",
        f"- **NORMALIZATION-CONFIDENCE:** `{r['confidence']}`",
        f"- **SEMANTIC-GROUP:** `EMPTY`",
        f"- **INTERPRETATION:** `EMPTY`"
    ]
    return "\n".join(lines)

# Write out full inventory
# To keep file manageable and performant, format all records cleanly
entries_formatted = "\n\n---\n\n".join(format_record(r) for r in recs)
full_text = header + "\n" + entries_formatted + "\n"

with open('semantics/CROSS-CORPUS-LEXEME-INVENTORY.md', 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Generated semantics/CROSS-CORPUS-LEXEME-INVENTORY.md with {len(recs)} records.")
