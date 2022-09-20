
#Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
#Сдвиг часто называют ключом шифрования.
#Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

def coder(word):
    letter_drift = 2
    coded = ""
    for i,code in enumerate(word):
        coded += chr(ord(code)+letter_drift)
    print(coded)
    with open(r"secret.txt", "w") as file:
            file.write(coded)

coder("secret")

def decoder():
    decode_drift = int(input("введите ключ (целое число): "))
    decoded = ""
    with open(r"secret.txt", "r") as file:
        for line in file:
            secret_word = line
    for i,code in enumerate(secret_word):
        decoded += chr(ord(code)-decode_drift)
    print(decoded)

decoder()
