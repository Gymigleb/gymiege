from itertools import *

alph = "0123456"
cnt = 0

for i in product(alph, repeat=7):
    if i[0] not in "035":
        i = "".join(i)
        a = "22" in i
        b = "44" in i
        if a + b < 2:
            cnt += 1

print(cnt)