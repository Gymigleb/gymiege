def f(n):
    out = []
    for d in range(2, 3):
        while n % d == 0:
            out.append(d)
            n //= d
    if len(out) > 5: return out 

    for d in range(3, int(n**0.5) + 1):
        while n % d == 0:
            out.append(d)
            n //= d
            if len(out) > 5:
                if n > 1: return out + [n]
                return out
    if n > 1: return out + [n]
    return out

cnt = 0

for i in range(13_475_125, 10**100):
# for i in range(1):
    # i = 13476875 
    d = f(i)
    if len(d) == 5:
        flag = True
        for j in d:
            if str(j).count("5") == 0: flag = False
        if flag and d[0]*d[1]*d[2]*d[3]*d[4] == i:
            print(i, max(d))
            cnt += 1
            if cnt > 5: break