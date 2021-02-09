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
import argparse
import time
from datetime import datetime
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
    '-T',
    '--task',
    required=True,
)
parser.add_argument(
    '-t',
    '--times',
    default=25,
    type=int,
)
parser.add_argument(
    '-p',
    '--pause',
    default=5,
    type=int,
)
parser.add_argument(
    '-c',
    '--cycle',
    default=4,
    type=int
)
args = parser.parse_args()
times, pause, cycle = args.times, args.pause, args.cycle
print(f'There will be: {cycle} cycles.\n')
for i in range(1, cycle+1):
    print(times, 'minutes to focus.')
    seconds = times * 60
    time.sleep(seconds)
    print('End of focus.\n')

    print(pause, 'minutes for a pause.')
    seconds = pause * 60
    time.sleep(seconds)
    print('End of pause.')

    print(f'\nEnd of {i} cycle.\n')

file_path = os.path.relpath(__file__)
dir_name = os.path.dirname(file_path)
file = os.path.join(dir_name, 'log_scripts_07.txt')
with open(file, 'a') as my_file:
    now = datetime.now()
    my_file.write(f'Date: {now.day}.{now.month}.{now.year}\n'
                  f'Time: {now.hour}:{now.minute}:{now.second}\n'
                  f'First name: {args.first_name}\n'
                  f'Last name: {args.last_name}\n'
                  f'My task: {args.task}\n'
                  f'Time to focus: {args.times}, '
                  f'time to pause: {args.pause}, '
                  f'cycle: {args.cycle}\n\n')

# (python scripts/scripts_07.py -fn Anton -ln Klimenka -T Work -t 5 -p 25 -c 1)
# По умочланию (python scripts/scripts_07.py -fn Anton -ln Klimenka -T Work)
