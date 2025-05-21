import math


def calculator(current, end):
    if current < end or current == 24: return 0
    if current == end: return 1
    return calculator(current - 1, end) + calculator(math.floor(current**0.5), end) + calculator(int(str(current)[:-1]) if current > 9 else 0, end)

print(calculator(602, 7))
