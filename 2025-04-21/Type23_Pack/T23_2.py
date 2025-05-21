def calculator(start, end):
    if start < end or start == 15: return 0
    if start == end: return 1
    return calculator(start - 2, end) + calculator(start - 3, end) + calculator(start // 3, end)

print(calculator(48, 25) * calculator(25, 17) * calculator(17, 4))