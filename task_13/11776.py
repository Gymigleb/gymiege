from ipaddress import *

net = ip_network("235.86.56.0/255.255.248.0", 0)

cnt = 0

for i in net:
    if f"{int(i):032b}"[-2:] == "11": cnt += 1

print(cnt)