def f(x):
    a = s <= x <= e
    b = 22 <= x <= 40
    c = 32 <= x <= 50
    return (not a) <= (b == c)

ans = []
l = [21, 23, 41, 33, 51]

for s in l:
    for e in l:
        if all(f(x) for x in l):
            ans.append(e-s)

print(min(ans))