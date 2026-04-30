from itertools import *

def f(x, y, z, w):
    return ((z <= x) <= (x == y)) or (not w)

for i in product([0, 1], repeat=5):
    t = [
        (i[0], 0, 1, 0),
        (0, i[1], i[2], 0),
        (i[3], 1, 1, i[4])
    ]
    if len(t) == len(set(t)):
        for j in permutations("xyzw"):
            if all(not f(**dict(zip(j, _))) for _ in t):
                print(*j, sep="")