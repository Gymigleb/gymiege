from itertools import product

def f(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 : return True
    return False

ans = []

for l1 in range(1, 5):
    for N in range(10**(l1-1), 10**l1):
        if f(N):
            for l2 in range(4 - l1 + 1):
                for Z1 in product("0123456789", repeat=l2):
                    Z1 = "".join(Z1)
                    for Z2 in product("0123456789", repeat=4 - l1 - l2):
                        Z2 = "".join(Z2)
                        num = int(f"1{N}03{Z1}6{Z2}")
                        if num % 22768 == 0 and num < 10**8:
                            ans.append([num, N])

print(sorted(ans))
for i in sorted(ans):
    print(*i)