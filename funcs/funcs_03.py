"""
Написать программу для нахождения факториала.
Факториал натурального числа n определяется
как произведение всех натуральных чисел от 1 до n включительно
"""


def my_factorial(numbers):
    fact = 1
    for i in range(1, numbers + 1):
        fact *= i
    return fact


def main():
    my_numbers = int(input("Введите число (кроме 0): "))
    if my_numbers != 0:
        print_fact = my_factorial(my_numbers)
        print(f'Факториал {my_numbers} равен {print_fact}')
    else:
        print("Факториал 0 равен 1")


if __name__ == '__main__':
    main()
