def f(x):
    return (x%17 == 0) <= (not (80 <= x <= 100) or (a < x+30))

for a in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(a)