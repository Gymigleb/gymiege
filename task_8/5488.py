from itertools import *

alph = "полина"

def m(s):
    a = "оиа"
    b = "плн"
    cnta = 0
    cntb = 0
    for i in a:
        cnta += s.count(i)
    for i in b:
        cntb += s.count(i)
    return cntb > cnta 

cnt = 0

for i in product(alph, repeat=8):
    if m(i): cnt += 1

print(cnt)