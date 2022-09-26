
#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1

list = ["qwe", "asd", "zxc", "qwe", "ertqe"]
x = "qwe"

def checker (x, list):
    cheked_list = [list.index(x) for i in list if i == x]
    list.remove(x)
    return int(list.index(x)) + 1 if len(cheked_list) > 1 else -1

check = checker (x, list)
print(check)

