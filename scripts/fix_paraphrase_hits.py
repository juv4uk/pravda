# -*- coding: utf-8 -*-
with open('scripts/build_atoms_data_part1.py', 'r', encoding='utf-8') as f:
    t1 = f.read()
# In HC-RP-EXP-004B: 'сплати' is in source text ('но сплати имъ во обчи 40 гривенъ').
# In linter check, 'сплат' matched 'сплати' / 'исплатившю'.
# In Old East Slavic text, 'сплати' and 'исплатившю' are source words!
# But in 'condition' of HC-RP-EXP-067A: 'при взыскании' -> 'оже ся взимаеть 12 гривенъ продажи'
# In HC-RP-EXP-098A: 'при завещании матерью своего имущества' -> 'аже мати дасть свое сыну или дчери'
