from string import printable
from itertools import *

ans = set()

for x, y in product(printable[:18], printable[9:18]):
    if y > x:
        a = int(f"5{x}{y}a", 18)
        b = int(f"18{x}7", int(y, 18))
        ans |= {a+b}

print(len(ans))