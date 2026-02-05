def f(n):
    d = {1}
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return d

def a(d):
    return sum(d) // len(d)

cnt = 0

for i in range(770000)[::-1]:
    d = f(i)
    A = a(d)
    if A%100 == 12:
        print(i, A)
        cnt += 1
        if cnt >= 5: break