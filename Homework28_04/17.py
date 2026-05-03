with open("./files/1_17.txt") as f:
    data = [int(i) for i in f]

m123 = min(i for i in data if i > 0 and i % 123 == 0)
cnt = 0
Ms = 0

for a, b in zip(data, data[1:]):
    s = a + b
    if s < m123:
        Ms = max(Ms, s)
        cnt += 1

print(cnt, abs(Ms))