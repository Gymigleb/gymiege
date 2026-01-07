from itertools import *
from string import printable

cnt = 0

for s in product(printable[:16], repeat=3):
    s = "".join(s)
    a = s

    for i in printable[:16:2]:
        a = a.replace(i, "0")
    for i in printable[1:16:2]:
        a = a.replace(i, "1")

    if s[0] != "0" and len(set(s)) == 3 and "00" not in a and "11" not in a:
        cnt += 1

print(cnt)