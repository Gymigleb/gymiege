def f(x):
    return x%a==0 or x%133!=0 or x%95!=0

ans = []

for a in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        ans.append(a)

print(max(ans))