# -*- coding: utf-8 -*-
"""
Automated and verified decomposition of all 115 articles of RP Expanded
(WIT-RP-EXP-TROITSKY).
Outputs a unified json list of claims with 100% field compliance.
"""

import json
import re
from parse_rp_exp_full import articles

# We will load and execute the claims generation.
