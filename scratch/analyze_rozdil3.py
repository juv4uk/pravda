import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/SRC-LS-1588-MAMONICZ-TRANSCRIPTION.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()[780:1161]

art_indices = []
for i, l in enumerate(lines):
    m = re.search(r"===\s*Артыкулъ\s+(\d+)", l)
    if m:
        art_indices.append((int(m.group(1)), i))

for idx, (num, start_line) in enumerate(art_indices):
    end_line = art_indices[idx+1][1] if idx+1 < len(art_indices) else len(lines)
    chunk = lines[start_line:end_line]
    title = ""
    body_lines = []
    for l in chunk[1:]:
        sl = l.strip()
        if not sl: continue
        if not title:
            title = sl
        else:
            body_lines.append(sl)
    body = " ".join(body_lines)
    print(f"=== {num} ===")
    print("TITLE:", title)
    print("BODY:", body[:200])
    print()
