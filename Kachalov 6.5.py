
#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

a = [1, 2, 3 , 5, 6, 7, 9, 12 ,15]

def multiplier(numbers_list):
    length = len(numbers_list)//2 + 1 if len(numbers_list) % 2 != 0 else len(numbers_list)//2
    mulitplied_list = [numbers_list[i]*numbers_list[len(numbers_list)-i-1] for i in range(length)]
    print(mulitplied_list)

multiplier(a)