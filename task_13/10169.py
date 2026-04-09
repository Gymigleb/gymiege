from ipaddress import *

ip_1 = ip_address("157.127.182.76")
ip_2 = ip_address("157.127.190.80")

for mask in range(16, 33):
    n1 = ip_network(f"{ip_1}/{mask}", 0)
    if ip_1 in n1.hosts() and ip_2 not in n1.hosts():
        print(n1.netmask, mask)
        break