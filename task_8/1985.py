from itertools import *

cnt = 0
a1 = "аиоу"
a2 = "бклн"

for i in permutations("абиклоун"):
    i = "".join(i)
    for j in a1: i = i.replace(j, "1")
    for j in a2: i = i.replace(j, "2")
    if "11" not in i and "22" not in i:
        cnt += 1
print(cnt)