from itertools import product

consonants = "ЗМ"
letters = "ЗИМА"
vowels = "ИА"
count = 0
for word in product(letters, repeat=5):
    if word[0] in consonants and word[-1] in vowels:
        count += 1

print(count)