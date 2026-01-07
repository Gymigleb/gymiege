a = 283**382 + 9**15 + 2**3

from string import digits
from string import ascii_lowercase

alph = digits + ascii_lowercase

def f(n):
    out = ""
    while n:
        out += alph[n%14]
        n //= 14
    return out[::-1]

print(f(a).count("b") - f(a).count("c"))