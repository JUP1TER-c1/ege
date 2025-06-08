odd = '13579'
even = '02468'
cnt = 0
for number in range(1000, 10000):
    number = str(number)
    if len(set(number)) != len(number): continue
    for i in range(0, len(number) - 1):
        if (number[i] in odd and number[i+1] in odd) or (number[i] in even and number[i+1] in even):
            cnt += 1

print(cnt)