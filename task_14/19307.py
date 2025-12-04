a = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005

cnt = 0

while a:
    if a % 5 == 0: cnt += 1
    a //= 5
print(cnt)