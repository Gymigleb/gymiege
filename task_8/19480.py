from itertools import *

alph = "парижанка"
cnt = 0

for s in set(permutations(alph)):
    s = "".join(s)
    if s.count("аа") + s.count("ааа") + s.count("иа") + s.count("аи") == 1: cnt += 1

print(cnt)