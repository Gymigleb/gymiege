def f(a):
    out = ""
    while a:
        out += str(a%8)
        a //= 8
    return out[::-1]

ans = []

for n in range(1, 100000):
    r = f(n)
    if r[0] == "5":
        r = r.replace("2", "*")
        r = r.replace("5", "2")
        r = r.replace("*", "5")
        r = "11" + r
    else:
        r = "2" + r[1:] + "10"
    
    r = int(r, 8)
    if r < 1354:
        ans.append([r, n])
print(max(ans))