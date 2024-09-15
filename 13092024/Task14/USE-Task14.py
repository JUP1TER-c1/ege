for i in '0123456789ABC':
    res = int('26' + i + '98', 13) + int('4' + i + '296', 13)
    if res % 34 == 0:
        print(res // 34)
        break

#Ответ: 6141

