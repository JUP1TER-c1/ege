
def game(x, t):
    if t == 3 and x >= 39:
        return 1
    elif t == 3 and x < 39:
        return 0
    elif x >= 39 and t < 3:
        return 0
    else:
        return game(x + 1, t + 1) or game(x + 2, t + 1) or game(x * 2, t + 1)


for x in range(1, 39):
    if game(x, 1) == 1:
        print(x)
        break

#Ответ: 10