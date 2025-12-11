from itertools import *

cnt = 0

for s in set(permutations("ворота", r=6)):
    s = "".join(s)
    if "оо" not in s and "оа" not in s and "ао" not in s:
        cnt += 1

print(cnt)