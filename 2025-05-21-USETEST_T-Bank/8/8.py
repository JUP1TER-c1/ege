banned = '5678'
cnt1 = 0
cnt2 = 0
for number in range(10000, 100000):
    number = str(number)
    if number.count('3') == 1:
        idx3 = number.find('3')
        if (number[idx3 - 1] not in banned if idx3 != 0 else 1) and (number[idx3 + 1] not in banned if idx3 != 4 else 1):
            cnt1 += 1
            print(number, idx3)
for number in range(10000, 100000):
    number = str(number)
    if number.count('3') != 1: continue
    number = '0' + number + '0'
    idx3 = number.find('3')
    if number[idx3 - 1] not in banned and number[idx3 + 1] not in banned:
        cnt2 += 1
        print(number, idx3)
print(cnt1, cnt2)