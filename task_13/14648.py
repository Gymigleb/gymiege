from ipaddress import *

ip_1 = ip_address("218.48.192.56")
ip_2 = ip_address("218.48.192.0")

for mask in range(16, 31):
    n1 = ip_network(f"{ip_2}/{mask}", 0)
    if n1[0] == ip_2 and ip_1 in n1.hosts() and n1.num_addresses - 2 >= 500:
        print(n1.netmask, n1.num_addresses)