def f(n):
    out = ""
    while n:
        out += str(n%3)
        n //= 3
    return out[::-1]

m = 100000000

for n in range(1, 1000000):
    nt = f(n)
    if sum(map(int, nt)) % 3 == 0:
        nt += "212"
    else:
        nt += f(sum(map(int, nt)) * 2)

    r = int(nt, 3)
    if r > 490:
        m = min(r, m)
print(m)