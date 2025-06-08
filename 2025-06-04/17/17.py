
seq = list(map(int, open('17.txt').read().split('\n')))
min_ele = min(seq)
pairs = []
for i in range(len(seq) - 1):
    pair = [seq[i], seq[i + 1]]
    if pair[0] % 16 == min_ele or pair[1] % 16 == min_ele:
        pairs.append(sum(pair))

print(len(pairs), max(pairs))