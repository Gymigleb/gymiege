def f(n):
    out = []
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            if str(d)[-2:] == "11" and d != 11: out.append(d)
            if str(n//d)[-2:] == "11" and n//d != 11: out.append(n//d)
    return min(out) if out else 0

cnt = 0

for i in range(1_350_051, 10**100):
    a = f(i)
    if  a != 0:
        print(i, a)
        cnt += 1
        if cnt >= 5: break