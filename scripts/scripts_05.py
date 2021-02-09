"""
Создать скрипт.
Программа принимает имя папки и имя файла с расширением.
Создает папку и создает в ней файл.
Если расширение файла py - записывает в файл следующее:
def main():
    pass


if __name__ == '__main__':
    main()
"""
import os
import sys

file_path = os.path.relpath(__file__)
dir_name = os.path.dirname(file_path)
os.mkdir(f'{dir_name}/{sys.argv[1]}')

fn = os.path.join(dir_name, sys.argv[1], sys.argv[2])
with open(fn, 'w') as my_file:
    if 'py' in sys.argv[2]:
        data = 'def main():', '\n    pass', \
               "\n\n\nif __name__ == '__main__':", '\n    main()\n'
        for row in data:
            my_file.write(row)

# Вызов (python scripts/scripts_05.py my_test_scripts test.py)
