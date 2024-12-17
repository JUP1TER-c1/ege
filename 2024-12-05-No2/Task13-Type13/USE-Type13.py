from ipaddress import *
maxx = 0
for mask in range(32+1):
    network = ip_network(f'98.162.71.94/{mask}', False)
    if str(network) == f'98.162.71.64/{mask}':
        maxx = max(maxx, network.num_addresses)
print(maxx)

print(ip_network(f'231.32.255.131/20'))