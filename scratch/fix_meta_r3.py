# Fix the 5 violations in metadata

with open('/home/agents/GitHub/pravda/scratch/meta_r3_part1.py', 'r', encoding='utf-8') as f:
    p1 = f.read()

# Replace DEFINES with SPECIFIES or DETERMINES
p1 = p1.replace('"REGULATES / REQUIRES / DEFINES"', '"REGULATES / REQUIRES / DETERMINES"')
p1 = p1.replace('"REGULATES / DEFINES / PRESERVES"', '"REGULATES / DETERMINES / PRESERVES"')

with open('/home/agents/GitHub/pravda/scratch/meta_r3_part1.py', 'w', encoding='utf-8') as f:
    f.write(p1)

with open('/home/agents/GitHub/pravda/scratch/meta_r3_part2.py', 'r', encoding='utf-8') as f:
    p2 = f.read()

# Replace "Батьківська автономія" -> "Батьківська воля"
p2 = p2.replace("Батьківська автономія:", "Батьківська воля:")

# Replace "Шляхетська диспозитивна автономія (вольність володіння майном)" -> "Шляхетська майнова вольність"
p2 = p2.replace("Шляхетська диспозитивна автономія (вольність володіння майном):", "Шляхетська майнова вольність:")

# Replace "сплата штрафу" -> "сплата судової вини"
p2 = p2.replace("сплата штрафу", "сплата судової вини")

with open('/home/agents/GitHub/pravda/scratch/meta_r3_part2.py', 'w', encoding='utf-8') as f:
    f.write(p2)

print("Patched metadata files.")
