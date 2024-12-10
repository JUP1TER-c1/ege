from itertools import product, permutations

alphabet = sorted('ГЕРАСИМ')
vowels = sorted('ЕАИ')
consonants = sorted('ГРСМ')

def way1(line):
    count = 0
    for word in permutations(line, r=7):
        word = ''.join(word)
        for l in range(len(word) - 1):
            letters = tuple([word[l], word[l+1]])
            if letters in list(permutations(vowels, 2)) or letters in list(permutations(consonants, 2)):
                break
        else:
            count += 1
    print(f'Кол-во: {count}')


def way2(line):
    count = 0
    for word in list(product(line, repeat=7)):
        word = ''.join(word)
        if len(set(word)) != 7: continue
        for l in range(len(word) - 1):
            letters = tuple([word[l], word[l + 1]])
            if letters in list(permutations(vowels, 2)) or letters in list(permutations(consonants, 2)):
                break
        else:
            count += 1
    print(f'Кол-во: {count}')

way1(alphabet)
way2(alphabet)