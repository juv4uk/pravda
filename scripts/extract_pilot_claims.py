import re

def search_in_file(path, pattern, context_lines=2):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    results = []
    for i, l in enumerate(lines):
        if re.search(pattern, l, re.IGNORECASE):
            start = max(0, i - context_lines)
            end = min(len(lines), i + context_lines + 1)
            results.append((i+1, lines[start:end]))
    return results

print("=== RP-SHORT art 16 ===")
for line_no, ctx in search_in_file("sources/primary/transcriptions/diplomatic/SRC-RP-SHORT-DIPLOMATIC.txt", r"свободн"):
    print(f"Line {line_no}:")
    print("".join(ctx))

print("=== RP-EXP art 58 ===")
for line_no, ctx in search_in_file("sources/primary/transcriptions/diplomatic/SRC-RP-EXP-DIPLOMATIC.txt", r"холоп|свобод"):
    if "закуп" in "".join(ctx) or "свобод" in "".join(ctx):
        print(f"Line {line_no}:")
        print("".join(ctx)[:300])
        break

print("=== MARCH 1654 art 1 ===")
for line_no, ctx in search_in_file("sources/primary/transcriptions/diplomatic/SRC-MARCH-1654-DIPLOMATIC.txt", r"прав.*ломат|права"):
    print(f"Line {line_no}:")
    print("".join(ctx))

