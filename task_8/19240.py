from itertools import *

alph = sorted("январь")

for p, s in enumerate(product(alph, repeat=5), start=1):
    if s[0] != "я" and s.count("ь") <= 1 and "яя" not in s:
        print(p, s)