with open("./files/17_9786.txt") as f:
    data = [int(i) for i in f]
    M25 = max(i for i in data if str(i)[-2:] == "25")

M = 0
cnt = 0

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    l = [len(str(abs(n1))), len(str(abs(n2))), len(str(abs(n3)))]
    if l.count(4) <= 2 and n1 + n2 + n3 <= M25:
        cnt += 1
        M = max(M, n1 + n2 + n3)

print(cnt, M)