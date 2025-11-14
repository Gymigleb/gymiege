def f(n):
    out = ""
    while n:
        out += str(n%3)
        n //= 3
    return out[::-1]


for n in range(1,10000):
    nt = f(n)
    s = sum(map(int, nt))
    if s % 2 == 0:
        nt = "12" + nt[2:] + "0"
    else:
        nt = "10" + nt[2:] + "2"
    
    r = int(nt, 3)
    if r > 105:
        print(n, r)
        break