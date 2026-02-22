from itertools import *

g = "гб бж же ев вд дг бк кг ка ад ае".split()
m = "248 137 268 15 467 357 256 13".split()

for i in permutations("абвгдежк"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(*i)