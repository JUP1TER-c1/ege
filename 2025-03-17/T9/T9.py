count = 0
for line in open('9.txt'):
    row = list(map(int, line.split()))
    if len(set(row)) != 5: continue
    repeated = []
    other = []
    for n in row:
        if row.count(n) > 1:
            repeated.append(n)
        else:
            other.append(n)
    if sum(other)/len(other) <= sum(repeated):
        count += 1

print(count)
