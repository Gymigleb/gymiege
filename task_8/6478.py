from itertools import *

alph = "моль"

cnt = 0

for s in product(alph, repeat=5):
    s = "".join(s)
    if "оь" not in s and s[0] != "ь" and "ьь" not in s:
        cnt += 1

print(cnt)