from math import *

#n kege 1855
L = 101
N = 4090 + 10
i = ceil(log(N, 2))
I = ceil(L*i/8)
print(2048*I/1024)

#n kege 23749
for N in range(1, 10**8):
    L = 2783
    i = ceil(log(N, 2))
    I = ceil(L*i/8)
    if 11*1024*1024*1024 <= I*3_845_627:
        print(N)
        break

#n kege 23370
for L in range(1, 10**100):
    N = 10 + 17
    i = ceil(log(N, 2))
    I = ceil(L*i/8)
    if I*7_564_230 > 31*1024*1024:
        print(L)
        break