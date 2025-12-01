from itertools import *

#permutations#permutations#permutations#
alph = "122"
res = permutations(alph)
print(*res)
for val in permutations(alph):
    val = "".join(val)
    print(val)
#permutations#permutations#permutations#

#product#product#product#product#product#
alph_2 = "123"
res = product(alph_2, repeat=2)
print(*res)
res = product("abc","abe")
print(*res)
for val in product(alph_2, repeat=2):
    val = "".join(val)
    print(val)
#product#product#product#product#product#

#enumerate#enumerate#enumerate#enumerate#
alph_3 = "123"
res = enumerate(alph_3, start=1)
print(*res)
#enumerate#enumerate#enumerate#enumerate#