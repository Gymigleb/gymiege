a = 729**8 - 3**18 + 85

def f(n):
    out = ""
    while n:
        out += str(n%9)
        n //= 9
    return out[::-1]

print(f(a).count("0"))