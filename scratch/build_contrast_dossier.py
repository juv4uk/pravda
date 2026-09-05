import json

with open('scratch/analyzed_voln.json', 'r', encoding='utf-8') as f:
    voln = json.load(f)

with open('scratch/analyzed_svob.json', 'r', encoding='utf-8') as f:
    svob = json.load(f)

print(f"Building contrast dossier from {len(voln)} VOLN and {len(svob)} SVOB records.")

# Prepare markdown tables
# Table 1: VOLNOST Morphosyntax Matrix (selected 25 representative tokens across all corpora)
# Table 2: SVOBODA Morphosyntax Matrix (all 31 tokens)

