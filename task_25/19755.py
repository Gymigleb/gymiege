def f(n):
    out = []
    a = n
    for d in range(2, int(n**0.5) + 1):
        while a%d == 0:
            out.append(d)
            a //= d
    if a != 1 and a != n: out.append(a)
    return out


def M(d):
    return min(d) + max(d)

cnt = 0

for i in range(1200001, 100000000):
    d = f(i)
    m = M(d) if len(d) != 0 else 0
    if m > 2000 and m%10 == 8:
        print(i, m)
        cnt += 1
        if cnt > 5: break