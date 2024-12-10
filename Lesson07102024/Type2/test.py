global n
n = 100
def a():
    global b
    def b():
        global c
        def c():
            global d
            def d():
                global g
                def g():
                    global h
                    def h():
                        global i
                        def i():
                            global j
                            def j():
                                global k
                                def k():
                                    global l
                                    def l():
                                        global m
                                        def m():
                                            global n
                                            def n():
                                                print(n)
a()
b()
c()
d()
g()
h()
i()
j()
k()
l()
m()
n()

# x = 6
# def a():
#     def b(y):
#         return x+y
#     return b
#
# n = 1
#
# def summ(m):
#     return n+m
#
# def state_k():
#     global k
#     k = 1000
#
# try:
#     print(k)
# except:
#     print('kekek')
# state_k()
# print(k)
#
# for i in range(k):
#     state_k()
#
# print(summ(5))
# print(a()(5))
