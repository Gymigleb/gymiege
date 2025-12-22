from itertools import *

g = "AE EH HG GC CF FA ED DB BH BG DF".split()
m = "23 168 158 578 347 27 456 234".split()

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g): print(*i)