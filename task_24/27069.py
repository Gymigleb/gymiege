from re import *

with open("24_27069.txt") as f:
    s = f.read().strip()

pat = r"[A-Z][a-z]*([ ][A-Z]?[a-z]*)*[.]"

matches = finditer(pat, s)
ans = set([m.group() for m in matches])

print(max(ans, key=len), len(max(ans, key=len).split()))
