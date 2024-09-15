#Пронумеруем буквы в алфавитном порядке: А = 0, В = 1, О = 2, Р = 3, Т = 4
#Тогда ТАРА = 4030

c = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for s in range(5):
                c+=1
                if i == 4 and j == 0 and k == 3 and s == 0:
                    print(c)

#Ответ 516
