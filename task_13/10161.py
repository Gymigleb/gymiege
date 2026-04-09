from ipaddress import *

ip_1 = ip_address("211.115.61.154")
ip_2 = ip_address("211.115.59.137")

for mask in range(16, 33):
    n1 = ip_network(f"{ip_1}/{mask}", 0)
    if ip_1 in n1.hosts() and ip_2 in n1.hosts():
        print(n1.netmask)