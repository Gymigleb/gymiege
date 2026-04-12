from ipaddress import *

ip1 = ip_address("157.127.172.56")
ip2 = ip_address("157.127.191.78")

for m in range(16, 31):
    net = ip_network(f"{ip1}/{m}", 0)
    if ip1 in net.hosts() and ip2 not in net.hosts():
        print(m)
        break