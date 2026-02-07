def f(n):
    out = []
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            out.append(n//d)
            out.append(d)
    return out

def is_prime(n):
    if n < 2: return False
    for d in range(2, 3):
        if n % d == 0: return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0: return False
    return True

cnt = 0

for i in range(1273548, 10**100):
    d = f(i)
    m = sum(d)
    if is_prime(m % 100000):
        print(i, m)
        cnt += 1

    if cnt >= 5: break