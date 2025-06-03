sequence = list(map(int, open('17.txt').read().split('\n')))

flagged = 0
for number in sequence:
    if number % 32 == 0:
        flagged += 1

pairs = []
for i in range(len(sequence) - 1):
    pair = [sequence[i], sequence[i + 1]]
    if (pair[0] < 0 or pair[1] < 0) and sum(pair) < flagged:
        pairs.append(sum(pair))

print(len(pairs), max(pairs))


