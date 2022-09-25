
#3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
#['python', 'c#']
#[1,2]
#Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
#[(1,'PYTHON'), (2,'C#')]

#Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
#[сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
#[(1,'PYTHON'), (102,'C#')]
#Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.

#Задача первая

lang_list = ['python', 'java', 'c#', 'c++', 'sql']

def upper(x):

    """
    Делаем все элементы списка капсом и нумеруем их
    """
    upper_list = [i.upper() for i in lang_list]
    tuples = list(enumerate(upper_list, start = 1))
    print(tuples)

upper(lang_list)

#Задача вторая
def filter(x):

    """
    Делаем все элементы списка капсом и нумеруем их
    """
    upper_list = [i.upper() for i in lang_list]
    tuples = list(enumerate(upper_list, start = 1))

    list1 = [] #соберем очки

    for i in upper_list:
        sum_chr = 0
        for j in i:
            sum_chr += ord(j)
        list1.append(sum_chr)

    list2 = [] #соберем номера "языков"
    list3 = []

    for i in tuples:
        list2.append(i[0])

    tuples_modified = []

    list3 = [i/j for i,j in zip(list1,list2)]

    for i in list3:
        if i % 1 == 0:
            tuples_modified.append(tuples[list3.index(i)])
        else:
            unmoded = (list1[list3.index(i)], upper_list[list3.index(i)])
            tuples_modified.append(unmoded)

    print(tuples_modified)

filter(lang_list)



