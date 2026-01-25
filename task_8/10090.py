from string import printable
from itertools import *

cnt = 0

for i in product(printable[:8], repeat=5):
    i = "".join(i)
    if i[0] != "0" and "1" not in i:
        if len(i) == len(set(i)):
            for j in printable[:8:2]: i = i.replace(j, "*")
            for j in printable[1:8:2]: i = i.replace(j, "+")
            if "++" not in i and "**" not in i: cnt += 1

print(cnt)