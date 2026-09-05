import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    full_text = f.read()

body = full_text.split('================================================================================')[1]
pacta_end = body.find('Approbacya kommissyj Hadyackiey.')
part_a = body[:pacta_end]
part_bc = body[pacta_end:]

# We will build structured claims for:
# 1. PART A: WIT-HADIACH-SEJM-1659-PACTA (Kommissya Hadiacka as inserted into Sejm register, pp. 297–301)
#    - Unit: UNIT-SEJM1659-KOMMISSYA
# 2. PART B: WIT-HADIACH-SEJM-1659-APPROBACYA (Approbacya kommissyj Hadyackiey, p. 301)
#    - Unit: UNIT-SEJM1659-APPROBACYA
# 3. PART C: WIT-HADIACH-SEJM-1659-STATUTES (Separate statutory constitutions, pp. 301–307)
#    - Individual units with PRINTED-HEADING and PAGE

print("Extracting full Sejm corpus...")
