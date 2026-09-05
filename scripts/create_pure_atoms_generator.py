# -*- coding: utf-8 -*-
import json
import re

# Load raw articles
with open('/home/agents/GitHub/pravda/scratch/rp_exp_raw_articles.json', 'r', encoding='utf-8') as f:
    raw_articles = json.load(f)

# Load existing 160 atoms from parts 1-5
import sys
sys.path.append('scripts')
from build_atoms_data_part1 import atoms_part1
from build_atoms_data_part2 import atoms_part2
from build_atoms_data_part3 import atoms_part3
from build_atoms_data_part4 import atoms_part4
from build_atoms_data_part5 import atoms_part5

all_atoms = atoms_part1 + atoms_part2 + atoms_part3 + atoms_part4 + atoms_part5
print(f"Total atoms loaded: {len(all_atoms)}")

# Now, we will purify every atom:
# Replace paraphrased TEXTUAL-OBJECT with literal source-near description using Old East Slavic words from the quote!
# Let's inspect each atom and provide pure source-near objects.
