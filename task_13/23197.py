from ipaddress import *

ip1 = ip_address("45.172.106.203")


net = ip_network(f"{ip1}/255.255.252.0", 0)
print(net[-2])