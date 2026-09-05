import json

with open('scratch/ryad_tokens.json') as f: ryad = json.load(f)
with open('scratch/dogovor_tokens.json') as f: dog = json.load(f)
with open('scratch/pakt_tokens.json') as f: pakt = json.load(f)

print("=== 1. RYAD GRAMMAR & ARGUMENT STRUCTURE ===")
# In RP-EXP:
# - како ся будеть рядилъ (verb рядити ся: домовлятися про умови найму/послуги)
# - безъ ряду (adv phrase: без попереднього договору/умови)
# - с рядомь ли (adv phrase: за наявності договору)
# - то тако же есть рядъ (nominal predicate: такий законний порядок/правило)
# In LS 1566/1588:
# - явным рядомъ и поступомъ права (instrumental: встановлений судовий порядок/процедура)
# - в ряде нашой (locative: у нашій Раді / уряді)

for t in ryad:
    print(f"[{t['src']} | {t['loc']}] {t['form']} -> {t['ctx']}")

print("\n=== 2. DOGOVOR GRAMMAR & ARGUMENT STRUCTURE ===")
# In March 1654:
# - по посольским договорам (prep phrase: згідно з дипломатичними статтями)
# - по Зборовскому договору (prep phrase: згідно з мирним трактатом 1649 р.)
# In Orlyk 1710:
# - Договори і Постановлення (Title & institutional pact)
# - договорили и постановили з ясновельможним (verbal coordination: укласти взаємну угоду)
# - общим договором установляється (instrumental: спільне нормативне погодження)
# - договоры зась сії... исполненію поручаєм (accusative: ратифікований письмовий акт)

for t in dog:
    print(f"[{t['src']} | {t['loc']}] {t['form']} -> {t['ctx']}")

print("\n=== 3. PAKT GRAMMAR & ARGUMENT STRUCTURE ===")
# In Hadiach 1658 / Sejm 1659:
# - Pakta Hadziackie (Title of the treaty)
# - dla tym lepszego tych pakt potwierdzenia (genitive plural: підтвердження статей союзу)
# - do zawarcia pakt (genitive plural: укладення міжнародного миру)
# In Orlyk 1710:
# - в своих границях, пактами... стверджених (instrumental plural: міжнародні договори про кордони)
# - пактами обварованы зостали (instrumental plural: захищені трактатами)

for t in pakt:
    print(f"[{t['src']} | {t['loc']}] {t['form']} -> {t['ctx']}")

