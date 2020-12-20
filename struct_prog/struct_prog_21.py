"""
Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего). [02-4.1-ML27]
"""


def my_print(x):
    count = 0
    result = 0
    for i in range(len(x)-2):
        if x[i + 2] > x[i + 1] > x[i]:
            count += 1
        elif count >= 1 and x[i + 1] > x[i + 2]:
            result += 1
            count = 0
    if x[-1] > x[-2] > x[-3]:
        result += 1
    return result


def main():
    array = [27, 17, 18, 19, 20, 1, 24, 25]
    print_array = my_print(array)
    print(f'Массиив: {array}')
    print(f'Количество возрастанний: {print_array}')


if __name__ == '__main__':
    main()
