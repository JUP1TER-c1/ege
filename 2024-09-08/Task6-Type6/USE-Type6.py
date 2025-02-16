from itertools import product

count = 0

consonant = 'ПРБЛ'
vowel = 'ОА'
for i in product(consonant, vowel, consonant, vowel, consonant, vowel, consonant, vowel):
    p=''.join(i)
    if p.count('П') == p.count('Р') == p.count('Б') == p.count('Л') == p.count('О') == 1 and p.count('А') == 3:
        count += 1
print(count*2)