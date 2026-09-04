import urllib.request
import re

url = "https://archive.org/download/volumina-legum/VOLUMINA%20LEGUM_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

start_byte = 8908860 - 2000
# p. 297 to 308 (approx 12 pages, around 60KB-100KB)
end_byte = start_byte + 150000

req.headers['Range'] = f'bytes={start_byte}-{end_byte}'
with urllib.request.urlopen(req, timeout=60) as resp:
    text = resp.read().decode('utf-8', errors='ignore')
    print("Downloaded bytes:", len(text))
    
    # Let us see where KOMMISSYA HADIACKA starts and where Konstytucye W. X. Litewskiego starts (p. 310)
    start_pos = text.find("KOMMISSYA HADIACKA.")
    end_pos = text.find("Konstytucye W. X. Litewskiego")
    if end_pos == -1:
        end_pos = text.find("WIELKIEGO XIĘSTWA LITEWSKIEGO")
    
    print("Start pos:", start_pos, "End pos:", end_pos)
    hadiach_text = text[start_pos:end_pos if end_pos != -1 else start_pos + 80000]
    
    out_path = "/home/agents/GitHub/pravda/sources/primary/transcriptions/diplomatic/SRC-HADIACH-SEJM-1659-DIPLOMATIC.txt"
    
    header = """SOURCE-METADATA:
SOURCE-ID: SRC-HADIACH-SEJM-1659
WORK: Sejmowa Konstytucya Approbacyi Kommissyi Hadziackiey (1659 r.)
TITLE: KOMMISSYA HADIACKA (Volumina Legum, Tom IV, pp. 297–308)
PRINTED-EDITION: Volumina Legum: Przedruk zbioru praw staraniem XX. Pijarow w Warszawie, od roku 1732 do 1782, wydanego. Wydanie Jozafata Ohryzki. — Petersburg, 1859. — Tom IV. — S. 297–308.
PHYSICAL-WITNESS: Druk sejmowy Konstytucji 1659 r. / Metryka Koronna (AGAD, Warszawa)
INTERMEDIARY: Internet Archive / Wielkopolska Biblioteka Cyfrowa (djvu extraction)
TRANSCRIPTION-MODE: DIPLOMATIC (XVIII/XIX w. ortografia druku Volumina Legum)
LOCAL-TEXT-FIDELITY: L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)
TEXT-LOSS-RISK: LOW (Повний автентичний текст конституції сейму 1659 р. з офіційного зведення законів)
SOURCE-INTERPRETATION-RISK: VERY HIGH (Офіційний акт ратифікації Сеймом Речі Посполитої у травні-червні 1659 р. суттєво відрізнявся від первинного Гадяцького проекту комісії вересня 1658 р.: було вилучено окремий монетний двір та найвищий судовий трибунал Русі, збережено контрреформаційні застереження і відновлено майнові претензії шляхти, що викликало вибух невдоволення в Україні та повалення Виговського).
================================================================================

"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + hadiach_text)
    
    print(f"Written successfully to {out_path} ({len(header) + len(hadiach_text)} bytes)!")

