with open("17628.txt") as f:
    data = [list(map(int, i.split())) for i in f]

cnt = 0

for i in data:
    i.sort()
    if i[0] + i[3] <= i[1] + i[2]:
        cnt += 1

print(cnt)