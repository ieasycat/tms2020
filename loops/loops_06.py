"""
Написать программу,
которая будет выводить на экран случайные числа от 1 до 10 до тех пор,
пока не выпадет 7.
"""
from random import randint

while True:
    i = randint(1, 10)
    if i == 7:
        break
    print(i)
print("This's End")
