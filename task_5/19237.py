def f(n):
    out = ""
    while n:
        out += str(n%3)
        n //= 3
    return out[::-1]

m = 1000000

for n in range(1,10000):
    nt = f(n)
    if n % 3 == 0:
        nt = nt + nt[-2:]
    else:
        nt = nt + f(sum(map(int, nt)))
    
    r = int(nt,3)
    if r > 220 and r % 2 == 0:
        m = min(r, m)
        print(n, r)

print(m)