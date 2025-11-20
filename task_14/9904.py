from string import printable

for y in range(9, 14):
    for x in range(y + 1, 14):
        a = int(f"7{printable[x]}37{printable[y]}")

def f(n):
    q = 0
    out = 0
    n = n[::-1]
    for i in n:
        out += int(i)*150**q
        if q == 0: q = 1
        q *= 150
    return out
