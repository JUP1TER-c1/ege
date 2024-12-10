from itertools import product
alphabet = sorted('01234567')

def way1(line):
    count = 0
    for l1 in line:
        for l2 in line:
            for l3 in line:
                for l4 in line:
                    for l5 in line:
                        word = ''.join([l1, l2, l3, l4, l5])
                        if word.count('6') != 1 or word[0] == '0': continue
                        flag = True
                        idx = word.index('6')
                        if idx > 0:
                            if int(word[idx - 1]) % 2 != 0:
                                flag = False
                        if idx < 4:
                            if int(word[idx + 1]) % 2 != 0:
                                flag = False
                        if flag:
                            count += 1
    print(f'Кол-во: {count}')


def way2(line):
    count = 0
    for word in list(product(line, repeat=5)):
        word = ''.join(word)
        if word.count('6') != 1 or word[0] == '0': continue
        flag = True
        idx = word.index('6')
        if idx > 0:
            if int(word[idx - 1]) % 2 != 0:
                flag = False
        if idx < 4:
            if int(word[idx + 1]) % 2 != 0:
                flag = False
        if flag:
            count += 1
    print(f'Кол-во: {count}')

way1(alphabet)
way2(alphabet)