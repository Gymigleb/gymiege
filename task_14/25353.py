for x in range(1, 27001):
    a = 3*27**9 + 2*27**6 + 27**3 - x
    cnt = 0
    while a:
        if a % 27 == 0: cnt += 1
        a //= 27
    if cnt == 6:
        print(x)
        break