def executor(start, end):
    if start == end:
        return 1
    if start > end or start == 56:
        return 0
    return executor(start + 3, end) + executor(start + 7, end) + executor(start * 3, end)

print(executor(12, 40) * executor(40, 72) * executor(72, 89))

