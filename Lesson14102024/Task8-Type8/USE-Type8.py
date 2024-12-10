from itertools import product
alphabet = sorted('ABCDXYZ')

def way1(line):
    count = 0
    for l1 in line:
        for l2 in line:
            for l3 in line:
                for l4 in line:
                    word = ''.join([l1, l2, l3, l4])
                    if word[0] in ['X', 'Y', 'Z'] and list(set(word[1:]) & {'X', 'Y', 'Z'}) == []:
                        count += 1
    print(f'Кол-во: {count}')


def way2(line):
    count = 0
    for word in list(product(line, repeat=4)):
        word = ''.join(word)
        if word[0] in ['X', 'Y', 'Z'] and list(set(word[1:]) & {'X', 'Y', 'Z'}) == []:
            count += 1
    print(f'Кол-во: {count}')

way1(alphabet)
way2(alphabet)