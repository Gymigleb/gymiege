from itertools import *

alph = ["cookie", "candy", "bar", "nothing"]

def t(s):
    if s.count("candy") > s.count("cookie") > s.count("bar"): return True
    return False

cnt = 0

for s in set(map(lambda x: tuple(sorted(list(x))), product(alph, repeat=15))):
    if t(s): cnt += 1
    if cnt % 10 == 0: print(cnt)

print(cnt)