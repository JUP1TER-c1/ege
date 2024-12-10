from itertools import product
alphabet = 'КЛРТ'

def way1(line):
    count = 1
    for l1 in line:
        for l2 in line:
            for l3 in line:
                for l4 in line:
                    if count == 67:
                        print(''.join([l1, l2, l3, l4]))
                    count += 1

def way2(line):
    words = list(product(line, repeat=4))
    print(*words[66])


way1(alphabet)
way2(alphabet)