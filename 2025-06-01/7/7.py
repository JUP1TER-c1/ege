from math import *

image_bit = 1280*960*ceil(log2(2048))
max_pack_size_bit = 132 * 96468992

max_images_in_pack = max_pack_size_bit/image_bit
print(max_images_in_pack)