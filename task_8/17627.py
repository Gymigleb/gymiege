from itertools import *

cnt = 0

for s in product(range(15), repeat=5):
    if s[0] != 0 and s.count(8) == 1:
        if sum(s.count(i) for i in range(10,15)) >= 2:
            cnt += 1

print(cnt)