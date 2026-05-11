from re import *

with open("./files/24_23206.txt") as f:
    s = f.readline().strip()

pat = "[0248]([13579A-RT-Z]*[S]){35}[13579A-RT-Z]*"

ans = [m.group() for m in finditer(pat, s)]

print(len(max(ans, key=len)))