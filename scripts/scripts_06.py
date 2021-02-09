"""
Написать скрипт - таймер.
Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
После программа начинает обратный отсчет выводя оставшееся время.
Программа должна хранить файл логирования
с информацией о том кто запускал программу и когда.
Пример:
00:00:03
00:00:02
00:00:01
ALARM!!!
"""

import argparse
from datetime import datetime
import time
import os

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
    '-H',
    '--hours',
    required=True,
    type=int,
)
parser.add_argument(
    '-m',
    '--minutes',
    required=True,
    type=int,
)
parser.add_argument(
    '-s',
    '--seconds',
    required=True,
    type=int,
)
args = parser.parse_args()
seconds = args.hours * 3600 + args.minutes * 60 + args.seconds
while seconds >= 0:
    hours = seconds // 3600
    minutes = seconds // 60 % 60
    second = seconds % 60
    print(f'{hours}:{minutes}:{second}')
    seconds -= 1
    time.sleep(1)
print("It's Finish!")

file_path = os.path.relpath(__file__)
dir_name = os.path.dirname(file_path)
file = os.path.join(dir_name, 'log_scripts_06.txt')
with open(file, 'a') as my_file:
    now = datetime.now()
    my_file.write(f'Date: {now.day}.{now.month}.{now.year}\n'
                  f'Time: {now.hour}:{now.minute}:{now.second}\n'
                  f'First name: {args.first_name}\n'
                  f'Last name: {args.last_name}\n'
                  f'Hours: {args.hours}\n'
                  f'Minutes: {args.minutes}\n'
                  f'Seconds: {args.seconds}\n\n')

# Вызов (python scripts/scripts_06.py -fn Anton -ln Klimenka -H 0 -m 0 -s 59)
