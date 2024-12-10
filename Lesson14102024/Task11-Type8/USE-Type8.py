from itertools import product, permutations

alphabet = sorted('РОСОМАХА')
vowels = sorted('ОА')
consonants = sorted('РСМХ')

def way1(line):
    count = set()
    for word in permutations(line, r=8):
        word = ''.join(word)
        for l in range(len(word) - 1):
            l1 = word[l]
            l2 = word[l+1]
            if (l1 in vowels and l2 in vowels) or (l1 in consonants and l2 in consonants):
                break
        else:
            count.add(word)
    print(f'Кол-во: {len(count)}')


def way2(line):
    count = set()
    for word in list(product(line, repeat=8)):
        word = ''.join(word)
        for letter in word:
            if word.count(letter) != line.count(letter): break
        else:
            for l in range(len(word) - 1):
                l1 = word[l]
                l2 = word[l + 1]
                if (l1 in vowels and l2 in vowels) or (l1 in consonants and l2 in consonants):
                    break
            else:
                count.add(word)
    print(f'Кол-во: {len(count)}')

way1(alphabet)
way2(alphabet)
