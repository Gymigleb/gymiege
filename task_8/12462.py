from itertools import *

cnt = 0

def f(s):
    for i in range(len(s) - 1):
        if not (s[i] > s[i + 1]): return False
    return True

for i in product(range(16), repeat=3):
    if f(i): cnt += 1
for i in product(range(16), repeat=5):
    if f(i): cnt += 1

print(cnt)