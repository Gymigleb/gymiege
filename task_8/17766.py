from itertools import *

alph = sorted("сентябрь")

for p, s in enumerate(product(alph, repeat=5), start=1):
    s = "".join(s)
    if p % 2 == 0 and s[0] == "р" and "ь" not in s:
        print(p, s)