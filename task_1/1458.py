from itertools import *

g = "АБ БЕ ЕЖ ЖД ДВ ВА ДЕ ГВ ГА ГД ГБ".split()
m = "256 13467 2456 237 136 1235 24".split()

for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g): print(*i)