from itertools import *

def f(x, y, z, w):
    return (w <= (not (z <= x))) or y

for i in product((0, 1), repeat=7):
    t = [
        (1, i[0], i[1], i[2]),
        (0, 1, 0, i[3]),
        (i[4], 0, i[5], i[6])
    ]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if all(not f(**dict(zip(j, _))) for _ in t):
                print(*j, sep="")