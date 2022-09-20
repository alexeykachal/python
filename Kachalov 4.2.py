
#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.

numbers_list = [1,1,1,1,2,2,2,3,3,3,4,5,7,9,9,9,9,9]
unique_list = []

for i in numbers_list:
    for j in numbers_list:
        if i != j and i not in unique_list:
            unique_list.append(i)

print(unique_list)
