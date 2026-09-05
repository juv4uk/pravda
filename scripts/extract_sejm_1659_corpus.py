import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text = f.read()

body = text.split('================================================================================')[1]

# Divide into Part A and Part B/C
pacta_end = body.find('Approbacya kommissyj Hadyackiey.')
part_a = body[:pacta_end]
part_b_c = body[pacta_end:]

# Part A extraction:
# Let's extract claims from Part A (Kommissya Hadiacka as inserted into Volumina Legum)
# It has Preamble, Art 1 (religia, edukacja), Art 2 (amnestia, granice), Art 3 (woysko, nobilitacja, woyska koronne),
# Art 4 (hetmanat, mennica, obrona), Art 5 (relacje z postronnymi), Art 6 (reindukcja, trybunal, urzedy, konwokacja)
print("Part A and Part B/C isolated.")
