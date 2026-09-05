import sys

reg_file = '/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md'
with open(reg_file, 'r', encoding='utf-8') as f:
    content = f.read()

target_start = "## 7. Еталонний повний блок: Руська Правда (Простора редакція)"
target_end = "## 8. Пілотні атоми Литовських Статутів"

if target_start not in content or target_end not in content:
    print("Error: targets not found in content!")
    sys.exit(1)

with open('/home/agents/GitHub/pravda/scratch/rp_exp_purified_block.md', 'r', encoding='utf-8') as f:
    purified_block = f.read().strip()

idx1 = content.find(target_start)
idx2 = content.find(target_end)

new_content = content[:idx1] + purified_block + "\n\n" + content[idx2:]

with open(reg_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully replaced Section 7 with purified block in {reg_file}!")
