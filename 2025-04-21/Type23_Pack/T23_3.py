def calculator(start, end, flag_a):
    if start - 2 > end or flag_a > 2: return 0
    if start == end: return 1
    return calculator(start - 1, end, flag_a + 1) + calculator(start + 5, end, 0) + calculator(start * 2, end, 0)

print(calculator(5, 34, 0))
