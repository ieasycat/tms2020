"""
Дан список чисел. Посчитать сколько раз встречается каждое число.
Использовать функцию.
Подсказка: для хранения данных использовать словарь.
Для проверки нахождения элемента в словаре использовать
метод get(), либо оператор in
"""


def score(numbers):
    dictt = {}
    for number in numbers:
        if number in dictt.keys():
            dictt[number] += 1
        else:
            dictt[number] = 1
    return dictt


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 0]
    pr_score = score(numbers)
    print(pr_score)


if __name__ == '__main__':
    main()
