def f(n):
    out = []
    for d in range(2, 3):
        while n % d == 0:
            out += [d]
            n //= d
    for d in range(3, int(n**0.5) + 1, 2):
        while n % d == 0:
            out += [d]
            n //= d
    return out + [n] if n > 1 else out

cnt = 0

for i in range(5000001, 10**100):
    if i % 100 == 12:
        d = f(i)
        s = set(sorted(d))
        for j in s:
            if d.count(j) == 5:
                print(i, j)
                cnt += 1
                if cnt >= 5: exit(0)
                break