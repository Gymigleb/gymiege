from itertools import *

alph = "0123456"

cnt = 0

for n in product(alph, repeat=5):
    n = "".join(n)
    if n[0] != "0":
        for j in alph[::2]: n = n.replace(j, "*")
        for j in alph[1::2]: n = n.replace(j, "+")
        if n.count("**") >= 2 and n.count("***") == 0:
            cnt += 1

print(cnt)