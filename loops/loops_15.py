"""
Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания. После колличество попыток.
В случае правильного ответа - выводить You are the winner.
В случае неправильного давать игроку подсказку
(больше или меньше искомое число). Если за указанное количество попыток
число не угадано - выводить: You are the loser и правильное число.
"""
from random import randint

a = randint(0, 10)
count = 3
for x in range(3):
    number = int(input("Введите число от 0 до 10: "))
    if number == a:
        print("You are the winner")
        break
    elif number > a:
        print("Больше")
    elif number < a:
        print("Меньше")
    count -= 1
    print(f'Осталось {count} попыток')
else:
    print(f'You are the loser, number - {a}')
