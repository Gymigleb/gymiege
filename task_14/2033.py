a = 6*144**26 + 11*12**75 - 48

count = 0
while a:
    if a % 12 == 11: count += 1
    a //= 12
print(count)