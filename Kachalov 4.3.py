
#В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».

#Сперва запишем ФИ и оценку в файл для демонстрации.

text_file = open("test.txt", "w")
lines = ["Волков Андрей 5", "Фредди Меркури 3", "Денис Байцуров 4", "Федя Крюгер 5", "Жаред Летов 3"]

with open(r"test.txt", "w") as file:
    for line in lines:
        file.write(line + '\n')

#Достаем строки из файла

parced_lines = []
parced_lines_amended = []

with open("test.txt", "r") as file:
    for line in file:
        string = line.rsplit(' ',maxsplit=1)
        parced_lines.append(string)


for i in parced_lines:
    if i[1] == "5\n":
        i[0] = i[0].upper()


for i in parced_lines:
    i_str = ' '.join(i)
    parced_lines_amended.append(i_str)

with open(r"test.txt", "w") as file:
    for line in parced_lines_amended:
        file.write(line)
