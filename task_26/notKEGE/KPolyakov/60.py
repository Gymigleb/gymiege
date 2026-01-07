f = open("26-60.txt")

k, n = map(int, f.readline().split())

s = []
a = []

for i in range(k):
    s.append(int(f.readline()))

last = s.copy()
for i in range(k): last[i] = 0
conk = last.copy()

for i in range(n):
    a.append(list(map(int, f.readline().split())))

a.sort(key=lambda x: x[0], reverse=True)

cnt = 0
s1 = s.copy() 

for i in range(n):
    mark, spec = a[i][0], a[i][1]
    conk[spec] += 1
    if s1[spec] != 0:
        cnt += 1
        s1[spec] -= 1
        last[spec] = mark

for i in range(k):
    conk[i] = conk[i] / s[i]

Mi = conk.index(max(conk))

print(cnt, last[Mi])