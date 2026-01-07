from itertools import *

alph1 = "конец"
alph2 = "дракон"
words1 = []
words2 = []
ans = []

for s in product(alph1, repeat=5):
    s = "".join(s)
    words1.append(s)

for s in product(alph2, repeat=5):
    s = "".join(s)
    words2.append(s)

for i in words1:
    if i not in words2: ans.append(i)

for i in words2:
    if i not in words1: ans.append(i)

print(ans)
print(len(ans))