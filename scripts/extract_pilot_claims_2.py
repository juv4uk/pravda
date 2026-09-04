import re

def search_in_file(path, pattern, max_matches=3):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    count = 0
    for i, l in enumerate(lines):
        if re.search(pattern, l, re.IGNORECASE):
            print(f"[{path}] Line {i+1}: {l.strip()[:150]}")
            start = max(0, i - 1)
            end = min(len(lines), i + 3)
            print("   CONTEXT:\n   " + "   ".join(lines[start:end]))
            count += 1
            if count >= max_matches:
                break

print("=== LS 1566 ===")
search_in_file("sources/primary/transcriptions/diplomatic/SRC-LS-1566-DIPLOMATIC.txt", r"вольност|волност")

print("=== LS 1588 ===")
search_in_file("sources/primary/transcriptions/diplomatic/SRC-LS-1588-DIPLOMATIC.txt", r"вольност|волност")

print("=== HADIACH 1658 ===")
search_in_file("sources/primary/transcriptions/diplomatic/SRC-HADIACH-1658-COMMISSION-DIPLOMATIC.txt", r"wolno[sś][cć]")

print("=== ORLYK 1710 ===")
search_in_file("sources/primary/transcriptions/diplomatic/SRC-ORLYK-1710-UA-DIPLOMATIC.txt", r"вольност|волност")
