from itertools import product

alphabet = 'М А Н Г У С Т'.split()
cnt = 0
for word in product(alphabet, repeat=6):
    if word[-1] == 'А' or word.count('У') < 1 or word.count('М') != 2: continue
    cnt += 1
print(cnt)