from string import printable
from itertools import *

for a in range(1,1000000):
    for x in printable[:15]:
        m = int(f"432{x}3", 15)
        n = int(f"86{x}86", 15)
        if (m + a) % n == 0:
            print(a, x)
            exit(0)
