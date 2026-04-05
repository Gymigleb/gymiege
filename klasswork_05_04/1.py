from itertools import *

g = "ef fa ab bg ge ef ec cb cd df da".split()
m = "457 567 45 136 123 247 126".split()

for i in permutations("abcdefg"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(*i)