a = 3*17**777 + 15*17**250 - 6*17**100 + 2

ans = []

while a:
    if a % 17 % 2 == 0: ans.append(a%17)
    a //= 17
print(set(ans))
print(len(set(ans)))