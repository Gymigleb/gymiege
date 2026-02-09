def f(num):
    dels = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            dels |= {i, num // i}
    if len(dels) == 3:
        return max(dels)
    return 0

for N in range(int(106_732_567 ** .5), int(152_673_836 ** .5)):
    if M := f(N ** 2):
        print(N ** 2, M)