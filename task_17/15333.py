with open("./files/17_15333.txt") as f:
    data = [int(i) for i in f]
    M19 = max(i for i in data if i % 19 == 0)

cnt = 0
M = 0

for n1, n2 in zip(data, data[1:]):
    if n1 > M19 or n2 > M19:
        cnt += 1
        M = max(M, n1 + n2)

print(cnt, M)