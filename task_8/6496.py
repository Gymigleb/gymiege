from itertools import *

alph = "берск"

cnt = 0

for i in range(5, 8):
    for s in product(alph, repeat=i):
        cnt += 1

print(cnt)