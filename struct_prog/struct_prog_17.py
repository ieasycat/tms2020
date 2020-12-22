"""
Дано число. Найти сумму и произведение его цифр.
"""


def calculation(numbers):
    my_summ = 0
    my_mult = 1
    while numbers > 0:
        my_remains = numbers % 10
        if my_remains != 0:
            my_summ += my_remains
            my_mult *= my_remains
        numbers //= 10
    print("Сумма: ", my_summ)
    print("Произведение: ", my_mult)


def main():
    my_number = int(input("A: "))
    calculation(my_number)


if __name__ == '__main__':
    main()
