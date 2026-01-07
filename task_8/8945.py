from itertools import *

def f(a):
    out = ""
    for i in a:
        if i % 3 == 0: out += "0"
        else: out += "1"
    return out

cnt = 0

for s in product(range(0, 12), repeat=7):
    if s[0] != 0:
        t = f(s)
        if "11" not in t and "00" not in t:
            cnt += 1
    if cnt != 0 and cnt % 10000 == 0: print(cnt)

print(cnt)