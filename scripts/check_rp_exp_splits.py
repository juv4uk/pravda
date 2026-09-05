import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-RP-EXP-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
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

print(f"Total articles parsed: {len(articles)}")
# Print articles that have clear multiple subclauses (semicolons, 'Аще ли', 'Будеть ли', 'Паки ли', etc.)
composite_count = 0
for art_no, line_no, art_text in articles:
    # check conditions
    conds = re.findall(r'(?:^|[.;])\s*(Аже|Аще|Оже|Будеть ли|Искавше ли|Паки ли|Не хотети ли)', art_text)
    if len(conds) > 1 or ';' in art_text:
        composite_count += 1

print(f"Articles with potential multi-condition structure: {composite_count}")
