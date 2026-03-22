def d(x,y): return abs(x) % abs(y) == 0

def f(x):
    return d(a, 25) and ((d(x, 24) and d(x,75)) <= d(x, a))

cnt = 0

for a in range(-100000, 100000):
    if a != 0 and all(f(x) for x in range(-10000, 10000)):
        cnt += 1
        print(a)

print("cnt", cnt)