from itertools import *

def f(x):
    p = 13 <= x <= 19
    q = 17 <= x <= 23
    a = s <= x <= e
    return (not ((not p) <= q)) <= (a <= ((not q) <= p))

l = [x + e for x in range(13, 24) for e in (0, 0.1, 0.9)]
ans = []

for s, e in combinations(l, 2):
    if all(f(x) for x in l):
        ans.append(e - s)
        print(s, e, e - s)

print(max(ans))