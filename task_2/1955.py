from itertools import *

def f(x, y, z, w):
    return not (y <= (x == w)) and (z <= x)

for i in product((0, 1), repeat=5):
    t = [
        (i[0], 1, 1, i[1]),
        (0, i[2], i[3], 0),
        (i[4], 0, 1, 0)
    ]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if [f(**dict(zip(j, _))) for _ in t] == [1, 1, 1]:
                print(*j)
                print(*j, sep="")