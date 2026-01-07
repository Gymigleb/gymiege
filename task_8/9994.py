from itertools import *

alph = sorted("школа")

for p, s in enumerate(product(alph, repeat=5), start=1):
    s = "".join(s)
    if s == "шалаш": print(p)