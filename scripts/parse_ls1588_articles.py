import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-LS-1588-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Split text into sections using the top-level section markers
# === SECTION: Title ===
# Notice top-level section markers have === TAG: Title ===
sec_splits = list(re.finditer(r'===\s*([A-Z0-9\-_]+):\s*([^=]+)\s*===', text))
units_1588 = []

for idx, s in enumerate(sec_splits):
    sec_tag = s.group(1).strip()
    sec_title = s.group(2).strip()
    start_pos = s.end()
    end_pos = sec_splits[idx+1].start() if idx+1 < len(sec_splits) else len(text)
    sec_text = text[start_pos:end_pos]
    
    if sec_tag in ['PRIVILEGE', 'DEDICATION-SIGISMUND', 'HERB-VERSE', 'PREFACE-SAPIEHA']:
        units_1588.append({
            'section_tag': sec_tag,
            'chapter': sec_title,
            'article': sec_tag,
            'locator': sec_title,
            'text': sec_text.strip()
        })
    else:
        # Split chapter into articles using '=== Артыкулъ N. ==='
        art_splits = list(re.finditer(r'===\s*Артыкул[ъ]?\s*(\d+)\.?\s*===', sec_text))
        if not art_splits:
            units_1588.append({
                'section_tag': sec_tag,
                'chapter': sec_title,
                'article': 'ТЕКСТ',
                'locator': f'{sec_title}, Текст',
                'text': sec_text.strip()
            })
        else:
            preface = sec_text[:art_splits[0].start()].strip()
            if len(preface) > 50:
                units_1588.append({
                    'section_tag': sec_tag,
                    'chapter': sec_title,
                    'article': 'ВСТУП',
                    'locator': f'{sec_title}, Вступ',
                    'text': preface
                })
            for j in range(len(art_splits)):
                a_num = art_splits[j].group(1)
                a_start = art_splits[j].start()
                a_end = art_splits[j+1].start() if j+1 < len(art_splits) else len(sec_text)
                art_content = sec_text[a_start:a_end].strip()
                units_1588.append({
                    'section_tag': sec_tag,
                    'chapter': sec_title,
                    'article': f'Артикул {a_num}',
                    'locator': f'{sec_title}, Артикул {a_num}',
                    'text': art_content
                })

print(f"Total units parsed in LS-1588: {len(units_1588)}")

