import re

def find_first(path, pattern):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        if re.search(pattern, l, re.IGNORECASE):
            return i+1, l.strip(), lines[max(0, i-2):min(len(lines), i+3)]
    return None

print("LS 1566:")
res = find_first("sources/primary/transcriptions/diplomatic/SRC-LS-1566-DIPLOMATIC.txt", r"волност|вольност")
if res:
    print(f"Line {res[0]}: {res[1]}")
    print("".join(res[2]))

print("\nLS 1588 (art 1 or similar):")
res = find_first("sources/primary/transcriptions/diplomatic/SRC-LS-1588-DIPLOMATIC.txt", r"всих прав и вольностей")
if res:
    print(f"Line {res[0]}: {res[1]}")
    print("".join(res[2]))

print("\nOrlyk 1710 art 6:")
res = find_first("sources/primary/transcriptions/diplomatic/SRC-ORLYK-1710-UA-DIPLOMATIC.txt", r"самовлад|волност|конференц")
if res:
    print(f"Line {res[0]}: {res[1]}")
    print("".join(res[2]))
