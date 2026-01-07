a = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1

count = 0
while a:
    if a % 16 == 0: count += 1
    a //= 16
print(count)