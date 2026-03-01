from itertools import *

def f(x, y, z, w):
    return y <= (((not w) <= (not z)) <= x)

for i in product((0, 1), repeat=7):
    t = [
        (i[0], i[1], 0 , i[2]),
        (i[3], i[4], i[5], 1),
        (0, i[6], 1, 0)
    ]
    for j in permutations("xyzw"):
        if all(not f(**dict(zip(j, _))) for _ in t):
            print(*j, sep="")