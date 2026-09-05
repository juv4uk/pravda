import json
import re

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

# Let's inspect the entire set of 88 VOLN tokens and classify each into its exact structural frame.
# We will identify:
# 1. Rubrication frame: [О / В / РОЗДЕЛ О] + [вольностяхъ / вольности] + [INF / GEN-ACTION / GEN-HOLDER]
# 2. Coordination frame: [права / свободи / привілеї / листи] + [вольності]
# 3. Prepositional attachment 'при / при вольностях' + [заховати / зоставити / держати / ставати]
# 4. Confirmation / granting: [дати / потвердити / конфирмовати / обварувати / надати] + [вольности]
# 5. Breach / deprivation: [порушити / отбирати / отводити / поламати / na ujmę] + [вольности]
# 6. Usage / enjoyment: [уживати / заживати / gaudere / веселитися] + [вольностей]
# 7. Singular capability / transit / choice: [вольность и моцъ] / [вольность на водах] / [вольность на соймики]
# 8. Attribution / genitive adjunct: [листи і вольності] / [вольності привілеїв] / [сторожа посполитої вольності]

print(f"Auditing complete set of {len(voln)} VOLN and {len(svob)} SVOB tokens.")

