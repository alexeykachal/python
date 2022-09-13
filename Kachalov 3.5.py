
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

a = 8
def fibo(a):
    b = []
    c = 0
    d = []
    e = []
    f = 0

    b.append(0)
    b.append(1)

    for i in range(2,a+1):
        c = b[i-1] + b[i-2]
        b.append(c)


    for i in range(1,a+1):
        f = (-1)**(i+1)*b[i]
        e.append(f)
    e.reverse()


    joinedlist = e + b
    print(joinedlist)

fibo(a)
