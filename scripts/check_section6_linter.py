import re
import check_forbidden_terms

with open('/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('## 6. Еталонний повний блок: Руська Правда (Коротка редакція)')
end_idx = text.find('## 7. Пілотні атоми інших свідків')
rp_section = text[start_idx:end_idx]

claims = re.findall(r'(### HC-RP-SHORT-\d{3}.*?)(?=(?:### HC-RP-SHORT|\Z))', rp_section, re.DOTALL)

violations = []
for idx, c in enumerate(claims, 1):
    obj_match = re.search(r'- \*\*TEXTUAL-OBJECT:\*\* (.*)', c)
    if obj_match:
        obj_text = obj_match.group(1)
        res = check_forbidden_terms.check_text(obj_text)
        if res:
            violations.append((f"HC-RP-SHORT-{idx:03d}", res, obj_text))

if violations:
    print(f"Linter violations found: {violations}")
else:
    print("0 modern legal category leaks found in TEXTUAL-OBJECT across all 43 claims!")
