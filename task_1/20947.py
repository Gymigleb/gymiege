from itertools import *

g = "аб бг ги ие ед дв ва бв гж жи дж".split()
m = "267 157 468 356 248 134 12 35".split()

for i in permutations("абвгдежи"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(*i)