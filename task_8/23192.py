from  itertools import *

alph = sorted("теория")

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 1 and not val[0] in "ртя" and val.count("и") >= 2:
        print(pos)
