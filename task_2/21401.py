from itertools import *

def f(x, y, z ,w):
    return x and (z <= w) and not y


for i in product((0, 1), repeat=7):
    t = [
        (i[0], i[1], 1, i[2]),
        (i[3], 1, 0, i[4]),
        (1, 0, i[5], i[6])
]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if [f(**dict(zip(j, _))) for _ in t] == [1, 1, 1]:
                print(*j, sep="")
