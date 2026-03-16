with open("./files/17_9748.txt") as f:
    data = [int(i) for i in f]
    M15 = max(i for i in data if str(i)[-2:] == "15")
M = 0
cnt = 0
for n1, n2, n3 in zip(data, data[1:], data[2:]):
    l = [len(str(n1)), len(str(n2)), len(str(n3))]
    if l.count(4) == 1 and n1 + n2 + n3 >= M15:
        cnt += 1
        M = max(M, n1 + n2 + n3)
print(cnt, M)