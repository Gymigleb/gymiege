from ipaddress import *

ip_1 = ip_address("118.187.59.255")
ip_2 = ip_address("118.187.65.115")

for mask in range(16, 31):
    n1 = ip_network(f"{ip_1}/{mask}", 0)
    if ip_1 in n1.hosts() and ip_2 not in n1.hosts():
        print(n1.netmask, mask, n1.num_addresses)