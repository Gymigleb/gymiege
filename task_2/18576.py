from itertools import *

print("x y z w")
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = not(w <= (x == (y or y))) and (z <= x)
                if f:
                    print(x, y, z, w)

def f(x, y, z, w): return not(w <= (x == (y or y))) and (z <= x)

for i in product((0, 1), repeat=5):
    t = [
        (i[0], 1, 1, i[1]),
        (0, i[2], i[3], 0),
        (i[4], 0, 1, 0)
    ]
    if len(set(t)) == len(t):
        for j in permutations("xyzw"):
            if all(f(**dict(zip(j, p))) for p in t):
                print(*j)