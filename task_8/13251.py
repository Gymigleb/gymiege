from itertools import *

cnt = 0

for i in permutations("кайф"):
    i = "".join(i)
    if i[-1] != "й" and "кф" not in i: cnt += 1

print(cnt)