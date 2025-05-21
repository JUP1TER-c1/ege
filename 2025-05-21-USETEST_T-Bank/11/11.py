from math import *


user_bytes = 800/40
user_bit = user_bytes*8
passw_bit = 20 * ceil(log2(18))
print((user_bit - passw_bit)/8)



