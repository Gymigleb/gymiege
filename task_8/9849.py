from itertools import *

alph = "abcdef"
cnt = 0

for i in product(alph, repeat=6):
    if i[0] not in "ae" and i[-1] not in "ae": cnt += 1

print(cnt)