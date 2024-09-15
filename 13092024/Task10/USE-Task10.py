file = open('Мастер и Маргарита.txt')
def find_all(string, substring):
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1: return
        yield start
        start += len(substring)

file = file.read()
file = file.lower()
indexes = list(find_all(file, "тридцат"))

for i in indexes:
    print(file[i:(i+20)])

#Посчитаем, сколько раз "тридцат" встречается само по себе. Ответ - 10
