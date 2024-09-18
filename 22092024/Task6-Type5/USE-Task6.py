count = 0
for number in range(1000, 10000):
    string_number = str(number)
    if int(string_number[0])%2!=0 and int(string_number[1])%2!=0 and int(string_number[2])%2!=0 and int(string_number[3])%2!=0:
        sum1 = int(string_number[0]) + int(string_number[1])
        sum2 = int(string_number[2]) + int(string_number[3])
        num1 = min(sum1, sum2)
        num2 = max(sum1, sum2)
        result = str(num1) + str(num2)
        if result == '616':
            count += 1

print(count) #Ответ: 12
