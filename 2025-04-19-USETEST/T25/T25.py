import fnmatch

number = 7993
while number < 10**10:
    if fnmatch.fnmatch(str(number), "4*4736*1"):
        print(f"Found number: {number}; {number/7993}")
    number += 7993