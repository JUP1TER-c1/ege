data = open('24.txt').readline()

lp = 0
maxlen = 0
current_combs = 0
for rp in range(1, len(data)):
    if data[rp] == 'B' and data[rp-1] == 'A':
        current_combs += 1
    while current_combs > 100:
        if data[lp] == 'A' and data[lp+1] == 'B':
            lp += 1
            current_combs -= 1
        else:
            lp += 1
    if current_combs == 100:
        maxlen = max((rp - lp) + 1, maxlen)
print(maxlen)