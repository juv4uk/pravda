import urllib.request
import re

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

# In the index we saw:
# "Approbacya deklaracyi laski Krola Imci Iana Kazimierza pod Zborowem woysku Zaporowskiemu daney: a. 1649, v. 1v, f. 285"
# Wait, "f. 285" (folio/page 285) or around page 130-150 for year 1649/1650!
# Let us search for "Zborow" in the body of Volume IV (between bytes 4,000,000 and 8,500,000)
chunk_size = 1024 * 1024
current_byte = 0

with urllib.request.urlopen(req, timeout=60) as resp:
    while True:
        chunk = resp.read(chunk_size)
        if not chunk:
            break
        text = chunk.decode("utf-8", errors="ignore")
        # search for Deklaracya and Zborow
        for m in re.finditer(r"(Deklaracya|Punkta|Zborow|Zborov)", text, re.IGNORECASE):
            sub = text[max(0, m.start()-100):min(len(text), m.start()+400)]
            if ("zborow" in sub.lower() or "zborov" in sub.lower()) and ("woysk" in sub.lower() or "kazimierz" in sub.lower() or "chmiel" in sub.lower() or "1649" in sub.lower() or "1650" in sub.lower()):
                print(f"FOUND MATCH at byte {current_byte + m.start()}:")
                print(sub)
                print("="*40)
                if current_byte < 20000000: # before index
                    with open("/home/agents/GitHub/pravda/scripts/zboriv_match.txt", "w", encoding="utf-8") as f_out:
                        f_out.write(text[max(0, m.start()-200):min(len(text), m.start()+8000)])
                    print("Saved match snippet to file!")
        current_byte += len(chunk)
        if current_byte > 10000000: # stop before volume IV index
            break
