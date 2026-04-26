def f(n): return n == 2 or n >= 3\
         and all(n%d for d in range(3, int(n*0.5) + 1, 2))

L = 4_234_679
R = 10_157_812
for i in range(3, int(10_157_812**0.25) + 1):
    if L <= i**4 <= R and f(i):
        print(i**4, i**3)