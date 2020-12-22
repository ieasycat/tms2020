"""
Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]
"""


def my_summ(x):
    summ = 0
    for i in range(1, x + 1):
        summ += 1/i
    return summ


def main():
    my_number = int(input("Введите число: "))
    print_summ = my_summ(my_number)
    print(f'Сумма числа {my_number} - {print_summ}')


if __name__ == '__main__':
    main()
