from itertools import *

alph = sorted("престол")

cnt = 0

for p, s in enumerate(product(alph, repeat=5), start=1):
    s = "".join(s)
    if p % 2 == 0 and sum([s.count(i) for i in "прстл"]) <= 3 and s[-1] in "ео": cnt += 1

print(cnt)