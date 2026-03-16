def f(n):
    out = ""
    while n >= 1:
        out += str(n%3)
        n//=3
    return out[::-1]    

ans = []

for n in range(1, 100000):
    r = f(n)
    if n % 3 != 0: r = "1" + r + r[-3:]
    else: r += str(f(sum(map(int, list(r)))*8))
    r = int(r, 3)
    ans.append((abs(1220-r), r, n))
print(sorted(ans, reverse=True))