
#Определить, присутствует ли в заданном списке строк некоторое число

mylist = ['7', 'abs2c', '2', '4', 'ter']
x= str(7)

finder = lambda x, list: print("Число находится в списке") if str(x) in list else print("Число находится не в списке")
finder(x,mylist)