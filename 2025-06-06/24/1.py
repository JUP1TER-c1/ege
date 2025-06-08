data = open('1.txt').readline()
alph = '0123456789ABCD'
even = '02468AC'
for i in range(len(data)):
    if data[i] not in alph and data[i] != '|':
        data = data.replace(data[i], '|')
while '||' in data or '|0' in data:
    data = data.replace('||', '|')
    data = data.replace('|0', '|')
data = data.split('|')
maxlen = 0
for number in data:
    if number == '': continue
    if number[0] == '0': number = number[1:]
    while number[-1] not in even and len(number) > 1:
        number = number[:-1]
    if len(number) >= maxlen:
        print(number)
        maxlen = max(len(number), maxlen)

print(maxlen)

