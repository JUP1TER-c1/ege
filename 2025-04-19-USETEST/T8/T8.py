from itertools import permutations, product

alphabet = sorted('П О Б Е Д А'.split())

words = list(product(alphabet, repeat=6))
for index in range(len(words)):
    if words[index][0] == 'О' and len(set(words[index])) == len(words[index]):
        if (index + 1) % 2 == 0:
            print(index + 1)


