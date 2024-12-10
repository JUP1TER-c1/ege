from itertools import product
alphabet = sorted('МАНГУСТ')

def way1(line):
    count = 0
    result = ''
    for l1 in line:
        for l2 in line:
            for l3 in line:
                for l4 in line:
                    for l5 in line:
                        for l6 in line:
                            count += 1
                            word = ''.join([l1, l2, l3, l4, l5, l6])
                            if word[0] != 'У' and word.count('М') == 2 and word.count('Г') < 2:
                                result = word
                                res_count = count
    print(f'Слово {result} под номером {res_count}')


def way2(line):
    count = 0
    result = ''
    for word in list(product(line, repeat=6)):
        count += 1
        word = ''.join(word)
        if word[0] != 'У' and word.count('М') == 2 and word.count('Г') < 2:
            result = word
            res_count = count
    print(f'Слово {result} под номером {res_count}')

way1(alphabet)
way2(alphabet)