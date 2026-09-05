import sys

reg_file = '/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md'
with open(reg_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Target block to replace: from line starting with "## 6. Очищені атоми інших свідків"
# up to "## 3.4. Гадяцька комісія 1658"

target_start = "## 6. Очищені атоми інших свідків (Руська Правда, Статути ВКЛ, Гадяч)"
target_end = "## 3.4. Гадяцька комісія 1658 (Повний текст, 47 тверджень у порядку документа)"

if target_start not in content or target_end not in content:
    print("Error: targets not found in content!")
    sys.exit(1)

with open('/home/agents/GitHub/pravda/scratch/rp_short_claims_block.md', 'r', encoding='utf-8') as f:
    rp_block = f.read().strip()

# We also retain the pilot claims for RP-EXP, LS-1566, LS-1588 under a dedicated subsection or keep Section 7 for them
residual_section = """
## 7. Пілотні атоми інших свідків (Руська Правда Простора, Статути ВКЛ)

### HC-RP-EXP-001
- **CLAIM-ID:** `HC-RP-EXP-001`
- **WITNESS-ID:** `WIT-RP-EXP-TROITSKY`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **LOCATOR:** Стаття 58 (Троїцький список, заголовок «О закупе»)
- **EXACT-QUOTE:**
  > «Аже закупъ бежить от господына, то обелныи холопъ; идеть ли искать купы, а явлено ходить, или к князю или к судъямъ бежить обиды деля своего господина, то про то не обелять его, но дати ему правду.»
- **LEXICAL-TERMS:** `закупъ, бежить, обелныи холопъ, к князю, к судъямъ, обиды деля, дати ему правду`
- **GRAMMATICAL-ACTOR:** закупъ; господинъ; князь; суддя
- **TEXTUAL-OPERATOR:** `PROHIBITS / REQUIRES`
- **TEXTUAL-OBJECT:** Заборона обертати закупа на повного (обельного) холопа, якщо він іде шукати грошей відкрито або біжить зі скаргою на образу від свого господаря до князя чи суддів; вимога надати йому суд («дати правду»).
- **INTERPRETATION:** `EMPTY`

---

### HC-LS1566-001
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

### HC-LS1588-001
- **CLAIM-ID:** `HC-LS1588-001`
- **WITNESS-ID:** `WIT-LS-1588-MAMONICZ-PRINCEPS`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **LOCATOR:** Розділ 1, Артикул 2
- **EXACT-QUOTE:**
  > «А ижъ бы кождому зъ обывателей Великого Князства Литовского свободней было справедливой обороны правъ своихъ уживати, жаденъ зъ урядниковъ нашыхъ судовыхъ... не маеть отсужати ани отнимати чести и маетьности безъ права и суду звычайного...»
- **LEXICAL-TERMS:** `обывателей, справедливой обороны правъ, урядниковъ, не маеть отсужати, безъ права и суду звычайного`
- **GRAMMATICAL-ACTOR:** урядники судовые; обывателе
- **TEXTUAL-OPERATOR:** `PROHIBITS / REQUIRES`
- **TEXTUAL-OBJECT:** Заборона судовим урядникам відбирати честь або маєтність без звичайного суду і права; збереження вільної оборони своїх прав.
- **INTERPRETATION:** `EMPTY`

---

### HC-LS1588-002
- **CLAIM-ID:** `HC-LS1588-002`
- **WITNESS-ID:** `WIT-LS-1588-MAMONICZ-PRINCEPS`
- **FIDELITY:** `L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)`
- **LOCATOR:** Розділ 4, Артикул 10
- **EXACT-QUOTE:**
  > «Роки завитые на судехъ мають быти постереганы... а хто бы на рокъ завитый не сталъ, тотъ безъ права отсужонъ быти маеть...»
- **LEXICAL-TERMS:** `роки завитые, на судехъ, постереганы, безъ права отсужонъ`
- **GRAMMATICAL-ACTOR:** судьи; стороны процессу
- **TEXTUAL-OPERATOR:** `REQUIRES`
- **TEXTUAL-OBJECT:** Дотримання визначених процесуальних строків (років завитих); винесення рішення проти сторони за неявку у завитий строк.
- **INTERPRETATION:** `EMPTY`

---
"""

replacement = rp_block + "\n\n" + residual_section.strip() + "\n\n"

# Cut between target_start and target_end
idx1 = content.find(target_start)
idx2 = content.find(target_end)

new_content = content[:idx1] + replacement + "\n\n" + content[idx2:]

with open(reg_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully updated {reg_file}!")
