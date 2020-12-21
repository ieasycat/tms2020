"""
Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания. После колличество попыток.
В случае правильного ответа - выводить You are the winner.
В случае неправильного давать игроку подсказку
(больше или меньше искомое число). Если за указанное количество попыток
число не угадано - выводить: You are the loser и правильное число.
"""
from random import randint


def game_number(numb, attempt):
    a = randint(numb[0], numb[1])
    for x in range(attempt):
        number = int(input(f"Введите число от {numb[0]} до {numb[1]}: "))
        if number == a:
            print("You are the winner")
            break
        elif number > a:
            print("Больше")
        elif number < a:
            print("Меньше")
        attempt -= 1
        print(f'Осталось {attempt} попыток')
    else:
        print(f'You are the loser, number - {a}')


def main():
    print("Введите ниже диапазон угадывания.")
    one_number = int(input("Введите 1-ое число: "))
    two_number = int(input("Введите 2-ое число: "))
    numbers = [one_number, two_number]
    count = int(input("Введите количество попыток угадывания: "))
    game_number(numbers, count)


if __name__ == '__main__':
    main()
