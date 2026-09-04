import urllib.request
import re

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

chunk_size = 1024 * 1024
current_byte = 0
found_pos = -1

with urllib.request.urlopen(req, timeout=60) as resp:
    while True:
        chunk = resp.read(chunk_size)
        if not chunk:
            break
        text = chunk.decode("utf-8", errors="ignore")
        m = re.search(r"Approbacya\s+kommissyi\s+Hadyackiey", text, re.IGNORECASE)
        if m:
            found_pos = current_byte + m.start()
            print(f"FOUND at byte: {found_pos}")
            # print surrounding text
            snippet = text[max(0, m.start()-500):min(len(text), m.start()+5000)]
            print(snippet)
            # save snippet
            with open("/home/agents/GitHub/pravda/scripts/hadiach_sejm_raw.txt", "w", encoding="utf-8") as out_f:
                out_f.write(snippet)
            break
        current_byte += len(chunk)

