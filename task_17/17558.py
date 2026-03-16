with open("./files/17_17558.txt") as f:
    data = [int(i) for i in f]
    n32 = len([i for i in data if i% 32 == 0])

M = 0
cnt = 0

for n1, n2 in zip(data, data[1:]):
    if (n1 < 0 or n2 < 0) and  n1 + n2 < n32:
        cnt += 1
        M = max(M, n1 + n2)

print(cnt, M)