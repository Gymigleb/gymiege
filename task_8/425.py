from itertools import *

cnt = 0

for s in permutations("запись"):
    s = "".join(s)
    if s[0] != "ь" and \
            "аь" not in s and \
            "иь" not in s:
        cnt += 1


print(cnt)