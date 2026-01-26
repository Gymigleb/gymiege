from itertools import *

cnt = 0

for i in product(range(9), repeat=7):
    if i[0] != 0 and i[0]%2 != 1 and i[-1]%2 != 0:
        if i.count(8) == 1: cnt += 1

print(cnt)