f = open("26-50.txt")

n = int(f.readline())

a = []

for i in range(n):
    a.append(int(f.readline()))

# print(a[:100])

a.sort()

# print(a[:100])

pol = a[len(a)//2-1]
chet = a[len(a)//4*3]

print(len(a)//2-1, pol)
print(len(a)//4*3-1, chet)

cnt = 0
m = 100000000

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if (a[i] + a[j]) % 2 == 0:
            s = (a[i] + a[j]) // 2
            if s > pol and s < chet:
                cnt += 1
                m = min(m, s)

print(cnt, m)