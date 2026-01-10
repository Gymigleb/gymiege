from itertools import *

l = [x + e for x in range(15, 168) for e in (0, 0.1, 0.9)]

def f(x):
    p = 15 <= x <= 142
    q = 38 <= x <= 167
    a = s <= x <= e
    return not ( q <=( ( (not a) and p) <= (not q)))

ans = []

for s, e in combinations(l, 2):
    if all(not f(x) for x in l):
        ans.append(e - s)
        
print(min(ans))