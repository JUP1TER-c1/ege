from re import *

max_len = [0, '']
text = open('24.txt').readline()
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
    pattern = rf"({char}+)(?=\1)?"
    matches = findall(pattern, text)
    lengths = [len(match) for match in matches]
    if max_len[0] < max(lengths):
        max_len[0] = max(lengths)
        max_len[1] = char

print(max_len)
