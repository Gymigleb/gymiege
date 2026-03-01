from itertools import *
from string import printable

cnt = 0

for i in product(printable[:13], repeat=6):
    if i[0] != "0" and i.count("0") >= 2 and sum([i.count(_) for _ in printable[9:13]]) == 2:
        cnt += 1

print(cnt)