from itertools import product
digits = '0123'
count = 0
for number in product(digits, repeat=3):
    if int(number[0]) == 0: continue
    if int(number[0]) + int(number[2]) > int(number[1]):
        count += 1

print(count)
