"""
В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы. [02-7.2-HL08]
"""


def change(word):
    strings_list = word.split()
    strings_list = strings_list[::-1]
    new_word = ' '.join(strings_list)
    return new_word


def main():
    strings = input('Введите строку: ')
    print(f'Ваша строка: {strings}')
    if len(strings) > 0:
        x = change(strings)
        print(f"Обратная строка: {x}")


if __name__ == '__main__':
    main()
