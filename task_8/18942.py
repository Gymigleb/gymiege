from itertools import *

alph = "дионсй"

def dn(s):
    if s.count("д") >= 1 and s.count("н") == 0: return True
    if s.count("д") == 0 and s.count("н") >= 1: return True
    return False

def rep(s):
    for i in alph:
        if i+i in s: return False
    return True

cnt = 0

for s in product(alph, repeat=6):
    s = "".join(s)
    if rep(s) and dn(s): cnt += 1

print(cnt)