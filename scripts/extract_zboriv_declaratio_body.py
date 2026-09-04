import urllib.request
import re

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

# Byte 7944909 has:
# "tedy tę deklaracyą łaski naszey uczynioną pod Zborowem woysku Zaporowskiemu, authoritate Conventus praesentis, za zgodą wszech Stanow, approbuiemy."
# Let us inspect the range around 7940000 - 7950000 to see whether the full text of Deklaracya was inserted into the Sejm constitution or only the approval clause!
start_byte = 7944909 - 8000
end_byte = 7944909 + 8000
req.headers['Range'] = f'bytes={start_byte}-{end_byte}'
with urllib.request.urlopen(req, timeout=30) as resp:
    snippet = resp.read().decode('utf-8', errors='ignore')
    print("Length of snippet:", len(snippet))
    print(snippet[:3000])

