from math import *
l = 2783
n = 3845627
for i in range(1000, 0, -1):
    if ceil(l*i/8)*n >= 11*1024*1024*1024:
        print(i)
print(2**8+1)