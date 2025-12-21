from itertools import *

g = "АБ БВ ВД ДЕ ЕВ ЕК КГ ГВ ГЕ".split()
m = "24 146 56 1267 36 23457 46".split()

print(*range(1,8))
for i in permutations("АБВГДЕК"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g): print(*i)