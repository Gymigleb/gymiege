def f (n):
    out = ""
    while n:
        out += str(n % 9)
        n //= 9
    return out[::-1]

for x in range(1, 3001):
    a = 9**150 + 9**30 - x
    at = f(a)
    if at.count("0") == 122:
        print(x)
        break