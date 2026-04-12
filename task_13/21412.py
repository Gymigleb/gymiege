from ipaddress import *

ip1 = ip_address("143.168.72.213")
net = ip_network(f"{ip1}/255.255.255.240", 0)

print(net[-2])