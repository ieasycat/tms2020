"""
Создать квадратную матрицу разметностью n
и заполнить ее случайными значениями от
1 до 9.
"""
from random import randint

n = int(input("Введите количество раз: "))
list_one = []
for i in range(n):
    row = []
    for j in range(3):
        row.append(randint(1, 9))
    list_one.append(row)
    print(list_one[i])
