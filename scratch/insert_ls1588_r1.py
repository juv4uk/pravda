with open('HISTORICAL-CLAIMS-REGISTER.md', 'r', encoding='utf-8') as f:
    text = f.read()

with open('scratch/LS1588_R1_GENERATED.md', 'r', encoding='utf-8') as f:
    r1_block = f.read()

target = "## 8. Пілотні атоми Литовських Статутів"
assert target in text, "Target heading not found!"

# Replace from '## 8. Пілотні атоми Литовських Статутів' up to '## 3.4. Гадяцька комісія 1658'
p1 = text.find(target)
p2 = text.find("## 3.4. Гадяцька комісія 1658")
assert p1 != -1 and p2 != -1, "Boundaries not found!"

pilot_ls1566 = """### HC-LS1566-001
- **CLAIM-ID:** `HC-LS1566-001`
- **WITNESS-ID:** `WIT-LS-1566-PRINT-1855`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **LOCATOR:** Розділ 1, Артикул 1 (Видання Лаппо 1900 / 1855, с. 1)
- **EXACT-QUOTE:**
  > «Напервей мы господаръ обѣцуемъ и шлюбуемъ под сумненьемъ и присягою нашою... што всих княжатъ, пановъ радныхъ, якъ духовныхъ такъ и свѣтскихъ, пановъ хоруговныхъ, шляхту, рыцерство, бояръ и вси станы... заховати въ ихъ правахъ, свободахъ и вольностяхъ... а тыхъ правъ ихъ и свободъ ни въ чомъ не нарушати...»
- **LEXICAL-TERMS:** `господаръ, обѣцуемъ и шлюбуемъ, под присягою, правахъ, свободахъ, вольностяхъ, не нарушати`
- **GRAMMATICAL-ACTOR:** господаръ; княжата; паны радные; шляхта; рыцерство
- **TEXTUAL-OPERATOR:** `CONFIRMS / PROHIBITS`
- **TEXTUAL-OBJECT:** Зобов'язання господаря під присягою зберігати княжат, радних панів і рицерство у їхніх правах, свободах і вольностях; заборона їх порушувати.
- **INTERPRETATION:** `EMPTY`

---

### HC-LS1566-002
- **CLAIM-ID:** `HC-LS1566-002`
- **WITNESS-ID:** `WIT-LS-1566-PRINT-1855`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **LOCATOR:** Розділ 3, Артикул 3
- **EXACT-QUOTE:**
  > «Тежъ уставимы и варуемъ: ижъ вси обывателе Великого Князства Литовского... шляхта и люди рыцерские... мають уживати вольностей своихъ хрестьянскихъ... и никому водле уподобанья нашого ничого не привлащати.»
- **LEXICAL-TERMS:** `обывателе, шляхта, вольностей своихъ хрестьянскихъ, не привлащати`
- **GRAMMATICAL-ACTOR:** господаръ; обывателе; шляхта
- **TEXTUAL-OPERATOR:** `CONFIRMS / PROHIBITS`
- **TEXTUAL-OBJECT:** Підтвердження вживання шляхтою християнських вольностей; заборона господарю привласнювати майно за власним уподобанням без суду.
- **INTERPRETATION:** `EMPTY`

---

"""

new_section = r1_block.strip() + "\n\n---\n\n## 9. Пілотні атоми Литовського Статуту 1566 року\n\n" + pilot_ls1566

new_full_text = text[:p1] + new_section + "\n" + text[p2:]

with open('HISTORICAL-CLAIMS-REGISTER.md', 'w', encoding='utf-8') as f:
    f.write(new_full_text)

print("Successfully replaced section with full LS 1588 Rozdil 1 (35 claims) and preserved LS 1566 pilots!")
