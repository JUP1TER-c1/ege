file = [int(i) for i in open('17.txt')]
array = [i for i in file if i%10 == 5]
result = []

for i in range(len(file)-1):
    n1, n2 = file[i], file[i+1]

    if str(min(n1, n2))[-1] == '5':
        if (n1 ** 2 + n2 ** 2) < min(array) ** 2:
            result.append(n1 ** 2 + n2 ** 2)

print(len(result), max(result)) #Ответ: 403 | 99805561