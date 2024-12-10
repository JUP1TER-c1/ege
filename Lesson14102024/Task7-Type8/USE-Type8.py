from itertools import product
alphabet = sorted('012345678')

def way1(line):
    count = 0
    for l1 in line:
        for l2 in line:
            for l3 in line:
                for l4 in line:
                    for l5 in line:
                        word = ''.join([l1, l2, l3, l4, l5])
                        sorted_word = ''.join(sorted(word))[::-1]
                        if sorted_word == word and word[0] != '0' and len(set(word)) == len(word):
                            count += 1
    print(f'Кол-во: {count}')


def way2(line):
    count = 0
    for word in list(product(line, repeat=5)):
        word = ''.join(word)
        sorted_word = ''.join(sorted(word))[::-1]
        if sorted_word == word and word[0] != '0' and len(set(word)) == len(word):
            count += 1
    print(f'Кол-во: {count}')

way1(alphabet)
way2(alphabet)