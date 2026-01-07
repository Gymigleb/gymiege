from itertools import * 

g = "AC CD DB BF FE ED DG GA AD".split()
m = "37 57 147 37 26 57 12346".split()

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g): print(*i)