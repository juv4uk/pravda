import re

src_file = '/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-RP-EXP-DIPLOMATIC.txt'

with open(src_file, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
articles = []
current_art = None
current_text = []
start_line = 0

for line_idx, line in enumerate(lines, 1):
    m = re.match(r'^(\d+)\.\s+(.*)', line.strip())
    if m:
        if current_art is not None:
            articles.append((current_art, start_line, ' '.join(current_text)))
        current_art = int(m.group(1))
        start_line = line_idx
        current_text = [m.group(2)]
    elif current_art is not None:
        if line.strip().startswith('==') or line.strip().startswith('[['):
            continue
        if line.strip():
            current_text.append(line.strip())

if current_art is not None:
    articles.append((current_art, start_line, ' '.join(current_text)))

print(f"Parsed {len(articles)} articles from SRC-RP-EXP-DIPLOMATIC.txt")
assert len(articles) == 115, f"Expected 115 articles, got {len(articles)}"
