"""
Создать скрипт. Программа принимает имя папки и имя файла.
Создает папку и создает в ней файл.
"""

import os
import sys

file_path = os.path.relpath(__file__)
dir_name = os.path.dirname(file_path)
os.mkdir(f'{dir_name}/{sys.argv[1]}')

fn = f'{dir_name}/{sys.argv[1]}/{sys.argv[2]}'
with open(fn, 'w') as my_file:
    pass
