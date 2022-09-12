
#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

a = [1, 2, 3 , 5, 6, 7, 9, 12 ,15]
def pair_multiplier(a):
    pairs = []
    count = 0
    c = 0
    if len(a) % 2 == 0:
        for i in range(int(len(a)/2)):
            count += 1
            b = a[i] * a[-count]
            pairs.append(b)
    else:
        for i in range(int(len(a) // 2)):
            count += 1
            b = a[i] * a[-count]
            pairs.append(b)
        c = a[int(len(a) // 2)] ** 2
        pairs.append(c)
    print(pairs)

pair_multiplier(a)
