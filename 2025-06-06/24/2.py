data = open('2.txt').readline()
lp = 0
cnt = 0
maxlen = 0
for rp in range(1, len(data)):
    if data[rp - 1] + data[rp] == 'CD':
        cnt += 1
    while cnt > 140:
        if data[lp] + data[lp + 1] == 'CD':
            cnt -= 1
        lp += 1
    maxlen = max((rp - lp) + 1, maxlen)
print(maxlen)

