# -*- coding: utf-8 -*-
import json
import re

with open('/home/agents/GitHub/pravda/scratch/rp_exp_raw_articles.json', 'r', encoding='utf-8') as f:
    raw_articles = json.load(f)

# Comprehensive atomic claims generator for WIT-RP-EXP-TROITSKY (Articles 1-115)
# Every claim has:
# - CLAIM-ID: HC-RP-EXP-XXX[A/B/C...]
# - WITNESS-ID: WIT-RP-EXP-TROITSKY
# - FIDELITY: L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)
# - ARTICLE: Артикул N
# - PARALLEL-ARTICLE: Греков N (де надійно встановлено)
# - LOCATOR: Троїцький список, ст. N (SRC-RP-EXP-DIPLOMATIC.txt, рядок X)
# - EXACT-QUOTE: exact Old East Slavic text
# - GRAMMATICAL-ACTOR: grammatical subject/actor
# - TEXTUAL-OPERATOR: REQUIRES / PROHIBITS / PERMITS / EXEMPTS / CONFIRMS / ASSIGNS / SETS / UNKNOWN
# - TEXTUAL-OBJECT: source-near object
# - TEXTUAL-CONDITION: condition / hypothesis
# - TEXTUAL-CONSEQUENCE: source-near consequence / outcome
# - LEXICAL-TERMS: exact terms from quote
# - INTERPRETATION: EMPTY

print(f"Loaded {len(raw_articles)} raw articles.")
