cnt = 0
for line in open('9.txt'):
    line = list(map(int, line.split()))
    counts = [line.count(number) for number in line]
    if counts.count(2) != 4 or counts.count(1) != 3: continue
    print(counts)
    unrepeated = []
    for i in range(len(counts)):
        if counts[i] == 1:
            unrepeated.append(line[i])
    if sum(unrepeated)/len(unrepeated) <= sum(line)/len(line):
        cnt += 1
print(cnt)