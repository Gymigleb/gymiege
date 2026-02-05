def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True

def fact(n):
    out = []
    i = 3
    while i < int(n**0.5) + 1:
        while n % i == 0:
            out.append(i)
            n //= i
        i+=2
    if n > 2: out.append(n)
    return out

cnt = 0

for n in range(5000001, 10**20, 2):
    d = fact(n)
    if len(d) == 2 and len(d) == len(set(d)):
        if is_prime(abs(d[0] - d[1])):
            print(n, max(d))

    if cnt >= 5: break