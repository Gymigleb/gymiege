from itertools import *

g = "аб бд де еж жз за зе ав вб вг гд".split()
m = "345 35 128 156 124 478 68 367".split()

for i in permutations("абвгдежз"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(*i, sep="")
