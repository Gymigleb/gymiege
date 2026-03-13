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
    out.sort()
    if n != 1: out.append(n)
    return 0 if len(out) == 1 else out[0] + out[-1]

cnt = 0
for i in range(23_600_001, 10**100):
    m = f(i)
    if m % 213 == 171:
        cnt+=1
        print(i, m)
        if cnt == 6: break