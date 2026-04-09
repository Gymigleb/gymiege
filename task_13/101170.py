from ipaddress import *

ip_1 = ip_address("193.175.175.231")
ip_2 = ip_address("193.175.176.118")

for mask in range(16, 33):
    n1 = ip_network(f"{ip_1}/{mask}", 0)
    if ip_1 in n1.hosts() and ip_2 not in n1.hosts():
        print(n1.netmask, mask)
        break