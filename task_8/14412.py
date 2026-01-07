from itertools import *

alph = "алгоритм"

cnt = 0

for s in product(alph, repeat=6):
    if s.count("л") <= 1 and s[0] != "р" and not s[-1] in "лгртм":
        cnt += 1

print(cnt)