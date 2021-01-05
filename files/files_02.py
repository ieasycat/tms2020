"""
Создать текстовый файл и записать в него 6 строк.
Записываемые строки вводятся с клавиатуры. [03-15.3]
"""


def write_file():
    with open('files_02', 'w') as my_file:
        for i in range(6):
            line = input('Введите строку: ')
            my_file.write(line + '\n')
    return my_file


def main():
    write_file()
    with open('files_02') as file:
        pr_line = file.readlines()
        print(pr_line)


if __name__ == '__main__':
    main()
