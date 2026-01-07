from itertools import *
from string import printable

cnt = 0

for s in product(printable[:8], repeat=5):
    s = "".join(s)
    if s[0] != "0" and s.count("6") == 1:
        if all(i + "6" not in s for i in printable[1:8:2]):
            if all("6" + i not in s for i in printable[1:8:2]):
                cnt += 1

print(cnt)