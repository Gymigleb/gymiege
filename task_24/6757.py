from re import *

with open("./files/24_6757.txt") as f:
    s = f.readline().strip()

pat = r"(CFE|FCE)*"
ans = [m.group() for m in finditer(pat,s)]

print(len(max(ans, key=len))//3)