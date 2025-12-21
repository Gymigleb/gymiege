from itertools import *

g = "AD DE EG GC CF FA AB BF BE".split()
m = "37 367 125 56 34 247 126".split()

print(*range(1,8))
for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g): print(*i)