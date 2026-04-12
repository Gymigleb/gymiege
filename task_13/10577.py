from ipaddress import *

ip1 = ip_address("165.112.200.70")
ip2 = ip_address("165.112.175.80")

for m in range(16, 31):
    net = ip_network(f"{ip1}/{m}", 0)
    if ip1 in net.hosts() and ip2 in net.hosts():
        print(m)