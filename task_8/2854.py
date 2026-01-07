from itertools import *

def f(a):
    out = ""
    for i in a:
        if i in "оа": out += "о"
        else: out += "р"
    return out

cnt = 0

for s in set(permutations("росомаха")):
    t = f(s)
    if "оо" not in t and "рр" not in t:
        cnt += 1

print(cnt)