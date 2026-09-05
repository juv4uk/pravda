# -*- coding: utf-8 -*-
import re
import sys
import check_forbidden_terms
import check_paraphrase_drift

reg_file = '/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md'
with open(reg_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "## 7. Еталонний повний блок: Руська Правда (Простора редакція)"
end_marker = "## 8. Пілотні атоми Литовських Статутів"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

rp_exp_section = content[start_idx:end_idx]

claims = re.findall(r'(### HC-RP-EXP-\d{3}[A-Z].*?)(?=(?:### HC-RP-EXP|\Z))', rp_exp_section, re.DOTALL)
print(f"Total RP-EXP claims in register: {len(claims)}")
assert len(claims) == 160, f"Expected 160 claims, got {len(claims)}"

# Check for leaks
forbidden_leaks = []
paraphrase_leaks = []

for idx, c in enumerate(claims, 1):
    actor = re.search(r'- \*\*GRAMMATICAL-ACTOR:\*\* (.*)', c).group(1)
    op = re.search(r'- \*\*TEXTUAL-OPERATOR:\*\* (.*)', c).group(1)
    obj = re.search(r'- \*\*TEXTUAL-OBJECT:\*\* (.*)', c).group(1)
    cond = re.search(r'- \*\*TEXTUAL-CONDITION:\*\* (.*)', c).group(1)
    cons = re.search(r'- \*\*TEXTUAL-CONSEQUENCE:\*\* (.*)', c).group(1)
    terms = re.search(r'- \*\*LEXICAL-TERMS:\*\* `(.*?)`', c).group(1)
    
    text_to_check = f"{actor} {obj} {cond} {cons} {terms}"
    
    fb = check_forbidden_terms.check_text(text_to_check)
    if fb:
        forbidden_leaks.append((f"Claim {idx}", fb, text_to_check))
    
    pr = check_paraphrase_drift.scan_text(text_to_check)
    if pr:
        paraphrase_leaks.append((f"Claim {idx}", pr, text_to_check))

print(f"Forbidden leaks: {len(forbidden_leaks)}")
print(f"Paraphrase drift leaks: {len(paraphrase_leaks)}")

assert len(forbidden_leaks) == 0, f"Forbidden leaks found: {forbidden_leaks}"
assert len(paraphrase_leaks) == 0, f"Paraphrase drift leaks found: {paraphrase_leaks}"

print("PASS: 100% PURIFIED SOURCE-NEAR COMPLIANCE VERIFIED ACROSS REGISTER!")
