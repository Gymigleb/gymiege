from itertools import *

alph = sorted("аргумент")

for pos, s in enumerate(product(alph, repeat=4), start=1):
    if len(s) == len(set(s)) and "".join(s) == "".join(sorted(s)):
        print(pos)
        print(pos, s)