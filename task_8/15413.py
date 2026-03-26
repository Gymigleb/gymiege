from  string import printable
from itertools import *

cnt = 0

for i in product(printable[:9], repeat=4):
    i = "".join(i)
    if i[0] != "0" and i.count("8") == 1:
        i = i.split("8")
        if sum(map(int, i[0])) == sum(map(int, i[1])):
            cnt += 1

print(cnt)