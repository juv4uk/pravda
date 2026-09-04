import urllib.request
import re

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

target_start_byte = 10000000
target_end_byte = 11000000

# Let us fetch the exact chunk around byte 10485760
req.headers['Range'] = f'bytes={10485760 - 300000}-{10485760 + 300000}'
with urllib.request.urlopen(req, timeout=30) as resp:
    chunk = resp.read().decode('utf-8', errors='ignore')
    print("Fetched chunk length:", len(chunk))
    # search for Approbacya
    pos = chunk.find("Approbacya kommissyi Hadyackiey")
    if pos != -1:
        print("Found Approbacya at pos:", pos)
        print(chunk[pos-200:pos+3000])
    else:
        print("Not found with exact string, searching regex:")
        m = re.search(r"Approbacya.*Hadyac", chunk, re.IGNORECASE)
        if m:
            print("Regex found:", m.group(0))
            p = m.start()
            print(chunk[p-200:p+3000])
