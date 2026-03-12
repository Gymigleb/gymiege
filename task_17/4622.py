with open("./files/17_4622.txt") as f:
    data = [int(i) for i in f]
M = 0
cnt = 0
for i in range(len(data)-1):
    num1, num2 = data[i:i+2]
    m = min([i for i in data if i > 0 and i % 19 == 0])
    if num1 + num2 < m:
        cnt += 1
        M = max(M, num1 + num2)
print(cnt, M)