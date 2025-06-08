from math import *

photo_bit = 1024*768*ceil(log2(4096))
packet_size_bit = 300*1310720
photo_per_packet = packet_size_bit/photo_bit
print(photo_per_packet)