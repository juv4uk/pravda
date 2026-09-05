import re
import sys

with open('sources/primary/transcriptions/SRC-LS-1588-MAMONICZ-TRANSCRIPTION.txt', 'r', encoding='utf-8') as f:
    text = f.read()

rozdil1 = text[text.find('Роздел первый'):text.find('Розделъ вторый')]
arts = re.split(r'\n(?==== Артыкулъ \d+\. ===)', rozdil1)

parsed_articles = []
for i in range(1, len(arts)):
    raw = arts[i].strip()
    m = re.match(r'=== Артыкулъ\s+(\d+)\.\s*===\s*\n+(.*?)(?=\n\n|\Z)', raw, re.DOTALL)
    num = int(m.group(1))
    title = m.group(2).strip().replace('\n', ' ')
    body = raw[m.end():].strip()
    parsed_articles.append((num, title, body))

for num, title, body in parsed_articles:
    print(f"--- ARTICLE {num} ---")
    print(f"TITLE: {title}")
    # print first 200 chars of body
    print(f"BODY: {body[:250]}...\n")

