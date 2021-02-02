"""
Создать скрипт, который принимает имя фамилию и возраст и дописывает их в файл.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-fn',
    '--first-name',
    required=True,
)
parser.add_argument(
    '-ln',
    '--last-name',
    required=True,
)
parser.add_argument(
    '-ag',
    '--age',
    required=True,
)
args = parser.parse_args()
with open('scripts/scripts_02.txt', 'a') as my_file:
    my_file.write(f'First name: {args.first_name}'
                  f'\nLast name: {args.last_name}'
                  f'\nAge: {args.age}')

# Вызов(python scripts/scripts_02.py -fn Anton -ln Klimenka -ag 28)
