def calc(start, end):
    if start < end: return 0
    if start == end: return 1
    return calc(start - 2, end) + calc(start//2, end) + calc(start//3, end)

print(calc(40, 20) * calc(20, 4))