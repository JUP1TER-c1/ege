def executor(start, end):
    # print(f"{start} -> {end}", start > end)
    if start > end or start == 35:
        return 0
    if start == end:
        return 1
    return executor(start + 1, end) + executor(start + 2, end) + executor(start*2, end)

print(executor(7, 13) * executor(13, 15) * executor(15, 51))