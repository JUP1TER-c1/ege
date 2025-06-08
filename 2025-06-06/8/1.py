from itertools import product
alphabet = '0123456'
banned_first = '0135'
banned_last = '23'
cnt = 0
for number in product(alphabet, repeat=5):
    if number[0] in banned_first or number.count('1') < 2 or number[-1] in banned_last: continue
    print(number)
    cnt += 1
print(cnt)