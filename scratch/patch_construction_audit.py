import json
import re

with open('scratch/audit_instances_payload.json', 'r', encoding='utf-8') as f:
    payload = json.load(f)

voln = payload['VOLN']
svob = payload['SVOB']

# We need to refine the exact formal rules:
# 1. Purge false positive multi-memberships:
#    - LEX-INV2-2306 (Орлик 1710, ряд. 113): «народ вільний руський при правах та вольностях непорушно буде»
#      Has CONST-VOLN-001 (coordination with права), but MUST NOT have CONST-VOLN-004 (not governed by breach verb!).
#      In fact, it has 'при вольностях' -> CONST-VOLN-002!
#    - LEX-INV2-0044 (RP-EXP, ряд. 292): «...но свобода имъ смертию»
#      Is NOM.SG noun свобода -> CONST-SVOB-003, NOT CONST-SVOB-001 (not adjectival!).
# 2. Add formal MATCH-RULE-ID and MATCH-EVIDENCE for every single matched token.
# 3. Define metrics:
#    - TOKEN-COUNT: count of distinct tokens matched by this rule.
#    - CONSTRUCTION-INSTANCE-COUNT: distinct formal construction instances (if 2 tokens are part of the exact same coordinated phrase in the same sentence, e.g. "прав, свобод и вольностей", that counts as 1 instance of the coordinated construction!).
#    - SENTENCE-COUNT: distinct sentence/line locators.

print("Patching rules and compiling formal evidence.")

