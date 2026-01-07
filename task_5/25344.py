def f(n):
    out = ""
    while n:
        out += str(n%3)
        n //= 3
    return out[::-1]

m = 1000000

for n in range(1, 1000000):
    nt = f(n)
    if n % 3 == 0:
        nt = nt + nt[-2:]
    else:
        nt += f(sum(map(int, nt))*3)
    r = int(nt, 3)

    if r > 208 and r % 2 != 0:
        m = min(m, r)

print(m)