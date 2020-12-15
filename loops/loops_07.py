"""
Получить сумму кубов натуральных чисел от n до m используя цикл for
"""

n = int(input("Введите 1-ое число: "))
m = int(input("Введите 2-ое число: "))
summ = 0
not n < m and not m > n
for i in range(n, m + 1):
    summ += i ** 3
print(summ)
