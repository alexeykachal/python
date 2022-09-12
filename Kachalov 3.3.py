
#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

a = [1.1, 1.9, 3.1, 5.17, 10.02767]
def minmax_subtraction(a):
    b = 0
    c = []
    d = 0
    sum_minmax = 0
    for i in a:
        b = round(i % 1, 10)
        c.append(b)
    d = max(c) - min(c)
    print(d)

minmax_subtraction(a)
