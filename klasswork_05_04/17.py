with open("./17.txt") as f:
    data = [int(i) for i in f]
    M2 = max([i for i in data\
    if len(str(i).replace("-", "")) == 2])

M = 0
cnt = 0

for n1, n2 in zip(data, data[1:]):
    u1 = len(str(n1).replace("-", "")) == 2
    u2 = len(str(n2).replace("-", "")) == 2
    # if u1 != u2: print(n1, n2, (n1 + n2) % M2 == 0)
    if u1 != u2 and (n1 + n2) % M2 == 0:
        cnt += 1
        M = max(M, n1 + n2)

print(cnt, M)