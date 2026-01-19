def f(x):
    return ((x%10 != 5) and (x%10 == 4)) <= (x > a-11)

for a in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(a)