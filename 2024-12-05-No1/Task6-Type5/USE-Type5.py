def f(n):
    r = n*4 + n%3
    return r*8 + r%5

n = 1111111110//32-5
m = 1444444416//32-5
while f(n) < 1111111110: n+=1
while f(m) <=  1444444416: m+=1
print(m-n)