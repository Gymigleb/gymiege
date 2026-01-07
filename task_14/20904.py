def f (n):
    out = ""
    while n:
        out += str(n % 3)
        n //= 3
    return out[::-1]

for x in range(1, 2031):
    a = 3**100 - x
    at = f(a)
    if at.count("0") == 1:
        print(x)