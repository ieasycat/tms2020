"""
Создать функцию, которая принимает на вход
неопределенное количество аргументов и возвращает их сумму и
максимальное из них.
"""


def sum_and_max(*args):
    summ = 0
    max_elem = 0
    for arg in args:
        summ += arg
    for elem in args:
        if elem > max_elem:
            max_elem = elem
    return summ, max_elem


def main():
    pr_summ, pr_max = sum_and_max(3, 4, 8, 10, 3, 5)
    print(f'Это сумма чисел - {pr_summ}')
    print(f'А это максимальный элемент {pr_max}')


if __name__ == '__main__':
    main()
