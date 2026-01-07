def f(n):
    out = ""
    while n:
        out += str(n%3)
        n //= 3
    return out[::-1]

m = 1000000

for n in range(11,1000):
    nt =  f(n)
    if nt.count("0") + nt.count("2") > nt.count("1"):
        nt = "22" + nt
    else:
        nt = "11" + nt
    r = int(nt, 3)
    if r > 100:
        m = min(m, r)
        print(n, r)
print(m)