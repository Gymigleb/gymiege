def f(x):
    p = 43 <= x <= 49
    q = 44 <= x <= 53
    a = s <= x <= e
    return not(a) or p or q

ans = []

for s in range(0, 54):
    for e in range(s, 54):
        if all(f(x) for x in range(-100, 100)):
            ans.append(e-s)

print(max(ans))