import re

# We will define the full list of 43 claims with their parsed details.
# Let's inspect each of the 43 articles to prepare their exact textual cards.

src_file = '/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-RP-SHORT-DIPLOMATIC.txt'
with open(src_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

raw_articles = []
for idx, line in enumerate(lines, 1):
    m = re.match(r'^#\s+(.*)', line.strip())
    if m:
        raw_articles.append((len(raw_articles) + 1, idx, m.group(1)))

print(f"Loaded {len(raw_articles)} raw articles.")
