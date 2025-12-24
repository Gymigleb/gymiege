f = open("26-39.txt")

n, M = [int(s) for s in f.readline().split()]
a = [int(s) for s in f]
a.sort()

ans = [e for e in a[::-1] if 310 <= e <= 320]
S = M - sum(ans)
print(S)

i = 0
while a[i] <= S:
    S -= a[i]
    ans.append(a[i])
    i += 1

print(S, i, a[i], ans)

S += ans.pop()

i = 0
while a[i] <= S:
    e = a[i]
    i += 1
ans.append(e)
print(e)

S -= e

print(len(ans), M - S)