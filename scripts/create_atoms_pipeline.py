# -*- coding: utf-8 -*-
import json
import re

# Load raw articles
from parse_rp_exp_full import articles

# We will generate atomic claims based on clear structural transitions in each article:
# Transition keywords: 'аще ли не будеть', 'аще ли будеть', 'паки ли', 'но оже', 'аже ли', 'будеть ли',
# 'идеть ли', 'а затемь', 'аче же', 'а матерня', 'а матери', 'а се', 'холопьство обелное трое'.

print(f"Total input articles: {len(articles)}")
