from ipaddress import *

net = ip_network('203.68.128.0/255.255.192.0', False)

count = 0
for ip in net:
    segments = str(ip).split('.')
    ones = sum(bin(int(segment))[2:].count('1') for segment in segments)
    if ones % 7 != 0:
        count += 1

print(count)



