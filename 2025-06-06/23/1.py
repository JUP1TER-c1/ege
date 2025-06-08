def calc(start, end, flag):
    if start > end: return 0
    if start == end: return 1
    if flag: return calc(start + 1, end, False) + calc(start * 2, end, False)
    return calc(start + 1, end, False) + calc(start + 2, end, True) + calc(start * 2, end, False)

print(calc(2, 22, False))