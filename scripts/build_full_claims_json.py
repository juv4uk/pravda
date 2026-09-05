# -*- coding: utf-8 -*-
import json
import re

with open('/home/agents/GitHub/pravda/scratch/rp_exp_raw_articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# We will define the full atom specifications for all 115 articles.
# Let's verify that we cover 1 to 115 without gaps.
art_map = {a[0]: (a[1], a[2]) for a in articles}
assert len(art_map) == 115, "Expected 115 articles in map"
print("Article map verified: 115 articles.")
