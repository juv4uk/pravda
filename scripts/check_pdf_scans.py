import urllib.request
import json

# Check availability of PDF scans for:
# 1. Volumina Legum Tom IV (1859 Ohryzko): WBC publication 47936 / Internet Archive volumina-legum
# 2. Third Lithuanian Statute 1588 (Minsk 1989 facsimile / Mamonichi 1588): Pravo.by / Bielarusian Digital Library
# 3. Orlyk 1710: RGADA f. 13, delo 10, ark 1-19 facsimile in "Arkhivy Ukrayiny" 2010 No 3-4 (O. Vovk)
# 4. Russkaya Pravda: Troitsky ms F.p.IV.183 facsimile (RNB) / Rossiyskoye zakonodatelstvo 1984
print("Checking scan links and metadata for L2 Collation Table...")
