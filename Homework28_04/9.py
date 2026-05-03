from itertools import *

data = []
with open("./files/9.txt") as f:
    for i in f:
        data.append(list(map(int, i.split())))

cnt = 0

for i in data:
    i.sort()
    if sum(i[:-1]) > i[-1]:
        if not any(a + b == c + d for a, b, c, d in permutations(i)):
            cnt += 1

print(cnt)