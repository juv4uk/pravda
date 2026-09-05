import json

with open('scratch/audit_instances_payload.json', 'r', encoding='utf-8') as f:
    payload = json.load(f)

with open('scratch/patched_audit_results.json', 'r', encoding='utf-8') as f:
    patched = json.load(f)

voln = payload['VOLN']
svob = payload['SVOB']
cid_tokens = patched['cid_tokens']
cid_instances = patched['cid_instances']
cid_sentences = patched['cid_sentences']

from scratch.build_audit_document import C_DEFS

out = []
out.append("# АУДИТ ЦІЛІСНОСТІ ТА МАТРИЦЯ СИНТАКСИЧНИХ КОНСТРУКЦІЙ (ВЕРСІЯ 2 — CALIBRATED)")
out.append("## CONSTRUCTION-INTEGRITY-AUDIT.md (Rigorous Boundaries, Explicit Rules, Three-Tier Metrics)")
out.append("")
out.append("> **МЕТОДОЛОГІЧНИЙ СТАТУС ТА ЕПІСТЕМОЛОГІЧНІ ІНВАРІАНТИ:**")
out.append("> 1. **FORMAL PATTERNS OVER INTERPRETIVE LABELS**:")
out.append(">    Кожна конструкція ідентифікується за суворим синтаксичним шаблоном (предикат, прийменник, відмінок, зв'язка). Назви конструкцій є суто дескриптивними формулами форми, а не змістовними визначеннями.")
out.append("> 2. **THREE-TIER SEPARATED METRICS**:")
out.append(">    - `TOKEN-COUNT`: кількість окремих лексемних входжень (словоформ), охоплених конструкцією.")
out.append(">    - `CONSTRUCTION-INSTANCE-COUNT`: кількість окремих підтверджених фактів спрацювання правила конструкції.")
out.append(">    - `SENTENCE-COUNT`: кількість унікальних текстових речень / артикулів / рядків джерела.")
out.append("> 3. **RULE-BASED MANY-TO-MANY MULTI-MEMBERSHIP**:")
out.append(">    Один токен може одночасно належати до кількох рамок ЛИШЕ за наявності окремого документального доказу для кожного правила (`MATCH-RULE-ID` + `MATCH-EVIDENCE`). Жодного включення за «тематичною спорідненістю».")
out.append("> 4. **PROVISIONAL STATUS OF CAUSALITY (CORRELATION ≠ CAUSATION)**:")
out.append(">    Збіг певної конструкції з певним жанром чи епохою фіксується як емпірична кореляція. Будь-які твердження про жанрову зумовленість маркуються строго як `GENRE-HYPOTHESIS` (PROVISIONAL).")
out.append("")
out.append("---")
out.append("")
out.append("## 1. РЕЄСТР АУДИТОВАНИХ КОНСТРУКЦІЙ (AUDITED CONSTRUCTIONS 01–13)")
out.append("")

all_tokens_dict = {t['id']: t for t in voln + svob}

for cid, cdef in sorted(C_DEFS.items()):
    tok_ids = cid_tokens.get(cid, [])
    insts = cid_instances.get(cid, [])
    sents = cid_sentences.get(cid, [])
    
    out.append(f"### {cid} — `{cdef['formal_pattern']}`")
    out.append(f"- **КЛЮЧОВИЙ ТЕРМІН:** `{cdef['term']}`")
    out.append(f"- **СПОСТЕРЕЖУВАНИЙ ШАБЛОН (OBSERVED FRAME):** `{cdef['formal_pattern']}`")
    out.append(f"- **ПРАВИЛО ВКЛЮЧЕННЯ (EXACT INCLUSION RULE):** {cdef['inclusion_rule']}")
    out.append(f"- **ПРАВИЛО ВИКЛЮЧЕННЯ (EXACT EXCLUSION RULE):** {cdef['exclusion_rule']}")
    out.append(f"- **МЕТРИКА ВХОДЖЕНЬ (THREE-TIER METRICS):**")
    out.append(f"  - **`TOKEN-COUNT`:** **{len(tok_ids)}**")
    out.append(f"  - **`CONSTRUCTION-INSTANCE-COUNT`:** **{len(insts)}**")
    out.append(f"  - **`SENTENCE-COUNT`:** **{len(sents)}**")
    out.append(f"- **СЕМАНТИЧНИЙ ГЛОС-КАНДИДАТ (GLOSS CANDIDATE):** {cdef['gloss_candidate']} `[PROVISIONAL]`")
    out.append(f"- **ФУНКЦІОНАЛЬНА ГІПОТЕЗА (FUNCTION HYPOTHESIS):** {cdef['function_hypothesis']} `[PROVISIONAL]`")
    out.append(f"- **ПОВНИЙ ПЕРЕЛІК ЗАСВІДЧЕНИХ ІНСТАНЦІЙ (LOCATOR-LEVEL LEDGER WITH MATCH-EVIDENCE):**")
    
    if len(insts) == 0:
        out.append("  - *Не зафіксовано підтверджених токенів у поточному корпусі під цими правилами.*")
    else:
        for inst in insts:
            tid = inst['token_id']
            t = all_tokens_dict[tid]
            out.append(f"  - `[{tid}]` **`{t['src']}`** ({t['loc']}) | форма: `{t['form']}`")
            out.append(f"    - **MATCH-RULE-ID:** `{inst['rule_id']}`")
            out.append(f"    - **MATCH-EVIDENCE:** {inst['evidence']}")
            
    out.append("")
    out.append("---")
    out.append("")

out.append("## 2. МАТРИЦЯ МУЛЬТИ-ПРИНАЛЕЖНОСТІ (MULTI-MEMBERSHIP ANALYSIS)")
out.append("")
out.append("Оскільки синтаксичні конструкції накладаються одна на одну, нижче зафіксовано всі випадки, де один токен бере участь одразу в кількох структурних рамках, підтверджених незалежними правилами:")
out.append("")
out.append("| ТОКЕН-ID | СВІДОК ТА РЯДОК | СЛОВОФОРМА | ПІДТВЕРДЖЕНІ ПРАВИЛА (MATCH-RULE-IDS) | СИНТАКСИЧНИЙ ДОКАЗ ПЕРЕТИНУ |")
out.append("|:---|:---|:---:|:---|:---|")

# Find tokens present in >1 construction
token_to_cids = {}
for cid, tids in cid_tokens.items():
    for tid in tids:
        token_to_cids.setdefault(tid, []).append(cid)

multi_tokens = {tid: cids for tid, cids in token_to_cids.items() if len(cids) > 1}
for tid, cids in sorted(multi_tokens.items()):
    t = all_tokens_dict[tid]
    rules = []
    for cid in cids:
        for inst in cid_instances[cid]:
            if inst['token_id'] == tid:
                rules.append(f"{cid} ({inst['rule_id']})")
    out.append(f"| `{tid}` | **`{t['src']}`** ({t['loc']}) | `{t['form']}` | `{'; '.join(rules)}` | *«{t['ctx'][:90]}»* |")

out.append("")
out.append("---")
out.append("")
out.append("## 3. БАГАТОВИМІРНА МАТРИЦЯ РОЗПОДІЛУ (MULTI-DIMENSIONAL MATRIX)")
out.append("")
out.append("Зіставлення 5 вимірів: **ТЕРМІН × КОНСТРУКЦІЯ × ЧАС × МОВА × ЖАНР × ІНСТИТУЦІЯ**:")
out.append("")
out.append("| CONSTRUCTION-ID | ТЕРМІН | СВІДКИ (ЧАС) | МОВА (`LANGUAGE-OF-PASSAGE`) | ДЖЕРЕЛЬНИЙ ЖАНР (`GENRE`) | ЮРИСДИКЦІЯ / ІНСТИТУЦІЯ | `TOKEN-COUNT` | `INSTANCE-COUNT` | `SENTENCE-COUNT` |")
out.append("|:---|:---:|:---:|:---|:---|:---|:---:|:---:|:---:|")

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
    tok_ids = cid_tokens.get(cid, [])
    insts = cid_instances.get(cid, [])
    sents = cid_sentences.get(cid, [])
    
    if not tok_ids:
        out.append(f"| `{cid}` | `{cdef['term']}` | *Немає даних* | *Немає* | *Немає* | *Немає* | **0** | **0** | **0** |")
    else:
        w_set = sorted(list(set(all_tokens_dict[tid]['src'] for tid in tok_ids)))
        dates = ", ".join(sorted(list(set(GENRE_MAP[w][0] for w in w_set))))
        langs = ", ".join(sorted(list(set(GENRE_MAP[w][1] for w in w_set))))
        genres = ", ".join(sorted(list(set(GENRE_MAP[w][2] for w in w_set))))
        instits = ", ".join(sorted(list(set(GENRE_MAP[w][3] for w in w_set))))
        w_str = ", ".join(w_set)
        out.append(f"| `{cid}` | `{cdef['term']}` | {w_str} ({dates}) | {langs} | {genres} | {instits} | **{len(tok_ids)}** | **{len(insts)}** | **{len(sents)}** |")

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
out.append("   Multi-membership is restricted strictly to verified formal rule matches (MATCH-RULE-ID).")
out.append("   Lexeme tokens participating simultaneously in coordination (права та вольності) and")
out.append("   predicate breach (вольності поламати) are accounted for separately under TOKEN-COUNT,")
out.append("   INSTANCE-COUNT, and SENTENCE-COUNT.")
out.append("```")

with open('semantics/CONSTRUCTION-INTEGRITY-AUDIT.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Rendered calibrated semantics/CONSTRUCTION-INTEGRITY-AUDIT.md successfully.")
