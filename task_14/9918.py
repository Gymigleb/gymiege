def f(a, sys):
    a = a[::-1]
    out = 0
    for i in range(len(a)):
        out += a[i] * sys ** i
    return out

s = set()

for x in range(10,67):
    for y in range(x):
        a = f([7, 3, x, 1, y], 67)
        b = f([4, 9, y], x)
        s.add(a + b)

print(len(s))