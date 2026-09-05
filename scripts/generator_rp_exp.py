# -*- coding: utf-8 -*-
"""
Full atomic extraction generator for Ruska Pravda Expanded (WIT-RP-EXP-TROITSKY).
Outputs all claims to /home/agents/GitHub/pravda/scratch/rp_exp_claims_all.json
"""
import json
import re

with open('/home/agents/GitHub/pravda/scratch/rp_exp_raw_articles.json', 'r', encoding='utf-8') as f:
    raw_articles = json.load(f)

art_dict = {a[0]: (a[1], a[2]) for a in raw_articles}
claims = []

def add_atom(cid, art, par, quote, actor, op, obj, cond, cons, terms):
    line_no, _ = art_dict[art]
    claims.append({
        "claim_id": cid,
        "witness_id": "WIT-RP-EXP-TROITSKY",
        "fidelity": "L1 (VERIFIED-AGAINST-DIGITAL-DERIVATIVE)",
        "article": f"Артикул {art}",
        "parallel_article": par,
        "locator": f"Троїцький список, ст. {art} (SRC-RP-EXP-DIPLOMATIC.txt, рядок {line_no})",
        "exact_quote": quote,
        "grammatical_actor": actor,
        "textual_operator": op,
        "textual_object": obj,
        "textual_condition": cond,
        "textual_consequence": cons,
        "lexical_terms": terms,
        "interpretation": "EMPTY"
    })

# Now let's import the atoms from modular definitions or populate them directly!
print("Generator framework loaded.")
