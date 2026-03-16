with open("./files/17_17636.txt") as f:
    data = [int(i) for i in f]
    M3 = max(i for i in data if len(str(abs(i))) == 3 and str(i)[-1] == "3")

M = 0
cnt = 0

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    q1 = [len(str(abs(n1))) == 3 and str(n1)[-1] == "3",\
         len(str(abs(n2))) == 3 and str(n2)[-1] == "3",\
         len(str(abs(n3))) == 3 and str(n3)[-1] == "3"]
    if any(q1) and n1 + n2 + n3 < M3:
        cnt += 1
        M = max(M, n1 + n2 + n3)

print(cnt, M)