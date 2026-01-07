a = 39*121**319 + 46*11**913 - 15*1331**15 - 1993

count = 0

while a:
    b = a % 121
    if  b >= 64 and b <= 104: count += 1
    a //= 121

print(count)