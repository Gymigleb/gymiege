from itertools import *

alph = sorted("бмюрн")
cnt = 0

for p, s in enumerate(product(alph, repeat=6), start=1):
    if p % 2 != 0 and s[0] != "м" and s.count("р") >= 2 and s.count("ю") == 0: cnt = p

print(cnt)