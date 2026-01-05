from itertools import *

def f(x, y, z ,w):
    return not(x <= y) or (z == w) or z

for i in product((0,1), repeat=7):
    t = [
        (0, 0, i[0], i[1]),
        (i[2], i[3], 1, i[4]),
        (i[5], 1, 0, i[6])
    ]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if [f(**dict(zip(j, _))) for _ in t] == [0, 0, 0]:
                print(*j, sep="")