
#Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
#Предусмотрите последний ход, ибо там конфет остается меньше.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

from random import randint

#Важно - если хотите сыграть против бота, введите имя второго игрока (player2) "bot"
#Candy amount - стартовое количество конфет. За раз можно брать не более 28 штук!

candy_amount = 45
player1 = input("Введите имя игрока номер один: ")
player2 = input("Введите имя игрока номер два : ")
lot = randint(1,2)

if lot == 1:
    print(f"Первый ход за первым игроком - {player1}")
else:
    print(f"Первый ход за вторым игроком - {player2}")

switch = 0

if player2 == "bot":
    print("Вы играете с ботом")
    while candy_amount > 28:
        if lot == 1:
            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
            if 0 < taken <= 28:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break
            else:
                while taken < 1 or taken > 28:
                    print('Введите коректное количество конфет')
                    taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break


            taken = int(randint(1,min(candy_amount,28)))
            candy_amount = candy_amount - taken
            if candy_amount == 1:
                print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                break
            if 1 < candy_amount <= 28:
                print(f'Уже понятно кто победил, после хода игрока два {player2}, но дойдем до условия')
                switch = 1
                break


        else:
            taken = int(randint(1,min(candy_amount,28)))
            if 0 < taken <= 28:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока два {player2}, но дойдем до условия')
                    switch = 1
                    break
            else:
                print("Введите число согласно условиям")

            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
            if 0 < taken <= 28:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break
            else:
                while taken < 1 or taken > 28:
                    print('Введите коректное количество конфет')
                    taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break


    while candy_amount > 1 and candy_amount <=28:
        if switch == 2:
            taken = candy_amount-1
            if 0 < taken <= candy_amount:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
            else:
                print("Введите число согласно условиям")
            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до {candy_amount-1}: "))

            while taken < 1 or taken > candy_amount-1:
                print('Введите коректное количество конфет')
                taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
            candy_amount = candy_amount - taken
            print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
            if candy_amount == 1:
                print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                break

        if switch == 1:
            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до {candy_amount-1}: "))
            if 0 < taken <= candy_amount:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
            else:
                while taken < 1 or taken > candy_amount:
                    print('Введите коректное количество конфет')
                    taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до {candy_amount-1}: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
            taken = candy_amount-1
            if 0 < taken <= candy_amount-1:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break


else:
    while candy_amount > 28:
        if lot == 1:
            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
            if 0 < taken <= 28:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break
            else:
                while taken < 1 or taken > 28:
                    print('Введите коректное количество конфет')
                    taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break


            taken = int(input(f"Ход Второго игрока {player2}. Введите положительное число от 1 до 28: "))
            if 0 < taken <= 28:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока два {player2}, но дойдем до условия')
                    switch = 1
                    break
            else:
                while taken < 1 or taken > 28:
                    print('Введите коректное количество конфет')
                    taken = int(input(f"Ход второго игрока {player2}. Введите положительное число от 1 до 28: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока два {player2}, но дойдем до условия')
                    switch = 1
                    break

        else:
            taken = int(input(f"Ход Второго игрока {player2}. Введите положительное число от 1 до 28: "))
            if 0 < taken <= 28:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока два {player2}, но дойдем до условия')
                    switch = 1
                    break
            else:
                while taken < 1 or taken > 28:
                    print('Введите коректное количество конфет')
                    taken = int(input(f"Ход второго игрока игрока {player2}. Введите положительное число от 1 до 28: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока два {player2}, но дойдем до условия')
                    switch = 1
                    break

            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
            if 0 < taken <= 28:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break
            else:
                while taken < 1 or taken > 28:
                    print('Введите коректное количество конфет')
                    taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до 28: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
                if 1 < candy_amount <= 28:
                    print(f'Уже понятно кто победил, после хода игрока один {player1}, но дойдем до условия')
                    switch = 2
                    break

    while candy_amount > 1 and candy_amount <=28:

        if switch == 2:
            taken = int(input(f"Ход второго игрока {player2}. Введите положительное число от 1 до {candy_amount-1}: "))
            if 0 < taken <= candy_amount-1:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
            else:
                while taken < 1 or taken > candy_amount-1:
                    print('Введите коректное количество конфет')
                    taken = int(input(
                        f"Ход второго игрока {player2}. Введите положительное число от 1 до {candy_amount - 1}: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до {candy_amount-1}: "))
            if 0 < taken <= candy_amount-1:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
            else:
                while taken < 1 or taken > candy_amount-1:
                    print('Введите коректное количество конфет')
                    taken = int(input(
                        f"Ход первого игрока {player1}. Введите положительное число от 1 до {candy_amount - 1}: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break

        if switch == 1:
            taken = int(input(f"Ход первого игрока {player1}. Введите положительное число от 1 до {candy_amount-1}: "))
            if 0 < taken <= candy_amount-1:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break
            else:
                while taken < 1 or taken > candy_amount-1:
                    print('Введите коректное количество конфет')
                    taken = int(input(
                        f"Ход первого игрока {player1}. Введите положительное число от 1 до {candy_amount - 1}: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Первый игрок {player1} победил, последняя конфета достается игроку {player2}")
                    break


            taken = int(input(f"Ход второго игрока {player2}. Введите положительное число от 1 до {candy_amount-1}: "))
            if 0 < taken <= candy_amount-1:
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
            else:
                while taken < 1 or taken > candy_amount-1:
                    print('Введите коректное количество конфет')
                    taken = int(input(
                        f"Ход второго игрока {player2}. Введите положительное число от 1 до {candy_amount - 1}: "))
                candy_amount = candy_amount - taken
                print(f'Игрок взял {taken} конфет, после хода на столе осталось {candy_amount} конфет')
                if candy_amount == 1:
                    print(f"Второй игрок {player2} победил, последняя конфета достается игроку {player1}")
                    break
