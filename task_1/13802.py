from itertools import *

g = "ae eh hg gc cf fa fd de db bh bg".split()
m = "367 568 18 58 247 127 156 234".split()

print("1 2 3 4 5 6 7 8")
for i in permutations("abcdefhg"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(*i)