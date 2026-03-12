with open("./files/17_4597.txt") as f:
    data = [int(i) for i in f]

m = min(data)
M = 0
cnt = 0
for i in range(len(data)-1):
    num1, num2 = data[i:i+2]
    if num1 % 117 == m or num2 % 117 == m:
        cnt += 1
        M = max(num1 + num2, M)
print(cnt, M)

minn = min(data)

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i: i + 2]
    u1 = num1 % 117 == minn
    u2 = num2 % 117 == minn
    if u1 + u2 >= 1:
        ans.append(num1 + num2)

print(len(ans), max(ans))

with open(r'.\files\17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 117 == minn
    u2 = num2 % 117 == minn
    if u1 + u2 >= 1:
        ans.append(num1 + num2)

print(len(ans), max(ans))


