import re

src_file = '/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-RP-SHORT-DIPLOMATIC.txt'

with open(src_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

articles = []
for idx, line in enumerate(lines, 1):
    m = re.match(r'^#\s+(.*)', line.strip())
    if m:
        articles.append((len(articles) + 1, idx, m.group(1)))

for num, line_no, text in articles:
    print(f"--- Article {num} (Line {line_no}) ---")
    print(text)
    print()
