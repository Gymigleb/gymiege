def f(n):
    out = ""
    while n:
        out += str(n%3)
        n //= 3
    return out[::-1]

for n in range(1, 10000):
    r = f(n)
    if n % 3 == 0: r = "1" + r + "02"
    else: r += f(n%3*4)
    r = int(r, 3)
    if r<100: print(n)