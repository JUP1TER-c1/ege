def game(x, t):
    if (t == 3 or t == 5) and x >= 39:
        return 1
    elif t == 5 and x < 39:
        return 0
    elif x >= 39 and t < 5:
        return 0
    else:
        if t % 2 == 0:
            return game(x + 1, t + 1) or game(x + 2, t + 1) or game(x * 2, t + 1)
        else:
            return game(x + 1, t + 1) and game(x + 2, t + 1) and game(x * 2, t + 1)

for x in range(1, 39):
    if game(x, 1) == 1:
        print(x)

#Получаем два ответа. Но ответ 19 камней не попадает под второе условие, при котором Ваня не может выиграть в свой первый ход
#Ответ: 16