import re

with open('scratch/svobod_dump.txt') as f:
    s_text = f.read()

for b in s_text.split('\n\n'):
    b_l = b.lower()
    if 'волн' in b_l or 'woln' in b_l:
        print(b)
        print("="*40)
