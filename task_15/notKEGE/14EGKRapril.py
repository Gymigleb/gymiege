def f(x, y):
    return (x * y < A) or (5 * x < y) or (486 <= x)

for A in range(1180494 - 200000, 1180494 + 2000):
    if all(f(x, y) for x in range(481, 486) for y in range(2400, 2450)):
        print(A)
        break