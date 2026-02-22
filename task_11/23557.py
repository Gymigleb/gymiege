from math import *
M =  52 + 100 + 500
n = 45877
i = ceil(log(M, 2))
for l in range(10000, 0, -1):
    if ceil(i*l/8)*n > 49*1024*1024:
        print(l)
