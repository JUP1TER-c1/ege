def is_prime(number):
    for divider in range(2, (number//2) + 1):
        if number % divider == 0:
            return False
    return True

# Среди команд, передаваемых редактору только одна меняет сумму цифр, а именно "заменить(010, 00)".
# Эта же команда прерывает цикл. В таком случае, сумма строки B будет на 1 меньше суммы строки A

for _ in range(69, 100):
    summ = _ * 1 + _ * 2 - 1
    if is_prime(summ):
        print(_)
        break

# Ответ: 76