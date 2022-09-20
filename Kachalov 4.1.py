
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simplenumber(n):

    """
    Проверяем число n - простое оно или нет
    Введите целое положительное число
    """

    list_multipliers = []
    list_nonsimple = []

    for i in range(1,n+1):
        for j in range (1,n+1):
            if i*j == n:
                list_multipliers.append(i)
                list_multipliers.append(j)

    list_set_multipliers = set(list_multipliers)
    list_set_multipliers.remove(1)

    for i in list_set_multipliers:
        for j in range(2,i):
            if i % j == 0 and i != j:
                list_nonsimple.append(i)

    list_set_nonsimple = set(list_nonsimple)
    simple_numbers = list_set_multipliers - list_set_nonsimple
    print(simple_numbers)

simplenumber(30)
