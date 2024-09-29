from itertools import product
words = [''.join(i) for i in product(['А', 'З', 'И', 'М'], repeat=5)]
count = 0
for i in range(len(words)):
    if words[i].count('И') + words[i].count('А') == 1:
        count += 1
print(count)