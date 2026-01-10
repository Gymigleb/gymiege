from itertools import *

l = [x + e for x in range(23, 57) for e in (0, 0.1, 0.9)]

def f(x):
    p = 23 <= x < 45
    q = 34 <= x <= 56
    a = s <= x <= e
    return (not a) or (not p) and q

ans = []

for s, e in combinations(l, 2):
    if all(f(x) for x in l):
        ans.append(e - s)
        
print(max(ans))