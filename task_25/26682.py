def f(n):
    out = []
    for d in range(2, 3):
        while n % d == 0:
            out += [d]
            n //= d
            if len(out) > 9: return out
    d = 3
    while d * d < n + 1:
        while n % d == 0:
            out += [d]
            n //= d
            if len(out) > 9: return out
        d += 2
    return out + [n] if n > 1 else out

def alldel(n):
    out = []
    for d in range(1,  int(n**0.5) + 1):
        if n % d == 0:
            out += [d, n // d]
    return set(out)

cnt = 0

for i in range(5_200_001, 10**100):
    d = f(i)
    if len(d) == 9:
        if len(alldel(i)) % 90 == 0:
            print(i, max(d))
            cnt += 1
            if cnt >= 5: break