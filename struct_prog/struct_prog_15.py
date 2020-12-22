"""
Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность,
в которой первые два числа равны либо 1 и 1,
а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
предоставить 2 решения. Одно с использованием цикла while,
другое с использованием цикла for с параметром.
Оба решения предоставить в одном файле.
"""


def my_for(numbers):
    listt = [numbers, numbers]
    for i in range(1, 14):
        listt.append(listt[i - 1] + listt[i])
    return listt


def my_while(numbers):
    replays = 13
    listt = [numbers, numbers]
    while replays > 0:
        listt.append(listt[numbers-1] + listt[numbers])
        numbers += 1
        replays -= 1
    return listt


def main():
    my_numbers = int(input("Введите число: "))
    print_for = my_for(my_numbers)
    print_while = my_while(my_numbers)
    print(f'Это метод for - {print_for}')
    print(f'Это метод while - {print_while}')


if __name__ == '__main__':
    main()
