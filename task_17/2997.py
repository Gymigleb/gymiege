with open("./files/17_2997.txt") as f:
    data = [int(i) for i in f]

data_3 = [str(abs(i))[1] for i in data if len(str(abs(i))) == 3]
most_com = max((data_3.count(i), i) for i in set(data_3))[1]

cnt = 0
M = 0

for n1, n2 in zip(data, data[1:]):
    u1 = str(n1)[-1] == str(most_com) or str(n2)[-1] == str(most_com)
    if u1:
        cnt += 1
        M = max(M, n1 + n2)

print(cnt, M)