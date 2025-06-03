
result = []
for line in open('9.txt'):
    line = list(map(int, line.split()))
    if sorted(line)[::-1] != line: continue
    minmax_avg = (line[0] + line[-1])/2
    other_avg = (sum(line) - minmax_avg*2)/5
    if minmax_avg > other_avg:
        result.append(sum(line))

print(result[0])
