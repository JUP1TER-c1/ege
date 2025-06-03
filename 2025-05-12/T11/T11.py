from math import *

for N in range(2, 10000):
    letter_bit = ceil(log2(N))
    serial_number_byte = ceil(letter_bit*246/8)
    all_numbers_byte = 703_569*serial_number_byte
    if all_numbers_byte <= 77*1024*1024:
        print(N)