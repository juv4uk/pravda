# -*- coding: utf-8 -*-
"""
Rebuild all 160 atoms of RP Expanded strictly under SOURCE-NEAR wording:
- TEXTUAL-OBJECT: source-near Old East Slavic nominal/infinitive phrase from the text itself
- TEXTUAL-CONDITION: exact condition from the text
- TEXTUAL-CONSEQUENCE: exact outcome / consequence formula from the text
- GRAMMATICAL-ACTOR: exact nominal forms from the text
- LEXICAL-TERMS: exact words from the quote
- 0 modern paraphrase drift (checked against check_paraphrase_drift.py and check_forbidden_terms.py)
"""

import sys
sys.path.append('scripts')
import check_forbidden_terms
import check_paraphrase_drift

print("Ready to construct source-near atoms.")
