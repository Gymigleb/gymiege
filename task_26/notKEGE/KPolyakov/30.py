f = open("26-j5.txt")

n, *a = [int(s) for s in f]
b = a.copy()
s = 0

for i in  range(1, n-1):
    b[i] = sorted(a[i-1:i+2])[1]
    if b[i] < a[i]: s += a[i] - b[i] 

print(a[:10:])
print(b[:10:])
print(b.count(min(b)), s)