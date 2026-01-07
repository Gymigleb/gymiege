from itertools import *

g = "DE EA AH HC CF FG GB BD BE HG".split()
m = "38 58 146 36 27 347 568 127".split()

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g): print(*i)