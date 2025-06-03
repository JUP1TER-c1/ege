
data = open('24_21717.txt').read()
lp = 0
cnt = 0
min_len = 10000

for rp in range(2, len(data)):
    # if data[rp] == 'Q': continue
    if data[rp - 2] + data[rp - 1] + data[rp] == 'RSQ': cnt += 1
    while cnt == 130 and data[rp] != 'Q':
        min_len = min(min_len, rp - lp+1)
        if data[lp] + data[lp + 1] + data[lp + 2] == 'RSQ': cnt -= 1
        lp += 1
print(min_len)
