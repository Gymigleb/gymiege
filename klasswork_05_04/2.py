from itertools import *

def f(x, y, z, w):
    return ((z == x) <= w) and (w <= (y and x))

for i in product([0, 1], repeat=3):
    t = [
        (1, 1, i[0], 0),
        (1, i[1], i[2], 0),
        (1, 0, 1, 1)
    ]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if all(f(**dict(zip(j,_))) for _ in t):
                print(*j)