def f(n): return n>2 and all(n%d for d in range(2, int(n**0.5) + 1))

for i in range(int((103*10**6/2)**0.5), int((104*10**6/2)**0.5)+1):
    if 103*10**6 <= 2*i**2 <= 104*10**6 and f(i):
        print(2*i**2, 2*i)