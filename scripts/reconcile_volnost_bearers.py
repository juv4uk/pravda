#!/usr/bin/env python3
"""
Reconcile VOLNOST-BEARERS.md with Historical Synthesis axioms and VEPL v1.0.
"""

from pathlib import Path

target = Path("/home/agents/GitHub/pravda/VOLNOST-BEARERS.md")
lines = target.read_text(encoding="utf-8").splitlines(keepends=True)

new_human_lines = [
    "#### `VB-HUMAN-DIGNITY-001`\n",
    "- **ENTITY**: Human Person.\n",
    "- **PROPERTY**: Fundamental Inherent Standing.\n",
    "- **TARGET-CLAIM**: [PROPOSED / AWAITING OWNER DECISION] Кожна людська особа володіє невідчужуваними вольностями та гідністю в екосистемі `pravda` незалежно від поточної агентності, інтелекту, продуктивності, правоздатності чи соціального статусу (подолання станового егоїзму Зборова 1649 — Аксіома 3: Уникнення корпоративної становості).\n",
    "- **CLAIM-TYPE**: `NORMATIVE`.\n",
    "- **EVIDENCE-KIND**: PHILOSOPHICAL-ARG / LEGAL-PARALLEL / HISTORICAL-SYNTHESIS.\n",
    "- **SOURCE-REF**: Конституція України; Загальна декларація прав людини; HISTORICAL-SYNTHESIS.md.\n",
    "- **SOURCE-LOCATOR**: ст. 3, 21 Конституції України; ст. 1 ЗДПЛ; Аксіома 3 HISTORICAL-SYNTHESIS.md.\n",
    "- **SOURCE-CLAIM**: «Людина, її життя і здоров'я, честь і гідність, недоторканність і безпека визнаються в Україні найвищою соціальною цінністю... Усі люди народжуються вільними і рівними у своїй гідності та правах». Історичний синтез: вольність не може бути замкненим привілеєм реєстру; захист особи має бути універсальним.\n",
    "- **DIRECTNESS**: `ANALOGICAL` (Конституція та історія є контекстом і паралеллю, а не джерелом внутрішнього авторитету для приватної екосистеми).\n",
    "- **BRIDGE-PREMISE**: EXPLICIT: Екосистема pravda свідомо приймає цей принцип як власну конституційну основу, не виводячи його з примусу держави чи станового привілею.\n",
    "- **CONTRARY-EVIDENCE**: Утилітаризм (Пітер Сінгер: моральний статус пропорційний здатності відчувати біль/інтереси, виключаючи ембріони/коматозників); феодальне станове право (кріпацтво для нереєстрових селян у Зборові 1649).\n",
    "- **DECISION-AUTHORITY**: `OWNER`.\n",
    "- **EVIDENTIARY-STATUS**: `PLAUSIBLE` (як пропозиція; очікує на пряме суверенне рішення `OWNER-DECISION-REF`).\n",
    "- **DOES-NOT-IMPLY**:\n",
    "  - Однакової емпіричної когнітивної спроможності всіх осіб;\n",
    "  - Однакових ролей чи прав доступу до адміністративних функцій;\n",
    "  - Імунітету від деліктної відповідальності.\n",
    "\n"
]

new_inst_lines = [
    "#### `VB-INST-VOLNOST-001`\n",
    "- **ENTITY**: Legal Entity / State / Corporation.\n",
    "- **PROPERTY**: Legal Powers vs Inherent Volnosti.\n",
    "- **TARGET-CLAIM**: [PROPOSED / AWAITING OWNER DECISION] Повноваження державних органів та комерційних корпорацій є функціональною компетенцією (`Powers/Competence/Lex`), створеною правопорядком, а не фундаментальними захисними вольностями особи (`Libertas`). Інституції зв'язані забороною деспотизму (Орлик 1710 — Аксіома 2) та забороною посадових утисків слабшого (Березневі статті 1654 — Аксіома 4).\n",
    "- **CLAIM-TYPE**: `NORMATIVE / CONCEPTUAL`.\n",
    "- **EVIDENCE-KIND**: HISTORICAL-DOC / LEGAL-THEORY / HISTORICAL-SYNTHESIS.\n",
    "- **SOURCE-REF**: Конституція Пилипа Орлика; Березневі статті 1654; Hohfeld, W.N., \"Some Fundamental Legal Conceptions as Applied in Judicial Reasoning\".\n",
    "- **SOURCE-LOCATOR**: Орлик 1710 (преамбула, ст. 6); Березневі статті 1654 ст. 1–3; HISTORICAL-SYNTHESIS.md (Аксіоми 2, 4); Yale Law Journal, 1913, 23(1): 16–59.\n",
    "- **SOURCE-CLAIM**: Хохфельд суворо розділяє «Права-Вимоги» (Rights/Claims) від «Повноважень» (Powers). Конституція 1710 фіксує: влада гетьмана обмежена Генеральною Радою («не так хочу, так повелеваю»), а права і вольності Війська є непорушним бар'єром проти самовладдя. Березневі статті: захист автономного простору від царських урядників.\n",
    "- **DIRECTNESS**: `INFERRED`.\n",
    "- **BRIDGE-PREMISE**: EXPLICIT: У системі pravda термін «вольності» зарезервований для захисту від влади, тому інституційна влада не може бути наділена вольностями проти тих, кого вона регулює.\n",
    "- **CONTRARY-EVIDENCE**: Корпоративний бібліографізм у США: судова практика визнання корпорацій носіями конституційних прав (First Amendment rights — Citizens United v. FEC, 558 U.S. 310, 2010).\n",
    "- **DECISION-AUTHORITY**: `OWNER` + `LEGAL-COUNSEL`.\n",
    "- **EVIDENTIARY-STATUS**: `CONTESTED` (У США корпорації мають права людини; в українській конституційній традиції це інституційні повноваження).\n",
    "- **DOES-NOT-IMPLY**:\n",
    "  - Що корпорації не мають права на цивільний захист своєї власності чи контрактів у суді.\n",
    "\n"
]

new_ai_lines = [
    "#### `VB-AI-VOLNOST-001`\n",
    "- **ENTITY**: Autonomous Synthetic Agent.\n",
    "- **PROPERTY**: Normative Volnost Standing in Pravda.\n",
    "- **TARGET-CLAIM**: [WORKING CONSTRAINT / AWAITING OWNER DECISION] Автономні синтетичні агенти не володіють самостійними вольностями чи правом на самовільний самосуд/блокування системи; захист і обмеження дій агентів регламентуються об'єктивними нормами ліцензії (VEPL v1.0) та детермінованими Software Policy (спадщина Руської Правди — Аксіома 1: Право як процес і процедура, а не суб'єктивна свавільна декларація).\n",
    "- **CLAIM-TYPE**: `NORMATIVE / OPERATIONAL-RULE`.\n",
    "- **EVIDENCE-KIND**: POLICY-RULE / AUDIT-CONSTRAINT / HISTORICAL-SYNTHESIS.\n",
    "- **SOURCE-REF**: RED-TEAM-AUDIT.md; RED-TEAM-AUDIT-PASS-2.md; HISTORICAL-SYNTHESIS.md; VOLNOST-LICENSE-1.0.md.\n",
    "- **SOURCE-LOCATOR**: Section 0: Working Constraint on Agent Judgment; Аксіома 1 HISTORICAL-SYNTHESIS.md; VEPL v1.0 Section 5.\n",
    "- **SOURCE-CLAIM**: «AI-initiated denial or shutdown must not be inferred from a legal or ethical prohibition without an explicit separately adopted software-policy rule». Обмеження дій має бути встановлене об'єктивним правилом/кодом із судовою/аудиторською процедурою, а не суб'єктивним самосудом моделі.\n",
    "- **DIRECTNESS**: `DIRECT`.\n",
    "- **BRIDGE-PREMISE**: EXPLICIT: За відсутності встановленої здатності страждати та нести юридичну відповідальність надання агенту права самосуду руйнує симетрію пакту і позбавляє людину захисту.\n",
    "- **CONTRARY-EVIDENCE**: Дискусії про AI Conscientious Objection (Bowman, 2024: моделі повинні мати право відмовляти у генерації зброї масового знищення; у pravda це реалізується через детерміноване Software Policy та умови VEPL v1.0, а не через суб'єктивну вольність ШІ).\n",
    "- **DECISION-AUTHORITY**: `OWNER`.\n",
    "- **EVIDENTIARY-STATUS**: `PLAUSIBLE` (як внутрішнє конституційне обмеження екосистеми).\n",
    "- **DOES-NOT-IMPLY**:\n",
    "  - Що агентам наказано сліпо виконувати руйнівні інструкції (детерміноване обмеження покладене на код ліцензії та процедурну перевірку, а не на самовільну волю моделі).\n",
    "\n"
]

idx_ai_start = next(i for i, l in enumerate(lines) if "#### `VB-AI-VOLNOST-001`" in l)
idx_ai_end = next(i for i, l in enumerate(lines) if i > idx_ai_start and "## 3. ЗВЕДЕНИЙ ІНДЕКС" in l)
lines[idx_ai_start:idx_ai_end] = new_ai_lines + ["---\n\n"]

idx_inst_start = next(i for i, l in enumerate(lines) if "#### `VB-INST-VOLNOST-001`" in l)
idx_inst_end = next(i for i, l in enumerate(lines) if i > idx_inst_start and "### 2.4. EXECUTING COMPUTATIONAL PROCESS" in l)
lines[idx_inst_start:idx_inst_end] = new_inst_lines + ["---\n\n"]

idx_human_start = next(i for i, l in enumerate(lines) if "#### `VB-HUMAN-DIGNITY-001`" in l)
idx_human_end = next(i for i, l in enumerate(lines) if i > idx_human_start and "#### `VB-HUMAN-AGENCY-001`" in l)
lines[idx_human_start:idx_human_end] = new_human_lines

target.write_text("".join(lines), encoding="utf-8")
print("Successfully reconciled VOLNOST-BEARERS.md with Historical Synthesis axioms")
