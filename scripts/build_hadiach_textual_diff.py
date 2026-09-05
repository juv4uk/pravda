import re

with open('/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Function to parse claim blocks
def parse_claims(txt, prefix):
    pattern = rf"(### ({prefix}-[A-Z0-9\-]+)\n.*?)(?=\n### |\n## |\n---\n\n## |\Z)"
    matches = re.finditer(pattern, txt, re.DOTALL)
    claims = {}
    for m in matches:
        cid = m.group(2)
        block = m.group(1)
        # extract quote
        q_match = re.search(r"- \*\*EXACT-QUOTE:\*\*\n\s+> «(.*?)»", block, re.DOTALL)
        quote = q_match.group(1).strip() if q_match else ""
        # extract terms
        t_match = re.search(r"- \*\*LEXICAL-TERMS:\*\* `(.*?)`", block)
        terms = t_match.group(1).strip() if t_match else ""
        # extract actor
        a_match = re.search(r"- \*\*GRAMMATICAL-ACTOR:\*\* (.*?)\n", block)
        actor = a_match.group(1).strip() if a_match else ""
        # extract object
        o_match = re.search(r"- \*\*TEXTUAL-OBJECT:\*\* (.*?)\n", block)
        t_obj = o_match.group(1).strip() if o_match else ""
        claims[cid] = {
            "id": cid,
            "quote": quote,
            "terms": terms,
            "actor": actor,
            "object": t_obj
        }
    return claims

claims_1658 = parse_claims(text, "HC-HAD1658")
claims_1659 = parse_claims(text, "HC-SEJM1659")

print(f"Parsed 1658 claims: {len(claims_1658)}")
print(f"Parsed 1659 claims: {len(claims_1659)}")

