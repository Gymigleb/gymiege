from itertools import *

alph = "01"
cnt = 0

for s in product(alph, repeat=16):
    if s[0] != "0" and s.count("1") % 3 == 0: cnt += 1 

print(cnt)