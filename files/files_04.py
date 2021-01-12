"""
Имеется текстовый файл.
Переписать в другой файл все его строки
с заменой в них символа 0 на символ 1 и наоборот. [03-15.28]
"""


def census(old_file, new_file, old_symbol, new_symbol):
    with open(new_file, 'w') as my_file_new:
        with open(old_file) as my_file:
            while True:
                line = my_file.readline()
                result = ''
                for i in line:
                    if i == old_symbol:
                        result += new_symbol
                    elif i == new_symbol:
                        result += old_symbol
                    else:
                        result += i
                my_file_new.writelines(result)
                if not line:
                    break


def main():
    one_files = 'files_04'
    two_files = 'files_new_04'
    one_symbol = input('Введите символ, который хотите заменить: ')
    two_symbol = input('Введите символ, на который хотите заменить: ')
    census(one_files, two_files, one_symbol, two_symbol)
    with open('files_04') as my_file:
        pr_old = my_file.read()
        print(f'Старый текст: \n{pr_old}')
    with open('files_new_04') as my_file:
        pr_new = my_file.read()
        print(f'Новый текст: \n{pr_new}')


if __name__ == '__main__':
    main()
