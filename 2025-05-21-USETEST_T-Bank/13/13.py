from ipaddress import *
for mask in range(32, 0, -1 ):
    print('hih')
    net = ip_network(f'149.238.225.115/{mask}', False)
    print(net)
    ips = [ip for ip in net]
    print(ips)