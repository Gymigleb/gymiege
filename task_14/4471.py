def f(n):
    out = ""
    while n:
        out += str(n%9)
        n //= 9
    return out[::-1]

a = 7*729**543 - 6*81**756 - 5*9**987 - 20
b = f(a)
print(b.count("8"))

count = 0
while a:
    if a % 9 == 8: count += 1
    a //= 9
print(count)