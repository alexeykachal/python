
#Напишите программу, которая будет преобразовывать десятичное число в двоичное

a = 3131
def converter(a):
    b = 0
    c = []
    d = 0
    e = []

    if a == 0:
        d = 0
    else:
        while a > 1:
            if a % 2 != 0:
                b = a - (a // 2) *2
                c.append(b)
            else:
                b = 0
                c.append(b)
            a = a // 2
        c.reverse()
        e.append(str(1))
        for i in c:
            i = str(i)
            e.append(i)

        d = ''.join(e)
    print(d)

converter(a)
