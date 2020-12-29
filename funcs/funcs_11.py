"""
Написать функцию по решению квадратных уравнений.[01-11.2-Proc17]
"""


def quadratic_equation(a, b, c):
    if b != 0 and c != 0:
        discriminant = b ** 2 - (4 * a * c)
        if discriminant < 0:
            print('Решений нет.')
        elif discriminant == 0:
            x1 = -b / (2 * a)
            print(f'Корень уравнения равны: {x1}')
        elif discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            print(f'Корни уравнения равны: {x1} и {x2}')
    elif b == 0:
        if (-c / a) >= 0:
            x1 = - (-(c / a)) ** 0.5
            x2 = (-(c / a)) ** 0.5
            print(f'Корни уравнения равны: {x1} и {x2}')
        else:
            print('Решений нет.')
    elif c == 0:
        x1 = 0
        x2 = -(b / a)
        print(f'Корни уравнения равны: {x1} и {x2}')


def main():
    one_number = int(input("Введите 'a': "))
    if one_number != 0:
        two_number = int(input("Введите 'b': "))
        tree_number = int(input("Введите 'c': "))
        quadratic_equation(one_number, two_number, tree_number)
    else:
        print("'a' не может быть равно '0''.")


if __name__ == '__main__':
    main()
