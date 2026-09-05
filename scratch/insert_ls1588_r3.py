with open('/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md', 'r', encoding='utf-8') as f:
    text = f.read()

with open('/home/agents/GitHub/pravda/scratch/LS1588_R3_GENERATED.md', 'r', encoding='utf-8') as f:
    r3_block = f.read()

target = "## 9. Пілотні атоми Литовського Статуту 1566 року"
assert target in text, "Target heading not found!"

# We will insert Section 9 before "## 9. Пілотні атоми Литовського Статуту 1566 року",
# and renumber Section 9 to Section 10.
p = text.find(target)

# Update the target heading to Section 10
renumbered_ls1566 = text[p:].replace("## 9. Пілотні атоми Литовського Статуту 1566 року", "## 10. Пілотні атоми Литовського Статуту 1566 року", 1)

new_full_text = text[:p] + r3_block.strip() + "\n\n---\n\n" + renumbered_ls1566

with open('/home/agents/GitHub/pravda/HISTORICAL-CLAIMS-REGISTER.md', 'w', encoding='utf-8') as f:
    f.write(new_full_text)

print("Successfully inserted Section 9: LS 1588 Rozdil 3 (51 claims) and renumbered Section 10!")
