from itertools import *

def f(x, y, z, w):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))

for i in product((0, 1), repeat=5):
    t = [
        (1, 1, 1, 0),
        (i[0], i[1], 0, 0),
        (i[2], 0, i[3], i[4])
    ]

    for j in permutations("xyzw"):
        if [f(**dict(zip(j, _))) for _ in t] == [1, 0, 0]:
            print(*j, sep="")