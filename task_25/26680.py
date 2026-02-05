def fact(n):
    out = []
    while n % 2 == 0:
        out.append(2)
        n //= 2
    for d in range(3, int(n**0.5) + 1, 2):
        while n % d == 0:
            out.append(d)
            n //= d
    if n > 2: out.append(n)
    return out

print(fact(1))