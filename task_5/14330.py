def f(s):
    M = 0
    m = 1000000000000
    for i in s:
        M = max(M, int(i))
        m = min(m, int(i))
    return (M + m) ** 2

def d(s):
    out = 1
    for i in s:
        if int(i) % 2 == 0:
            out *= int(i)
    return out



for n in range(10000, 100000):
    ns = str(n)
    a = f(ns)
    b = d(ns)
    if str(max(a,b)) + str(min(a,b)) == "12116":
        print(n)
        break

