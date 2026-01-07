def f(a):
    cnt = 0
    while a:
        if a % 7 == 0:
            cnt += 1
        a //= 7
    return cnt
lastX = 0
Mz = 0
for x in range(1, 10001):
    a = 7**270 + 7**170 + 7**70 - x
    z = f(a)
    if Mz <= z:
        lastX = x
        Mz = z
        
print(lastX)