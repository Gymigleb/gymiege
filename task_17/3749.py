with open("./files/17_3749.txt") as f:
    data = [int(i) for i in f]

sqrt_M = max(i for i in data if int(i ** 0.5) == i ** 0.5) * 3

cnt = 0
ans = []

for n1, n2 in zip(data, data[1:]):
    u1 = (n1 * n2) ** 0.5 == int((n1 * n2) ** 0.5)
    u2 = n1 <= sqrt_M or n2 <= sqrt_M 
    if u1 and n2:
        cnt += 1
        ans.append((n1 * n2) ** 0.5)

print(cnt, min(ans) + max(ans))