"""
Имеется текстовый файл.
Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
[03-15.16]
"""


def print_txt(text):
    pass


def main():
    my_file = open('files_01')
    print(my_file.readline(), end='')
    my_file.close()

    my_file = open('files_01')
    i = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        if i == 5:
            print(line)
            break
        i += 1
    my_file.close()

    my_file = open('files_01')
    i = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        if i < 5:
            print(line, end='')
            i += 1
    my_file.close()

    my_file = open('files_01')
    one_number = int(input('Введите 1-ое число: '))
    two_number = int(input('Введите 2-ое число: '))
    i = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        if one_number <= i <= two_number:
            print(line, end='')
        i += 1
    my_file.close()

    my_file = open('files_01')
    while line := my_file.readline():
        print(line, end='')
    my_file.close()


if __name__ == '__main__':
    main()
