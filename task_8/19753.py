from itertools import *

def f(a):
    out = ""
    for i in a:
        if i % 2 == 0: out += "0"
        else: out += "1"
    return out

cnt = 0

for s in permutations(range(0,10), r=6):
    b = map(str, s)
    b = "".join(b)
    if s[0] != 0:
        t = f(s)
        if int(b) % 4 == 0 and "00" not in t:
            cnt += 1


print(cnt)