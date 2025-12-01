from  itertools import *

alph = sorted("строка")

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 1 and not val[0] in "ал" and val.count("с") == 1:
        print(pos)
