from itertools import product
alphabet = sorted('ВЕРОНИКА')

def way1(line):
    count = 0
    for l1 in line:
        for l2 in line:
            for l3 in line:
                word = ''.join([l1, l2, l3])
                if word.count('В') != 1: continue
                count += 1
                if word.count('А') == 0 and word.count('В') == 1:
                    print(f'Слово {word} под номером {count}')
                    return


def way2(line):
    count = 0
    for word in list(product(line, repeat=3)):
        word = ''.join(word)
        if word.count('В') != 1: continue
        count += 1
        if word.count('А') == 0 and word.count('В') == 1:
            print(f'Слово {word} под номером {count}')
            return

way1(alphabet)
way2(alphabet)