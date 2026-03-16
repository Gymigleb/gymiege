with open("./files/17_9840.txt") as f:
    data = [int(i) for i in f]
    M39 = max(i for i in data if len(str(abs(i))) == 4 and str(i)[-2:] == "39")

M = 0
cnt = 0

for n1, n2 in zip(data, data[1:]):
    l = [len(str(abs(n1))), len(str(abs(n2)))]
    if l.count(4) == 1 and (n1 + n2)**2 <= M39**2:
        cnt += 1
        M = max(M, n1 + n2)

print(cnt, M)