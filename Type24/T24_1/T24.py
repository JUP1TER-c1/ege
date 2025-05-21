from re import *

line = open('24.txt').read()


max_len = 0
for iteration in finditer(r"[ABC]+", line):
    max_len = max(len(iteration.group()), max_len)
print(max_len)