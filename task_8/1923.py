from itertools import *

alph = "питон"
cnt = 0

for p, s in enumerate(product(alph, repeat=4), start=1):
    s = "".join(s)
    sm = s.replace("т", "п").replace("н", "п")
    sm = sm.replace("о", "и")
    if sm.find("пп") == -1 and sm.find("ии") == -1:
        cnt += 1
        print(p, s, sm)
print(cnt)