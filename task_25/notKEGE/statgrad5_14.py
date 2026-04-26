def S(n):
    ans = set()
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            ans.add(d)
            ans.add(n//d)
    # print(ans)
    return sum(ans)

def K(n):
    st=n
    ans = set()
    for d in range(2, int(n**0.5) + 1):
        while n % d == 0:
            ans.add(d)
            n //= d
    for d in range(3, int(n**0.5) + 1, 2):
        while n % d == 0:
            ans.add(d)
            n //= d
    if n != 1: ans.add(n)
    # print(ans)
    if len(ans) == 1 and st not in ans:return len(ans)
    return 0

cnt = 0
# print(K(25))
# print(S(25))

for i in range(4_555_706, 10**100):
    if i % 10 != 3 and 0 < (i - S(i) - K(i)) % 100 == 23:
        cnt += 1
        print(i)
        if cnt >= 5: break