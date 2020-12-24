"""
Описать функцию is_power_n( k , n ) логического типа, возвращающую
True, если целый параметр k (> 0) является степенью числа n (> 1), и False
в противном случае.
Дано число n (> 1) и набор из 10 целых положитель-
ных чисел. С помощью функции is_power_n найти количество степеней чис-
ла N в данном наборе.
[01-11.2-Proc27]
"""


def is_power_n(k, n):
    while True:
        k /= n
        if k == 1:
            return True
        elif k < 1:
            return False


def main():
    one_number = int(input("Введите 1-ое число: "))
    two_number = int(input("Введите 2-ое число: "))
    pr_power = is_power_n(one_number, two_number)
    print(f'Это первое решение - {pr_power}')
    test = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    for my_number in range(len(test)):
        if is_power_n(64, test[my_number]) is True:
            count += 1
    print(f'А это вторая чать задачки - {count}')


if __name__ == '__main__':
    main()
