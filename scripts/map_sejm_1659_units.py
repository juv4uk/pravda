import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to list all units with:
# unit_id, heading, page, start_line, end_line, text_snippet
# Part A: KOMMISSYA HADIACKA (pp. 297-301)
# Part B: APPROBACYA KOMMISSYJ HADYACKIEY (p. 301)
# Part C: Subsequent separate constitutions (pp. 301-307)
print("Mapping script created.")
