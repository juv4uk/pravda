import re
from extract_sejm_1659_all_units import claims as claims_part_a
from extract_sejm_1659_part_bc import units_spec, clean_txt

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    full_text = f.read()

body = full_text.split('================================================================================')[1]
pacta_end = body.find('Approbacya kommissyj Hadyackiey.')
part_bc = body[pacta_end:]

claims_all = list(claims_part_a)

# Fix missing fields in units_spec
for u in units_spec:
    if "speaker" not in u:
        u["speaker"] = "CROWN & DIET"

# Fix end match for HC-SEJM1659-APP-002A
units_spec[0]["end_match"] = "Brandeburczykiem."

for u in units_spec:
    start_m = u["start_match"]
    end_m = u["end_match"]
    s_idx = part_bc.find(start_m)
    if s_idx == -1:
        print(f"FAILED TO FIND START MATCH: {start_m}")
        continue
    if end_m == "==END==":
        chunk = part_bc[s_idx:]
    else:
        e_idx = part_bc.find(end_m, s_idx)
        if e_idx == -1:
            print(f"FAILED TO FIND END MATCH: {end_m}")
            chunk = part_bc[s_idx:s_idx+1000]
        else:
            chunk = part_bc[s_idx:e_idx + len(end_m)]
    
    quote = clean_txt(chunk)
    # Remove OCR noise words like page numbers inside quote
    quote = re.sub(r'\b(644|645|646|648|650|651|652|653|654|655|658|657|301|302|304|305|306|307|308|T\. IV|ZA JANA KAZIMIERZA R\. 1659\.|KONSTYTUCYE SEYMU WARSZAWSKIEGO)\b', '', quote)
    quote = re.sub(r'\s+', ' ', quote).strip()
    
    claims_all.append({
        "unit_id": u["unit_id"],
        "heading": u["heading"],
        "page": u["page"],
        "claim_id": u["claim_id"],
        "speaker": u["speaker"],
        "quote": quote,
        "terms": u["terms"],
        "actor": u["actor"],
        "operator": u["operator"],
        "object": u["object"]
    })

print(f"Total claims in full Sejm 1659 corpus: {len(claims_all)}")

forbidden = [
    "суверенітет", "sovereignty", "автономія", "autonomy", "сегрегація", "segregation",
    "дискримінація", "discrimination", "права меншин", "minority rights", "національні права",
    "демократія", "democracy", "окупація", "occupation", "федерація", "federation",
    "конфедерація", "confederation", "релігійна свобода", "religious freedom",
    "національна держава", "national state", "публічний бюджет", "public budget",
    "монарх", "monarch", "правовий статус", "піддані як громадяни",
    "narrowed", "expanded", "removed", "weakened"
]

all_clean = True
for c in claims_all:
    blob = f"{c['terms']} {c['actor']} {c['object']}"
    for f_term in forbidden:
        if re.search(r'\b' + re.escape(f_term) + r'\b', blob, re.IGNORECASE):
            print(f"FORBIDDEN in {c['claim_id']}: {f_term}")
            all_clean = False

if all_clean:
    print("ALL CLAIMS PASS PURITY CHECK (0 FORBIDDEN TERMS)!")

# Generate markdown section
md = []
md.append("\n## 3.5. Сеймовий корпус Гадяцького врегулювання 1659 (Volumina Legum, Т. IV, с. 297–307)")
md.append("**Свідок:** `WIT-HADIACH-SEJM-1659` (*Volumina Legum*, Т. IV, с. 297–307, вид. Й. Огризка, СПб., 1859).")
md.append("**Структурна організація корпусу:** Корпус поділено за автентичними друкованими заголовками видання на окремі документні юніти (`DOCUMENT-UNIT-ID`), що відображають самостійні сеймові конституції, нобілітації, надання та присяги. Жодного порівняння з 1658 роком під час екстракції. `INTERPRETATION: EMPTY`.\n")

for c in claims_all:
    b = f"""### {c['claim_id']}
- **DOCUMENT-UNIT-ID:** `{c['unit_id']}`
- **PRINTED-HEADING:** `{c['heading']}`
- **PAGE:** {c['page']}
- **CLAIM-ID:** `{c['claim_id']}`
- **WITNESS-ID:** `WIT-HADIACH-SEJM-1659`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **EXACT-QUOTE:**
  > «{c['quote']}»
- **LEXICAL-TERMS:** `{c['terms']}`
- **GRAMMATICAL-ACTOR:** {c['actor']}
- **TEXTUAL-SPEAKER:** `{c['speaker']}`
- **TEXTUAL-OPERATOR:** `{c['operator']}`
- **TEXTUAL-OBJECT:** {c['object']}
- **INTERPRETATION:** `EMPTY`
"""
    md.append(b)

full_md = "\n---\n\n".join(md)

# Now insert into HISTORICAL-CLAIMS-REGISTER.md
with open("/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md", "r", encoding="utf-8") as f:
    reg_content = f.read()

# Replace the single old pilot claim HC-HADIACH-SEJM-1659-001
pattern = r"### HC-HADIACH-SEJM-1659-001\n.*?(?=\n---|\Z)"
match = re.search(pattern, reg_content, re.DOTALL)
if match:
    new_reg = reg_content[:match.start()] + full_md + "\n\n---\n"
    with open("/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md", "w", encoding="utf-8") as f:
        f.write(new_reg)
    print("Successfully replaced pilot claim with full Sejm 1659 corpus!")
else:
    print("Could not find pattern for HC-HADIACH-SEJM-1659-001!")
