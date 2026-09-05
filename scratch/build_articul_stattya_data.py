import re
import os
import json

files = {
    'RP-SHORT': 'sources/primary/transcriptions/SRC-RP-SHORT-ACADEMIC-WITNESS.txt',
    'RP-EXP': 'sources/primary/transcriptions/SRC-RP-EXP-TROITSKY-WITNESS.txt',
    'LS-1566': 'sources/primary/transcriptions/SRC-LS-1566-TRANSCRIPTION.txt',
    'LS-1588': 'sources/primary/transcriptions/SRC-LS-1588-MAMONICZ-TRANSCRIPTION.txt',
    'ZBORIV': 'sources/primary/transcriptions/SRC-ZBORIV-1649-DECLARATION.txt',
    'MARCH-1654': 'sources/primary/transcriptions/SRC-MARCH-1654-POSOLSKIY-TRANSCRIPTION.txt',
    'HADIACH-1658': 'sources/primary/transcriptions/SRC-HADIACH-1658-COMMISSION-POLISH.txt',
    'ORLYK-1710': 'sources/primary/transcriptions/SRC-ORLYK-1710-UA-TRANSCRIPTION.txt'
}

corpus = {}
for code, path in files.items():
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            corpus[code] = f.read()

# Analyze ARTICUL
art_data = {}
for code, text in corpus.items():
    matches = list(re.finditer(r'(?:[^\n]+\n){0,1}[^\n]*\b(артыкул[а-яѣъ]*|артикул[а-яѣъ]*|artykuł[a-z]*)\b[^\n]*(?:\n[^\n]+){0,1}', text, re.IGNORECASE))
    tokens = []
    for m in matches:
        raw_token = re.search(r'\b(артыкул[а-яѣъ]*|артикул[а-яѣъ]*|artykuł[a-z]*)\b', m.group(0), re.IGNORECASE).group(0)
        tokens.append({
            'form': raw_token,
            'context': m.group(0).strip().replace('\n', ' ')
        })
    art_data[code] = tokens

# Analyze STATTYA
stat_data = {}
for code, text in corpus.items():
    # Only genuine article meanings: стать*, стате* (excluding статки, статечне)
    matches = list(re.finditer(r'(?:[^\n]+\n){0,1}[^\n]*\b(стат[ьъеѣя][а-яѣъ]*)\b[^\n]*(?:\n[^\n]+){0,1}', text, re.IGNORECASE))
    tokens = []
    for m in matches:
        raw_token = re.search(r'\b(стат[ьъеѣя][а-яѣъ]*)\b', m.group(0), re.IGNORECASE).group(0)
        if any(ex in raw_token.lower() for ex in ['статък', 'статки', 'статок', 'статечн']):
            continue
        tokens.append({
            'form': raw_token,
            'context': m.group(0).strip().replace('\n', ' ')
        })
    stat_data[code] = tokens

print("=== ARTICUL TOKENS SUMMARY ===")
for code, items in art_data.items():
    print(f"{code}: {len(items)} tokens")

print("\n=== STATTYA TOKENS SUMMARY ===")
for code, items in stat_data.items():
    print(f"{code}: {len(items)} tokens")

