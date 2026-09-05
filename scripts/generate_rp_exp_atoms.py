# -*- coding: utf-8 -*-
"""
Generate complete atomic decomposition of WIT-RP-EXP-TROITSKY (Articles 1-115).
Enforces:
- PRIMARY ARTICLE NUMBER: 1 to 115 from witness text.
- PARALLEL-NUMBER: established cross-reference where verified.
- ATOMIC DECOMPOSITION: A/B/C splitting strictly on change of:
  CONDITION / ACTOR / OPERATOR / OBJECT / CONSEQUENCE.
- ZERO modern legal vocabulary (0 linter hits).
- SOURCE-NEAR consequence wording.
- INTERPRETATION: EMPTY.
"""

from parse_rp_exp_full import articles
import re
import sys

