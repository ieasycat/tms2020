"""
Дан словарь, создать новый словарь, поменяв местам ключ и значение
"""


def main():
    one_dictt = {'one': 1, 'two': 2, 'three': 3}
    two_dict = {value: key for key, value in one_dictt.items()}
    print(two_dict)


if __name__ == '__main__':
    main()
