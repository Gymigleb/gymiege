with open("./files/17_25356.txt") as f:
    data = [int(i) for i in f]

M = max(i for i in data if str(i)[-2:] == "30")
cnt = 0
m = 0
for n1, n2, n3 in zip(data, data[1:], data[2:]):
    if len(str(abs(n1))) != 4 and\
        len(str(abs(n2))) != 4 and\
        len(str(abs(n3))) != 4 and\
        n1 + n2 + n3 > M:
        cnt += 1
        m = max(m, n1 + n2 + n3)
 
print(cnt, m)