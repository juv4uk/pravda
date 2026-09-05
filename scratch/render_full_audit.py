import json

with open('scratch/audit_instances_payload.json', 'r', encoding='utf-8') as f:
    payload = json.load(f)

voln = payload['VOLN']
svob = payload['SVOB']
v_aud = payload['voln_audited']
s_aud = payload['svob_audited']

from scratch.build_audit_document import C_DEFS

# Compile full markdown document
out = []
out.append("# АУДИТ ЦІЛІСНОСТІ ТА МАТРИЦЯ СИНТАКСИЧНИХ КОНСТРУКЦІЙ")
out.append("## CONSTRUCTION-INTEGRITY-AUDIT.md (Rigorous Boundary, Multi-Membership & Multi-Dimensional Matrix)")
out.append("")
out.append("> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ЕПІСТЕМОЛОГІЧНІ ІНВАРІАНТИ:**")
out.append("> 1. **FORMAL PATTERNS OVER INTERPRETIVE LABELS**:")
out.append(">    Кожна конструкція ідентифікується за суворим синтаксичним шаблоном (предикат, прийменник, відмінок, зв'язка). Назви конструкцій є суто дескриптивними формулами форми, а не змістовними визначеннями.")
out.append("> 2. **SEPARATION OF METRICS: TOKEN-COUNT vs INSTANCE-COUNT**:")
out.append(">    - `TOKEN-COUNT`: кількість окремих лексемних входжень (словоформ), охоплених конструкцією.")
out.append(">    - `INSTANCE-COUNT`: кількість унікальних текстових втілень конструкції (речень, синтагм, текстових рядків свідка).")
out.append("> 3. **MANY-TO-MANY RELATIONSHIP (MULTI-MEMBERSHIP)**:")
out.append(">    Один лексемний токен може одночасно належати до 0..N конструкцій (наприклад, водночас до координаційного ряду [права + вольності] та предикативного керування [порушити + вольності]). Конструкції не є взаємовиключними кошиками.")
out.append("> 4. **PROVISIONAL STATUS OF CAUSALITY (CORRELATION ≠ CAUSATION)**:")
out.append(">    Збіг певної конструкції з певним жанром чи епохою фіксується як емпірична кореляція. Будь-які твердження про жанрову зумовленість маркуються строго як `GENRE-HYPOTHESIS` (PROVISIONAL).")
out.append("")
out.append("---")
out.append("")
out.append("## 1. РЕЄСТР АУДИТОВАНИХ КОНСТРУКЦІЙ (AUDITED CONSTRUCTIONS 01–13)")
out.append("")

# Collect tokens per frame
tokens_by_frame = {}
instances_by_frame = {}

for cid in C_DEFS.keys():
    tokens_by_frame[cid] = []
    instances_by_frame[cid] = set()

for t in voln:
    for cid in v_aud.get(t['id'], []):
        if cid in tokens_by_frame:
            tokens_by_frame[cid].append(t)
            instances_by_frame[cid].add((t['src'], t['loc']))

for t in svob:
    for cid in s_aud.get(t['id'], []):
        if cid in tokens_by_frame:
            tokens_by_frame[cid].append(t)
            instances_by_frame[cid].add((t['src'], t['loc']))

for cid, cdef in sorted(C_DEFS.items()):
    toks = tokens_by_frame[cid]
    insts = instances_by_frame[cid]
    
    out.append(f"### {cid} — `{cdef['formal_pattern']}`")
    out.append(f"- **КЛЮЧОВИЙ ТЕРМІН:** `{cdef['term']}`")
    out.append(f"- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `{cdef['formal_pattern']}`")
    out.append(f"- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** {cdef['inclusion_rule']}")
    out.append(f"- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** {cdef['exclusion_rule']}")
    out.append(f"- **МЕТРИКА ВХОДЖЕНЬ:**")
    out.append(f"  - **`TOKEN-COUNT`:** **{len(toks)}** (кількість токенів, що беруть участь у конструкції)")
    out.append(f"  - **`INSTANCE-COUNT`:** **{len(insts)}** (кількість незалежних текстових речень/синтагм)")
    out.append(f"- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** {cdef['gloss_candidate']} `[PROVISIONAL]`")
    out.append(f"- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** {cdef['function_hypothesis']} `[PROVISIONAL]`")
    out.append(f"- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER):**")
    
    if len(toks) == 0:
        out.append("  - *Не зафіксовано підтверджених токенів у поточному корпусі під цими правилами.*")
    else:
        for t in toks:
            out.append(f"  - `[{t['id']}]` **`{t['src']}`** ({t['loc']}) | форма: `{t['form']}` | цитата: *«{t['ctx'][:100]}»*")
            
    out.append("")
    out.append("---")
    out.append("")

out.append("## 2. МАТРИЦЯ МУЛЬТИ-ПРИНАЛЕЖНОСТІ (MULTI-MEMBERSHIP ANALYSIS)")
out.append("")
out.append("Оскільки синтаксичні конструкції накладаються одна на одну, нижче зафіксовано всі випадки, де один токен бере участь одразу в кількох структурних рамках:")
out.append("")
out.append("| ТОКЕН-ID | СВІДОК ТА РЯДОК | СЛОВОФОРМА | КОНСТРУКЦІЇ, ЩО ПЕРЕТИНАЮТЬСЯ | ЦИТАТА ТА СИНТАКСИЧНИЙ АНАЛІЗ ПЕРЕТИНУ |")
out.append("|:---|:---|:---:|:---|:---|")

multi_v = [(t, v_aud[t['id']]) for t in voln if len(v_aud.get(t['id'], [])) > 1]
for t, fs in multi_v:
    out.append(f"| `{t['id']}` | **`{t['src']}`** ({t['loc']}) | `{t['form']}` | `{', '.join(fs)}` | *«{t['ctx'][:90]}»* (Токен є одночасно елементом координаційного ряду та прямим додатком дієслова). |")

multi_s = [(t, s_aud[t['id']]) for t in svob if len(s_aud.get(t['id'], [])) > 1]
for t, fs in multi_s:
    out.append(f"| `{t['id']}` | **`{t['src']}`** ({t['loc']}) | `{t['form']}` | `{', '.join(fs)}` | *«{t['ctx'][:90]}»* (Токен поєднує атрибутивну кваліфікацію особи з предикативним судовим правилом). |")

out.append("")
out.append("---")
out.append("")
out.append("## 3. БАГАТОВИМІРНА МАТРИЦЯ РОЗПОДІЛУ (MULTI-DIMENSIONAL MATRIX)")
out.append("")
out.append("Зіставлення 5 вимірів: **ТЕРМІН × КОНСТРУКЦІЯ × ЧАС × МОВА × ЖАНР × ІНСТИТУЦІЯ**:")
out.append("")
out.append("| CONSTRUCTION-ID | ТЕРМІН | СВІДКИ (ЧАС) | МОВА (`LANGUAGE-OF-PASSAGE`) | ДЖЕРЕЛЬНИЙ ЖАНР (`GENRE`) | ЮРИСДИКЦІЯ / ІНСТИТУЦІЯ | `TOKEN-COUNT` | `INSTANCE-COUNT` |")
out.append("|:---|:---:|:---:|:---|:---|:---|:---:|:---:|")

GENRE_MAP = {
    'SRC-RP-SHORT': ('XI–XII ст.', 'Давньоруська', 'Судовий збірник звичаєвого права', 'Князівський / общинний суд верві'),
    'SRC-RP-EXP': ('XII–XV ст.', 'Давньоруська', 'Процесуальний судовий кодекс', 'Князівсько-боярський суд'),
    'SRC-LS-1566': ('1566 р.', 'Руська канцелярська', 'Кодифікований земський статут', 'Сойм ВКЛ / земські суди'),
    'SRC-LS-1588': ('1588 р.', 'Руська канцелярська', 'Загальнодержавна кодифікація', 'Вальний Сойм / Трибунал ВКЛ'),
    'SRC-HADIACH-1658': ('1658 р.', 'Ранньомодерна польська', 'Міжнародно-правовий пакт унії', 'Спільна Комісія Корони і В.К.Р.'),
    'SRC-HADIACH-1659': ('1659 р.', 'Ранньомодерна польська', 'Сеймова ратифікаційна конституція', 'Сейм Речі Посполитої (Volumina Legum)'),
    'SRC-MARCH-1654': ('1654 р.', 'Московсько-руська двомовна', 'Двосторонні договірні статті', 'Посольський приказ / Військо Запорозьке'),
    'SRC-ORLYK-1710': ('1710 р.', 'Староукраїнська книжна', 'Конституційний договір-пакт', 'Генеральна Рада / Гетьманський уряд')
}

for cid, cdef in sorted(C_DEFS.items()):
    toks = tokens_by_frame[cid]
    insts = instances_by_frame[cid]
    w_set = sorted(list(set(t['src'] for t in toks)))
    
    if not w_set:
        out.append(f"| `{cid}` | `{cdef['term']}` | *Немає даних* | *Немає* | *Немає* | *Немає* | **0** | **0** |")
    else:
        dates = ", ".join(sorted(list(set(GENRE_MAP[w][0] for w in w_set))))
        langs = ", ".join(sorted(list(set(GENRE_MAP[w][1] for w in w_set))))
        genres = ", ".join(sorted(list(set(GENRE_MAP[w][2] for w in w_set))))
        instits = ", ".join(sorted(list(set(GENRE_MAP[w][3] for w in w_set))))
        w_str = ", ".join(w_set)
        out.append(f"| `{cid}` | `{cdef['term']}` | {w_str} ({dates}) | {langs} | {genres} | {instits} | **{len(toks)}** | **{len(insts)}** |")

out.append("")
out.append("---")
out.append("")
out.append("## 4. ДИСЦИПЛІНА ВИСНОВКІВ: КОРЕЛЯЦІЇ ПРОТИ ПРИЧИННОСТІ")
out.append("")
out.append("```text")
out.append("CORRELATION ≠ CAUSALITY PROTOCOL")
out.append("")
out.append("1. GENRE-HYPOTHESIS-001 (PROVISIONAL):")
out.append("   The observed absence of VOLN- constructions in the Old Rus witnesses (RP-SHORT, RP-EXP)")
out.append("   correlates with the judicial-torts genre of those documents. Whether this reflects an authentic")
out.append("   absence in the spoken/legal language of the 11th-12th centuries or is an artifact of the surviving")
out.append("   codification genres cannot be resolved without contemporaneous contractual witnesses.")
out.append("")
out.append("2. LANGUAGE-HYPOTHESIS-001 (PROVISIONAL):")
out.append("   The syntactic behavior of 'wolność' and 'swoboda' in Hadiach (1658-1659) strictly belongs to the")
out.append("   Early Modern Polish parliamentary and treaty tradition. Formal cognacy with Chancery Ruthenian")
out.append("   'вольность' does not imply identical semantic evolution.")
out.append("")
out.append("3. MULTI-MEMBERSHIP FINDING:")
out.append("   A substantial portion of VOLN- instances (e.g., Orlyk 1710) participate simultaneously in coordination")
out.append("   (права та вольності) and predicate breach (вольності поламати). Counts of constructions must never")
out.append("   be summed linearly into a token total.")
out.append("```")

with open('semantics/CONSTRUCTION-INTEGRITY-AUDIT.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Rendered semantics/CONSTRUCTION-INTEGRITY-AUDIT.md successfully.")
