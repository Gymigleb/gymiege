from itertools import *

cnt = 0

for i in product(list(range(9)), repeat=7):
    if i[0] % 2 == 0 and i[0] != 0:
        if i[-1] % 3 != 0 and i.count(6) >= 1:
            cnt += 1

print(cnt)
