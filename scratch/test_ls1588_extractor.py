import re
import sys

with open('sources/primary/transcriptions/SRC-LS-1588-MAMONICZ-TRANSCRIPTION.txt', 'r', encoding='utf-8') as f:
    text = f.read()

rozdil1 = text[text.find('Роздел первый'):text.find('Розделъ вторый')]
arts = re.split(r'\n(?==== Артыкулъ \d+\. ===)', rozdil1)

print(f"Total blocks in Rozdil 1: {len(arts)}")
assert len(arts) == 36, f"Expected 36 blocks, got {len(arts)}"

parsed_articles = []
for i in range(1, len(arts)):
    raw = arts[i].strip()
    m = re.match(r'=== Артыкулъ\s+(\d+)\.\s*===\s*\n+(.*?)(?=\n\n|\Z)', raw, re.DOTALL)
    if not m:
        print(f"Failed to match Art {i}")
        continue
    num = int(m.group(1))
    title = m.group(2).strip().replace('\n', ' ')
    body = raw[m.end():].strip()
    parsed_articles.append((num, title, body))

print(f"Successfully parsed {len(parsed_articles)} articles.")
for num, title, body in parsed_articles[:5]:
    print(f"Art {num}: {title[:60]}... (body length: {len(body)})")

