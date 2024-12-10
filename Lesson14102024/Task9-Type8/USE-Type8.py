from itertools import product, permutations

alphabet = sorted('МАТВЕЙ')

def way1(line):
    count = 0
    for word in permutations(line, r=6):
        word = ''.join(word)
        if word[0] != 'Й' and word.find('АЕ') == -1:
            count += 1
    print(f'Кол-во: {count}')


def way2(line):
    count = 0
    for word in list(product(line, repeat=6)):
        word = ''.join(word)
        if len(set(word)) == 6 and word[0] != 'Й' and word.find('АЕ') == -1:
            count += 1
    print(f'Кол-во: {count}')

way1(alphabet)
way2(alphabet)