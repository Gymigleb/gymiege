from itertools import *

alph = sorted("солнце")

cnt = 0

for p, s in enumerate(product(alph, repeat=6), start=1):
    if p % 2 == 0 and not s[0] in "ое" and s.count("ц") == 2:
        cnt += 1
print(cnt)