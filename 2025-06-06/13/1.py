from ipaddress import *

def ip_to_bin(ip):
    return '.'.join([bin(int(byte) + 256)[3:] for byte in ip.split('.')])

print(ip_to_bin('157.220.185.237'))
print(ip_to_bin('157.220.184.230'))
cnt = 0
for ip in ip_network('157.220.185.237/23', False):
    #print(str(ip), ip_to_bin(str(ip)))
    if ip_to_bin(str(ip)).count('1') == 15:
        cnt += 1
print(cnt)