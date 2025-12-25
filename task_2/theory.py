# in math
# 1) not
# 2) and
# 3) or
# 4) <=
# 5) ==
#
# python
# 1) ()
# 2) **
# 3) /, //, %, *
# 4) +, -
# 5) ==, !=, <, <=, >=, >
# 6) not
# 7) and
# 8) or

# args
def f1(a, b, c):
    return a + b + c

test = [1, 2, 3]
print(f1(*test))
test = "123"
print(f1(*test))
# print(f1(test)) error

# kwargs

def f2(a, b):
    return a / b

test2 = {"a": 5, "b": 2}
print(f2(**test2))
test2 = {"b": 3, "a": 7}
print(f2(**test2))

# auto solve# auto solve# auto solve# auto solve# auto solve# auto solve#
from itertools import *

def f(x, y, z, w):
    return (x or y) and not (y == z) and not w

for i in product((0, 1), repeat=4):
    table = [
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]
    if len(set(table)) == len(table):
        for j in permutations("xyzw"):
            if [f(**dict(zip(j, t))) for t in table] == [1, 1, 1]:
                print(*j)
                print(*j, sep="")
# auto solve# auto solve# auto solve# auto solve# auto solve# auto solve#