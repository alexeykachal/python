
#Напишите программу, которая принимает на вход число N и выдает набор произведений
# (набор - это список) чисел от 1 до N.

def fact_components(x):
    a = x
    num = []
    numx = []
    while x != 1:
        x = x - 1
        num.append(x)
    num.insert(0,a)

    for i in range(len(num)):
        if i == 0:
            numx = [1]
        else:
            numx.append(numx[i-1]*(i+1))
    print(numx)

fact_components(5)