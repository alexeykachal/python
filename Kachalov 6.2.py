
#Найти сумму чисел списка стоящих на нечетной позиции

number_list = [1,2,4,5,6,7,8,9,10,19,18,17,16]
list_sum = lambda number_list: print(sum([number_list[i] for i in range(len(number_list)) if i % 2 !=0]))
list_sum(number_list)

