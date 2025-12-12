from itertools import *

alph = "кидала"

cnt = 0

for s in set(permutations(alph, r=5)):
    s = "".join(s)
    if "аа" not in s: cnt += 1

print(cnt)