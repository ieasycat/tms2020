"""
Создать скрипт, который принимает имя папки и создает ее рядом со скриптом.
"""

import os
import sys

file_path = os.path.relpath(__file__)
dir_name = os.path.dirname(file_path)
os.mkdir(f'{dir_name}/{sys.argv[1]}')

# Вводим(python scripts/scripts_03.py my_test_scripts)
