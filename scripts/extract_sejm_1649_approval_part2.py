import urllib.request

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

req.headers['Range'] = 'bytes=7944000-7946500'
with urllib.request.urlopen(req, timeout=15) as resp:
    content = resp.read().decode('utf-8', errors='ignore')
    print("Fetched Sejm 1649 approval clause exact lines:")
    print(content)

