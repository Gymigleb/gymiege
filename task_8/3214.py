from itertools import *

alph = sorted("парус")

for p, s in enumerate(product(alph, repeat=5), start=1):
    s = "".join(s)
    if s[0] == "у" and not "аа" in s:
        print(p, s)
        break