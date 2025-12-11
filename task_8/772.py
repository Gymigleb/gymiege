from itertools import *

cnt = 0

for s in permutations("пробник"):
    s = "".join(s)
    if s[0] in "прбнк" and s[-1] in "прбнк" \
        and "ои" not in s and "ио" not in s:
        cnt += 1


print(cnt)