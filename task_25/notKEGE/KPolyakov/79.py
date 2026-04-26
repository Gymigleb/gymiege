def f(n):
    d = 2
    if n % d == 0: return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0: return False
    return True

cnt = 1
for i in range(3, 9000000 + 1, 2):
    if f(i): cnt += 1
print(cnt)