"""systems of count"""

#binary#binary#binary#binary#
N = 25
print(bin(N)[2:])
print(f"{N:b}")
#binary#binary#binary#binary#

#octogonal#octogonal#octogonal#octogonal#
print(oct(N)[2:])
print(f"{N:o}")
#octogonal#octogonal#octogonal#octogonal#

#hexogoal#hexogoal#hexogoal#hexogoal#hexogoal#
print(hex(N))
print(f"{N:x}")
#hexogoal#hexogoal#hexogoal#hexogoal#hexogoal#

#from decimal to another#from decimal to another#
# 2 <= k <= 9
def num_from_dec_to_k(num, k):
    out = ""
    while num > 0:
        out += str(num % k)
        num = num // k
    return out[::-1]
print(num_from_dec_to_k(N,2))
#from decimal to another#from decimal to another#

#from decimal to another#from decimal to another#
from string import digits,ascii_lowercase
# k <= 36
def num_from_dec_to_k(num, k):
    out = ""
    alph = digits + ascii_lowercase
    while num > 0:
        out += alph[num % k]
        num = num // k
    return out[::-1]
print(num_from_dec_to_k(124,14))
#from decimal to another#from decimal to another#

#from another to decimal#from another to decimal#from another to decimal#
bin_n = "101"
oct_n = "765"
tri_n = "1201"
print(int(bin_n, 2))
print(int(oct_n, 8))
print(int(tri_n, 3))
#from another to decimal#from another to decimal#from another to decimal#