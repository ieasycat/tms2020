"""
Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
"""


def division(m, n):
    for numbers in range(m, n + 1):
        tmp = []
        for divider in range(2, numbers - 1):
            if numbers % divider == 0:
                tmp.append(divider)
        if len(tmp) > 0:
            print(f'{numbers}: {tmp}')
        else:
            print(f'{numbers} - нет делителей')


def main():
    one_number = int(input("Введите 1-ое число: "))
    two_number = int(input("Введите 2-ое число: "))
    division(one_number, two_number)


if __name__ == '__main__':
    main()
