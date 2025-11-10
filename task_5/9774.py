def f(a):
    out = ""
    while a:
        out += str(a%3)
        a //= 3
    return out[::-1]

m = 1000000000
for n in range(1, 1000):
    nt = f(n)
    if n % 3 == 0:
        nt += nt[-2:]
    else:
        nt += f(n%3*5)
    r = int(nt, 3)
    if r>133:
        print(n, r)
        m = min(m,r)
print(m)