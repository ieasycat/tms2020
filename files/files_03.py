"""
В конец существующего текстового файла записать три новые строки текста.
Записываемые строки вводятся с клавиатуры. [03-15.6]
"""


def write_file():
    with open('files_03', 'a') as my_file:
        for i in range(3):
            line = input('Введите строку: ')
            my_file.write(line + '\n')


def main():
    write_file()
    with open('files_03') as file:
        pr_line = file.readlines()
        print(pr_line)


if __name__ == '__main__':
    main()
