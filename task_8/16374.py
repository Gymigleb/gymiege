from itertools import * 

cnt = 0

for i in product(range(7), repeat=7):
    if i[0] != 0 and sum(1 for j in i if j % 2 == 0) == 2: cnt += 1

print(cnt)