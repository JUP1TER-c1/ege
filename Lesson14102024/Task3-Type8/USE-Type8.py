from itertools import product
alphabet = sorted('КОМПЬТЕР')

def way1(line):
    result = ''
    count = 0
    for l1 in line:
        for l2 in line:
            for l3 in line:
                for l4 in line:
                    for l5 in line:
                        count += 1
                        word = ''.join([l1, l2, l3, l4, l5])
                        if word.count('К') == 0 and word.count('Р') == 2:
                            result = word
                            res_count = count
    print(f'Слово {result} под номером {res_count}')



def way2(line):
    count = 0
    result = ''
    for word in list(product(line, repeat=5)):
        count += 1
        word = ''.join(word)
        if word.count('К') == 0 and word.count('Р') == 2:
            result = word
            res_count = count
    print(f'Слово {result} под номером {res_count}')


way1(alphabet)
way2(alphabet)