from itertools import *
from string import printable

cnt = 0

for s in product(printable[:12], repeat=7):
    s = "".join(s)
    m = s
    if s[0] != "0":
        for i in printable[:12:2]: m = m.replace(i, "0")
        for i in printable[1:12:2]: m = m.replace(i, "1")
        if s.count("b") == 2 and "00" not in m and "11" not in m:
            cnt += 1
    if cnt != 0 and cnt % 10000 == 0: print(cnt)


print(cnt)