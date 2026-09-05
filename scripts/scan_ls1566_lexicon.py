import re

with open('/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-LS-1566-DIPLOMATIC.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Tier A patterns:
tier_a_patterns = [
    (r'\bвольн[ое][сз]т[а-яЂі]*', 'вольност*'),
    (r'\bпривил[еЂи][а-яЂі]*', 'привил*'),
    (r'\bсвобод[а-яЂі]*', 'свобод*'),
    (r'\b[оз]выча[а-яЂі]*', 'обыча* / звыча*'),
    (r'\bпр[иы][сЂ]яг[а-яЂі]*', 'присяг* / прысяг*')
]

# Let us see the frequency of Tier A in LS-1566
for pat, label in tier_a_patterns:
    matches = list(re.finditer(pat, text, re.IGNORECASE))
    print(f"Pattern '{label}': {len(matches)} matches")

