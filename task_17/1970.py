with open("./files/17_1970.txt") as f:
    data = [int(i) for i in f]

M = 0
cnt = 0

for n1, n2 in zip(data, data[1:]):
    if n1 % 3 == 0 or n2 % 3 == 0:
        cnt += 1
        M = max(n1 + n2, M)

print(cnt, M)