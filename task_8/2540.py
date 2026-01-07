from itertools import *

alph = sorted("автор")

for p, s in enumerate(product(alph, repeat=4), start=1):
    s = "".join(s)
    if s == "вата":
        print(p)
        break