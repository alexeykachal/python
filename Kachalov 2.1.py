
#Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр. Учтите, что числа могут быть отрицательными

float_num = input("Введите вещественное число: ")
sum = 0
for i in float_num:
    if i == "-":
        i = 0
    if i != '.':
        sum += int(i)
print(sum)
