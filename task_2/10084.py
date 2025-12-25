from itertools import *

def f(x, y, z, w):
    return (x and not y) or (y == z) or not w

for i in product((0, 1), repeat=4):
    t = [
        (i[0], i[1], 0, 0),
        (1, 0, i[2], 0),
        (1, 0, 1, i[3])
    ]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if [f(**dict(zip(j, _))) for _ in t] == [0, 0, 0]:
                print(*j)
                print(*j, sep="")