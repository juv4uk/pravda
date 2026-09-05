import json

with open('scratch/ryad_tokens.json') as f: ryad = json.load(f)
with open('scratch/dogovor_tokens.json') as f: dog = json.load(f)
with open('scratch/pakt_tokens.json') as f: pakt = json.load(f)

print(f"Loaded: RYAD={len(ryad)}, DOGOVOR={len(dog)}, PAKT={len(pakt)}")

# We will generate dictionary/RYAD-vs-DOGOVOR-vs-PAKT-CONTRAST.md with:
# A. Distribution matrix (Time x Language x Genre x Institution)
# B. Exact morphosyntactic forms breakdown
# C. Governing verbs and predicates
# D. Argument structure & Parties (Who agrees? Who binds? What is agreed?)
# E. Presence of oath and written instrument (Oral vs Written vs Sworn)
# F. Same-sentence co-occurrences
# G. Academic lexicography provenance (LEX-EVID-024..030)
# H. Counterexamples & anomalies
# I. Unresolved cases
# J. Provisional contrast hypothesis (strictly scoped to corpus)

