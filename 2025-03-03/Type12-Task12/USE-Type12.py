def redactor(n: str):
    while '49' in n or '97' in n or '47' in n:
        if '47' in n:
            n = n.replace('47', '74', 1)
        if '97' in n:
            n = n.replace('97', '79', 1)
        if '49' in n:
            n = n.replace('49', '94', 1)
    return n


line = 40*'7' + 40*'9' + 50*'4'
res = redactor(line)
print(res[24], res[70], res[104])