"""
Создать функцию, принимающая на вход неопределенное количество
аргументом и возвращающая сумму args[i] * i
Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10

"""


def my_summ(*args):
    summ = 0
    for elem in range(len(args)):
        summ += args[elem] * elem
    return summ


def main():
    print_summ = my_summ(2, 4, 6, 9, 7, 3)
    print(print_summ)


if __name__ == '__main__':
    main()
