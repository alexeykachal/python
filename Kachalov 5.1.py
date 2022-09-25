
#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"

text = "привет, пишу абвразную абвштуку текст - это хорабвшее хорошее упражнение"

def text_cleaner(text):

    '''
    удаляет слова с буквами "абв" подряд
    '''

    list_clean = []

    for i in list(text.split()):
        if "абв" not in i:
            list_clean.append(i)

    print(" ".join(list_clean))

text_cleaner(text)
