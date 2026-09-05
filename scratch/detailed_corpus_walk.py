import re

with open('scratch/voln_noun_dump.txt', 'r', encoding='utf-8') as f:
    voln_blocks = f.read().split('\n\n')

for b in voln_blocks:
    if 'SRC-HADIACH' in b or 'SRC-MARCH' in b:
        print(b)
        print("-" * 40)
