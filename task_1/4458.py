from itertools import *

m = "45 345 256 117 123 37 46".split()
g = "fb bd de ea ag gf gc cb cd".split()

print(*[i for i in range(1, 8)])
for i in permutations("abcdefg"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g): print(*i)
#15236741
print(21+30+13+2+39+8+5)