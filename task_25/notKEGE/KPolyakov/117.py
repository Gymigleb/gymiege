def f(n):
    out = []
    d = 2
    while n % d == 0:
        out.append(d)
        n //= d
        if len(out) >= 4: return out

    d = 3
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
            if len(out) >= 4: return out
        d += 2
    if n > 1: out.append(n)
    return out

cnt = 0
M = 0

for i in range(105_673, 220_784 + 1):
    out = f(i)
    if len(set(out)) == 3: 
        cnt += 1
        M = max(M, i)
        # print(i)

print(cnt, M)