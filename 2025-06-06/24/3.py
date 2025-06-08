data = open('3.txt').readline()
lp = 0
cnt = 0
minlen = 10 ** 40
for rp in range(1, len(data)):
    if data[rp - 1] + data[rp] == 'TT':
        cnt += 1
    while cnt == 150:
        if data[lp] + data[lp + 1] == 'TT':
            minlen = min((rp - lp) + 1, minlen)
            cnt -= 1
        lp += 1

print(minlen)

