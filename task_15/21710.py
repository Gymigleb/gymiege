from itertools import *

#l = [x + y for x in range(36, 101) for y in (0, 0.1, 0.9)]

def f(x):
    a = s <= x <= e
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    return (not a) <= (b == c)

la = [36, 60, 75, 110]
lx = [37, 61, 76]

ans = []

for s, e in combinations(la, 2):
    if all(f(x) for x in lx):
        ans.append(e - s)

print(min(ans))