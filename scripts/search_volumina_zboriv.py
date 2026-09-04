import urllib.request
import re

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

# In Volumina Legum, Jan Casimir's Sejm of 1649 or 1650 (Warsaw) ratified the Zboriv agreement
# Under the title "Deklaracya łaski naszey woysku Zaporoskiemu" or "Punkta pod Zborowem"
chunk_size = 1024 * 1024
current_byte = 0

with urllib.request.urlopen(req, timeout=60) as resp:
    while True:
        chunk = resp.read(chunk_size)
        if not chunk:
            break
        text = chunk.decode("utf-8", errors="ignore")
        m = re.search(r"Zborow|Zborov", text, re.IGNORECASE)
        if m:
            # check if it's 1649/1650
            sub = text[max(0, m.start()-200):min(len(text), m.start()+500)]
            if any(y in sub for y in ["1649", "1650", "Chmielnick", "Zaporos"]):
                print(f"FOUND Zboriv at byte {current_byte + m.start()}:")
                print(sub)
                break
        current_byte += len(chunk)

