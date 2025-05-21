def executor(start, end):
    if start < end: return 0
    if start == end: return 1
    return executor(start - 1, end) + executor(start // 2, end)

print(executor(30, 13) * executor(13, 1))