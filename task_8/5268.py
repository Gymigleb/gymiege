from itertools import *

alph = "амфибрахий"
cnt = 0

for i in set(permutations(alph)):
    i = "".join(i)
    if "иифаа" in i or "аафии" in i: cnt += 1

print(cnt)