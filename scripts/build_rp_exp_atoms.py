# -*- coding: utf-8 -*-
"""
Build atomic claims for Ruska Pravda Expanded Recension (WIT-RP-EXP-TROITSKY).
Follows strictly:
- Primary 115-article numbering of the witness
- Parallel numbering only where established
- Atomic decomposition on change of CONDITION / ACTOR / OPERATOR / OBJECT / CONSEQUENCE
- Extended schema:
  CLAIM-ID, WITNESS-ID, FIDELITY, ARTICLE, PARALLEL-ARTICLE, LOCATOR, EXACT-QUOTE,
  GRAMMATICAL-ACTOR, TEXTUAL-OPERATOR, TEXTUAL-OBJECT, TEXTUAL-CONDITION, TEXTUAL-CONSEQUENCE,
  LEXICAL-TERMS, INTERPRETATION: EMPTY
- ZERO modern legal categories (no human rights, property rights, sovereignty, criminal law, fine, state, etc.)
- Source-near wording in consequences.
"""

import re
from parse_rp_exp_full import articles

# We will structure all atoms systematically.
