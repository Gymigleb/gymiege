from itertools import *

cnt = 0

for s in product(range(8), repeat=5):
    if s[0] != 0 and s[0] % 2 == 0  and s[-1] not in [2,6] and s.count(7) <= 2:
        cnt += 1

print(cnt)