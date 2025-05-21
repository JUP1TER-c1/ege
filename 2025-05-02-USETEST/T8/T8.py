from itertools import *

alphabet = sorted('Д Г И А Ш Э'.split())
vowels = sorted('И А Э'.split())
consonants = sorted('Д Г Ш'.split())

cnt = 0
for word in product(alphabet, repeat=5):
    if (word[0] in consonants) and (word[-1] in vowels):
        cnt += 1
print(cnt)