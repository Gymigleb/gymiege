from  itertools import *

with open("./files/19702.txt") as f:
    data = [list(map(int, i.split())) for i in f]

cnt = 0

for i in data:
    for j in combinations(i, 4):
        j = sorted(j)
        if j[0] - j[1] == j[1] - j[2] == j[2] - j[3]:
            cnt += 1
            break


print(cnt)