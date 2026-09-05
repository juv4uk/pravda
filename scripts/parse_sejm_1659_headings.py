import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text = f.read()

body = text.split('================================================================================')[1]
pacta_end = body.find('Approbacya kommissyj Hadyackiey.')
part_a = body[:pacta_end]
part_bc = body[pacta_end:]

# Let us verify the units in Part B/C
# Pattern of headings in Part B/C:
# Each heading is followed by an article number or text.
lines = part_bc.split('\n')

units = []
current_unit = None
cur_lines = []

for idx, line in enumerate(lines):
    l = line.strip()
    # Check if line is a page marker or header artifact
    if l.isdigit() or l.startswith(('T. IV', 'ZA JANA', 'KONSTYTUCYE SEYMU')):
        continue
    # Let's see if line is a heading
    # We can detect headings from our verified list
