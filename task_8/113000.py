from itertools import *

alph = sorted("гондубш")
for p, s in enumerate(product(alph, repeat=6), start=1):
    if p % 2 == 1 and s[0] != "б" and s.count("н") >= 2 and not "у" in s:
        print(p, s)