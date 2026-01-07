from itertools import *

alph = sorted("гранит")

for p, s in enumerate(product(alph, repeat=6), start=1):
    s = "".join(s)
    if p % 2 == 1 and s[0] not in "аиг" and s.count("а") == 1:
        print(p, s)
        break