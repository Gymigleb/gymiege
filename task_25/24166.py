def f(n):
    out = []
    for d in range(2, 3):
        while n % d == 0:
            out += [d]
            n //= d
            if len(out) > 4: return out + [n] if n > 1 else out
    for d in range(3, int(n**0.5) + 1, 2):
        while n % d == 0:
            out += [d]
            n //= d
            if len(out) > 4: return out + [n] if n > 1 else out
    return out + [n] if n > 1 else out

def pal(s):
    s = str(s)
    return True if s == s[::-1] else False

cnt = 0

for i in range(7_305_678, 10**100):
    d = f(i)
    if len(d) == 4:
        s = sum(d)
        if pal(s): 
            print(i, s)
            cnt += 1
            if cnt >= 5: break
