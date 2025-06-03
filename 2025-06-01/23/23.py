def ex(start, end):
    if start < end: return 0
    if start == end: return 1
    return ex(start - 2, end) + ex(start // 2, end)

print(ex(38, 16) * ex(16, 2))