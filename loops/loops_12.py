"""
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы,
превосходящих среднее арифметическое значение элементов матрицы
и сумма индексов которых четна.[02-4.2-BL23]
"""
from random import randint

n = int(input("Введите количество раз: "))
m = int(input("Введите количество раз: "))
list_one = []
list_two = []
count = 0
numbers = 0
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(1, 9))
    list_one.append(row)
    list_two += list_one[i]
a = (min(list_two) + max(list_two)) / 2
print(list_two)
for v in range(len(list_two)):
    for z in range(len(list_two)):
        if v + z % 2 == 0:
            numbers += list_two[v]
    print(numbers)
# print(list_two)
"""for x in list_two:
    if x > a:
        count += 1
print(count)"""
