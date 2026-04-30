from itertools import *

alph = sorted("апрель")
cnt = 0

for pos, i in enumerate(product(alph, repeat=6), start=1):
    if pos % 2 != 0 and i[0] not in "ал" and i.count("п") >= 2:
        cnt += 1

print(cnt)