"""
Имеется текстовый файл.
Все четные строки этого файла записать во второй файл,
а нечетные — в третий файл. Порядок следования строк сохраняется. [03-15.29]
"""


def parity(original):
    with open('files_even_05', 'w') as even_files:
        with open('files_odd_05', 'w') as odd_files:
            with open(original) as my_files:
                i = 1
                while True:
                    line = my_files.readline()
                    if not line:
                        break
                    if i % 2 == 0:
                        even_files.writelines(line)
                    else:
                        odd_files.writelines(line)
                    i += 1


def main():
    file = 'files_04'
    parity(file)
    with open('files_04') as my_file:
        line = my_file.read()
        print(line)
    with open('files_even_05') as my_file:
        line = my_file.read()
        print(f'Это четные строки: \n{line}')
    with open('files_odd_05') as my_file:
        line = my_file.read()
        print(f'Это нечетные строки: \n{line}')


if __name__ == '__main__':
    main()
