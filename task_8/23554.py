from  itertools import *

alph = sorted("алгоритм")

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and not val[0] in "аг" and val.count("р") >= 2:
        print(pos)
        break
