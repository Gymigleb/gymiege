from itertools import *

def f(x):
    c = 47 <= x <= 115
    b = 24 <= x <= 90
    a = s <= x <= e
    return c <= ((not a and b) <= (not c))

lx = [25, 48, 91, 116]
la = [24, 47, 90, 115]

ans = []

for s, e in product(la, repeat=2):
    if all(f(x) for x in lx):
        ans += [e-s]

print(min(ans))