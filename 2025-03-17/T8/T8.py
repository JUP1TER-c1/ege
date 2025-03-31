from itertools import product

letters = 'А Н Д Р Е Й'.split()
count = 0
for word in product(letters, repeat=6):
    if word.count('А') >= 1 >= word.count('Й'):
        count += 1

print(count)