A = []
for line in open('27A_18678.txt'):
    print(list(map(float, line.replace(',','.').split())))