from ipaddress import *

ip1 = ip_address("105.224.200.224")
net = ip_network(f"{ip1}/255.255.255.224", 0)
cnt = 0

for i in net:
    b = f"{int(i):032b}"
    if b.count("1") % 4 == 0:
        cnt += 1

print(cnt)