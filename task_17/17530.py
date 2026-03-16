with open("./files/17_17530.txt") as f:
    data = [int(i) for i in f]
    m = min(data)

M = 10**100
cnt = 0

for n1, n2 in zip(data, data[1:]):
    if n1%55 == m or n2%55 == m:
        cnt += 1
        M = min(M, n1 + n2)

print(cnt, M)