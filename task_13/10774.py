from ipaddress import *

ip1 = ip_address("217.19.128.131")
net = ip_network(f"{ip1}/255.255.192.0", 0)

print(net[0], "HCEA")