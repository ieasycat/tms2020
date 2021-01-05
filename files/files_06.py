"""
Имеются два текстовых файла с одинаковым числом строк.
Выяснить, совпадают ли их строки. Если нет,
то получить номер первой строки, в которой эти файлы отличаются друг от друга.
[03-15.31]
"""


def coincidence(one_text, two_text):
    with open(one_text) as one_files:
        with open(two_text) as two_files:
            i = 1
            while True:
                a = one_files.readline()
                b = two_files.readline()
                if not a and not b:
                    break
                if a != b:
                    return i
                else:
                    i += 1
                    continue
    return False


def main():
    one_files = 'files_04'
    two_files = 'files_new_04'
    result = coincidence(one_files, two_files)
    if not result:
        print('Данные текстовые файлы - одинаковы.')
    else:
        print(f'{result} неравная строчка.')


if __name__ == '__main__':
    main()
