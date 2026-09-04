# In Volumina Legum Tom IV, page 120 (Sejm 1649):
# The Sejm passed the Constitution: "Approbaeja deklaracyi laski naszey woysku Zaporowskiemu daney"
# Let us read the exact lines around byte 7944909 in Volumina Legum:
with open("/home/agents/GitHub/pravda/scripts/hadiach_body_snippet.txt", "r", encoding="utf-8") as f:
    pass

import urllib.request

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

# We will stream the slice from byte 7943000 to 7946000
req.headers['Range'] = 'bytes=7943000-7946500'
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        print("Fetched Sejm 1649 approval clause:")
        print(content)
except Exception as e:
    print("Error:", e)

