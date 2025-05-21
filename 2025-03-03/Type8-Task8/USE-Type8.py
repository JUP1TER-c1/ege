from itertools import product

letters = 'Б О Р И С'.split()
count = 0
for word in product(letters, repeat=6):
    if word.count('С') <= 1 and word.count('Б') == 1 and word.count('Р') == 1:
        count += 1

print(count)
