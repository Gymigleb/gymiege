from itertools import *

cnt = 0

for s in permutations("левиоса"):
    s = "".join(s)
    if s[0] not in "еиоа":
        if s[3] not in "лвс":
            cnt += 1


print(cnt)