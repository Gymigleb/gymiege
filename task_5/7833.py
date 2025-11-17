def f(n):
    out = ""
    while n:
        out += str(n%3)
        n //= 3
    return out[::-1]

mn = 10000
m = 10000
for n in range(10,100000):
    nt = f(n)
    if n % 2 == 0:
        nt += nt[-2:]
    else:
        nt += f(sum(map(int, nt)))
    
    r = int(nt, 3)
    if r <= m:
        print(n, r)
        if m > r:
            mn = n
            m = r

print(mn, m)