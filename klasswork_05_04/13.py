from ipaddress import *

net = ip_network("172.16.192.0/255.255.192.0")
cnt = 0

for i in net:
    if str(i).count("5")% 5 != 0:
        cnt += 1

print(cnt)