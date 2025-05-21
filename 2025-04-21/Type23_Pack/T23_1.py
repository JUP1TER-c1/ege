

def calculator(start, end):
    if start > end or start == 35:
        return 0
    if start == end:
        return 1
    return calculator(start + 1, end) + calculator(start + 2, end) + calculator(start * 2, end)

print(
    calculator(7, 13) *
    calculator(13, 15) *
    calculator(15, 51)
)