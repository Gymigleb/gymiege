def f(n):
    out = []
    for d in range(2, 3):
        while n % d == 0:
            out.append(d)
            n //= d
    for d in range(3, round(n**0.5) + 1, 2):
        while n % d == 0:
            out.append(d)
            n //= d
    if n != 1: out.append(n)
    return 0 if len(out) == 1 else sum(set(out))

cnt = 0

for i in range(250_000, 10**100):
    s = f(i)
    if s % 17 == 0 and s != 0:
        cnt += 1
        print(i, s)
        if cnt == 5: break