from itertools import *

def f(x, y, z, w):
    return ((x or y) <= z) or (y == w) or z

for i in product((0, 1), repeat=4):
    t = [
        (0, 1, i[0], i[1]),
        (1, i[2], 1, 0),
        (i[3], 1, 1, 0)
    ]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if [f(**dict(zip(j, _))) for _ in t] == [0, 0, 0]:
                print(*j)
                print(*j, sep="")