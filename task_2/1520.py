from itertools import *

def f(a, b, c):
    return (a <= b) and ((a and b) <= (not c))


t = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]
for j in permutations("abc"):
    if [f(**dict(zip(j, _))) for _ in t] == [1, 0, 1, 1, 1, 0, 1, 0]:
        print(*j)
        print(*j, sep="")