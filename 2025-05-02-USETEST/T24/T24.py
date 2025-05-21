from re import *

line = open('24.txt').readline()
pattern = "[123456789AB][0123456789AB]*[02468A]"
matches = findall(pattern, line)

matches = dict(zip([len(match) for match in matches], matches))
print(max(matches), matches[max(matches)])