with open("./files/17_12249.txt") as f:
    data = [int(i) for i in f]

M = max(i for i in data if len(str(i)) == 5 and abs(i) % 10 == 3)
cnt = 0
m = 0
for n1, n2, n3 in zip(data, data[1:], data[2:]):
    if n1 + n2 + n3 <= M and (abs(n1)%10 == 3 or abs(n2)%10 == 3 or abs(n3)%10 == 3):
        cnt += 1
        m = max(n1 + n2 + n3, m)

print(cnt, m)