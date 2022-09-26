
#Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.


sequence = lambda x: print(list(map(lambda x: (-3)**x, [i for i in range(x)])))
sequence(6)