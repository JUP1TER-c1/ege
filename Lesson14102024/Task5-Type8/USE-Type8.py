from itertools import product
alphabet = sorted('АЛГОРИТМ')

def way1(line):
    count = 0
    for l1 in line:
        for l2 in line:
            for l3 in line:
                for l4 in line:
                    count += 1
                    word = ''.join([l1, l2, l3, l4])
                    if word[:2] == 'ИГ':
                        print(f'Слово {word} под номером {count}')
                        return


def way2(line):
    count = 0
    for word in list(product(line, repeat=4)):
        count += 1
        word = ''.join(word)
        if word[:2] == 'ИГ':
            print(f'Слово {word} под номером {count}')
            return

way1(alphabet)
way2(alphabet)