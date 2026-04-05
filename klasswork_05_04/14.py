def f(n):
    out = ""
    while n:
        out += str(n%39)
        n //= 39
    return out[::-1] if len(out) != 0 else "0"

M = 0

for x in range(1,9431):
    a = 39**483 + 39**235 - x
    b = f(a)
    M = max(M, b.count("0"))

print(M)