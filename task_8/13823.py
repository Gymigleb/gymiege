from itertools import *

alph = sorted("мизантроп")
cnt = 0

for p, s in enumerate(product(alph, repeat=5), start=1):
    if p % 2 == 0 and s[0] == "н" and s.count("р") == 2: cnt = p

print(cnt)