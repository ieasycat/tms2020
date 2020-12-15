"""

"""

from random import randint

n = int(input("Введите количество раз: "))
m = int(input("Введите количество раз: "))
list_one = []
count = 0
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(1, 9))
    list_one.append(row)
for row in list_one:        # для каждой строки в списке
    for elemnt in row:      # для каждого элемента в строке
        if elemnt == 7:
            count += 1
print(f'{count} кол-во 7-ок в матрице')

for row in list_one:
    for elemnt in row:
        print(elemnt, end=' ')
    print()
