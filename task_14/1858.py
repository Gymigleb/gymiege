def f(n):
    out = ""
    while n:
        out += str(n%5)
        n //= 5
    return out[::-1]

a = 4*625**9 - 25**15 + 2*5**11 - 7
b = f(a)
print(b.count("4"))