a = 15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809

cnte = 0
cnto = 0

while a:
    if (a%7) % 2 == 0: cnte += 1
    else: cnto += 1
    a //= 7
print(cnte-cnto)