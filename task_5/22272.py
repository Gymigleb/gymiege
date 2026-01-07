def f(n):
    out = ""
    while n:
        out += str(n%9)
        n //= 9
    return out[::-1]

M = 0
N = 0
for n in range(1, 1000000):
    nr = f(n)
    if nr[0] == "7":
        nr = nr.replace("6", "a")
        nr = nr.replace("3", "6")
        nr = nr.replace("a", "3")
        nr = "34" + nr
    else:
        nr = "3" + nr[1:] + "45"
    r = int(nr, 9)
    if r < 2876 and r >= M:
        print(n, r)
        N = max(N,n)
        M = r

print(N)