from itertools import *

alph = sorted("сортировка")
cnt = 0

def f(s):
    for i in "сртвк": s = s.replace(i, "0")
    for i in "иоа": s = s.replace(i, "1")
    return not("111" in s or "000" in s)

for s in set(permutations(alph)):
    s = "".join(s)
    if f(s): cnt += 1

print(cnt)