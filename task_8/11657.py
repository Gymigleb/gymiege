from itertools import *

cnt = 0

for i in product(range(8), repeat=6):
    if i[0] != 0:
        if len(i) == len(set(i)) and i.count(3) == 0:
            i = map(str, i)
            i = "".join(i)
            for j in range(0, 8, 2):
                i = i.replace(str(j), "*")
            if "**" in i: cnt += 1

print(cnt)