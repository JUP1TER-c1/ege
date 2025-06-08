from ipaddress import *

def ip_to_bin(ip):
    return '.'.join([bin(int(byte) + 256)[3:] for byte in ip.split('.')])

cnt = 0
for ip in ip_network('112.160.0.0/255.240.0.0', False):
    #print(str(ip), ip_to_bin(str(ip)))
    if ip_to_bin(str(ip)).count('1') % 5 != 0:
        cnt += 1
print(cnt)