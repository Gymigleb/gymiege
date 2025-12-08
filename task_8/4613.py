from itertools import *
from string import printable

cnt = 0

for s in product(printable[:9], repeat=5):
    s = "".join(s)
    if s[0] not in "013579" and s[-1] not in "18" and s.count("3") <= 1:
        cnt += 1

print(cnt)