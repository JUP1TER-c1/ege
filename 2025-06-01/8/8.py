from itertools import product

alphabet = sorted("Ф О К У С".split())
word_num = 0
res = []
for word in product(alphabet, repeat=5):
    word_num += 1
    if word.count("У") == 2 and word.count("Ф") == 0:
        res.append([word_num, ''.join(word)])
print(res[-1])
