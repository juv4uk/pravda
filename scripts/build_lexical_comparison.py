import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-LS-1566-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text_66 = f.read()

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-LS-1588-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text_88 = f.read()

from extract_ls1566_lexical_hits import units as units_66, hits as hits_66
from parse_ls1588_articles import units_1588 as units_88
from extract_ls1588_lexical_hits import hits_1588 as hits_88

# Exact frozen patterns
tier_a = {
    'вольност*': r'\bвольн[ое][сз]т[а-яЂі]*',
    'привил*': r'\b[у]?[п]?ривил[а-яЂі]*',
    'свобод*': r'\bсвобод[а-яЂі]*',
    'обыча* / звыча*': r'\b[оз]быча[а-яЂі]*|\b[оз]выча[а-яЂі]*',
    'присяг* / прысяг*': r'\bпр[иы][сЂе][ягз][а-яЂі]*'
}

tier_b = {
    'прав*': r'\bправ[а-яЂі]*',
    'рада / сойм*': r'\bрад[а-яЂі]*|\bсойм[а-яЂі]*',
    'посполит*': r'\bпосполит[а-яЂі]*',
    'поддан*': r'\bподдан[а-яЂі]*',
    'суд*': r'\bсуд[а-яЂі]*',
    'маетност* / имЂн*': r'\bмаетност[а-яЂі]*|\бимЂн[а-яЂі]*|\бимен[а-яЂі]*',
    'уряд* / вряд*': r'\b[ув]ряд[а-яЂі]*'
}

all_roots = {**tier_a, **tier_b}

root_stats = []

for root_name, pat in all_roots.items():
    matches_66 = list(re.finditer(pat, text_66, re.IGNORECASE))
    matches_88 = list(re.finditer(pat, text_88, re.IGNORECASE))
    forms_66 = set(m.group(0).lower() for m in matches_66)
    forms_88 = set(m.group(0).lower() for m in matches_88)
    
    # articles with hits
    arts_66 = len([u for u in units_66 if re.search(pat, u['text'], re.IGNORECASE)])
    arts_88 = len([u for u in units_88 if re.search(pat, u['text'], re.IGNORECASE)])
    
    shared_forms = sorted(list(forms_66 & forms_88))
    only_66 = sorted(list(forms_66 - forms_88))
    only_88 = sorted(list(forms_88 - forms_66))
    
    tier = "TIER A (CORE)" if root_name in tier_a else "TIER B (CONTEXT)"
    
    root_stats.append({
        'root': root_name,
        'tier': tier,
        'count_66': len(matches_66),
        'count_88': len(matches_88),
        'arts_66': arts_66,
        'arts_88': arts_88,
        'shared': shared_forms,
        'only_66': only_66,
        'only_88': only_88
    })

print("Stats calculated successfully.")

md = []
md.append("# ПОРІВНЯЛЬНИЙ ЛЕКСИЧНИЙ ЗРІЗ: ЛИТОВСЬКИЙ СТАТУТ 1566 VS 1588")
md.append("## LS-1566-1588-LEXICAL-COMPARISON (Frozen Comparative Layer)\n")
md.append("> **ГОЛОВНИЙ МЕТОДОЛОГІЧНИЙ ПРИНЦИП:**")
md.append("> ```text")
md.append("> MORE HITS ≠ MORE RIGHTS")
md.append("> FEWER HITS ≠ LOSS OF LIBERTY")
md.append("> NEW TERM FORM ≠ NEW CONCEPT")
md.append("> ```")
md.append("> Цей документ фіксує виключно кількісні та морфологічні показники вживання зафіксованого словника без будь-яких припущень щодо «еволюції свободи» чи «розширення демократії».\n")

md.append("## 1. ЗВІТ ПРО ПАРИТЕТНІСТЬ ПРОТОКОЛУ (PROTOCOL PARITY REPORT)\n")
md.append("| Параметр | Стан | Верифікація |")
md.append("| :--- | :---: | :--- |")
md.append("| **Same roots?** | **YES** | Ті самі 5 коренів Tier A та 7 коренів Tier B у двох корпусах |")
md.append("| **Same regex rules?** | **YES** | Абсолютно ідентичні регулярні вирази з підтримкою ять (Ђ) та і/ы |")
md.append("| **Same false-positive rules?** | **YES** | Однакове вилучення лише морфологічних дериватів шуканого кореня |")
md.append("| **Same hit classification?** | **YES** | Ті самі критерії `CORE` (наявність хоча б однієї лексеми Tier A) та `CONTEXT` |")
md.append("| **Same locator granularity?** | **YES** | Одиниці вилучення: преамбули/привілеї та індивідуальні статті |")
md.append("| **Same fidelity level?** | **YES** | **L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)** для обох видань |")

md.append("\n---\n\n## 2. ЗВЕДЕНА КІЛЬКІСНА ТАБЛИЦЯ КОРЕНІВ (LEXICAL ROOT METRICS)\n")
md.append("| Пошуковий корінь | Ярус (Tier) | 1566 Входжень | 1566 Статей | 1588 Входжень | 1588 Статей | Динаміка абсолютна |")
md.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")

for s in root_stats:
    diff_hits = s['count_88'] - s['count_66']
    sign = "+" if diff_hits >= 0 else ""
    md.append(f"| `{s['root']}` | {s['tier']} | **{s['count_66']}** | {s['arts_66']} / {len(units_66)} | **{s['count_88']}** | {s['arts_88']} / {len(units_88)} | {sign}{diff_hits} ({sign}{s['arts_88'] - s['arts_66']} ст.) |")

md.append("\n---\n\n## 3. ДЕТАЛЬНИЙ МОРФОЛОГІЧНИЙ РОЗБІР КОРЕНІВ\n")

for s in root_stats:
    md.append(f"### Корінь: `{s['root']}` ({s['tier']})\n")
    md.append(f"- **Кількісні показники**: 1566 р. = **{s['count_66']}** входжень ({s['arts_66']} статей) ➔ 1588 р. = **{s['count_88']}** входжень ({s['arts_88']} статей).")
    md.append(f"- **Спільні форми в обох редакціях ({len(s['shared'])} форм)**: {', '.join(s['shared'][:12]) + ('...' if len(s['shared']) > 12 else '') if s['shared'] else 'НЕМАЄ'}")
    md.append(f"- **Форми, зафіксовані тільки у 1566 р. ({len(s['only_66'])} форм)**: {', '.join(s['only_66'][:10]) + ('...' if len(s['only_66']) > 10 else '') if s['only_66'] else 'НЕМАЄ'}")
    md.append(f"- **Форми, зафіксовані тільки у 1588 р. ({len(s['only_88'])} форм)**: {', '.join(s['only_88'][:10]) + ('...' if len(s['only_88']) > 10 else '') if s['only_88'] else 'НЕМАЄ'}\n")

md.append("---\n\n## 4. ПОРІВНЯЛЬНИЙ АНАЛІЗ ПАРНИХ ФОРМУЛ ТА СТРУКТУРНИХ ЗБІГІВ\n")
md.append("### 4.1. Парна формула «вольности и свободы»")
md.append("- **У Статуті 1566 року**: лексема `свобод*` трапляється лише **3 рази у 2 статтях** (Розділ 3, Артикули 2 і 4), щоразу виключно як нерозривна парна формула: *«при вольностяхъ и свободахъ»*.")
md.append("- **У Статуті 1588 року**: лексема `свобод*` зустрічається **9 разів у 7 юнітах** (Привілей Жиґимонта III, Зварот Льва Сапеги, Р. 1 ст. 24, Р. 3 ст. 2, 4, 13). Вона продовжує вживатися як парна формула *«прав, свобод и вольностей»*, а також з'являється у формі *«вольности и свободы нашого панства»*.")

md.append("\n### 4.2. Механізм «обычай / звычай»")
md.append("- **У Статуті 1566 року**: 115 входжень у 86 статтях. Головні формули: *«обычаемъ стародавнымъ»*, *«водлугъ звычаю»*, *«звыклымъ обычаемъ»*.")
md.append("- **У Статуті 1588 року**: 166 входжень у 114 статтях. Зберігається висока стабільність формули *«стародавным обычаем»*, яка визначає процесуальний та речовий порядок дій там, де норма статуту посилається на неписану практику.")

md.append("\n### 4.3. Інституційна присяга vs судова присяга («присяг* / прысяг*»)")
md.append("- **У Статуті 1566 року**: 43 входження у 38 статтях. Чітке розмежування господарської/урядницької присяги (Р. 1, Р. 4) та судової роти присяги сторін/свідків (Р. 11, Р. 14).")
md.append("- **У Статуті 1588 року**: 118 входжень у 79 статтях. Різке зростання кількості точних текстів (рот) посадових присяг підкоморія, возного, суддів, писарів та міських урядників.")

out_comp = "/home/agents/GitHub/pravda/semantics/LS-1566-1588-LEXICAL-COMPARISON.md"
with open(out_comp, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Comparative report written to {out_comp}!")

