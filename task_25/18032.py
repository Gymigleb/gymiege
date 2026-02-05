def dev(n):
    out = set()
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            out.add(d)
            out.add(n // d)
    return out

for i in range(1000, 10000):
    s = sum(dev(i))
    if s % 100 == 23:
        print(i, s)