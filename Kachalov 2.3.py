
#Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def polindrom(x):
    first_num = x
    count = 0
    while True:
        if x == 196:
            print("у числа 196 нет полиндрома")
            break
        else:
            x = str(x)
            if str(x) == str(x)[::-1]:
                print(f'полиндром найден за {count} раз')
                break
            else:
                reversed_x = str(x)[::-1]
                x = int(x) + int(reversed_x)
                count +=1


polindrom(1967)