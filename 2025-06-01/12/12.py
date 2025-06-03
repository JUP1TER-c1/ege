def redactor(l):
    while '111' in l or '8888' in l:
        if '111' in l:
            l = l.replace('111', '88', 1)
        else:
            l = l.replace('88888', '8', 1)
    return l

print(redactor('1'*81))