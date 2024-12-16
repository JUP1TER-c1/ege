from itertools import *

glr = "АБ АД БА БВ БД БЕ ВБ ВГ ВЕ ВЖ ВИ ГВ ГИ ДА ДБ ДЕ ЕБ ЕВ ЕД ЕЖ ЖВ ЖЕ ЖИ ИВ ИГ ИЖ"
snr = "14 15 16 23 25 27 32 37 38 41 46 51 52 56 58 61 64 65 67 72 73 76 78 83 85 87"

up = set(glr.replace(' ', ''))
for permutation in permutations(up):
    cache = glr
    for index, letter in enumerate(permutation):
        cache = cache.replace(letter, str(index + 1))
    difference1 = set(snr.split()) - set(cache.split())
    difference2 = set(cache.split()) - set(snr.split())
    if len(difference1) == 2 and len(difference2) == 2:
        print(f'Порядок пунктов: {permutation}\nПерепутанные дороги: {difference1} {difference2}')