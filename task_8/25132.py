from itertools import *

alph = sorted("сдайегэ")

ans = 0

for p, s in enumerate(product(alph, repeat=6), start=1):
    s = "".join(s)
    if "егэ" in s: ans += p

print(ans)