from itertools import *

g = "CE EG GF FA AC CD DH HE FB AB".split()
m = "68 47 45 237 368 15 248 157".split()

print(*range(1,9))
for i in permutations("ABCDEFHG"):
    if all(str(i.index(x)+1) in m[i.index(y)] for x, y in g): print(*i)