from itertools import*

m = "27 1567 67 5 246 2357 1236".split()
g = "АБ БД ДК КЕ ЕГ ГВ ВБ ВД ДЕ ЕВ".split()

for i in permutations("АБВГДЕК"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(i)

print(9)