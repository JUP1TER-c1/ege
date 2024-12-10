from itertools import product, permutations

alphabet = sorted('МИТРОФАН')
vowels = sorted('ИОА')
consonants = sorted('МТРФН')

def way1(line):
    count = 0
    for word in permutations(line, r=6):
        word = ''.join(word)
        for l in range(len(word) - 1):
            l1 = word[l]
            l2 = word[l + 1]
            if l1 in vowels and l2 in vowels:
                break
        else:
            if len(list(set(word) & set(vowels))) < len(list(set(word) & set(consonants))):
                count += 1
    print(f'Кол-во: {count}')


def way2(line):
    count = 0
    for word in list(product(line, repeat=6)):
        word = ''.join(word)
        if len(set(word)) != len(word): continue
        for l in range(len(word) - 1):
            l1 = word[l]
            l2 = word[l + 1]
            if l1 in vowels and l2 in vowels:
                break
        else:
            if len(list(set(word) & set(vowels))) < len(list(set(word) & set(consonants))):
                count += 1
    print(f'Кол-во: {count}')

way1(alphabet)
way2(alphabet)