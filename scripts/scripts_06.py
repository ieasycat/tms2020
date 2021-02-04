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
)
parser.add_argument(
    '-m',
    '--minutes',
    required=True,
)
parser.add_argument(
    '-s',
    '--seconds',
    required=True,
)
args = parser.parse_args()
seconds = int(args.hours) * 3600 + int(args.minutes) * 60 + int(args.seconds)
while seconds >= 0:
    hours = seconds // 3600
    minutes = seconds // 60 % 60
    second = seconds % 60
    print(f'{hours}:{minutes}:{second}')
    seconds -= 1

with open('/home/tms/PycharmProjects/tms2020/'
          'scripts/log_scripts_06.txt', 'a') as my_file:
    now = datetime.now()
    my_file.write(f'Date: {now.day}.{now.month}.{now.year}\n'
                  f'Time: {now.hour}:{now.minute}:{now.second}\n'
                  f'First name: {args.first_name}\n'
                  f'Last name: {args.last_name}\n'
                  f'Hours: {args.hours}\n'
                  f'Minutes: {args.minutes}\n'
                  f'Seconds: {args.seconds}\n\n')

# Вызов (python scripts/scripts_06.py -fn Anton -ln Klimenka -H 0 -m 0 -s 59)
