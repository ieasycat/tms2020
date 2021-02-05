"""
Написать скрипт - таймер.
Создать программу Pomodoro.
На вход программа получает имя, фамилию,
время для фокусировки(по-умолчанию 25 минут),
длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи.
Программа указывает оставшееся время фокусировки,
после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки.
Программа должна вести файл лога о всех запусках.
"""
import sys
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
    '-t',
    '--time',
)
parser.add_argument(
    '-p',
    '--pause',
)
parser.add_argument(
    '-c',
    '--cycle',
)
args = parser.parse_args()
if len(sys.argv) == 5:
    time, pause, cycle = args.time, args.pause, args.cycle = 25, 5, 4
else:
    time, pause, cycle = int(args.time), int(args.pause), int(args.cycle)
print(f'There will be: {cycle} cycles.\n')
for i in range(1, cycle+1):
    print(time, 'minutes to focus.')
    seconds = time * 60
    while seconds >= 0:
        seconds -= 1
    print('End of focus.\n')

    print(pause, 'minutes for a pause.')
    seconds = pause * 60
    while seconds >= 0:
        seconds -= 1
    print('End of pause.')

    print(f'\nEnd of {i} cycle.\n')

with open('/home/tms/PycharmProjects/tms2020/'
          'scripts/log_scripts_07.txt', 'a') as my_file:
    now = datetime.now()
    my_file.write(f'Date: {now.day}.{now.month}.{now.year}\n'
                  f'Time: {now.hour}:{now.minute}:{now.second}\n'
                  f'First name: {args.first_name}\n'
                  f'Last name: {args.last_name}\n'
                  f'Time to focus: {args.time}, '
                  f'time to pause: {args.pause}, '
                  f'cycle: {args.cycle}\n\n')

# Вызов (python scripts/scripts_07.py -fn Anton -ln Klimenka -t 5 -p 25 -c 1)
# Вызов по умочланию (python scripts/scripts_07.py -fn Anton -ln Klimenka)
